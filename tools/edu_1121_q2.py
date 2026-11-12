"""Робот edu, 12.11 (одиннадцатый запуск): OSM edu21y-<N> по карточкам второго круга «Особым детям» (ey<N>-1121e) + сайты в очередь."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_batch14 import MET
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {n.lower().replace("ё", "е"): (a, b) for n, a, b in MET}
def st(n): return D[n.lower().replace("ё", "е")]
Q = [
 {"id": "edu21y-112", "lat": 55.8890, "lon": 37.4440, "radius": 3000, "name": "Тунейро", "street": "Марии Рубцовой"},
 {"id": "edu21y-113", "lat": 55.5920, "lon": 37.9850, "radius": 3000, "name": "Князьков", "street": "Баулинская"},
 {"id": "edu21y-6", "lat": 55.5920, "lon": 37.9850, "radius": 3000, "name": "Ава", "street": "Баулинская"},
 {"id": "edu21y-36", **dict(zip(("lat", "lon"), st("Нахимовский проспект"))), "radius": 1600, "name": "Альтера", "street": "Болотниковская"},
 {"id": "edu21y-92", **dict(zip(("lat", "lon"), st("Воробьёвы горы"))), "radius": 900, "name": "Дивные", "street": "Лужнецкая"},
 {"id": "edu21y-19", **dict(zip(("lat", "lon"), st("Новаторская"))), "radius": 1600, "name": "Здоровый", "street": "Новаторов"},
 {"id": "edu21y-24", **dict(zip(("lat", "lon"), st("Проспект Вернадского"))), "radius": 1300, "name": "Верное", "street": "Кравченко"},
 {"id": "edu21y-21", **dict(zip(("lat", "lon"), st("Некрасовка"))), "radius": 900, "name": "ABA", "street": "Рождественская"},
 {"id": "edu21y-118", **dict(zip(("lat", "lon"), st("Жулебино"))), "radius": 900, "name": "Ава", "street": "Авиаконструктора Миля"},
 {"id": "edu21y-32", **dict(zip(("lat", "lon"), st("Свиблово"))), "radius": 1000, "name": "Нейропсих", "street": "Снежная"},
 {"id": "edu21y-117", "lat": 55.6750, "lon": 37.8580, "radius": 2500, "name": "Ава", "street": "Авиаторов"},
 {"id": "edu21y-111", "lat": 55.5600, "lon": 37.7100, "radius": 3000, "name": "Здоровый", "street": "Зелёные Аллеи"},
 {"id": "edu21y-42", "lat": 55.6780, "lon": 37.2750, "radius": 3500, "name": "АВА", "street": "Вокзальная"},
 {"id": "edu21x-112", "lat": 55.67058, "lon": 37.44901, "radius": 900, "name": "Пиксель", "street": "Озёрная"},
 {"id": "edu21x-142", "lat": 55.776, "lon": 37.487, "radius": 1400, "name": "AcademKids", "street": "Новохорошёвский"},
 {"id": "edu21x-90", "lat": 55.682428, "lon": 37.650354, "radius": 700, "name": "Свой", "street": "Нагатинская"},
 {"id": "edu21x-113", "lat": 55.6630, "lon": 37.4800, "radius": 1000, "name": "Инжинириум", "street": "Покрышкина"},
]
SITES = ["divnyeribki.ru", "twoneiro.ru", "doctorknyazkov.ru", "zr-vidnoe.ru", "zr-moscow.ru", "abatherapymsk.ru", "abacw.ru",
         "neirocentr.ru", "altera-vita.ru", "yaizmenilsyaaba.ru", "abaplanet.ru", "v-sektre.ru"]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith(("edu21y-", "edu21x-1", "edu21x-9"))]
    json.dump(old + Q, open(p, "w"), ensure_ascii=False, indent=1)
    fq = os.path.join(ROOT, "auto/fetch-queue.txt")
    open(fq, "w").write("\n".join("https://" + s + "/" for s in SITES) + "\n" + open(fq).read())
    print(len(Q), len(SITES))
