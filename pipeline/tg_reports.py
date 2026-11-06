"""Telegram-бот @kudapoiti_deti_bot: приём сообщений об ошибках из приложения.
Работает внутри GitHub Action reports.yml почти непрерывно (каждый запуск ~5,8 часа, новый — каждые 6 часов),
поэтому отвечает людям сразу (long polling), а не раз в 5 минут.
- Приложение открывает t.me/<бот>?start=e_<id места>; бот здоровается и объясняет, что делать.
- Сообщения → auto/reports.json (status new) — коммит сразу после каждого нового сообщения.
- Раз в минуту git pull: решения робота-исправителя из auto/report-answers.json → ответ человеку.
Нужен секрет репозитория TELEGRAM_BOT_TOKEN. Запуск: python3 pipeline/tg_reports.py [--minutes 345]"""
import json, os, subprocess, sys, time, urllib.parse, urllib.request

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    print("нет секрета TELEGRAM_BOT_TOKEN — бот ещё не подключён"); sys.exit(0)
API = f"https://api.telegram.org/bot{TOKEN}/"
REP, STATE, ANS = "auto/reports.json", "auto/reports-state.json", "auto/report-answers.json"
MINUTES = int(sys.argv[sys.argv.index("--minutes") + 1]) if "--minutes" in sys.argv else 0

HELLO = ("👋 Здравствуйте! Это помощник приложения «Куда пойти с детьми».\n\n"
         "Сюда пишут, если в приложении что-то неточно: неверные часы, адрес, цена, место закрылось или "
         "переехало, нет детской комнаты и т.п.\n\n")
ASK_PLACE = HELLO + "✍️ Напишите одним сообщением: какое место и что не так. Можно приложить фото."
DONE = "Спасибо! 🙌 Сообщение получено. Мы проверим и исправим — обычно в течение часа — и напишем сюда, что сделали."


def call(method, http_timeout=30, **params):
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(API + method, data=data, timeout=http_timeout) as r:
        return json.load(r)["result"]


def say(chat, text):
    try: call("sendMessage", chat_id=chat, text=text)
    except Exception as e: print("send:", e)


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True)


def load():
    places = {p["id"]: p["name"] for p in json.load(open("places.json"))["places"]}
    reports = json.load(open(REP)) if os.path.exists(REP) else []
    state = json.load(open(STATE)) if os.path.exists(STATE) else {"offset": 0, "chats": {}}
    return places, reports, state


def save(reports, state, msg):
    json.dump(reports, open(REP, "w"), ensure_ascii=False, indent=1)
    json.dump(state, open(STATE, "w"), ensure_ascii=False, indent=1)
    git("add", REP, STATE)
    if git("diff", "--cached", "--quiet").returncode == 0: return
    git("commit", "-q", "-m", msg)
    for _ in range(5):
        if git("pull", "-q", "--rebase", "-X", "theirs", "origin", "main").returncode == 0 and \
                git("push", "-q").returncode == 0: return
        time.sleep(5)


def handle(u, places, reports, state):
    m = u.get("message") or {}
    chat = str(m.get("chat", {}).get("id")); text = (m.get("text") or m.get("caption") or "").strip()
    if not chat or chat == "None": return False
    if text.startswith("/start"):
        arg = text[6:].strip()
        pid = arg[2:] if arg.startswith("e_") else None
        state["chats"][chat] = pid if pid in places else None
        if pid in places:
            say(chat, HELLO + f"📍 Вы сообщаете о месте: «{places[pid]}».\n\n"
                      "✍️ Напишите одним сообщением, что не так. Можно приложить фото.")
        else:
            say(chat, ASK_PLACE)
        return False
    photo = (m.get("photo") or [{}])[-1].get("file_id")
    pid = state["chats"].get(chat)
    reports.append({"id": str(u["update_id"]), "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(m.get("date", 0))),
                    "chat": chat, "place_id": pid, "place": places.get(pid), "text": text, "photo": photo,
                    "status": "new"})
    say(chat, DONE)
    return True


def answers(reports):
    a = json.load(open(ANS)) if os.path.exists(ANS) else {}
    changed = False
    for r in reports:
        x = a.get(r["id"])
        if x and r["status"] == "new":
            r["status"], r["answer"] = x.get("status"), x.get("answer"); changed = True
        if r.get("status") in ("fixed", "rejected") and not r.get("notified"):
            head = "✅ Исправили, спасибо! " if r["status"] == "fixed" else "🔎 Проверили. "
            say(r["chat"], head + (r.get("answer") or "")); r["notified"] = True; changed = True
    return changed


def setup():
    # описание бота видно ещё до нажатия «Запустить»
    try:
        call("setMyDescription", description=
             "Помощник приложения «Куда пойти с детьми» (Москва и Подмосковье).\n\n"
             "Нашли неточность — неверные часы, адрес, цена, место закрылось? Нажмите «Запустить» и напишите, "
             "что не так. Мы проверим и исправим, обычно в течение часа.")
        call("setMyShortDescription", short_description="Сообщить о неточности в приложении «Куда пойти с детьми»")
    except Exception as e:
        print("описание:", e)


def main():
    setup()
    deadline = time.time() + MINUTES * 60
    places, reports, state = load()
    last_pull = 0
    while True:
        try:
            ups = call("getUpdates", http_timeout=70, offset=state["offset"], timeout=50 if MINUTES else 0,
                       allowed_updates='["message"]')
        except Exception as e:
            print("getUpdates:", e); time.sleep(5); ups = []
        new = False
        for u in ups:
            state["offset"] = u["update_id"] + 1
            new |= handle(u, places, reports, state)
        if ups:
            save(reports, state, "Сообщения об ошибках")
        if time.time() - last_pull > 60 or not MINUTES:
            git("pull", "-q", "--rebase", "-X", "theirs", "origin", "main")
            # своё состояние (reports/state) держим в памяти — оно новее; после pull свежие только места и ответы робота
            places = load()[0]
            if answers(reports):
                save(reports, state, "Ответы на сообщения об ошибках")
            last_pull = time.time()
        if not MINUTES or time.time() > deadline:
            break
    print("новых:", sum(1 for r in reports if r["status"] == "new"))


main()
