"""Робот edu, 14.11 (двадцать шестой запуск), волна 3 — только «Особым детям» (ключи eu<N>-1136h): сенсорная интеграция/АВА/АФК по тем же
15 районам и по городам Подмосковья."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
from edu_1136_queue import METRO
INC = ["сенсорная интеграция для детей", "АВА терапия для детей", "логопед для детей с ОВЗ", "нейропсихолог для детей с ЗПР"]
Q = [f"{INC[i % 4]} метро {a}" for i, a in enumerate(METRO)] + [f"{INC[(i + 2) % 4]} метро {a}" for i, a in enumerate(METRO)]
for t in ("Балашиха", "Химки", "Мытищи", "Люберцы", "Подольск", "Королёв", "Красногорск", "Одинцово", "Раменское", "Пушкино", "Щёлково", "Зеленоград", "Видное", "Домодедово", "Сергиев Посад", "Ногинск", "Электросталь", "Долгопрудный", "Реутов", "Наро-Фоминск"):
    Q.append(f"центр для детей с ОВЗ {t}")
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1136h&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1136_queries3.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
