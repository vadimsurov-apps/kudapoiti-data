"""Робот pools 13.11 (11 UTC), шаг 2: карточки Яндекс Карт новых кандидатов (ключ po<N>=1113k) → auto/fetch-queue.txt,
справка OSM (pl20-*) → auto/osm-queries.json.   python3 tools/pools_1113k_cardq.py"""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BAL, KHI, POD, MYT, LYU = (55.797, 37.938), (55.889, 37.445), (55.431, 37.545), (55.911, 37.736), (55.678, 37.894)
# id: (название в Яндексе, адрес в Яндексе, центр поиска, радиус, улица OSM, имя для сверки)
Q = {
 "malenkiy-plovets-balashikha": ("Маленький пловец", "Балашиха, просп. Ленина, 81", BAL, 3500, "Ленина", "пловец"),
 "volna-balashikha-olgino": ("Волна, бассейн", "Балашиха, микрорайон Ольгино, Четвёртая ул., 25", (55.737, 38.045), 3000, "етвёртая", "Волна"),
 "rannee-plavanie-khimki-yunnatov": ("Школа раннего плавания", "Химки, ул. Юннатов, вл1А", KHI, 3500, "Юннатов", "плавани"),
 "spn-khimki-michurina": ("Спн, обучение плаванию", "Химки, ул. Мичурина, с24к1", (55.888, 37.446), 2500, "Мичурина", "бассейн"),
 "spn-novogorsk": ("Спн, обучение плаванию", "Химки, микрорайон Новогорск, к3А", (55.905, 37.36), 2500, "", "бассейн"),
 "pik-zevsa-khimki-chkalova": ("Пик Зевса", "Химки, ул. Чкалова, 4А", KHI, 3500, "Чкалова", "Зевс"),
 "pik-zevsa-khimki-michurina": ("Пик Зевса", "Химки, ул. Мичурина, с24к1", None, 0, "", ""),
 "moy-akva-start-podolsk": ("Мой Аква старт", "Подольск, Октябрьский просп., 2Г", POD, 4500, "Октябрьский", "старт"),
 "aqua-baby-corp-podolsk": ("Aqua Baby Corp", "Подольск, Большая Серпуховская ул., 53", POD, 4500, "Серпуховская", "Baby"),
 "mevis-podolsk": ("Mevis", "Подольск, ул. Орджоникидзе, 7Б", POD, 4500, "Орджоникидзе", "бассейн"),
 "fok-podolsk-ordzhonikidze": ("МБУ Физкультурно-оздоровительный комплекс с бассейном", "Подольск, ул. Орджоникидзе, 7Б", None, 0, "", ""),
 "solnyshki-podolsk": ("Солнышки, бассейн", "Подольск, ул. Клемента Готвальда, 1/42", (55.42, 37.533), 2500, "Готвальда", "Солнышк"),
 "raduga-podolsk": ("Радуга, центр развития ребёнка", "Подольск, Первомайская ул., 11", None, 0, "", ""),
 "schastlivy-delfin-tikhonravova": ("Счастливый Дельфин", "Королёв, микрорайон Юбилейный, ул. М.К. Тихонравова, 17", (55.9369, 37.8399), 1500, "Тихонравова", "ельфин"),
 "schastlivy-delfin-oktyabrsky": ("Счастливый Дельфин", "Королёв, Октябрьский бул., 10", (55.91711, 37.8273), 500, "Октябрьский", "ельфин"),
 "akvakids-korolev-lesnaya": ("АкваКидс", "Королёв, микрорайон Юбилейный, Лесная ул., 14А", (55.933, 37.846), 2500, "Лесная", "кидс"),
 "komanda-korolev-mayakovskogo": ("Команда, бассейн", "Королёв, микрорайон Юбилейный, ул. Маяковского, 2", (55.92892, 37.84399), 400, "Маяковского", "Команда"),
 "more-detyam-mytishchi": ("Море детям", "Мытищи, ул. Разведчика Абеля, 3А", MYT, 4500, "Абеля", "Море"),
 "malenkiy-plovets-mytishchi": ("Маленький пловец", "Мытищи, ул. Колпакова, 24", (55.918, 37.728), 2000, "Колпакова", "пловец"),
 "splash-mytishchi": ("Splash", "Мытищи, просп. Астрахова, 8А", (55.92557, 37.72558), 400, "Астрахова", "бассейн"),
 "akuly-mytishchi": ("Акулы", "Мытищи, просп. Астрахова, 8А", None, 0, "", ""),
 "lyagushonok-lyubertsy": ("Лягушонок, бассейн", "Люберцы, Комсомольский просп., 12", LYU, 4500, "Комсомольский", "Лягуш"),
 "budu-plyt-orekhovy": ("Буду Плыть", "Москва, Ореховый пр., 12", None, 0, "", ""),
 "ss1-kashirskoe-65": ("Школа плавания № 1", "Москва, Каширское ш., 65, корп. 1", None, 0, "", ""),
 "tswim-lyubertsy-check": ("Школа плавания Территория Фитнеса", "Люберцы, ул. 3-е Почтовое Отделение, 102", None, 0, "", ""),
}
if __name__ == "__main__":
    lines, out = [], []
    for i, (pid, (nm, addr, c, r, st, match)) in enumerate(Q.items()):
        lines.append("https://yandex.ru/maps/1/moscow-and-moscow-oblast/?po%d=1113k&text=%s" % (i, urllib.parse.quote(nm + ", " + addr)))
        if c:
            q = {"id": "pl20-" + pid, "lat": c[0], "lon": c[1], "radius": r, "name": match}
            if st: q["street"] = st
            out.append(q)
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read().rstrip("\n").split("\n")
    open(p, "w").write("\n".join(old + [l for l in lines if l not in old]) + "\n")
    p = os.path.join(ROOT, "auto/osm-queries.json")
    old = [x for x in json.load(open(p)) if not x["id"].startswith("pl20-")]
    json.dump(old + out, open(p, "w"), ensure_ascii=False, indent=1)
    print(len(out), len(lines))
