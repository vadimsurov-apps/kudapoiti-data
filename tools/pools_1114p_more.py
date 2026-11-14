"""Робот pools 14.11 (14 UTC): карточки школы SwimRocket по страницам бассейнов swimrocket.ru/bassein-<…> (auto/pages).
Страница каждого бассейна сама говорит, есть ли в нём детские группы и с какого возраста («детей от 4 лет», «Группы по плаванию
для детей») — у «Буревестника», «Коломенского» и «Медведкова» детских групп на странице нет, их здесь нет. Цен на страницах
бассейнов нет — не пишем. Подключается из tools/add_pools_1114p.py (MORE)."""
import os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# id: (ключ страницы, название, адрес, размеры чаш для «Плюса»)
SR = {
 "swimrocket-arktika": ("arktika", "бассейн «Арктика», Новопеределкино", "Новоорловская ул., 7В", "Бассейн 25 м, 4 дорожки"),
 "swimrocket-bauman": ("baumana", "бассейн МГТУ им. Баумана", "Госпитальная наб., 4, стр. 1", "Бассейн 50 м, 10 дорожек"),
 "swimrocket-beskudnikovo": ("beskudnikovo", "бассейн «Бескудниково»", "Бескудниковский бул., 12А", "Бассейн 25 м, 4 дорожки"),
 "swimrocket-krylatskie-kholmy": ("krylatskie-kholmy", "бассейн «Крылатские холмы»", "ул. Крылатские Холмы, 15, корп. 2", "Бассейн 25 м"),
 "swimrocket-luzhniki-sambo": ("mezhdunarodnyy-tsentr-sambo", "Международный центр самбо, Лужники", "Новолужнецкий пр-д, 13",
                               "Бассейн 25 м, 6 дорожек"),
 "swimrocket-mgsu": ("mgsu", "бассейн МГСУ, Ярославское шоссе", "Ярославское ш., 26, стр. 4", "Бассейн 25 м, 10 дорожек"),
 "swimrocket-mgusit": ("mgusit", "бассейн МГУСиТ, Бибирево", "ул. Лескова, 25А, стр. 1", "Бассейн 25 м, 6 дорожек"),
 "swimrocket-mgyua": ("mgyua", "бассейн МГЮА, Бауманская", "Бакунинская ул., 13, стр. 1", "Бассейн 25 м, 6 дорожек"),
 "swimrocket-severny": ("severnyy", "бассейн «Северный», Физтех", "ул. Арсюкова, 11", "Бассейн 50 м, 8 дорожек"),
 "swimrocket-akvamarin": ("sk-akvamarin", "СК «Аквамарин», Митино", "ул. Рословка, 5", "Бассейн 25 м, 5 дорожек"),
 "swimrocket-garmoniya": ("sk-garmoniya", "СК «Гармония», Тропарёво", "ул. Саморы Машела, 6, корп. 4",
                          "Две чаши: 25 м × 5 дорожек и детская длиной 11 м"),
 "swimrocket-stalnoy": ("stalnoy", "бассейн «Стальной», ВДНХ", "ул. Павла Корчагина, 7/1", "Бассейн 50 м, 10 дорожек"),
 "swimrocket-yantar": ("yantar", "Дворец спорта «Янтарь», Строгино", "ул. Маршала Катукова, 22", "Бассейн 25 м, 8 дорожек"),
 "swimrocket-yuzhnoe-butovo": ("yuzhnoe-butovo", "ФОК «Южное Бутово»", "ул. Поляны, 35",
                               "Две чаши: большая 25 × 13,5 м и малая 13,5 × 6 м"),
 "swimrocket-yuzhnoportovy": ("yuzhnoportovyy", "бассейн «Южнопортовый»", "ул. Трофимова, 30, корп. 3", "Бассейн 25 м, 6 дорожек"),
 "swimrocket-marina-roshcha": ("marina-roshcha", "бассейн в Марьиной Роще", "ул. Образцова, 11, стр. 4", "Бассейн 25 м, 4 дорожки"),
 "swimrocket-gazoprovod": ("ozdorovitelnyy-kompleks", "оздоровительный комплекс в посёлке Газопровод", "пос. Газопровод, 101А",
                           "Бассейн 25 м, 6 дорожек"),
}


def page(slug):
    t = open(os.path.join(ROOT, "auto/pages/www-swimrocket-ru-bassein-%s.txt" % slug), encoding="utf-8").read().split("\n### ")[0]
    L = [l.strip() for l in t.splitlines() if len(l.strip()) > 2]
    i = next(k for k, l in enumerate(L) if l.startswith("Бассейн") and k > 5 and "Адреса" not in l)
    blk = L[i:i + 30]
    j = next(k for k, l in enumerate(blk) if "следующих форматах" in l)
    fm = [x for x in blk[j + 1:j + 6] if x.startswith(("Групп", "Индивид"))]
    kid = next(l for l in blk if re.search(r"детей от \d+ лет", l))
    end = next(k for k, l in enumerate(blk) if l.startswith(("Научиться", "Посмотреть расписание", "Учим плавать")))
    return L[1], blk[:end], kid, fm


MORE = []
for pid, (slug, label, addr, size) in SR.items():
    title, desc, kid, fm = page(slug)
    age = int(re.search(r"детей от (\d+) лет", kid).group(1))
    assert age == 4 and "Группы по плаванию для детей" in fm, pid
    ind = any(x.startswith("Индивидуальные") and "детей" in x for x in fm)
    dry = any("сухому" in x for x in fm)
    plus = ("Учат плавать детей с 4 лет: детские группы" + (" и индивидуальные занятия" if ind else "") +
            ", кроль, кроль на спине, брасс и дельфин" + (", есть «сухое плавание» в зале" if dry else "") + ". " + size)
    src = ("сайт swimrocket.ru/bassein-%s (auto/pages): «%s», «%s», «%s», «мы проводим занятия в следующих форматах: %s», "
           "«Кроль. Кроль на спине. Брасс. Дельфин», «+7(495)-132-00-15»" % (
               slug, title, ". ".join(d.rstrip(".") for d in desc), re.split(r"(?<=лет)[ .]", kid)[0].strip(), ". ".join(fm)))
    MORE.append((pid, "Школа плавания SwimRocket (%s)" % label, "школа плавания", 4, 17, (45, 60), addr, None, None, None, plus,
                 "Малышей до 4 лет не берут", "", "https://www.swimrocket.ru/bassein-%s/" % slug, "+7 495 132-00-15", src,
                 {"Запись": "обязательна"}))
