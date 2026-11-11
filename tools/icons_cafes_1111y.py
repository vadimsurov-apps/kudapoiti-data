"""Иконки робота cafes, 2026-11-11 (20 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно,
герои и сцены сверены с subjects.txt (драник-бургер в лавровом венке, креветки на горке из спагетти, буше на ложке-качелях,
горшочек чанахи под виноградной лозой, пицца ветчина-грибы в лифте, ролл на экваторе глобуса, сказочный ларец — таких нет).
Запуск: python3 tools/icons_cafes_1111y.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "y_laurel": ("#FFF3D6", "#E0A23A"),
    "y_tomato": ("#FFE1DA", "#E0573F"),
    "y_mint": ("#E3FFF4", "#62C9A0"),
    "y_vine": ("#F1E6FF", "#7E5BB5"),
    "y_steel": ("#EAF0F7", "#7C93B0"),
    "y_ocean": ("#D6F1FF", "#2F86C9"),
    "y_fairy": ("#FFE6F6", "#C4499A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Легенда (Орехово-Зуево): драник-бургер из меню — в лавровом венке легенды
add("cafe-legenda-orekhovo-zuevo",
    "драник-бургер — две румяные картофельные оладьи вместо булочек, а между ними котлета, сыр и салат",
    "надел золотой лавровый венок, как настоящая легенда, и гордо подмигивает",
    "y_laurel", f'''
<ellipse cx="64" cy="106" rx="44" ry="9" fill="#FFFFFF" {W(3)}/>
<path d="M24 92 Q24 82 64 82 Q104 82 104 92 Q104 102 64 102 Q24 102 24 92Z" fill="#E3A548" {W(3)}/>
<path d="M30 92 l6 3 M46 96 l6 -2 M70 96 l8 2 M88 93 l6 -3" stroke="#B5742A" stroke-width="2.4" stroke-linecap="round"/>
<path d="M22 80 Q30 74 38 80 Q46 86 54 79 Q62 73 70 80 Q78 86 86 79 Q94 73 106 80 L104 86 L24 86Z" fill="#7BC94A" {W(2.6)}/>
<rect x="26" y="70" width="76" height="13" rx="6" fill="#7A3E22" {W(3)}/>
<path d="M30 70 L98 70 L92 78 L84 72 L74 79 L64 72 L54 79 L44 72 L36 78Z" fill="#FFD23F" {W(2.4)}/>
<path d="M24 64 Q24 40 64 38 Q104 40 104 64 Q104 70 64 70 Q24 70 24 64Z" fill="#E8AE52" {W(3)}/>
<path d="M34 56 l7 -3 M50 48 l6 2 M74 47 l7 -1 M88 54 l6 4 M60 60 l6 0" stroke="#B5742A" stroke-width="2.4" stroke-linecap="round"/>
{eye(50, 56, 0.9)}<path d="M74 56 q4 -3 8 0" fill="none" {W(2.6)}/>
<path d="M58 62 Q64 67 70 62" fill="none" {W(2.4)}/>
<ellipse cx="42" cy="63" rx="4.5" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="88" cy="63" rx="4.5" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<g fill="#F2C230" {W(2)}>
<path d="M30 38 Q24 30 30 24 Q36 30 30 38Z"/><path d="M38 30 Q34 20 42 16 Q46 24 38 30Z"/><path d="M50 24 Q48 14 58 12 Q58 20 50 24Z"/>
<path d="M98 38 Q104 30 98 24 Q92 30 98 38Z"/><path d="M90 30 Q94 20 86 16 Q82 24 90 30Z"/><path d="M78 24 Q80 14 70 12 Q70 20 78 24Z"/>
</g>
<circle cx="64" cy="18" r="4" fill="#E2554A" {W(2)}/>
{sparkle(16, 52, 5)}{sparkle(112, 50, 4)}
''')

# 2. Траттория la Famiglia (Реутов): паста Гамберетти — креветки катаются по спагетти, как с горки
add("cafe-trattoria-la-famiglia-reutov",
    "гнездо спагетти в томатном соусе в глубокой белой тарелке",
    "три розовые креветки-малыша катаются по вьющимся макаронинам, как с горки-серпантина, а спагетти улыбается",
    "y_tomato", f'''
<ellipse cx="64" cy="98" rx="52" ry="16" fill="#FFFFFF" {W(3)}/>
<ellipse cx="64" cy="94" rx="40" ry="10" fill="#F4F1EC"/>
<path d="M28 90 Q26 60 64 56 Q102 60 100 90 Q86 100 64 100 Q42 100 28 90Z" fill="#F7D774" {W(3)}/>
<path d="M34 86 Q40 66 64 64 Q90 66 94 86 M40 90 Q50 72 72 74 Q88 78 88 92 M48 94 Q56 82 70 84" fill="none" stroke="#E8BC48" stroke-width="2.6" stroke-linecap="round"/>
<path d="M44 70 Q52 62 64 66 Q76 60 84 70 Q76 78 64 74 Q52 80 44 70Z" fill="#D9402E" {W(2.4)}/>
{face(64, 84, d=8, k=0.85)}
<path d="M64 56 Q60 40 72 30 Q84 22 92 30" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M64 56 Q60 40 72 30 Q84 22 92 30" fill="none" stroke="#F7D774" stroke-width="4" stroke-linecap="round"/>
<path d="M58 58 Q44 44 30 46 Q20 48 18 58" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M58 58 Q44 44 30 46 Q20 48 18 58" fill="none" stroke="#F7D774" stroke-width="4" stroke-linecap="round"/>
<g {W(2)}>
<path d="M84 22 Q94 16 100 24 Q100 32 90 32 Q94 26 86 26Z" fill="#FF8C7A"/>
<path d="M66 38 Q74 30 82 36 Q82 44 72 44 Q76 38 68 40Z" fill="#FF8C7A"/>
<path d="M22 42 Q30 36 36 42 Q36 50 28 50 Q32 44 24 46Z" fill="#FF8C7A"/>
</g>
<circle cx="94" cy="24" r="1.4" fill="{O}"/><circle cx="76" cy="37" r="1.4" fill="{O}"/><circle cx="30" cy="43" r="1.4" fill="{O}"/>
<path d="M100 22 l6 -6 M82 34 l6 -6 M36 40 l5 -6" stroke="{O}" stroke-width="1.6"/>
<path d="M88 58 l4 6 M100 52 l2 6" stroke="#4FA34A" stroke-width="3" stroke-linecap="round"/>
''')

# 3. Алекс Кейк (Орехово-Зуево): пирожное буше качается на чайной ложке-качелях
add("cafe-aleks-keik-orekhovo-zuevo",
    "пирожное буше — две круглые бисквитные половинки с кремом, облитые шоколадом с белыми полосками",
    "качается на серебряной чайной ложечке, как на качелях-балансире, напротив сидит пухлая клубничка-подружка",
    "y_mint", f'''
<path d="M54 106 L64 92 L74 106Z" fill="#8FD3B8" {W(3)}/>
<path d="M12 84 L116 66" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M12 84 L116 66" stroke="#D7DEE6" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="108" cy="66" rx="12" ry="7" fill="#D7DEE6" {W(3)} transform="rotate(-10 108 66)"/>
<g transform="rotate(-10 44 66)">
<ellipse cx="44" cy="74" rx="26" ry="10" fill="#E9C48A" {W(3)}/>
<rect x="18" y="62" width="52" height="8" fill="#FFF7EA" {W(2.6)}/>
<path d="M18 62 Q18 38 44 36 Q70 38 70 62Z" fill="#5A2E1E" {W(3)}/>
<path d="M28 50 Q44 42 60 50 M26 58 Q44 50 64 58" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
{face(44, 52, d=8, k=0.8)}
</g>
<g transform="rotate(-10 98 52)">
<path d="M88 44 Q86 64 98 66 Q110 64 108 44 Q98 38 88 44Z" fill="#F0485A" {W(2.8)}/>
<path d="M88 44 Q92 36 98 40 Q104 34 108 44" fill="#5DBB46" {W(2.4)}/>
<g fill="#FFE7A0"><circle cx="94" cy="54" r="1"/><circle cx="102" cy="56" r="1"/><circle cx="98" cy="60" r="1"/></g>
{eye(94, 48, 0.55)}{eye(102, 48, 0.55)}
</g>
{sparkle(24, 26, 5)}{sparkle(76, 22, 3)}
''')

# 4. Твиши (Пушкино): горшочек чанахи под виноградной лозой «твиши»
add("cafe-tvishi-pushkino",
    "грузинская чанахи — пузатый глиняный горшочек с рагу из баклажанов и помидоров, накрытый круглой лепёшкой",
    "отдыхает в тени виноградной лозы, сверху свисает гроздь светлого винограда и одна виноградинка падает ему на лепёшку",
    "y_vine", f'''
<path d="M0 20 Q40 30 64 16 Q90 4 128 18" fill="none" stroke="#6B4A2A" stroke-width="5"/>
<g fill="#7CBF52" {W(2)}>
<path d="M22 26 Q12 18 18 10 Q26 14 30 8 Q36 18 22 26Z"/><path d="M100 14 Q94 4 104 0 Q108 8 116 6 Q116 18 100 14Z"/>
</g>
<path d="M64 18 L64 26" stroke="#6B4A2A" stroke-width="2.4"/>
<g fill="#D9E87A" {W(1.8)}>
<circle cx="58" cy="30" r="5"/><circle cx="70" cy="30" r="5"/><circle cx="64" cy="38" r="5"/><circle cx="54" cy="40" r="4.5"/><circle cx="74" cy="40" r="4.5"/><circle cx="64" cy="48" r="4.5"/>
</g>
<circle cx="80" cy="56" r="4" fill="#D9E87A" {W(1.8)}/>
<path d="M80 48 v-4" stroke="#fff" stroke-width="1.6"/>
<ellipse cx="64" cy="112" rx="36" ry="6" fill="#4A2F6E" opacity=".35"/>
<path d="M34 76 Q28 110 64 112 Q100 110 94 76Z" fill="#C46A3C" {W(3)}/>
<path d="M36 90 Q64 96 92 90" fill="none" stroke="#E8A070" stroke-width="2.4"/>
<path d="M40 100 l4 2 M84 100 l-4 2" stroke="#8E4424" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="64" cy="74" rx="34" ry="9" fill="#9E5A32" {W(3)}/>
<path d="M30 70 Q30 60 64 60 Q98 60 98 70 Q98 78 64 78 Q30 78 30 70Z" fill="#E7B66A" {W(3)}/>
<path d="M44 66 l5 2 M60 64 l6 1 M78 66 l5 -1" stroke="#B9813E" stroke-width="2.2" stroke-linecap="round"/>
<path d="M36 80 Q40 74 46 80 M82 80 Q88 74 92 80" fill="#6B3A8A" {W(2)}/>
<path d="M90 80 q4 -6 8 -2" fill="#E2554A" {W(2)}/>
{face(64, 92, d=9, k=0.9)}
''')

# 5. IL Патио (Чехов): пицца ветчина-грибы едет в лифте на 4 этаж
add("cafe-ilpatio-chekhov",
    "круглая пицца с ветчиной и шампиньонами",
    "едет в стеклянном лифте на четвёртый этаж — на табло горит цифра «4», а пицца радостно машет рукой",
    "y_steel", f'''
<rect x="26" y="14" width="76" height="104" rx="6" fill="#F4F8FC" {W(3)}/>
<rect x="34" y="34" width="60" height="78" rx="3" fill="#CFE6F7" {W(2.6)}/>
<path d="M64 34 L64 112" stroke="{O}" stroke-width="2"/>
<rect x="48" y="18" width="32" height="13" rx="4" fill="#2E2A3A" {W(2.4)}/>
<path d="M60 22 L56 28 L64 28 M61 22 L61 30" fill="none" stroke="#FFC23D" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M72 28 L72 22 L69 25 M72 22 L75 25" fill="none" stroke="#FFC23D" stroke-width="2" stroke-linecap="round"/>
<circle cx="64" cy="76" r="27" fill="#E8A84E" {W(3)}/>
<circle cx="64" cy="76" r="21" fill="#F6D266"/>
<g fill="#F49AA0" {W(1.8)}><circle cx="50" cy="66" r="4.5"/><circle cx="78" cy="88" r="4.5"/><circle cx="52" cy="90" r="4"/></g>
<g {W(1.8)}><path d="M72 62 q4 -5 8 0 v3 h-8Z" fill="#F2EAD8"/><path d="M44 78 q4 -5 8 0 v3 h-8Z" fill="#F2EAD8"/><path d="M80 74 q3 -4 7 0 v3 h-7Z" fill="#F2EAD8"/></g>
{face(64, 74, d=8, k=0.85)}
<path d="M90 70 Q100 60 98 50" fill="none" {W(3)}/>
<circle cx="98" cy="48" r="4" fill="#E8A84E" {W(2.2)}/>
<path d="M102 40 q4 2 4 6 M106 36 q6 3 6 10" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
''')

# 6. Вокруг Света (Можайск): ролл с лососем шагает по экватору глобуса с узелком
add("cafe-vokrug-sveta-mozhaisk",
    "ролл с лососем в полоске нори",
    "путешествует вокруг света — шагает по экватору маленькой планеты с узелком на палочках для еды через плечо",
    "y_ocean", f'''
<circle cx="64" cy="112" r="46" fill="#4FB0E8" {W(3)}/>
<path d="M30 92 Q40 84 52 90 Q58 100 46 104 Q34 106 30 92Z M78 84 Q92 80 98 92 Q94 102 82 98 Q74 92 78 84Z" fill="#7CCB62" {W(2.4)}/>
<path d="M18 112 Q64 96 110 112" fill="none" stroke="#FFE07A" stroke-width="3" stroke-dasharray="5 4"/>
<rect x="42" y="38" width="40" height="46" rx="14" fill="#2B3A33" {W(3)}/>
<ellipse cx="62" cy="40" rx="20" ry="9" fill="#FFFFFF" {W(3)}/>
<ellipse cx="62" cy="40" rx="10" ry="4.5" fill="#FF8F6B" {W(2)}/>
<path d="M58 39 l3 1.5 M63 38 l3 1.5" stroke="#FFD2C2" stroke-width="1.4"/>
<rect x="42" y="56" width="40" height="4" fill="#3E5247"/>
{face(62, 66, d=8, k=0.85)}
<path d="M50 84 L46 96 M74 84 L80 94" fill="none" {W(3.4)}/>
<path d="M82 52 L104 32 M84 54 L106 34" stroke="#C98A4A" stroke-width="3" stroke-linecap="round"/>
<path d="M82 52 L104 32 M84 54 L106 34" stroke="{O}" stroke-width="1" stroke-linecap="round" opacity=".6"/>
<path d="M98 30 Q104 20 112 26 Q116 36 108 40 Q100 40 98 30Z" fill="#E2554A" {W(2.4)}/>
<g fill="#fff"><circle cx="104" cy="30" r="1.4"/><circle cx="110" cy="34" r="1.4"/><circle cx="106" cy="36" r="1.2"/></g>
<path d="M78 52 Q84 50 84 54" fill="none" {W(2.6)}/>
{sparkle(20, 30, 5)}{sparkle(34, 16, 3)}
''')

# 7. Ларец сказок (Можайск): сказочный ларец открывается, из него выпрыгивает пряничная звёздочка
add("cafe-larets-skazok-mozhaisk",
    "расписной деревянный ларец с золотыми уголками и мордашкой на передней стенке",
    "приоткрыл крышку, а оттуда в золотом сиянии выпрыгивает пряничная звёздочка в глазури",
    "y_fairy", f'''
<path d="M64 60 L34 14 L94 14Z" fill="#FFE98A" opacity=".55"/>
<rect x="24" y="66" width="80" height="46" rx="5" fill="#C0392B" {W(3)}/>
<path d="M24 66 L104 66 L104 74 L24 74Z" fill="#9E2B22"/>
<path d="M30 60 Q30 46 64 44 Q98 46 98 60" fill="#C0392B" {W(3)} transform="rotate(-16 98 60)"/>
<g fill="#F2C230" {W(2)}>
<path d="M24 100 h10 v12 h-10Z"/><path d="M94 100 h10 v12 h-10Z"/><path d="M24 66 h10 v8 h-10Z"/><path d="M94 66 h10 v8 h-10Z"/>
</g>
<path d="M40 84 q6 -6 12 0 q-6 6 -12 0Z M76 84 q6 -6 12 0 q-6 6 -12 0Z" fill="#FFD84A" {W(1.6)}/>
<circle cx="64" cy="104" r="4" fill="#F2C230" {W(2)}/>
{face(64, 88, d=9, k=0.85)}
<path d="M64 20 L69 32 L82 33 L72 41 L76 54 L64 47 L52 54 L56 41 L46 33 L59 32Z" fill="#D9934A" {W(3)}/>
<path d="M60 30 l2 3 M66 34 l3 -1 M58 42 l3 1 M68 44 l2 -2" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
{eye(60, 38, 0.6)}{eye(68, 38, 0.6)}
{sparkle(30, 34, 5, "#FFF6B0")}{sparkle(100, 30, 4, "#FFF6B0")}{sparkle(94, 50, 3)}
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
