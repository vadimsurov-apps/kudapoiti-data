"""Робот pools 14.11 (17 UTC), шаг 2: карточки Яндекс Карт новых кандидатов (ключ po<N>=1114s) и сайты → auto/fetch-queue.txt.
python3 tools/pools_1114s_cardq.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = [
 "Плыви, малыш, Москва, Мичуринский просп., 16",
 "Мама, я плыву!, Москва, Беломорская ул., 9",
 "Стрела обучение плаванию, Москва, ул. Гримау, 6",
 "Малыш и море, Москва, Лосиноостровский район, жилой комплекс Ты и Я, к2",
 "Детский бассейн Медси, Москва, Трёхпрудный пер., 16",
 "SwimRocket, Москва, ул. Молостовых, 10А, стр. 5",
 "SwimRocket, Москва, ул. Вилиса Лациса, 8",
 "ФОК Касатка бассейн, Москва, ул. Молостовых, 10А, стр. 5",
 "Акватория Тушино бассейн, Москва, ул. Вилиса Лациса, 8",
 "Малыш и море, Москва, ул. Коминтерна, 15",
 "Плыви малыш аква-садик Раменки грудничковое плавание",
 "World Class детский бассейн, Москва, Пятницкое ш., 29, корп. 5",
 "Hills Fitness детский бассейн, Москва, Минская ул., 1Г, корп. 9",
 "Self club детский бассейн, Москва, Верхоянская ул., 9",
 "Школа плавания Xfit, Москва, Флотская ул., 5, корп. В",
 "Школа плавания Xfit, Москва, ул. Федосьино, 12",
 "Bright Fit детский бассейн, Москва, Профсоюзная ул., 31, корп. 5",
 "СССР фитнес детский бассейн, Москва, Новоалексеевская ул., 25",
]
EXTRA = ["https://malishimore.ru/", "https://malishimore.ru/contacts", "https://mamayaplyvu.com/", "https://mamayaplyvu.com/contacts",
         "https://mamayaplyvu.com/belomorskaya", "https://plyvimalysh.ru/", "https://medsi.ru/services/detskiy-basseyn/",
         "https://www.swimrocket.ru/bassein-kasatka/", "https://www.swimrocket.ru/bassein-tushino/", "https://www.swimrocket.ru/tseny/",
         "https://hillsfitness.ru/kids/", "https://selfclub.ru/kids/", "https://brightfit.ru/detskij-fitnes/"]
if __name__ == "__main__":
    lines = list(EXTRA)
    for i, q in enumerate(Q):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1114s&text=%s" % (i, urllib.parse.quote(q)))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    print(len(lines))
