"""Робот edu, 14.11 (двадцать второй запуск), вторая волна: только «Особым детям» (ключи eu<N>-1132f) — выдачи Яндекс Карт."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PL = ["Москва ЮАО", "Москва САО", "Москва ВАО", "Москва ЗАО", "Москва СВАО", "Москва ЮВАО", "Москва ЮЗАО", "Москва СЗАО", "Москва ЦАО",
      "Зеленоград", "Подольск", "Королёв", "Одинцово", "Люберцы", "Красногорск", "Химки", "Балашиха", "Мытищи", "Раменское", "Щёлково"]
T = ["АВА-терапия для детей с аутизмом", "адаптивная физкультура для детей с ОВЗ", "инклюзивная студия для детей", "иппотерапия для детей"]
Q = [f"{T[i % 4]} {p}" for i, p in enumerate(PL)] + [f"{T[(i + 1) % 4]} {p}" for i, p in enumerate(PL)]
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1132f&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1132_queries2.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
