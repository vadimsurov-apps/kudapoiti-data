"""Возраст по направлениям (урок 8) у мест робота edu 11.11 (четвёртый запуск) — только из названий услуг карточки Яндекс Карт.
python3 tools/edu_1114_catages.py → дописывает auto/cat-ages.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1114 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "Яндекс Карты, карточка организации, услуги: "
CA = {
 "umnyasha-yuzhnobutovskaya-117": ({"early": [1, 3], "languages": [3, 7], "school": [5, 7]}, "«Раннее развитие 1-3 года», «Английский язык 3-7 лет», «Подготовка к школе 5-7 лет»"),
 "shag-ilmensky-14": ({"early": [1, 3], "psych": [1, 17], "speech": [3, 17], "languages": [4, 17], "school": [5, 7]}, "«Мама+малыш (1+)», «Мини-сад для 2-3 лет», «Нейропсихолог (1,5+)», «Логопед (3+)», «Английский язык (4+)», «Подготовка к школе (5-6, 6-7)»"),
 "tsentr-razvitiya-rechi-seligerskaya": ({"lfk": [1, 3]}, "«Индивидуальное занятие ЛФК для детей от 1,5 до 3 лет»"),
 "esther-leningradskoe-52a": ({"early": [3, 6]}, "мини-сад для детей 3-6 лет"),
 "baby-club-staropetrovsky-8": ({"early": [0, 6], "school": [6, 7]}, "«Раннее развитие (8 мес-1,5л.)» … «Флагманский курс (5,5-6,5)», «Подготовка к школе (6-7 лет)»"),
 "alternativa-reutov": ({"montessori": [2, 6], "languages": [3, 7]}, "«Занятия по системе М.Монтессори с 2,6 - 6 лет», «Английский язык (по методике Мещеряковой) с 3 до 7 лет»"),
 "logos-dolgoprudny": ({"school": [4, 7], "speech": [3, 17]}, "«Мышематика для детей 4-7 лет», «Логопед от 3 лет»"),
 "logotsentr-slova-mitinskaya-31": ({"speech": [2, 17], "school": [4, 7]}, "«Запуск речи — от 2 лет», «Подготовка к школе для детей 4-7 лет»"),
 "poliglotiki-novatorov-8": ({"early": [3, 6]}, "«Английский Мини-сад с 3 до 6 лет»"),
 "raduga-kosvintsevoy-zhukovsky": ({"early": [2, 5]}, "«Малышарики 2-3 года», «Непоседы (развивашки) 4-5 лет»"),
 "rechiumik-vidnoe": ({"speech": [2, 17], "school": [5, 17]}, "«Логоритмика для малышей от 2-х лет», «Нейроподготовка к школе для детей от 5 лет»"),
 "umnarium-vidnoe": ({"school": [4, 17], "languages": [5, 17]}, "«Подготовка к школе с 4-х лет», «Английский язык 5+»"),
}
p = os.path.join(ROOT, "auto", "cat-ages.json")
data = json.load(open(p))
ids = {r["id"] for r in ROWS}
n = 0
for pid, (ages, txt) in CA.items():
    if pid in ids:
        data[pid] = {**ages, "src": Y + txt + "; 11.11.2026"}
        n += 1
json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
print("cat_ages:", n)
