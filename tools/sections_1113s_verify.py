"""Пачка для tools/set_verified.py по местам робота sections 13.11 (21 UTC, 1113s): поля, подтверждённые карточкой Яндекс Карт
(auto/pages, yandex-ru-maps-org-*, сайты) — адрес, тип, категории, возраст, телефон, сайт, «как найти», доступная
среда; точка — справка OSM (sections_1113s_points.json). Возраст по направлениям — auto/cat-ages.json.
python3 tools/sections_1113s_verify.py > batch.json   (--cat-ages — дописать auto/cat-ages.json)"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_sections_1113s import ROWS, PHONE, SRC, URL, PT, CAT_AGES, ACCESS

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
if "--cat-ages" in sys.argv:
    p = os.path.join(ROOT, "auto/cat-ages.json")
    d = json.load(open(p))
    for pid, (ages, src) in CAT_AGES.items():
        if pid in PT:
            d[pid] = {**ages, "src": src}
    json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
    sys.exit()
out = {}
for r in ROWS:
    pid = r["id"]
    f = {"address": r["Адрес"], "type": r["Тип"], "cats": r["Категории"], "age_min": r["Возраст от"]}
    if r["Возраст до"] is not None:
        f["age_max"] = r["Возраст до"]
    if PHONE.get(pid):
        f["phone"] = PHONE[pid]
    if URL.get(pid):
        f["url"] = URL[pid]
    if r.get("Часы работы"):
        f["hours"] = r["Часы работы"]
    if r.get("Как найти"):
        f["how"] = r["Как найти"]
    if pid in ACCESS:
        f["access"] = ACCESS[pid]
    if r.get("Детский билет, ₽"):
        f["price_child"] = r["Детский билет, ₽"]
    p = PT[pid]
    f["point"] = {"lat": p[0], "lon": p[1], "level": p[3], "how": p[2]}
    out[pid] = {"fields": f, "src": SRC[pid] + "; OSM (справка osm-query) (проверено 2026-11-13)"}
print(json.dumps(out, ensure_ascii=False, indent=1))
