"""Робот fun 1114q: сайты новых мест (возраст, часы, правила) → auto/fetch-queue.txt."""
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITES = ["https://museumruss.ru/", "https://tushino.vzmoscow.ru/", "https://skaz-gor.ru/", "https://museumbread.ru/",
         "https://kolomna-navigator.ru/", "https://www.ecoderevushka.ru/", "https://museum-nf.mo.muzkult.ru/",
         "https://museum.angstrem.ru/", "https://www.jelezomuzey.com/", "https://semenovsky.ru/", "https://www.kapitoliy.ru/",
         "https://vitte-mall.ru/", "https://www.dzvr.ru/", "https://kursky.dzvr.ru/", "https://kazansky.dzvr.ru/",
         "https://yaroslavsky.dzvr.ru/", "https://leningradsky.dzvr.ru/", "https://belorussky.dzvr.ru/", "https://savelovsky.dzvr.ru/",
         "https://kievsky.dzvr.ru/", "https://paveletsky.dzvr.ru/", "https://vostochny.dzvr.ru/"]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(SITES) + "\n" + old)
    print(len(SITES))
