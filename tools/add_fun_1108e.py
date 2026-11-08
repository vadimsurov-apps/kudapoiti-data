"""Робот fun, 2026-11-08 (вечер): кандидаты OSM (auto/candidates.json), подтверждённые кэшем сайтов (auto/pages)
и WebSearch. Иконки — tools/icons_fun_1108e.py. Запуск: KP_PART=fun python3 tools/add_fun_1108e.py"""
import json, os
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from batch_helpers import P, SRC
from add_batch14 import metro

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DAY = "2026-11-08"
ROWS = []


def add(pid, name, typ, cats, tags, addr, lat, lon, a0, a1, d0, d1, energy, price, note, hours, plus, minus,
        src, exact=False, acc=None, indoor="да", adult=2, booking="не нужна", sit="нет", dark="нет", loud="нет",
        food="нет", season=None, stroller="частично", crowd="частично", moscow=True, site="", adult_price=None,
        dark_="нет"):
    m = metro(lat, lon) if moscow else "— (на машине / электричке)"
    r = P(pid, name, typ, m, addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor, plus, minus,
          adult=adult, src=src, acc="точно (OpenStreetMap)" if exact else (acc or "приблизительно, ±500 м"),
          booking=booking, sit=sit, dark=dark, loud=loud, food=food, season=season, stroller=stroller, crowd=crowd,
          adult_price=adult_price)
    r["Сайт"] = site
    r["Категории"] = cats
    r["Проверено (дата)"] = DAY
    ROWS.append(r)



O = " ; OpenStreetMap"

add("oruzheyny-podval", "Музей «Оружейный подвал»", "музей", "museums", "история",
    "Москва, Никольская ул., 11-13, стр. 1 (вход через арку и направо)", 55.756937, 37.621778, 7, 14, 60, 120,
    "средне", 500, "детский билет 500 ₽, взрослый 1000 ₽; тир — 300 ₽", "ежедневно 11:00–20:00",
    "Контактный музей в подвале на Никольской: доспехи, холодное и огнестрельное оружие (модели) и предметы быта "
    "разных эпох — все экспонаты можно брать в руки и разбираться, как они работают. Есть страйкбольный тир и "
    "метание ножа с инструктором, экскурсии и квесты для групп от 5 человек",
    "Тема оружия — скорее для школьников; мастер-классы временно не проводятся (по сайту музея)",
    "https://podval-museum.ru/" + O, exact=True, site="https://podval-museum.ru/", adult_price=1000, adult=3,
    booking="не нужна")
add("chess-museum-gogolevsky", "Музей шахмат (Центральный дом шахматиста)", "музей", "museums,chess",
    "шахматы, история", "Москва, Гоголевский бульвар, 14, стр. 1", 55.747791, 37.60043, 7, 14, 45, 90, "спокойно",
    None, "экскурсии — по записи, цены уточняйте у Федерации шахмат России", "уточняйте",
    "Музей Федерации шахмат России в отреставрированном Центральном доме шахматиста: шахматы из стекла, дерева и "
    "янтаря, комплекты царских детей начала XIX века, призы и вещи чемпионов мира. Хорошо дополняет занятия "
    "шахматами — после экскурсии можно сыграть партию",
    "Часы работы и формат посещения (свободный вход или экскурсии) уточнять заранее",
    "https://ruchess.ru/chess_in_museums/museums/museum_tsdsh/ ; ruchess.ru (новость об открытии музея)" + O,
    exact=True, site="https://ruchess.ru/chess_in_museums/museums/museum_tsdsh/", booking="желательна", adult=3)
add("diamond-fund-kremlin", "Выставка «Алмазный фонд» (Московский Кремль)", "музей", "museums",
    "история, драгоценности", "Москва, Кремль, здание Оружейной палаты (вход через Боровицкие ворота)",
    55.749614, 37.613758, 7, 14, 45, 60, "спокойно", None,
    "билеты — на сеанс по времени, на сайте и в кассе; цены уточняйте", "пт–ср 10:00–13:00, 14:00–17:00 (чт — выходной)",
    "Сокровищница Гохрана: Большая императорская корона, скипетр с алмазом «Орлов», держава, знаменитые "
    "самородки золота и платины с забавными названиями, крупнейшие алмазы и ювелирные украшения. Детям "
    "интереснее всего самородки и камни-рекордсмены",
    "Строгий досмотр, фото запрещено, вход по сеансам — билеты лучше брать заранее; малышам скучно",
    "OpenStreetMap (часы) ; gokhran.ru ; kudago.com/msk/place/muzej-almaznyij-fond/", exact=True,
    site="http://www.gokhran.ru", booking="обязательна", adult=3, stroller="нет")
add("cin-moskva-okhotny", "Киноклуб «Москва» (Охотный Ряд)", "кинотеатр", "cinema", "сказки и театр",
    "Москва, Охотный Ряд, 2, 4-й этаж торговой галереи Four Seasons", 55.757028, 37.617406, 6, 14, 90, 150,
    "спокойно", 5000, "детский билет 5000 ₽, взрослый 10 000 ₽ (все залы)", "ежедневно 11:00–01:30",
    "Премиальный киноклуб у Кремля: 10 залов с креслами-реклайнерами и звуком Dolby Atmos, 7 «диванных» залов, "
    "ресторан с детским меню; залы на 7 мест можно арендовать на день рождения",
    "Очень дорого — вариант для особого случая; детские сеансы смотрите в репертуаре",
    "http://cinema.moscow" + O, exact=True, site="http://cinema.moscow", adult_price=10000, sit="да",
    dark="да", food="да", adult=2)
add("cin-5zvezd-paveletskaya", "Кинотеатр «Пять звёзд на Павелецкой»", "кинотеатр", "cinema", "сказки и театр",
    "Москва, ул. Бахрушина, 25", 55.73294, 37.637167, 3, 14, 90, 120, "спокойно", 400,
    "цена зависит от сеанса; детям до 3 лет часто бесплатно без места", "по расписанию",
    "Мультиплекс сети «Пять звёзд» с 2001 года у Павелецкой: семейное кино и мультфильмы, кафе PREMIEREcafe, "
    "клубные дни со скидками",
    "Детские сеансы — по расписанию, проверяйте афишу",
    "https://5zvezd.ru/cinemas/paveletskaya" + O, exact=True, site="https://5zvezd.ru/cinemas/paveletskaya",
    sit="да", dark="да", food="да")

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allids = {x["id"] for x in json.load(open(os.path.join(ROOT, "places.json")))["places"]}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
