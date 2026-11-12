"""Раздельные категории (Вадим 11.11: «не смешивай, пусть лучше будут отдельно; раздели, которые раньше были объединены —
типа хоккея и фигурного катания»). Сборка (xlsx_to_json.py) вызывает split(p) для каждого места:
1) объединённые категории делятся на отдельные по названию/типу/«Плюсу» места;
2) творческие студии (балет, вокал, музыка, театральная студия, рисование, керамика) получают свою категорию.
Правило честности: если вид из источника не понятен — место остаётся в общей категории (hockey/racket/ballgames/martial/
gymnastics/skate), а не попадает наугад в узкую. Роботы могут ставить узкие категории в таблицу сами."""
import re

# родитель -> [(узкая категория, regex)], keep — regex, при котором родитель тоже остаётся
SPLITS = {
    "hockey": dict(subs=[("figureskating", r"фигурн|figure.?skat")], keep=r"хокке|hockey"),
    "racket": dict(subs=[("squash", r"сквош|squash"), ("tabletennis", r"настольн\w* теннис|пинг.?понг|ping.?pong")],
                   keep=r"(?<!настольный )(?<!настольного )(?<!настольному )теннис|tennis"),
    "ballgames": dict(subs=[("volleyball", r"волейбол|volley")], keep=r"баскетбол|basket|стритбол"),
    "martial": dict(subs=[("boxing", r"бокс|boxing|муай|тайск\w* бокс"), ("sambo", r"самбо|sambo"),
                          ("judo", r"дзюдо|judo"), ("wrestling", r"борьб|греко|вольн\w* стил|wrestling"),
                          ("karate", r"карат[еэ]|karate|киокушин|kyokushin"), ("taekwondo", r"тх[эе]квондо|taekwon")],
                    keep=r"айкидо|ушу|\bмма\b|\bmma\b|кудо|джиу|рукопаш|кунг|капоэйр|фехтов|единоборств|боев\w* искусств"),
    "gymnastics": dict(subs=[("rhythmic", r"художествен\w* гимнаст|\bхуд\.? ?гимнаст|rhythmic"),
                             ("acrobatics", r"акробат|acrobat|паркур|чирлид|cheer")],
                       keep=r"спортивн\w* гимнаст|эстетическ\w* гимнаст|(?<!художественная )(?<!художественной )гимнастик"),
    "skate": dict(subs=[("pumptrack", r"памп|pump")], keep=r"скейт|skate|роллер|самокат|scoot|bmx"),
    "circus": dict(subs=[("animaltheater", r"театр\w* зверей|театр\w* кошек|театр\w* животн|дуров|театр зверей")],
                   keep=r"цирк|шапито|circus"),
    "dance": dict(subs=[("ballet", r"балет|ballet")], keep=r"танц|хореограф|dance|хип.?хоп|брейк|бальн|джаз|модерн|вог|тверк|латин|народн"),
}
# в каких категориях искать вид спорта по «Плюсу» (секции) — чтобы каток «можно поиграть в хоккей» не стал секцией
SECTION = {"sport", "martial", "racket", "ballgames", "gymnastics", "hockey", "dance", "skate", "circus"}
# творческие направления: ставятся любому не-кафе месту по названию/типу, а секциям/центрам — и по «Плюсу»
CREATIVE = [
    ("ballet", r"балет|ballet"),
    ("singing", r"вокал|\bпени[еяю]\b|\bхор\b|\bхора\b|хоров|vocal"),
    ("music", r"музыкальн\w* (школ|студи|центр|класс|занят)|\bдмш\b|\bдшм\b|\bдши\b|фортепиан|гитар|скрипк|барабан|сольфеджио|music school"),
    ("theaterstudio", r"театральн\w* (студи|школ|кружк|мастерск|класс)|театр.?студи|актёрск|актерск|актёрского"),
    ("drawing", r"рисован|\bизо\b|изостуди|художествен\w* (школ|студи)|живопис|\bдхш\b|арт.?студи|art.?studio|скетч"),
    ("ceramics", r"керамик|гончарн|\bлепк|\bглин[аеуы]\b"),
]
# Вадим 12.11: «Давай ещё добавим развивашек других тоже» — узкие направления «Развития и учёбы». Ставятся местам,
# которые уже в этом разделе (по названию/типу/«Плюсу»); детский сад — только по названию/типу.
EDU_SET = {"montessori", "early", "school", "languages", "robotics", "coding", "lego", "kindergarten", "reading", "math", "mentalmath"}
EDU = [
    ("coding", r"программир|кодинг|python|scratch|\bit\b|айти|компьютерн\w* (курс|школ|грамот|академ)|кибершкол|web-?разработ|создани\w* игр"),
    ("lego", r"лего|lego|конструирован"),
    ("mentalmath", r"ментальн\w* арифм|ментальн\w* математ|соробан|абакус|abacus"),
    ("reading", r"скорочтен|каллиграф|обучени\w* чтени|учим\w* читать|техник\w* чтени|постановк\w* почерк"),
    ("math", r"(?<!ментальная )(?<!ментальной )математик|математическ|олимпиадн"),
]
KINDERGARTEN = r"детск\w* сад|мини-?сад|частн\w* сад|детсад|ясли\b|билингвальн\w* сад"
ROBOT_KEEP = r"робот|robot|электроник|ардуино|arduino|инженер|кванториум|техническ\w* творч|3d|дрон|мехатрон"
PLUS_OK = {"dance", "masterclass", "early", "school", "sport", "montessori", "languages", "gymnastics", "shows", "playcenters"}


