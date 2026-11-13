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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cat_split
try:   # реестр проверок: поля, подтверждённые источником, сборка не переопределяет
    _VERIFIED = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "auto", "verified.json"), encoding="utf-8"))
except Exception:
    _VERIFIED = {}

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
    "Телефон": "phone",
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


_YA = None


def _ya_hours(pid):
    """Часы организации из Яндекс Карт в нашем формате; None — нет записи, место закрыто или текст не разбирается."""
    global _YA
    if _YA is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "auto", "yandex-entrances.json")
        _YA = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    r = _YA.get(pid) or {}
    t = (r.get("hours") or "").strip()
    if not t or "lat" not in r or r.get("status") not in (None, "open"):
        return None
    # 13.11: с серверов GitHub Яндекс отдаёт часы в 12-часовом виде («10:00 AM–8:00 PM») — переводим в 24-часовой
    def _24(mo):
        h, mi, ap = int(mo.group(1)), mo.group(2), mo.group(3).upper()
        h = (h % 12) + (12 if ap == "PM" else 0)
        return f"{h:02d}:{mi}"
    t = re.sub(r"(\d{1,2}):(\d{2})[\s\u202f\u00a0]*(AM|PM)", _24, t, flags=re.I)
    t = re.sub(r"(\d{2}:\d{2})–00:00", r"\1–24:00", t)
    t = re.sub(r",?\s*перерыв[^;]*", "", t)
    t = re.sub(r"^ежедневно,\s*", "ежедневно ", t)
    if "круглосуточно" in t:
        t = "круглосуточно"
    try:
        mode, week = parse_hours(t)
    except Exception:
        return None
    return t if mode in ("hours", "always") else None


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
            # работает за полночь («11:30-00:30», «10:00-00:00»): для приложения считаем до конца суток
            close = 24 * 60
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
            v = "verified" if v == "проверено" else ("closed" if str(v or "").strip().lower() == "closed" else "draft")
        p[key] = v

    # Цирки — отдельная категория circus (не shows): по типу «цирк»/«театр зверей» или слову «цирк» в названии
    if p.get("cats") and ({"цирк", "театр зверей"} & set(p.get("type") or []) or any(k in (p.get("name") or "").lower() for k in ("цирк", "театр кошек"))):
        p["cats"] = ["circus"] + [c for c in p["cats"] if c not in ("shows", "circus")]

    # Детская комната (10.11, категория kidsroom): по типу и «Плюсу» — у кафе, ТЦ, кинотеатров и т.п.
    kr_text = (" ".join(p.get("type") or []) + " " + (p.get("plus") or "")).lower()
    if p.get("cats") is not None and "kidsroom" not in p["cats"] and re.search(r"детск\w* (игров\w* )?комнат|игров\w* комнат|детск\w* игров\w*(?! площадк)", kr_text) \
            and not ({"museums", "parks", "tours"} & set(p["cats"]) and not re.search(r"игров\w* комнат|детск\w* игров", kr_text)):
        p["cats"] = p["cats"] + ["kidsroom"]

    # Развитие и специалисты (11.11): явные по названию/типу места (не кафе) — получают свою категорию сами
    nt = ((p.get("name") or "") + " " + " ".join(p.get("type") or [])).lower()
    if p.get("cats") is not None and "food" not in p["cats"]:
        for cat, rx in (("montessori", r"монтессори|montessori"), ("robotics", r"робототехн|программирован|кванториум|it-школ"),
                        ("speech", r"логопед|дефектолог"), ("lfk", r"\bлфк\b|детск\w* массаж"), ("psych", r"психолог"),
                        ("school", r"подготовк\w* к школе|ментальн\w* арифметик"), ("languages", r"языков\w* (школ|центр)|английск\w* для детей")):
            if cat not in p["cats"] and re.search(rx, nt):
                p["cats"] = p["cats"] + [cat]

    # Раздельные категории (11.11): хоккей/фигурное катание, теннис/сквош/настольный, борьба/самбо/дзюдо/бокс…, балет,
    # вокал, музыка, театральная студия, рисование, керамика — tools/cat_split.py
    cat_split.split(p)
    # Вадим 12.11 (обсудил с женой дважды): пеленальные комнаты доступны ВСЕМ возрастам — нужны не только малышам
    # (папа с дочкой: в женский туалет одна боится, в мужской уже нельзя)
    if "changing" in (p.get("cats") or []) and any("пеленальная комната" in t for t in (p.get("type") or [])):
        p["age_min"], p["age_max"] = 0, 17
    # Вадим 12.11 (Smoothie & Coffee): «почему возраст 0–12? Старше уже не пустят?» — в кафе/ресторан ходит вся семья,
    # возраст детской комнаты — не возраст заведения. У заведений питания (тип — кафе, ресторан, кофейня…) возраст 0–17;
    # ограничение детской комнаты, если есть в источнике, пишется в «Минус»/«Как найти». Исключение: игровые центры,
    # парки и т.п. с кафе внутри (тип не про еду) — их возраст по правилам самого места.
    if "food" in (p.get("cats") or []) and re.search(
            r"кафе|ресторан|кофейн|пиццер|чайхан|бистро|стейк|бургер|кондитер|гастробар|сыроварн|суши|трактир|таверн|харчевн|пекарн|блинн|столов|рестобар|хинкальн|дайнер|банкетн",
            " ".join(p.get("type") or []).lower()):
        p["age_min"], p["age_max"] = 0, 17
    # Вадим 12.11 (фехтовальный клуб «Сталь»): «Занятие бесплатно», хотя бесплатно только ПЕРВОЕ занятие. Цена 0 у секции,
    # где источник пишет «первое/пробное занятие бесплатно», — это пробное, а не цена: цену не знаем, ставим trial_free.
    if p["price_child"] == 0 and re.search(r"перв\w+ (занят|урок|трениров)\w* (—\s*)?бесплат|пробн\w+ (занят|урок|трениров)\w*( —)? бесплат|бесплатн\w+ (перв|пробн)",
                                           ((p.get("plus") or "") + " " + (p.get("free_note") or "")).lower()):
        p["price_child"] = None
        p["trial_free"] = True
    # Вадим 13.11 («Лисёнок»: «Это не может называться билетом… Исправь во всех подобных заведениях»): у секций, кружков,
    # садов и центров развития взрослый ничего не покупает — «Взрослый билет: бесплатно» там бессмыслица. Цена 0 для
    # взрослого у них не пишется (поле пустое). Билетные места (музеи, парки, игровые, батуты) не трогаем.
    _t = " ".join(p.get("type") or []).lower()
    if p["price_adult"] == 0 and re.search(r"секци|школ|студи|кружок|центр развития|детский сад|мини-сад|логопед|дефектолог|курс|коррекц|клуб|дворец творчества|репетитор", _t) \
            and not re.search(r"игров|батут|парк|музе|библиотек|кафе|ресторан|пеленальн", _t):
        p["price_adult"] = None
    # Вадим 13.11 (Цирк Никулина «от 4 до 14 лет»: «В 3 года или раньше не пустят? И более 14 лет не пустят? Недопустимые
    # ограничения! Исправить для этого места и всех других»). Места, куда ходят всей семьёй с любым ребёнком (цирк, зоопарк,
    # музей, парк, усадьба, библиотека…), возрастных ограничений не имеют: «до 14» и «от 4–6 лет» там были догадкой
    # «кому интересно», а фильтр «Кто идёт» по ним прятал место. Ставим 0–17, КРОМЕ возраста, подтверждённого источником
    # (age_min/age_max в auto/verified.json — правила посещения места). Театры, кино, секции, квесты — не трогаем
    # (там бывают настоящие ограничения: спектакль 6+, фильм 12+, набор в группу).
    if re.search(r"цирк|зоопарк|контактн\w* зоопарк|океанариум|музе|парк\b|парк |лесопарк|усадьб|кремль|библиотек|ботаническ|планетари|выставк|смотров|набережн|пляж|ферм", _t) \
            and not re.search(r"театр|кино|квест|секци|школ|студи|батут|аквапарк|верёвочн|веревочн|скейт|памп|картинг|тир\b|лазертаг|пейнтбол|vr|игров|развлекательн|развлечен|аттракцион|технопарк|кванториум", _t):
        _ver = _VERIFIED.get(p["id"], {})
        if "age_min" not in _ver and p["age_min"] is not None:
            p["age_min"] = 0
        if "age_max" not in _ver and p["age_max"] is not None:
            p["age_max"] = 17

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

    # Вадим 13.11 (в 03:22 вся карта цветная: «разве сейчас все эти заведения работают?») — у 2/3 мест часов не было
    # вовсе. Нет своих часов → берём часы той же организации из Яндекс Карт (auto/yandex-entrances.json).
    if not (p.get("hours") or "").strip():
        yh = _ya_hours(p["id"])
        if yh:
            p["hours"], p["hours_src"] = yh, "Яндекс Карты"
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


