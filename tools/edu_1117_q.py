"""Робот edu 12.11 (седьмой запуск): запросы OSM edu17-<N> по отобранным карточкам → auto/osm-queries.json.
Центр запроса — станция/город района выдачи (или ближайшая к адресу станция), радиус 9 км; здания фильтруются по улице."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(os.path.join(ROOT, "tools/edu_1117_ext.json")))
D = {n: (a, b) for n, a, b in MET}
TOWN = {"Ногинск": (55.8526, 38.4381), "Лобня": (56.0129, 37.4748), "Дмитров": (56.3446, 37.5203)}
NEAR = {95: "Бибирево", 7: "Некрасовка", 98: "Некрасовка", 102: "Некрасовка", 64: "Профсоюзная", 143: "Сокольники", 108: "Лухмановская"}
NAME = {95: "адаптивн", 99: "АВС", 180: "АВС", 81: "Маяк", 149: "НСМ", 141: "НеоКидс", 115: "3D", 190: "коррекции речи", 39: "Мир ощущений",
        64: "Мелфоник", 143: "БукваРиУМ", 18: "Китенок", 7: "Инклюзия", 93: "Смарт", 108: "коррекции речи", 185: "нейропсихолог",
        193: "Альф", 37: "Истомин", 123: "академия речи", 176: "академия речи", 148: "коррекции речи", 1: "Нейрофитнес",
        35: "Яркие дети", 36: "Первый диалог", 40: "К.И.Д.С", 46: "Тесла", 57: "Студия знаний", 98: "Совёнок", 102: "Инженерия",
        112: "Я мир", 118: "Лэнди", 132: "Montessori", 134: "Монтессори", 156: "Юнисити", 173: "Инжинириум", 177: "IQ лого",
        207: "Ориентир", 208: "Школа для малышей", 219: "Бритландия", 222: "Прогресс", 225: "Логодом", 228: "Радужная зебра",
        233: "Генезис", 192: "Уникум", 232: "Логопед", 224: "IQ007"}
KW = r"(ул\.|улица|пр-т|просп\.|проспект|ш\.|шоссе|пер\.|бул\.|бульвар|наб\.|пр\.|проезд)"
def core(st):
    return re.sub(r"\s*\b(ул\.|улица|пр-т|просп\.|проспект|ш\.|шоссе|пер\.|бул\.|бульвар|наб\.|пр\.|проезд)\s*", " ", st).strip().replace("ё", "е")
Q = []
for n, nm in NAME.items():
    o = E[str(n)]; a = o["addr"][0]
    st = next((p.strip() for p in a.split(",") if re.search(KW, p)), None)
    area = o["q"].split(" метро ")[-1] if " метро " in o["q"] else next(t for t in TOWN if o["q"].endswith(t))
    lat, lon = TOWN[area] if area in TOWN else D[NEAR.get(n, area)]
    q = {"id": f"edu17-{n}", "lat": lat, "lon": lon, "radius": 9000, "name": nm}
    if st: q["street"] = core(st).split(" ")[-1] if core(st).startswith(("1-", "2-", "4-", "Большая", "Старая")) else core(st)
    Q.append(q)
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("edu17-")]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    for q in Q: print(q["id"], q["name"], q.get("street"))
