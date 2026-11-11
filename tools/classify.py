"""Раскладывает места по категориям фильтра и отмечает, где проводят дни рождения.
Пишет колонки «Категории» и «День рождения» в таблицу. Ручные правки — в OVERRIDE."""
import openpyxl, re, sys
SRC = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "..", "data", "kuda-poiti-mesta.xlsx")

OVERRIDE = {
    # id: [категории]
    "panorama360": ["tours"], "aerial-city-deck": ["tours"], "cdm-observation": ["tours"], "ostankino-tower": ["tours"],
    "kanatka": ["tours"], "solnce-moskvy": ["amusement", "tours"], "river-cruise": ["tours", "water"],
    "lock-cruise": ["tours", "water"], "city-sightseeing": ["tours"], "annushka-tram": ["tours", "transport", "food"],
    "aeroexpress-ride": ["tours", "transport"], "chistaya-liniya": ["tours", "masterclass"],
    "pobeda-chocolate": ["tours", "masterclass"], "konfael": ["masterclass", "tours"], "mosfilm": ["tours", "museums"],
    "tsdm": ["playcenters", "tours"], "ded-moroz": ["tours", "shows"], "i-can-fly": ["amusement"], "vacuum-tube-sokolniki": ["amusement"],
    "experimentanium": ["science"], "innopark": ["science"], "lunarium": ["science"], "darwin": ["museums", "science"],
    "polytech-main": ["science", "museums"], "polytech-open": ["science"], "planetarium": ["science"],
    "museum-emotions": ["science"], "brain-museum": ["science"], "museum-darkness": ["science"], "atom-sandbox": ["science"],
    "vdnh-atom": ["science", "museums"], "kvantorium-moscow": ["science", "masterclass"], "robostation": ["science"],
    "machines-uprising": ["science"], "museum-cryptography": ["science", "museums"], "water-museum": ["science", "museums"],
    "illuzion-cinema": ["cinema"], "cinema-pioner": ["cinema"], "soyuzmultpark": ["cinema", "playcenters"],
    "museum-cinema-vdnh": ["cinema", "museums"], "animation-museum": ["museums", "cinema"],
    "gaidarovka": ["museums"], "rgdb": ["museums"], "golf-mcc-kids": ["sport"], "minigolf-bauman": ["amusement"],
    "arcade-museum": ["museums", "playcenters"], "kidzania": ["playcenters"], "kidburg": ["playcenters"],
    "kidburg-skazki": ["playcenters", "shows"], "fixi-park": ["playcenters"], "hello-park": ["playcenters"],
    "joki-joya": ["playcenters"], "zamania": ["playcenters"], "panda-park": ["ropes", "playcenters"],
    "kidlandia": ["playcenters"], "more-peska": ["playcenters"], "happy-city": ["playcenters"], "niki-land": ["playcenters"],
    "veselye-dzhungli": ["playcenters"], "indigo-terra": ["playcenters", "trampolines"], "skytown-vdnh": ["ropes"],
    "drift-cdm": ["karting", "transport"], "tasty-lab-krasnogorsk": ["masterclass"], "impressions-museum-sp": ["museums"],
    "master-panin": ["shows"], "izmailovo-kremlin": ["museums", "masterclass"],
}
# типы → категории (если нет в OVERRIDE)
TYPES = [
    ("parks", {"парк", "детская площадка", "ботанический сад", "усадьба"}),
    ("playcenters", {"игровой центр", "игровой город профессий"}),
    ("trampolines", {"батутный центр"}),
    ("amusement", {"парк развлечений"}),
    ("ropes", {"верёвочный парк", "веревочный парк"}),
    ("climbing", {"скалодром"}),
    ("karting", {"картинг"}),
    ("skate", {"скейт-парк"}),
    ("dance", {"танцы", "балет", "танцевальная студия"}),
    ("sport", {"спортивная секция"}),
    ("quests", {"квест", "лазертаг"}),
    ("museums", {"музей", "музей-макет", "музей-заповедник", "кремль", "монастырь", "библиотека"}),
    ("science", {"музей науки"}),
    ("shows", {"театр", "цирк", "театр зверей", "концертный зал"}),
    ("cinema", {"кинотеатр"}),
    ("masterclass", {"мастерская", "мастер-класс"}),
    ("tours", {"экскурсия", "смотровая площадка", "прогулка"}),
    ("animals", {"зоопарк", "контактный зоопарк", "ферма", "конный клуб", "океанариум"}),
    ("water", {"аквапарк", "пляж"}),
    ("pools", {"бассейн"}),
    ("transport", {"железная дорога", "картинг"}),
    ("rinks", {"каток"}), ("sledding", {"горка"}), ("ski", {"горнолыжный курорт"}),  # 11.11: «Зима» расформирована
    ("food", {"кафе", "ресторан"}),
]
# где почти всегда проводят детские праздники
BDAY_CATS = {"playcenters", "trampolines", "quests", "masterclass", "ropes", "climbing", "karting"}


