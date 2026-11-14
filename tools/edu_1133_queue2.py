"""Робот edu, 14.11 (двадцать третий запуск), волна 2 — только «Особым детям»: выдачи Яндекс Карт (ключи eu<N>-1133f)."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
from edu_1133_queue import METRO, TOWNS
INC2 = ["АФК для детей с инвалидностью", "иппотерапия", "инклюзивный театр для детей", "сенсорная интеграция для детей",
        "центр для особых детей", "адаптивное плавание для детей с ОВЗ", "АВА-терапия", "занятия для детей с ДЦП"]
Q = []
for i, a in enumerate(METRO + TOWNS):
    w = f"метро {a}" if a in METRO else a
    for t in (INC2[i % len(INC2)], INC2[(i + 3) % len(INC2)]):
        Q.append(f"{t} {w}")
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1133f&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1133_queries2.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
