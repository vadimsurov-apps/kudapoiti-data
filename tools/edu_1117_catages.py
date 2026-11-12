"""Возраст по направлениям (урок 8) у мест робота edu 12.11 (седьмой запуск) — из названий услуг карточек Яндекс Карт.
python3 tools/edu_1117_catages.py → дописывает auto/cat-ages.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1117 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "Яндекс Карты, карточка организации, услуги: "
CATAGES = {
 "mayak-razvitiya-akademicheskaya": ({"robotics": [5, 12]}, "«Робототехника … для детей от 5 до 12 лет»"),
 "yarkie-deti-skandinavsky": ({"early": [1, 3], "school": [4, 7], "robotics": [4, 10]}, "«Комплексное развитие для малышей (1-3 года)», «Комплексная подготовка к школе 4-7 лет», «Робототехника (4,5+ лет)»"),
 "kids-kommunarka-7a": ({"early": [0, 4], "school": [4, 7], "robotics": [4, 10]}, "«Мама и малыш (0,10 - 1,8 лет)», «Занятия (2,10 - 4 года)», «Подготовка к школе (4-7 лет)», «Робототехника 4+»"),
 "studiya-znaniy-butlerova-4": ({"early": [2, 5], "robotics": [3, 9]}, "«Пробный день в мини-саду для детей 2,5-5 лет», «Робототехника для детей от 3,5 до 9 лет»"),
 "sovyonok-sochinskaya": ({"school": [5, 6], "robotics": [4, 15]}, "«Подготовка к школе 5 лет / 6 лет», «Робототехника для детей (4-15 лет)»"),
 "yamir-domodedovskaya": ({"early": [1, 3], "speech": [2, 17], "school": [6, 17]}, "«Мама и малыш с 1 года», «Комплексное развитие для детей 1,5 - 3 года», «Логопед 2+», «Ментальная арифметика 6+», «Скорочтение 7+»"),
 "klub-landi-shipilovskaya": ({"early": [1, 3], "school": [5, 7]}, "«Мама+Малыш» (1–2 и 2–3 года), «Подготовка к школе (5-6 лет; 6-7 лет)»"),
}
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in ROWS}
n = 0
for pid, (ages, txt) in CATAGES.items():
    if pid in ids:
        data[pid] = {**ages, "src": Y + txt + "; 12.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
