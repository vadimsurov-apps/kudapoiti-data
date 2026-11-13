"""Робот rare, 13.11 (12:50 UTC; 1113e): выдача Яндекс Карт по районам второго круга (ключи rr13j*) + сайты кандидатов 1113d в fetch-queue.
python3 tools/rare_1113e_queue.py"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Александровский сад", "Аэропорт Внуково", "Баррикадная", "Битцевский Парк", "Борисово", "Боровское шоссе",
         "Ботанический сад", "Братиславская", "Бульвар Адмирала Ушакова", "Бульвар Дмитрия Донского", "Бульвар Рокоссовского",
         "Бунинская аллея", "Бутырская", "ВДНХ"]
Q = ["каток {} метро", "хоккей для детей {} метро", "скалодром для детей {} метро"]
EXTRA = ["тюбинг Москва", "ватрушки горка Москва", "горнолыжный склон Москва", "сквош для детей Москва",
         "театр зверей Москва", "памп-трек Москва", "цирк Москва детский", "каток в ТЦ Москва"]
qs = [q.format(a) for a in AREAS for q in Q] + EXTRA
fq = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr13j{i:03d}=1113e&text=" + u.quote(t) for i, t in enumerate(qs)]
SITES = ["https://sportvsegda.ru/", "https://arenaleg.ru/", "https://na-ldu.ru/", "https://mirsportastal.ru/", "https://ice-park.org/",
         "https://bresmarteam.ru/", "https://deinega-team.ru/", "https://academy-ice-zubrus.ru/", "https://tc-racketlon.ru/",
         "https://rttf.ru/", "https://table-tennis-club.ru/", "https://www.sportbeach.ru/", "https://xn--b1acdg8aaebq.xn--p1ai/"]
fq += SITES
open(os.path.join(ROOT, "auto", "fetch-queue.txt"), "a").write("\n".join(fq) + "\n")
print(len(fq))
