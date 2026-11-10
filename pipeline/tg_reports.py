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
# Проверяющие (Вадим 10.11: помощница лично проверяет карточки): {chat_id: имя}. Их отметки «Всё верно» — в
# auto/human-checks.json (считаются подтверждением карточки), их правки — доверенные (trusted) для робота-исправителя.
CHECKERS, CHECKS = "auto/checkers.json", "auto/human-checks.json"
CHECK_KB = json.dumps({"keyboard": [[{"text": "▶️ Проверять карточки"}]], "resize_keyboard": True, "is_persistent": True})
NEXT_KB = json.dumps({"inline_keyboard": [[{"text": "▶️ Следующая карточка", "callback_data": "next:x"}]]})
PRIORITY = ["food", "kidsroom", "playcenters", "pools", "dance", "martial", "gymnastics", "football", "ballgames",
            "sport", "trampolines", "quests", "masterclass", "museums", "shows", "animals", "parks"]
MINUTES = int(sys.argv[sys.argv.index("--minutes") + 1]) if "--minutes" in sys.argv else 0

SITE = "https://vadimsurov-apps.github.io/kudapoiti-data/"
MAP_KB = json.dumps({"inline_keyboard": [[{"text": "🗺 Открыть карту", "web_app": {"url": SITE}}],
                                         [{"text": "% Акции и бесплатные пробные", "web_app": {"url": SITE + "?deals=1"}}]]})
WELCOME = ("👋 Здравствуйте! Это «Куда пойти с детьми» — карта 1600+ детских мест Москвы и Подмосковья: "
           "игровые центры, секции, кафе с детской комнатой, музеи, бассейны, театры.\n\n"
           "Часы работы, цены, как найти вход, а ещё акции, скидки и бесплатные пробные занятия.\n\n"
           "Нажмите «🗺 Открыть карту» 👇 (она же всегда в кнопке «Карта» внизу чата).\n\n"
           "Нашли неточность? Просто напишите сюда, что не так, — мы проверим и исправим.")
HELLO = ("👋 Здравствуйте! Это помощник приложения «Куда пойти с детьми».\n\n"
         "Сюда пишут, если в приложении что-то неточно: неверные часы, адрес, цена, место закрылось или "
         "переехало, нет детской комнаты и т.п.\n\n")
ASK_PLACE = HELLO + "✍️ Напишите одним сообщением: какое место и что не так. Можно приложить фото."
DONE = "Спасибо! 🙌 Сообщение получено. Мы проверим и исправим — обычно в течение часа — и напишем сюда, что сделали."


def call(method, http_timeout=30, **params):
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(API + method, data=data, timeout=http_timeout) as r:
        return json.load(r)["result"]


def say(chat, text, kb=None):
    try: call("sendMessage", chat_id=chat, text=text, **({"reply_markup": kb} if kb else {}))
    except Exception as e: print("send:", e)


def call_quiet(method, **params):
    try: return call(method, **params)
    except Exception as e: print(method, e)


def checkers():
    return json.load(open(CHECKERS)) if os.path.exists(CHECKERS) else {}


def load_checks():
    return json.load(open(CHECKS)) if os.path.exists(CHECKS) else []


def all_places():
    return json.load(open("places.json"))["places"]


def next_place(chat, state, checks):
    """Следующая карточка: на карте, не проверена людьми за 30 дней, не пропущена этим человеком; важные категории первыми."""
    fresh = time.strftime("%Y-%m-%d", time.gmtime(time.time() - 30 * 86400))
    done = {c["place_id"] for c in checks if c.get("date", "") >= fresh}
    skipped = set(state.setdefault("skipped", {}).get(chat, []))
    def rank(p):
        cats = p.get("cats") or []
        return min([PRIORITY.index(c) for c in cats if c in PRIORITY] or [len(PRIORITY)])
    left = [p for p in all_places() if p["id"] not in done and p["id"] not in skipped]
    left.sort(key=rank)
    return (left[0] if left else None), len(left)


