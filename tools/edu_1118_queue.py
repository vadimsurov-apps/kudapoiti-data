"""Робот edu, 12.11 (восьмой запуск): выдачи Яндекс Карт по районам → auto/fetch-queue.txt (ключи eu<N>-1118e).
По 2 запроса «Особым детям» + 2 по развитию/специалистам на район."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Корниловская", "Котельники", "Красные ворота", "Крестьянская застава", "Кропоткинская", "Крылатское", "Крымская",
         "Кузнецкий мост", "Курская", "Кутузовская", "Ленинский проспект", "Лермонтовский проспект", "Клин", "Чехов", "Егорьевск"]
TOWNS = {"Клин", "Чехов", "Егорьевск"}
INC = ["занятия для детей с ОВЗ", "инклюзивный центр для детей", "адаптивная физкультура для детей",
       "занятия для детей с аутизмом", "сенсорная интеграция для детей"]
TH = ["монтессори", "центр раннего развития", "подготовка к школе", "английский для детей", "робототехника для детей",
      "детский логопед", "ЛФК для детей", "детский нейропсихолог"]
Q = []
for i, a in enumerate(AREAS):
    for t in (INC[(2 * i + 1) % 5], INC[(2 * i + 2) % 5], TH[(2 * i + 3) % 8], TH[(2 * i + 4) % 8]):
        Q.append(f"{t} {a}" if a in TOWNS else f"{t} метро {a}")
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1118e&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1118_queries.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
