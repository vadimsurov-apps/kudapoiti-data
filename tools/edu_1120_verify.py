"""Пачка для tools/set_verified.py по местам робота edu 12.11 (десятый запуск): поля, подтверждённые карточкой Яндекс Карт
(и сайтами центров), + доступная среда (урок 10) из блока «Особенности» карточки.
python3 tools/edu_1119_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1120 import ROWS, E, PTS, access, SITE_SRC
from edu_1120_sel import SEL

PROG = {  # что продумано для особых детей — только факты из карточки/сайта
 "chernyak-perovskaya": "запуск речи у неговорящих детей, АВА-терапия, нейрологопедия, нейропсихолог, дефектологи",
 "altera-vita-musorgskogo": "занятия для детей 2–16 лет, в том числе с ЗПР, ЗРР, РАС, ОНР: сенсорная интеграция в оборудованном зале, Флортайм, логопед-дефектолог, нейропсихолог",
 "cns-neiro-zlatoustinsky": "нейропсихологи и занятия по сенсорной интеграции",
 "zdorovy-rebenok-fryazino": "АВА-терапия, DIR/Floortime-терапия, дефектолог, нейропсихолог, запуск речи с 2 лет",
 "zdorovy-rebenok-ivanteevka": "сенсорная интеграция, занятия по методу DIR Floortime, дефектолог, нейропсихолог",
}
out = {}
for r in ROWS:
    pid = r["id"]; v = SEL[pid]; o = E[v[0]]
    src = f"Яндекс Карты, карточка организации и выдача «{o['q']}» (12.11.2026)" + (f"; {SITE_SRC[pid]}" if pid in SITE_SRC else "")
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": v[4], "age_max": v[5]}
    if o.get("phone"):
        f["phone"] = o["phone"].split(" (доб")[0]
    if r.get("Сайт"):
        f["url"] = r["Сайт"]
    if v[6]:
        f["price_child"] = v[6]
    if r.get("Как найти"):
        f["how"] = r["Как найти"]
    lat, lon, acc = PTS[pid]
    if acc.startswith("точно (объект:"):
        f["point"] = {"lat": lat, "lon": lon, "level": "объект", "how": acc}
    a = access(v[0], PROG.get(pid))
    if a:
        f["access"] = a
    out[pid] = {"fields": f, "src": src}
print(json.dumps(out, ensure_ascii=False, indent=1))
