"""Робот rare 14.11 (1114a): справка OSM (rare14a-*) по кандидатам → auto/osm-queries.json.  python3 tools/rare_1114a_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {  # id: (lat, lon, radius, имя, улица)
 "pump-chertanovo": (55.630, 37.600, 2500, "Памп", ""),
 "pump-kudrinka": (56.005, 37.862, 3500, "Памп", ""),
 "pump-dolgoprudny": (55.940, 37.510, 3000, "Памп", ""),
 "samolet-arena": (55.548, 37.455, 4500, "Самол", ""),
 "arenaplay-yug": (55.5706, 37.4765, 800, "Arena", "Монаховой"),
 "vershina-tsaritsyno": (55.609, 37.712, 1800, "Вершина", ""),
 "cska-manezh": (55.789, 37.555, 900, "ЦСКА", "Ленинградский"),
 "mosfilm-41k3": (55.7098, 37.5107, 350, "Мастера", "Мосфильмовская"),
 "olimp-fryazino": (55.960, 38.048, 900, "Олимп", "Комсомольская"),
 "arena-istra": (55.913, 36.860, 2500, "Арена", "Советская"),
 "borisoglebsky-ramenskoe": (55.567, 38.225, 3000, "Борисоглеб", "Махова"),
 "petruseva-pavposad": (55.782, 38.655, 3000, "Петрусев", "Покровская"),
 "nadezhda-pavposad": (55.782, 38.655, 3000, "Надежда", "Кирова"),
 "krasnogorsk-arena": (55.825, 37.330, 3000, "Арена", "Лесная"),
 "petrov-academy-krasnogorsk": (55.815, 37.340, 4000, "Петров", "Петровых"),
 "lider-volokolamsk": (56.030, 35.955, 4000, "Лидер", "Рижское"),
 "bobry-mytishchi": (55.980, 37.700, 4000, "Бобр", "Пионерская"),
 "nara-naro-fominsk": (55.390, 36.735, 3000, "Нара", "Воровского"),
 "total-volley-aprelevka": (55.550, 37.070, 3000, "Total", "Августовская"),
 "bauma-nakhabino": (55.8336, 37.1595, 500, "Баума", "Парковая"),
 "lucentr-starokirochny": (55.770, 37.682, 600, "", "Старокирочный"),
 "hurricane-sushchevsky": (55.795, 37.593, 500, "", "Сущёвский"),
}
p = os.path.join(ROOT, "auto/osm-queries.json")
q = [x for x in json.load(open(p)) if not x["id"].startswith("rare14a-")]
for k, (la, lo, r, nm, st) in Q.items():
    x = {"id": "rare14a-" + k, "lat": la, "lon": lo, "radius": r, "name": nm, "geom": True}
    if st: x["street"] = st
    q.append(x)
json.dump(q, open(p, "w"), ensure_ascii=False, indent=1)
print(len(Q), len(q))
