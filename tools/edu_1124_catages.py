"""Возраст по направлениям (урок 8) у мест робота edu, четырнадцатый запуск: отложенные — из tools/edu_1121_catages.py и
описаний карточек 1122 (SEL), новые — из карточек Яндекс Карт и сайтов. python3 tools/edu_1124_catages.py → дописывает auto/cat-ages.json."""
import json, os, sys, io, contextlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
with contextlib.redirect_stdout(io.StringIO()):
    import add_edu_1124 as A23
src = open(os.path.join(ROOT, "tools/edu_1121_catages.py")).read()
CAT21 = eval(re.search(r"CATAGES = (\{.*?\n\})\n", src, re.S).group(1))
Y = "Яндекс Карты, карточка организации, услуги: "
NEW = {
 # отложенные 1122 (карточки Яндекс Карт 12.11)
 "kosmos-montessori-novorogozhskaya": ({"montessori": [0, 3]}, "«Монтессори-группа «Вместе с мамой» с 8 месяцев до 3 лет»"),
 "uh-ty-kub-mikhaylova": ({"early": [0, 3], "robotics": [5, 12]}, "«Малыш + Ко» от 9 месяцев, «Тяп-ляп» 1–3 года, «Робототехника 5–12 лет»"),
 "luchik-sokol": ({"kindergarten": [1, 7]}, "«Детский сад от 1,5 до 7 лет»"),
 "milgrad-vladimirskaya": ({"early": [1, 3], "school": [4, 7], "languages": [4, 12], "robotics": [4, 12]}, "«Раннее развитие 1–3 года», «Подготовка к школе 4–5 и 6–7 лет», «Английский 4–12 лет», «Робототехника 4–12 лет»"),
 "vershina-mytishchi": ({"school": [5, 7]}, "«Подготовка к школе 5–7 лет»"),
 "kubik-sokolovskogo": ({"coding": [5, 15]}, "«Scratch Junior 5–7 лет», «Minecraft и Roblox для 1–7 классов», «Blender для 5–9 классов»"),
 "ladushki-kuchino": ({"psych": [3, 10]}, "«Нейропсихолог для детей 3–10 лет»"),
 "talantika-mytishchi": ({"reading": [8, 11]}, "«Скорочтение и каллиграфия 8–11 лет»"),
 "mamin-chasik-shipilovskaya": ({"kindergarten": [3, 6]}, "«Мини-сад для детей 3–6 лет»"),
}
from edu_1123_sel import CATAGES as C23
from edu_1124_sel import CATAGES as C24
NEW23 = {**C23, **C24}
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in A23.ROWS}
n = 0
for pid, v in {**{k: v for k, v in CAT21.items() if v}, **NEW, **NEW23}.items():
    if pid in ids:
        ages, txt = v
        data[pid] = {**ages, "src": (txt if txt.startswith("сайт") else Y + txt) + "; 13.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
