"""Робот edu, 13-й запуск, второй заход: выдачи «Особым детям» по следующим 15 районам (ключи ew<N>-1123e) + сайты
инклюзивных центров (возраст групп, доступная среда) → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AREAS = ["Площадь Революции", "Полянка", "Потапово", "Пражская", "Преображенская площадь", "Прокшино", "Пролетарская",
         "Проспект Вернадского", "Проспект Мира", "Профсоюзная", "Пушкинская", "Пыхтино", "Пятницкое шоссе", "Раменки", "Рассказовка"]
INC = ["занятия для детей с ОВЗ", "инклюзивный центр для детей", "адаптивная физкультура для детей",
       "занятия для детей с аутизмом", "сенсорная интеграция для детей", "коррекционный центр для детей"]
Q = [f"{INC[(i + k) % 6]} метро {a}" for i, a in enumerate(AREAS) for k in (0, 2, 4)]
Q += ["центр для детей с ДЦП Москва", "адаптивный спорт для детей с инвалидностью Москва", "занятия для незрячих детей Москва",
      "инклюзивная студия для детей с синдромом Дауна Москва", "иппотерапия для детей Московская область", "инклюзивный центр для детей Одинцово",
      "инклюзивный центр для детей Щёлково", "занятия для детей с ОВЗ Пушкино", "центр для детей с аутизмом Домодедово"]
SITES = ["https://smelostmechtat.ru/", "https://sash.mossport.ru/", "https://centrkubiki.ru/", "https://www.livingthread.ru/",
         "https://invacon.ru/", "https://downsideup.org/", "https://www.logosad.ru/", "https://nsm-m.ru/", "https://kdc-center.ru/",
         "https://cns-neiro.ru/", "https://neiromsk.ru/", "https://zr-kommunarka.ru/", "https://neuropsy-centr.ru/", "https://uspeh-dc.ru/"]
if __name__ == "__main__":
    urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ew{n}=1123e&text=" + urllib.parse.quote(q) for n, q in enumerate(Q)] + SITES
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls) + "\n" + old)
    json.dump(Q, open(os.path.join(ROOT, "tools/edu_1123_queries2.json"), "w"), ensure_ascii=False, indent=0)
    print(len(urls))
