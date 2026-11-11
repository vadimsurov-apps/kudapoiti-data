"""Робот edu, 2026-11-11 (третий запуск): поиск по районам Беляево, Бибирево, Библиотека им.Ленина, Битцевский Парк,
Борисово, Боровицкая, Боровское шоссе, Ботанический сад, Братиславская, Бульвар Адмирала Ушакова, Бульвар Дмитрия Донского,
Бульвар Рокоссовского, Одинцово, Щёлково. Выдачи Яндекс Карт по 7 темам (монтессори, робототехника, английский, ЛФК,
логопед, подготовка к школе, нейропсихолог; auto/pages *-eu<N>-1113e*), каждое место сверено с карточкой организации
(*-ev<N>-1113e*): рубрика, адрес, этаж/вход, телефон, сайт, услуги с ценами и возрастами групп. WebFetch не использовался.
Точка — справка OSM (auto/osm-answers.json, edu13-*), tools/edu_1113_pick.py: объект OSM места или здание строго по адресу.
Отброшены: дубли (Лисёнок Монтессори, Бэби-клуб на Профсоюзной уже есть другие; филиалы сетей, уже стоящие на карте),
клиники и диагностические центры, общеобразовательные школы и детские сады без кружков, карточки без возраста групп
(ЛФК-кабинеты, часть логопедов — на следующий запуск), карточки без номера дома.
Запуск: KP_PART=edu python3 tools/add_edu_1113.py [--dry]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC
from edu_1113_sel import SEL

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
DT = "2026-11-11"
PTS = json.load(open(os.path.join(HERE, "edu_1113_points.json")))
ADDR = json.load(open(os.path.join(HERE, "edu_1113_addr.json")))
YA = "Яндекс Карты: карточка организации (рубрика, адрес, этаж/вход, телефон, сайт, услуги, цены и возраст групп), выдача «{q}», 11.11.2026"
HOW = {
    "summa-tekhnologiy-butlerova": "Этаж: 1\nДомофон: 100",
    "anglichanka-profsoyuznaya": "Этаж: 4",
    "cherryville-profsoyuznaya": "Этаж: 1",
    "raznotsvetnye-tsyplyata-profsoyuznaya": "Этаж: 2",
    "estetik-altufyevskoe-56": "Этаж: 1",
    "sunrise-montessori-leninsky-83": "Вход: подъезд 1\nЭтаж: 1",
    "begemontiki-novoyasenevsky": "Этаж: 2",
    "iq007-rokotova": "Вход: со двора через серую калитку, позвонить в звонок\nЭтаж: 2",
    "radost-borisovskie-prudy-8": "Этаж: 2",
    "radost-borisovskie-prudy-20": "Этаж: 1",
    "radost-brateevskaya-21": "Этаж: 1",
    "montessori-volshebnaya-strana": "Вход: подъезд 3",
    "lucky-owl-borovskoe-20": "Этаж: 1",
    "roboteh-club-rusanova": "Этаж: 1, кабинет 101",
    "neiropsikhologiya-9-parkovaya": "Этаж: 2",
    "neiropsikholog-fokeeva-rusanova": "Этаж: 1",
    "karamelki-bratislavskaya": "Вход: подъезд 2\nЭтаж: 4",
    "interyes-lyublinskaya": "Вход: в БЦ «Марьино»\nЭтаж: 4",
    "las-mamas-admirala-lazareva": "Этаж: 1",
    "zelenaya-volna-yuzhnobutovskaya": "Этаж: 2",
    "nastenka-starokachalovskaya": "Этаж: 1",
    "kids-up-rokossovskogo": "Этаж: 2\nДомофон: 12",
    "sovenok-zashchitnikov-moskvy": "Вход: со стороны двора",
    "junlab-odintsovo": "Этаж: 6, офис 608/2",
    "tochka-sborki-odintsovo": "Этаж: 2, помещение 102",
}


def row(n):
    pid, name, typ, cats, a0, a1, price, note, plus, tags, trial = SEL[n]
    a = ADDR[pid]
    lat, lon, acc = PTS[pid]
    addr = a["addr"]
    if addr.endswith(", Одинцово") or addr.endswith(", Щёлково"):
        town = addr.rsplit(", ", 1)[1]; addr = f"{town}, {addr.rsplit(', ', 1)[0]}"
    r = P(pid, name, typ, metro(lat, lon), addr, lat, lon, a0, a1, 45, 60, "спокойно", tags, price, note, None, "да",
          plus, None, adult=1, src=YA.format(q=a["q"].replace(" | ", " метро ")), acc=acc, adult_price=None,
          booking="обязательна", loud="нет", sit="частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = a["site"]
    r["Категории"] = cats
    r["Как найти"] = HOW.get(pid)
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(n) for n in SEL if SEL[n][0] in PTS]

if __name__ == "__main__":
    pa = json.load(open(os.path.join(ROOT, "places-all.json")))
    PL = {p["id"] for p in (pa["places"] if isinstance(pa, dict) else pa)}
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in PL], [i for i in ids if i in existing or i in PL]
    if "--dry" in sys.argv:
        print(len(ROWS)); sys.exit()
    r0 = 2 if ws.max_row == 1 or ws.cell(row=2, column=1).value is None else ws.max_row + 1
    for n, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = r0 + n
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS))
