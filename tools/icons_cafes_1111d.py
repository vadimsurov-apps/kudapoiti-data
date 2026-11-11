"""Иконки робота cafes, 2026-11-11 (05 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована отдельно.
Сверено с каталогом (листы cafe-*) и subjects.txt: у «Тануки» уже заняты тануки-официант, дораяки-фонарик, гёдза в лабиринте,
удон-скакалка, футомаки-колесо, омурайсу, бенто-автобус, калифорния в лодке, тофу в мисо, гёдза у соуса, наруто на палочках;
у «Додо» — десятки кусков пиццы. Новые: гункан под портовым краном, маття с венчиком, додстер на финише стадиона, налисник-труба с вишнями-нотами,
грибы-купальщики в кеци, пеламуши перед выступлением, колбаска загорает на мангале, лаваш-подзорная труба на причале,
ягодки брусники на веточке-качелях.
Запуск: python3 tools/icons_cafes_1111d.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k21_port": ("#E6F4FF", "#5B8FC9"),
    "k21_matcha": ("#FFF8EC", "#C9A86B"),
    "k21_arena": ("#E9F7EC", "#3E9A5A"),
    "k21_music": ("#FFF0F3", "#D9637A"),
    "k21_clay": ("#FFF3E4", "#B9733F"),
    "k21_stage": ("#3A2E5C", "#1C1736"),
    "k21_grill": ("#FFF7D6", "#E39A2B"),
    "k21_river": ("#EAF7FF", "#6FB0E0"),
    "k21_forest": ("#F1FBEA", "#6FA85A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Тануки (Симоновский Вал, у Южного порта): гункан с икрой, портовый кран опускает ему на макушку икринку
add("cafe-tanuki-simonovsky-15",
    "ролл-гункан в полоске нори с горкой оранжевой икры",
    "стоит на причале речного порта, а жёлтый портовый кран бережно опускает ему на макушку ещё одну икринку", "k21_port", f'''
<path d="M0 104 Q32 98 64 104 T128 104 V128 H0Z" fill="#3E7DC4"/>
<path d="M8 112 Q20 108 32 112 M70 116 Q82 112 94 116" fill="none" stroke="#BFE2FF" stroke-width="2.4" stroke-linecap="round"/>
<rect x="6" y="94" width="116" height="10" rx="2" fill="#A57A55" {W(2.4)}/>
<path d="M98 94 V22 M98 22 H40 M98 30 L84 22 M98 40 L84 22" fill="none" stroke="#F2B630" stroke-width="5" stroke-linecap="round"/>
<path d="M98 94 V22 H40" fill="none" {W(2)}/>
<rect x="90" y="18" width="16" height="12" rx="2" fill="#F2B630" {W(2.2)}/>
<path d="M48 22 V40" stroke="{O}" stroke-width="1.8"/>
<circle cx="48" cy="44" r="4.2" fill="#FF8A2A" {W(2)}/><circle cx="46.6" cy="42.6" r="1.2" fill="#fff"/>
<rect x="24" y="58" width="48" height="36" rx="8" fill="#2F3B37" {W(2.6)}/>
<rect x="24" y="64" width="48" height="10" fill="#3E4C47"/>
<path d="M26 60 Q34 46 48 50 Q62 46 70 60Z" fill="#FF8A2A" {W(2.4)}/>
<g fill="#FFB25A"><circle cx="36" cy="55" r="2.6"/><circle cx="44" cy="52" r="2.6"/><circle cx="52" cy="53" r="2.6"/><circle cx="60" cy="56" r="2.6"/><circle cx="48" cy="57" r="2.4"/></g>
<rect x="28" y="76" width="40" height="14" rx="5" fill="#F7F5EE"/>
{face(48, 80, d=7, k=0.75)}
{sparkle(20, 30, 4)}{sparkle(70, 40, 3)}
''')

# 2. Тануки (Привольная, Жулебино): пиала маття, венчик-часэн взбивает пенку, пиала хохочет от щекотки
add("cafe-tanuki-privolnaya-65",
    "зелёный чай маття в керамической пиале",
    "бамбуковый венчик-часэн с мордашкой взбивает ему пенку, а пиала хохочет от щекотки, зажмурившись", "k21_matcha", f'''
<ellipse cx="60" cy="108" rx="44" ry="8" fill="#B88F57" opacity=".45"/>
<path d="M18 66 Q20 108 60 108 Q100 108 102 66Z" fill="#5E7F9E" {W(2.8)}/>
<path d="M22 84 Q60 94 98 84" fill="none" stroke="#86A6C2" stroke-width="5"/>
<ellipse cx="60" cy="66" rx="42" ry="10" fill="#8CC152" {W(2.6)}/>
<ellipse cx="56" cy="65" rx="22" ry="5" fill="#B5DC7E"/>
<g fill="#D9F0B8"><circle cx="44" cy="64" r="2"/><circle cx="70" cy="66" r="2.2"/><circle cx="60" cy="62" r="1.6"/></g>
<path d="M44 86 Q48 82 52 86" fill="none" {W(2.6)}/><path d="M66 86 Q70 82 74 86" fill="none" {W(2.6)}/>
<path d="M53 94 Q59 102 65 94Z" fill="#E5533D" {W(2.2)}/>
<ellipse cx="40" cy="94" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/><ellipse cx="78" cy="94" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/>
<g transform="rotate(24 92 40)">
<rect x="86" y="8" width="12" height="28" rx="5" fill="#E8D29A" {W(2.4)}/>
<path d="M84 36 Q82 52 86 62 M88 36 Q88 52 90 63 M92 36 Q92 52 93 63 M96 36 Q96 52 96 63 M100 36 Q102 52 99 62" fill="none" stroke="#C9A55E" stroke-width="2"/>
<path d="M84 36 Q92 70 100 36" fill="none" {W(2.2)}/>
{face(92, 22, d=3.4, k=0.5)}
</g>
<path d="M104 70 l5 -3 M106 78 l6 0 M14 58 l-5 -3" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>
''')

# 3. Додо (Верхняя Масловка, у стадиона «Динамо»): додстер рвёт финишную ленточку на беговой дорожке
add("cafe-dodo-verkhnyaya-maslovka-10",
    "ролл-додстер в бумажной обёртке с курицей и салатом",
    "рвёт грудью финишную ленточку на красной беговой дорожке стадиона, вскинув руки", "k21_arena", f'''
<path d="M0 92 L128 80 V128 H0Z" fill="#D9573E"/>
<path d="M0 104 L128 94 M0 118 L128 110" stroke="#fff" stroke-width="2.4" opacity=".85"/>
<path d="M4 66 L4 98 M124 56 L124 90" stroke="#fff" stroke-width="4"/>
<path d="M4 70 Q34 74 52 64 M76 62 Q100 58 124 60" fill="none" stroke="#F6E04A" stroke-width="4.5" stroke-linecap="round"/>
<path d="M52 64 L48 72 M76 62 L80 70" stroke="#F6E04A" stroke-width="4" stroke-linecap="round"/>
<g transform="rotate(-12 64 60)">
<path d="M48 34 Q64 24 80 34 L78 92 Q64 98 50 92Z" fill="#F4E3C0" {W(2.6)}/>
<path d="M48 34 Q56 26 64 30 Q72 26 80 34 Q72 40 64 36 Q56 40 48 34Z" fill="#7CCB4E" {W(2)}/>
<circle cx="57" cy="32" r="3" fill="#E89A3C"/><circle cx="70" cy="31" r="3.2" fill="#E89A3C"/>
<path d="M49 60 L79 60 L78 92 Q64 98 50 92Z" fill="#E7442E" {W(2.4)}/>
<path d="M56 74 h16" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{face(64, 48, d=6.5, k=0.75)}
</g>
<path d="M50 52 L34 28 M78 46 L96 24" fill="none" {W(3.4)}/>
<circle cx="33" cy="26" r="3.6" fill="#F4E3C0" {W(2)}/><circle cx="97" cy="22" r="3.6" fill="#F4E3C0" {W(2)}/>
<path d="M30 92 l-6 4 M40 96 l-8 2" stroke="{O}" stroke-width="2" stroke-linecap="round" opacity=".6"/>
{sparkle(18, 22, 5)}{sparkle(112, 34, 4)}
''')

# 4. Корчма (Намёткина), украинская кухня: блинчик-налисник трубочкой дудит, вылетают вишенки-ноты
add("cafe-korchma-nametkina-13",
    "блинчик-налисник, свёрнутый трубочкой, с вишнёвой начинкой",
    "дудит в себя, как в трубу, а из раструба вылетают вишенки-ноты", "k21_music", f'''
<ellipse cx="54" cy="106" rx="38" ry="7" fill="#C24B60" opacity=".3"/>
<g transform="rotate(-18 56 74)">
<rect x="16" y="58" width="70" height="30" rx="15" fill="#F6D58A" {W(2.6)}/>
<path d="M30 60 Q34 74 30 86 M46 59 Q50 74 46 87 M62 59 Q66 74 62 87" fill="none" stroke="#E2B65E" stroke-width="2.4"/>
<ellipse cx="86" cy="73" rx="10" ry="16" fill="#F6D58A" {W(2.6)}/>
<ellipse cx="86" cy="73" rx="6" ry="11" fill="#9C1F3C" {W(2)}/>
<circle cx="84" cy="69" r="2" fill="#D9405E"/>
<ellipse cx="17" cy="73" rx="5" ry="10" fill="#E9B95A" {W(2.2)}/>
{face(44, 70, d=7, k=0.8)}
</g>
<g {W(2)}>
<circle cx="100" cy="38" r="6" fill="#C8203E"/><path d="M104 34 Q108 22 116 20" fill="none"/>
<circle cx="112" cy="58" r="5" fill="#C8203E"/><path d="M115 55 Q118 46 124 44" fill="none"/>
<circle cx="88" cy="22" r="4.5" fill="#C8203E"/><path d="M91 19 Q93 12 99 10" fill="none"/>
</g>
<path d="M98 24 l3 3 M118 30 l4 -1" stroke="{O}" stroke-width="2" stroke-linecap="round"/>
{sparkle(24, 30, 5)}
''')

# 5. Sаперавия (грузинская): глиняная сковородка-кеци, грибочки купаются в расплавленном сыре
add("cafe-saperaviya-kozhukhovskaya-9",
    "глиняная сковородка-кеци с запечёнными шампиньонами в сыре",
    "грибочки нежатся в пузырьках расплавленного сулугуни, как в джакузи, раскинув ручки по краю", "k21_clay", f'''
<ellipse cx="64" cy="102" rx="50" ry="9" fill="#7A4524" opacity=".3"/>
<path d="M14 70 Q16 98 64 98 Q112 98 114 70Z" fill="#B85A2E" {W(2.8)}/>
<path d="M114 72 L124 70 L124 80 L113 82" fill="#B85A2E" {W(2.4)}/>
<ellipse cx="64" cy="70" rx="50" ry="13" fill="#F7E08A" {W(2.6)}/>
<g fill="#FFF3B8"><circle cx="30" cy="70" r="4"/><circle cx="98" cy="68" r="3.5"/><circle cx="62" cy="76" r="3"/><circle cx="80" cy="76" r="2.4"/></g>
<path d="M30 66 Q30 50 44 50 Q58 50 58 66Z" fill="#EDE2D0" {W(2.4)}/>
<rect x="38" y="64" width="12" height="8" fill="#F4EDE2" {W(2)}/>
{face(44, 58, d=5, k=0.6)}
<path d="M70 64 Q70 46 86 46 Q102 46 102 64Z" fill="#E6D8C2" {W(2.4)}/>
<rect x="80" y="62" width="12" height="9" fill="#F4EDE2" {W(2)}/>
<path d="M80 54 Q83 51 86 54 M88 54 Q91 51 94 54" fill="none" {W(2.2)}/>
<path d="M83 58 Q87 62 91 58" fill="none" {W(2.2)}/>
<path d="M30 64 Q22 62 18 66 M102 62 Q110 60 112 64" fill="none" {W(2.6)}/>
<path d="M40 36 q4 -6 0 -12 M64 34 q4 -6 0 -12 M88 34 q4 -6 0 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".85"/>
''')

# 6. Швили (Профсоюзная): виноградное желе пеламуши волнуется перед выступлением на сцене
add("cafe-shvili-profsoyuznaya-61",
    "грузинское желе пеламуши — бордовый кубик с грецкими орешками",
    "стоит в луче прожектора на детской сцене у микрофона и дрожит от волнения перед выступлением", "k21_stage", f'''
<path d="M40 0 L14 128 L114 128 L88 0Z" fill="#FFF3B0" opacity=".28"/>
<path d="M0 100 H128 V128 H0Z" fill="#8B5A3C"/>
<path d="M0 100 H128" {W(2.6)}/>
<path d="M8 0 Q20 40 6 96 L0 96 V0Z M120 0 Q108 40 122 96 L128 96 V0Z" fill="#C2334D" {W(2.4)}/>
<ellipse cx="58" cy="100" rx="30" ry="5" fill="#E6E0F0" {W(2.2)}/>
<path d="M34 98 L36 56 Q58 48 80 56 L82 98 Q58 104 34 98Z" fill="#8E1E46" {W(2.6)}/>
<path d="M36 56 Q58 64 80 56" fill="none" stroke="#B83A66" stroke-width="3"/>
<g fill="#D9A15E" {W(1.6)}><ellipse cx="46" cy="80" rx="4" ry="3"/><ellipse cx="68" cy="86" rx="4" ry="3"/><ellipse cx="60" cy="72" rx="3.5" ry="2.6"/></g>
{eye(50, 66, 0.75)}{eye(66, 66, 0.75)}
<path d="M53 75 q2.5 -2 5 0 q2.5 2 5 0" fill="none" {W(2.2)}/>
<path d="M28 60 l-5 -2 M28 70 l-6 0 M88 60 l5 -2 M88 70 l6 0" stroke="#FFE07A" stroke-width="2.4" stroke-linecap="round"/>
<path d="M98 100 V64" {W(3)}/><rect x="93" y="50" width="10" height="16" rx="5" fill="#9AA3B5" {W(2.4)}/>
<path d="M90 100 h16" {W(3)}/>
{sparkle(30, 22, 4, "#FFE07A")}{sparkle(96, 30, 3.5, "#FFE07A")}
''')

# 7. Колбасофф (Симферопольский б-р): колбаска-гриль загорает на решётке мангала в тёмных очках
add("cafe-kolbasoff-simferopolsky-22",
    "колбаска-гриль с поджаристыми полосками",
    "загорает на решётке мангала, как на пляжном лежаке, в тёмных очках, подложив руки под голову", "k21_grill", f'''
<circle cx="104" cy="24" r="12" fill="#FFD24A"/>
<path d="M104 6 v-4 M120 24 h4 M116 12 l3 -3 M92 12 l-3 -3" stroke="#FFD24A" stroke-width="3" stroke-linecap="round"/>
<path d="M18 86 L110 86 L100 112 L28 112Z" fill="#4A4F5C" {W(2.6)}/>
<path d="M30 112 l-6 12 M98 112 l6 12" {W(3)}/>
<path d="M42 96 h44" stroke="#E2572E" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<path d="M14 84 H114" stroke="#9AA0AC" stroke-width="4"/>
<path d="M24 80 V88 M40 80 V88 M56 80 V88 M72 80 V88 M88 80 V88 M104 80 V88" stroke="#9AA0AC" stroke-width="2.4"/>
<rect x="22" y="62" width="84" height="20" rx="10" fill="#C9623A" {W(2.6)}/>
<path d="M38 64 l-4 16 M54 64 l-4 16 M70 64 l-4 16 M86 64 l-4 16" stroke="#7A3218" stroke-width="3"/>
<path d="M30 64 Q22 52 34 50 Q38 56 36 64" fill="#C9623A" {W(2.2)}/>
<rect x="74" y="64" width="9" height="6" rx="2" fill="#2B2B3A"/><rect x="86" y="64" width="9" height="6" rx="2" fill="#2B2B3A"/>
<path d="M83 66 h3" {W(2)}/>
<path d="M80 75 Q85 79 90 75" fill="none" {W(2.2)}/>
<path d="M40 40 q4 -6 0 -12 M58 44 q4 -6 0 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
''')

# 8. Хинкали-Gали! (ул. Речников, у Москвы-реки): лаваш свернулся подзорной трубой и смотрит с причала на кораблик
add("cafe-hinkali-gali-rechnikov-32",
    "тонкий лаваш, свёрнутый подзорной трубой",
    "стоит на деревянном причале и разглядывает в себя-трубу белый речной кораблик на реке", "k21_river", f'''
<path d="M0 86 Q32 80 64 86 T128 86 V128 H0Z" fill="#4E92D0"/>
<path d="M60 96 q8 -4 16 0 M92 106 q8 -4 16 0" fill="none" stroke="#CDE9FF" stroke-width="2.4" stroke-linecap="round"/>
<path d="M84 76 L118 76 L112 86 L90 86Z" fill="#fff" {W(2.2)}/>
<rect x="92" y="66" width="18" height="10" rx="2" fill="#fff" {W(2)}/>
<path d="M100 66 V58" {W(2)}/><path d="M100 58 l8 3 l-8 3" fill="#E5533D"/>
<rect x="0" y="96" width="66" height="10" fill="#A57A55" {W(2.4)}/>
<path d="M12 106 v22 M50 106 v22" stroke="#7A5638" stroke-width="5"/>
<path d="M26 96 L22 70 Q30 62 40 70 L38 96Z" fill="#F1DDB0" {W(2.4)}/>
<path d="M24 82 Q31 86 39 82" fill="none" stroke="#D9BC80" stroke-width="2"/>
<g fill="#C98E4C"><circle cx="28" cy="90" r="1.6"/><circle cx="34" cy="76" r="1.4"/></g>
{face(30, 74, d=4, k=0.55)}
<g transform="rotate(-14 52 60)">
<rect x="38" y="54" width="34" height="11" rx="5" fill="#F1DDB0" {W(2.4)}/>
<ellipse cx="73" cy="59.5" rx="4" ry="7" fill="#E9CF98" {W(2.2)}/>
<path d="M48 55 Q50 60 48 65 M58 55 Q60 60 58 65" fill="none" stroke="#D9BC80" stroke-width="2"/>
</g>
<path d="M40 74 Q42 64 42 62" fill="none" {W(2.6)}/>
{sparkle(18, 24, 5)}{sparkle(60, 30, 3.5)}
''')

# 9. Брусника (Украинский бульвар): три ягодки брусники-сестрички качаются на веточке, как на качелях
add("cafe-brusnika-ukrainsky-6",
    "три красные ягодки брусники-сестрички",
    "качаются на изогнутой веточке с листиками, как на качелях, и болтают ножками", "k21_forest", f'''
<path d="M8 40 Q60 74 120 34" fill="none" stroke="#6B4A2E" stroke-width="5" stroke-linecap="round"/>
<path d="M8 40 Q60 74 120 34" fill="none" {W(1.6)}/>
<g {W(2)}>
<path d="M22 46 Q14 32 26 28 Q30 40 22 46Z" fill="#4F9A43"/>
<path d="M98 46 Q108 34 116 42 Q106 52 98 46Z" fill="#4F9A43"/>
<path d="M64 58 Q60 44 72 42 Q74 54 64 58Z" fill="#5FAE4E"/>
</g>
<path d="M36 52 V62 M64 57 V68 M92 50 V60" {W(2.2)}/>
<circle cx="36" cy="74" r="13" fill="#D2263A" {W(2.6)}/>
<circle cx="64" cy="82" r="15" fill="#E0303F" {W(2.6)}/>
<circle cx="92" cy="72" r="12" fill="#C81F35" {W(2.6)}/>
<path d="M33 62 l3 3 l3 -3 M60 68 l4 3 l4 -3 M89 61 l3 3 l3 -3" fill="none" stroke="#7A1424" stroke-width="2"/>
<circle cx="31" cy="69" r="2.4" fill="#fff" opacity=".7"/><circle cx="58" cy="76" r="2.8" fill="#fff" opacity=".7"/><circle cx="88" cy="67" r="2.2" fill="#fff" opacity=".7"/>
{face(36, 75, d=4.5, k=0.55)}{face(64, 84, d=5.5, k=0.65)}{face(92, 73, d=4.2, k=0.5)}
<path d="M30 86 l-3 8 M42 86 l3 8 M58 96 l-3 9 M70 96 l3 9 M88 84 l-3 8 M96 84 l3 8" {W(2.6)}/>
{sparkle(18, 100, 5)}{sparkle(110, 96, 4)}
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
