"""Пачка для tools/set_verified.py по местам робота edu 13.11 (двадцать первый запуск): поля, подтверждённые карточкой
Яндекс Карт (и сайтами центров), + доступная среда (урок 10) из блока «Особенности» карточки.
python3 tools/edu_1131_verify.py > batch.json"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1131 as A26
A = A26.A
from edu_1131_sel import PROG, SENS, ACCESS_EXTRA
out = {}
for r in A26.ROWS:
    pid = r["id"]; v = A.SEL[pid]; o = A.E[v[0]]
    src = f"Яндекс Карты, карточка организации и выдача «{o['q']}» (13.11.2026)" + (f"; {A.SITE_SRC[pid]}" if pid in A.SITE_SRC else "")
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": v[4], "age_max": v[5]}
    if o.get("phone") and o["phone"].startswith("+7"):
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
