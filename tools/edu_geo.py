"""Робот edu, 14.11 (27-й запуск): локальный поиск здания OSM по адресу во всех уже выгруженных справках auto/osm-answers.json
(справка osm-query.yml с 12:13 14.11 не доходит: файл ответов > 100 МБ). Берём здание, только если улица (с типом) и номер дома
совпадают полностью и все такие здания лежат в одном месте (≤ 80 м) в нужном населённом пункте; иначе — нет точки.
Также ищем объект OSM с тем же названием в 150 м от здания (точка «объект»). geo(addr, name) → (lat, lon, accuracy_text) | None"""
import json, os, re, math
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AB = {"ул.": "улица", "просп.": "проспект", "бул.": "бульвар", "наб.": "набережная", "ш.": "шоссе", "пер.": "переулок", "пр.": "проезд",
      "б-р": "бульвар", "пл.": "площадь", "мкр.": "микрорайон", "пр-т": "проспект", "туп.": "тупик"}
TOWNC = {"Москва": (55.7558, 37.6173, 32000), "Зеленоград": (55.9890, 37.1990, 6000), "Коммунарка": (55.5700, 37.4870, 6000), "Троицк": (55.4850, 37.3050, 5000),
         "Балашиха": (55.7960, 37.9380, 9000), "Мытищи": (55.9116, 37.7308, 7000), "Люберцы": (55.6780, 37.8930, 6000), "Одинцово": (55.6780, 37.2700, 6000),
         "Химки": (55.8970, 37.4300, 8000), "Подольск": (55.4310, 37.5450, 8000), "Красногорск": (55.8200, 37.3300, 7000), "Королёв": (55.9220, 37.8540, 6000),
         "Пушкино": (56.0110, 37.8470, 6000), "Реутов": (55.7600, 37.8600, 3000), "Долгопрудный": (55.9380, 37.5000, 5000), "Серпухов": (54.9150, 37.4100, 8000),
         "Раменское": (55.5670, 38.2300, 6000), "Сергиев Посад": (56.3150, 38.1350, 7000), "Ногинск": (55.8530, 38.4400, 6000), "Лобня": (56.0130, 37.4800, 5000),
         "Чехов": (55.1430, 37.4550, 5000), "Орехово-Зуево": (55.8060, 38.9650, 6000), "Видное": (55.5530, 37.7100, 5000), "Щёлково": (55.9200, 37.9900, 6000),
         "Жуковский": (55.5970, 38.1200, 6000), "Электросталь": (55.7850, 38.4500, 6000), "Дмитров": (56.3440, 37.5200, 6000), "Котельники": (55.6600, 37.8600, 3000),
         "Дзержинский": (55.6300, 37.8500, 3000), "Лыткарино": (55.5800, 37.9000, 3000), "Ивантеевка": (55.9700, 37.9300, 3000), "Фрязино": (55.9600, 38.0500, 3000),
         "Наро-Фоминск": (55.3860, 36.7330, 6000), "Истра": (55.9150, 36.8600, 4000), "Домодедово": (55.4400, 37.7600, 8000), "Климовск": (55.3600, 37.5300, 4000), "Клин": (56.3330, 36.7300, 6000), "Егорьевск": (55.3830, 39.0350, 6000), "Солнечногорск": (56.1850, 36.9800, 5000), "Ступино": (54.8870, 38.0780, 6000)}
_I = None
def nst(s):
    s = (s or "").lower().replace("ё", "е")
    for a, b in AB.items(): s = re.sub(r"(^|\s)" + re.escape(a) + r"(?=\s|$)", r"\1" + b, s)
    return tuple(sorted(w for w in re.split(r"[\s.]+", s) if w and w != "имени"))
def osm_hn(t):
    t = (t or "").lower().replace(" ", "").replace("корпус", "к").replace("строение", "с").replace("стр.", "с").replace("к.", "к").replace("лит.", "")
    return t
def house(addr):
    parts = [p.strip() for p in addr.split(",")]
    hn = None; extra = ""
    for i, p in enumerate(parts):
        pp = p.replace(" ", "").replace("д.", "")
        if re.match(r"^\d+[А-Яа-яA-Za-z]?(/\d+[А-Яа-я]?)?([кс]\d+)*$", pp) and hn is None:
            hn = pp.lower()
            for q in parts[i + 1:i + 3]:
                m = re.match(r"(корп\.|стр\.|корпус|строение)\s*(\S+)", q)
                if m: extra += ("к" if m.group(1).startswith("корп") else "с") + m.group(2).lower()
    return (hn or "") + extra if hn else None
def street(addr):
    for part in addr.split(","):
        if re.search(r"(ул\.|улица|ш\.|шоссе|просп|пр-т|бул\.|бульвар|пер\.|переулок|наб\.|набережная|проезд|площадь|пл\.|Вал|тупик|аллея|микрорайон|мкр\.)", part):
            return nst(part.strip())
def town(addr):
    for t in TOWNC:
        if t != "Москва" and re.search(r"(^|, |посёлок |поселок |г\. )" + t + r"(,|$)", addr): return t
    if "Зеленоград" in addr: return "Зеленоград"
    if addr.startswith("Москва") or "Москва," in addr: return "Москва"
    return None
def dist(a, b, c, d): return math.hypot((a - c) * 111200, (b - d) * 111200 * math.cos(math.radians(a)))
def norm(s): return re.sub(r"[^a-zа-я0-9]", "", (s or "").lower().replace("ё", "е"))
def index():
    global _I
    if _I is None:
        A = json.load(open(os.path.join(ROOT, "auto/osm-answers.json")))
        B, P = {}, {}
        for a in A.values():
            for b in a.get("buildings", []):
                if b.get("addr:housenumber") and b.get("addr:street"):
                    B.setdefault((nst(b["addr:street"]), osm_hn(b["addr:housenumber"])), {})[b["osm"]] = b
            for p in a.get("pois", []):
                if p.get("name"): P[p["osm"]] = p
        _I = (B, list(P.values()))
    return _I
def geo(addr, name=None):
    B, P = index()
    t, st, hn = town(addr), street(addr), house(addr)
    if not (t and st and hn): return None
    c = TOWNC[t]
    bl = [b for b in B.get((st, hn), {}).values() if dist(b["lat"], b["lon"], c[0], c[1]) <= c[2]]
    if not bl: return None
    if any(dist(b["lat"], b["lon"], bl[0]["lat"], bl[0]["lon"]) > 80 for b in bl): return None
    b = bl[0]
    if name:
        nn = norm(re.sub(r"[«»\"]", "", name))
        for p in P:
            pn = norm(p["name"])
            if len(nn) >= 5 and pn and (nn in pn or pn in nn) and len(pn) >= 5 and dist(p["lat"], p["lon"], b["lat"], b["lon"]) <= 150:
                return (p["lat"], p["lon"], f'точно (объект: {p["osm"]}), OSM по названию «{p["name"]}» у здания {b["osm"]}, 14.11')
    return (b["lat"], b["lon"], f'точно (OpenStreetMap), здание {b["osm"]} по адресу {b.get("addr:street")}, {b.get("addr:housenumber")}')
if __name__ == "__main__":
    import sys
    for a in sys.argv[1:]: print(a, "→", geo(a))
