"""Робот pools 14.11 (11 UTC), шаг 4: сайты кандидатов и уточняющие поиски Яндекс Карт (ключ pc<N>=1114k) → auto/fetch-queue.txt,
справка OSM (pl33-*) → auto/osm-queries.json.   python3 tools/pools_1114k_siteq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pc%d=1114k&text=%s"
LINES = ["https://xn--5-9tbac5d.xn--p1ai/", "https://na-volne.su/price", "https://na-volne.su/pools", "https://okeanika-swim.com/moscow",
         "https://artisticsport.ru/kontakty/", "https://artisticsport.ru/filialy/", "https://swim-school-1.ru/zanyatiya-dlya-detey-3-6-let"]
for i, q in enumerate(["Na VoL. Ne плавательный клуб, Москва, Фрязевская ул., 13А", "Na VoL. Ne плавательный клуб, Москва, Косинская ул., 12Б",
                       "Na VoL. Ne плавательный клуб Звенигород санаторий Звенигород", "Артистик клуб синхронного плавания",
                       "Артистик синхронное плавание для детей бассейн", "Океаника школа плавания Измайлово",
                       "Пять утят детский бассейн Малая Филёвская 30 цены", "Плыви, малыш Аква-садик Мичуринский проспект 16 бассейн для детей",
                       "Школа спортивно-оздоровительного плавания, Москва, Рублёвское ш., 48/1"]):
    LINES.append(Y % (i, urllib.parse.quote(q)))
OSM = [{"id": "pl33-navolne-fryazevskaya", "lat": 55.7610, "lon": 37.8310, "radius": 1200, "name": "Олимпия", "street": "Фрязевская"},
       {"id": "pl33-shsop-rublevskoe-48", "lat": 55.7600, "lon": 37.4100, "radius": 1500, "name": "M&G", "street": "Рублёвское"},
       {"id": "pl33-ss1-ranhigs-sadovniki", "lat": 55.6790, "lon": 37.6570, "radius": 1000, "name": "бассейн", "street": "Садовники"}]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in LINES if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    json.dump(old + [q for q in OSM if q["id"] not in have], open(p, "w"), ensure_ascii=False, indent=1)
    print(len(LINES))
