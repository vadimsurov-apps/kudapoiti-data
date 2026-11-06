"""Иконки 19 падел-клубов (06.11). Сюжеты проверены по icons-src/subjects.txt и каталогу — не заняты."""
import os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda x, y, d=6, k=0.5, **kw: face(x, y, d=d, k=k, **kw)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
SUBJ = {}
I = {}


def add(pid, subj, bg, body):
    SUBJ[pid] = subj; I[pid] = (bg, body)


add("padel-lunda-konstruktor", "рулон обмотки-грипа", "purple",
    f'<ellipse cx="64" cy="70" rx="34" ry="34" fill="#FF7FA8" {s()}/><ellipse cx="64" cy="70" rx="13" ry="13" fill="#fff" {W(3)}/>'
    f'<path d="M34 54 Q64 44 94 54 M30 72 Q64 62 98 72 M36 90 Q64 80 92 90" fill="none" stroke="#E8558A" stroke-width="3"/>'
    f'<path d="M96 76 Q112 92 106 112 L94 108 Q98 94 88 84Z" fill="#FF7FA8" {W(3)}/>' + f(64, 40, d=6, k=0.45) + sparkle(22, 24, 6))
add("padel-lunda-rechnoy", "рюкзак для падел-ракеток", "teal",
    f'<path d="M30 46 Q30 24 64 24 Q98 24 98 46 V104 Q98 112 90 112 H38 Q30 112 30 104Z" fill="#FF8A3D" {s()}/>'
    f'<path d="M46 24 Q46 12 64 12 Q82 12 82 24" fill="none" {W(4)}/><rect x="40" y="70" width="48" height="30" rx="6" fill="#FFB347" {W(3)}/>'
    f'<path d="M64 70 V100" {W(2.4)}/>' + f(64, 48, d=7, k=0.55) + sparkle(110, 28, 6))
add("padel-luzhniki-academy", "козырёк от солнца", "sky",
    f'<path d="M22 70 Q64 26 106 70" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M22 70 Q64 26 106 70" fill="none" {W(3)}/>'
    f'<path d="M30 66 Q64 78 98 66 Q108 86 92 92 Q64 102 36 92 Q20 86 30 66Z" fill="#5CB7F2" {s()}/>'
    f'<path d="M40 82 Q64 90 88 82" fill="none" stroke="#fff" stroke-width="4"/>' + f(64, 54, d=6, k=0.45) + sparkle(100, 24, 7))
add("padel-friends-luzhniki", "стеклянная дверь корта с ручкой", "green",
    f'<rect x="32" y="16" width="64" height="96" rx="6" fill="#DFF3FF" fill-opacity=".9" {s()}/>'
    f'<path d="M40 26 L58 44 M40 40 L52 52" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="80" y="56" width="8" height="22" rx="4" fill="#9AA0B8" {W(2.4)}/><path d="M32 16 H96" stroke="#3E9BE0" stroke-width="6"/>'
    + f(58, 76, d=7, k=0.55) + sparkle(20, 30, 6))
add("padel-sky-afimall", "шейкер для воды", "night",
    f'<path d="M42 34 H86 L82 108 Q82 114 76 114 H52 Q46 114 46 108Z" fill="#9AE6D8" {s()}/>'
    f'<rect x="40" y="20" width="48" height="16" rx="5" fill="#FF7FA8" {W(3)}/><rect x="56" y="10" width="16" height="12" rx="4" fill="#FF7FA8" {W(3)}/>'
    f'<path d="M48 60 H80" stroke="#fff" stroke-width="4"/>' + f(64, 82, d=7, k=0.55) + sparkle(104, 30, 6) + sparkle(22, 70, 5))
add("padel-tennisru-riviera", "секундомер", "yellow",
    f'<circle cx="64" cy="72" r="38" fill="#fff" {s()}/><circle cx="64" cy="72" r="38" fill="none" stroke="#FF8A3D" stroke-width="7"/>'
    f'<circle cx="64" cy="72" r="38" fill="none" {W(2.6)}/><rect x="56" y="20" width="16" height="12" rx="3" fill="#FF8A3D" {W(3)}/>'
    f'<path d="M92 36 L100 28" {W(5)}/><path d="M64 72 L78 54" {W(4)}/><circle cx="64" cy="72" r="4" fill="{O}"/>'
    + f(64, 92, d=6, k=0.45, blush=False))
