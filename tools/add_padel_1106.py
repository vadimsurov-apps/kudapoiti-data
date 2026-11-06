"""Все падел-клубы Москвы и Подмосковья (06.11, просьба Вадима). Источники — обзоры Т—Ж (18.08.2026),
tennisfirst.moscow (07.2026), 360.ru (06.2025), top15moscow, buenospadel.ru. Координаты приблизительные —
уточняет робот сверки (OSM + дом по адресу). Пишет в data/parts/sections.xlsx (KP_PART=sections)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "parts", "sections.xlsx")
TJ = "https://t-j.ru/padel-moscow/"; TF = "https://tennisfirst.moscow/2026/07/05/krytye-padel-korty-moskva/"
R360 = "https://360.ru/tekst/sport/raketki-i-mjachi-gde-poigrat-v-padel-tennis-v-moskve-i-podmoskove/"
BP = "https://buenospadel.ru/blog/padel-v-moskve-gde-igrat.html"; T15 = "https://top15moscow.ru/novosti/gde-igrat-v-padel-v-moskve"
KIDS_UNK = "детские группы — уточняйте у клуба"
# id: (название, адрес, lat, lon, сайт, источник, плюс, как найти, цена корта от, детские подтверждены)
CLUBS = {
    "padel-lunda-konstruktor": ("LUNDA Padel «Конструктор»", "ул. Большая Филёвская, 32", 55.7470, 37.4880, "https://lundapadel.ru", TJ,
                                "Крытые корты, есть детская секция", None, 2200, True),
    "padel-lunda-rechnoy": ("LUNDA Padel «Речной» (ТЦ «Капитолий»)", "ул. Правобережная, 1Б, ТЦ «Капитолий»", 55.8790, 37.4640,
                            "https://lundapadel.ru", TJ, "Крытые корты, есть детская секция", "Внутри ТЦ «Капитолий», 1 этаж", 2200, True),
    "padel-luzhniki-academy": ("Академия падела «Лужники»", "ул. Лужники, 24, стр. 21", 55.7150, 37.5600, "https://padel.luzhniki.ru", TJ,
                               "Детская школа падела с 4 лет", "Территория «Лужников», строение 21", 2800, True),
    "padel-friends-luzhniki": ("Padel Friends (Лужники)", "ул. Лужники, 24, стр. 1", 55.7165, 37.5570, None, R360,
                               "Крытые падел-корты в «Лужниках»; " + KIDS_UNK, "Территория «Лужников», строение 1", None, False),
    "padel-sky-afimall": ("Sky Padel (Афимолл Сити)", "Пресненская наб., 2, ТЦ «Афимолл Сити»", 55.7490, 37.5395, "https://skypadel.club", TJ,
                          "Корты с видом на Москва-Сити; " + KIDS_UNK, "Внутри ТЦ «Афимолл Сити»", 10000, False),
    "padel-tennisru-riviera": ("Падел-корты «Теннис.ру» (ТЦ «Ривьера»)", "ул. Автозаводская, 18, ТЦ «Ривьера»", 55.7090, 37.6570, None, TF,
                               "Крытые корты в ТЦ; " + KIDS_UNK, "Внутри ТЦ «Ривьера»", None, False),
    "padel-first-club": ("First Padel Club", "ул. Шарикоподшипниковская, 13, стр. 5", 55.7175, 37.6770, "https://firstpadel.ru", TJ,
                         "Корты и детская игровая площадка для младших; " + KIDS_UNK, None, 2000, False),
    "padel-park-belokamenny": ("Падел Парк", "1-й Белокаменный пр-д, 7А", 55.8280, 37.7120, "https://mypadelpark.ru", TJ,
                               "Падел-клуб со школой; " + KIDS_UNK, None, 3500, False),
    "padel-rink-skolkovo": ("The Rink Fitness — падел (Сколково)", "Сколково, ул. Новая, 100", 55.6980, 37.3600, "https://therinkfitness.ru", TJ,
                            "Падел в фитнес-клубе; " + KIDS_UNK, None, 6000, False),
    "padlhub-nagatino": ("Академия падела Padl Hub (Нагатинский пр-д)", "1-й Нагатинский пр-д, 2, стр. 17", 55.6830, 37.6280,
                         "https://padlhub.ru/padelacademy", TJ, "Детская академия падела, группы до 4 человек", None, 4000, True),
    "padlhub-kuntsevo": ("Академия падела Padl Hub (Сколковское ш.)", "Сколковское ш., 33, вл. 1", 55.7140, 37.4020,
                         "https://padlhub.ru/padelacademy", R360, "Детская академия падела, группы до 4 человек", None, 4000, True),
    "padel-pari": ("Пари Падел", "ул. 8 Марта, 14, стр. 1", 55.8020, 37.5670, "https://paripadel.ru", TJ,
                   "Крытые корты; " + KIDS_UNK, None, 4500, False),
    "padel-korty-setki": ("Корты — Сетки", "3-я Мытищинская ул., 16, стр. 3", 55.8170, 37.6400, "https://korty-setki.ru", TJ,
                          "Падел-корты; " + KIDS_UNK, None, 4490, False),
    "padel-buenos-skladochnaya": ("Buenos Padel (Складочная)", "ул. Складочная, 1, стр. 6", 55.8045, 37.5890, "https://buenospadel.ru", BP,
                                  "Крытые корты у Савёловской; " + KIDS_UNK, None, 3000, False),
    "padel-buenos-vdnh": ("Buenos Padel (ВДНХ)", "пр-т Мира, 119, стр. 22", 55.8330, 37.6290, "https://buenospadel.ru/vdnh", BP,
                          "Корты на ВДНХ; " + KIDS_UNK, "ВДНХ, строение 22", 3000, False),
    "padel-vnukovo-sport": ("Vnukovo Sport Club — падел", "д. Рогозинино, ул. Луговая, 20а, стр. 2", 55.5830, 37.2480, None, R360,
                            "Занятия для взрослых и детей", None, None, True),
    "padel-zhukovka": ("Padel Club Zhukovka", "Одинцовский г. о., д. Жуковка, Ильинский подъезд, с1", 55.7350, 37.2500, None, R360,
                       "Падел-клуб на Рублёвке; " + KIDS_UNK, None, None, False),
    "padel-berta-village": ("Berta Village — падел", "г. о. Истра, КП «Ламишино Парк», 11Д", 55.9050, 36.8300, None, R360,
                            "Загородный клуб с падел-кортами; " + KIDS_UNK, None, None, False),
    "padel-cooltennis-malevich": ("CoolTennis — падел (парк Малевича)", "Одинцовский г. о., парк им. Малевича", 55.7160, 37.3770, None, R360,
                                  "Группы 2–4 человека и индивидуально; " + KIDS_UNK, "В парке им. Малевича", None, False),
}


def main():
    wb = openpyxl.load_workbook(SRC); ws = wb["Места"]
    hdr = [c.value for c in ws[1]]; col = {h: i + 1 for i, h in enumerate(hdr)}
    rows = {ws.cell(r, 1).value: r for r in range(2, ws.max_row + 1)}
    tpl = [ws.cell(rows["padlhub-yasenevo"], i).value for i in range(1, len(hdr) + 1)]
    body = Font(name="Arial", size=10); thin = Side(style="thin", color="D0D0D0")
    n = 0
    for pid, (name, addr, lat, lon, site, src, plus, hint, price, kids) in CLUBS.items():
        r = rows.get(pid)
        if not r:
            r = ws.max_row + 1; n += 1
            for i, v in enumerate(tpl, 1):
                c = ws.cell(r, i, v); c.font = body
                c.border = Border(left=thin, right=thin, top=thin, bottom=thin); c.alignment = Alignment(wrap_text=True, vertical="top")
        vals = {"id": pid, "Название": name, "Адрес": addr, "Широта": lat, "Долгота": lon,
                "Точность координат": "приблизительно — уточнить по OSM", "Метро": metro(lat, lon), "Сайт": site,
                "Источник": src, "Плюс": plus, "Как найти": hint, "Возраст от": 4 if kids else 6,
                "Детский билет, ₽": None, "Взрослый билет, ₽": price,
                "Бесплатно до (лет / см)": (f"аренда корта от {price} ₽/час" if price else "цены — на сайте клуба"),
                "Минус": "Аренда корта недешёвая, бронировать заранее", "Проверено (дата)": "2026-11-06",
                "Статус данных": "черновик — проверить", "Категории": "padel"}
        for k, v in vals.items():
            if k in col: ws.cell(r, col[k]).value = v
    wb.save(SRC); print("добавлено:", n)


if __name__ == "__main__":
    main()
