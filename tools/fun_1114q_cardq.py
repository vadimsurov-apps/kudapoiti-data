"""Робот fun 1114q, круг 2: карточки «Комната матери и ребенка, <адрес>» на вокзалах и в ТЦ (fqn-<k>-1114q), карточки
кандидатов из выдач по районам (fqd-<n>-1114q), сайты ТЦ → auto/fetch-queue.txt."""
import json, os, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ADDR = {"kazansky": "Москва, Комсомольская площадь, 2", "yaroslavsky": "Москва, Комсомольская площадь, 5",
        "leningradsky": "Москва, Комсомольская площадь, 3", "kievsky": "Москва, площадь Киевского Вокзала, 1",
        "paveletsky": "Москва, Павелецкая площадь, 1", "belorussky": "Москва, площадь Тверская Застава, 7",
        "rizhsky": "Москва, Рижская площадь, 1", "savelovsky": "Москва, площадь Савёловского Вокзала, 2",
        "vostochny": "Восточный вокзал, Москва", "kursky": "Москва, ул. Земляной Вал, 29",
        "kapitoliy-mr": "Москва, Шереметьевская ул., 20", "vykhodnoy": "Люберцы, Октябрьский просп., 112",
        "akvarel": "Пушкино, 33-й километр автодороги М-8 Холмогоры, 18", "vitte": "Москва, Венёвская ул., 6",
        "globalcity": "Москва, Кировоградская ул., 14", "tsum": "Москва, ул. Петровка, 2", "semenovsky": "Москва, Семёновская площадь, 1"}
PICK = [2, 9, 14, 17, 21, 22, 23, 25, 26, 29, 31, 35, 39, 49, 50, 52, 53, 54, 65, 69, 72, 76, 77, 85, 87, 97, 98, 36, 8]
SITES = ["https://www.kapitoliy.ru/", "https://vykhodnoy.ru/", "https://pushkino.aquarelle-centre.ru/", "https://sc-globalcity.ru/"]
if __name__ == "__main__":
    C = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/fun_1114q_cands.json")))}
    base = "https://yandex.ru/maps/1/moscow-and-moscow-oblast/?"
    urls = [f"{base}fqn-{k}=1114q&text=" + urllib.parse.quote("Комната матери и ребенка, " + a) for k, a in ADDR.items()]
    urls += [f"{base}fqd-{n}=1114q&text=" + urllib.parse.quote(C[n]["name"] + ", " + C[n]["addr"]) for n in PICK]
    p = os.path.join(ROOT, "auto/fetch-queue.txt")
    old = open(p).read()
    open(p, "w").write("\n".join(SITES + urls) + "\n" + old)
    print(len(SITES + urls))
