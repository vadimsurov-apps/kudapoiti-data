"""Робот edu, 13.11 (четырнадцатый запуск), второй заход «Особым детям»: ещё 15 районов × 2 запроса (ключи ew<N>-1124e)
+ карточки кандидатов из городских запросов про адаптивный спорт/плавание/инклюзивные студии (ключи ev<N>-1124e)."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Сокол", "Соколиная Гора", "Сокольники", "Солнцево", "Спартак", "Спортивная", "Сретенский бульвар", "Стахановская",
         "Стрешнево", "Строгино", "Студенческая", "Сухаревская", "Сходненская", "Таганская", "Тверская"]
INC = ["занятия для детей с ОВЗ", "инклюзивный центр для детей", "адаптивная физкультура для детей",
       "занятия для детей с аутизмом", "сенсорная интеграция для детей", "коррекционный центр для детей", "АВА-терапия для детей"]
Q = [f"{INC[(2 * i + k) % 7]} метро {a}" for i, a in enumerate(AREAS) for k in (3, 4)]
K = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/edu_1124_keep.json")))}
CARDS = [222, 223, 224, 234, 236, 237, 256, 127, 258, 165]
def short(a):
    return re.split(r", (Метро|этаж|подъезд|вход|Вход|офис|кабинет|в помещ|домофон|жилой|ЖК)", a)[0]
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ew{n}=1124e&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)]
    urls += [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ev{n}=1124e&text=" + urllib.parse.quote(f'{K[n]["name"]}, {short(K[n]["addr"])}') for n in CARDS if n in K]
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1124_queries2.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
