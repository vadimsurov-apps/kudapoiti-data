"""Робот fun, 13.11 (запуск 1113c): выдачи Яндекс Карт по 15 районам второго круга (fwa<N>-1113c) и комнаты матери и
ребёнка в ТРЦ по адресу ТРЦ (fwc<N>-1113c) → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = json.load(open(os.path.join(ROOT, "auto/search-areas.json")))
P = json.load(open(os.path.join(ROOT, "auto/search-progress-fun.json")))
T = ["детский развлекательный центр", "квест для детей", "мастер-класс для детей", "музей для детей",
     "детская игровая комната"]
metro = [x for x in A["metro"] if P.get(x, "") <= "2026-11-11"][:12]
towns = [x for x in A["towns"] if P.get(x, "") <= "2026-11-11"][:3]
AREAS = metro + towns
Q = []
for i, a in enumerate(AREAS):
    for k in range(3):
        t = T[(3 * i + k + 1) % 5]
        Q.append({"area": a, "theme": t, "text": f"{t} метро {a}" if a in metro else f"{t} {a}"})
MALLS = {"metropolis": "Москва, Ленинградское ш., 16А, стр. 4", "atrium": "Москва, ул. Земляной Вал, 33",
         "aviamall": "Москва, Ходынский бул., 4", "iyun": "Мытищи, ул. Мира, 51",
         "ryazanka": "Москва, Рязанский просп., 2, корп. 2", "vesna": "Алтуфьевское шоссе, 1-й километр, 3, стр. 1",
         "kashplaza": "Москва, Каширское ш., 61Г", "zelenopark": "Ржавки, 2-й микрорайон, с20",
         "kaleid": "Москва, Сходненская ул., 56", "butovo": "Чечёрский пр., 51", "tsvetnoy": "Москва, Цветной бул., 15, стр. 1",
         "rio-len": "Москва, Ленинский просп., 109", "kapit-mr": "Москва, Шереметьевская ул., 20",
         "xl-myt": "Мытищи, Коммунистическая ул., 1", "kosino": "Москва, Святоозёрская ул., 1А",
         "otrada": "Отрадное, Пятницкое ш., 1, стр. 1", "evrop": "Москва, пл. Киевского Вокзала, 2",
         "novomosk": "Московский, ул. Хабарова, 2", "megabd": "Котельники, 1-й Покровский пр., 5",
         "vegas-kuntsevo": "56-й километр МКАД, 1", "mari": "Москва, ул. Перерва, 43", "okhotny": "Москва, Манежная пл., 1, стр. 2",
         "granat": "Москва, Ленинградский просп., 76А", "semen": "Москва, Большая Семёновская ул., 16",
         "orang": "Пушкино, Ярославское шоссе"}
if __name__ == "__main__":
    json.dump({"areas": AREAS, "q": Q, "malls": MALLS}, open(os.path.join(ROOT, "tools/fun_1113c_queries.json"), "w"),
              ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwa{n}=1113c&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(Q)]
    urls += [f"{base}fwc-{k}=1113c&text=" + urllib.parse.quote("Комната матери и ребенка, " + v) for k, v in MALLS.items()]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(AREAS, len(urls))
