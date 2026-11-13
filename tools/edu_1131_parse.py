"""Разбор выдач Яндекс Карт (ключи eu<N>-1131e) → кандидаты tools/edu_1131_cands.json."""
import json, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = json.load(open(os.path.join(ROOT, "tools/edu_1131_queries.json")))
out = []
for n, q in enumerate(Q):
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-eu{n}-1131e-*.txt"))
    if not fs:
        continue
    txt = open(fs[0]).read().split("\n### ")[0]
    L = [l.strip() for l in txt.splitlines()]
    for i, l in enumerate(L):
        if re.match(r"^Фото( \d+)?$", l) is None and re.search(r" Фото( \d+)?$", l):
            name = re.sub(r" Фото( \d+)?$", "", l)
            # дальше до адреса
            for j in range(i + 1, min(i + 14, len(L))):
                if re.search(r"(ул\.|пр-т|просп|ш\.|пер\.|бул\.|наб\.|пл\.|проезд|пр\.|мкр|микрорайон|д\.|\d)", L[j]) and "," in L[j] and not L[j].startswith(("Рейтинг", "Закрыто", "Открыто")):
                    if re.search(r" Фото( \d+)?$", L[j]):
                        break
                    out.append({"n": len(out), "q": q, "qn": n, "name": name, "rubric": L[j - 1], "addr": L[j]})
                    break
json.dump(out, open(os.path.join(ROOT, "tools/edu_1131_cands.json"), "w"), ensure_ascii=False, indent=0)
print(len(out))
