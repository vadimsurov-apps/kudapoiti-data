"""Робот rare 13.11 (1113f): справка OSM (rare13i-*) для бесплатных катков «Московских сезонов» и катков в парках
(список адресов сезона 2025/26 — auto/pages vfokuse.mail.ru …69210990). Ищем объект «Каток» рядом с адресом.
python3 tools/rare_1113f_osmq.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (lat, lon, radius, имя для сверки, улица OSM)
Q = {
 "rink-ms-brateevo": (55.6319, 37.7624, 500, "Каток", "Ключевая"),
 "rink-ms-brigantina": (55.835, 37.522, 700, "Каток", ""),
 "rink-ms-matveevskaya": (55.7055, 37.487, 700, "Каток", "Матвеевская"),
 "rink-ms-olimpiyskaya-derevnya": (55.676, 37.468, 700, "Каток", ""),
 "rink-ms-zelenograd-16": (55.9785, 37.165, 1200, "Каток", ""),
 "rink-ms-veshnyaki": (55.725, 37.818, 700, "Каток", "Вешняковская"),
 "rink-ms-golyanovo": (55.8115, 37.8075, 700, "Каток", "Уральская"),
 "rink-ms-svyatoozerskaya": (55.714248, 37.879945, 500, "Каток", ""),
 "rink-ms-gorodetskaya": (55.744, 37.866, 900, "Каток", ""),
 "rink-ms-tsimlyanskaya": (55.6735, 37.7645, 800, "Каток", "Цимлянская"),
 "rink-ms-nekrasovka": (55.703, 37.925, 1200, "Каток", ""),
 "rink-ms-ploshchad-slavy": (55.705, 37.776, 800, "Каток", ""),
 "rink-ms-profsoyuznaya-41": (55.670013, 37.55584, 500, "Каток", ""),
 "rink-ms-teply-stan": (55.6185, 37.506, 800, "Каток", ""),
 "rink-ms-admirala-rudneva": (55.542312, 37.527273, 500, "Каток", ""),
 "rink-ms-khachaturyana": (55.8615, 37.6, 900, "Каток", ""),
 "rink-ms-sukhonskaya": (55.8775, 37.652, 700, "Каток", "Сухонская"),
 "rink-ms-grekova": (55.8875, 37.658, 800, "Каток", "Грекова"),
 "rink-ms-serebryakova": (55.8525, 37.6505, 700, "Каток", ""),
 "rink-ms-startovaya": (55.874, 37.708, 700, "Каток", "Стартовая"),
 "rink-ms-kurkino": (55.8945, 37.3985, 900, "Каток", ""),
 "rink-ms-aviatsionnaya": (55.8085, 37.4645, 600, "Каток", ""),
 "rink-vorobyovy-gory-kosygina": (55.702321, 37.553563, 700, "Каток", ""),
 "rink-severny-rechnoy-park": (55.851, 37.4655, 900, "Каток", ""),
 "rink-ostankino-park": (55.824358, 37.60812, 900, "Каток", ""),
 "rink-bolotnaya": (55.7455, 37.6205, 600, "Каток", ""),
 "pumptrack-svobody-53": (55.8605, 37.4355, 800, "памп", "Свободы"),
 "pumptrack-gastello-26": (55.7865, 37.6835, 800, "памп", "Гастелло"),
 "pumptrack-orekhovy-24": (55.6115, 37.7275, 900, "памп", "Ореховый"),
}
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("rare13i-")]
    out = []
    for k, (la, lo, r, nm, st) in Q.items():
        q = {"id": "rare13i-" + k, "lat": la, "lon": lo, "radius": r, "name": nm}
        if st: q["street"] = st
        out.append(q)
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out))
