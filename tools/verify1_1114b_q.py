"""Смена verify-1 14.11 (~16 UTC): карточки Яндекс Карт мест очереди (ключ v1q<N>=1114b), сайты, справка OSM (verify-1-*).
python3 tools/verify1_1114b_q.py /path/q.json"""
import json, os, sys, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITES = ["https://www.kant.ru/tubing/", "https://www.kant.ru/contacts/", "https://mirax-park.com/infrastructure/zoopark/",
 "https://www.winzavod.ru/", "https://www.winzavod.ru/contacts/", "https://lionsland.ru/", "https://lionsland.ru/contacts",
 "https://www.ecobiocentre.ru/", "https://mori-cinema.ru/cinema_detail/82_mytishchi", "https://karofilm.ru/theatres/30",
 "https://formulakino.ru/", "https://kinomax.ru/", "https://www.luzhniki.ru/excursions/", "https://www.luzhniki.ru/contacts/",
 "https://victorymuseum.ru/", "https://www.vdnh.ru/", "https://www.vdnh.ru/contacts/", "https://www.mosdvorec.ru/",
 "https://fungrad.ru/", "https://masterpaninpark.ru/", "https://zilcc.ru/", "https://zilcc.ru/contacts/",
 "https://claustrophobia.com/quest/smeshariki", "https://www.ato-teatr.ru/", "https://bapark.ru/", "https://liapark.ru/",
 "https://www.swimrocket.ru/bassein-sk-volna/", "https://www.swimrocket.ru/bassein-yuzhnoportovyy/", "https://kido.center/",
 "https://kolomnakremlin.ru/", "https://www.kolomnagrad.ru/"]
OSM = [
 {"id": "verify-1-chg-tomilinsky-lesopark", "lat": 55.604394, "lon": 37.963134},
 {"id": "verify-1-fd-borovskoe-43", "lat": 55.639606, "lon": 37.356871, "name": "Fitness Дети"},
 {"id": "verify-1-akairyukan-dojo-gabrichevskogo", "lat": 55.812026, "lon": 37.453518, "name": "айкидо"},
 {"id": "verify-1-ten-dance-korolev", "lat": 55.935878, "lon": 37.836818, "name": "Ten Dance"},
 {"id": "verify-1-vdnh-fantastic-city", "lat": 55.833238, "lon": 37.635708, "name": "Фантастический город"},
 {"id": "verify-1-skazkin-dom", "lat": 55.704948, "lon": 37.642377, "name": "Сказкин дом"},
 {"id": "verify-1-filatov-lug-park", "lat": 55.601635, "lon": 37.409637, "name": "Филатов"},
 {"id": "verify-1-lt-kobra", "lat": 55.774244, "lon": 37.746389, "name": "Кобра"},
 {"id": "verify-1-lib-smart-krylatskoe", "lat": 55.76486, "lon": 37.410483, "name": "библиотека"},
 {"id": "verify-1-lib-shevchenko", "lat": 55.737367, "lon": 37.516363, "name": "библиотека"},
 {"id": "verify-1-quest-smeshariki", "lat": 55.789967, "lon": 37.531024, "name": "Клаустрофобия"},
 {"id": "verify-1-master-panin", "lat": 55.730801, "lon": 37.538468, "name": "Мастер Панин"},
 {"id": "verify-1-cin-budapest", "lat": 55.89727, "lon": 37.604648, "name": "Будапешт"},
 {"id": "verify-1-cin-gorizont", "lat": 55.728111, "lon": 37.584349, "name": "Горизонт"},
 {"id": "verify-1-tour-luzhniki-stadium", "lat": 55.715657, "lon": 37.553622, "name": "Лужники"},
 {"id": "verify-1-mc-vinzavod", "lat": 55.755994, "lon": 37.665104, "name": "Винзавод"},
 {"id": "verify-1-ato-theatre", "lat": 55.791359, "lon": 37.808819, "name": "АТО"},
 {"id": "verify-1-ecobiocentre", "lat": 55.820211, "lon": 37.671618, "name": "эколого"},
 {"id": "verify-1-swimrocket-volna-chertanovskaya", "lat": 55.607191, "lon": 37.593563, "name": "Волна"},
 {"id": "verify-1-swimrocket-yuzhnoportovy", "lat": 55.70124, "lon": 37.683126, "name": "бассейн"},
 {"id": "verify-1-kido-skandinavsky", "lat": 55.554667, "lon": 37.513183, "name": "Kido"},
]
if __name__ == "__main__":
    t = open(sys.argv[1]).read(); q = json.loads(t[:t.rindex("]") + 1])
    lines = list(SITES)
    for i, x in enumerate(q):
        s = x["name"].split("(")[0].strip() + ", " + (x.get("address") or "")
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?v1q%d=1114b&text=%s" % (i, urllib.parse.quote(s)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = json.load(open(p)); have = {x["id"] for x in old}
    new = [dict(o, radius=150, geom=True) for o in OSM if o["id"] not in have]
    json.dump(old + new, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(lines), len(new))
