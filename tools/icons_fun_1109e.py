"""Иконки робота fun (2026-11-09, 4-й проход): 3 места из tools/add_fun_1109e.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности); сюжеты сверены с subjects.txt.
Запуск: python3 tools/icons_fun_1109e.py  (пишет icons-src/<id>.svg и печатает строки для subjects.txt)"""
import os
from draw_icons import s, face, sparkle

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


I = {}

# Жуковский — город авиации; детский клуб с изостудией: аэродромный «колдун» сушит детские рисунки
I["sovenok-club-zhukovsky"] = ("#E6F7FF", "#5FB2E8",
    "полосатый аэродромный ветроуказатель-«колдун» с мордашкой",
    "надулся от ветра на мачте, а на его полосках сушатся прищепками детские рисунки",
    f'<path d="M18 128 L22 30" {W(4)}/><circle cx="22" cy="28" r="5" fill="#E8434A" {W(2.4)}/>'
    f'<path d="M22 36 L104 48 L104 74 L22 82Z" fill="#fff" {W(3)}/>'
    f'<path d="M22 36 L46 39.5 L46 78.5 L22 82Z" fill="#FF7A2F"/>'
    f'<path d="M64 42 L84 45 L84 71 L64 74Z" fill="#FF7A2F"/>'
    f'<path d="M22 36 L104 48 L104 74 L22 82Z" fill="none" {W(3)}/>'
    f'<ellipse cx="104" cy="61" rx="6" ry="13" fill="#FFB27A" {W(2.6)}/>'
    + face(56, 58, d=8, k=0.75) +
    f'<path d="M30 92 Q64 100 112 88" fill="none" {W(2)}/>'
    f'<rect x="38" y="94" width="20" height="22" fill="#FFF7D6" {W(2.2)}/><circle cx="48" cy="104" r="5" fill="#FFD23F"/>'
    f'<path d="M42 112 L48 106 L54 112" fill="none" stroke="#4CC38A" stroke-width="2.4"/>'
    f'<rect x="72" y="92" width="20" height="22" fill="#FFF7D6" {W(2.2)}/>'
    f'<path d="M76 106 Q82 96 88 106" fill="none" stroke="#E8434A" stroke-width="2.6"/><path d="M76 110 H88" stroke="#5FB2E8" stroke-width="2.6"/>'
    f'<rect x="45" y="90" width="5" height="7" fill="#C98B4E" {W(1.6)}/><rect x="79" y="88" width="5" height="7" fill="#C98B4E" {W(1.6)}/>'
    + sparkle(110, 28, 5) + sparkle(92, 20, 3.5))

# «Капитоша» — группы «Самостоятельный малыш»: ботиночек сам застёгивает липучку
I["kapitosha-ramenskoe"] = ("#FFF4E8", "#F5A86B",
    "детский ботиночек на липучке с мордашкой на носке",
    "сидит на низкой деревянной скамеечке в раздевалке и сам гордо застёгивает свою липучку",
    f'<rect x="10" y="94" width="108" height="10" rx="3" fill="#C98B4E" {W(3)}/>'
    f'<path d="M22 104 V124 M106 104 V124" {W(5)}/>'
    f'<path d="M36 92 L36 46 Q36 38 46 38 L66 38 Q74 38 74 46 L74 62 Q100 62 106 78 Q110 92 96 92Z" fill="#4C8DF0" {W(3.2)}/>'
    f'<path d="M34 92 H104" {W(4)}/><rect x="32" y="88" width="76" height="8" rx="4" fill="#fff" {W(2.6)}/>'
    f'<path d="M44 52 Q62 46 80 58 L76 70 Q60 60 44 66Z" fill="#FFD23F" {W(2.6)}/>'
    f'<path d="M50 56 L52 62 M58 54 L59 60 M66 54 L66 60" stroke="#C9A21F" stroke-width="1.8" stroke-linecap="round"/>'
    + face(88, 78, d=6, k=0.55) +
    f'<path d="M80 58 Q90 50 96 54" fill="none" {W(2.4)}/>'
    + sparkle(100, 36, 6, "#FFF6A8") + sparkle(26, 30, 4, "#FFF6A8"))

# «Золушка» — «Школа изобретателей», занятия в форме сюжетной игры: песочные часы решают задачку
I["zolushka-center-odintsovo"] = ("#F3F0FF", "#8C7BE0",
    "песочные часы с золотым песком и мордашкой на верхней колбе",
    "стоят на раскрытой тетради в клетку, где карандашом решена задачка «2+3=5»",
    f'<path d="M6 104 L64 92 L122 104 L122 124 L6 124Z" fill="#fff" {W(3)}/>'
    f'<path d="M64 92 V124" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {96 + abs(64 - x) * .2:.1f} V124" stroke="#B9D3F5" stroke-width="1.2"/>' for x in range(14, 120, 8)) +
    f'<text x="76" y="118" font-family="Arial" font-weight="700" font-size="11" fill="#3B6FD8">2+3=5</text>'
    f'<rect x="36" y="20" width="56" height="8" rx="3" fill="#C98B4E" {W(2.8)}/>'
    f'<rect x="36" y="88" width="56" height="8" rx="3" fill="#C98B4E" {W(2.8)}/>'
    f'<path d="M42 28 Q42 50 62 58 Q42 66 42 88 L86 88 Q86 66 66 58 Q86 50 86 28Z" fill="#EAF6FF" {W(3)}/>'
    f'<path d="M46 34 Q48 48 64 54 Q80 48 82 34Z" fill="#FFC93C"/>'
    f'<path d="M64 58 V80" stroke="#FFC93C" stroke-width="2.6"/>'
    f'<path d="M48 88 Q64 70 80 88Z" fill="#FFC93C"/>'
    f'<path d="M42 28 Q42 50 62 58 Q42 66 42 88 L86 88 Q86 66 66 58 Q86 50 86 28Z" fill="none" {W(3)}/>'
    + face(64, 40, d=7, k=0.6) +
    f'<path d="M24 40 L42 44" stroke="#FFE36B" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(104, 34, 7, "#FFE36B") + sparkle(22, 60, 4, "#FFE36B"))

if __name__ == "__main__":
    for pid, (a, b, hero, scene, body) in I.items():
        open(os.path.join(out, pid + ".svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
