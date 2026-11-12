"""Возраст по направлениям (урок 8) у мест робота edu 12.11 (двенадцатый запуск): отложенные — из tools/edu_1121_catages.py,
новые «Особым детям» — из карточек Яндекс Карт и сайтов. python3 tools/edu_1122_catages.py → дописывает auto/cat-ages.json."""
import json, os, sys, io, contextlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1122 as A22
src = open(os.path.join(ROOT, "tools/edu_1121_catages.py")).read()
CAT21 = eval(re.search(r"CATAGES = (\{.*?\n\})\n", src, re.S).group(1))
Y = "Яндекс Карты, карточка организации, услуги: "
NEW = {
 "minakova-kosmodemyanskikh": ({"early": [1, 3]}, "«Мы работаем с малышами от 12 месяцев до 3 лет» (ранняя коррекция)"),
 "semeyny-centr-orientir-pervomayskaya": ({"inclusive": [3, 5]}, "«Коррекционно-развивающие занятия для детей от 3-5 лет с ЗПР, ЗПРР, ОНР»"),
 "logocentr-umnitsa-izmaylovo": ({"speech": [2, 12]}, "сайт logo-umnitsa.ru: «коррекции устной и письменной речи у детей 2-12 лет»"),
}
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in A22.ROWS}
n = 0
for pid, v in {**{k: v for k, v in CAT21.items() if v}, **NEW}.items():
    if pid in ids:
        ages, txt = v
        data[pid] = {**ages, "src": (txt if txt.startswith("сайт") else Y + txt) + "; 12.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
