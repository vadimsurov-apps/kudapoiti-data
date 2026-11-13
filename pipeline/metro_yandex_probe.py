"""Разведка: что Яндекс Карты отдают про станцию метро и её выходы. Сырые ответы — в папку probe/ (артефакт)."""
import json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yandex_entrances import fetch
os.makedirs("probe", exist_ok=True)
Q = [("метро Фили", 55.7461, 37.5148), ("метро Фили выход 3", 55.7461, 37.5148), ("метро Киевская выход 2", 55.7439, 37.5666),
     ("станция метро Октябрьское Поле", 55.7935, 37.4936), ("выход метро", 55.7935, 37.4936)]
for i, (q, la, lo) in enumerate(Q):
    h = fetch(q, la, lo)
    blobs = re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', h, re.S)
    open(f"probe/{i}.json", "w").write(json.dumps({"q": q, "len": len(h), "head": h[:300], "blobs": blobs}, ensure_ascii=False))
    print(q, len(h), len(blobs), "captcha" if "captcha" in h.lower()[:5000] else "")
    time.sleep(6)
