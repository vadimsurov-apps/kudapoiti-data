"""Партия 14: места, где робот нашёл живые акции (пробные занятия, скидки именинникам и т.п.).
Координаты — из OpenStreetMap (точные), метро — ближайшая станция."""
import math, re, json
from batch_helpers import *  # noqa
from batch_helpers import P
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

MET = [(n, float(a), float(b)) for n, a, b in
       re.findall(r'": \("([^"]+)", ([\d.]+), ([\d.]+)\)', open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "MetroStations.swift")).read())]


def metro(lat, lon):
    d, n = min((math.hypot((lat - a) * 111, (lon - b) * 63), n) for n, a, b in MET)
    return n if d < 2.5 else "— (на машине / электричке)"


OSM = "OpenStreetMap; акция — с сайта места, проверено 2026-11-04"
EX = "точно (OpenStreetMap)"


def base(pid, name, typ, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor, plus, minus, site,
         cats, bday=False, addr=None, **kw):
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor,
          plus, minus, src=OSM, acc=EX, **kw)
    r["Сайт"] = site
    r["Категории"] = cats
    if bday:
        r["День рождения"] = "да"
    return r


def swim(pid, name, lat, lon, site, plus, a0=0, a1=7, price=2500, addr=None, hours=None):
    return base(pid, name, "детский бассейн", lat, lon, a0, a1, 30, 60, "активно", "вода, спорт и активность", price,
                "цена «от» за занятие; первое занятие — см. акцию", hours, "да", plus,
                "Занятия по записи; уточняйте возраст группы", site, "pools", addr=addr, booking="обязательна",
                food="нет", stroller="частично", adult=1)


def section(pid, name, lat, lon, site, plus, sport, a0=4, a1=14, price=1000, addr=None, hours=None):
    return base(pid, name, "спортивная секция", lat, lon, a0, a1, 45, 90, "активно", "спорт и активность", price,
                "цена «от» за занятие; первое — см. акцию", hours, "да", plus,
                f"{sport}: группы по возрасту, запись заранее", site, "sport", addr=addr, booking="обязательна",
                food="нет", stroller="нет", adult=1)


def play(pid, name, typ, lat, lon, site, a0, price, plus, minus, cats, bday=True, hours=None, energy="активно",
         tags="спорт и активность", indoor="да", loud="да", addr=None, adult=1):
    return base(pid, name, typ, lat, lon, a0, 14, 60, 180, energy, tags, price, "цена «от»", hours, indoor, plus,
                minus, site, cats, bday=bday, addr=addr, booking="желательна", loud=loud, adult=adult)


