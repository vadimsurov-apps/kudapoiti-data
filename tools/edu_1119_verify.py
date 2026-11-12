"""Пачка для tools/set_verified.py по местам робота edu 12.11 (девятый запуск): поля, подтверждённые карточкой Яндекс Карт
(и сайтами центров), + доступная среда (урок 10) из блока «Особенности» карточки.
python3 tools/edu_1119_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1119 import ROWS, E, PTS, access, SITE_SRC
from edu_1119_sel import SEL

PROG = {  # что продумано для особых детей — только факты из карточки/сайта
 "smelost-mechtat-pudovkina": "центр для детей с особенностями развития (РАС, задержка речевого развития) от 1 года: логопед, адаптивная физкультура (АФК), музыкальные занятия, программа PEAK, пищевой тренинг",
 "lisenok-sema-shokalskogo": "арт-терапия для детей с ОВЗ, нейропсихолог для детей с ОВЗ",
 "alye-parusa-naro-fominsk": "занятия для детей с ОВЗ 4–15 лет: дети с РАС, задержкой психического и речевого развития, нарушениями интеллекта",
 "belyi-grach-maryinsky-park": "помощь детям с РАС, СДВГ, ЗРР, ЗПР: сенсорная интеграция с 1 года, игровая терапия, инструктор по адаптивной физкультуре",
 "iris-aba-yurlovsky": "АВА-терапия и тренинги навыков для детей с РАС, СДВГ, ЗПР; логопед при задержке речи с 2 лет",
 "mir-skhodnya": "комплексная помощь детям с особенностями развития: занятия для детей с ОВЗ, занятия в паре для детей с РАС и ЗПР 5–6 лет, нейрологопед",
 "orange-mama-ivanteevka": "занятия для детей с аутизмом: нейропсихолог, дефектолог, коррекционный педагог, нейрологопедия",
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
