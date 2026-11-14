"""Робот rare 14.11 (1114b), шаг 3: обзорные страницы найденных организаций + сайты + выдачи «каток Зима в Москве» по
округам и «каток в парке …» (ключи rr14bz*) → auto/fetch-queue.txt.   python3 tools/rare_1114b_round3.py"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ORGS = ["karting_vegas/92604120155", "ice_rink_iskra/1042428828", "fungrad/232594849821", "katok_v_rayone_tsaritsyno/244043113060",
        "katok_v_rayone_mitino/178976694881", "ice_rink/1349795969", "sportivnaya_ploshchadka/184763448787"]
SITES = ["https://fetisovhockeyacademy.com/", "https://lama-sport.ru/", "https://www.mos.ru/city/projects/katki/"]
Q = [f"каток Зима в Москве {o}" for o in ["ЦАО", "САО", "СВАО", "ВАО", "ЮВАО", "ЮАО", "ЮЗАО", "ЗАО", "СЗАО", "Зеленоград", "Новая Москва"]]
Q += [f"каток в парке {p} Москва" for p in ["Останкино", "Кузьминки", "Лианозовский", "Бабушкинский", "Перовский", "Тропарёво",
      "Южное Тушино", "Борисовские пруды", "Воронцовский", "Таганский", "Олимпийская деревня", "Ангарские пруды", "Садовники",
      "Покровское-Стрешнево", "Дубки", "Северное Тушино", "Бутово", "Зарядье", "Музеон", "Сиреневый сад", "Дружба", "Яуза"]]
fq = ["https://yandex.ru/maps/org/" + o + "/" for o in ORGS] + SITES
fq += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14bz{i:02d}=1114b&text=" + u.quote(t) for i, t in enumerate(Q)]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
