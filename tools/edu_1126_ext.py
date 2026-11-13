"""Структурная выжимка карточек Яндекс Карт (ev<n>-1126e): блок «Особенности» (доступность, занятия), услуги с ценами,
акции → tools/edu_1126_ext.json; печать коротко для отбора."""
import json, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
C = json.load(open(os.path.join(ROOT, "tools/edu_1126_cards.json")))
OUT = {}
for n, d in sorted(C.items(), key=lambda x: int(x[0])):
    f = glob.glob(os.path.join(ROOT, f"auto/pages/*-ev{n}-1126e-*.txt"))[0]
    secs = open(f).read().split("\n### ")
    main = "\n".join([secs[0]] + [s for s in secs[1:] if s.startswith("https://yandex.ru/maps/org/")])
    L = [l.strip() for l in main.splitlines() if l.strip()]
    feats = []
    for i, l in enumerate(L):
        if l == "Особенности" and i and L[i - 1] in ("Показать парковки", "Показать входы") or (l == "Особенности" and i + 1 < len(L) and L[i + 1] not in ("Похожие места", "Витрина", "Товары и услуги", "Подробнее об организации") and i > 40 and not feats):
            for x in L[i + 1:]:
                if x in ("Подробнее об организации", "Панорама"): break
                feats.append(x)
            break
    serv = []
    for i, l in enumerate(L):
        if l in ("Товары и услуги", "Витрина") and i > 5:
            for j in range(i + 1, min(i + 60, len(L))):
                x = L[j]
                if x.startswith("Посмотреть все") or x in ("Панорама", "Адрес", "Новости"): break
                if re.match(r"^(от )?[\d\s]+₽", x) and serv: serv[-1] += " = " + x
                elif x not in ("Давно не обновлялось",) and len(x) < 150: serv.append(x)
            break
    act = [l for l in L if l.startswith("Акция :")][:2]
    OUT[n] = {"name": d["cand"], "head": d["head"][:2], "addr": d.get("addr"), "phone": d.get("phone"), "site": d.get("site"),
              "org": d.get("org"), "q": d["q"], "feats": feats, "serv": serv[:14], "act": act}
json.dump(OUT, open(os.path.join(ROOT, "tools/edu_1126_ext.json"), "w"), ensure_ascii=False, indent=1)
SKIP = re.compile(r"^(Оплата картой|Wi-Fi|Подарочный сертификат|Можно с собакой|Посещение с животными|Способ оплаты|Акции :|Кнопка вызова|Онлайн-запись|Есть сайт)", re.I)
for n, o in OUT.items():
    if not o["addr"]:
        print(f"== {n} {o['name']} — НЕТ КАРТОЧКИ"); continue
    print(f"== {n} {o['name']} | {o['head'][1] if len(o['head'])>1 else ''} | {', '.join(o['addr'])} | {o['phone']} | {o['site']}")
    print("  F:", " ¦ ".join(x[:120] for x in o["feats"] if not SKIP.match(x)))
    print("  S:", " ¦ ".join(x[:70] for x in o["serv"][:9]))
    if o["act"]: print("  A:", " ¦ ".join(o["act"]))
