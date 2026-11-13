"""Пачка для tools/set_verified.py по местам робота edu 13.11 (пятнадцатый запуск): поля, подтверждённые карточкой
Яндекс Карт (и сайтами центров), + доступная среда (урок 10) из блока «Особенности» карточки и сайтов.
python3 tools/edu_1124_verify.py > batch.json"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1125 as A24
    from edu_1124_sel import PROG as PROG24x, SENS as SENS24x
    from edu_1122_verify import PROG as PROG22
    from edu_1123_sel import PROG as PROG23, SENS as SENS23
A = A24.A
from edu_1125_sel import PROG as PROG24, SENS as SENS24, ACCESS_EXTRA
PROG = {**PROG22, **PROG23, **PROG24x, **PROG24}
SENS = {**SENS23, **SENS24x, **SENS24}
out = {}
for r in A24.ROWS:
    pid = r["id"]; v = A.SEL[pid]; o = A.E[v[0]]
    day = "13.11.2026" if v[0].startswith(("23", "24", "25")) else "12.11.2026"
    src = f"Яндекс Карты, карточка организации и выдача «{o['q']}» ({day})" + (f"; {A.SITE_SRC[pid]}" if pid in A.SITE_SRC else "")
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": v[4], "age_max": v[5]}
    if o.get("phone"):
        f["phone"] = o["phone"].split(" (доб")[0]
    if r.get("Сайт"):
        f["url"] = r["Сайт"]
    if v[6]:
        f["price_child"] = v[6]
    if r.get("Как найти"):
        f["how"] = r["Как найти"]
    lat, lon, acc = A.PTS[pid]
    if acc.startswith("точно (объект:"):
        f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": acc}
    a = A.access(v[0], PROG.get(pid))
    if SENS.get(pid): a["sensory"] = SENS[pid]
    a.update(ACCESS_EXTRA.get(pid, {}))
    if a:
        f["access"] = a
    out[pid] = {"fields": f, "src": src}
print(json.dumps(out, ensure_ascii=False, indent=1))
