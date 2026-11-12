"""Пачка для tools/set_verified.py по местам робота edu 12.11 (восьмой запуск): поля, подтверждённые карточкой Яндекс Карт
(и сайтами центров), + доступная среда (урок 10) из блока «Особенности» карточки.
python3 tools/edu_1118_verify.py > batch.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1118 import ROWS, E, PTS, access, SITE_SRC
from edu_1118_sel import SEL

PROG = {  # что продумано для особых детей — только факты из карточки/сайта
 "zdorovy-rebenok-kotelniki": "АВА-терапия, Бобат- и Войта-терапия, дефектология, ЛФК и детский массаж, нейропсихолог",
 "aba-na-ponyatnom-marksistskaya": "индивидуальные и групповые занятия для детей с РАС, ЗПР и СДВГ (2–14 лет): АВА, коммуникативные группы",
 "minakova-aba-remizova": "центр для детей и подростков с РАС, ЗРР, ЗПР: АВА, дефектолог, нейропсихолог, адаптивная физкультура, подготовка к школе детей с РАС",
 "malysharium-klin": "инклюзивная игровая комната для детей от 6 месяцев до 5 лет и детей с ОВЗ",
 "dvigai-zhizn-egoryevsk": "центр для детей с ОВЗ: адаптивная физкультура, Floortime, логопед, психолог, арт-терапия; занятия по социальным сертификатам для детей с инвалидностью",
 "tauber-studio-dolgorukovskaya": "курс «Солнечные дети» для детей с синдромом Дауна, инклюзивный театр, коррекционный вокал",
 "neyroklass-privolnaya": "работа с детьми с ОВЗ (РАС, ЗПРР, алалия, ТМНР): нейропсихологическая коррекция, речевое развитие",
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
