"""Разбор выдач Яндекс Карт (ключи eu<N>-1138e, eu<N>-1138f, волна 2 — eu<N>-1137g) → кандидаты tools/edu_1138_cands.json (название, рубрика, адрес, запрос)."""
import json, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
out = []
for tag, fn in (("1138e", "edu_1138_queries.json"), ("1138f", "edu_1138_queries2.json")):
    Q = json.load(open(os.path.join(ROOT, "tools", fn)))
    for n, q in enumerate(Q):
        fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-eu{n}-{tag}-*.txt"))
        if not fs: continue
        L = [l.strip() for l in open(fs[0]).read().split("\n### ")[0].splitlines()]
        for i, l in enumerate(L):
            if re.search(r" Фото( \d+)?$", l) and not re.match(r"^Фото", l):
                name = re.sub(r" Фото( \d+)?$", "", l)
                for j in range(i + 1, min(i + 14, len(L))):
                    if re.search(r" Фото( \d+)?$", L[j]): break
                    if re.search(r"(ул\.|пр-т|просп|ш\.|пер\.|бул\.|наб\.|пл\.|проезд|пр\.|мкр|микрорайон|д\.|\d)", L[j]) and "," in L[j] and not L[j].startswith(("Рейтинг", "Закрыто", "Открыто", "Акция", "Награды")):
                        out.append({"n": len(out), "q": q, "tag": tag, "name": name, "rubric": L[j - 1], "addr": L[j]})
                        break
json.dump(out, open(os.path.join(ROOT, "tools/edu_1138_cands.json"), "w"), ensure_ascii=False, indent=0)
print(len(out))
