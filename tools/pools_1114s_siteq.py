"""Робот pools 14.11 (17 UTC), шаг 3: сайты и страницы организаций кандидатов → auto/fetch-queue.txt.  python3 tools/pools_1114s_siteq.py"""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?pc%d=1114s&text=%s"
LINES = ["https://yandex.ru/maps/org/mama_ya_plyvu_/26107119308/", "https://yandex.ru/maps/org/73159727925/", "https://yandex.ru/maps/org/kidswim/170890098315/",
         "https://kidsfunclub.ru/", "https://kidsfunclub.ru/pool", "https://hills-sport.ru/", "https://hills-sport.ru/kids/", "https://brightfit-msk.ru/",
         "https://flotskaja.xfit.ru/", "https://selfclub.ru/", "https://selfclub.ru/children/",
         "https://zoon.ru/msk/fitness/tsentr_grudnichkovogo_i_detskogo_plavaniya_babysharkpool_na_pyatnitskom_shosse/",
         "https://t-j.ru/list/aqua-babies/", "https://t-j.ru/guide/baby-pool/", "https://www.sportmaster.ru/media/articles/grudnichkovoe-plavanie-podborka-shkol-moskvy/"]
for i, q in enumerate(["Babysharkpool центр грудничкового и детского плавания, Москва, Пятницкое шоссе",
                       "Kidswim детский бассейн Москва",
                       "Мама, я плыву! Беломорская ул., 9 грудничковое плавание возраст",
                       "ГрудничОк, Москва, жилой комплекс Бутово Парк, 20, корп. 1",
                       "Детский бассейн Медси Благовещенский переулок грудничковое плавание"]):
    LINES.append(Y % (i, urllib.parse.quote(q)))
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in LINES if l not in old]) + "\n")
    print(len(LINES))
