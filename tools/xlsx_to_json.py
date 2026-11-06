#!/usr/bin/env python3
"""
Конвертер базы мест «Куда пойти»: таблица .xlsx -> places.json для приложения.

Запуск на Mac (один раз установить библиотеку):
    pip3 install openpyxl
    python3 xlsx_to_json.py kuda-poiti-mesta.xlsx places.json

Флаги:
    --only-verified   выгружать только места со статусом «проверено»

Скрипт ничего не выдумывает: пустая ячейка -> null в JSON.
В конце печатает список проблем по каждому месту (нет координат, цены и т.п.).
"""
import json, os
import re
import sys
from datetime import date, datetime

try:
    import openpyxl
except ImportError:
    sys.exit("Нет библиотеки openpyxl. Установи: pip3 install openpyxl")

# Ник в Telegram для кнопки «Здесь ошибка» (без @). Пусто — кнопка скрыта.
CONTACT_TELEGRAM = "kudapoiti_deti_bot"  # бот приёма ошибок (pipeline/tg_reports.py)

# Колонка в таблице -> ключ в JSON
COLUMNS = {
    "id": "id",
    "Название": "name",
    "Тип": "type",
    "Метро": "metro",
    "Адрес": "address",
    "Широта": "lat",
    "Долгота": "lon",
    "Возраст от": "age_min",
    "Возраст до": "age_max",
    "Длит. от, мин": "duration_min",
    "Длит. до, мин": "duration_max",
    "Энергия": "energy",
    "Громко": "loud",
    "Темно": "dark",
    "Толпы": "crowded",
    "Сидеть неподвижно": "sit_still",
    "Теги интересов": "tags",
    "Детский билет, ₽": "price_child",
    "Взрослый билет, ₽": "price_adult",
    "Бесплатно до (лет / см)": "free_note",
    "Запись": "booking",
    "Часы работы": "hours",
    "Сезон (месяцы)": "season",
    "В помещении": "indoor",
    "Еда на месте": "food",
    "Пеленальный стол": "changing_table",
    "Гардероб": "cloakroom",
    "Коляска": "stroller",
    "Парковка": "parking",
    "Интересно взрослым (1–3)": "adult_interest",
    "Плюс": "plus",
    "Минус": "minus",
    "Сайт": "url",
    "Источник": "source",
    "Проверено (дата)": "verified_at",
    "Статус данных": "status",
    "Категории": "cats",
    "Точность координат": "coord_exact",
    "День рождения": "birthday",
    "Как найти": "how_to_find",
}

ENERGY = {"спокойно": "calm", "средне": "medium", "активно": "active"}
TRISTATE = {"да": "yes", "нет": "no", "частично": "partial"}
BOOKING = {"не нужна": "none", "желательна": "recommended",
           "обязательна": "required", "проверить": None}
TAGS = {
    "животные": "animals", "динозавры": "dinosaurs",
    "машины и транспорт": "transport", "космос": "space",
    "творчество": "creativity", "музыка": "music",
    "наука и опыты": "science", "вода": "water",
    "спорт и активность": "sport", "сказки и театр": "theatre",
    "природа": "nature", "конструкторы": "building",
}
TRISTATE_KEYS = {"loud", "dark", "crowded", "sit_still", "indoor", "food",
                 "changing_table", "cloakroom", "stroller", "parking"}
INT_KEYS = {"age_min", "age_max", "duration_min", "duration_max", "adult_interest"}


def clean(v):
    if v is None:
        return None
    if isinstance(v, str):
        v = v.strip()
        return v or None
    return v


