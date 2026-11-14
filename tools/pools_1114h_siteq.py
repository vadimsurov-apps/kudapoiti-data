"""Робот pools 14.11 (08 UTC), шаг 3: сайты кандидатов и уточняющие поиски Яндекс Карт (ключ pc<N>=1114h) → auto/fetch-queue.txt.
python3 tools/pools_1114h_siteq.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pc%d=1114h&text=%s"
LINES = ["https://laguna-boba.ru/", "https://laguna-boba.ru/price", "https://dvvs.ru/", "https://watersport.ruza.ru/",
         "https://mbudo-kashira.ru/", "https://sk-kashira.ru/", "https://chaikaschool.com/locations/gazoprovod",
         "https://detskij-bassejn-kitik.clients.site/"]
for i, q in enumerate(["Глубина бассейн обучение плаванию улица Берзарина 32", "Кря-Ква детский бассейн Ступино",
                       "Аквариум бассейн Луховицы Парковая 1 цены", "Мама, я плыву центр раннего плавания филиалы"]):
    LINES.append(Y % (i, urllib.parse.quote(q)))
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in LINES if l not in old]) + "\n")
    print(len(LINES))
