"""Робот edu, 14.11 (двадцать четвёртый запуск), волна 2 — только «Особым детям»: выдачи Яндекс Карт (ключи eu<N>-1134f)."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
from edu_1134_queue import METRO, TOWNS
INC2 = ["АФК для детей с инвалидностью", "сенсорная интеграция для детей", "центр для особых детей", "АВА-терапия",
        "занятия для детей с ДЦП", "инклюзивный клуб для детей", "коррекционные занятия для детей с ЗПР", "центр для детей с аутизмом",
        "адаптивное плавание для детей с ОВЗ", "инклюзивная творческая студия"]
Q = []
for i, a in enumerate(METRO + TOWNS):
    w = f"метро {a}" if a in METRO else a
    for t in (INC2[i % len(INC2)], INC2[(i + 3) % len(INC2)], INC2[(i + 6) % len(INC2)]):
        Q.append(f"{t} {w}")
Q += ["иппотерапия Москва", "иппотерапия для детей Московская область", "инклюзивный театр для детей Москва", "клуб для детей с синдромом Дауна Москва",
      "занятия для слабовидящих детей", "занятия для слабослышащих детей Москва", "адаптивная верховая езда для детей", "инклюзивный центр для детей Химки",
      "инклюзивный центр для детей Королёв", "центр для детей с аутизмом Подмосковье", "адаптивный спорт для детей Подольск", "сенсорная комната для детей Москва"]
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1134f&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1134_queries2.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