def apply_precise_points(places, manual_ids=()):
    """Точные точки из автоматических сверок (auto/osm-address.json — дом по адресу из OSM, auto/geo-yandex.json —
    организации Яндекса). Применяются, только если в таблице точку с тех пор не меняли (src совпадает) и место
    не исправляли вручную по сообщению пользователя (ручная правка важнее)."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def load(name):
        path = os.path.join(root, "auto", name)
        return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    manual = set(manual_ids)          # «Точность координат = точно (вручную)» в таблице — точку не трогать никогда
    for r in (load("reports.json") or []):
        if r.get("location") or re.search(r"точк|здани|вход|подъезд|метк|не там|дом", (r.get("text") or "").lower()):
            if r.get("place_id"): manual.add(r["place_id"])
    # объект OSM с тем же названием — только рядом (≤ 300 м): дальше это часто другой филиал сети («Китёнок», «IL Патио»)
    sources = [("geocode-report.json", lambda e: e.get("status") == "high" and 15 < e.get("moved_m", 0) <= 300),
               ("osm-address.json", lambda e: e.get("status") == "moved"),
               ("geo-yandex.json", lambda e: e.get("method") in ("yandex-org", "yandex-addr"))]
    verified_pt = load("verified.json")
    n = {}
    for name, ok in sources:
        data = load(name)
        for p in places:
            e = data.get(p["id"])
            if not e or not ok(e) or p["id"] in manual or p.get("lat") is None: continue
            # 12.11 (бассейн OctoSkills в «Фили Граде»): точку, подтверждённую на объекте/входе САМОГО места (реестр
            # проверок), нельзя переносить на «главный вход дома по адресу» — это вход ТЦ в 134 м, а не вход студии
            if name == "osm-address.json" and verified_pt.get(p["id"], {}).get("point", {}).get("level") in ("объект", "вход"): continue
            src = e.get("src") or [e.get("src_lat"), e.get("src_lon")]
            if src[0] is None or abs(src[0] - p["lat"]) > 1e-6 or abs(src[1] - p["lon"]) > 1e-6: continue
            p["lat"], p["lon"], p["coord_exact"] = e["lat"], e["lon"], True
            n[name] = n.get(name, 0) + 1
    if n:
        print("точные точки:", n)


def norm_phone(s):
    """Российские номера → +7 (XXX) XXX-XX-XX; до двух номеров через «, ». Прочее — как есть."""
    if not s:
        return None
    out = []
    for part in re.split(r"[;,]|\s{2,}", str(s)):
        d = re.sub(r"\D", "", part)
        if len(d) == 11 and d[0] in "78":
            d = "7" + d[1:]
        elif len(d) == 10 and d[0] in "3489":
            d = "7" + d
        else:
            if part.strip() and len(d) >= 6:
                out.append(part.strip())
            continue
        f = f"+7 ({d[1:4]}) {d[4:7]}-{d[7:9]}-{d[9:11]}"
        if f not in out:
            out.append(f)
    return ", ".join(out[:2]) or None


# Служебные пометки роботов и пустые отговорки не показываем людям (Вадим 09.11: «что значит „вечером ресторан
# взрослый“? так по-русски не говорят»; «Детская комната — по справочнику …» — это не минус, а источник).
FILLER = re.compile(r"по справочник|по каталог|по описани|по яндекс|по 2гис|2gis|zoon|jsprav|spravk|в каталоге|"
                    r"по отзыв|по данным|источник|уточняйте|уточнять|уточните|не описан|не подтвержд|"
                    r"ресторан взрослый|вечером взрослый|отмечена детская", re.I)


# «Бесплатно до» (Вадим 11.11, цирк Никулина: «логика в предоставляемой информации… отсекать ненужное»):
# только конкретный факт о цене/бесплатном входе. Отсылки «цены — у клуба / на сайте / уточняйте», «цена «от»» без
# числа и догадки «часто / обычно бесплатно» — не информация, их не показываем.
FREE_FILLER = re.compile(r"уточня|уточн|у клуба|у студии|у школы|у центра|у администратор|у организатор|по телефону|"
                         r"по запросу|по прайсу|на сайте|на месте|в соцсет|зависит от|часто|обычно|как правило|"
                         r"в филиале|у менеджера|у тренера|по записи$|см\.? акци|по афише|по сеансу|назовут|есть$|«от»|"
                         r"^цена от$|^стоимость$", re.I)
FREE_GUESS = re.compile(r"часто|обычно|как правило", re.I)  # догадки — не показывать даже с числом


def clean_texts(p):
    """Из «Плюс»/«Минус» убрать служебные пометки и отговорки; убранное — в «Источник» (для роботов, не для людей)."""
    moved = []
    s = p.get("free_note")
    if s:
        parts = [x.strip() for x in re.split(r"\s*;\s*", s) if x and x.strip()]
        food = "food" in (p.get("cats") or [])
        bad = lambda x: bool(FREE_GUESS.search(x) or (FREE_FILLER.search(x) and not re.search(r"\d", x))
                             or (food and "чек" in x))  # у кафе чек показывается из «Взрослый билет»
        keep = [x for x in parts if not bad(x)]
        moved += [x for x in parts if bad(x)]
        p["free_note"] = "; ".join(keep).strip(" .;,") or None
    for key in ("plus", "minus"):
        s = p.get(key)
        if not s:
            continue
        parts = [x.strip() for x in re.split(r"\s*(?:;|·|\. |, (?=[А-ЯЁа-яё]+ уточн))\s*", s) if x and x.strip()]
        keep = [x for x in parts if not FILLER.search(x)]
        moved += [x for x in parts if FILLER.search(x)]
        out = "; ".join(keep).strip(" .;,")
        p[key] = (out[0].upper() + out[1:]) if out else None
    if moved:
        p["source"] = "; ".join(filter(None, [p.get("source"), *moved]))


def apply_changing(places):
    """Пеленальный стол по OSM (Вадим 11.11, карапузы до года): объект OSM этого места отмечен changing_table=yes —
    «Пеленальный стол = да», если в таблице пусто (auto/osm-changing.json, pipeline/osm_changing.py)."""
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "auto", "osm-changing.json")
    if not os.path.exists(path):
        return
    ids = (json.load(open(path, encoding="utf-8")).get("places") or {})
    n = 0
    for p in places:
        if p["id"] in ids and not p.get("changing_table"):
            p["changing_table"] = "yes"; n += 1
    print(f"Пеленальный стол по OSM: {n}")


def apply_access(places):
    """Доступная среда (Вадим 12.11: «места для людей с ограниченными возможностями — один из самых важных разделов»).
    auto/access-needs.json {id: {wheelchair, toilet, lift, parking, sensory, hearing, vision, programs, free, note, src}}
    — только подтверждённое источником (пишут сверщики через set_verified, поле access). Плюс тег OSM wheelchair
    у объекта этого места (auto/osm-access.json), если своего значения нет. Поле access у места в places.json."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def load(name):
        path = os.path.join(root, "auto", name)
        return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    needs, osm = load("access-needs.json"), load("osm-access.json")
    n = 0
    for p in places:
        a = {k: v for k, v in (needs.get(p["id"]) or {}).items() if k not in ("src", "checked") and v}
        w = ((osm.get(p["id"]) or {}).get("poi") or {}).get("wheelchair") if isinstance(osm.get(p["id"]), dict) else None
        if w in ("yes", "limited", "no") and "wheelchair" not in a:
            a["wheelchair"] = w
        if a:
            p["access"] = a; n += 1
    print(f"Доступная среда: {n}")


