"""Робот creative, 2026-11-11 (первый запуск). Поиск по районам Авиамоторная … Бабушкинская (14 станций метро) —
выдачи Яндекс Карт по 7 темам (танцы, балет, вокал, музыкальная школа, театральная студия, рисование, гончарная
мастерская; auto/pages *-cs<N>-1111c*). Каждое место сверено с карточкой организации (*-cv<N>-1111c*: рубрика,
адрес, этаж/вход, телефон, сайт, услуги с ценами и возрастом групп) и с сайтом места (auto/pages, возраст групп
набора). Отброшены: без возраста групп, только взрослые, аренда залов, разовые мастер-классы (это робот fun),
дубли уже стоящих мест (Ирбис, IDC, ГрандБалет, Сердце балета, Гончарная «Среда», Dance Class и др.).
Точка — справка OSM (cr2-*, tools/creative_1111_pick.py): объект OSM места или здание строго по адресу.
WebFetch не использовался. Запуск: KP_PART=creative python3 tools/add_creative_1111.py [--dry]"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from add_batch14 import metro
from batch_helpers import P, SRC
from creative_1111_sel import SEL

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
DT = "2026-11-11"
PTS = json.load(open(os.path.join(HERE, "creative_1111_points.json")))
CARD = json.load(open(os.path.join(HERE, "creative_1111_cards.json")))

NAMES = {
    "donner-ballet-krasnokazarmennaya": "Школа балета Марианны Доннер (Лефортово)",
    "flying-dreams-kabelny": "Школа брейкинга Flying Dreams (Лефортово)",
    "art-insight-avtozavodskaya": "Школа рисования «Арт Инсайт» (ТЦ «Ривьера»)",
    "russkaya-rech-vlasova": "Театральная студия «Русская речь» (Новые Черёмушки)",
    "nat-profsoyuznaya": "Театральная студия «НАТ 2.0» (Профсоюзная)",
    "detal-ceramics-shukhova": "Студия керамики «Деталь» (у Шуховской башни)",
    "rnbsh-gnezdnikovsky": "Русская национальная балетная школа (Тверская)",
    "akademiya-krutogo-myasnitskaya": "Академия Игоря Крутого (Мясницкая)",
    "action-krasny-oktyabr": "Театральная студия Action (Красный Октябрь)",
    "lisse-arbat": "Театральная школа-студия «ЛиссЭ» (Арбат)",
    "buff-fadeeva": "Театральная студия «Буфф» (Новослободская)",
    "rnbsh-maryinskaya": "Русская национальная балетная школа (Марьина Роща)",
    "dykhanie-zvuka-mytishchinskaya": "Студия вокала «Дыхание звука» (Алексеевская)",
    "free-voice-lab-olminskogo": "Студия вокала и хор Free Voice Lab (Алексеевская)",
    "teatr-mira-mytishchinskaya": "Театральная студия «Театр-Мира» (Алексеевская)",
    "yaro-mira-150": "Гончарная студия YarO (ВДНХ)",
    "guitar-school-1-krasnokazarmennaya": "Гитарная школа № 1 (Лефортово)",
    "start-brateevskaya": "Студия рисования «СтАрт» (Братеево)",
    "vozdukh-muranovskaya": "Школа танцев «Воздух» (Бибирево)",
    "muz-dorozhka-altufyevskoe": "Музыкальная студия «Музыкальная дорожка» (Алтуфьево)",
    "kidsvoks-matveevskaya": "Студия вокала «КидсВокс» (Матвеевское)",
    "ritm-mosfilmovskaya": "Центр искусств «Ритм» (Мосфильмовская)",
    "volna-ceramics-oktyabrsky": "Студия керамики Volna (Марьина Роща)",
    "soul-dance-entuziastov": "Школа танцев Soul Dance (ш. Энтузиастов)",
    "triumf-varshavskoe": "Шоу-театр «Триумф» (Аннино)",
    "viktoriya-khor-annino": "Музыкально-хоровая студия ДЮЦ «Виктория» (Аннино)",
    "shum-gazoprovod": "Театральная студия «Шум» (Аннино)",
    "arbatclass-sivtsev": "Балетная студия «Арбаткласс» (Арбат)",
    "cbs-sivtsev-45": "Центральная балетная школа (Арбат)",
    "nikolaev-choreo-arbat": "Мастерская хореографии Антона Николаева (Арбат)",
    "dosimi-novopeschanaya": "Музыкальная студия «ДоСиМи и STARше» (Сокол)",
    "azart-supruna": "Театральная студия «АзАрт+» (Аэропорт)",
    "invibe-vnukovo": "Школа танцев Invibe (Внуково)",
    "tri-chetverti-vnukovo": "Музыкальная школа «Три четверти» (Внуково)",
    "paint-school-vnukovo": "Студия рисования и лепки (Внуково, ул. Лётчика Грицевца)",
    "tertsiya-lenskaya": "Центр искусств «Терция» (Бабушкинская)",
    "guitar-school-1-starovatutinsky": "Гитарная школа № 1 (Бабушкинская)",
    "kupina-ivovaya": "Школа музыки Екатерины Купиной (Свиблово)",
    "act-place-polyarnaya": "Театральная студия «Акт Плэйс» (Медведково)",
    "vorontsova-ballet-mira": "Балетная студия «Воронцова-балет» (Рижская)",
    "art-pokolenie-krasnoarmeyskaya": "Студия рисования «Art Поколение» (Аэропорт)",
}
TAGS = {"dance": "спорт и активность, музыка", "ballet": "спорт и активность, музыка", "singing": "музыка",
        "music": "музыка", "theaterstudio": "сказки и театр, творчество", "drawing": "творчество",
        "ceramics": "творчество"}


def addr(a):
    a = a.replace("Москва, Новомосковский административный округ, район Внуково, улица", "Внуково, ул.")
    a = re.sub(r"^Москва, |, Москва$", "", a)
    return a


HOW = {
    "art-insight-avtozavodskaya": "Вход: через ТЦ «Ривьера»\nЭтаж: 2",
    "action-krasny-oktyabr": "Ориентир: территория «Красного Октября»",
    "lisse-arbat": "Этаж: 3, аудитория 346",
    "dykhanie-zvuka-mytishchinskaya": "Этаж: 7, аудитория 709",
    "volna-ceramics-oktyabrsky": "Этаж: 2, офис 16",
    "azart-supruna": "Вход: через библиотеку, зал направо",
    "art-pokolenie-krasnoarmeyskaya": "Этаж: цокольный",
}


def how(c, pid=None):
    if pid in HOW:
        return HOW[pid]
    t = c.get("addr2") or ""
    t = re.sub(r"Метро: [^,]+, [^,]+, ", "", t)
    if not t or t.startswith("Организация"):
        return None
    out = []
    for part in [p.strip() for p in t.split(",")]:
        m = re.match(r"этаж (.+)", part, re.I)
        if m:
            out.append("Этаж: " + m.group(1).replace("цокольный", "цокольный").replace("Второй", "2")); continue
        m = re.match(r"(офис|кабинет|комната|аудитория|ауд\.)\s*(.+)", part, re.I)
        if m:
            out.append("Помещение: " + part); continue
        out.append("Вход: " + part[0].lower() + part[1:] if part.lower().startswith(("вход", "свой вход")) else "Ориентир: " + part)
    return "\n".join(out) or None


def row(pid, typ, cats, a0, a1, plus):
    c = CARD[pid]
    lat, lon, acc = PTS[pid]
    first = cats.split(",")[0]
    active = first in ("dance", "ballet")
    r = P(pid, NAMES[pid], typ, metro(lat, lon), addr(c["address"]), lat, lon, a0, a1, 45, 90,
          "активно" if active else "спокойно", TAGS[first], None, None, None, "да", plus, None, adult=1,
          src=f"Яндекс Карты: карточка организации (рубрика, адрес, этаж/вход, телефон, сайт, услуги, возраст групп), "
              f"выдача «{c['q']}», 11.11.2026; сайт {c['site'] or '—'} (возраст групп)",
          acc=acc, adult_price=None, booking="обязательна", loud="частично" if active or first == "music" else "нет",
          sit="нет" if active else "частично", crowd="нет", food="нет", stroller="частично")
    r["Взрослый билет, ₽"] = None
    r["Сайт"] = ("https://" + c["site"].lower()) if c.get("site") else None
    r["Категории"] = cats
    r["Как найти"] = how(c, pid)
    r["Проверено (дата)"] = DT
    return r


ROWS = [row(v[0], v[1], v[2], v[3], v[4], v[5]) for v in SEL.values() if v[0] in PTS]

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
        for r in ROWS:
            print(r["id"], "|", r["Адрес"], "|", r["Как найти"], "|", r["Метро"])
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
