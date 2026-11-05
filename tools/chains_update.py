"""Сверка сетей кафе с детскими комнатами по официальным сайтам (05.11.2026).
Координаты — из ссылок «Посмотреть на карте» на сайтах сетей (точка организации в Яндекс Картах).
- АндерСон: cafeanderson.com/cafe — детская комната и аниматоры во всех кафе.
- Чайхона №1: chaihona1.ru/restaurants — детский зал/игровая зона только в части ресторанов.
Закрытые/не найденные на сайте сети филиалы удаляются (история — в git)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import SRC
from add_batch14 import metro

YA = "точно (Яндекс Карты, ссылка с сайта сети)"
AND_SRC = "https://cafeanderson.com/cafe"
CH_SRC = "https://chaihona1.ru/restaurants"

# id: (название, адрес, широта, долгота, часы, как найти)
ANDERSON = {
    "cafe-anderson-molodezhnaya": ("АндерСон (Крылатское, Рублёвское ш.)", "Рублёвское ш., 28, корп. 1", 55.746509, 37.421951, "пн-пт 09:00-22:00; сб-вс 09:00-23:00", None),
    "cafe-anderson-5avenue": ("АндерСон (ТРЦ «Пятая Авеню»)", "ул. Маршала Бирюзова, 32, ТРЦ «Пятая Авеню»", 55.799335, 37.482982, "пн-пт 08:30-22:00; сб-вс 10:00-22:00", "Внутри ТРЦ «Пятая Авеню»"),
    "cafe-anderson-gilyarovskogo": ("АндерСон (Гиляровского)", "ул. Гиляровского, 39, стр. 3", 55.783464, 37.632062, "пн-пт 08:00-22:00; сб-вс 09:00-22:00", None),
    "cafe-anderson-shuvalovsky": ("АндерСон (ЖК «Шуваловский»)", "Мичуринский пр-т, 7, корп. 1", 55.701719, 37.512245, "вс-чт 09:00-21:00; пт-сб 09:00-22:00", "В ЖК «Шуваловский»"),
    "cafe-anderson-perovo": ("АндерСон (Кусковская)", "ул. Кусковская, 47", 55.744313, 37.794352, "ежедневно 10:00-22:00", None),
    "cafe-anderson-resort": ("АндерСон (Льва Толстого)", "ул. Льва Толстого, 23, корп. 1", 55.734917, 37.584820, "ежедневно 09:00-22:00", None),
    "cafe-anderson-obrucheva": ("АндерСон (Обручева)", "ул. Обручева, 30/1", 55.656285, 37.527256, "пн-пт 09:00-22:00; сб-вс 10:00-22:00", None),
    "cafe-anderson-ostrovityanova": ("АндерСон (Островитянова)", "ул. Островитянова, 5", 55.644864, 37.493186, "ежедневно 09:00-22:00", None),
    # новые
    "cafe-anderson-domodedovo": ("АндерСон (Домодедово)", "г. Домодедово, Каширское ш., 42", 55.436920, 37.765315, "ежедневно 09:00-22:00", None),
    "cafe-anderson-vorontsovsky": ("АндерСон (Воронцовский парк)", "ул. Академика Пилюгина, 18", 55.668350, 37.534383, "вс-чт 09:00-22:00; пт-сб 09:00-23:00", "Рядом с Воронцовским парком"),
    "cafe-anderson-afanasyevsky": ("АндерСон (Гагаринский, Б. Афанасьевский)", "Большой Афанасьевский пер., 2", 55.744931, 37.597657, "пн-пт 09:00-22:00; сб-вс 10:00-22:00", None),
    "cafe-anderson-donskoy": ("АндерСон (ЖК «Донской Олимп»)", "Серпуховской Вал, 21, корп. 4", 55.710697, 37.607449, "ежедневно 10:00-22:00", "В ЖК «Донской Олимп»"),
    "cafe-anderson-medvedkovo": ("АндерСон (Медведково)", "ул. Стартовая, 9, корп. 2", 55.886337, 37.701736, "ежедневно 10:00-22:00", None),
    "cafe-anderson-mitino-dubravnaya": ("АндерСон (Митино, Дубравная)", "ул. Дубравная, 34/29", 55.846381, 37.358148, "ежедневно 10:00-22:00", None),
    "cafe-anderson-tsaritsyno": ("АндерСон (парк Царицыно)", "ул. Тюрина, 1", 55.618446, 37.672827, "пн-пт 10:00-22:00; сб-вс 10:00-22:00", "У парка Царицыно"),
    "cafe-anderson-fort-yasenevo": ("АндерСон (ТЦ «Fort Ясенево»)", "Новоясеневский пр-т, 11, ТЦ «Fort Ясенево»", 55.606670, 37.536284, "ежедневно 10:00-22:00", "Внутри ТЦ «Fort Ясенево»"),
    "cafe-anderson-pushkino": ("АндерСон (Пушкино, ТРЦ «Пушкино Парк»)", "г. Пушкино, Красноармейское ш., стр. 104, ТРЦ «Пушкино Парк»", 56.017085, 37.885369, "ежедневно 10:00-22:00", "ТРЦ «Пушкино Парк»: вход 1, 2 этаж"),
}
ANDERSON_GONE = ["cafe-anderson-vdnh", "cafe-anderson-bratislavskaya", "cafe-anderson-sokol", "cafe-anderson-festival",
                 "cafe-anderson-krasnoselskaya", "cafe-anderson-butovo", "cafe-anderson-korolev", "cafe-anderson-mitino",
                 "cafe-anderson-strastnoy", "cafe-anderson-zhulebino"]

# Чайхона №1 (официальная сеть) — только рестораны с детским залом / игровой зоной
CHAIHONA = {
    "cafe-chaihona1-altufevo": ("Чайхона №1 (Алтуфьево)", "Алтуфьевское ш., 16", 55.857321, 37.585673, "ежедневно 12:00-24:00", "Лего-комната, ежедневно 12:00–24:00", "Отдельная игровая зона, лего-комната, детское меню"),
    "cafe-chaihona1-vernadskogo": ("Чайхона №1 (Вернадского)", "пр-т Вернадского, 105, корп. 3", 55.663806, 37.484864, None, None, "Детский зал с аниматором, детское меню"),
    "cafe-chaihona1-zhukovka": ("Чайхона №1 (Жуковка)", "Одинцовский г. о., д. Жуковка, Ильинский подъезд, с1", 55.7445114, 37.2350265, "ежедневно 12:00-24:00", None, "Детский зал с играми и конкурсами, ханская юрта"),
    "cafe-chaihona1-marino": ("Чайхона №1 (Марьино)", "ул. Люблинская, 96", 55.657123, 37.739375, "ежедневно 12:00-24:00", None, "Настоящая юрта для детей, аниматоры"),
    "cafe-chaihona1-mitino": ("Чайхона №1 (Митино)", "Пятницкое ш., 39", 55.855153, 37.355498, "ежедневно 11:00-24:00", None, "Детский зал с занятиями"),
    "cafe-chaihona1-novokosino": ("Чайхона №1 (Новокосино)", "ул. Городецкая, 5", 55.742874, 37.866927, None, None, "Оборудованная игровая зона, детское меню"),
    "cafe-chaihona1-tushino": ("Чайхона №1 (Тушино)", "ул. Лодочная, 4", 55.835776, 37.455085, "ежедневно 12:00-24:00", None, "Детский зал с аниматором и игровой программой"),
}
# в базе как «с детской», но на сайте сети: Полянка — без детского зала; Грузинская и Пражская — нет в списке
CHAIHONA_GONE = ["cafe-chaihona-polyanka", "cafe-chaihona-gruzinskaya", "cafe-chaihona-prazhskaya"]


def main():
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    col = {h: i + 1 for i, h in enumerate(hdr)}
    rows = {ws.cell(r, 1).value: r for r in range(2, ws.max_row + 1)}
    template = [ws.cell(rows["cafe-anderson-obrucheva"], i).value for i in range(1, len(hdr) + 1)]

    def put(r, pid, name, addr, lat, lon, hours, hint, plus=None, src=AND_SRC, site=None):
        vals = {"id": pid, "Название": name, "Адрес": addr, "Широта": lat, "Долгота": lon, "Точность координат": YA,
                "Метро": metro(lat, lon), "Часы работы": hours, "Как найти": hint, "Источник": src, "Сайт": site or src,
                "Категории": "food", "День рождения": "да"}
        if plus: vals["Плюс"] = plus
        for k, v in vals.items():
            ws.cell(r, col[k]).value = v

    body = Font(name="Arial", size=10); thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    def new_row():
        r = ws.max_row + 1
        for i, v in enumerate(template, 1):
            c = ws.cell(r, i, v); c.font = body; c.border = border; c.alignment = Alignment(wrap_text=True, vertical="top")
        return r

    added, updated = [], []
    for pid, (name, addr, lat, lon, hours, hint) in ANDERSON.items():
        r = rows.get(pid) or new_row()
        (updated if pid in rows else added).append(pid)
        put(r, pid, name, addr, lat, lon, hours, hint, plus="Семейное кафе сети «АндерСон»: детская комната и аниматоры")
    for pid, (name, addr, lat, lon, hours, hint, plus) in CHAIHONA.items():
        r = rows.get(pid) or new_row()
        (updated if pid in rows else added).append(pid)
        put(r, pid, name, addr, lat, lon, hours, hint, plus=plus, src=CH_SRC)
        ws.cell(r, col["Теги интересов"]).value = "творчество"
        ws.cell(r, col["Взрослый билет, ₽"]).value = 2000
        ws.cell(r, col["Бесплатно до (лет / см)"]).value = "средний чек ~1500–2000 ₽ на взрослого"
        ws.cell(r, col["Минус"]).value = "Взрослый ресторан с кальяном; детский зал — уточняйте часы работы"
    gone = [g for g in ANDERSON_GONE + CHAIHONA_GONE if g in rows]
    for r in sorted((rows[g] for g in gone), reverse=True):
        ws.delete_rows(r)
    wb.save(SRC)
    print("обновлено:", len(updated), "добавлено:", len(added), added, "удалено:", gone)


if __name__ == "__main__":
    main()
