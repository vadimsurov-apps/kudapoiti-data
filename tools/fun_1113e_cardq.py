"""Робот fun 1113e: карточки (fwd-<ключ>-1113e) и дома (fwe-<ключ>-1113e) кандидатов третьего набора районов → auto/fetch-queue.txt."""
import os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
D = {"kvestlend": ("КвестЛенд", "Москва, ул. Свободы, 35, стр. 39"), "avatar-dmd": ("Арена Аватар", "Домодедово, Каширское шоссе, 1"),
     "fortb-pod": ("Форт Боярд", "Подольск, Авиационная ул., 29"), "gudlandia": ("Гудландия", "Серпухов, Московское ш., 55"),
     "detilend": ("Детиленд", "Щёлково, ул. Радиоцентра № 5, 7А"), "zamok": ("Замок чудес", "Щёлково, ул. Шмидта, 9"),
     "okvest": ("Оквест", "Москва, Тушинская ул., 17"), "kraskibum": ("КраскиБум", "Домодедово, ул. Корнеева, 8"),
     "happyland": ("Happy Land", "Серпухов, Советская ул., 111"), "kvestium": ("КвестиУм", "Щёлково, Комсомольская ул., 8А")}
if __name__ == "__main__":
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fwd-{k}=1113e&text=" + urllib.parse.quote(f"{n}, {a}") for k, (n, a) in D.items()]
    urls += [f"{base}fwe-{k}=1113e&text=" + urllib.parse.quote(a) for k, (n, a) in D.items()]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(urls) + "\n" + old)
    print(len(urls))
