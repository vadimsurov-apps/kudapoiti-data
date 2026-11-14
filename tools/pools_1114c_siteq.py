"""Робот pools 14.11 (02 UTC), шаг 3: сайты кандидатов и карточки организаций Яндекс Карт (ключ pc<N>=1114c), у которых
поиск по «название + адрес» открыл дом, а не организацию → auto/fetch-queue.txt.   python3 tools/pools_1114c_siteq.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITES = ["https://lagunadetstva.ru/", "https://sharksh2o.ru/", "https://newmoscow.mossport.ru/", "https://vremyapobezhdat.ru/",
         "https://bassejn-kitenok.ru/", "https://foknahabino.ru/", "https://t-fitnessclub.ru/",
         "https://yandex.ru/maps/org/umka/183656016837/", "https://yandex.ru/maps/org/umka/183656016837/prices/",
         "https://yandex.ru/maps/org/more_emociy/68936387215/", "https://yandex.ru/maps/org/more_emociy/68936387215/prices/",
         "https://yandex.ru/maps/org/aqualeader/73909453346/", "https://yandex.ru/maps/org/aqualeader/73909453346/prices/",
         "https://yandex.ru/maps/org/aqualeader/113198235753/", "https://yandex.ru/maps/org/aqualeader/113198235753/prices/",
         "https://yandex.ru/maps/org/sportland/58417574612/", "https://yandex.ru/maps/org/agoshkov_center/1381402013/prices/",
         "https://yandex.ru/maps/org/escalada/174876841864/",
         "https://www.swimrocket.ru/raspisanie", "https://lagunadetstva.ru/contacts", "https://sharksh2o.ru/contacts"]
TEXT = ["Нептунята бассейн Троицк", "Морекидс бассейн Московский Радужная", "Морекидс бассейн Московский Солнечная",
        "РезиДетство Троицк", "Дельфинчик бассейн 2-й Грайвороновский проезд", "Морепользы бассейн Коммунарка проспект Куприна",
        "Плавать Умеем школа плавания Глаголева", "Море эмоций бассейн Зеленоград корпус 1841", "Акулы школа плавания Троицк Армейская"]
if __name__ == "__main__":
    lines = list(SITES)
    for i, t in enumerate(TEXT):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pc%d=1114c&text=%s" % (i, urllib.parse.quote(t)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    print(len(lines))
