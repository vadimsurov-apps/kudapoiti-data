"""Сообщения об ошибках из приложения → Telegram-бот → auto/reports.json (каждые 5 минут, GitHub Action reports.yml).
Приложение открывает t.me/<бот>?start=e_<id места>. Бот отвечает, просит описать ошибку, складывает сообщения
в auto/reports.json со статусом new. Робот-исправитель (каждый час) проверяет и пишет решение в auto/report-answers.json —
этот же скрипт отправляет человеку ответ и ставит notified.
Нужен секрет репозитория TELEGRAM_BOT_TOKEN."""
import json, os, sys, time, urllib.parse, urllib.request

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN: sys.exit("нет TELEGRAM_BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}/"
REP, STATE = "auto/reports.json", "auto/reports-state.json"


def call(method, **params):
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(API + method, data=data, timeout=30) as r:
        return json.load(r)["result"]


def say(chat, text):
    try: call("sendMessage", chat_id=chat, text=text)
    except Exception as e: print("send:", e)


places = {p["id"]: p["name"] for p in json.load(open("places.json"))["places"]}
reports = json.load(open(REP)) if os.path.exists(REP) else []
state = json.load(open(STATE)) if os.path.exists(STATE) else {"offset": 0, "chats": {}}

for u in call("getUpdates", offset=state["offset"], timeout=0, allowed_updates='["message"]'):
    state["offset"] = u["update_id"] + 1
    m = u.get("message") or {}
    chat = str(m.get("chat", {}).get("id")); text = (m.get("text") or m.get("caption") or "").strip()
    if not chat or chat == "None": continue
    if text.startswith("/start"):
        arg = text[6:].strip()
        pid = arg[2:] if arg.startswith("e_") else None
        state["chats"][chat] = pid
        if pid and pid in places:
            say(chat, f"Вы сообщаете о неточности: «{places[pid]}».\nНапишите одним сообщением, что не так "
                      "(часы, адрес, цена, место закрылось…). Можно приложить фото.")
        else:
            say(chat, "Здравствуйте! Это бот приложения «Куда пойти с детьми». Напишите, что не так и про какое место.")
        continue
    photo = (m.get("photo") or [{}])[-1].get("file_id")
    pid = state["chats"].get(chat)
    reports.append({"id": f'{u["update_id"]}', "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(m.get("date", 0))),
                    "chat": chat, "place_id": pid, "place": places.get(pid), "text": text, "photo": photo,
                    "status": "new"})
    say(chat, "Спасибо! Проверим и исправим — обычно в течение часа. Напишем сюда, что сделали.")

# ответы после проверки: робот-исправитель пишет решения в auto/report-answers.json {id: {status, answer}}
# (у каждого файла один писатель — без конфликтов)
answers = json.load(open("auto/report-answers.json")) if os.path.exists("auto/report-answers.json") else {}
for r in reports:
    a = answers.get(r["id"])
    if a and r["status"] == "new":
        r["status"], r["answer"] = a.get("status"), a.get("answer")
    if r.get("status") in ("fixed", "rejected") and not r.get("notified"):
        head = "Исправили, спасибо! " if r["status"] == "fixed" else "Проверили. "
        say(r["chat"], head + (r.get("answer") or ""))
        r["notified"] = True

json.dump(reports, open(REP, "w"), ensure_ascii=False, indent=1)
json.dump(state, open(STATE, "w"), ensure_ascii=False, indent=1)
print("новых:", sum(1 for r in reports if r["status"] == "new"))
