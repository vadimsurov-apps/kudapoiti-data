"""Точки мест робота rare 12.11 из справки OSM (auto/osm-answers.json, запросы rare12-*; копия ответа — tools/rare_1112_answers.json):
1) объект OSM с тем же названием (тот же дом или рядом со зданием по адресу) → «точно (объект: …)»;
2) иначе здание строго по адресу карточки (улица + номер дома/корпус/строение) — точка на вход этого здания, если вход
   есть в OSM (≤ 60 м), иначе центр здания. Нет совпадения — место не добавляется.
python3 tools/rare_1112_pick.py → tools/rare_1112_points.json"""
import json, os, re, math
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ANS = json.load(open(os.path.join(ROOT, "tools", "rare_1112_answers.json")))
# id места: (id запроса, адрес, имя объекта OSM для поиска среди pois или None)
Q = {
 "hockey-rus-mha-zyablikovo": ("hockey-rus-mha-zyablikovo", "Воронежская ул., 13", None),
 "hockey-star-kosino": ("hockey-star-kosino", "Новоухтомское ш., 2А", "Город"),
 "hockey-kharlamov-sokolniki": ("hockey-kharlamov-sokolniki", "ул. Сокольнический Вал, 1Б", "Ледовый дворец Сокольники"),
# «Снегирь Арена»: адреса «д. Марушкино, 2» нет в OSM (здание «ул. Связистов, 2» — не то) — не добавлено.
 "fk-volosozhar-sokolniki": ("fk-volosozhar-sokolniki", "ул. Сокольнический Вал, 1Б, стр. 2", None),
 "fk-morozovo-school": ("fk-morozovo-school", "Новоостаповская ул., 5, стр. 2", None),
 "rink-mayak-chertanovo": ("rink-mayak-yasenevo", "ул. Красного Маяка, вл28", None),
 "rink-kasatonov-korolev": ("rink-kasatonov-korolev", "Октябрьский бул., 10, стр. 1", None),
 "volley-sunvolley-novokuznetskaya": ("volley-sunvolley-novokuznetskaya", "Новокузнецкая ул., 16, стр. 10", None),
 "volley-krokodil-sokolniki": ("volley-krokodil-sokolniki", "ул. Сокольнический Вал, 1Б, стр. 4", None),
 "volley-rusvolley-zoologicheskaya": ("volley-rusvolley-zoologicheskaya", "Зоологическая ул., 28, стр. 1", None),
 "volley-rusvolley-krasina": ("volley-rusvolley-krasina", "ул. Красина, 20, стр. 1", None),
 "volley-rusvolley-ukrainsky": ("volley-rusvolley-ukrainsky", "Украинский бул., 9", None),
 "volley-rusvolley-bakhrushina": ("volley-rusvolley-bakhrushina", "ул. Бахрушина, 24, стр. 1", None),
 "volley-rusvolley-dubininskaya-42": ("volley-rusvolley-dubininskaya", "Дубининская ул., 42", None),
 "volley-rusvolley-krasnoselskaya": ("volley-rusvolley-krasnoselskaya", "Верхняя Красносельская ул., 30", None),
 "volley-rusvolley-saltykovskaya": ("volley-rusvolley-saltykovskaya", "Салтыковская ул., вл49", None),
 "ski-rodina-skhodnya": ("ski-rodina-skhodnya", "Овражная ул., 35", "Горнолыжная база Родина"),
}


def hn_of(addr):
    m = re.search(r",\s*(?:вл\.?\s*)?(\d+[А-Яа-я]?(?:/\d+)?)(?:,\s*(корп|стр)\.\s*(\w+))?", addr)
    if not m:
        return None
    h = m.group(1).lower()
    if m.group(2):
        h += ("к" if m.group(2) == "корп" else "с") + m.group(3).lower()
    return h


def osm_hn(t):
    t = (t or "").lower().replace(" ", "")
    for a, b in (("корпус", "к"), ("строение", "с"), ("стр.", "с"), ("стр", "с"), ("к.", "к"), ("с.", "с")):
        t = t.replace(a, b)
    return t


def d(a, b, c, e):
    return math.hypot((a - c) * 111320, (b - e) * 111320 * math.cos(math.radians(a)))


PT, MISS = {}, []
for pid, (qid, addr, nm) in Q.items():
    v = ANS.get("rare12-" + qid)
    if not v:
        MISS.append((pid, "нет ответа")); continue
    hn = hn_of(addr)
    bld = next((b for b in v["buildings"] if hn and osm_hn(b.get("addr:housenumber")) == hn), None)
    got = None
    if nm:
        for p in v["pois"]:
            if p.get("name") == nm or (p.get("match") and nm.lower() in p.get("name", "").lower()):
                if not p.get("addr:housenumber") or osm_hn(p["addr:housenumber"]) == (hn or "").split("с")[0].split("к")[0] or osm_hn(p["addr:housenumber"]) == hn:
                    got = (p["lat"], p["lon"], f'точно (объект: {p["osm"]} «{p.get("name")}»), OSM по названию, 12.11'); break
    if not got and bld:
        ent = [e for e in v.get("entrances", []) if d(e["lat"], e["lon"], bld["lat"], bld["lon"]) <= 60]
        if ent:
            e = min(ent, key=lambda e: d(e["lat"], e["lon"], bld["lat"], bld["lon"]))
            got = (e["lat"], e["lon"], f'точно (OpenStreetMap), вход {e["osm"]} здания {bld["osm"]} по адресу {bld.get("addr:street")}, {bld.get("addr:housenumber")}')
        else:
            got = (bld["lat"], bld["lon"], f'точно (OpenStreetMap), здание {bld["osm"]} по адресу {bld.get("addr:street")}, {bld.get("addr:housenumber")}')
    if got:
        PT[pid] = got
    else:
        MISS.append((pid, hn, sorted({osm_hn(b.get("addr:housenumber")) for b in v["buildings"]})[:30]))
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1112_points.json"), "w"), ensure_ascii=False, indent=1)
print("точек:", len(PT), "нет:", len(MISS))
for k, v in PT.items():
    print(" ", k, v[2])
for m in MISS:
    print(" НЕТ", m)
