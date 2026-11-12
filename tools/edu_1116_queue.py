"""Робот edu, 12.11 (шестой запуск): выдачи Яндекс Карт по районам → auto/fetch-queue.txt (ключи eu<N>-1116e)."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Зорге", "Зюзино", "Зябликово", "Измайлово", "Измайловская", "Калужская", "Кантемировская", "Каховская",
         "Каширская", "Китай-город", "Кленовый бульвар", "Кожуховская", "Серпухов", "Орехово-Зуево", "Раменское", "Сергиев-Посад"]
TOWNS = {"Серпухов", "Орехово-Зуево", "Раменское", "Сергиев-Посад"}
TH = ["монтессори", "центр раннего развития", "подготовка к школе", "английский для детей", "робототехника для детей",
      "детский логопед", "ЛФК для детей", "детский нейропсихолог"]
Q = []
for i, a in enumerate(AREAS):
    for j in range(3):
        t = TH[(3 * i + j) % 8]
        Q.append(f"{t} {a.replace('-', ' ')}" if a in TOWNS else f"{t} метро {a}")
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1116e&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1116_queries.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
