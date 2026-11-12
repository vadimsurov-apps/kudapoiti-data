"""Возраст по направлениям (урок 8) у мест робота edu 12.11 (восьмой запуск) — из названий услуг карточек Яндекс Карт и сайтов.
python3 tools/edu_1118_catages.py → дописывает auto/cat-ages.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1118 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "Яндекс Карты, карточка организации, услуги: "
CATAGES = {
 "zdorovy-rebenok-kotelniki": ({"psych": [2, 14]}, "«Консультация детского нейропсихолога (2-5 лет)», «(6-14 лет)»"),
 "minakova-aba-remizova": ({"early": [1, 3]}, "сайт aba-center.ru: «работаем с малышами от 12 месяцев до 3 лет»"),
 "malysharium-klin": ({"early": [0, 3], "inclusive": [0, 5]}, "сайт maliysharium.ru: «Групповые развивающие занятия (от 9 мес до 3 лет)», «игровая комната для детей от 6 месяцев до 5 лет»"),
 "tauber-studio-dolgorukovskaya": ({"early": [0, 6], "singing": [3, 17]}, "сайт tauber-school.ru: «с 9 месяцев до 6 лет», «Уроки вокала для детей от 3 лет»"),
 "neyroklass-privolnaya": ({"school": [5, 6], "speech": [1, 12]}, "«Подготовка к школе, 5-6л», «Диагностика речевого развития: от 1,5 лет»"),
 "baby-club-obolensky": ({"early": [0, 5]}, "«Развивающие занятия для детей от 8 месяцев до 2,5 лет», «2,5-5 лет»"),
 "sandpro-krylatskie-kholmy": ({"school": [5, 7], "drawing": [3, 14]}, "«Подготовка к школе СэндПРО (от 5,5 до 7 лет)», «Художественная студия (от 3 лет)», «Глубинные чувства (с 11 до 14 лет)»"),
 "iq007-shvernika": ({"school": [4, 14], "robotics": [7, 14]}, "«Детей от 4 лет научим…», «Программирование и робототехника для детей 7–14 лет»"),
 "sunrise-montessori-leninsky": ({"early": [0, 3]}, "«Группа мама и малыш от 2 мес», «Группа от 1,5 до 3 лет»"),
 "strana-detstva-klin": ({"school": [4, 7], "robotics": [6, 17]}, "«Курс для дошколят 4-5 лет», «Подготовка к школе 6-7 лет», «Робототехника для детей от 6 лет»"),
 "deti-v-teme-vavilova": ({"school": [5, 7], "languages": [5, 15]}, "«Подготовка к школе для детей 5-7 лет», «Английский язык для детей 5-15 лет»"),
}
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in ROWS}
n = 0
for pid, (ages, txt) in CATAGES.items():
    if pid in ids:
        data[pid] = {**ages, "src": (txt if txt.startswith("сайт") else Y + txt) + "; 12.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
