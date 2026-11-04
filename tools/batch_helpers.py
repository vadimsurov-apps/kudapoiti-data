"""Общие функции для добавления мест."""
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

SRC = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "..", "data", "kuda-poiti-mesta.xlsx")
KP = "https://www.kp.ru/afisha/msk/obzory/moj-gorod/luchshie-batutnye-parki-moskvy/"
HALVA = "https://media.halvacard.ru/entertainment/top-batutnyx-parkov-v-moskve"


def P(pid, name, typ, metro, addr, lat, lon, a0, a1, d0, d1, energy, tags, price, note, hours, indoor,
      plus, minus, adult=2, src="", acc="приблизительно, ±500 м", adult_price=None, booking="не нужна",
      season=None, loud="нет", dark="нет", sit="нет", crowd="частично", food="частично", stroller="частично"):
    return {"id": pid, "Название": name, "Тип": typ, "Метро": metro, "Адрес": addr, "Широта": lat, "Долгота": lon,
            "Точность координат": acc, "Возраст от": a0, "Возраст до": a1, "Длит. от, мин": d0, "Длит. до, мин": d1,
            "Энергия": energy, "Громко": loud, "Темно": dark, "Толпы": crowd, "Сидеть неподвижно": sit,
            "Теги интересов": tags, "Детский билет, ₽": price,
            "Взрослый билет, ₽": adult_price if adult_price is not None else price,
            "Бесплатно до (лет / см)": note, "Запись": booking, "Часы работы": hours, "Сезон (месяцы)": season,
            "В помещении": indoor, "Еда на месте": food, "Коляска": stroller, "Интересно взрослым (1–3)": adult,
            "Плюс": plus, "Минус": minus, "Источник": src, "Статус данных": "черновик — проверить"}


def jump(pid, name, metro, addr, lat, lon, price, plus, minus="Цена «от», уточняйте детский тариф", src=KP, a0=3):
    return P(pid, name, "батутный центр", metro, addr, lat, lon, a0, 14, 60, 120, "активно",
             "спорт и активность", price, "цена «от» за сеанс; взрослым-сопровождающим часто бесплатно",
             None, "да", plus, minus, adult=1, src=src, adult_price=0, loud="да", booking="желательна", food="нет")


def park(pid, name, metro, addr, lat, lon, plus, minus, water=False, extra="", adult=2, season=None, typ="парк"):
    tags = "природа, спорт и активность" + (", вода" if water else "") + (", " + extra if extra else "")
    return P(pid, name, typ, metro, addr, lat, lon, 1, 14, 60, 240, "активно", tags, 0,
             "вход свободный", "круглосуточно", "нет", plus, minus, adult=adult, stroller="да", season=season)


def museum(pid, name, metro, addr, lat, lon, a0, tags, price, note, plus, minus, adult=3, d1=120, hours=None, src=""):
    return P(pid, name, "музей", metro, addr, lat, lon, a0, 14, 60, d1, "средне", tags, price, note,
             hours, "да", plus, minus, adult=adult, src=src, food="нет")


def stage(pid, name, typ, metro, addr, lat, lon, a0, tags, price, note, plus, minus, d=60, adult=2):
    return P(pid, name, typ, metro, addr, lat, lon, a0, 14, d, d + 30, "спокойно", tags, price, note,
             "по расписанию", "да", plus, minus, adult=adult, booking="обязательна", dark="частично", sit="да",
             food="нет", stroller="нет")


def trip(pid, name, typ, addr, lat, lon, a0, tags, price, note, plus, minus, adult=3, indoor="частично",
         d0=180, d1=360, season=None, energy="средне", hours=None, acc="приблизительно, ±1 км"):
    return P(pid, name, typ, "— (на машине / электричке)", addr, lat, lon, a0, 14, d0, d1, energy, tags, price, note,
             hours, indoor, plus, minus, adult=adult, acc=acc, season=season)


