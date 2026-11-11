"""Иконки робота cafes, 2026-11-11 (13 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно,
герои сверены с subjects.txt (Цезарь, белый гриб, рожок-стегозавр, сибас, гречка с котлетой, ламаджо — в реестре нет).
Запуск: python3 tools/icons_cafes_1111k.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k_caesar": ("#FFF6E0", "#7FA650"),
    "k_forest": ("#F4ECD9", "#9C6B3E"),
    "k_jurassic": ("#EAF9D8", "#4E9A62"),
    "k_canal": ("#E0F1FF", "#2E6FB0"),
    "k_canteen": ("#FFF0F0", "#D9575F"),
    "k_lemon": ("#FFFBD6", "#E2B21E"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Семейные традиции (Видное): миска «Цезаря», на краю — семья гренок
add("cafe-semeynye-traditsii-vidnoe",
    "большая миска салата «Цезарь» с волнистыми листьями романо и стружкой пармезана",
    "на краю миски, как на семейной скамейке, сидят три гренки — большая, средняя и крошечная",
    "k_caesar", f'''
<path d="M20 70 Q64 64 108 70 Q104 108 64 110 Q24 108 20 70Z" fill="#F4F1EA" {W(3)}/>
<path d="M26 82 Q64 90 102 82" fill="none" stroke="#7FB0C9" stroke-width="3"/>
<path d="M26 70 Q22 50 34 40 Q38 56 44 62 Q42 38 56 28 Q60 50 64 60 Q68 34 84 30 Q84 50 82 62 Q92 44 104 46 Q104 60 102 70Z" fill="#7CC250" {W(2.8)}/>
<path d="M34 46 L42 66 M56 34 L60 64 M82 36 L76 64 M98 52 L92 68" fill="none" stroke="#4E9A2E" stroke-width="2"/>
<path d="M48 56 l10 -4 l2 6 l-10 3Z M70 52 l9 2 l-2 6 l-9 -2Z" fill="#FFF2B0" {W(1.8)}/>
{face(64, 92, d=10, k=1.0)}
<rect x="22" y="56" width="20" height="16" rx="4" fill="#E8B04A" {W(2.6)}/>{face(32, 63, d=4, k=0.55)}
<rect x="88" y="60" width="15" height="12" rx="3.5" fill="#E8B04A" {W(2.4)}/>{face(95.5, 65, d=3.2, k=0.45)}
<rect x="104" y="64" width="9" height="8" rx="2.5" fill="#E8B04A" {W(2)}/>
<circle cx="107" cy="67" r="0.9" fill="{O}"/><circle cx="110" cy="67" r="0.9" fill="{O}"/>
{sparkle(104, 28, 5)}
''')

# 2. Nikol'sky (Зеленоград): белый гриб выглядывает из горки тальятелле
add("cafe-nikolsky-zelenograd",
    "белый гриб-боровичок с коричневой шляпкой",
    "выглядывает из горки ленточной пасты тальятелле на белой тарелке, как из-под осенней листвы, и держит вилку как посох",
    "k_forest", f'''
<ellipse cx="64" cy="104" rx="50" ry="12" fill="#FFFFFF" {W(3)}/>
<path d="M22 100 Q30 74 64 70 Q98 74 106 100 Q64 108 22 100Z" fill="#F6D776" {W(3)}/>
<path d="M28 96 Q46 80 62 92 Q78 80 100 96 M34 88 Q50 76 66 84 Q82 76 96 88" fill="none" stroke="#D9AE3A" stroke-width="3"/>
<path d="M52 82 Q50 60 54 48 L74 48 Q78 60 76 82Z" fill="#F7EBD3" {W(3)}/>
<path d="M30 52 Q32 22 64 20 Q96 22 98 52 Q64 60 30 52Z" fill="#9C5B2E" {W(3)}/>
<path d="M42 34 Q52 28 60 30" fill="none" stroke="#C88A5A" stroke-width="3" stroke-linecap="round"/>
{face(64, 64, d=7, k=0.85)}
<path d="M90 98 L100 40" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M90 98 L100 40" stroke="#C9CED8" stroke-width="3" stroke-linecap="round"/>
<path d="M95 44 L97 30 M100 45 L102 31 M105 46 L107 32" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M82 80 Q86 74 90 78" fill="none" {W(2.4)}/>
''')

# 4. Мореман (Долгопрудный, Набережная): сибас на причале машет теплоходу
add("cafe-moreman-dolgoprudny",
    "сибас на гриле с полосками от решётки и долькой лимона под плавником",
    "стоит хвостом на деревянном причале канала и машет плавником проплывающему вдали белому теплоходику",
    "k_canal", f'''
<path d="M0 92 Q20 88 40 92 T80 92 T128 92 L128 128 L0 128Z" fill="#4E9BD8" {W(2.4)}/>
<path d="M78 80 L112 80 L106 88 L82 88Z" fill="#fff" {W(2)}/><rect x="88" y="72" width="14" height="8" rx="2" fill="#fff" {W(2)}/>
<path d="M14 98 L78 98 L78 106 L14 106Z" fill="#B07A47" {W(2.6)}/>
<path d="M22 106 L22 124 M70 106 L70 124" stroke="{O}" stroke-width="5"/><path d="M22 106 L22 124 M70 106 L70 124" stroke="#8A5B30" stroke-width="2.4"/>
<path d="M38 98 L30 86 L48 90Z" fill="#9FB3C2" {W(2.6)}/>
<path d="M40 92 Q24 60 40 30 Q50 16 56 24 Q70 44 58 92Z" fill="#C7D3DC" {W(3)}/>
<path d="M36 70 L56 62 M36 56 L58 48 M38 42 L56 36" stroke="#6B4A33" stroke-width="2.6" stroke-linecap="round"/>
{face(47, 34, d=5, k=0.7)}
<path d="M56 50 Q70 40 66 30" fill="none" {W(3)}/><path d="M64 32 q6 -6 10 -2" fill="none" {W(2.4)}/>
<path d="M32 70 Q20 70 22 80 Q30 82 34 76Z" fill="#FFE04A" {W(2.2)}/>
{sparkle(108, 30, 5)}
''')

# 5. Фабрика (Егорьевск, столовая с игровой): гречка с котлетой поднимает ложку как штангу
add("cafe-fabrika-egorevsk",
    "горка гречневой каши с румяной котлетой на макушке",
    "стоит на подносе столовой и гордо поднимает над головой большую ложку, как силач штангу",
    "k_canteen", f'''
<path d="M10 100 L118 100 L112 118 L16 118Z" fill="#E8EEF2" {W(3)}/>
<path d="M24 100 Q24 66 64 62 Q104 66 104 100Z" fill="#8A5A36" {W(3)}/>
<g fill="#6B4226"><circle cx="40" cy="88" r="2"/><circle cx="54" cy="80" r="2"/><circle cx="76" cy="84" r="2"/><circle cx="90" cy="92" r="2"/><circle cx="64" cy="94" r="2"/><circle cx="46" cy="96" r="2"/><circle cx="84" cy="76" r="2"/></g>
<ellipse cx="64" cy="60" rx="20" ry="11" fill="#B9672F" {W(3)}/>
<path d="M50 56 Q64 50 78 56" fill="none" stroke="#DB8E4E" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 82, d=10, k=1.0)}
<path d="M28 84 Q14 70 18 40 M100 84 Q114 70 110 40" fill="none" {W(3.4)}/>
<path d="M14 40 L114 40" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M14 40 L114 40" stroke="#D0D6DE" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="18" cy="40" rx="9" ry="12" fill="#D0D6DE" {W(2.6)}/>
''')

# 6. Лама Джони (Долгопрудный): ламаджо жмурится, лимон брызгает сверху
add("cafe-lama-dzhoni-dolgoprudny",
    "тонкая круглая лепёшка-ламаджо с мясной начинкой и зеленью",
    "лежит на дощечке и жмурится от удовольствия, а сверху долька лимона брызгает на неё соком",
    "k_lemon", f'''
<rect x="16" y="84" width="96" height="26" rx="8" fill="#C99460" {W(3)}/>
<path d="M112 92 L124 92 L124 102 L112 102" fill="#C99460" {W(2.6)}/>
<ellipse cx="62" cy="86" rx="46" ry="20" fill="#EDC27A" {W(3)}/>
<ellipse cx="62" cy="84" rx="38" ry="14" fill="#C9502E"/>
<g fill="#7FC24A" {W(1.4)}><path d="M40 80 l6 -3 l1 5Z"/><path d="M78 78 l6 2 l-4 4Z"/><path d="M60 92 l5 -4 l2 5Z"/></g>
<path d="M52 82 q4 3 8 0 M66 82 q4 3 8 0" fill="none" {W(2.4)}/>
<path d="M58 88 Q63 92 68 88" fill="none" {W(2.2)}/>
<ellipse cx="47" cy="88" rx="4" ry="2.2" fill="#FF7FA8" opacity=".7"/><ellipse cx="79" cy="88" rx="4" ry="2.2" fill="#FF7FA8" opacity=".7"/>
<path d="M60 16 Q96 16 100 46 L62 46Z" fill="#FFE04A" {W(3)}/>
<path d="M66 42 Q88 38 94 24 M66 42 L80 22 M66 42 L94 36" fill="none" stroke="#F2C21A" stroke-width="2"/>
<g fill="#FFF3A0" {W(1.6)}><path d="M58 54 q-3 5 0 7 q3 -2 0 -7Z"/><path d="M70 56 q-3 5 0 7 q3 -2 0 -7Z"/><path d="M48 60 q-3 5 0 7 q3 -2 0 -7Z"/><path d="M80 62 q-3 5 0 7 q3 -2 0 -7Z"/></g>
''')

draw_icons.BG.update({
    "k_stage": ("#F3E6FF", "#5B3E9C"),
    "k_dacha": ("#EFFBE3", "#6FAE4E"),
    "k_spicy": ("#FFF0E0", "#E2603A"),
    "k_dill": ("#E3F6FF", "#3E9AB5"),
    "k_cream": ("#FFF8EC", "#C9A06A"),
    "k_skewer": ("#FFEBD0", "#B5562B"),
    "k_cap": ("#E8EEFF", "#6170B8"),
})

# 9. Карло (Таганка): горка спагетти арабьята пыхтит от остроты
add("cafe-karlo-taganka",
    "горка острых спагетти арабьята в красном томатном соусе с тёртым пармезаном",
    "пыхтит от остроты: щёки пылают, язычок высунут, из макушки вырываются облачка пара",
    "k_spicy", f'''
<ellipse cx="64" cy="104" rx="50" ry="13" fill="#fff" {W(3)}/>
<path d="M18 100 Q18 52 64 48 Q110 52 110 100 Q64 110 18 100Z" fill="#F6D27A" {W(3)}/>
<path d="M26 90 Q40 60 60 74 Q80 56 102 88 M30 76 Q50 54 66 64 Q84 50 98 70" fill="none" stroke="#E0A63C" stroke-width="3"/>
<path d="M30 62 Q46 40 64 50 Q84 38 100 62 Q86 70 64 66 Q44 72 30 62Z" fill="#E2382B" {W(2.6)}/>
<g fill="#FFF8D8"><circle cx="50" cy="56" r="1.8"/><circle cx="72" cy="52" r="1.8"/><circle cx="62" cy="60" r="1.8"/><circle cx="84" cy="58" r="1.8"/></g>
{face(64, 82, d=11, k=1.0, mouth=False, blush=False)}
<ellipse cx="46" cy="90" rx="6" ry="3.4" fill="#FF4A4A" opacity=".8"/><ellipse cx="82" cy="90" rx="6" ry="3.4" fill="#FF4A4A" opacity=".8"/>
<path d="M58 90 Q64 94 70 90 L68 98 Q64 102 60 98Z" fill="#FF7A8A" {W(2.2)}/>
<path d="M40 30 Q34 22 42 16 Q48 10 44 4 M64 34 Q58 24 66 18 Q72 12 68 4 M88 30 Q82 22 90 16 Q96 10 92 4" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
''')

# 10. Клешни и Хвосты (Марьино): варёный рак машет клешнями из миски с укропом
add("cafe-kleshni-hvosty-maryino",
    "красный варёный речной рак с длинными усами",
    "сидит в синей миске на подушке из укропа и радостно машет обеими клешнями",
    "k_dill", f'''
<path d="M18 86 Q64 80 110 86 Q106 118 64 120 Q22 118 18 86Z" fill="#3A6FC2" {W(3)}/>
<path d="M24 98 Q64 104 104 98" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 6"/>
<path d="M20 86 l6 -8 l4 7 l6 -9 l4 8 l6 -8 l4 8 l6 -9 l4 9 l6 -8 l4 8 l6 -9 l4 8 l6 -7 l6 8 l6 -7 l2 8" fill="#5DB84A" {W(2)}/>
<path d="M50 88 Q44 54 64 46 Q84 54 78 88Z" fill="#E8432E" {W(3)}/>
<path d="M50 72 Q64 76 78 72 M52 80 Q64 84 76 80" fill="none" stroke="#B22A1C" stroke-width="2.2"/>
<path d="M58 48 Q46 18 30 12 M70 48 Q82 18 98 12" fill="none" {W(2.2)}/>
{face(64, 60, d=6, k=0.8)}
<path d="M50 66 Q34 62 30 44" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M50 66 Q34 62 30 44" fill="none" stroke="#E8432E" stroke-width="4.6" stroke-linecap="round"/>
<path d="M78 66 Q94 62 98 44" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M78 66 Q94 62 98 44" fill="none" stroke="#E8432E" stroke-width="4.6" stroke-linecap="round"/>
<path d="M30 46 Q18 34 24 22 Q30 30 34 26 Q40 36 30 46Z M98 46 Q110 34 104 22 Q98 30 94 26 Q88 36 98 46Z" fill="#E8432E" {W(2.6)}/>
''')

# 11. Гранатовый сад (Марьино): кусочек курицы плывёт на ленте фетучини по сливочному соусу
add("cafe-granatovy-sad-porechnaya",
    "золотистый кусочек курицы в сливочном соусе",
    "плывёт на длинной ленте фетучини, как на волне-серфе, по озеру сливочного соуса в глубокой тарелке",
    "k_cream", f'''
<ellipse cx="64" cy="92" rx="54" ry="26" fill="#FFFFFF" {W(3)}/>
<ellipse cx="64" cy="90" rx="44" ry="18" fill="#FFF1C9" {W(2.4)}/>
<path d="M22 92 Q40 70 58 86 Q76 102 100 76 L104 82 Q78 110 56 94 Q40 80 26 98Z" fill="#F7D978" {W(2.6)}/>
<path d="M44 66 Q42 46 62 44 Q84 44 84 62 Q82 76 62 76 Q46 76 44 66Z" fill="#E09A48" {W(3)}/>
<path d="M50 52 Q60 48 72 50" fill="none" stroke="#F4C07A" stroke-width="3" stroke-linecap="round"/>
{face(64, 62, d=7, k=0.8)}
<path d="M44 62 Q34 54 36 44 M84 60 Q94 52 92 42" fill="none" {W(3)}/>
<g fill="#7FC24A" {W(1.4)}><path d="M30 86 l6 -4 l1 6Z"/><path d="M92 92 l6 -2 l-3 5Z"/></g>
{sparkle(104, 34, 5)}
''')

# 12. Tavaaduree (Люберцы): три молодые картофелины на шампуре делают «волну»
add("cafe-tavaaduree-lyubertsy",
    "три молодые картофелины на гриле с полосками от решётки",
    "нанизаны на один шампур и по очереди поднимают руки, делая «волну», как болельщики на трибуне",
    "k_skewer", f'''
<path d="M6 84 L118 72" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M6 84 L118 72" stroke="#C9CED8" stroke-width="3.4" stroke-linecap="round"/>
<path d="M118 72 l6 -1" stroke="{O}" stroke-width="3"/>
<circle cx="12" cy="83" r="6" fill="#C9CED8" {W(2.6)}/>
<ellipse cx="34" cy="84" rx="15" ry="13" fill="#E9C26A" {W(3)}/>
<ellipse cx="64" cy="70" rx="16" ry="14" fill="#E9C26A" {W(3)}/>
<ellipse cx="94" cy="76" rx="15" ry="13" fill="#E9C26A" {W(3)}/>
<path d="M26 80 l6 -6 M36 92 l8 -8 M56 66 l8 -8 M66 78 l8 -8 M86 74 l8 -8 M96 84 l6 -6" stroke="#8A5A2A" stroke-width="2.6" stroke-linecap="round"/>
{face(34, 86, d=5, k=0.6)}{face(64, 72, d=5.5, k=0.65)}{face(94, 78, d=5, k=0.6)}
<path d="M22 82 Q16 92 20 98 M46 84 Q52 92 50 98" fill="none" {W(2.6)}/>
<path d="M50 64 Q40 50 44 40 M78 64 Q88 50 84 40" fill="none" {W(2.6)}/>
<path d="M82 76 Q76 66 78 60 M106 76 Q112 66 110 60" fill="none" {W(2.6)}/>
<path d="M60 52 q2 -6 6 -2" fill="#5DB84A" {W(1.6)}/>
''')

# 13. Деда хинкали (Люберцы): хинкали-дедушка в кепке читает газету
add("cafe-deda-hinkali-lyubertsy",
    "хинкали-дедушка с пышными седыми усами и в широкой клетчатой кепке",
    "сидит, читает газету через круглые очки, сдвинутые на кончик носа",
    "k_cap", f'''
<path d="M22 112 Q20 72 44 58 Q64 50 84 58 Q108 72 106 112Z" fill="#F7EEDC" {W(3)}/>
<path d="M44 62 Q50 84 48 108 M64 56 L64 108 M84 62 Q78 84 80 108" fill="none" stroke="#D9C7A2" stroke-width="2.4"/>
<path d="M50 56 Q64 40 78 56 Q72 48 64 52 Q56 48 50 56Z" fill="#F7EEDC" {W(2.6)}/>
<path d="M30 52 Q36 26 66 26 Q92 28 98 46 L112 50 Q100 58 30 54Z" fill="#8C6E5A" {W(3)}/>
<path d="M44 32 L48 52 M60 28 L62 52 M76 28 L74 52 M38 42 Q64 38 94 44" fill="none" stroke="#6B5242" stroke-width="2"/>
<circle cx="54" cy="70" r="7" fill="#fff" opacity=".4" {W(2.2)}/><circle cx="74" cy="70" r="7" fill="#fff" opacity=".4" {W(2.2)}/>
<path d="M61 70 h6" {W(2.2)}/>
{eye(54, 70, 0.75)}{eye(74, 70, 0.75)}
<path d="M48 84 Q56 78 64 82 Q72 78 80 84 Q72 90 64 86 Q56 90 48 84Z" fill="#FFFFFF" {W(2.4)}/>
<rect x="30" y="90" width="68" height="34" rx="2" fill="#FFFFFF" {W(2.8)}/>
<path d="M64 90 L64 124 M36 98 h22 M36 104 h22 M36 110 h18 M70 98 h22 M70 104 h22 M70 110 h16" stroke="#9AA3B5" stroke-width="2.2"/>
''')


def main(ids):
    ids = ids or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    have = {l.split(" — ", 1)[0] for l in lines if " — " in l}
    with open(reg, "a", encoding="utf-8") as f:
        for pid in ids:
            if pid not in have:
                h, sc = SUBJ[pid]
                f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))


if __name__ == "__main__":
    main(sys.argv[1:])
