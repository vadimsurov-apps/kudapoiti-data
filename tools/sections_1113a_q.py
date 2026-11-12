"""Робот sections 12.11 (21 UTC, партия 1113a): запросы OSM sec13a-* (здание по улице из адреса карточки Яндекс Карт)
→ auto/osm-queries.json.  python3 tools/sections_1113a_q.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
M = {n: (a, b) for n, a, b in MET}
TOWN = {"Видное": (55.553, 37.709), "Королёв": (55.918, 37.850), "Юбилейный": (55.934, 37.835), "Опалиха": (55.814, 37.255)}
Q = {
 "effekt-vidnoe": ("Видное", "Ольховая", "Эффект"),
 "aerial-gym-vostochnaya": ("Автозаводская", "Восточная", "гимнаст"),
 "tsvetkov-karate-oktyabrsky": ("Марьина Роща", "Октябрьский", "каратэ"),
 "orlenok-judo-yubileyny": ("Юбилейный", "Лесная", "Орл"),
 "fight-zone-korolev": ("Королёв", "Октябрьский", "Fight"),
 "altis-tkd-korolev": ("Королёв", "Октябрьский", "Вымпел"),
 "shindo-tkd-korolev": ("Королёв", "Стадионная", "ШинДо"),
 "jungle-korolev-grabina": ("Королёв", "Грабина", "Jungle"),
 "bryksina-rg-opalikha": ("Опалиха", "Ахматовой", "Арена"),
 "attitude-koneva": ("Щукинская", "Конева", "школа"),
 "chg1-khoroshevskaya": ("Хорошёвская", "Хорошёвская", "гимнаст"),
 "fd-kashirskoe-67": ("Каширская", "Каширское", "FD"),
}
if __name__ == "__main__":
    out = []
    for pid, (c, st, nm) in Q.items():
        lat, lon = TOWN.get(c) or M[c]
        out.append({"id": "sec13a-" + pid, "lat": lat, "lon": lon, "radius": 5000, "name": nm, "street": st})
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("sec13a-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
