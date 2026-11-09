"""Робот cafes, 2026-11-09 (16 UTC): исправление карточек по правилам «Качество карточек» (Вадим 09.11).
Osteria Mario — сайт сети osteriamario.ru (кэш auto/pages/osteriamario-ru*.txt: «Итальянский семейный ресторан»,
список ресторанов «Наличие детской комнаты»: комната / уголок; мастер-классы по выходным 3–12 лет, без записи).
Додо Пицца — карточки Яндекс Карт (кэш auto/pages/yandex-*): рубрика «Пиццерия», «Ср. чек», аспект «Детская комната».
Vasilchuki Chaihona №1 / Чайхона №1 — сайты chaihona.ru / chaihona1.ru (кэш auto/pages).
Запуск: KP_PART=cafes python3 tools/fix_cafes_quality_1109.py"""
import glob, json, os, re, sys
import openpyxl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helpers import SRC

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MARK = "качество 2026-11"
FIX = {}  # id -> {колонка: значение}

# --- Osteria Mario ---
OM = "https://osteriamario.ru/ (список ресторанов с детской комнатой)"
OM_ROOM = {"metropolis", "sokol", "kapitoliy", "kashirskaya-plaza", "cdm", "krasny-kit", "akademik", "michurinsky",
           "kaluzhskaya", "kuntsevo-plaza", "crocus", "baykonur", "butyrskaya", "evropolis", "aviapark",
           "rumyantsevo", "riviera", "osenniy"}
OM_CORNER = {"vegas-kuntsevo", "barrikadnaya"}
OM_OTHER = {"okhotny", "paveletskaya"}  # нет в списке сети; детская — по описанию каталога
for k in OM_ROOM | OM_CORNER | OM_OTHER:
    corner = k in OM_CORNER
    what = "детский уголок" if corner else "детская комната"
    plus = ("Итальянский семейный ресторан: пицца, паста, ризотто, есть детское меню. "
            + ("Детский уголок с деревянными и текстильными игрушками" if corner else
               "Детская комната в эко-стиле с деревянными и текстильными игрушками" if k not in OM_OTHER else
               "Есть детская комната")
            + ". По выходным в ресторанах сети — бесплатные мастер-классы для детей 3–12 лет, без записи")
    minus = ("Отдельной детской комнаты нет, только уголок; мастер-классы — только по субботам и воскресеньям"
             if corner else "Мастер-классы для детей — только по субботам и воскресеньям")
    FIX["cafe-osteria-" + k] = {"Тип": f"семейный итальянский ресторан с {'детским уголком' if corner else 'детской комнатой'}",
                                "Плюс": plus, "Минус": minus, "_src": OM if k not in OM_OTHER else "https://osteriamario.ru/",
                                "_keep_check": 2000 if k in OM_OTHER else None}

# --- Додо Пицца: карточки Яндекс Карт ---
CARDS = {}
for f in glob.glob(os.path.join(ROOT, "auto/pages/yandex-*")):
    t = open(f, encoding="utf-8").read().split('{"config"')[0]
    if "Додо" in t[:600]:
        CARDS[f] = t


def dodo(pid, addr):
    city = addr.split(",")[0].strip()
    street = addr.split(",")[1].strip() if addr.count(",") >= 1 else addr
    hits = [t for t in CARDS.values() if city in t and street.split()[-1] in t]
    hits.sort(key=lambda t: "Детская комната ·" not in t)
    if not hits:
        return
    t = hits[0]
    m = re.search(r"Ср\. чек (\d+)–(\d+) ₽", t)
    corner = pid == "cafe-dodo-klin"
    fx = {"Тип": "пиццерия с детским уголком" if corner else "пиццерия с детской комнатой",
          "Плюс": "Пиццерия «Додо»: пицца, закуски, десерты и кофе. Есть " + ("детский уголок" if corner else "детская комната"),
          "Минус": None, "_src": "Яндекс Карты (карточка филиала: рубрика «Пиццерия», средний чек, отзывы о детской комнате)"}
    if m:
        lo, hi = int(m.group(1)), int(m.group(2))
        fx["Взрослый билет, ₽"] = lo if (hi <= lo or hi > 2 * lo) else int(round((lo + hi) / 2 / 50) * 50)
    FIX[pid] = fx


def main():
    wb = openpyxl.load_workbook(SRC)
    ws = wb["Места"]
    hdr = [c.value for c in ws[1]]
    col = {n: i + 1 for i, n in enumerate(hdr)}
    rows = {ws.cell(row=r, column=1).value: r for r in range(2, ws.max_row + 1)}
    for pid, r in rows.items():
        if pid.startswith("cafe-dodo-"):
            dodo(pid, ws.cell(row=r, column=col["Адрес"]).value or "")
    extra = os.environ.get("FIX_JSON")
    if extra:
        FIX.update(json.load(open(extra, encoding="utf-8")))
    n = 0
    for pid, fx in FIX.items():
        r = rows.get(pid)
        if not r:
            print("нет строки", pid); continue
        src = ws.cell(row=r, column=col["Источник"]).value or ""
        if MARK in src:
            continue
        ws.cell(row=r, column=col["Детский билет, ₽"]).value = None
        ws.cell(row=r, column=col["Бесплатно до (лет / см)"]).value = None
        if "Взрослый билет, ₽" not in fx:
            # средний чек оставляем, только если он был из источника-каталога с чеком; иначе пусто
            fx["Взрослый билет, ₽"] = fx.pop("_keep_check", None)
        add_src = fx.pop("_src", None)
        for k, v in fx.items():
            if k.startswith("_"):
                continue
            ws.cell(row=r, column=col[k]).value = v
        parts = [src] if src else []
        if add_src and add_src not in src:
            parts.append(add_src)
        parts.append(MARK)
        ws.cell(row=r, column=col["Источник"]).value = "; ".join(parts)
        ws.cell(row=r, column=col["Проверено (дата)"]).value = "2026-11-09"
        n += 1
    wb.save(SRC)
    left = sum(1 for rr in range(2, ws.max_row + 1) if MARK not in (ws.cell(row=rr, column=col["Источник"]).value or ""))
    print("исправлено", n, "осталось", left)


if __name__ == "__main__":
    main()