add("padel-first-club", "мегафон тренера", "orange",
    f'<path d="M30 56 L82 30 V100 L30 76Z" fill="#fff" {s()}/><rect x="16" y="54" width="16" height="24" rx="4" fill="#E8654F" {W(3)}/>'
    f'<ellipse cx="82" cy="65" rx="10" ry="35" fill="#E8654F" {W(3)}/><path d="M40 78 L46 100 H58 L54 82" fill="#9AA0B8" {W(3)}/>'
    f'<path d="M100 46 Q110 64 100 84 M108 36 Q122 64 108 94" fill="none" {W(3)}/>' + f(54, 62, d=5, k=0.42))
add("padel-park-belokamenny", "банан-перекус", "green",
    f'<path d="M24 40 Q30 100 96 102 Q110 100 104 90 Q50 86 40 36Z" fill="#FFD25E" {s()}/>'
    f'<path d="M24 40 L18 30 L28 28 L34 38" fill="#8A5530" {W(2.6)}/><path d="M40 52 Q48 80 84 90" fill="none" stroke="#E0A830" stroke-width="3"/>'
    + f(66, 84, d=6, k=0.5) + sparkle(102, 30, 7))
add("padel-rink-skolkovo", "пакет со льдом", "blue",
    f'<path d="M26 50 Q26 34 44 34 H84 Q102 34 102 50 V90 Q102 106 84 106 H44 Q26 106 26 90Z" fill="#9ED3FF" {s()}/>'
    f'<rect x="52" y="20" width="24" height="16" rx="4" fill="#fff" {W(3)}/>'
    f'<rect x="38" y="48" width="14" height="14" rx="3" fill="#fff" {W(2)} transform="rotate(12 45 55)"/>'
    f'<rect x="76" y="80" width="12" height="12" rx="3" fill="#fff" {W(2)} transform="rotate(-15 82 86)"/>'
    + f(66, 72, d=7, k=0.55) + sparkle(112, 22, 6))
add("padlhub-nagatino", "тюбик энергетического геля", "pink",
    f'<path d="M40 30 H88 L80 104 Q78 112 70 112 H58 Q50 112 48 104Z" fill="#7CD26E" {s()}/>'
    f'<path d="M40 30 L36 16 H92 L88 30" fill="#5CB04F" {W(3)}/><path d="M58 112 V120 H70 V112" fill="#5CB04F" {W(2.6)}/>'
    f'<path d="M60 46 L52 66 H64 L58 84 L76 58 H64 L70 46Z" fill="#FFD25E" {W(2.4)}/>' + f(64, 94, d=5, k=0.42, blush=False))
add("padlhub-kuntsevo", "флаг на флагштоке", "sky",
    f'<path d="M34 112 V16" {W(5)}/><circle cx="34" cy="14" r="5" fill="#FFD25E" {W(2.4)}/>'
    f'<path d="M36 22 Q60 14 74 24 Q90 34 108 26 V64 Q90 72 74 62 Q60 52 36 60Z" fill="#FF7A8A" {s()}/>'
    + f(70, 42, d=6, k=0.5) + f'<path d="M22 112 H50" {W(5)}/>' + sparkle(104, 92, 6))
add("padel-pari", "мишень на стене корта", "purple",
    f'<rect x="18" y="18" width="92" height="92" rx="10" fill="#DFF3FF" {s()}/>'
    f'<circle cx="64" cy="64" r="34" fill="#fff" {W(3)}/><circle cx="64" cy="64" r="24" fill="#FF7A8A" {W(3)}/>'
    f'<circle cx="64" cy="64" r="13" fill="#fff" {W(3)}/><circle cx="64" cy="64" r="5" fill="#FF7A8A"/>'
    f'<circle cx="84" cy="44" r="8" fill="#D7F25A" {W(2.6)}/>' + f(84, 44, d=2.6, k=0.25, blush=False, mouth=False))
