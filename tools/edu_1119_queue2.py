"""Робот edu, 12.11 (девятый запуск): выдачи Яндекс Карт по темам «Особым детям» по всей Москве и области (ключи eu<N>-1119f)."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = ["иппотерапия для детей", "адаптивное плавание для детей с ОВЗ", "инклюзивная театральная студия для детей",
     "адаптивная физкультура для детей с ОВЗ", "занятия для детей с синдромом Дауна", "сенсорная комната для детей с ОВЗ",
     "инклюзивная творческая студия для детей", "занятия для детей с ДЦП", "инклюзивный клуб для детей с аутизмом", "АФК для детей с аутизмом"]
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?eu{n}=1119f&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    p = os.path.join(ROOT, "auto/fetch-queue.txt"); old = open(p).read()
    if urls[0] not in old: open(p, "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1119_queries2.json"), "w"), ensure_ascii=False, indent=0)
