"""Разбор выдач «Особым детям» (ключи eu<N>-1119f) → tools/edu_1119_cands2.json (n с 300)."""
import json, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
Q = json.load(open(os.path.join(ROOT, "tools/edu_1119_queries2.json")))
out = []
for n, q in enumerate(Q):
    fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-eu{n}-1119f-*.txt"))
    if not fs: continue
    L = [l.strip() for l in open(fs[0]).read().split("\n### ")[0].splitlines()]
    for i, l in enumerate(L):
        if re.search(r" Фото( \d+)?$", l):
            name = re.sub(r" Фото( \d+)?$", "", l)
            for j in range(i + 1, min(i + 14, len(L))):
                if re.search(r" Фото( \d+)?$", L[j]): break
                if re.search(r"(ул\.|пр-т|просп|ш\.|пер\.|бул\.|наб\.|пл\.|проезд|пр\.|мкр|микрорайон|д\.|\d)", L[j]) and "," in L[j] and not L[j].startswith(("Рейтинг", "Закрыто", "Открыто")):
                    out.append({"n": 300 + len(out), "q": q, "qn": n, "name": name, "rubric": L[j - 1], "addr": L[j]}); break
json.dump(out, open(os.path.join(ROOT, "tools/edu_1119_cands2.json"), "w"), ensure_ascii=False, indent=0)
print(len(out))
