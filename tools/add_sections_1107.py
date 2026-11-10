"""Робот sections, 2026-11-06 (ночь, 21 UTC): бадминтон (СШОР МГФСО, БК «Красногорск»), волейбол/баскетбол
(RusVolley, Русская баскетбольная академия, JUNIBASKET, пляжный волейбол Beach Volleyball), шахматы (ChessKids, Chess First,
«Совёнок», «Гроссмейстер», Moscow Chess School, «Феномен»), прочий спорт (фехтование, настольный теннис, лёгкая атлетика,
парусный спорт), секции Подмосковья (гимнастика Перевозникова, ДСШ Яковлева, Raviga, «Русский самурай», Hockey Way,
Первая школа тенниса, «Футландия»), бассейны («Шторм», «Триумф»), балет и танцы («Азбука балета», «Вортэкс», TDANCE).
Источники — WebSearch → WebFetch только по ссылкам из поиска (проверено 2026-11-06), сырые записи в
tools/sections_1107_data.json (поле source). Не брали: подтверждённые только каталогами (50chess, kartasporta, yandex/zoon
без сайта), часть залов RusVolley и «Шторма» рядом с уже добавленными бассейнами/залами.
Координаты — по метро или по городу («приблизительно»), уточнит geocode-address.yml.
Запуск: KP_PART=sections python3 tools/add_sections_1107.py [--dry]"""
import json, os, re, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import add_sections_1106 as A
from add_sections_1106 import at, ST, SRC
from add_batch14 import MET

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sections_1107_data.json")
D = "проверено 2026-11-06"
MO = "приблизительно, ±1–2 км (по адресу)"

DROP = set("""akademiya-shahmat-korolev chess-vostochny-balashikha ddyut-chess-lyubertsy triatlonia-kuzminki ssh26-canoe-samotechny
labirint-archery-kurskaya 40-love-odintsovo junior-podolsk fse-nakhabino mitsuden-mytishchi derzhava-odintsovo-sshor
fetisov-academy-domodedovo joy-dance-balashikha flash-fencing-mitino shtorm-altayskiy shtorm-yauza shtorm-luzhniki
shtorm-krylatskie shtorm-mgtu shtorm-guu shtorm-misis rusvolley-yablochkova rusvolley-nikulinskaya rusvolley-saltykovskaya
rusvolley-aviamotornaya rusvolley-olimpiyskaya-derevnya rusvolley-samory-mashela rusvolley-800-letiya
rusvolley-kolomenskaya-nab rusvolley-litovsky rusvolley-tsimlyanskaya
vortex-dance-center tdance-tango-aviapark""".split())   # последние два — уже есть (vortex-dance, tdance-tango-tsska)

# координаты по адресу (приблизительно) для мест без метро в справочнике
XY = {"mgfso-badminton-michsport": (55.6364, 37.3216), "badminton-club-krasnogorsk": (55.8240, 37.3170),
      "rba-basket-logos": (55.6900, 37.2480), "rba-basket-skolka": (55.6980, 37.3580), "rba-basket-sportville": (55.8400, 37.1830),
      "junibasket-mytishchi": (55.9180, 37.7350), "chesskids-mytishchi": (55.9120, 37.7370), "chesskids-smolnaya": (55.8600, 37.4830),
      "chess-first-mytishchi": (55.9030, 37.7180), "sovenok-chess-korolev": (55.9100, 37.8580),
      "grossmeyster-zhukovsky": (55.5980, 38.1220), "grossmeyster-ramenskoe": (55.5740, 38.2150),
      "moscow-chess-school-khimki": (55.8860, 37.4320), "fenomen-chess-krasnogorsk": (55.8170, 37.3600),
      "flash-fencing-krasnogorsk": (55.8250, 37.3200), "flash-fencing-istra": (55.9170, 36.8600),
      "flash-fencing-ramenskoe": (55.5630, 38.2300), "galaktika-fencing-mytishchi": (55.9200, 37.7600),
      "vodnik-sailing-dolgoprudny": (55.9350, 37.5170), "ignis-athletics-tenisty": (55.8930, 37.5860),
      "perevoznikov-korolev": (55.9270, 37.8100), "perevoznikov-krasnogorsk": (55.8230, 37.3340),
      "perevoznikov-vidnoe": (55.5530, 37.7050), "perevoznikov-pushkino": (56.0080, 37.8480),
      "perevoznikov-khimki": (55.8850, 37.4300), "yakovlev-balashiha-olgino": (55.7330, 38.0000),
      "yakovlev-balashiha-yubileynaya": (55.7440, 38.0100), "yakovlev-balashiha-sovetskaya": (55.7520, 38.0180),
      "yakovlev-korolev-yubileyny": (55.9370, 37.8380), "yakovlev-reutov": (55.7630, 37.8560),
      "raviga-khimki-skhodnya": (55.9480, 37.3000), "raviga-khimki-mayakovskogo": (55.8960, 37.4450),
      "raviga-krasnogorsk": (55.8360, 37.3580), "rusamurai-ramenskoe-saturn": (55.5680, 38.2370),
      "rusamurai-zhukovsky": (55.5950, 38.1150), "hockeyway-mytishchi": (55.9150, 37.7670),
      "hockeyway-khimki": (55.8750, 37.4800), "psht-krasnogorsk-zenit": (55.8245, 37.3190),
      "psht-dolgoprudny": (55.9500, 37.5350), "footlandiya-dolgoprudny-salyut": (55.9280, 37.5200),
      "footlandiya-mytishchi": (55.9000, 37.7000), "footlandiya-balashiha": (55.8000, 37.9400),
      "footlandiya-khimki-skhodnya": (55.9530, 37.3050), "shtorm-sputnik-zelenograd": (55.9850, 37.2050),
      "triumf-umka": (55.8660, 37.4750), "triumf-mytishchi-astrakhova": (55.9060, 37.7220),
      "triumf-mytishchi-brigantina": (55.9170, 37.7730), "triumf-mytishchi-letnaya": (55.9250, 37.7120),
      "azbuka-baleta-khimki": (55.9040, 37.3980)}

