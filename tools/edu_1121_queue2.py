"""Робот edu, 12.11 (одиннадцатый запуск), второй круг «Особым детям»: выдачи Яндекс Карт (ключи ew<N>-1121e) + повтор карточек,
которые не открылись в первом круге (ключи ex<n>-1121e — простой запрос «название, город»)."""
import json, os, re, urllib.parse
from edu_1121_queue import AREAS, TOWNS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = []
for a in AREAS:
    for t in ("АВА-терапия для детей", "центр для детей с РАС"):
        Q.append(f"{t} {a}" if a in TOWNS else f"{t} метро {a}")
Q += ["инклюзивный клуб для детей Москва", "адаптивная физкультура для детей с ОВЗ Москва", "иппотерапия для детей с ДЦП Подмосковье",
      "центр для особых детей Москва", "занятия для детей с синдромом Дауна Подмосковье", "инклюзивная студия рисования Москва",
      "сенсорная интеграция для детей Подмосковье", "АВА-терапия Подмосковье", "инклюзивный центр Подмосковье", "адаптивный спорт для детей Подмосковье"]
RETRY = [87, 74, 129, 217, 262, 13, 22, 40, 58, 119, 125, 171, 240, 100]
if __name__ == "__main__":
    K = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/edu_1121_keep.json")))}
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ew{n}=1121e&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    for n in RETRY:
        c = K[n]; a = c["addr"]
        town = next((t for t in ("Москва", "Красногорск", "Истра", "Дубна", "Воскресенск", "Ступино", "Зеленоград") if t in a), "Москва")
        hn = re.search(r"([А-Яа-яё\-\. ]+(ул\.|просп\.|ш\.|бул\.|пр\.|пер\.|наб\.)[^,]*|(ул\.|просп\.) [^,]+), (\d+[^,]*)", a)
        t = f'{c["name"]} {town}' + (f', {hn.group(1).strip()}, {hn.group(4)}' if hn else "")
        urls.append(f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ex{n}=1121e&text=" + urllib.parse.quote(t))
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1121_queries2.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
