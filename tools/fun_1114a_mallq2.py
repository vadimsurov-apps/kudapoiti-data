"""Робот fun 1114a: сайты ТЦ (часы) и поиск «Комната матери и ребенка, <адрес ТЦ>» (fxn-<ключ>-1114a) → auto/fetch-queue.txt."""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITES = ["https://www.avenue-sw.ru/", "https://varshavskiy.com/", "https://newriga-outlet.com/", "https://www.waypark.ru/",
         "https://www.trk-mari.ru/", "https://vesna-trk.ru/", "https://june-mytishi.ru/", "https://love-mall.ru/",
         "https://www.tcperlovsky.ru/", "https://gorodtrc.ru/"]
ADDR = {"atrium": "Москва, ул. Земляной Вал, 33", "okhotny": "Москва, Манежная площадь, 1, стр. 2",
        "vesna": "Москва, Алтуфьевское шоссе, 1-й километр, 3, стр. 1", "kaleidoskop": "Москва, Сходненская ул., 56",
        "june": "Мытищи, ул. Мира, 51", "moskvorechye": "Москва, Каширское ш., 26", "lovemall": "Москва, Люблинская ул., 153",
        "perlovsky": "Мытищи, ул. Селезнёва, 33", "kapitoliy-mr": "Москва, Шереметьевская ул., 20",
        "kosino": "Москва, Новоухтомское ш., 2А", "provykhodnoy": "Люберцы, Октябрьский просп., 112",
        "podolsk-bs45": "Подольск, Большая Серпуховская ул., 45"}
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fxn-{k}=1114a&text=" + urllib.parse.quote("Комната матери и ребенка, " + a) for k, a in ADDR.items()]
    urls.append(f"{base}fxe-podolsk-bs45=1114a&text=" + urllib.parse.quote("Подольск, Большая Серпуховская улица, 45"))
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(SITES + urls) + "\n" + old)
    print(len(SITES + urls))