def card_text(p, left):
    q = lambda v: v if v not in (None, "", []) else "—"
    food = "food" in (p.get("cats") or [])
    if food:
        price = f"средний чек ≈ {p['price_adult']} ₽" if p.get("price_adult") else "—"
    else:
        parts = []
        if p.get("price_child") is not None: parts.append(f"детский {p['price_child']} ₽")
        if p.get("price_adult") is not None: parts.append(f"взрослый {p['price_adult']} ₽")
        price = ", ".join(parts) or "—"
    lines = [f"🔎 Проверка карточки (осталось {left})", "", (p['name'] if "«" in p['name'] else f"«{p['name']}»"), f"Тип: {q(', '.join(p.get('type') or []))}",
             f"📍 Адрес: {q(p.get('address'))}", f"🚪 Как найти: {q(p.get('how_to_find'))}",
             f"🕒 Часы: {q(p.get('hours'))}", f"💳 Цена: {price}", f"📞 Телефон: {q(p.get('phone'))}",
             f"🌐 Сайт: {q(p.get('url'))}", f"👶 Возраст: {q(p.get('age_min'))}–{q(p.get('age_max'))} лет"]
    if "kidsroom" in (p.get("cats") or []): lines.append("🧸 Детская комната: есть")
    if p.get("plus"): lines.append(f"👍 {p['plus']}")
    if p.get("minus"): lines.append(f"⚠️ {p['minus']}")
    lines += ["", "Сверьте с Яндекс Картами / сайтом / звонком. «Наша точка» — где стоит метка в приложении: она должна быть ровно на входе."]
    return "\n".join(lines)


def card_kb(p):
    q = urllib.parse.quote
    row1 = [{"text": "📍 Наша точка", "url": f"https://yandex.ru/maps/?pt={p['lon']},{p['lat']}&z=18&l=map"},
            {"text": "🗺 Найти в Яндексе", "url": "https://yandex.ru/maps/?text=" + q(f"{p['name']} {p.get('address') or ''}")}]
    rows = [row1]
    if p.get("url"): rows.append([{"text": "🌐 Сайт места", "url": p["url"]}])
    rows.append([{"text": "✅ Всё верно", "callback_data": f"ok:{p['id']}"[:64]},
                 {"text": "✏️ Есть ошибка", "callback_data": f"bad:{p['id']}"[:64]}])
    # 10.11 (Виктория через Вадима): отдельная кнопка — место больше не работает, карточку убрать с карты
    rows.append([{"text": "🚫 Закрылось — удалить карточку", "callback_data": f"close:{p['id']}"[:64]}])
    rows.append([{"text": "⏭ Пропустить", "callback_data": f"skip:{p['id']}"[:64]}])
    return json.dumps({"inline_keyboard": rows})


def send_card(chat, state, checks):
    p, left = next_place(chat, state, checks)
    if not p:
        say(chat, "🎉 Все карточки на карте проверены за последние 30 дней. Спасибо!"); return
    say(chat, card_text(p, left), card_kb(p))


