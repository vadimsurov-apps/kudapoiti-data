"""Фильтр спама казино/букмекеров (взломанные сайты мест). Общий для роботов, сборки и проверок.
Сайт спамный, если в тексте есть бренд казино/БК/даркнета (BRANDS) или >= 2 общих признаков (GENERIC),
или домен уже в auto/spam-domains.txt. Слово «казино» само по себе НЕ спам (квест «Ограбление казино», VR-карта),
спам — только в связке с «онлайн», «зеркало», «бонус», «вход», «регистрация», «официальный сайт».
Запуск как скрипт: python3 pipeline/spam.py — проверяет places.json, deals.json, таблицы и кэш auto/pages."""
import os, re
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINS_FILE = os.path.join(ROOT, "auto", "spam-domains.txt")

# бренды казино/БК, даркнет-маркеты, индонезийские «slot gacor»: одного совпадения достаточно
BRANDS = re.compile(
    r"\b1\s?win\b|1вин|1x\s?bet|1хбет|mostbet|мостбет|melbet|мелбет|pin[\s-]?up|пин[\s-]?ап|pokerdom|покердом|"
    r"vavada|вавада|riobet|риобет|\bizzi\b|\bиззи\b|fresh casino|фреш казино|vodka casino|водка казино|kometa casino|"
    r"комета казино|mellstroy|мелстрой|bet4win|parimatch|пари\s?матч|фонбет|fonbet|винлайн|winline|leonbets|"
    r"betcity|бетсити|olimpbet|олимпбет|\bggbet|joycasino|джойказино|selector casino|cat casino|daddy casino|"
    r"kent casino|\bstarda\b|\bстарда\b|irwin casino|gama casino|lex casino|drip casino|monro casino|r7 casino|"
    r"\bazino|\bазино|вулкан (?:казино|вегас|платинум|делюкс|старс|24)|\bvulkan|slot ?gacor|situs slot|maxwin|"
    r"\bqris\b|machines? à sous|blacksprut|блэкспрут|kraken ?(?:market|darknet|onion)|кракен (?:маркет|даркнет|сайт)|"
    r"\bомг ?(?:маркет|даркнет)|гидра (?:маркет|онион)|даркнет|darknet|\.onion\b", re.I)
# общие слова: нужно >= 2 совпадений (слово «казино» в одиночку — не спам: квест «Ограбление казино»)
GENERIC = re.compile(
    r"онлайн[\s-]*казино|казино[\s-]*онлайн|online[\s-]*casino|casino[\s-]*online|"
    r"казино\W{0,3}(?:\w+\W+){0,4}?(?:зеркал|бонус|вход|регистрац|официальн\w* сайт|промокод|слот|фриспин|депозит)|"
    r"(?:зеркал\w*|официальн\w* сайт\w*|бонус\w*|вход|регистрац\w*)\W+(?:\w+\W+){0,3}?казино|"
    r"\bcasino\b|букмекер|ставк\w* на спорт|беттор|бездепозит|фриспин|free ?spins?|отыгрыш|вейджер|\bwager|"
    r"рабоч\w* зеркал|зеркал\w* (?:официальн|рабоч|сайта)|промокод\w* при регистрац|jackpot|джекпот", re.I)


def hits(text):
    t = text or ""
    return [m.group(0) for m in BRANDS.finditer(t)] + [m.group(0) for m in GENERIC.finditer(t)]


def is_spam_text(text):
    t = text or ""
    return bool(BRANDS.search(t)) or len(GENERIC.findall(t)) >= 2


def domain(url):
    if not url: return ""
    u = str(url).split()[0].strip(";, ")
    return urlparse(u if "//" in u else "http://" + u).netloc.lower().removeprefix("www.")


def load_domains():
    if not os.path.exists(DOMAINS_FILE): return set()
    return {l.split("#")[0].strip().lower() for l in open(DOMAINS_FILE) if l.split("#")[0].strip()}


def add_domains(new):
    have = load_domains()
    new = sorted({d for d in new if d and d not in have})
    if new:
        with open(DOMAINS_FILE, "a") as f:
            for d in new: f.write(d + "\n")
    return new


def is_spam_url(url, domains=None):
    return domain(url) in (domains if domains is not None else load_domains())


if __name__ == "__main__":
    import glob, json, sys
    os.chdir(ROOT)
    D = load_domains(); bad = 0
    for p in json.load(open("places-all.json" if __import__("os").path.exists("places-all.json") else "places.json"))["places"]:
        txt = " ".join(str(v) for v in p.values() if isinstance(v, str))
        if is_spam_url(p.get("url"), D) or is_spam_text(txt):
            bad += 1; print("МЕСТО", p["id"], p.get("url"), hits(txt)[:3])
    for d in json.load(open("deals.json"))["deals"]:
        if is_spam_url(d.get("url"), D) or is_spam_text(json.dumps(d, ensure_ascii=False)):
            bad += 1; print("АКЦИЯ", d["id"], d.get("url"))
    idx = json.load(open("auto/pages/index.json")) if os.path.exists("auto/pages/index.json") else {}
    found = set()
    for f in glob.glob("auto/pages/*.txt"):
        if is_spam_text(open(f).read()):
            u = idx.get(os.path.basename(f)[:-4], {}).get("url")
            found.add(domain(u)); print("КЭШ", f, u)
    if "--add" in sys.argv:
        print("новые спам-домены:", add_domains(found))
    sys.exit(1 if bad else 0)
