"""Иконки робота sections (2026-11-06, вечер-2), метод «Якорь + Характер + Шутка».
Якорь — канонический предмет вида спорта крупно и персонажем (баскетбольный мяч / кольцо со щитом, волейбольный мяч /
мяч над сеткой, волан, шахматный конь / пешка, фехтовальная маска, ракетка для настольного тенниса, роликовый конёк,
мишень со стрелой, парусник «Оптимист», спасательный круг / малыш в шапочке и очках). Шутка — один крупный понятный
аксессуар (корона, шапка выпускника, шарик, кепка…). Уникальна пара «якорь + аксессуар» (сверено с icons-src/subjects.txt
и листами icons-catalog/sheet-01..23).
Запуск: python3 tools/icons_sections_1106e.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O
from icons_cafes_1106 import acc, ACC_RU
import add_sections_1106e as E

W = lambda w: s(f'stroke-width="{w}"')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
F = lambda x, y, d=10, k=0.85, **kw: face(x, y, d=d, k=k, **kw)
WATER = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'


# ---------- якоря: (svg, верх головы для шапки, полуширина, центр лица) ----------
def bball():
    b = (f'<circle cx="64" cy="74" r="38" fill="#F28C38" {W(3)}/>'
         f'<path d="M26 74 H102 M64 36 V112" fill="none" {W(2.6)}/>'
         f'<path d="M38 46 Q54 74 38 102 M90 46 Q74 74 90 102" fill="none" {W(2.6)}/>')
    return b + F(64, 72), 38, 38, (64, 72)


def hoop():
    b = (f'<rect x="26" y="26" width="76" height="50" rx="6" fill="#fff" {W(3)}/>'
         f'<rect x="50" y="46" width="28" height="22" fill="none" stroke="#E8554A" stroke-width="3.5"/>'
         + "".join(f'<path d="M{x} 80 L{x+(64-x)//5} 112" fill="none" stroke="#fff" stroke-width="3"/>' for x in (44, 54, 64, 74, 84))
         + f'<path d="M44 80 L52 112 H76 L84 80" fill="none" {W(2.2)}/><path d="M48 92 H80 M50 102 H78" fill="none" stroke="#fff" stroke-width="2.4"/>'
         f'<ellipse cx="64" cy="80" rx="22" ry="5" fill="none" stroke="{O}" stroke-width="8"/>'
         f'<ellipse cx="64" cy="80" rx="22" ry="5" fill="none" stroke="#F28C38" stroke-width="4"/>')
    return b + F(64, 46, d=9, k=0.75, mouth=False) + f'<path d="M58 56 Q64 61 70 56" fill="none" {W(2.4)}/>', 26, 38, (64, 46)


def vball():
    b = (f'<circle cx="64" cy="74" r="38" fill="#fff" {W(3)}/>'
         f'<clipPath id="vb"><circle cx="64" cy="74" r="38"/></clipPath><g clip-path="url(#vb)">'
         f'<path d="M64 74 Q40 60 36 34 L0 40 V80 Q30 70 64 74Z" fill="#FFD25E" {W(2.4)}/>'
         f'<path d="M64 74 Q90 66 108 86 L110 128 H80 Q86 96 64 74Z" fill="#5CB7F2" {W(2.4)}/>'
         f'<path d="M64 74 Q60 100 40 112" fill="none" {W(2.4)}/></g>'
         f'<circle cx="64" cy="74" r="38" fill="none" {W(3)}/>')
    return b + F(64, 74), 38, 38, (64, 74)


def vnet():
    b = (f'<path d="M6 102 H122" stroke="{O}" stroke-width="3"/><rect x="6" y="88" width="116" height="26" fill="none" {W(2.2)}/>'
         + "".join(f'<path d="M{x} 88 V114" stroke="#fff" stroke-width="2"/>' for x in range(16, 120, 10))
         + f'<path d="M6 101 H122" stroke="#fff" stroke-width="2"/><rect x="4" y="84" width="120" height="6" fill="#fff" {W(2.2)}/>'
         f'<circle cx="64" cy="54" r="30" fill="#fff" {W(3)}/>'
         f'<clipPath id="vn"><circle cx="64" cy="54" r="30"/></clipPath><g clip-path="url(#vn)">'
         f'<path d="M64 54 Q44 44 42 22 L10 26 V60 Q38 50 64 54Z" fill="#FFD25E" {W(2.2)}/>'
         f'<path d="M64 54 Q86 48 100 64 L100 100 H78 Q82 74 64 54Z" fill="#5CB7F2" {W(2.2)}/></g>'
         f'<circle cx="64" cy="54" r="30" fill="none" {W(3)}/>')
    return b + F(64, 54, d=9, k=0.75), 24, 30, (64, 54)


def shuttle():
    b = (f'<path d="M48 84 L26 24 Q64 12 102 24 L80 84Z" fill="#fff" {W(3)}/>'
         + "".join(f'<path d="M{64+dx*0.35:.0f} 84 L{64+dx} 22" stroke="#B8BCCB" stroke-width="2"/>' for dx in (-26, -13, 0, 13, 26))
         + f'<path d="M34 46 Q64 38 94 46 M40 64 Q64 58 88 64" fill="none" stroke="#B8BCCB" stroke-width="2.4"/>'
         f'<path d="M44 82 H84 V90 H44Z" fill="#E8554A" {W(2.4)}/>'
         f'<path d="M44 90 Q44 116 64 116 Q84 116 84 90Z" fill="#FFE9C9" {W(3)}/>')
    return b + F(64, 100, d=8, k=0.7), 20, 38, (64, 100)


def knight(dark=False):
    c, c2 = ("#4A4466", "#6A6488") if dark else ("#FFF7EC", "#E9DCC8")
    b = (f'<rect x="34" y="102" width="60" height="12" rx="4" fill="{c}" {W(3)}/>'
         f'<rect x="42" y="90" width="44" height="14" rx="3" fill="{c2}" {W(3)}/>'
         f'<path d="M46 90 C40 70 44 50 54 38 L50 22 L64 32 C84 30 98 44 96 62 L84 64 C76 64 72 68 76 76 C80 82 84 86 86 90Z" fill="{c}" {W(3)}/>'
         f'<path d="M58 36 Q50 52 52 70" fill="none" stroke="{c2}" stroke-width="5"/>')
    ew = "#fff" if dark else O
    b += (f'<ellipse cx="74" cy="46" rx="4.4" ry="5.2" fill="{ew}"/><circle cx="72.6" cy="44" r="1.7" fill="{"#4A4466" if dark else "#fff"}"/>'
          f'<ellipse cx="82" cy="56" rx="5" ry="3" fill="#FF7FA8" opacity=".7"/><circle cx="92" cy="58" r="1.6" fill="{O}"/>')
    return b, 28, 26, (74, 48)


def pawn():
    b = (f'<rect x="32" y="102" width="64" height="12" rx="4" fill="#4A4466" {W(3)}/>'
         f'<path d="M40 104 Q46 80 54 70 H74 Q82 80 88 104Z" fill="#4A4466" {W(3)}/>'
         f'<rect x="46" y="64" width="36" height="9" rx="4" fill="#6A6488" {W(3)}/>'
         f'<circle cx="64" cy="44" r="22" fill="#4A4466" {W(3)}/>')
    b += (f'<ellipse cx="56" cy="44" rx="4" ry="4.8" fill="#fff"/><ellipse cx="72" cy="44" rx="4" ry="4.8" fill="#fff"/>'
          f'<circle cx="56" cy="45" r="2" fill="{O}"/><circle cx="72" cy="45" r="2" fill="{O}"/>'
          f'<ellipse cx="50" cy="52" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="78" cy="52" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>'
          f'<path d="M60 52 Q64 56 68 52" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>')
    return b, 22, 22, (64, 44)


def fmask():
    foil = lambda x1, y1, x2, y2: (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
                                   f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#D9DDE8" stroke-width="2.4" stroke-linecap="round"/>')
    b = (foil(18, 18, 110, 110) + foil(110, 18, 18, 110)
         + f'<path d="M40 92 Q40 112 64 114 Q88 112 88 92Z" fill="#fff" {W(3)}/>'
         f'<ellipse cx="64" cy="62" rx="30" ry="34" fill="#4A4466" {W(3)}/>'
         f'<clipPath id="fm"><ellipse cx="64" cy="62" rx="27" ry="31"/></clipPath><g clip-path="url(#fm)">'
         + "".join(f'<path d="M{x} 20 V110" stroke="#8A85A6" stroke-width="1.6"/>' for x in range(36, 96, 6))
         + "".join(f'<path d="M30 {y} H100" stroke="#8A85A6" stroke-width="1.6"/>' for y in range(30, 100, 6)) + '</g>'
         f'<ellipse cx="64" cy="62" rx="30" ry="34" fill="none" stroke="#fff" stroke-width="3"/>'
         f'<ellipse cx="64" cy="62" rx="30" ry="34" fill="none" {W(2)}/>')
    b += (f'<ellipse cx="54" cy="60" rx="5" ry="6" fill="#fff"/><ellipse cx="74" cy="60" rx="5" ry="6" fill="#fff"/>'
          f'<circle cx="54" cy="61" r="2.4" fill="{O}"/><circle cx="74" cy="61" r="2.4" fill="{O}"/>'
          f'<path d="M58 74 Q64 79 70 74" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>')
    return b, 28, 30, (64, 60)


def paddle():
    b = (f'<path d="M78 82 L98 108" stroke="{O}" stroke-width="16" stroke-linecap="round"/>'
         f'<path d="M78 82 L98 108" stroke="#C08A5A" stroke-width="10" stroke-linecap="round"/>'
         f'<circle cx="58" cy="58" r="34" fill="#E8554A" {W(3)}/>'
         f'<circle cx="104" cy="40" r="9" fill="#fff" {W(2.6)}/>')
    return b + F(58, 58), 24, 34, (58, 58)


def rskate():
    b = (f'<path d="M36 28 H70 V62 Q96 62 100 82 V92 H30 V36Z" fill="#FF8FB8" {W(3)}/>'
         f'<path d="M36 40 H70" stroke="#fff" stroke-width="3"/><path d="M30 92 H100" {W(3)}/>'
         f'<rect x="26" y="90" width="78" height="8" rx="4" fill="#B8BCCB" {W(2.6)}/>'
         + "".join(f'<circle cx="{x}" cy="106" r="9" fill="#FFD25E" {W(2.6)}/><circle cx="{x}" cy="106" r="3" fill="{O}"/>' for x in (38, 58, 76, 94))
         + f'<path d="M84 64 l4 -6 m4 8 l4 -6" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>')
    return b + F(56, 70, d=9, k=0.75), 28, 22, (56, 70)


def target():
    b = (f'<circle cx="62" cy="68" r="40" fill="#fff" {W(3)}/><circle cx="62" cy="68" r="31" fill="#5CB7F2" {W(2.4)}/>'
         f'<circle cx="62" cy="68" r="22" fill="#E8554A" {W(2.4)}/><circle cx="62" cy="68" r="12" fill="#FFD25E" {W(2.4)}/>'
         f'<path d="M66 64 L108 22" stroke="{O}" stroke-width="5" stroke-linecap="round"/><path d="M66 64 L108 22" stroke="#C08A5A" stroke-width="2.6"/>'
         f'<path d="M100 22 L112 12 L114 20 L106 30Z" fill="#5CB04F" {W(2.2)}/>')
    b += (eye(50, 66, 0.7) + eye(74, 66, 0.7) + f'<path d="M56 80 Q62 85 68 80" fill="none" {W(2.4)}/>'
          f'<ellipse cx="44" cy="76" rx="4" ry="2.4" fill="#FF7FA8" opacity=".8"/><ellipse cx="80" cy="76" rx="4" ry="2.4" fill="#FF7FA8" opacity=".8"/>')
    return b, 28, 34, (62, 66)


def sailboat():
    b = (WATER + f'<path d="M66 20 V86" {W(3.4)}/><path d="M68 24 L104 80 H68Z" fill="#fff" {W(3)}/>'
         f'<path d="M64 28 L34 78 H64Z" fill="#FFD25E" {W(3)}/>'
         f'<path d="M24 86 H106 Q100 106 80 106 H48 Q30 106 24 86Z" fill="#E8554A" {W(3)}/>')
    return b + F(64, 94, d=12, k=0.7), 20, 20, (64, 94)


def ring():
    b = (WATER + f'<circle cx="64" cy="70" r="36" fill="#fff" {W(3)}/><circle cx="64" cy="70" r="16" fill="#7FD3F7" {W(3)}/>'
         + "".join(f'<path d="M{64+16*c:.1f} {70+16*s_:.1f} L{64+36*c:.1f} {70+36*s_:.1f}" stroke="#E8554A" stroke-width="13"/>'
                   for c, s_ in [(0.707, -0.707), (-0.707, -0.707), (0.707, 0.707), (-0.707, 0.707)])
         + f'<circle cx="64" cy="70" r="36" fill="none" {W(3)}/><circle cx="64" cy="70" r="16" fill="none" {W(3)}/>')
    b += eye(52, 44, 0.6) + eye(76, 44, 0.6) + f'<path d="M60 47 Q64 51 68 47" fill="none" {W(2.2)}/>'
    return b, 34, 36, (64, 44)


def swimkid():
    b = (WATER + f'<circle cx="64" cy="72" r="30" fill="#FFD9B8" {W(3)}/>'
         f'<path d="M34 70 Q34 38 64 38 Q94 38 94 70 Q64 60 34 70Z" fill="#A98BF0" {W(3)}/>'
         f'<rect x="44" y="60" width="16" height="11" rx="5" fill="#9ED3FF" {W(2.4)}/><rect x="68" y="60" width="16" height="11" rx="5" fill="#9ED3FF" {W(2.4)}/>'
         f'<path d="M60 65 H68" {W(2.4)}/>'
         + eye(52, 79, 0.6) + eye(76, 79, 0.6) + f'<path d="M58 88 Q64 93 70 88" fill="none" {W(2.4)}/>'
         + WATER.replace("M0 100", "M0 104").replace('fill="#7FD3F7"', 'fill="#7FD3F7" opacity=".9"'))
    return b, 38, 30, (64, 79)


def glasses(fc):
    x, y = fc
    return (f'<rect x="{x-24}" y="{y-7}" width="20" height="13" rx="5" fill="{O}"/><rect x="{x+4}" y="{y-7}" width="20" height="13" rx="5" fill="{O}"/>'
            f'<path d="M{x-4} {y-3} H{x+4}" {W(3)}/><path d="M{x-20} {y-4} l5 0" stroke="#fff" stroke-width="2" stroke-linecap="round"/>')


def medal(fc):
    return (f'<path d="M92 70 L100 88 L108 70" fill="#5CB7F2" {W(2.4)}/><circle cx="100" cy="98" r="12" fill="#FFC93C" {W(2.6)}/>'
            f'<text x="100" y="103" font-family="Arial" font-weight="bold" font-size="14" text-anchor="middle" fill="{O}">1</text>')


ANCH = dict(bball=(bball, "баскетбольный мяч-персонаж"), hoop=(hoop, "баскетбольное кольцо со щитом-персонаж"),
            vball=(vball, "волейбольный мяч-персонаж"), vnet=(vnet, "волейбольный мяч-персонаж над сеткой"),
            shuttle=(shuttle, "волан-персонаж"), knight=(knight, "белый шахматный конь-персонаж"),
            knightd=(lambda: knight(True), "тёмный шахматный конь-персонаж"), pawn=(pawn, "шахматная пешка-персонаж"),
            fmask=(fmask, "фехтовальная маска-персонаж на скрещённых шпагах"),
            paddle=(paddle, "ракетка для настольного тенниса-персонаж с шариком"), rskate=(rskate, "роликовый конёк-персонаж"),
            target=(target, "мишень со стрелой-персонаж"), sail=(sailboat, "парусник «Оптимист»-персонаж"),
            ring=(ring, "спасательный круг-персонаж на воде"), swimkid=(swimkid, "малыш в плавательной шапочке и очках"))
ACCS = ["crown", "graduate", "balloon", "cap", "beanie", "headphones", "party", "bow", "star", "heart", "flower",
        "propeller", "cowboy", "tiara", "wreath", "bunnyears", "rainbow", "wand", "teddy", "sprout", "umbrella",
        "sunglasses", "medal", "pirate", "santa"]
HATS = {"crown", "graduate", "cap", "beanie", "headphones", "party", "bow", "propeller", "cowboy", "tiara", "wreath",
        "bunnyears", "sprout", "pirate", "santa", "sunglasses"}
RU = dict(ACC_RU, sunglasses="в тёмных очках", medal="с золотой медалью «1»")
BGS = ["orange", "blue", "green", "pink", "purple", "yellow", "teal", "sky"]


def anchors_for(r):
    pid, c = r["id"], r["Категории"]
    if c == "badminton": return ["shuttle"]
    if c == "chess": return ["knight", "pawn", "knightd"]
    if c == "pools": return ["ring", "swimkid"]
    if pid.startswith(("nevsky", "rusvolley", "foton")): return ["vball", "vnet"]
    if c == "ballgames": return ["bball", "hoop"]
    if "roller" in pid: return ["rskate"]
    if "fencing" in pid: return ["fmask"]
    if "tabletennis" in pid: return ["paddle"]
    if "archery" in pid: return ["target"]
    if "sea" in pid: return ["sail"]
    raise ValueError(pid)


SPEC = {"peter-sea-center": "sunglasses", "karpov-chess-school": "crown", "petrosian-chess-club": "medal",
        "myslitel-academy-chess": "graduate", "nepo-chess-school": "star"}


def plan():
    reg = open(os.path.join(OUT, "subjects.txt")).read()
    used, cnt, out = set(), {}, []
    for r in E.ROWS:
        opts = anchors_for(r)
        k = cnt.get(r["Категории"] + opts[0], 0); cnt[r["Категории"] + opts[0]] = k + 1
        an = opts[k % len(opts)]
        cand = ([SPEC[r["id"]]] if r["id"] in SPEC else []) + ACCS
        for a in cand:
            if an == "swimkid" and a in HATS: continue
            phrase = f"{ANCH[an][1]} {RU[a]}"
            if (an, a) not in used and phrase not in reg:
                break
        else:
            raise SystemExit(f"нет свободного аксессуара для {r['id']}")
        used.add((an, a))
        out.append((r["id"], an, a, BGS[(k * 3 + len(an)) % len(BGS)], phrase))
    return out


if __name__ == "__main__":
    reg = os.path.join(OUT, "subjects.txt"); txt = open(reg).read()
    for pid, an, a, bg, phrase in plan():
        body, top, half, fc = ANCH[an][0]()
        extra = glasses(fc) if a == "sunglasses" else medal(fc) if a == "medal" else acc(a, top, half)
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(svg(bg, body + extra))
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
        txt += f"{pid} — {phrase}\n"
    open(reg, "w").write(txt)
    print("ok")