ROWS = [
    swim("fiji-kids", "Fiji Kids — детский фитнес и бассейн", 55.785662, 37.498655, "https://fijikids.ru/",
         "Детский клуб с бассейном и фитнесом, пробное занятие бесплатно", a0=1, a1=12, hours="ежедневно 9:00–21:00"),
    play("hippo-land", "Hippo — семейный парк развлечений", "развлекательный центр", 55.659472, 37.199732,
         "http://www.hippo-land.ru", 1, 900, "Большой игровой парк под крышей, безлимитный вход",
         "В выходные много детей", "playcenters", hours="ежедневно 10:00–21:00"),
    swim("kidway-rodionovskaya", "Kidway — плавание и развитие для малышей", 55.89315, 37.396933, "https://kidway.pro",
         "Занятия с малышами в воде, первое со скидкой 50%", addr="Родионовская ул., 5", hours="ежедневно 8:00–21:00"),
    section("m-dance-dolgoprudny", "Школа танцев M-Dance (Долгопрудный)", 55.941391, 37.504704, "https://m-sportdance.com",
            "Танцы для детей от 3 лет, пробный урок в подарок при покупке абонемента", "Танцы", a0=3, price=800),
    play("skypark-luzhniki", "Skypark Москва — парк высотных развлечений", "веревочный парк", 55.710053, 37.541565,
         "https://moscow.skypark.ru/", 6, 1500, "Высотные аттракционы и верёвочные трассы со страховкой",
         "Есть ограничения по росту и весу", "active", bday=False, indoor="нет"),
    section("sportstation-kozhukhovo", "Sportstation — скалодром и вейк", 55.723149, 37.67771, "https://station.club/",
            "Скалодром для детей и вейк-парк, первая тренировка бесплатно", "Скалолазание", a0=5, price=1200),
    play("vr-mania", "VR Mania — клуб виртуальной реальности", "VR-клуб", 55.804323, 37.763482, "https://vr-mania.club/",
         7, 490, "VR-игры для детей и родителей", "Не для самых маленьких: от 7 лет", "playcenters",
         energy="средне", tags="техника и роботы"),
    play("unreal-place", "«Нереальное место» — VR-парк", "VR-клуб", 55.760033, 37.66428, "https://www.unreal.place",
         7, 900, "Большой VR-парк с игровыми зонами и арена-шутерами", "Громко, от 7 лет", "playcenters",
         energy="средне", tags="техника и роботы", hours="ежедневно 12:00–24:00"),
    swim("aqua-class-alekseevskaya", "Аква Класс — детский бассейн", 55.822842, 37.620473, "https://aqua-class.com/",
         "Детское плавание, первое занятие со скидкой 50%", a0=0, a1=12, hours="ежедневно 9:00–21:00"),
    swim("aquapups", "Аквапупс — бассейн для малышей", 55.888734, 37.61448, "https://www.aquapups.ru/",
         "Грудничковое и детское плавание, первое занятие в подарок", hours="ежедневно 8:00–21:00"),
    swim("akvaroom", "Акварум — детский бассейн", 55.860689, 37.612292, "https://akvaroom.club/",
         "Плавание для малышей и дошкольников, бесплатное пробное занятие"),
    section("bolshoi-ballet-zelenograd", "Школа «Большой балет» (Зеленоград)", 55.973495, 37.182589,
            "https://bolshoiballet.pro/", "Детский балет, пробное занятие в подарок при покупке абонемента", "Балет",
            a0=3, price=900),
    play("garnizon-a", "«Гарнизон-А» — военно-игровой парк", "активный отдых", 56.895897 - 1, 38.70058,
         "http://garnizon-a.com/", 7, 1500, "Лазертаг и военно-спортивные игры на открытой площадке",
         "Далеко от Москвы, лучше с компанией", "active", indoor="нет"),
    play("zolotoy-shar-krasnogorsk", "Боулинг «Золотой шар» (Красногорск)", "боулинг", 55.817824, 37.31123,
         "https://bowling-krasnogorsk.ru/", 5, 600, "Боулинг для семьи, детские шары и бортики",
         "Вечером громко и много взрослых", "playcenters", energy="средне", tags="", adult=2),
    swim("kitenok-orekhovo", "«Китёнок» — детский бассейн", 55.586195, 37.675394, "https://1kitenok.ru/",
         "Плавание для малышей, скидка 10% на второго ребёнка", hours="ежедневно 9:00–21:00"),
    base("kuklab-theatre", "Театр КукLab", "театр", 55.746025, 37.578287, 3, 10, 50, 70, "спокойно",
         "сказки и театр", 1000, "цена «от»", "по расписанию", "да", "Камерный кукольный театр для малышей",
         "Маленький зал — билеты заранее", "https://www.teatrkuklab.ru", "shows", booking="обязательна", sit="да",
         dark="частично", food="нет", stroller="нет"),
    swim("malysh-i-more", "«Малыш и море» — бассейн для малышей", 55.870695, 37.687888, "https://malishimore.ru/",
         "Индивидуальное плавание с малышами, первое занятие бесплатно", addr="ул. Коминтерна, 15", price=2600),
    swim("mama-ya-plyvu-preobrazhenka", "«Мама, я плыву» (Преображенская)", 55.80113, 37.709602,
         "https://mamayaplyvu.com/preobragensckaya", "Плавание с малышами, пробное за 990 ₽ вместо 3 800 ₽",
         addr="Краснобогатырская ул., 90, стр. 2", price=3800, hours="ежедневно 9:00–21:00"),
    play("lazertag-medved", "Лазертаг-клуб «Медведь»", "лазертаг", 55.77462, 37.74627, "https://lazertag.msk.ru/",
         6, 900, "Лазертаг для детских праздников и семейных игр", "От 6 лет, громко", "active", indoor="частично"),
    base("mirage-maryino", "Кинотеатр «Мираж» (Марьино)", "кинотеатр", 55.649429, 37.769466, 3, 14, 90, 120,
         "спокойно", "сказки и театр", 350, "цена зависит от сеанса", "ежедневно 10:30–23:00", "да",
         "Детские сеансы, скидка в день рождения", "Проверяйте афишу", "https://mirage.ru/", "cinema",
         dark="да", sit="да", food="да", loud="частично"),
    base("relizpark-solnechnogorsk", "Кинотеатр «Релизпарк» (Солнечногорск)", "кинотеатр", 56.184738, 36.976709, 3,
         14, 90, 120, "спокойно", "сказки и театр", 300, "детям до 12 — скидка 20% на сеансы 0+ и 6+",
         "по расписанию", "да", "Скидка детям на семейные фильмы", "Проверяйте афишу",
         "https://solnechnogorsk.relizpark.ru/", "cinema", dark="да", sit="да", food="да", loud="частично"),
    section("sambo-chalykh", "Школа самбо Александра Чалых", 55.882507, 37.636765, "https://chalykh-sambo.clients.site/",
            "Самбо для детей, первая тренировка бесплатно", "Самбо", addr="Полярная ул., 27, корп. 2"),
    section("nosov-martial-arts", "Школа боевых искусств Дмитрия Носова", 55.794309, 37.726347, "https://nspreo.ru/",
            "Боевые искусства для детей, первая тренировка бесплатно", "Единоборства"),
    section("karate-zakharov-reutov", "Школа каратэ Владимира Захарова (Реутов)", 55.753327, 37.856892,
            "https://karate-reutov.ru", "Каратэ для детей, первое занятие бесплатно", "Каратэ"),
    section("schoolball-kuntsevo", "«Школа мяча» — футбол для малышей", 55.764011, 37.437485, "https://schoolball.ru",
            "Футбол для детей с 3 лет, пробная тренировка бесплатно", "Футбол", a0=3,
            hours="ежедневно 10:00–20:00"),
    section("sambo-svao", "Школа самбо (СВАО)", 55.868595, 37.640077, "https://sambo-svao.ru/",
            "Самбо для детей, бесплатная пробная тренировка", "Самбо"),
    swim("flamingo-naro-fominsk", "Детский центр «ФламинGo!» (Наро-Фоминск)", 55.387242, 36.727586,
         "https://flamingocentr.ru", "Бассейн и развитие для малышей, первое занятие −50%"),
    play("lionsland", "Парк львов «Земля Прайда»", "зоопарк", 56.225916, 36.679688, "https://lionsland.ru", 2, 1200,
         "Львы, тигры и другие большие кошки в просторных вольерах", "Далеко от Москвы, много ходить", "animals",
         bday=False, energy="средне", tags="животные", indoor="нет", loud="нет", hours="ежедневно 10:00–19:00", adult=3),
    swim("chaika-swim-school", "Школа плавания «Чайка»", 55.93654, 37.557633, "https://chaikaschool.com/",
         "Обучение детей плаванию, пробное занятие за 990 ₽", a0=3, a1=14, price=1500),
    play("another-world-odintsovo", "VR-арена Another World (Одинцово)", "VR-клуб", 55.650086, 37.256833,
         "https://odin-vr.ru", 7, 1000, "VR-квесты и арена для детей и родителей", "От 7 лет",
         "playcenters", energy="средне", tags="техника и роботы", hours="ежедневно 11:00–22:00"),
]
# опечатка-страховка: координата «Гарнизона» из OSM
for r in ROWS:
    if r["id"] == "garnizon-a":
        r["Широта"] = 55.895897

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing], [i for i in ids if i in existing]
    for row in ROWS:
        assert not (set(row) - set(hdr)), (row["id"], set(row) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
    for r in ROWS: print(r["id"], "|", r["Метро"])
