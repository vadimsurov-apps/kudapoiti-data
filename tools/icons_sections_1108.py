"""Иконки робота sections, 2026-11-08 (00 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая иконка придумана отдельно,
свой герой, своя сцена, своя палитра фона (21 разная палитра).
Бассейны — без дельфинов, уток, китов, тюленей и прочих занятых героев: облачко-Ветерок, корги, флажки поворота,
солнце в очках, кристалл, малинка, колобашка, ныряние за колечками, синхронистка, кувырок-поворот, грибок-фонтан,
доска «1», брассист. Шахматы — слон-библиотекарь, ладья-крепость с подъёмным мостом, кони-братья в чехарде.
Бадминтон — волан-купава. Баскетбол — мяч с чемоданом у вокзала, данк девочки, три мяча по росту, бросок снизу малыша.
Сверено с листами icons-catalog/sheet-01…35 и icons-src/subjects.txt.
Запуск: python3 tools/icons_sections_1108.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O
from icons_sections_1107d import W, PINK, GOLD, RED, ORG, shuttle
from icons_sections_1107i import water, bubbles, drops, edge, capkid, SKIN
from icons_sections_1107c import ball, hoop, cloud
from icons_sections_1107h import G, king, rook, bishop, knight, WHITE, BLACK

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({
    "mango": ("#FFF0C9", "#FF9F45"), "lilac": ("#F3E6FF", "#C08BE8"), "deepsea": ("#BFF3E6", "#2E9C8E"),
    "mint": ("#E8FFF2", "#86DDB0"), "lemon": ("#FFFDE0", "#E8E05A"), "sand": ("#FFF1D6", "#E6B877"),
    "coral": ("#FFE3DC", "#FF8C7A"), "rose": ("#FFE8F3", "#E98AC0"), "steel": ("#E2ECF7", "#7F9DC4"),
    "peach": ("#FFEADF", "#F7A68A"), "aqua": ("#D9FBFF", "#3FC3D8"), "olive": ("#F0F6D8", "#A9C25C"),
    "berry": ("#F7DDF0", "#B05C9E"), "dusk": ("#FFD9C2", "#8D6CC0"), "ice": ("#F2FBFF", "#B5D8F0"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def limb(d, c=SKIN, w=6):
    return f'<path d="{d}" fill="none" stroke="{O}" stroke-width="{w+3}" stroke-linecap="round"/>' \
           f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'


# ============================== БАССЕЙНЫ ==============================
# 1. «Бриз» (Дмитров): щекастое облачко-Ветерок дует в спину малышу на доске для плавания
add("pool-briz-dmitrov", "sky",
    water(78, "#5BC0EA", amp=5, n=3, edge="#3C9AD0")
    + f'<path d="M14 40 Q4 30 14 22 Q20 10 34 16 Q42 6 54 14 Q64 10 66 22 Q76 26 70 38 Q66 46 54 44 Q44 52 32 46 Q20 50 14 40Z" fill="#FFFFFF" {W(3)}/>'
    + face(40, 30, d=8, k=0.75, mouth=False)
    + f'<ellipse cx="56" cy="34" rx="5.5" ry="6.5" fill="#FFB3C8" {W(2.4)}/>'
    + f'<ellipse cx="57" cy="34" rx="2.2" ry="3" fill="{O}"/>'
    + "".join(f'<path d="M{x} {y} q10 -4 20 0" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>' for x, y in [(66, 40), (70, 50), (64, 58)])
    + f'<path d="M58 84 L112 78 L114 90 L60 96Z" fill="#FFC93C" {W(3)}/>'
    + f'<circle cx="104" cy="85" r="3" fill="{RED}"/>'
    + capkid(98, 70, RED, sc=0.95)
    + limb("M90 82 Q96 82 104 80", SKIN, 5)
    + limb("M84 90 Q74 96 62 92", SKIN, 6)
    + drops([(52, 76), (44, 84)], "#BFE8FF")
    + f'<path d="M36 92 q6 -6 12 0 q6 6 12 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    "щекастое облачко-Ветерок «Бриз»",
    "надув щёки, дует в спину малышу, и тот мчится по бассейну на жёлтой доске для плавания")

# 2. «Дельфин» (Воскресенск, 50 м): корги в шапочке плывёт по-собачьи вдоль разделительной дорожки
_corgi = (
    f'<path d="M30 70 Q30 52 48 50 L84 50 Q102 52 100 70 Q98 80 64 80 Q32 80 30 70Z" fill="#F29A4A" {W(3)}/>'
    f'<path d="M52 56 Q64 64 76 56 Q76 72 64 76 Q52 72 52 56Z" fill="#FFFFFF" {W(2.2)}/>'
)
add("pool-delfin-voskresensk", "deepsea",
    f'<rect x="-6" y="62" width="140" height="72" fill="#4FB6E8"/>'
    + "".join(f'<circle cx="{x}" cy="66" r="4.2" fill="{c}" {W(1.6)}/>' for x, c in zip(range(-2, 134, 10), [RED, "#FFFFFF"] * 7))
    + "".join(f'<path d="M-6 {y} H134" stroke="#7FD0F5" stroke-width="2" stroke-dasharray="10 8"/>' for y in (96, 116))
    + f'<path d="M30 60 L38 32 L50 50Z" fill="#F29A4A" {W(3)}/><path d="M36 42 L39 34 L45 47Z" fill="#FFB3C8"/>'
    + f'<path d="M78 60 L90 32 L98 52Z" fill="#F29A4A" {W(3)}/><path d="M88 43 L90 35 L95 49Z" fill="#FFB3C8"/>'
    + f'<ellipse cx="64" cy="62" rx="34" ry="26" fill="#F29A4A" {W(3)}/>'
    + f'<path d="M34 50 Q64 22 94 50 Q80 42 64 42 Q48 42 34 50Z" fill="{ORG}" {W(2.8)}/>'
    + f'<path d="M46 64 Q64 50 82 64 Q82 84 64 86 Q46 84 46 64Z" fill="#FFFFFF" {W(2.4)}/>'
    + face(64, 58, d=12, k=0.72, mouth=False)
    + f'<ellipse cx="64" cy="70" rx="5" ry="3.6" fill="{O}"/>'
    + f'<path d="M58 74 Q64 80 70 74" fill="none" {W(2.4)}/>'
    + f'<path d="M62 77 Q62 90 68 88 Q72 86 68 77Z" fill="#FF7FA8" {W(2.2)}/>'
    + f'<path d="M-6 84 Q16 76 30 84 Q44 92 56 86 M72 86 Q86 92 100 84 Q114 76 134 84" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>'
    + limb("M30 90 q-8 6 -14 2", "#F29A4A", 7) + limb("M98 90 q8 6 14 2", "#F29A4A", 7),
    "рыжий корги в оранжевой плавательной шапочке",
    "плывёт по-собачьи вдоль красно-белой разделительной дорожки 50-метрового бассейна, высунув язык")

# 3. ДС «Пушкино»: девочка с косичкой плывёт на спине и смотрит на гирлянду флажков поворота
add("pool-ds-pushkino", "lemon",
    f'<path d="M-6 30 Q64 44 134 30" fill="none" {W(2.2)}/>'
    + "".join(f'<path d="M{x} {30+14*(1-((x-64)/70)**2)*0+ (6 if 20<x<108 else 2)} l6 14 l6 -14Z" fill="{c}" {W(1.8)}/>'
              for x, c in zip(range(2, 124, 14), [RED, "#5CB7F2", "#FFFFFF", "#4FBF6B", RED, "#5CB7F2", "#FFFFFF", "#4FBF6B", RED]))
    + water(66, "#5BC0EA", amp=3, n=4, edge="#3C9AD0")
    + f'<ellipse cx="62" cy="80" rx="36" ry="10" fill="#9C6ADE" {W(3)}/>'
    + f'<circle cx="34" cy="74" r="15" fill="{SKIN}" {W(3)}/>'
    + f'<path d="M20 70 Q22 56 36 58 Q46 60 48 70 Q36 64 20 70Z" fill="#7E4BC8" {W(2.6)}/>'
    + f'<path d="M20 74 Q8 80 10 92 Q14 86 18 84" fill="#7A4A2E" {W(2.4)}/>'
    + f'<circle cx="11" cy="93" r="3.2" fill="#FF7FA8" {W(1.6)}/>'
    + face(36, 74, d=5, k=0.55)
    + limb("M44 70 Q56 50 72 52", SKIN, 6)
    + limb("M88 78 q12 -2 22 4", SKIN, 6) + limb("M88 84 q12 2 22 8", SKIN, 6)
    + f'<path d="M106 76 q6 -8 12 -2 M106 92 q8 -4 12 4" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    + drops([(80, 46), (90, 56)], "#BFE8FF"),
    "девочка с косичкой в фиолетовой шапочке, плывущая на спине",
    "смотрит вверх на гирлянду разноцветных треугольных флажков поворота, натянутую над дорожкой")

# 4. «Горизонт» (Зеленоград): солнышко в плавательных очках наполовину нырнуло за горизонт воды
add("pool-gorizont-zelenograd", "dusk",
    f'<circle cx="64" cy="70" r="34" fill="#FFC93C" {W(3)}/>'
    + "".join(f'<path d="M{64+40*math.cos(a):.1f} {70-40*math.sin(a):.1f} L{64+50*math.cos(a):.1f} {70-50*math.sin(a):.1f}" stroke="#FFE27A" stroke-width="5" stroke-linecap="round"/>'
              for a in [math.radians(d) for d in (20, 50, 90, 130, 160)])
    + f'<path d="M38 56 H90" stroke="#3B3355" stroke-width="4"/>'
    + f'<ellipse cx="52" cy="58" rx="10" ry="8" fill="#7FD0F5" {W(3)}/><ellipse cx="76" cy="58" rx="10" ry="8" fill="#7FD0F5" {W(3)}/>'
    + eye(52, 58, 0.7) + eye(76, 58, 0.7)
    + f'<ellipse cx="44" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="84" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>'
    + f'<path d="M58 66 Q64 72 70 66" fill="none" {W(2.6)}/>'
    + f'<rect x="-6" y="76" width="140" height="60" fill="#4D7BD8"/>'
    + f'<path d="M-6 76 H134" {W(3)}/>'
    + "".join(f'<path d="M{64-w} {y} H{64+w}" stroke="#FFE27A" stroke-width="4" stroke-linecap="round"/>' for w, y in [(30, 86), (22, 96), (14, 106), (8, 116)])
    + f'<path d="M10 92 q6 -4 12 0 M104 100 q6 -4 12 0" fill="none" stroke="#BFE8FF" stroke-width="2.6" stroke-linecap="round"/>',
    "солнышко в голубых плавательных очках",
    "наполовину нырнуло за горизонт воды бассейна, по воде к зрителю бежит золотая дорожка")

# 5. «Кристалл» (Электросталь): голубой кристалл ныряет головой вниз, за ним цепочка пузырей
add("pool-kristall-elektrostal", "aqua",
    f'<rect x="-6" y="56" width="140" height="80" fill="#2F9FD6"/>'
    + f'<path d="M-6 56 q16 -6 32 0 t32 0 t32 0 t32 0 t32 0" fill="none" stroke="#BFF3FF" stroke-width="3"/>'
    + G(64, 70, f'<polygon points="0,-34 22,-12 14,30 -14,30 -22,-12" fill="#BDEBFF" {W(3)}/>'
        f'<path d="M0 -34 L-6 -12 L0 30 M0 -34 L6 -12 L0 30 M-22 -12 H22" fill="none" stroke="#7FC8EA" stroke-width="2"/>'
        f'<polygon points="0,-34 22,-12 14,30 -14,30 -22,-12" fill="none" {W(3)}/>'
        + face(0, 2, d=7, k=0.6), rot=180)
    + bubbles([(70, 30, 4), (76, 20, 3), (66, 12, 2.5), (58, 40, 5)], "#FFFFFF")
    + sparkle(36, 74, 6) + sparkle(94, 92, 5) + sparkle(42, 108, 4)
    + f'<path d="M30 56 q-6 -12 -16 -10 M98 56 q6 -12 16 -10" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>',
    "голубой гранёный кристалл-ныряльщик",
    "ныряет головой вниз в синюю воду бассейна, оставляя наверху цепочку пузырей и блёстки")

# 6. «Малино» (Зеленоград): малинка в белой шапочке держится за бортик и болтает ножками
_rasp = "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#E23D6E" {W(2.4)}/>' for x, y in
                [(-14, -6), (0, -10), (14, -6), (-18, 8), (-4, 6), (10, 6), (20, 8), (-10, 20), (4, 22), (16, 18), (-2, 34), (10, 30)])
add("pool-malino-zelenograd", "rose",
    water(84, "#5BC0EA", amp=3, n=5, edge="#3C9AD0")
    + edge(72, "#FFFFFF", "#E0D6E6")
    + G(64, 70, _rasp)
    + f'<path d="M44 58 Q44 34 64 34 Q84 34 84 58 Q64 50 44 58Z" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M58 34 Q64 24 72 30 Q66 34 58 34Z" fill="#4FBF6B" {W(2)}/>'
    + face(64, 66, d=7, k=0.62)
    + limb("M48 72 Q42 70 40 74", "#4FBF6B", 5) + limb("M80 72 Q86 70 88 74", "#4FBF6B", 5)
    + limb("M58 100 q-6 10 -16 8", "#4FBF6B", 5) + limb("M70 100 q6 10 16 6", "#4FBF6B", 5)
    + drops([(30, 92), (98, 90), (36, 104)], "#BFE8FF"),
    "ягодка-малинка в белой плавательной шапочке",
    "держится зелёными лапками за белый бортик маленького бассейна и болтает ножками, поднимая брызги")

# 7. ДЮСШ «Чайка» (Озёры): колобашка-восьмёрка сама плывёт по дорожке, загребая ручками
add("pool-chayka-ozery", "olive",
    f'<rect x="-6" y="40" width="140" height="96" fill="#4FB6E8"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}" {W(1.4)}/>' for y in (44, 116) for x, c in zip(range(-2, 134, 10), ["#2E6FD0", "#FFFFFF"] * 7))
    + f'<path d="M-6 80 H134" stroke="#2A6FB8" stroke-width="5" opacity=".5"/>'
    + G(66, 80, f'<path d="M-34 -12 Q-36 -24 -20 -24 Q-6 -24 -4 -10 Q0 -4 4 -10 Q6 -24 20 -24 Q36 -24 34 -12 Q36 0 34 12 Q36 24 20 24 '
        f'Q6 24 4 10 Q0 4 -4 10 Q-6 24 -20 24 Q-36 24 -34 12 Q-36 0 -34 -12Z" fill="#FFD23F" {W(3)}/>'
        f'<path d="M4 -10 Q6 -24 20 -24 Q36 -24 34 -12 Q36 0 34 12 Q36 24 20 24 Q6 24 4 10Z" fill="#2E6FD0" {W(3)}/>'
        + face(-18, 0, d=6, k=0.55) + face(20, 0, d=6, k=0.55, mouth=False), rot=-8)
    + limb("M30 70 Q18 58 8 66", "#FFD23F", 5) + limb("M98 72 Q110 60 120 68", "#2E6FD0", 5)
    + f'<path d="M20 98 q8 -6 16 0 M86 100 q8 -6 16 0" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    + drops([(6, 58), (120, 56)], "#BFE8FF"),
    "жёлто-синяя колобашка-восьмёрка для плавания",
    "сама плывёт по дорожке, загребая ручками, — тренировка «только руки»")

# 8. «Дельфин» (Видное): мальчик в оранжевой маске ныряет на дно за тонущими колечками
add("pool-delfin-vidnoe", "coral",
    f'<rect x="-6" y="24" width="140" height="112" fill="#4FB6E8"/>'
    + f'<path d="M-6 24 q16 -5 32 0 t32 0 t32 0 t32 0 t32 0" fill="none" stroke="#FFFFFF" stroke-width="3"/>'
    + f'<rect x="-6" y="104" width="140" height="30" fill="#BFEFF5"/>'
    + "".join(f'<path d="M{x} 104 V134" stroke="#8FD3E3" stroke-width="1.6"/>' for x in range(4, 130, 16))
    + f'<path d="M-6 104 H134" stroke="#8FD3E3" stroke-width="2"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="4" fill="none" stroke="{O}" stroke-width="7.6"/><ellipse cx="{x}" cy="{y}" rx="10" ry="4" fill="none" stroke="{c}" stroke-width="4.6"/>'
              for x, y, c in [(28, 112, RED), (104, 116, "#FFC93C")])
    + f'<ellipse cx="84" cy="110" rx="10" ry="4" fill="none" stroke="{O}" stroke-width="7.6"/><ellipse cx="84" cy="110" rx="10" ry="4" fill="none" stroke="#4FBF6B" stroke-width="4.6"/>'
    + G(60, 70, f'<path d="M-10 -8 Q-30 -30 -26 -50" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
        f'<path d="M-10 -8 Q-30 -30 -26 -50" fill="none" stroke="#2E6FD0" stroke-width="6" stroke-linecap="round"/>'
        f'<path d="M6 -6 Q20 -28 30 -40" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
        f'<path d="M6 -6 Q20 -28 30 -40" fill="none" stroke="#2E6FD0" stroke-width="6" stroke-linecap="round"/>'
        f'<path d="M-14 -14 Q-16 10 0 14 Q16 10 14 -14Z" fill="#FFC93C" {W(3)}/>'
        f'<circle cx="0" cy="22" r="14" fill="{SKIN}" {W(3)}/>'
        f'<rect x="-13" y="16" width="26" height="12" rx="5" fill="#BFE8FF" stroke="{ORG}" stroke-width="4"/>'
        + eye(-5, 22, 0.5) + eye(5, 22, 0.5)
        + f'<path d="M14 14 V-2" stroke="{ORG}" stroke-width="4" stroke-linecap="round"/>', rot=-20)
    + limb("M50 92 Q40 104 30 108", SKIN, 6)
    + bubbles([(76, 50, 4), (82, 40, 3), (78, 30, 2.5)], "#FFFFFF"),
    "мальчик в оранжевой маске для ныряния",
    "ныряет на кафельное дно за разноцветными тонущими колечками и тянется рукой к красному")

# 9. Московская академия плавания «Косино»: синхронистка с зажимом на носу вынырнула с руками-«звёздочкой»
add("pool-kosino-msa", "lilac",
    water(86, "#5BC0EA", amp=4, n=4, edge="#3C9AD0")
    + limb("M46 70 L22 34", SKIN, 7) + limb("M82 70 L106 34", SKIN, 7)
    + f'<circle cx="20" cy="31" r="4.4" fill="{SKIN}" {W(2)}/><circle cx="108" cy="31" r="4.4" fill="{SKIN}" {W(2)}/>'
    + f'<path d="M44 96 Q42 70 64 68 Q86 70 84 96Z" fill="#E8318A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#FFFFFF"/>' for x, y in [(54, 80), (70, 76), (62, 88), (76, 86)])
    + f'<circle cx="64" cy="52" r="18" fill="{SKIN}" {W(3)}/>'
    + f'<path d="M46 52 Q44 30 64 30 Q84 30 82 52 Q64 42 46 52Z" fill="#FFC93C" {W(2.8)}/>'
    + "".join(sparkle(x, y, 3.2, "#FFFFFF") for x, y in [(56, 38), (70, 36), (64, 44)])
    + face(64, 54, d=7, k=0.62, mouth=False)
    + f'<path d="M55 61 Q64 70 73 61 Z" fill="#FFFFFF" {W(2.4)}/>'
    + f'<rect x="60" y="51" width="8" height="5" rx="2" fill="#2E6FD0" {W(1.6)}/>'
    + sparkle(30, 60, 5) + sparkle(100, 62, 5) + sparkle(64, 18, 4),
    "девочка-синхронистка с зажимом на носу и блёстками на жёлтой шапочке",
    "вынырнула по пояс, вскинув прямые руки «звёздочкой», и сияет улыбкой во весь рот")

# 10. «Нева» (Дзержинский): пловчиха делает кувырок-поворот у стенки, ногами отталкиваясь от плитки
add("pool-neva-dzerzhinsky", "steel",
    f'<rect x="-6" y="40" width="96" height="96" fill="#4FB6E8"/>'
    + f'<path d="M-6 40 q12 -5 24 0 t24 0 t24 0 t24 0" fill="none" stroke="#FFFFFF" stroke-width="3"/>'
    + f'<rect x="90" y="30" width="44" height="106" fill="#F4F1EA"/>'
    + "".join(f'<path d="M90 {y} H134" stroke="#CFC8BA" stroke-width="1.6"/>' for y in range(42, 136, 12))
    + "".join(f'<path d="M{x} 30 V136" stroke="#CFC8BA" stroke-width="1.6"/>' for x in (104, 118))
    + f'<path d="M90 30 V136" {W(3)}/>'
    + f'<rect x="88" y="66" width="6" height="34" fill="#2E2A36"/>'
    + G(56, 82, f'<path d="M-16 -4 Q-20 -24 0 -26 Q20 -24 18 -4 Q16 14 0 14 Q-18 14 -16 -4Z" fill="{RED}" {W(3)}/>'
        + limb("M10 -10 L30 -16 L30 -2", SKIN, 7) + limb("M10 4 L30 6 L30 18", SKIN, 7)
        + f'<circle cx="-18" cy="10" r="14" fill="{SKIN}" {W(3)}/>'
        f'<path d="M-32 8 Q-32 -6 -18 -6 Q-4 -6 -4 8 Q-18 2 -32 8Z" fill="{RED}" {W(2.6)}/>'
        + face(-18, 12, d=5, k=0.5), rot=-30)
    + f'<path d="M30 70 a26 26 0 1 0 8 -24" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="6 6"/>'
    + f'<path d="M34 42 l6 4 l-7 3" fill="none" stroke="#FFFFFF" stroke-width="3"/>'
    + bubbles([(76, 112, 4), (70, 120, 3), (80, 124, 2.5)], "#FFFFFF"),
    "пловчиха в красной шапочке и красном купальнике",
    "делает кувырок-поворот под водой у стенки бассейна, отталкиваясь ногами от кафельной плитки")

# 11. «Олимп» (Серпухов, детский бассейн): грибок-фонтан поливает двух малышей в лягушатнике
add("pool-olimp-serpukhov", "peach",
    water(88, "#7FD0F5", amp=3, n=4, edge="#3C9AD0")
    + f'<rect x="58" y="44" width="12" height="48" fill="#FFFFFF" {W(3)}/>'
    + f'<path d="M24 50 Q30 18 64 16 Q98 18 104 50 Q64 40 24 50Z" fill="#E8554A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4.2" fill="#FFFFFF"/>' for x, y in [(44, 32), (64, 26), (84, 32), (56, 40), (74, 40)])
    + face(64, 62, d=4, k=0.45)
    + "".join(f'<path d="M{x} 50 Q{x+(x-64)*0.25:.0f} 64 {x+(x-64)*0.45:.0f} 80" fill="none" stroke="#BFE8FF" stroke-width="2.6" stroke-dasharray="4 4"/>'
              for x in (28, 38, 48, 80, 90, 100))
    + capkid(26, 88, "#FFC93C", sc=0.8) + capkid(104, 90, "#4FBF6B", sc=0.8, closed=True)
    + limb("M16 92 L10 80", SKIN, 4) + limb("M36 92 L42 80", SKIN, 4),
    "грибок-фонтан детского бассейна с красной шляпкой в белый горох",
    "поливает зонтиком струек двух малышей в лягушатнике — один радуется, другой зажмурился")

# 12. Школа плавания № 1: малыш держится за доску с цифрой «1» и бьёт ножками
add("swim-school-1-fotievoy", "mint",
    water(74, "#5BC0EA", amp=3, n=4, edge="#3C9AD0")
    + f'<path d="M20 58 Q20 44 34 44 H64 Q78 44 78 58 V78 Q78 86 70 86 H28 Q20 86 20 78Z" fill="#5CB7F2" {W(3)}/>'
    + f'<text x="49" y="80" font-family="Arial Black, Arial" font-weight="900" font-size="32" text-anchor="middle" fill="#FFFFFF" stroke="{O}" stroke-width="2">1</text>'
    + face(49, 54, d=8, k=0.6)
    + f'<circle cx="34" cy="89" r="5" fill="{SKIN}" {W(2)}/><circle cx="62" cy="89" r="5" fill="{SKIN}" {W(2)}/>'
    + limb("M36 92 Q46 100 60 100", SKIN, 6) + limb("M62 92 Q70 100 78 100", SKIN, 6)
    + capkid(90, 96, RED, sc=0.95)
    + limb("M100 104 q10 -2 16 6", SKIN, 6) + limb("M100 108 q8 6 12 14", SKIN, 6)
    + drops([(116, 92), (122, 104), (110, 118)], "#BFE8FF")
    + sparkle(96, 30, 5) + sparkle(26, 26, 4),
    "голубая пенопластовая доска для плавания с цифрой «1»",
    "малыш в красной шапочке держится за неё вытянутыми руками и бьёт ножками, впервые плывя сам")

# 13. «Сатурн» (Раменское): мальчик-брассист плывёт в вечернем бассейне, в окне — планета с кольцом
add("pool-saturn-ramenskoe", "night",
    f'<rect x="20" y="14" width="88" height="44" rx="4" fill="#2B2F6E" {W(3)}/>'
    + f'<path d="M64 14 V58 M20 36 H108" {W(2.4)}/>'
    + f'<circle cx="86" cy="28" r="8" fill="#FFC93C" {W(2.2)}/>'
    + f'<ellipse cx="86" cy="28" rx="15" ry="4" fill="none" stroke="#FFE27A" stroke-width="2.6" transform="rotate(-18 86 28)"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#FFFFFF"/>' for x, y in [(30, 22), (44, 30), (52, 18), (34, 46), (98, 48), (72, 46)])
    + water(70, "#3E8FD8", amp=4, n=4, edge="#2A6FB8")
    + limb("M50 86 Q30 76 20 88", SKIN, 6) + limb("M78 86 Q98 76 108 88", SKIN, 6)
    + f'<circle cx="18" cy="89" r="4.6" fill="{SKIN}" {W(2)}/><circle cx="110" cy="89" r="4.6" fill="{SKIN}" {W(2)}/>'
    + capkid(64, 84, "#2E6FD0", sc=1.15)
    + f'<path d="M40 104 q8 -6 16 0 t16 0 t16 0" fill="none" stroke="#BFE8FF" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(14, 60, 3.6, "#FFE27A"),
    "мальчик-брассист в синей шапочке",
    "плывёт брассом, разведя руки, в вечернем бассейне, а в большом окне над водой светит планета с кольцом")

# ============================== ШАХМАТЫ ==============================
# 14. «Шахматное королевство» (Царицыно, библиотека): слон-библиотекарь в очках листает учебник на стопке книг
add("chess-korolevstvo-tsaritsyno", "berry",
    "".join(f'<rect x="{x}" y="{y}" width="{w}" height="12" rx="2" fill="{c}" {W(2.6)}/>'
            for x, y, w, c in [(30, 108, 68, "#4FBF6B"), (34, 96, 60, "#5CB7F2"), (28, 84, 70, "#FFC93C")])
    + G(64, 84, bishop(WHITE, sc=0.78))
    + f'<circle cx="59" cy="38" r="5" fill="none" stroke="{O}" stroke-width="2.2"/><circle cx="69" cy="38" r="5" fill="none" stroke="{O}" stroke-width="2.2"/>'
    + f'<path d="M64 38 H64" {W(2)}/>'
    + G(64, 70, f'<path d="M-30 -6 Q-15 -12 0 -4 Q15 -12 30 -6 V12 Q15 6 0 14 Q-15 6 -30 12Z" fill="#FFF7EC" {W(2.8)}/>'
        f'<path d="M0 -4 V14" {W(2)}/>'
        + "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="#8A6A55"/>' for x, y in [(-24, -2), (-14, -2), (-19, 3), (12, -2), (22, -2), (17, 3)]))
    + sparkle(22, 30, 5) + sparkle(108, 46, 4),
    "белый шахматный слон-библиотекарь в круглых очках",
    "сидит на стопке разноцветных книг и листает раскрытый шахматный учебник с клетками")

# 15. «Шахматное королевство» (Бирюлёво): ладья-крепость опустила подъёмный мост, по нему въезжает белый конь
add("chess-korolevstvo-biryulevo", "mango",
    f'<path d="M-6 112 Q64 100 134 112 V134 H-6Z" fill="#7CC46A" {W(2.6)}/>'
    + f'<path d="M-6 118 H134" stroke="#5CB7F2" stroke-width="10" opacity=".8"/>'
    + G(76, 112, rook(BLACK, sc=1.15, fy=-46))
    + f'<path d="M58 30 V8 L74 14 L58 20" fill="{RED}" {W(2.4)}/>'
    + f'<path d="M66 108 L28 116" stroke="#8A5A3C" stroke-width="8"/><path d="M66 108 L28 116" {W(1.6)}/>'
    + f'<path d="M66 82 L30 108" stroke="{O}" stroke-width="1.6"/>'
    + f'<rect x="64" y="80" width="18" height="28" rx="9" fill="#2E2A36" stroke="#FFFFFF" stroke-width="1.6"/>'
    + G(34, 114, knight(WHITE, sc=0.5, flip=True)),
    "чёрная шахматная ладья-крепость с красным флажком и подъёмным мостом",
    "опустила мост через ров, и по нему в ворота въезжает маленький белый конь")

# 16. «Шахматное королевство» (Братеево): кони-братья играют в чехарду — белый прыгает буквой «Г»
add("chess-korolevstvo-brateevo", "teal",
    "".join(f'<rect x="{x}" y="{y}" width="16" height="16" fill="{"#FFF2D8" if (x//16+y//16) % 2 else "#5E9E8E"}"/>' for x in range(-8, 136, 16) for y in (104, 120))
    + f'<path d="M-6 104 H134" {W(2.6)}/>'
    + G(76, 108, knight(BLACK, sc=0.72))
    + G(48, 62, knight(WHITE, sc=0.66), rot=-14)
    + f'<path d="M30 102 V44 H64" fill="none" stroke="{GOLD}" stroke-width="3.4" stroke-dasharray="6 5" stroke-linecap="round"/>'
    + f'<path d="M60 39 L68 44 L60 49" fill="none" stroke="{GOLD}" stroke-width="3.4" stroke-linecap="round"/>'
    + sparkle(104, 34, 5) + sparkle(16, 28, 4),
    "белый и чёрный шахматные кони-братья",
    "белый перепрыгивает через чёрного по пунктирной букве «Г», как в чехарде на шахматной доске")

# ============================== БАДМИНТОН ==============================
# 17. Купавинский бадминтон-клуб: волан с юбкой из лепестков жёлтой купавы парит над сеткой на летней площадке
add("badminton-kupavna", "green",
    f'<path d="M-6 104 Q64 96 134 104 V134 H-6Z" fill="#8BD46E" {W(2.6)}/>'
    + f'<ellipse cx="64" cy="110" rx="22" ry="4" fill="#3B3355" opacity=".25"/>'
    + f'<path d="M6 104 V70 M122 104 V70" {W(3.2)}/>'
    + f'<rect x="6" y="70" width="116" height="16" fill="#FFFFFF" fill-opacity=".35"/>'
    + "".join(f'<path d="M{x} 70 V86" stroke="{O}" stroke-width="1" opacity=".6"/>' for x in range(12, 122, 7))
    + f'<path d="M6 70 H122 M6 86 H122" {W(2.4)}/>'
    + G(64, 50, shuttle(feathers=("#FFD23F", "#FFC024", "#FFD23F", "#FFC024", "#FFD23F"), cork="#FFFFFF", band="#4FBF6B"), rot=-12, sc=0.78)
    + "".join(f'<path d="M{x} {y} q-6 -10 0 -18 q6 8 0 18Z" fill="#4FBF6B" {W(1.6)}/>' for x, y in [(20, 104), (110, 106), (96, 104)]),
    "волан с юбкой из жёлтых лепестков купавы и зелёной перевязкой",
    "парит над сеткой на летней травяной площадке, отбрасывая на траву круглую тень")

# ============================== БАСКЕТБОЛ «СТРЕМЛЕНИЕ» ==============================
# 18. Каланчёвская (у трёх вокзалов): мяч-путешественник с чемоданчиком спешит на поезд мимо башни с часами
add("stremlenie-basket-kalanchevskaya", "sand",
    f'<path d="M84 120 V40 L96 22 L108 40 V120Z" fill="#E8C9A0" {W(3)}/>'
    + f'<path d="M96 8 V22" {W(2.6)}/><circle cx="96" cy="50" r="9" fill="#FFFFFF" {W(2.4)}/>'
    + f'<path d="M96 50 V44 M96 50 L100 52" {W(2)}/>'
    + f'<rect x="88" y="70" width="16" height="22" rx="8" fill="#8A6A55" {W(2.4)}/>'
    + f'<path d="M-6 118 H134" stroke="#8A6A55" stroke-width="4"/>'
    + "".join(f'<rect x="{x}" y="116" width="8" height="4" fill="#8A6A55"/>' for x in range(-2, 134, 14))
    + ball(52, 74, 26)
    + limb("M30 82 Q20 90 22 98", ORG, 5)
    + f'<rect x="8" y="96" width="30" height="20" rx="4" fill="#E8554A" {W(3)}/>'
    + f'<path d="M17 96 V91 H29 V96" fill="none" {W(2.6)}/><path d="M8 105 H38" stroke="#FFFFFF" stroke-width="2"/>'
    + limb("M46 98 L40 112", ORG, 5) + limb("M60 98 L68 112", ORG, 5)
    + f'<path d="M80 70 h-8 M82 80 h-10" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>',
    "баскетбольный мяч-путешественник с красным чемоданчиком",
    "спешит на тренировку мимо вокзальной башни с часами, перешагивая через рельсы")

# 19. Пражская: девочка-баскетболистка в жёлтой форме висит на кольце после броска сверху
add("stremlenie-basket-prazhskaya", "orange",
    hoop(74, 40, w=40, board=True)
    + ball(76, 84, 13, fc=False)
    + f'<path d="M66 102 l-4 6 M86 102 l4 6" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    + limb("M44 72 L54 42", SKIN, 6) + limb("M40 72 L42 42", SKIN, 6)
    + f'<circle cx="54" cy="41" r="4" fill="{SKIN}" {W(2)}/><circle cx="42" cy="41" r="4" fill="{SKIN}" {W(2)}/>'
    + f'<path d="M28 62 Q22 50 30 46 Q34 56 34 62Z" fill="#7A4A2E" {W(2.2)}/>'
    + f'<circle cx="40" cy="62" r="12" fill="{SKIN}" {W(3)}/>'
    + f'<path d="M28 60 Q28 48 40 48 Q52 48 52 60 Q44 54 40 56 Q34 54 28 60Z" fill="#7A4A2E" {W(2.4)}/>'
    + f'<circle cx="29" cy="52" r="3" fill="{RED}" {W(1.4)}/>'
    + face(40, 64, d=4.5, k=0.45)
    + f'<path d="M28 76 Q28 72 40 72 Q52 72 52 76 L50 102 H30Z" fill="#FFD23F" {W(3)}/>'
    + f'<text x="40" y="96" font-family="Arial Black, Arial" font-weight="900" font-size="15" text-anchor="middle" fill="{RED}">7</text>'
    + limb("M34 102 L30 120", SKIN, 6) + limb("M46 102 L52 118", SKIN, 6)
    + sparkle(104, 76, 5) + sparkle(18, 30, 4),
    "девочка-баскетболистка в жёлтой форме с хвостиком",
    "висит на кольце после броска сверху, а мяч проваливается сквозь сетку")

# 20. Балаклавский: три мяча-брата — большой, средний и маленький — выстроились по росту
add("stremlenie-basket-balaklavsky", "purple",
    f'<path d="M-6 108 H134 V134 H-6Z" fill="#E8C9A0" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 108 V134" stroke="#C9A77C" stroke-width="2"/>' for x in range(10, 130, 20))
    + ball(36, 78, 30)
    + ball(80, 90, 18)
    + ball(108, 84, 11, fc=True)
    + f'<path d="M100 102 q8 4 16 0" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<ellipse cx="108" cy="104" rx="9" ry="2.6" fill="#3B3355" opacity=".25"/>'
    + sparkle(106, 60, 5) + sparkle(70, 58, 4),
    "три баскетбольных мяча-брата — большой, средний и маленький",
    "выстроились по росту, как матрёшки, а младший подпрыгнул от нетерпения")

# 21. Коньково: малыш в огромной майке до пят бросает мяч снизу в низкое детское кольцо
add("stremlenie-basket-konkovo", "yellow",
    f'<path d="M-6 112 H134 V134 H-6Z" fill="#E8C9A0" {W(2.6)}/>'
    + f'<path d="M104 112 V48" stroke="#8A8FA8" stroke-width="6"/><path d="M104 112 V48" {W(1.6)}/>'
    + hoop(92, 52, w=26, board=False)
    + f'<rect x="100" y="24" width="12" height="32" rx="3" fill="#FFFFFF" {W(2.6)}/>'
    + ball(66, 36, 13, fc=False)
    + f'<path d="M50 58 l6 -8 M44 54 l4 -8" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M20 116 Q16 76 40 70 Q64 76 60 116Z" fill="#E8554A" {W(3)}/>'
    + f'<text x="40" y="104" font-family="Arial Black, Arial" font-weight="900" font-size="18" text-anchor="middle" fill="#FFFFFF" stroke="{O}" stroke-width="1.2">3</text>'
    + limb("M28 80 Q34 62 52 48", SKIN, 6) + limb("M52 80 Q58 62 58 48", SKIN, 6)
    + f'<circle cx="40" cy="56" r="14" fill="{SKIN}" {W(3)}/>'
    + f'<path d="M26 54 Q28 38 40 40 Q52 38 54 54 Q46 46 40 48 Q34 46 26 54Z" fill="#7A4A2E" {W(2.4)}/>'
    + face(40, 59, d=5, k=0.5)
    + f'<ellipse cx="32" cy="117" rx="7" ry="3" fill="#FFFFFF" {W(2)}/><ellipse cx="50" cy="117" rx="7" ry="3" fill="#FFFFFF" {W(2)}/>',
    "малыш в огромной красной майке до пят",
    "двумя руками бросает мяч снизу в низкое детское кольцо на стойке")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for pid, code in ICONS.items():
        open(os.path.join(OUT, pid + ".svg"), "w").write(code)
    reg = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(reg, encoding="utf-8") if l.split(" — ", 1)[0] not in SUBJ]
    lines += [line + "\n" for line in SUBJ.values()]
    open(reg, "w", encoding="utf-8").writelines(lines)
    print(len(ICONS), "иконок:", " ".join(ICONS))
