"""Робот fun, 13.11 (запуск 1113b): выдачи Яндекс Карт по 15 районам второго круга (ключи fwa<N>-1113b) и
поиск комнат матери и ребёнка в крупных ТЦ (fwb<N>-1113b) → auto/fetch-queue.txt."""
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
        t = T[(3 * i + k) % 5]
        Q.append({"area": a, "theme": t, "text": f"{t} метро {a}" if a in metro else f"{t} {a}"})
MALLS = ["ТЦ Метрополис", "ТРЦ Атриум", "ТРЦ Авиамолл", "ТРК Vegas Каширское шоссе", "МЕГА Белая Дача",
         "ТРЦ Июнь Мытищи", "ТЦ Город Рязанка", "ТРЦ Весна Алтуфьево", "ТРЦ Каширская Плаза", "ТРЦ Зеленопарк",
         "ТРЦ Калейдоскоп Сходненская", "ТРЦ Бутово Молл", "ТРЦ Саларис", "ТЦ Цветной", "ТРЦ Семёновский",
         "ТРЦ Гранд Каньон", "ТРЦ Рио Ленинский проспект", "ТЦ Капитолий Марьина Роща", "ТРЦ XL Мытищи",
         "ТРЦ Вегас Кунцево", "ТРЦ Город Косино", "ТРЦ Мари", "ТРЦ Оранжевый Пушкино", "ТРЦ Отрада Красногорск",
         "ТРЦ Ашан Сити Капитолий", "ДЕПО Москва Лесная", "ТЦ Гранд Химки", "ТРЦ Новомосковский", "ТРЦ Лефортово Молл"]
QB = [{"mall": m, "text": f"комната матери и ребенка {m}"} for m in MALLS]
if __name__ == "__main__":
    json.dump({"areas": AREAS, "q": Q, "qb": QB}, open(os.path.join(ROOT, "tools/fun_1113b_queries.json"), "w"),
              ensure_ascii=False, indent=0)
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwa{n}=1113b&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(Q)]
    urls += [f"{base}fwb{n}=1113b&text=" + urllib.parse.quote(q["text"]) for n, q in enumerate(QB)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(AREAS, len(urls))
