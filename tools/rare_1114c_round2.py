"""Робот rare 14.11 (1114c), шаг 2: обзорные страницы организаций-кандидатов (Яндекс Карты) и поиск карточек тех,
у кого в выдаче не было ссылки (ключи rr14ct*) → auto/fetch-queue.txt.   python3 tools/rare_1114c_round2.py"""
import os, urllib.parse as u
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ORGS = ["monster_hockey/11054832904", "polar_team/151935720009", "hockey_edition/199517589937", "arena_play_south/78122914574",
        "tt_tekstil_shchiki_table_tennis/169433476803", "lyod/172656009981", "hockey_school_pro_hockey/78617652415",
        "crazy_snowflakes/192377533583", "sokol_territoriya_sporta/222317826597", "cska_arena/1425831484", "voika_tt/1173551594",
        "schoolskate_ru/173307838687", "skalodrom_les/239413039252", "mayak/10363208249", "serebryaniy_led/1056470557",
        "lucenter/101699636488", "klub_figurnogo_kataniya_ice_fenix/98177661965", "shkola_figurnogo_kataniya_razryad/133677399945",
        "arena_play_ice_night/209790482153", "table_tennis_club/153518775631", "sportsart_iva/95010739557",
        "bulldozer/216766891620", "luch/84438881703", "yauza/210161247792",
        "ledovy_tsentr_medvedkovo_moskovskoy_akademii_figurnogo_kataniya_na_konkakh_moskomsporta/85002786458"]
CARDS = ["Каток ЦУМ, Петровка, 2", "Черневская горка, Южное Бутово", "Московская академия зимних видов спорта СК Ново-Переделкино",
         "Ледовая арена имени Н.А. Петрусевой, Павловский Посад, Большая Покровская ул., 60В",
         "Ледовый дворец Дмитров, Профессиональная ул., 25", "Династия мяча волейбол, Новороссийская ул., 36",
         "Хищники хоккей, Мосфильмовская ул., 41, корп. 2", "Хоккейная академия IceZubrus, Ленинградский просп., 39",
         "НоваСпин настольный теннис, ул. Новаторов, 15", "Тип-Топ верёвочный парк", "Adm Raceway картинг",
         "Легенда 77, Даниловская наб., 8А", "Молодёжка каток Кунцево", "Арена Плей Север, Ботаническая ул., 2"]
fq = ["https://yandex.ru/maps/org/" + o + "/" for o in ORGS]
fq += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?rr14ct{i:02d}=1114c&text=" + u.quote(t) for i, t in enumerate(CARDS)]
if __name__ == "__main__":
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
    print(len(fq))
