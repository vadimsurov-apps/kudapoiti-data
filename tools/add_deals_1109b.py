"""Робот акций 09.11 утро (тема 2: бассейны и секции). Источники — фразы promo-snippets с сайтов мест и кэш auto/pages.
Запуск: python3 tools/add_deals_1109b.py"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
F = os.path.join(ROOT, "deals.json")
TODAY = "2026-11-09"
d = json.load(open(F)); L = d["deals"]
before = len(L)
L[:] = [x for x in L if not (x.get("until") and x["until"] < TODAY)]
removed = before - len(L)

NEW = [
    dict(id="casa-la-famiglia-bday", place_id="cafe-casa-la-famiglia", kind="birthday",
         title="Имениннику −10% (пн–чт) или десерт от шефа (пт–вс)",
         details="В честь дня рождения с понедельника по четверг — скидка 10%; с пятницы по воскресенье и в праздники — десерт-комплимент от шеф-повара. Только при посещении ресторана.",
         code="", url="https://casadifamiglia.ru/", checked=TODAY),
    dict(id="steak-it-easy-myasnitskaya-bday", place_id="cafe-steak-it-easy-myasnitskaya", kind="birthday",
         title="Имениннику −15%",
         details="Скидка 15% в день рождения. Условия (документ, дни действия) уточняйте у ресторана при бронировании.",
         code="", url="http://steakiteasy.ru/news", checked=TODAY),
    dict(id="botanika-ivanteevka-bday", place_id="cafe-botanika-ivanteevka", kind="birthday",
         title="Имениннику — кэшбэк 10% и сладкий комплимент",
         details="Кэшбэк 10% от суммы банкета на карту лояльности и сладкий комплимент в честь дня рождения. Действует в день рождения и 6 дней после.",
         code="", url="https://botanica.rest/actions/", checked=TODAY),
    dict(id="boyarsky-bday", place_id="cafe-boyarsky", kind="birthday",
         title="Имениннику −20% (кроме пт, сб)",
         details="Скидка 20% в день рождения — в любые дни, кроме пятницы, субботы и праздников.",
         code="", url="http://boyarski.ru", checked=TODAY),
    dict(id="gans-i-marta-novokosino-bday", place_id="cafe-gans-i-marta-novokosino", kind="birthday",
         title="Имениннику −10%",
         details="Скидка 10% в день рождения. Условия уточняйте у ресторана при бронировании.",
         code="", url="https://www.gansmarta.ru/", checked=TODAY),
    dict(id="kaspiyka-bday", place_id="cafe-kaspiyka", kind="birthday",
         title="Имениннику −20% по промокоду",
         details="Скидка 20% в день рождения по промокоду DR20. На фуршеты не распространяется.",
         code="DR20", url="http://kaspiyka.ru", checked=TODAY),
    dict(id="tutta-la-vita-tretyakov", place_id="cafe-tutta-la-vita", kind="discount",
         title="−10% по билету в Третьяковку (вт, ср)",
         details="Покажите сотруднику билет в Третьяковскую галерею — скидка 10% на блюда и безалкогольные напитки. По вторникам и средам.",
         code="", url="https://www.tuttalavita.ru/novosti/skidka-po-biletu-v-tretakovskuu-galereu", checked=TODAY),
    dict(id="forte-bello-crocus-kids", place_id="cafe-forte-bello-crocus", kind="promo",
         title="Детские сеты по специальной цене",
         details="Комбо-предложение для детей: детские сеты по спеццене. Также при заказе от трёх пицц — литр лимонада в подарок.",
         code="", url="http://fortebellorest.ru", checked=TODAY),
    dict(id="babysharkpool-pyatnitskoe-trial", place_id="babysharkpool-pyatnitskoe", kind="trial",
         title="Пробное занятие −50%",
         details="Пробное занятие в детском бассейне — 1500 ₽ вместо 3000 ₽ (30 минут). Запись через сайт.",
         code="", url="https://www.sharkypool.com/", checked=TODAY),
]
EXTRA = os.path.join(ROOT, "tools", "deals_1109b_extra.json")
if os.path.exists(EXTRA):
    NEW += json.load(open(EXTRA))
ids = {x["id"] for x in L}
added = 0
for n in NEW:
    if n["id"] not in ids:
        L.append(n); ids.add(n["id"]); added += 1
d["version"] = TODAY
json.dump(d, open(F, "w"), ensure_ascii=False, indent=1)
print("снято", removed, "добавлено", added)
