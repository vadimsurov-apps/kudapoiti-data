"""Пачка для tools/set_verified.py по местам робота edu 12.11 (седьмой запуск): поля, подтверждённые карточкой Яндекс Карт
(и сайтами центров), + доступная среда (урок 10) из блока «Особенности» карточки.
python3 tools/edu_1117_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1117 import ROWS, E, PTS, access, SITE_SRC
from edu_1117_sel import SEL

PROG = {  # что продумано для особых детей — только факты из карточки/сайта
 "sash-korneychuka": "спортивно-адаптивная школа Москомспорта с бассейном",
 "abc-aba-volzhsky": "АВА-терапия и Денверская модель (ESDM) для детей с аутизмом, обучение родителей",
 "abc-aba-matveevskaya": "АВА-терапия и Денверская модель (ESDM) для детей с аутизмом, обучение родителей",
 "mayak-razvitiya-akademicheskaya": "нейропсихологическая диагностика и коррекция детей с СДВГ и ЗПР, дефектолог",
 "nsm-m-staraya-basmannaya": "центр для детей с РАС, ЗПР, ОНР: логопед-дефектолог, адаптивная физкультура",
 "neokids-zhebrunova": "индивидуальные программы для детей с РАС, ЗПР, ЗРР с 1 года: АВА, сенсорная интеграция, дефектолог",
 "center-3d-domodedovskaya": "дефектологи, нейропсихолог, логопед с 2 лет",
 "korrektsiya-rechi-noginsk": "логопед-дефектолог, нейропсихолог, сурдолог, сенсорная интеграция",
 "mir-oshchushcheniy-kommunarka": "сенсорная интеграция, адаптивная/лечебная физкультура, занятия для детей с РАС, ДЦП, СДВГ, СМА, ЗПР; интенсивы для детей с ОВЗ",
 "bukvarium-shumkina": "коммуникативные группы для детей 4–7 лет с РАС, АВА-терапия, адаптивная физкультура, дефектолог",
 "korrektsiya-rechi-zhulebinsky": "логопед-дефектолог: коррекция ЗРР и ЗПР, запуск речи",
}
out = {}
for r in ROWS:
    pid = r["id"]; v = SEL[pid]; o = E[str(v[0])]
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