KIND = {"badminton": ("спортивная секция", "спорт и активность", (60, 90)),
        "ballgames": ("спортивная секция", "спорт и активность", (60, 90)),
        "chess": ("шахматный клуб", "логика и головоломки", (60, 90)),
        "sport": ("спортивная секция", "спорт и активность", (60, 90)),
        "martial": ("спортивная секция", "спорт и активность", (45, 90)),
        "gymnastics": ("спортивная секция", "спорт и активность", (45, 90)),
        "racket": ("спортивная секция", "спорт и активность", (45, 90)),
        "hockey": ("спортивная секция", "спорт и активность", (45, 90)),
        "football": ("спортивная секция", "спорт и активность", (45, 60)),
        "pools": ("детский бассейн", "вода, спорт и активность", (45, 60)),
        "dance": ("танцевальная студия", "музыка, спорт и активность", (45, 60))}


def mdist(lat, lon):
    return min((math.hypot((lat - a) * 111, (lon - b) * 63), n) for n, a, b in MET)


def clean_addr(a):
    a = re.sub(r"^(Московская обл\.,\s*)", "", a.strip())
    a = re.sub(r"^Москва,\s*", "", a)
    a = re.sub(r"^г\.\s*", "", a)
    return a


def load():
    raw = json.load(open(DATA))
    out = []
    for x in raw:
        if x["id"] in DROP: continue
        m = (x.get("metro") or "").split(" (")[0].strip()
        if x["id"] in XY:
            lat, lon = XY[x["id"]]
            km, st = mdist(lat, lon)
            loc = (lat, lon, st if km < 2.0 else None, MO)
        elif m and m.lower().replace("ё", "е") in ST:
            loc = at(m)
        else:
            raise SystemExit(f"нет координат: {x['id']} {m}")
        typ, tags, d = KIND[x["cat"]]
        if x["cat"] == "dance" and "балет" in x["name"].lower(): typ = "балетная школа"
        if "водн" in x.get("sport", "") or x["id"].startswith("vodnik"): tags = "вода, спорт и активность"
        price = x.get("price")
        note = x.get("price_note") or ("бесплатно" if price == 0 else None)
        r = A.row(x["id"], x["name"], typ, loc, clean_addr(x["address"]), x["age_from"], x["age_to"], d[0], d[1], tags,
                  price, note, None, x["plus"], x["minus"], x["url"], x["cat"], src=f"{x['source']} ({D})")
        r["Детский билет, ₽"] = price
        r["Взрослый билет, ₽"] = None
        out.append(r)
    return out


ROWS = load()

if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    existing = {ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)}
    allp = json.load(open(os.path.join(ROOT, "places-all.json")))["places"]
    allids = {x["id"] for x in allp}
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids)), "повтор id"
    assert not [i for i in ids if i in existing or i in allids], [i for i in ids if i in existing or i in allids]
    # дубли: то же название (первые слова) ближе 300 м
    import glob
    pts = [(p["name"], p["lat"], p["lon"]) for p in allp]
    for f in glob.glob(os.path.join(ROOT, "data", "parts", "*.xlsx")):
        rr = list(openpyxl.load_workbook(f, read_only=True)["Места"].values); h = rr[0]
        pts += [(r[h.index("Название")], r[h.index("Широта")], r[h.index("Долгота")]) for r in rr[1:] if r[h.index("Широта")]]
    key = lambda n: re.sub(r"[«»\"()—,.-]", " ", str(n).lower()).split()[:2]
    for r in ROWS:
        for n, a, b in pts:
            if a and math.hypot((r["Широта"] - a) * 111000, (r["Долгота"] - b) * 63000) < 300 and key(n) == key(r["Название"]):
                print("ДУБЛЬ?", r["id"], "~", n)
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Название"], "|", r["Метро"], "|", r["Категории"], "|", r["Широта"], r["Долгота"])
        from collections import Counter
        print("rows", len(ROWS), Counter(r["Категории"] for r in ROWS)); sys.exit()
    body = Font(name="Arial", size=10)
    thin = Side(style="thin", color="D0D0D0")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row_ in ROWS:
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        r = ws.max_row + 1
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS), "total", ws.max_row - 1)
