"""Робот rare 14.11 (1114a), шаг 2: обзорные страницы организаций Яндекс Карт из выдачи rr14q*/rr14x* → auto/fetch-queue.txt.
python3 tools/rare_1114a_cardq.py"""
import glob, json, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
idx = {v["url"] for v in json.load(open(os.path.join(ROOT, "auto/pages/index.json"))).values()}
orgs = set()
for f in glob.glob(os.path.join(ROOT, "auto/pages/*rr14[qx]*1114a*.txt")):
    orgs |= set(re.findall(r"yandex\.ru/maps/org/[a-z0-9_]+/\d+/", open(f).read()))
fq = sorted("https://" + o for o in orgs if "https://" + o not in idx)
p = os.path.join(ROOT, "auto/fetch-queue.txt")
old = open(p).read().rstrip("\n").split("\n")
open(p, "w").write("\n".join(old + [l for l in fq if l not in old]) + "\n")
print(len(orgs), len(fq))
