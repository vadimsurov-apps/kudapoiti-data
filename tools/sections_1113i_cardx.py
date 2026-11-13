"""Выжимка карточек Яндекс Карт партии (ключи sc<n>-s<партия>) — название, рубрика, адрес, телефон, сайт, особенности, возраст.
python3 tools/sections_1113i_cardx.py <партия> <n,n,…>"""
import glob, re, sys, json
def card(part, n):
    fs = glob.glob(f"auto/pages/*-sc{n}-s{part}-*.txt")
    if not fs: return None
    secs = open(fs[0]).read().split("\n### ")
    L = [l.strip() for l in secs[0].splitlines()]
    r = {"n": n, "name": L[1] if len(L) > 1 else "", "rubric": L[2] if len(L) > 2 else ""}
    if "Адрес" in L:
        i = L.index("Адрес"); r["addr"] = L[i + 1]; r["addr2"] = L[i + 2] if L[i + 2] not in ("Маршрут", "Показать входы") else ""
    if "Контакты" in L:
        i = L.index("Контакты")
        for l in L[i + 1:i + 6]:
            m = re.match(r"(\+7 \(\d{3}\) \d{3}-\d{2}-\d{2})", l)
            if m and "phone" not in r: r["phone"] = m.group(1)
            if re.match(r"^[\w.\-а-яё]+\.(ru|рф|com|school|ws|su|org|net|pro|moscow|club|online|site)(/\S*)?$", l, re.I): r["site"] = l
    r["feat"] = [l for l in L if " : " in l][:4]
    r["ages"] = sorted({l for l in L if re.search(r"\d+\s*[-–]\s*\d+\s*(лет|год)|от \d+(,\d)? (лет|год)|с \d+(,\d)? (лет|год)|\d+\+", l)})[:12]
    r["list"] = bool(re.search(r"^Открыто$|Оплата картой", "\n".join(L[:4]), re.M)) and "Адрес" not in L
    return r
if __name__ == "__main__":
    part = sys.argv[1]
    for n in map(int, sys.argv[2].split(",")):
        print(json.dumps(card(part, n), ensure_ascii=False))
