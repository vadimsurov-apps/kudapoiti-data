"""Сеть семейных парков Joki Joya: 19 филиалов в Москве и области (кроме уже добавленных Авиапарка, Саларис, Мозаики).
Список — cyclowiki «Парки Joki Joya» (источники проверены 20.02.2025). Координаты — ТЦ, приблизительно:
их уточняет робот сверки с OSM (по названию ТЦ в адресе). Иконки — tools/icons_joki_joya.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import SRC
from add_batch14 import metro

SRCURL = "https://cyclowiki.org/wiki/Парки_Joki_Joya"
ACC = "приблизительно (по ТЦ) — уточнить по OSM"
# id-хвост: (ТЦ, адрес, широта, долгота)
BR = {
    "columbus": ("ТРЦ «Columbus»", "ул. Кировоградская, 13А, ТРЦ «Columbus»", 55.6110, 37.6024),
    "iyun-mytishchi": ("ТРЦ «Июнь» Мытищи", "г. Мытищи, ул. Мира, 51, ТРЦ «Июнь»", 55.9183, 37.7605),
    "vegas-kuntsevo": ("ТРК «Vegas Кунцево»", "56-й км МКАД, ТРК «Vegas Кунцево»", 55.7414, 37.4156),
    "spektr": ("ТРЦ «Спектр»", "Новоясеневский пр-т, 1, ТРЦ «Спектр»", 55.6185, 37.5085),
    "edelweiss": ("ТРЦ «Эдельвейс»", "г. Балашиха, мкр. Железнодорожный, ул. Советская, 9, ТРЦ «Эдельвейс»", 55.7505, 38.0105),
    "otrada": ("ТЦ «Отрада»", "Пятницкое ш., 7-й км, вл. 2, ТЦ «Отрада»", 55.8585, 37.3165),
    "shchelkovsky": ("ТРЦ «Щёлковский»", "Щёлковское ш., 75, ТРЦ «Щёлковский»", 55.8100, 37.7983),
    "vesna": ("ТРЦ «Весна!»", "Алтуфьевское ш., 1-й км, вл. 3, стр. 1, ТРЦ «Весна!»", 55.9095, 37.5870),
    "mega-belaya-dacha": ("ТЦ «МЕГА Белая Дача»", "г. Котельники, 1-й Покровский пр-д, 5, ТЦ «МЕГА Белая Дача»", 55.6545, 37.8420),
    "riga-mall": ("ТРК «Рига Молл»", "Новорижское ш., 5-й км от МКАД, ТРК «Рига Молл»", 55.7930, 37.2580),
    "mari": ("ТРК «MARI»", "ул. Поречная, 10, ТРК «MARI»", 55.6545, 37.7470),
    "kosino": ("ТРЦ «Город Косино»", "Новоухтомское ш., 2А, ТРЦ «Город Косино»", 55.7085, 37.8620),
    "rostokino": ("ТРК «Европолис Ростокино»", "пр-т Мира, 211, корп. 2, ТРК «Европолис Ростокино»", 55.8435, 37.6620),
    "evropeisky": ("ТРК «Европейский»", "пл. Киевского вокзала, 2, ТРК «Европейский»", 55.7444, 37.5659),
    "gagarinsky": ("ТРЦ «Гагаринский»", "ул. Вавилова, 3, ТРЦ «Гагаринский»", 55.7095, 37.5910),
    "lefortovo": ("ТРЦ «Город Лефортово»", "ш. Энтузиастов, 12, корп. 2, ТРЦ «Город Лефортово»", 55.7505, 37.7095),
    "oblaka": ("ТРЦ «Облака»", "Ореховый б-р, 22А, ТРЦ «Облака»", 55.6110, 37.7340),
    "kuzminki": ("ТРЦ «Кузьминки Молл»", "ул. Зеленодольская, вл. 42, ТРЦ «Кузьминки Молл»", 55.7050, 37.7660),
    "rio-leninsky": ("ТРЦ «РИО» Ленинский", "Ленинский пр-т, 109, ТРЦ «РИО»", 55.6638, 37.4995),
}


def main():
    wb = openpyxl.load_workbook(SRC); ws = wb["Места"]
    hdr = [c.value for c in ws[1]]; col = {h: i + 1 for i, h in enumerate(hdr)}
    rows = {ws.cell(r, 1).value: r for r in range(2, ws.max_row + 1)}
    tpl = [ws.cell(rows["joki-joya"], i).value for i in range(1, len(hdr) + 1)]
    body = Font(name="Arial", size=10); thin = Side(style="thin", color="D0D0D0")
    added = []
    for tail, (mall, addr, lat, lon) in BR.items():
        pid = f"joki-joya-{tail}"
        r = rows.get(pid)
        if not r:
            r = ws.max_row + 1
            for i, v in enumerate(tpl, 1):
                c = ws.cell(r, i, v); c.font = body
                c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
                c.alignment = Alignment(wrap_text=True, vertical="top")
            added.append(pid)
        vals = {"id": pid, "Название": f"Joki Joya ({mall.replace('ТРЦ ', '').replace('ТРК ', '').replace('ТЦ ', '')})",
                "Адрес": addr, "Широта": lat, "Долгота": lon, "Точность координат": ACC, "Метро": metro(lat, lon),
                "Как найти": f"Внутри {mall}", "Источник": SRCURL,
                "Часы работы": "ежедневно 10:00-22:00 (уточняйте у парка)", "Детский билет, ₽": None,
                "Бесплатно до (лет / см)": "цена за ребёнка — зависит от парка и дня недели; взрослые — бесплатно"}
        for k, v in vals.items():
            ws.cell(r, col[k]).value = v
    wb.save(SRC)
    print("добавлено:", len(added))


if __name__ == "__main__":
    main()
