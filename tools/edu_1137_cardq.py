"""Робот edu 14.11 (27-й запуск): карточки организаций кандидатов, для которых нашлось здание OSM (ключи ev<n>-1137e), + волна 2 выдач
(ещё 3 направления на каждый из 15 районов и «Особым детям» по округам Москвы, ключи eu<N>-1137g) → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def short(a):
    return re.split(r", (Метро|метро|этаж|подъезд|вход|Вход|офис|кабинет|помещ|домофон|жилой|ЖК|Отдельный|Пройдите|цокольный)", a)[0]
K = json.load(open(os.path.join(ROOT, "tools/edu_1137_keep.json")))
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{c['n']}=1137e&text=" + urllib.parse.quote(f'{c["name"]}, {short(c["addr"])}') for c in K if c["pt"]]
AREAS = ["метро Лихоборы", "метро Ломоносовский проспект", "метро Люблино", "метро Марьина Роща", "метро Марьино", "метро Маяковская", "метро Медведково",
         "метро Международная", "Серпухов", "Раменское", "Сергиев Посад", "Ногинск", "Лобня", "Чехов", "Орехово-Зуево"]
TH2 = ["лего студия для детей", "школа программирования для детей", "детский мини-сад", "обучение чтению дошкольников", "математика для детей",
       "ментальная арифметика для детей", "логопед дефектолог", "нейропсихолог для детей", "детский массаж ЛФК", "монтессори центр", "раннее развитие малышей",
       "английский для дошкольников", "робототехника", "подготовка к школе"]
Q3 = []
for i, a in enumerate(AREAS):
    for j in range(3): Q3.append(f"{TH2[(3 * i + j) % len(TH2)]} {a}")
for d in ("САО", "СВАО", "ВАО", "ЮВАО", "ЮАО", "ЮЗАО", "ЗАО", "СЗАО", "ЦАО"):
    Q3.append(f"занятия для детей с ОВЗ {d} Москва")
    Q3.append(f"центр для детей с аутизмом {d} Москва")
if __name__ == "__main__":
    urls += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1137g&text=" + urllib.parse.quote(q) for n, q in enumerate(Q3)]
    json.dump(Q3, open(os.path.join(ROOT, "tools/edu_1137_queries3.json"), "w"), ensure_ascii=False, indent=0)
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
