"""Робот edu, 2026-11-13 (четырнадцатый запуск): 1) места, отложенные запусками 1122–1123 (карточки и точки готовы,
иконки — tools/icons_edu_1123.py и tools/icons_edu_1124.py); 2) новые «Особым детям» — карточки Яндекс Карт *-ev<N>-1124e* / *-ex<N>-1124e*
(tools/edu_1124_sel.py). Строка таблицы — функция row() из add_edu_1121.py. Запуск: KP_PART=edu python3 tools/add_edu_1124.py [--dry]"""
import json, os, sys, io, contextlib, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1123 as A23
A = A23.A
from batch_helpers import SRC
from edu_1124_sel import SEL as SEL24, SITE_SRC as SS24, HOW_FIX as HF24
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
for suf, fn in (("24:", "edu_1124_ext.json"), ("24x:", "edu_1124_ext2.json")):
    if os.path.exists(os.path.join(HERE, fn)):
        A.E.update({suf + k: v for k, v in json.load(open(os.path.join(HERE, fn))).items()})
_pp = os.path.join(HERE, "edu_1124_points.json")
A.PTS.update(json.load(open(_pp)) if os.path.exists(_pp) else {})
_page = A.page
def _page24(n):
    """второй заход: «24x:N» — страницы *-ex<N>-1124e*"""
    if n.startswith("24x:"):
        f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ex{n[4:]}-1124e-*.txt"))[0]
        secs = open(f).read().split("\n### ")
        return [l.strip() for l in "\n".join([secs[0]] + [s for s in secs[1:] if s.startswith("https://yandex.ru/maps/org/")]).splitlines() if l.strip()]
    return _page(n)
A.page = _page24
A.SEL.update(SEL24); A.SITE_SRC.update(SS24); A.HOW_FIX.update(HF24)
A.DT = "2026-11-13"
A.YA = A.YA.replace("12.11.2026", "13.11.2026") if "24" else A.YA
SEL = A.SEL
# Отложенные (точка + иконка готовы): новые направления (программирование, чтение, сады) и специалисты.
TAKE_DEF = ["coddy-timura-frunze", "ida-school-leninsky", "pixel-khodynsky", "kiberone-shelikhova", "kiberone-lobachevskogo",
            "andreev-kolobovsky", "mamiki-kids-ermolaevsky", "smile-khodynsky", "twinkle-kids-luzhniki", "sozvezdie-garibaldi",
            "poslushayka-elektrolitny", "zdorovy-rebenok-skandinavsky", "uspeh-korolyov-gorkogo", "sonechka-khimki-sovkhoznaya",
            "puteshestvie-rechi-lavrinenko", "kosmos-montessori-novorogozhskaya", "uh-ty-kub-mikhaylova", "milgrad-vladimirskaya"]
INCL_DEF = ["akademiya-rechi-novocheryomushkinskaya"]
NDEF = int(os.environ.get("EDU_NDEF", len(TAKE_DEF)))
NEW = [p for p in SEL24 if p in A.PTS]
IDS = INCL_DEF + NEW + TAKE_DEF[:NDEF]
IDS = [p for p in IDS if p in A.PTS]
ROWS = [A.row(p) for p in IDS]

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
    ROWS = [r for r in ROWS if r["id"] not in existing and r["id"] not in PL]
    if "--dry" in sys.argv:
        for r in ROWS: print(r["id"], "|", r["Адрес"], "|", (r["Как найти"] or "").replace("\n", " / "), "|", r["Метро"], "|", r["Сайт"], "|", r["Категории"], r["Возраст от"], r["Возраст до"], "|", r["Точность координат"][:40])
        print(len(ROWS)); sys.exit()
    r0 = ws.max_row + 1
    while r0 > 2 and ws.cell(row=r0 - 1, column=1).value is None: r0 -= 1
    for k, row_ in enumerate(ROWS):
        assert not (set(row_) - set(hdr)), (row_["id"], set(row_) - set(hdr))
        for i, name in enumerate(hdr, 1):
            c = ws.cell(row=r0 + k, column=i, value=row_.get(name))
            c.font = body; c.border = border
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(SRC)
    print("rows", len(ROWS))
