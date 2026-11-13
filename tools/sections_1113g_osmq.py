"""Робот sections 13.11 (06 UTC, 1113g/1113h): запросы OSM sec13g-* (здание по улице из адреса источника) → auto/osm-queries.json.
python3 tools/sections_1113g_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = {
 "gladiator-taganskaya": (55.7407, 37.6560, "Таганская", "Гладиатор"),
 "gladiator-luganskaya": (55.6361, 37.6562, "Луганская", "Гладиатор"),
 "gladiator-marksistskaya": (55.7407, 37.6560, "Марксистская", "Гладиатор"),
 "gladiator-izyumskaya": (55.5481, 37.5527, "Изюмская", "Гладиатор"),
 "gladiator-kovshovoy": (55.6500, 37.4000, "Наташи Ковшовой", "Гладиатор"),
 "gladiator-obrucheva": (55.6567, 37.5400, "Обручева", "Гладиатор"),
 "gladiator-rudnevka": (55.7030, 37.8510, "Руднёвка", "Гладиатор"),
 "gladiator-vernadskogo": (55.6880, 37.5200, "Вернадского", "Гладиатор"),
 "tkd-yug-sholokhova": (55.6397, 37.3552, "Шолохова", "Тхэквондо"),
 "tkd-yug-lukinskaya": (55.6397, 37.3552, "Лукинская", "Тхэквондо"),
 "tkd-yug-bromley": (55.6012, 37.4080, "Братьев Бромлей", "Тхэквондо"),
 "husky-basket-latsisa": (55.8597, 37.4368, "Вилиса Лациса", "Хаски"),
 "mon-svobody": (55.8550, 37.4400, "Свободы", "Мон"),
 "dobrynya-svobody": (55.8550, 37.4400, "Свободы", "Добрыня"),
 "footballmsk-zhivopisnaya": (55.8094, 37.4632, "Живописная", "футбол"),
 "footballmsk-peschanaya": (55.7920, 37.5100, "3-я Песчаная", "футбол"),
 "footballmsk-novozavodskaya": (55.7468, 37.5140, "Новозаводская", "футбол"),
 "footballmsk-razumovskaya": (55.7920, 37.5600, "Петровско-Разумовская", "футбол"),
 "footballmsk-ostrovityanova": (55.6319, 37.5192, "Островитянова", "футбол"),
 "footballmsk-yaroslavskaya": (55.8200, 37.6400, "Ярославская", "футбол"),
 "musa-tkd-leninsky": (55.6459, 37.4725, "Ленинский", "Муса"),
 "mir-edinoborstv-polyany": (55.5380, 37.5100, "Поляны", "Мир единоборств"),
 "tigry-tkd-izyumskaya": (55.5481, 37.5527, "Изюмская", "Тигры"),
 "baglay-aerial-tushinskaya": (55.8255, 37.4370, "Тушинская", "Баглай"),
}
if __name__ == "__main__":
    out = [{"id": "sec13g-" + k, "lat": a, "lon": b, "radius": 5000, "name": nm, "street": st} for k, (a, b, st, nm) in Q.items()]
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("sec13g-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
