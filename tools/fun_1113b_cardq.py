"""Робот fun 1113b: карточки организаций Яндекса для новых кандидатов (fwd-<ключ>-1113b) и комнат матери и ребёнка
в ТРЦ (fwc-<ключ>-1113b) → auto/fetch-queue.txt; справки OSM по ТРЦ → auto/osm-queries.json."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {
 "piggy": "Пигги Плейс, Москва, Профсоюзная ул., 7/12",
 "nochleg": "Ночлег квесты, Москва, ул. Дмитрия Ульянова, 32",
 "kvestern": "Квестерн, Москва, ул. Кедрова, 6, корп. 1",
 "imerscape": "Имерскейп, Москва, ул. Кржижановского, 8, корп. 2",
 "qreality": "QuestReality, Москва, просп. Мира, 79",
 "hogwarts": "Тайны Хогвартса, Москва, Ключевая ул., 10, корп. 2",
 "vrreal": "VrRealTeam, Москва, Новокосинская ул., 22",
 "vtemnote": "Прятки от Втемноте, Москва, просп. Вернадского, 11/19",
 "miniland": "Miniland, посёлок Внуково, 2-я Рейсовая ул., 2, корп. 5",
 "bublik": "Бублик игровая комната, Подольск, Комсомольская ул., 24",
 "oasis": "Oasis Vr Club, Подольск, Советская площадь, 3",
 "nedetskie": "Недетские Прятки, Подольск, просп. Ленина, 132",
 "wonderland": "Wonderland, Королёв, Пионерская ул., 15, корп. 2",
 "happykids": "Хэппи Кидс, Химки, Ленинский просп., 24",
 "forsazh": "Форсаж на кухне, Химки, Молодёжная ул., 3А",
 "rotang": "Мастер класс из ротанга, Москва, Абрамцевская ул., 30, стр. 3",
 "vitrazh": "Витражная, Москва, 3-я Мытищинская ул., 16, стр. 3",
 "terrart": "Территория искусства, Москва, Староалексеевская ул., 4",
 "chashka": "Чашка, Королёв, просп. Космонавтов, 34Б",
 "schastye": "Счастье мастер-классы, Королёв, ул. Академика Легостаева, 8",
 "dolzhikova": "Творческая студия Ольги Должиковой, Химки, Ленинский просп., 22",
 "molekula": "Молекула, Королёв, просп. Космонавтов, 34Б",
}
C = {
 "salaris": "Комната матери и ребенка, Москва, Киевское шоссе, 23-й км, 1, Саларис",
 "kuzminki": "Комната матери и ребенка, Москва, Зеленодольская ул., 42, Кузьминки Молл",
 "botanica": "Комната матери и ребенка, Москва, ул. Вильгельма Пика, 11, Ботаника",
 "shchelk": "Комната матери и ребенка, Москва, Щёлковское шоссе, 75, Щёлковский",
 "vegaskash": "Комната матери и ребенка, МКАД 24-й километр, 1, Vegas",
}
MALLS = [("fun-1113b-salaris", 55.6262, 37.4234, "Саларис"), ("fun-1113b-kuzminki", 55.7012, 37.7643, "Кузьминки Молл"),
         ("fun-1113b-botanica", 55.8439, 37.6370, "Ботаника"), ("fun-1113b-shchelk", 55.8110, 37.7998, "Щёлковский"),
         ("fun-1113b-vegaskash", 55.5874, 37.7240, "Vegas")]
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwd-{k}=1113b&text=" + urllib.parse.quote(t) for k, t in D.items()]
    urls += [f"{base}fwc-{k}=1113b&text=" + urllib.parse.quote(t) for k, t in C.items()]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    q = os.path.join(ROOT, "auto/osm-queries.json")
    Q = json.load(open(q))
    Q += [{"id": i, "lat": la, "lon": lo, "radius": 300, "name": n, "geom": False} for i, la, lo, n in MALLS]
    json.dump(Q, open(q, "w"), ensure_ascii=False, indent=1)
    print(len(urls))
