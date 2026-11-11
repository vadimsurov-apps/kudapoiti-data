"""Возраст по направлениям (урок 8) у мест робота edu 11.11 (пятый запуск) — только из названий услуг карточки Яндекс Карт.
python3 tools/edu_1115_catages.py → дописывает auto/cat-ages.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1115 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "Яндекс Карты, карточка организации, услуги: "
CA = {
 "zdorovyi-rebenok-elektrostal": ({"psych": [2, 14]}, "«Нейродиагностика, 2-5 лет», «Нейродиагностика, 6-14 лет», «Занятие с нейропсихологом, 2-5 лет / 6-14 лет»"),
 "logo-like-elektrostal": ({"speech": [2, 10], "school": [4, 7]}, "«Логопед (индивидуальные занятия) от 2,5 лет», «занятия с логопедом для детей от 3 до 10 лет», «Подготовка к школе (4-7 лет)»"),
 "iq007-chayanova": ({"languages": [3, 15], "speech": [3, 17], "school": [6, 17]}, "«Английский OXFORD 3-7 лет / 6-12 лет / 12-15+», «Для детей от 3-х лет. Постановка звуков и развитие речи», «Для детей от 6 лет» (скорочтение)"),
 "yamir-domodedovskaya-33": ({"early": [1, 3], "speech": [2, 17], "school": [6, 17]}, "«Мама и малыш с 1 года», «Комплексное развитие для детей 1,5 - 3 года», «Логопед 2+», «Ментальная арифметика 6+», «Скорочтение 7+»"),
 "akademiya-razvitiya-keramichesky": ({"early": [1, 3], "montessori": [1, 7]}, "«Ясли 1,5-3 лет», «Детский сад 3-4 лет», «Детский сад 4-7 лет»"),
 "uno-center-lyusinovskaya": ({"early": [3, 17]}, "«Раннее развитие 3+»"),
 "baby-club-spasonalivkovsky": ({"early": [0, 5], "school": [5, 7], "languages": [3, 7]}, "«Раннее развитие (8 мес.-1,5 лет)» … «Гармоничное развитие (4,5-5,5 лет)», «Подготовка к школе (5,5-7 лет)», «Английский язык (3-7 лет)»"),
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