add("padel-korty-setki", "кроссовочный шнурок бантиком", "orange",
    f'<path d="M64 64 Q30 30 22 54 Q18 76 64 64 Q110 76 106 54 Q98 30 64 64Z" fill="#fff" {s()}/>'
    f'<path d="M64 64 Q50 90 40 110 M64 64 Q80 90 92 110" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M64 64 Q50 90 40 110 M64 64 Q80 90 92 110" fill="none" {W(2.6)}/>'
    f'<rect x="34" y="106" width="10" height="12" rx="3" fill="#5CB7F2" {W(2.2)}/><rect x="88" y="106" width="10" height="12" rx="3" fill="#5CB7F2" {W(2.2)}/>'
    f'<circle cx="64" cy="64" r="9" fill="#FF8A3D" {W(2.6)}/>' + sparkle(104, 22, 6))
add("padel-buenos-skladochnaya", "спортивный носок с полосками", "yellow",
    f'<path d="M44 14 H82 V70 Q82 84 94 90 Q110 98 104 110 Q98 118 84 114 L54 104 Q40 98 42 82Z" fill="#fff" {s()}/>'
    f'<path d="M44 26 H82 M44 36 H82" stroke="#5CB7F2" stroke-width="5"/><path d="M44 14 H82" {W(3)}/>'
    + f(62, 60, d=6, k=0.5) + sparkle(22, 40, 6))
add("padel-buenos-vdnh", "штатив с камерой для записи игры", "teal",
    f'<path d="M64 62 L36 114 M64 62 L92 114 M64 62 V114" {W(4)}/>'
    f'<rect x="34" y="24" width="56" height="38" rx="8" fill="#5A5470" {s()}/><circle cx="62" cy="43" r="12" fill="#9ED3FF" {W(3)}/>'
    f'<circle cx="62" cy="43" r="5" fill="#3B3355"/><path d="M90 34 L106 26 V60 L90 52" fill="#5A5470" {W(3)}/>'
    f'<circle cx="44" cy="32" r="3" fill="#FF5A6A"/>' + sparkle(18, 20, 6))
add("padel-vnukovo-sport", "ветроуказатель-конус", "sky",
    f'<path d="M30 112 V18" {W(5)}/><path d="M32 24 L104 34 V54 L32 66Z" fill="#fff" {s()}/>'
    f'<path d="M48 26 V64 M76 30 V60" stroke="#FF8A3D" stroke-width="12"/><path d="M32 24 L104 34 V54 L32 66Z" fill="none" {W(3)}/>'
    + f(92, 44, d=4, k=0.35, blush=False) + f'<path d="M14 98 Q30 92 46 98" fill="none" stroke="#9AA0B8" stroke-width="4" stroke-linecap="round"/>')
add("padel-zhukovka", "членская карта клуба", "green",
    f'<rect x="16" y="34" width="96" height="62" rx="10" fill="#FFC93C" {s()}/>'
    f'<rect x="26" y="46" width="18" height="14" rx="3" fill="#E0A830" {W(2.4)}/><path d="M26 80 H70 M26 88 H54" {W(3)}/>'
    + f(90, 62, d=7, k=0.55) + sparkle(110, 22, 7) + sparkle(18, 106, 5))
add("padel-berta-village", "шезлонг у корта", "yellow",
    f'<path d="M24 94 L52 46 H62 L40 94 M40 94 H104 L94 72 H50" fill="#5CB7F2" {s()}/>'
    f'<path d="M30 94 V108 M96 94 V108" {W(5)}/><path d="M52 46 L62 46 L40 94 L34 94Z" fill="#FF7FA8" {W(3)}/>'
    f'<circle cx="96" cy="30" r="14" fill="#FFD25E" {W(3)}/>' + f(96, 30, d=4.5, k=0.4, blush=False))
add("padel-cooltennis-malevich", "чёрный квадрат в раме", "orange",
    f'<rect x="20" y="20" width="88" height="88" rx="4" fill="#E0A830" {s()}/><rect x="30" y="30" width="68" height="68" fill="#fff" {W(3)}/>'
    f'<rect x="40" y="40" width="48" height="48" fill="#3B3355"/>'
    + eye(56, 60, 0.8).replace(O, "#fff") + eye(72, 60, 0.8).replace(O, "#fff")
    + f'<path d="M58 72 Q64 78 70 72" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

for pid, (bg, body) in I.items():
    open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
with open(os.path.join(out, "subjects.txt"), "a") as fh:
    fh.write("".join(f"{k} — {v}\n" for k, v in SUBJ.items()))
print(len(I))