def to_int(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return int(v)
    m = re.search(r"\d[\d\s]*", str(v))
    return int(re.sub(r"\s", "", m.group())) if m else None


def to_float(v):
    if v is None:
        return None
    try:
        return float(str(v).replace(",", "."))
    except ValueError:
        return None


DAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
TIME_RANGE = re.compile(r"^(\d{1,2}):(\d{2})\s*[-–—]\s*(\d{1,2}):(\d{2})$")


def parse_days(spec):
    """«ежедневно», «пн», «вт-чт», «вт,ср,пт» -> индексы 0..6 (пн..вс)."""
    spec = spec.strip().lower()
    if spec in ("ежедневно", "ежедн.", "ежедн", "каждый день"):
        return list(range(7))
    out = []
    for token in spec.replace(" ", "").split(","):
        if not token:
            continue
        if "-" in token or "–" in token:
            a, b = re.split(r"[-–]", token)
            if a not in DAYS or b not in DAYS:
                raise ValueError(token)
            i, j = DAYS.index(a), DAYS.index(b)
            out += list(range(i, j + 1)) if i <= j else list(range(i, 7)) + list(range(0, j + 1))
        else:
            if token not in DAYS:
                raise ValueError(token)
            out.append(DAYS.index(token))
    return out


def parse_hours(text):
    """
    Текст часов -> (mode, week).
    mode: always | schedule | hours | unknown
    week: 7 элементов (пн..вс), каждый [открытие, закрытие] в минутах от полуночи или None (закрыто).
    """
    if not text:
        return "unknown", None
    t = text.strip().lower()
    if t == "круглосуточно":
        return "always", None
    if t.startswith("по расписанию") or t.startswith("по записи"):
        return "schedule", None
    week = [None] * 7
    for part in t.split(";"):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^(.*?)\s+(выходной|\d{1,2}:\d{2}\s*[-–—]\s*\d{1,2}:\d{2})$", part)
        if not m:
            raise ValueError(part)
        days = parse_days(m.group(1))
        if m.group(2) == "выходной":
            for d in days:
                week[d] = None
            continue
        h1, m1, h2, m2 = map(int, TIME_RANGE.match(m.group(2)).groups())
        open_, close = h1 * 60 + m1, h2 * 60 + m2
        if close <= open_:
            raise ValueError(part)
        for d in days:
            week[d] = [open_, close]
    return "hours", week


def convert_row(raw, problems):
    p = {}
    for ru, key in COLUMNS.items():
        v = clean(raw.get(ru))
        if key in INT_KEYS:
            v = to_int(v)
        elif key in ("lat", "lon"):
            v = to_float(v)
        elif key in ("price_child", "price_adult"):
            # «от 2 800 (стандартный билет)» -> 2800, «0» -> 0
            v = to_int(v)
        elif key == "energy":
            v = ENERGY.get(v) if v else None
        elif key in TRISTATE_KEYS:
            v = TRISTATE.get(v.lower()) if isinstance(v, str) else None
        elif key == "booking":
            v = BOOKING.get(v) if v else None
        elif key == "tags":
            ru_tags = [t.strip().lower() for t in (v or "").split(",") if t.strip()]
            unknown = [t for t in ru_tags if t not in TAGS]
            if unknown:
                problems.append(f"неизвестные теги: {', '.join(unknown)}")
            v = [TAGS[t] for t in ru_tags if t in TAGS]
        elif key == "type":
            v = [t.strip() for t in (v or "").split(",") if t.strip()]
        elif key == "cats":
            v = [t.strip() for t in (v or "").split(",") if t.strip()] or None
        elif key == "coord_exact":
            v = True if isinstance(v, str) and v.strip().lower().startswith("точно") else None
        elif key == "birthday":
            v = True if isinstance(v, str) and v.strip().lower() == "да" else None
        elif key == "verified_at":
            if isinstance(v, (datetime, date)):
                v = v.strftime("%Y-%m-%d")
        elif key == "status":
            v = "verified" if v == "проверено" else "draft"
        p[key] = v

    # Цирки — отдельная категория circus (не shows): по типу «цирк»/«театр зверей» или слову «цирк» в названии
    if p.get("cats") and ({"цирк", "театр зверей"} & set(p.get("type") or []) or any(k in (p.get("name") or "").lower() for k in ("цирк", "театр кошек"))):
        p["cats"] = ["circus"] + [c for c in p["cats"] if c not in ("shows", "circus")]

    # Сезон «11-03» -> [11, 12, 1, 2, 3]; пусто -> круглый год
    p["season_months"] = None
    if p.get("season"):
        m = re.match(r"^\s*(\d{1,2})\s*[-–]\s*(\d{1,2})\s*$", str(p["season"]))
        if m and 1 <= int(m.group(1)) <= 12 and 1 <= int(m.group(2)) <= 12:
            a, b = int(m.group(1)), int(m.group(2))
            p["season_months"] = list(range(a, b + 1)) if a <= b else list(range(a, 13)) + list(range(1, b + 1))
        else:
            problems.append(f"не разобран сезон «{p['season']}» — нужен формат 11-03")
    p.pop("season", None)

    # Часы работы -> структура для фильтра «открыто сейчас»
    try:
        p["open_mode"], p["open_week"] = parse_hours(p["hours"])
    except ValueError as e:
        problems.append(f"не разобраны часы «{p['hours']}» (кусок: {e}) — см. формат в листе «Как заполнять»")
        p["open_mode"], p["open_week"] = "unknown", None

    # Проверки, без которых подбор работать не будет
    if p["lat"] is None or p["lon"] is None:
        problems.append("нет координат (Широта/Долгота) — не посчитать расстояние")
    if p["age_min"] is None or p["age_max"] is None:
        problems.append("нет возраста")
    elif p["age_min"] > p["age_max"]:
        problems.append("возраст «от» больше «до»")
    if p["duration_min"] is None:
        problems.append("нет длительности")
    if p["indoor"] is None:
        problems.append("не указано «В помещении» — не сработает фильтр погоды")
    if p["price_child"] is None and p["price_adult"] is None:
        problems.append("нет цены")
    if p["hours"] is None:
        problems.append("нет часов работы")
    if not p["tags"]:
        problems.append("нет тегов интересов")
    if p["status"] != "verified":
        problems.append("не проверено")
    return p


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only_verified = "--only-verified" in sys.argv
    if len(args) != 2:
        sys.exit(__doc__)
    src, dst = args

    # основная таблица + таблицы роботов data/parts/*.xlsx (у каждого робота своя — не мешают друг другу)
    import glob
    files = [src] + sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(src)), "parts", "*.xlsx")))
    rows = []
    for fpath in files:
        ws = openpyxl.load_workbook(fpath, data_only=True)["Места"]
        header = [clean(c.value) for c in ws[1]]
        missing = [c for c in ("id", "Название") if c not in header]
        if missing:
            sys.exit(f"{fpath}: в листе «Места» нет колонок: {', '.join(missing)}")
        rows += [dict(zip(header, row)) for row in ws.iter_rows(min_row=2, values_only=True)]

    # ссылки на взломанные сайты (казино/букмекеры) в приложение не пускаем — см. pipeline/spam.py
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
    import spam
    spam_domains = spam.load_domains()
    places, report, ids = [], [], set()
    for raw in rows:
        if not clean(raw.get("id")):
            continue
        problems = []
        p = convert_row(raw, problems)
        if p["id"] in ids:
            sys.exit(f"Повтор id: {p['id']}")
        ids.add(p["id"])
        if p.get("url") and spam.is_spam_url(p["url"], spam_domains):
            print(f"СПАМ-САЙТ убран из места {p['id']}: {p['url']}")
            p["url"] = None
        if spam.is_spam_text(" ".join(str(v) for v in p.values() if isinstance(v, str))):
            print(f"СПАМ в тексте места {p['id']} — место не выгружено")
            continue
        if only_verified and p["status"] != "verified":
            continue
        places.append(p)
        if problems:
            report.append((p["name"], problems))

    with open(dst, "w", encoding="utf-8") as f:
        json.dump({"version": date.today().isoformat(),
                   "contact_telegram": CONTACT_TELEGRAM or None,
                   "places": places},
                  f, ensure_ascii=False, indent=2)

    print(f"Выгружено мест: {len(places)} -> {dst}")
    if report:
        print(f"\nМест с проблемами: {len(report)}")
        for name, probs in report:
            print(f"- {name}: {'; '.join(probs)}")


if __name__ == "__main__":
    main()