def apply_contacts(places, spam, spam_domains):
    """Телефон и сайт (Вадим 09.11: «во всех карточках — рабочие телефоны и ссылки на основной сайт»).
    Порядок: таблица → auto/contacts.json (проверено роботом «навигатор» по сайту/поиску) → объект OSM с тем же
    названием (auto/osm-access.json, теги phone/website). Сайт из контактов ставится, только если в таблице пусто."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def load(name):
        path = os.path.join(root, "auto", name)
        return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    contacts, osm = load("contacts.json"), load("osm-access.json")
    n_phone = n_url = 0
    for p in places:
        c = contacts.get(p["id"]) or {}
        poi = (osm.get(p["id"]) or {}).get("poi") or {}
        if not p.get("phone"):
            p["phone"] = norm_phone(c.get("phone") or poi.get("phone") or poi.get("contact:phone"))
        else:
            p["phone"] = norm_phone(p["phone"])
        if c.get("url_override") and c.get("url") == "":
            p["url"] = None  # сверщик: сайт в OSM/таблице чужой (объект OSM не того места) — не подставлять
        elif not p.get("url") or c.get("url_override"):
            u = c.get("url") or poi.get("website") or poi.get("contact:website") or poi.get("url")
            if u and not u.startswith("http"):
                u = "https://" + u
            if u and not spam.is_spam_url(u, spam_domains):
                p["url"] = u
                n_url += 1
        n_phone += bool(p.get("phone"))
    print(f"Телефонов: {n_phone} из {len(places)}; сайтов добавлено из контактов/OSM: {n_url}")


def apply_cat_ages(places):
    """Возраст по направлениям (Вадим 11.11: робототехника с 5 лет не должна предлагаться трёхлетке, хотя мини-сад
    того же центра с 2,5). auto/cat-ages.json {id: {cat: [от, до], "src": …}} → поле cat_ages у места; age_min/age_max
    места остаются общими (минимум/максимум по всем направлениям)."""
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "auto", "cat-ages.json")
    if not os.path.exists(path):
        return
    data = json.load(open(path, encoding="utf-8"))
    n = 0
    for p in places:
        d = data.get(p["id"])
        if not isinstance(d, dict):
            continue
        ages = {c: v for c, v in d.items() if c in (p.get("cats") or []) and isinstance(v, list) and len(v) == 2}
        if ages:
            p["cat_ages"] = ages; n += 1
    print(f"Возраст по направлениям: {n}")


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

    # координаты из таблиц ДО автоматических уточнений — от них считают сверки (иначе бы «ехали» сами от себя)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json.dump({p["id"]: [p["lat"], p["lon"]] for p in places if p.get("lat") is not None},
              open(os.path.join(root, "auto", "table-coords.json"), "w"), separators=(",", ":"))
    manual_ids = {clean(r.get("id")) for r in rows if "вручную" in str(r.get("Точность координат") or "").lower()}
    apply_precise_points(places, manual_ids)
    apply_contacts(places, spam, spam_domains)
    apply_changing(places)
    apply_cat_ages(places)
    apply_access(places)
    for p in places:
        clean_texts(p)

    # Вадим 10.11: «исключительно точные и проверенные адреса, аватарки прямо на вход» — места без точной точки
    # (приблизительные координаты, «±2 км») приложению и сайту НЕ показываем. Полный список — places-all.json
    # (для роботов и конвейеров: дубли, сверка OSM, навигатор); место вернётся на карту, когда точку подтвердят.
    all_path = os.path.join(os.path.dirname(os.path.abspath(dst)), "places-all.json")
    # 10.11: на карту — только точка до входа/объекта места; «дом по адресу» и «примерно» — скрыты до подтверждения
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import point_level
    acc_txt = {clean(r.get("id")): r.get("Точность координат") for r in rows}
    for p in places:
        p["point_level"] = point_level.level(p["id"], acc_txt.get(p["id"]), p.get("coord_exact"))
        if p["point_level"] == "вход":
            p["point_door"] = point_level.door(p["id"], acc_txt.get(p["id"]))
    # Вадим 12.11: «аватарка — прямо на входе в нужный подъезд… точки должны находить боты: вход в заведение, расположение
    # внутри больших ТЦ». auto/yandex-entrances.json (pipeline/yandex_entrances.py) — та же организация в Яндекс Картах:
    # один вход → точка на этот вход (point_door «вход_яндекс»); входов нет или несколько (ТЦ) → точка организации внутри
    # здания («точка_яндекс»), этаж — в «Как найти». Метку человека («дверь») не трогаем; сдвиг больше 200 м не применяем.
    ya_path = os.path.join(os.path.dirname(os.path.abspath(dst)), "auto", "yandex-entrances.json")
    ya = json.load(open(ya_path, encoding="utf-8")) if os.path.exists(ya_path) else {}

    def _m(a, b, c, d):
        import math
        return math.hypot((a - c) * 111200, (b - d) * 111200 * math.cos(math.radians(a)))
    for p in places:
        r = ya.get(p["id"]) or {}
        if "lat" not in r or p.get("point_level") != "вход" or p.get("point_door") == "дверь" or p.get("lat") is None:
            continue
        if r.get("status") not in (None, "open"):
            continue
        ent = r.get("entrances") or []
        if len(ent) == 1 and _m(p["lat"], p["lon"], ent[0][0], ent[0][1]) <= 200:
            p["lat"], p["lon"], p["point_door"] = ent[0][0], ent[0][1], "вход_яндекс"
        elif p.get("point_door") == "объект" and _m(p["lat"], p["lon"], r["lat"], r["lon"]) <= 200:
            p["lat"], p["lon"], p["point_door"] = r["lat"], r["lon"], "точка_яндекс"
        # Вадим 12.11 («Этаж: 1905???»): у Яндекса поле этажа — свободный текст («Метро: …, Улица 1905 года, этаж 1»,
        # «павильон 151, этаж 3», «Школа 1492»). Берём только явный этаж: число целиком или «этаж N» / «N этаж».
        fs = str(r.get("floor") or "").strip()
        fl = (re.fullmatch(r"(-?\d{1,2})", fs) or re.search(r"этаж\s*(-?\d{1,2}|цокольный|подвальный)(?![\d])", fs, re.I)
              or re.search(r"(?<![\d-])(-?\d{1,2})-?й?\s+этаж", fs, re.I))
        if fl and fl.group(1).lstrip("-").isdigit() and not -5 <= int(fl.group(1)) <= 95:
            fl = None
        if fl and p.get("point_door") in ("вход_яндекс", "точка_яндекс") and "этаж" not in (p.get("how_to_find") or "").lower():
            p["how_to_find"] = ((p.get("how_to_find") or "") + "\nЭтаж: " + fl.group(1)).strip()
    # Вадим 13.11: «Места должны появляться на карте вместе с уникальной картинкой» — без своей иконки место на карту не идёт
    # (исходник icons-src/<id>.svg или встроенная p/img/<id>.png); в places-all.json у него no_icon: true — рисует «художник».
    _root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    _svg = {f[:-4] for f in os.listdir(os.path.join(_root, "icons-src")) if f.endswith(".svg")}
    _img = {f[:-4] for f in os.listdir(os.path.join(_root, "p", "img")) if f.endswith(".png")} if os.path.isdir(os.path.join(_root, "p", "img")) else set()
    for p in places:
        if p["id"] not in _svg and p["id"] not in _img:
            p["no_icon"] = True
    shown = [p for p in places if p["point_level"] == "вход" and p.get("lat") is not None and p.get("status") != "closed"
             and not p.get("no_icon")]
    print("без своей иконки (на карту не идут):", sum(1 for p in places if p.get("no_icon")))
    for path, lst in ((all_path, places), (dst, shown)):
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"version": date.today().isoformat(),
                       "contact_telegram": CONTACT_TELEGRAM or None,
                       "places": lst},
                      f, ensure_ascii=False, indent=2)

    print(f"Выгружено мест: {len(shown)} -> {dst} (скрыто без точки до входа: {len(places) - len(shown)}; все — places-all.json)")
    if report:
        print(f"\nМест с проблемами: {len(report)}")
        for name, probs in report:
            print(f"- {name}: {'; '.join(probs)}")


if __name__ == "__main__":
    main()