def classify(pid, types, tags, name):
    if pid in OVERRIDE:
        cats = list(OVERRIDE[pid])
    else:
        cats = [c for c, ts in TYPES if ts & types]
        if "VR" in name or "Аэротруба" in name:
            cats = ["quests"] if "VR" in name else ["amusement"]
    SPORT = [("martial", r"самбо|дзюдо|борьб|карат|тхэквон|бокс|айкидо|единоборств|ушу|кикбокс"),
             ("football", r"футбол|мини-футбол|школа мяча"), ("padel", r"падел|padel"), ("badminton", r"бадминтон"), ("racket", r"теннис|сквош"),
             ("gymnastics", r"гимнаст|акробат|спортивн\w* гимн|батут.*секц"), ("ballgames", r"баскетбол|волейбол"),
             ("hockey", r"хокке|фигурн"), ("chess", r"шахмат|шашк")]
    if "sport" in cats or "спортивная секция" in types:
        for c, rx in SPORT:
            if re.search(rx, name, re.I):
                cats = [c] + [x for x in cats if x != "sport"]
                break
    if re.search(r"[Тт]анц|[Бб]алет|[Dd]ance", name):
        cats = ["dance"] + [c for c in cats if c != "sport"]
    if "animals" not in cats and "животные" in tags and not ({"парк", "детская площадка"} & types):
        cats.append("animals")
    if "transport" not in cats and "машины и транспорт" in tags and ({"музей"} & types):
        cats.append("transport")
    if "museums" in cats and "science" not in cats and "наука и опыты" in tags:
        cats.append("science")
    out = []
    for c in cats:
        if c not in out:
            out.append(c)
    return out


wb = openpyxl.load_workbook(SRC); ws = wb["Места"]
hdr = [c.value for c in ws[1]]
for col in ("Категории", "День рождения"):
    if col not in hdr:
        ws.cell(row=1, column=len(hdr) + 1, value=col); hdr.append(col)
ci = {n: i + 1 for i, n in enumerate(hdr)}
from collections import Counter
cnt = Counter(); bd = 0; empty = []
for r in range(2, ws.max_row + 1):
    pid = ws.cell(r, ci["id"]).value
    if not pid:
        continue
    types = {t.strip() for t in str(ws.cell(r, ci["Тип"]).value or "").split(",") if t.strip()}
    tags = {t.strip().lower() for t in str(ws.cell(r, ci["Теги интересов"]).value or "").split(",") if t.strip()}
    name = ws.cell(r, ci["Название"]).value or ""
    cur_cats = ws.cell(r, ci["Категории"]).value
    cats = [c.strip() for c in cur_cats.split(",")] if (cur_cats and pid not in OVERRIDE) else classify(pid, types, tags, name)
    if not cats:
        empty.append((pid, types))
    ws.cell(r, ci["Категории"]).value = ", ".join(cats)
    plus = str(ws.cell(r, ci["Плюс"]).value or "") + " " + name
    is_bd = bool(BDAY_CATS & set(cats)) or ("food" in cats and re.search(r"аниматор|праздник|день рожд|детск", plus, re.I) is not None) \
        or bool(re.search(r"дн[ия] рожд|праздник", plus, re.I))
    cur = ws.cell(r, ci["День рождения"]).value
    if cur not in ("да", "нет"):
        ws.cell(r, ci["День рождения"]).value = "да" if is_bd else None
    if ws.cell(r, ci["День рождения"]).value == "да":
        bd += 1
    cnt.update(cats)
wb.save(SRC)
print(dict(cnt)); print("дни рождения:", bd); print("без категории:", empty)
