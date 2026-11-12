"""Пачка для tools/set_verified.py по местам робота edu 12.11 (двенадцатый запуск): поля, подтверждённые карточкой Яндекс Карт
(и сайтами центров), + доступная среда (урок 10) из блока «Особенности» карточки и сайтов.
python3 tools/edu_1122_verify.py > batch.json"""
import json, os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1122 as A22
    import add_edu_1121 as A
    from edu_1121_verify import PROG
PROG = dict(PROG)
PROG.update({
 "dom-dlya-detey-s-ras-rybalko": "для детей с РАС: мини-группа полного дня 4–7 лет и старшая группа полного пребывания 9–14 лет, арт-студия и кулинарная мастерская",
 "minakova-kosmodemyanskikh": "для детей с РАС, ЗПР, СДВГ: ABA, АФК, коммуникативная группа, группа краткосрочного пребывания и подготовка к школе для особенных детей, ранняя коррекция с 12 месяцев",
 "semeyny-centr-orientir-pervomayskaya": "коррекционно-развивающие занятия для детей 3–5 лет с ЗПР, ЗПРР, ОНР; нейропсихолог",
 "logocentr-umnitsa-izmaylovo": "коррекционные группы для детей с ОВЗ, занятия с АВА-терапевтом с 3 лет, работа с детьми с РАС и задержкой речевого развития",
 "rechevye-shagi-mytishchi": "АВА-терапия, адаптивная физкультура, сенсорно-коммуникативная группа, музыкальная терапия, группа подготовки к школе для детей с ОВЗ 4–7 лет",
 "slovo-detyam-berzarina": "занятия для детей с аутизмом: логопеды-дефектологи и нейропсихолог",
 "podsolnukh-balashikha": "центр для детей с ОВЗ, созданный организацией родителей детей-инвалидов: дефектолог, DIR Floortime, сенсорная интеграция, АФК, социально-бытовая адаптация, группы дневного пребывания",
})
SENS = {"minakova-kosmodemyanskikh": None, "podsolnukh-balashikha": "специалист по сенсорной интеграции", "rechevye-shagi-mytishchi": "сенсорно-коммуникативная группа 3–5 лет"}
out = {}
for r in A22.ROWS:
    pid = r["id"]; v = A.SEL[pid]; o = A.E[v[0]]
    src = f"Яндекс Карты, карточка организации и выдача «{o['q']}» (12.11.2026)" + (f"; {A.SITE_SRC[pid]}" if pid in A.SITE_SRC else "")
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
    if a:
        f["access"] = a
    out[pid] = {"fields": f, "src": src}
print(json.dumps(out, ensure_ascii=False, indent=1))
