"""Точки мест робота rare 12.11 (22 UTC): справка OSM (auto/osm-answers.json, rare12z-*) — объект места (каток, ледовый дворец,
спорткомплекс по названию); для школ в здании, где у базы уже есть место с точкой «вход»/«объект», — та же точка.
Не нашлось объекта/здания по адресу (места НЕ добавлены): «Снайпер-select» и «Айс Групп» (Б. Филёвская ул., 22 с15 — в OSM только с16
за 1,3 км), «Разряд» (Филёвский бул., 38 — нет здания), «Монстр хоккея» (Балаклавский пр-т, 33 — в OSM только 33А),
школа Али Ишанова (Нижняя Красносельская, 40/12к4 — нет здания).
python3 tools/rare_1112z_pick.py → tools/rare_1112z_points.json"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto", "osm-answers.json")))
PT = {}


def obj(q, osm, what):
    a = A["rare12z-" + q]
    p = next(p for p in a["pois"] + a["buildings"] if p["osm"] == osm)
    return [p["lat"], p["lon"], f"точно (объект: {osm} {what}), OSM"]


PT["rink-kolomna-speed-center"] = obj("rink-kolomna-speed-center", "relation/18075818", "«Конькобежный центр «Коломна»», наб. реки Коломенки, 7")
PT["fk-curling-dmitrov"] = obj("fk-curling-dmitrov", "way/35399873", "«Центр фигурного катания и кёрлинга», Дмитров")
PT["rink-lobnya-ds"] = obj("rink-lobnya-ds", "node/2377965039", "«Ледовый каток» у Дворца спорта, Лобня, ул. Ленина, 65")
arena = obj("hockey-verkhovod-solntsevo", "way/993106697", "«Ледовая Арена Солнцево», ул. Авиаторов, 7А")
for k in ("hockey-verkhovod-solntsevo", "hockey-star-solntsevo", "hockey-snaiper-select-solntsevo", "fk-victory-skating-solntsevo"):
    PT[k] = arena
arkt = obj("hockey-star-novoorlovskaya", "node/12817684901", "ледовый дворец «Арктика», Новоорловская ул., 7В")
PT["hockey-star-novoorlovskaya"] = arkt
PT["hockey-dnk-novoperedelkino"] = arkt
PT["hockey-star-skhodnenskaya"] = obj("hockey-star-skhodnenskaya", "node/2056514868", "каток «Калейдоскоп» (ice_rink) в ТРЦ «Калейдоскоп», Сходненская ул., 56")
PT["hockey-star-tikhonovskaya"] = [55.802762, 37.686486, "точно (объект: OSM relation/11126282 «Спартак академия», Большая Тихоновская ул., 2), OSM; та же точка, что у spartak-hockey-sokolniki"]
PT["tt-planet-flotskaya"] = [55.853865, 37.496476, "точно (вход: OSM главный вход (entrance=main) здания way/376457689 ТРЦ «Флотилия», Флотская ул. 7 с1), OSM; та же точка, что у matsarr-activity-hall"]
json.dump(PT, open(os.path.join(ROOT, "tools", "rare_1112z_points.json"), "w"), ensure_ascii=False, indent=1)
for k, v in PT.items():
    print(k, v)
