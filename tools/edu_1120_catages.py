"""Возраст по направлениям (урок 8) у мест робота edu 12.11 (десятый запуск) — из названий услуг карточек Яндекс Карт и сайтов.
python3 tools/edu_1119_catages.py → дописывает auto/cat-ages.json (только места, добавленные в таблицу)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_edu_1120 import ROWS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Y = "Яндекс Карты, карточка организации, услуги: "
CATAGES = {
 "chernyak-perovskaya": None,
 "altera-vita-musorgskogo": ({"early": [2, 4], "inclusive": [2, 16], "psych": [2, 16], "speech": [2, 16]}, "«Раннее развитие (2-4 г.), занятие 40 мин с элементами сенсорной интеграции», «Для детей от 2-х до 16-ти лет»"),
 "plyvem-v-rech-pyatnitskoe": None,
 "prokids-grimau": ({"early": [0, 3], "speech": [2, 7], "languages": [2, 4], "robotics": [3, 7]}, "«Развивающие занятия мини-1 (от 7 мес до 1,5 лет)», «Мини сад (от 1,5 до 2,5 лет)», «Запуск речи (от 2 лет)», «Английский язык (от 2,5 до 4,5 лет)», «Робототехника (от 3,5 лет)»"),
 "amakids-kuskovskaya": ({"school": [4, 12]}, "«Ментальная арифетика 5 - 12 лет», «Подготовка к школе (4 -7 лет)»"),
 "garmoniya-lytkarino": ({"early": [1, 3], "school": [4, 8]}, "«\"Ма-малыш\" - кружки раннего развития для детей 1-2 и 2-3 лет», «\"Речь-и-ум\" ... для детей 4-5 лет», «Для школьников 1-2 классов»"),
 "ostrovok-detstva-mnevniki": ({"speech": [2, 12], "psych": [4, 12], "school": [5, 12], "early": [3, 7]}, "«Дефектологическая коррекция с 2,5 - 12 лет», «Нейропсихологическая коррекция с 4 - 12 лет», «Подготовка к школе с 5 - 7 лет», «Репетитор по русскому языку и чтению с 7 - 12 лет», «Группа выходного дня с 3 - 6 лет», «Нейройога с 3,5 - 7 лет»"),
 "dai-pyat-dzerzhinsky": ({"school": [3, 7], "speech": [2, 4], "languages": [3, 17]}, "«Чтение 3 - 7 лет», «Запуск речи (2,5-4 года с логопедом)», «Говорилка (малыш + мама, раннее развитие)», «Английский язык (дошкольники)», «Английский язык (школьники)»"),
 "poslushayka-elektrolitny": ({"early": [1, 5], "school": [5, 7], "languages": [3, 10]}, "«Возрастные группы: 1-2, 2-3, 3-4 года, 4-5 лет», «Группы 1 и 2 года до школы», «Учим детей с 3,5 до 10 лет»"),
}
CATAGES = {k: v for k, v in CATAGES.items() if v}
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
