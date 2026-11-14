"""Точки мест робота sections 14.11 (1114a). Справка OSM с поиском по всему городу оказалась слишком тяжёлой (osm_query.py
работал 20 минут и тормозил остальных роботов), поэтому запросы sec14a сняты. Места добавляются с ПРИМЕРНОЙ точкой — центр
города/района из адреса (такие точки скрыты с карты); дом по адресу строго (улица + номер) находит osm-local.yml
(pipeline/osm_address.py, ищет здание в 8 км от точки), вход и точку организации — yandex-entrances.yml. Точку в реестр проверок
не пишем. python3 tools/sections_1114a_pick.py → tools/sections_1114a_points.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = os.path.join(ROOT, "tools", "sections_1114a_points.json")
if os.path.exists(P): os.remove(P)
from add_sections_1114a import SPEC
ST = {n: (a, b) for n, a, b in MET}
TOWN = [("Химки, мкр Сходня", 55.950, 37.300), ("Химки, мкр Планерная", 55.918, 37.335), ("Химки", 55.889, 37.440),
        ("Балашиха, мкр Авиаторов", 55.763, 37.980), ("Балашиха", 55.796, 37.938), ("Реутов", 55.760, 37.857),
        ("Мытищи г.о., д. Беляниново", 55.935, 37.680), ("Мытищи", 55.910, 37.736), ("Люберцы", 55.676, 37.893),
        ("Котельники", 55.660, 37.860), ("Электросталь", 55.784, 38.445), ("Домодедово", 55.437, 37.766),
        ("Серпухов", 54.913, 37.416), ("Щёлково", 55.920, 37.997), ("Раменское", 55.567, 38.230),
        ("Долгопрудный", 55.938, 37.510)]
MOS = {"Полярная ул.": "Медведково", "ул. Генерала Белова": "Домодедовская"}
PT = {}
for s in SPEC:
    pid, addr = s[0], s[6]
    for t, a, b in TOWN:
        if addr.startswith(t):
            PT[pid] = [a, b, f"примерно (центр: {t}; дом по адресу найдёт osm-local)", "примерно"]; break
    else:
        st = next(v for k, v in MOS.items() if addr.startswith(k))
        a, b = ST[st]
        PT[pid] = [a, b, f"примерно (у метро {st}; дом по адресу найдёт osm-local)", "примерно"]
json.dump(PT, open(P, "w"), ensure_ascii=False, indent=1)
print(len(PT), "из", len(SPEC))
