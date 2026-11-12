"""Робот fun, 2026-11-12 (проход u). Пеленальные — карточки ТРЦ в Яндекс Картах с отметкой «Особенности: Комната матери и
ребёнка» (кэш auto/pages *-fum*-1112u*: МЕГА Тёплый Стан, Каширская Плаза, Гудзон, Красный кит, ЕвроПарк, Райкин Плаза,
Филион, Кунцево Плаза) + объект ТРЦ в OSM (справки fu12u-*). Этажа комнаты в источниках нет — «Как найти» не пишем.
Второй круг поиска по районам (Яндекс Карты, *-fua*-1112u*: Университет, Университет дружбы народов, Физтех, Филатов Луг,
Филевский парк, Фили, Фонвизинская, Фрунзенская, Хорошево, Хорошёвская, ЦСКА, Цветной бульвар, Черкизовская, Чертановская,
Чеховская) — почти всё найденное уже есть в базе; квесты 14+/18+ и хорроры пропущены; Virtualka — нет возраста в
источнике; «Прятки от Втемноте» на Вернадского — «временно не работает».
Иконки — tools/icons_fun_1112u.py. Запуск: KP_PART=fun python3 tools/add_fun_1112u.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-12"
YA = "Яндекс Карты, карточка организации (12.11.2026)"
HOUSE = "приблизительно — здание по адресу (Яндекс Карты, координаты дома)"
ROWS, VER = [], {}
PT = json.load(open(os.path.join(ROOT, "tools", "fun_1112u_points.json")))


def place(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, plus, phone, site, src,
          hours=None, child=None, adult=None, note=None, how=None, minus="", loud="частично", sit="частично",
          booking="желательна", adult_int=2, food="нет", stroller="частично", crowd="частично", indoor="да",
          osm=None, changing=None, entr=None, season=None):
    acc = (f"точно (OSM {osm})" if osm else f"точно (вход: OSM {entr})" if entr else HOUSE)
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, child, note, hours, indoor,
          plus, minus or None, adult=adult_int, src=src, acc=acc, adult_price=adult, booking=booking, sit=sit,
          loud=loud, dark="нет", stroller=stroller, crowd=crowd, food=food, season=season)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    if changing:
        r["Пеленальный стол"] = changing
    if how:
        r["Как найти"] = how
    ROWS.append(r)
    f = {"address": addr, "age_min": a0, "age_max": a1}
    if osm:
        f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": f"OSM {osm}"}
    elif entr:
        f["point"] = {"lat": lat, "lon": lon, "level": "вход", "how": f"OSM {entr}"}
    if phone:
        f["phone"] = phone
    if site:
        f["url"] = site
    if hours:
        f["hours"] = hours
    if child is not None:
        f["price_child"] = child
    if adult not in (None, ""):
        f["price_adult"] = adult
    if note:
        f["free_note"] = note
    VER[pid] = {"fields": f, "src": src}


# --- пеленальные (Яндекс Карты: у карточки ТРЦ в «Особенностях» — «Комната матери и ребёнка») ---
CHG = [
 ("chg-mega-teply-stan", "МЕГА Тёплый Стан", "Москва, Калужское ш., 21-й км, с1, ТЦ «МЕГА Тёплый Стан»", "+7 800 707-10-44",
  "https://mega.ru", None, "OSM — ТЦ «Мега Тёплый Стан» relation/6578558 (shop=mall)",
  "Комната матери и ребёнка в МЕГЕ Тёплый Стан — можно спокойно перепеленать и покормить малыша посреди большого похода по магазинам"),
 ("chg-kashirskaya-plaza", "Каширская Плаза", "Москва, Каширское ш., 61Г, ТРЦ «Каширская Плаза»", "+7 495 139-29-60",
  "https://enkatc.ru", None, None,
  "Комната матери и ребёнка в ТРЦ «Каширская Плаза» — перепеленать и покормить малыша, не уезжая из торгового центра"),
 ("chg-gudzon", "Гудзон", "Москва, Каширское ш., 14, ТРЦ «Гудзон»", "+7 495 021-50-46", "https://goodzone.ru",
  "ежедневно 10:00–22:00", "OSM — ТРЦ «Гудзон» relation/7930860 (shop=mall, opening_hours 10:00-22:00)",
  "Комната матери и ребёнка в ТРЦ «Гудзон» у Нагатинского затона — переодеть и покормить малыша в тишине"),
 ("chg-krasny-kit-mytishchi", "Красный кит", "Мытищи, Шараповский пр., вл2, ТРЦ «Красный кит»", "+7 969 021-59-68",
  "https://www.redkit.ru", None, None,
  "Комната матери и ребёнка в мытищинском «Красном ките» — место, где можно перепеленать и покормить малыша"),
 ("chg-europark", "ЕвроПарк", "Москва, Рублёвское ш., 62, ТРЦ «ЕвроПарк»", "+7 495 641-36-09", "https://euro-park.ru",
  None, None,
  "Комната матери и ребёнка в ТРЦ «ЕвроПарк» на Рублёвском шоссе — перепеленать и покормить малыша во время покупок"),
 ("chg-raikin-plaza", "Райкин Плаза", "Москва, Шереметьевская ул., 6, корп. 1, ТРЦ «Райкин Плаза»", "+7 495 542-44-55",
  "https://raikinplaza.ru", None, "OSM — ТРЦ «Райкин плаза» relation/15961180",
  "Комната матери и ребёнка в ТРЦ «Райкин Плаза» у Марьиной Рощи — перепеленать и покормить малыша"),
 ("chg-filion", "Филион", "Москва, Багратионовский пр., 5, ТРЦ «Филион»", None, "https://www.filion.ru",
  "ежедневно 10:00–22:00", "OSM — ТРЦ «Филион» way/77761990 (shop=mall, opening_hours Mo-Su 10:00-22:00)",
  "Комната матери и ребёнка в ТРЦ «Филион» у метро «Фили» — удобно, если в торговом центре вы надолго, например на лазертаге или в кино"),
 ("chg-kuntsevo-plaza", "Кунцево Плаза", "Москва, Ярцевская ул., 19, ТРЦ «Кунцево Плаза»", None, "https://kuntzevo-plaza.ru",
  None, "OSM — ТРЦ «Кунцево Плаза» relation/7007632 (shop=mall)",
  "Комната матери и ребёнка в ТРЦ «Кунцево Плаза» — перепеленать и покормить малыша"),
]
for pid, mall, addr, phone, site, hours, osmsrc, plus in CHG:
    if pid not in PT:
        continue
    lat, lon, osm = PT[pid][:3]
    src = (f"Яндекс Карты, карточка ТРЦ «{mall}» (12.11.2026): «Особенности: … Комната матери и ребёнка», адрес {addr.split(', ТРЦ')[0].split(', ТЦ')[0]}"
           + (f", телефон {phone}" if phone else "") + f", сайт {site.split('//')[1]}; " + (osmsrc or PT[pid][3]))
    place(pid, f"Пеленальная комната — ТРЦ «{mall}»", "пеленальная комната", "changing", "малыши", addr, lat, lon, 0, 3,
          10, 20, "спокойно", plus, phone, site, src, hours=hours, loud="нет", sit="частично", booking="не нужна",
          adult_int=1, stroller="да", crowd="нет", osm=osm, changing="да", child=0, adult=0)

# --- места ---
if "fun-lazertag-loft-varshavka" in PT:
    lat, lon, osm, why = PT["fun-lazertag-loft-varshavka"]
    place("fun-lazertag-loft-varshavka", "Лазертаг Лофт (Варшавское шоссе)", "лазертаг", "quests",
          "приключения, спорт и активность", "Москва, Варшавское ш., 95, корп. 1, 3 этаж", lat, lon, 5, 17, 60, 120, "активно",
          "Лазертаг с безопасными бластерами и сюжетными режимами — захват базы, обезвреживание бомбы, сбор артефактов; "
          "после игры можно пострелять в страйкбольном тире и сесть за стол в ресторане прямо на площадке",
          "+7 993 918-97-74", "https://lasertag-loft.ru",
          "сайт lasertag-loft.ru (кэш auto/pages, 12.11.2026): «Москва, Варшавское шоссе, 95, к1», +7 993 918-97-74, «Время работы "
          "Ежедневно с 10:00 до 22:00», «Командная игра с безопасными бластерами и игровыми заданиями: захват базы, "
          "обезвреживание бомбы, сбор артефактов», «После лазертага предусмотрен страйкбольный тир», «С какого возраста можно "
          "играть? Рекомендуемый возраст для комфортной игры — от 7 лет. Для детей 5–6 лет предусмотрены специальные "
          "укороченные…», группы 4–6 / 7–10 / 11–14 человек, бронь стола 2–3 часа; Яндекс Карты, карточка «Лазертаг Лофт» "
          f"(12.11.2026): этаж 3, «Закрытая игра 9 000 ₽»; {why}",
          hours="ежедневно 10:00–22:00", how="Этаж: 3", booking="обязательна", loud="да", stroller="нет", crowd="нет",
          adult_int=2, food="да", osm=osm if osm and not osm.startswith("entr:") else None,
          entr=osm[5:] if osm and osm.startswith("entr:") else None,
          minus="Играют только своей компанией по предварительной брони (закрытая игра — от 9000 ₽); комфортнее всего с 7 лет, "
                "для 5–6 лет — укороченные режимы")

if "fun-igrobaza-vr-rio" in PT:
    lat, lon, osm, why = PT["fun-igrobaza-vr-rio"]
    place("fun-igrobaza-vr-rio", "VR-клуб «ИгроБаза VR» (ТРЦ «РИО», Дмитровское шоссе)", "VR-клуб", "playcenters",
          "приключения, техника", "Москва, Дмитровское ш., 163А, корп. 1, ТРЦ «РИО», 2 этаж", lat, lon, 6, 17, 30, 60, "активно",
          "VR-арена в стиле граффити со свободным перемещением: до 10 игроков в одной игре, без проводов; для детей — блоки "
          "Kids и Magic Animals 6+, для всей семьи — сборник мини-игр Family; рядом лаунж-зона с PS5 и настолками",
          "+7 985 128-90-66", "https://www.igrobaza-vr.ru",
          "сайт igrobaza-vr.ru (кэш auto/pages, 12.11.2026): «клуб виртуальной реальности в ТЦ РИО Дмитровка», «VR-игр разных "
          "жанров для взрослых и детей от 6 лет», «Арена со свободным передвижением… До 10 человек одновременно», «Детские блоки "
          "Kids и Magic Animals 6+», «сборник мини-игр Family», цена за 1 игрока: будни 900 ₽ / 30 мин и 1600 ₽ / 60 мин, "
          "выходные 1100 ₽ / 2000 ₽, +7 (985) 128-90-66; Яндекс Карты, карточка «ИгроБаза VR» (12.11.2026): «Дмитровское ш., "
          "163А, корп. 1, вход А, Д, этаж 2»; часы — часы ТРЦ «РИО» (auto/mall-hours.json: OSM way/1151175520 opening_hours "
          f"Mo-Su 10:00-22:00), своих часов клуб не публикует; {why}",
          hours="ежедневно 10:00–22:00", child=900, adult=900, how="Вход: А или Д (ТРЦ «РИО»)\nЭтаж: 2",
          booking="желательна", loud="частично", stroller="нет", adult_int=2,
          osm=osm if osm and not osm.startswith("entr:") else None,
          entr=osm[5:] if osm and osm.startswith("entr:") else None,
          minus="Играть можно с 6 лет; цена за игрока — 900 ₽ за 30 минут в будни и 1100 ₽ в выходные (час — 1600 и 2000 ₽)")

if "fun-zabey-kover-chertanovskaya" in PT:
    lat, lon, osm, why = PT["fun-zabey-kover-chertanovskaya"]
    place("fun-zabey-kover-chertanovskaya", "Мастер-классы по тафтингу «Забей ковёр» (Чертановская)", "мастер-класс",
          "masterclass", "творчество", "Москва, Чертановская ул., 1Г, ТЦ «Свод», 2 этаж", lat, lon, 10, 17, 180, 180, "спокойно",
          "Мастер-класс по тафтингу: специальным пистолетом «набиваете» пряжей свой пушистый коврик по эскизу и забираете "
          "его домой; есть отдельный детский мастер-класс для ребят от 10 лет, минута пешком от метро «Чертановская»",
          "+7 915 181-87-90", "https://taftingstudio.ru",
          "сайт taftingstudio.ru (кэш auto/pages, 12.11.2026): «г. Москва, ул. Чертановская, 1 Г», «1 минута от м. Чертановская», "
          "«Детский мастер-класс по тафтингу для детей от 10 лет», «3 часа дети 10-15 лет», «Бронь по предоплате 1 100₽», "
          "+7 (915) 181-87-90; Яндекс Карты, карточка «Забей ковер» (12.11.2026): «Чертановская ул., 1Г, этаж 2», «Детский мастер "
          "класс по тафтингу | Чертановская 6500 ₽», «Групповой мастер класс по тафтингу (Ковёр 40 на 40) 4500 ₽», «(Ковёр 50 на "
          f"50) 5500 ₽»; {why}",
          child=6500, adult=4500, how="Этаж: 2 (ТЦ «Свод»)", booking="обязательна", loud="нет", sit="да", stroller="нет",
          adult_int=3, osm=osm if osm and not osm.startswith("entr:") else None,
          entr=osm[5:] if osm and osm.startswith("entr:") else None,
          minus="Детский мастер-класс — с 10 лет и длится 3 часа; запись по предоплате 1100 ₽; взрослый групповой — 4500 ₽ "
                "за коврик 40×40 и 5500 ₽ за 50×50")


if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=i, column=1).value for i in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places-all.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [x["id"] for x in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        rr = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=rr, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    out = os.environ.get("VER_OUT", "/tmp/claude-0/ver_fun_1112u.json")
    json.dump(VER, open(out, "w"), ensure_ascii=False, indent=1)
    print("rows", len(ROWS), "total", ws.max_row - 1)
