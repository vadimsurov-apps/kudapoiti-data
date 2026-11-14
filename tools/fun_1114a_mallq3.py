"""Робот fun 1114a: координаты ТЦ по адресу (fxe-<ключ>-1114a) → auto/fetch-queue.txt."""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
H = {"varshavsky": "Москва, Варшавское шоссе, 87Б", "newriga": "Истра, деревня Покровское, Центральная улица, 33",
     "waypark": "Путилково, МКАД 71-й километр, 16А", "mari": "Москва, Поречная улица, 10",
     "lovemall": "Москва, Люблинская улица, 153"}
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fxe-{k}=1114a&text=" + urllib.parse.quote(t) for k, t in H.items()]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