def handle_callback(cb, places, reports, state, checks):
    chat = str(cb["message"]["chat"]["id"]); data = cb.get("data", "")
    names = checkers()
    call_quiet("answerCallbackQuery", callback_query_id=cb["id"])
    if chat not in names or ":" not in data: return False
    act, pid = data.split(":", 1)
    mid = cb["message"]["message_id"]
    if act == "ok":
        checks.append({"place_id": pid, "by": names[chat], "chat": chat, "ok": True,
                       "date": time.strftime("%Y-%m-%d"), "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
        call_quiet("editMessageReplyMarkup", chat_id=chat, message_id=mid,
                   reply_markup=json.dumps({"inline_keyboard": [[{"text": "✅ Проверено — всё верно", "callback_data": "noop:x"}]]}))
        send_card(chat, state, checks); return True
    if act == "bad":
        state["chats"][chat] = pid; state.setdefault("fixing", {})[chat] = pid
        # карточку с ошибкой больше не подсовываем (10.11: бот присылал её снова и снова)
        checks.append({"place_id": pid, "by": names[chat], "chat": chat, "ok": False,
                       "date": time.strftime("%Y-%m-%d"), "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
        call_quiet("editMessageReplyMarkup", chat_id=chat, message_id=mid,
                   reply_markup=json.dumps({"inline_keyboard": [[{"text": "✏️ Пишу, что не так…", "callback_data": "noop:x"}]]}))
        say(chat, f"✍️ «{places.get(pid, pid)}»: напишите, что не так и как правильно (часы, цена, телефон, вход, этаж…). "
                  "Можно несколькими сообщениями. Метка не на входе — пришлите геопозицию входа: 📎 → «Геопозиция» "
                  "(или координаты текстом). Можно фото вывески.\n\nКогда закончите — «▶️ Следующая карточка».", NEXT_KB)
        return True
    if act == "close":
        # заявка на удаление: робот-исправитель сверит (её скриншот «Больше не работает» в Яндексе — уже источник)
        # и поставит closed — место пропадёт с карты и сайта, а в places-all останется, чтобы роботы не добавили его снова
        state["chats"][chat] = pid; state.setdefault("fixing", {})[chat] = pid
        checks.append({"place_id": pid, "by": names[chat], "chat": chat, "ok": False,
                       "date": time.strftime("%Y-%m-%d"), "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
        reports.append({"id": f"close-{cb['id']}", "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                        "chat": chat, "place_id": pid, "place": places.get(pid), "action": "close",
                        "text": "Место больше не работает — удалить карточку", "photo": None, "photo_file": None,
                        "location": None, "status": "new", "trusted": True, "by": names[chat]})
        call_quiet("editMessageReplyMarkup", chat_id=chat, message_id=mid,
                   reply_markup=json.dumps({"inline_keyboard": [[{"text": "🚫 Отмечено: закрылось", "callback_data": "noop:x"}]]}))
        say(chat, f"🚫 «{places.get(pid, pid)}» — приняли: удалить с карты. Чтобы убрали сразу, пришлите скриншот, где видно "
                  "«Больше не работает» (Яндекс Карты, 2ГИС) или объявление о закрытии, либо ссылку. Скриншот прикрепится "
                  "к этому месту.\n\nДальше — «▶️ Следующая карточка».", NEXT_KB)
        return True
    if act == "next":
        state.get("fixing", {}).pop(chat, None)
        call_quiet("editMessageReplyMarkup", chat_id=chat, message_id=mid, reply_markup=json.dumps({"inline_keyboard": []}))
        send_card(chat, state, checks); return True
    if act == "skip":
        state.setdefault("skipped", {}).setdefault(chat, []).append(pid)
        call_quiet("editMessageReplyMarkup", chat_id=chat, message_id=mid,
                   reply_markup=json.dumps({"inline_keyboard": [[{"text": "⏭ Пропущено", "callback_data": "noop:x"}]]}))
        send_card(chat, state, checks); return True
    return False


def greet_checkers(state):
    for chat, name in checkers().items():
        if chat not in state.setdefault("greeted", []):
            say(chat, f"👋 {name}, вы подключены к проверке карточек «Куда пойти с детьми».\n\n"
                      "Нажмите «▶️ Проверять карточки» внизу — бот пришлёт карточку места. Сверьте её с Яндекс Картами, "
                      "сайтом или звонком и нажмите «✅ Всё верно» или «✏️ Есть ошибка». После ответа сразу придёт "
                      "следующая. Ваши проверки сразу засчитываются, а исправления вносятся в приложение.", CHECK_KB)
            state["greeted"].append(chat)


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True)


def load():
    places = {p["id"]: p["name"] for p in json.load(open("places-all.json" if __import__("os").path.exists("places-all.json") else "places.json"))["places"]}
    reports = json.load(open(REP)) if os.path.exists(REP) else []
    state = json.load(open(STATE)) if os.path.exists(STATE) else {"offset": 0, "chats": {}}
    return places, reports, state


def save(reports, state, msg):
    json.dump(reports, open(REP, "w"), ensure_ascii=False, indent=1)
    json.dump(state, open(STATE, "w"), ensure_ascii=False, indent=1)
    json.dump(CHECKS_MEM, open(CHECKS, "w"), ensure_ascii=False, indent=0)
    git("add", REP, STATE, CHECKS, "auto/report-photos")
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
    names = checkers()
    if chat in names and (text in ("▶️ Проверять карточки", "/check") or text.startswith("▶️")):
        state.get("fixing", {}).pop(chat, None)
        send_card(chat, state, CHECKS_MEM); return True
    if text.startswith("/start"):
        arg = text[6:].strip()
        pid = arg[2:] if arg.startswith("e_") else None
        state["chats"][chat] = pid if pid in places else None
        if pid in places:
            say(chat, HELLO + f"📍 Вы сообщаете о месте: «{places[pid]}».\n\n"
                      "✍️ Напишите одним сообщением, что не так. Можно приложить фото.\n\n"
                      "🎯 Точка стоит не там? Пришлите геопозицию входа: 📎 → «Геопозиция» → "
                      "передвиньте метку ровно на вход → «Отправить». Это самый точный способ.")
        else:
            say(chat, WELCOME, MAP_KB)
        return False
    photo = (m.get("photo") or [{}])[-1].get("file_id")
    loc = m.get("location") or (m.get("venue") or {}).get("location")
    location = [loc["latitude"], loc["longitude"]] if loc else None
    if location and not text:
        text = "Геопозиция входа"
    pid = state["chats"].get(chat)
    photo_file = None
    if photo:   # скачиваем фото, чтобы робот-исправитель мог его посмотреть
        try:
            fp = call("getFile", file_id=photo)["file_path"]
            os.makedirs("auto/report-photos", exist_ok=True)
            photo_file = f"auto/report-photos/{u['update_id']}.jpg"
            urllib.request.urlretrieve(f"https://api.telegram.org/file/bot{TOKEN}/{fp}", photo_file)
        except Exception as e:
            print("photo:", e); photo_file = None
    reports.append({"id": str(u["update_id"]), "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(m.get("date", 0))),
                    "chat": chat, "place_id": pid, "place": places.get(pid), "text": text, "photo": photo,
                    "photo_file": photo_file, "location": location, "status": "new",
                    **({"trusted": True, "by": names[chat]} if chat in names else {})})
    if chat in names and state.get("fixing", {}).get(chat):
        say(chat, f"📝 Записали к «{places.get(pid, pid)}». Можно дописать ещё или нажать «▶️ Следующая карточка».", NEXT_KB)
        return True
    say(chat, DONE)
    return True


def answers(reports, state=None):
    a = json.load(open(ANS)) if os.path.exists(ANS) else {}
    changed = False
    for r in reports:
        x = a.get(r["id"])
        if x and r["status"] == "new":
            r["status"], r["answer"] = x.get("status"), x.get("answer"); changed = True
        if r.get("status") in ("fixed", "rejected") and not r.get("notified"):
            head = "✅ Исправили, спасибо! " if r["status"] == "fixed" else "🔎 Проверили. "
            say(r["chat"], head + (r.get("answer") or "")); r["notified"] = True; changed = True
        # 10.11 (Вадим): правку не подтвердили по источникам — спрашиваем, где это видно; ответ пойдёт к тому же месту
        if r.get("status") == "need_source" and not r.get("notified"):
            say(r["chat"], "🔎 Пока не нашли подтверждения: " + (r.get("answer") or "") +
                "\n\nПодскажите, пожалуйста, где это видно — ссылку на сайт/страницу места, скриншот или фото. "
                "Ответьте следующим сообщением — оно прикрепится к этому месту.")
            if state is not None and r.get("place_id"):
                state.setdefault("chats", {})[r["chat"]] = r["place_id"]
            r["notified"] = True; changed = True
    return changed


def setup():
    # описание бота видно ещё до нажатия «Запустить»
    try:
        call("setMyDescription", description=
             "Карта детских мест Москвы и Подмосковья: игровые центры, секции, кафе с детской, музеи, бассейны.\n\n"
             "Часы работы, цены, акции и бесплатные пробные занятия. Нажмите «Запустить» — и откройте карту.")
        call("setMyShortDescription", short_description="Куда пойти с детьми в Москве: карта 1600+ мест, акции и скидки")
        call("setChatMenuButton", menu_button=json.dumps({"type": "web_app", "text": "Карта", "web_app": {"url": SITE}}))
    except Exception as e:
        print("описание:", e)


CHECKS_MEM = []


def main():
    global CHECKS_MEM
    setup()
    CHECKS_MEM = load_checks()
    deadline = time.time() + MINUTES * 60
    places, reports, state = load()
    greet_checkers(state)
    last_pull = 0
    while True:
        try:
            ups = call("getUpdates", http_timeout=70, offset=state["offset"], timeout=50 if MINUTES else 0,
                       allowed_updates='["message","callback_query"]')
        except Exception as e:
            print("getUpdates:", e); time.sleep(5); ups = []
        new = False
        for u in ups:
            state["offset"] = u["update_id"] + 1
            if u.get("callback_query"):
                new |= handle_callback(u["callback_query"], places, reports, state, CHECKS_MEM)
            else:
                new |= handle(u, places, reports, state)
        if ups:
            save(reports, state, "Сообщения об ошибках")
        if time.time() - last_pull > 60 or not MINUTES:
            git("pull", "-q", "--rebase", "-X", "theirs", "origin", "main")
            # своё состояние (reports/state) держим в памяти — оно новее; после pull свежие только места и ответы робота
            places = load()[0]
            greet_checkers(state)
            if answers(reports, state):
                save(reports, state, "Ответы на сообщения об ошибках")
            last_pull = time.time()
        if not MINUTES or time.time() > deadline:
            break
    print("новых:", sum(1 for r in reports if r["status"] == "new"))


main()