# Вадим 11.11: «Подмосковье и зима надо расформировать. И сделать отдельно всё, что туда входило».
# winter → rinks (катки), sledding (горки и тюбинг), ski (горнолыжные склоны и школы); «Подмосковье» (trips) было
# вычисляемым (дальше 25 км) — убрано из фильтра; усадьбы, кремли и монастыри — своя категория estates.
WINTER = [("rinks", r"каток|катк|ледов\w* (дворец|арен)|массов\w* катан"),
          ("sledding", r"горк|тюбинг|ватрушк|санк"),
          ("ski", r"горнолыж|лыжн|сноуборд|\bski\b")]
ESTATE = r"усадьб|(?<!кремлёвская )кремл(?!ёвск)|монастыр|лавр[аы]\b|музей-заповедник"


def split(p):
    cats = p.get("cats")
    if cats is None:
        return
    if "winter" in cats:
        nt = ((p.get("name") or "") + " " + " ".join(p.get("type") or [])).lower()
        hits = [c for c, rx in WINTER if re.search(rx, nt)]
        cats = [c for c in cats if c != "winter"] + [c for c in hits if c not in cats]
        p["cats"] = cats
    if "food" in cats:
        return
    if "estates" not in cats and ({"museums", "parks", "tours", "shows"} & set(cats) or not cats) and \
            re.search(ESTATE, ((p.get("name") or "") + " " + " ".join(p.get("type") or [])).lower()):
        cats = cats + ["estates"]
        p["cats"] = cats
    name_type = ((p.get("name") or "") + " " + " ".join(p.get("type") or [])).lower()
    full = (name_type + " " + (p.get("plus") or "")).lower()
    out = list(cats)
    for parent, rule in SPLITS.items():
        if parent not in out:
            continue
        text = full if parent in SECTION else name_type
        hits = [c for c, rx in rule["subs"] if re.search(rx, text)]
        if not hits:
            # «Баскетбол» — узкая категория: мяч другого вида (гандбол и т.п.) — в «Другие секции»
            if parent == "ballgames" and not re.search(rule["keep"], text):
                out.remove(parent)
                if "sport" not in out:
                    out.append("sport")
            continue
        for c in hits:
            if c not in out:
                out.append(c)
        if not re.search(rule["keep"], text):
            out.remove(parent)
    # виды спорта, записанные в «прочие секции»
    if "sport" in out:
        for parent, rule in SPLITS.items():
            if parent in ("circus", "dance", "skate"):
                continue
            for c, rx in rule["subs"] + [(parent, rule["keep"])]:
                if c not in out and re.search(rx, name_type) and not (c in ("martial", "gymnastics") ):
                    out.append(c)
    for c, rx in CREATIVE:
        text = full if PLUS_OK & set(out) else name_type
        if c not in out and re.search(rx, text):
            out.append(c)
    if EDU_SET & set(out):
        for c, rx in EDU:
            if c not in out and re.search(rx, full):
                out.append(c)
        if "kindergarten" not in out and re.search(KINDERGARTEN, name_type):
            out.append("kindergarten")
        # школа программирования без роботов — не в «Робототехнике»
        if "robotics" in out and "coding" in out and not re.search(ROBOT_KEEP, full):
            out.remove("robotics")
    # «Балет»-школа без других танцев — не в общей «Танцы»
    if "ballet" in out and "dance" in out and not re.search(SPLITS["dance"]["keep"], full):
        out.remove("dance")
    p["cats"] = out
