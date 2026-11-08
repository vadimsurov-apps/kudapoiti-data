"""Иконки робота cafes, 2026-11-08 (22–24 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по кухне/названию, своя сцена, своя компоновка и палитра фона). Сверено с листами
icons-catalog и icons-src/subjects.txt. Запуск: python3 tools/icons_cafes_1108h.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "h_vine": ("#F4FFE2", "#A3C76A"),
    "h_space": ("#5B3FA8", "#1A1240"),
    "h_bakery": ("#FFF4E8", "#F2B48C"),
    "h_nonna": ("#FFF0F0", "#E58C8C"),
    "h_izba": ("#FFF6DA", "#D9A55B"),
    "h_arabnight": ("#3C2E7A", "#14103A"),
    "h_surf": ("#E0FBFF", "#3FB6D8"),
    "h_mint": ("#ECFFF6", "#73CFA4"),
    "h_gym": ("#FFF3D6", "#F2A93B"),
    "h_lilac": ("#F7EEFF", "#B69AE6"),
    "h_museum": ("#FFF7E4", "#B98A5A"),
    "h_kremlin": ("#E9F5FF", "#8AB8E8"),
    "h_kitchen": ("#FFF0E4", "#F09A6A"),
    "h_cherry": ("#FFF1F4", "#E86A86"),
    "h_sunset": ("#FFE9C9", "#F07E5A"),
    "h_window": ("#EAF6FF", "#9CC9EE"),
    "h_oak": ("#F2F7E3", "#8EA35A"),
})

# 1. Джонджоли (Дмитровское) — квеври в земле под лозой
ICONS["cafe-dzhondzholi-dmitrovskoe-72"] = svg("h_vine", f'''
<path d="M-4 22 Q40 6 70 20 Q100 34 132 18" fill="none" stroke="#7A5232" stroke-width="5" stroke-linecap="round"/>
<path d="M30 14 q-10 8 -2 18 q10 -4 2 -18z M84 26 q-10 10 0 18 q10 -6 0 -18z" fill="#5FAE4E" {W(2)}/>
<g fill="#8E4BB8" {W(1.6)}><circle cx="56" cy="28" r="5"/><circle cx="64" cy="28" r="5"/><circle cx="60" cy="36" r="5"/><circle cx="52" cy="36" r="5"/><circle cx="56" cy="44" r="5"/></g>
<rect x="0" y="88" width="128" height="44" fill="#9B6A3E"/>
<path d="M0 88 Q32 82 64 88 T128 88" fill="#7FBF5A" {W(2.4)}/>
<path d="M34 92 Q26 56 46 46 H82 Q102 56 94 92Z" fill="#D9784A" {s()}/>
<ellipse cx="64" cy="46" rx="20" ry="6" fill="#B85A34" {W(2.4)}/>
<ellipse cx="64" cy="45" rx="13" ry="3.5" fill="#5A2A3E"/>
{face(64, 68, d=9, k=0.85)}
<path d="M86 40 q6 -10 14 -6 q-2 8 -14 6z" fill="#FF9A3C" {W(1.8)}/><circle cx="95" cy="35" r="1.6" fill="{O}"/>
<path d="M88 42 l-2 6 M92 42 l0 6" {W(1.6)}/>
''')
SUBJ["cafe-dzhondzholi-dmitrovskoe-72"] = ("терракотовый грузинский кувшин-квеври с широким горлышком",
                                          "закопан по плечи в землю под виноградной лозой, на краю горлышка сидит рыжая птичка")

# 2. Галактика 2.0 — торт-планета с кольцом и свечкой-ракетой
ICONS["cafe-galaktika-2-korolyova"] = svg("h_space", f'''
{sparkle(20, 30, 4)}{sparkle(104, 22, 5)}{sparkle(110, 96, 3)}{sparkle(18, 98, 3)}
<circle cx="30" cy="60" r="1.6" fill="#fff"/><circle cx="96" cy="44" r="1.4" fill="#fff"/><circle cx="74" cy="112" r="1.6" fill="#fff"/>
<ellipse cx="64" cy="80" rx="56" ry="12" fill="none" stroke="#FFC93C" stroke-width="7"/>
<path d="M34 86 Q30 52 64 50 Q98 52 94 86 Q64 98 34 86Z" fill="#FF8FB1" {s()}/>
<path d="M36 62 Q50 70 64 64 Q78 70 92 62" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<path d="M8 80 Q64 104 120 80" fill="none" stroke="#FFC93C" stroke-width="7"/>
<path d="M8 80 Q64 104 120 80" fill="none" {W(2)}/>
{face(64, 76, d=9, k=0.8)}
<path d="M58 50 V34 Q64 22 70 34 V50Z" fill="#9ED3FF" {W(2.4)}/><circle cx="64" cy="38" r="3" fill="#fff" {W(1.4)}/>
<path d="M58 44 l-5 6 h5z M70 44 l5 6 h-5z" fill="#E8554A" {W(1.6)}/>
<path d="M64 22 q-4 -6 0 -12 q4 6 0 12z" fill="#FFB43C" {W(1.6)}/>
''')
SUBJ["cafe-galaktika-2-korolyova"] = ("розовый торт-планета с жёлтым кольцом, как у Сатурна",
                                      "парит в фиолетовом космосе, а на макушке вместо свечки стоит голубая ракетка с огоньком")

# 3. Здрасте (Волгоградский) — шоколадное полено-рулет здоровается на прилавке
ICONS["cafe-zdraste-volgogradsky-32"] = svg("h_bakery", f'''
<rect x="0" y="98" width="128" height="32" fill="#F7DCC4"/><path d="M0 98 H128" {W(2.4)}/>
<path d="M22 58 H96 Q106 58 106 78 Q106 98 96 98 H22Z" fill="#6B3E26" {s()}/>
<path d="M30 64 Q50 60 70 66 M28 90 Q52 94 80 88 M60 78 Q74 74 90 80" fill="none" stroke="#8A5634" stroke-width="3"/>
<ellipse cx="22" cy="78" rx="12" ry="20" fill="#F4E0B8" {s()}/>
<path d="M22 66 Q30 70 28 80 Q24 88 18 82 Q14 74 22 72" fill="none" stroke="#6B3E26" stroke-width="3"/>
<path d="M60 58 V44 Q60 40 64 40 H70 Q74 40 74 44 V58" fill="#6B3E26" {W(2.4)}/><ellipse cx="67" cy="42" rx="7" ry="3" fill="#F4E0B8" {W(1.8)}/>
<circle cx="88" cy="56" r="6" fill="#E8304A" {W(2)}/><path d="M80 60 q-4 -6 2 -8 q4 4 -2 8z" fill="#5FAE4E" {W(1.4)}/>
{face(66, 80, d=9, k=0.75)}
<path d="M104 72 q12 -6 14 -20" fill="none" {W(4)}/><circle cx="118" cy="50" r="5" fill="#6B3E26" {W(2)}/>
<circle cx="40" cy="50" r="2" fill="#fff"/><circle cx="50" cy="40" r="1.6" fill="#fff"/><circle cx="96" cy="36" r="2" fill="#fff"/>
''')
SUBJ["cafe-zdraste-volgogradsky-32"] = ("шоколадное полено-рулет с кремовой спиралью на срезе и сучком",
    "лежит на прилавке пекарни под сахарной пудрой и машет рукой — здоровается")

# 4. ДаНонна — бабушка-нонна раскатывает тесто
ICONS["cafe-danonna-chistova"] = svg("h_nonna", f'''
<rect x="0" y="92" width="128" height="40" fill="#C98A5A"/>
<path d="M0 92 H128" {W(2.4)}/>
<path d="M30 92 Q24 58 64 54 Q104 58 98 92Z" fill="#5E8FD6" {s()}/>
<path d="M44 92 Q42 68 64 66 Q86 68 84 92Z" fill="#fff" {W(2)}/>
<circle cx="64" cy="40" r="20" fill="#FFD9BE" {s()}/>
<path d="M44 36 Q44 14 64 14 Q84 14 84 36 Q76 24 64 26 Q52 24 44 36Z" fill="#E6E6EE" {W(2.4)}/>
<circle cx="64" cy="14" r="8" fill="#E6E6EE" {W(2.4)}/>
<circle cx="56" cy="40" r="6" fill="#fff" fill-opacity=".5" {W(2)}/><circle cx="72" cy="40" r="6" fill="#fff" fill-opacity=".5" {W(2)}/>
<path d="M62 40 h4" {W(2)}/>
<circle cx="56" cy="40" r="2" fill="{O}"/><circle cx="72" cy="40" r="2" fill="{O}"/>
<path d="M58 50 Q64 55 70 50" fill="none" {W(2.4)}/>
<ellipse cx="50" cy="48" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="78" cy="48" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<ellipse cx="64" cy="104" rx="40" ry="9" fill="#FFF3D6" {W(2.4)}/>
<rect x="30" y="92" width="68" height="10" rx="5" fill="#E2B070" {W(2.4)}/>
<rect x="20" y="94" width="12" height="6" rx="3" fill="#B87A44" {W(2)}/><rect x="96" y="94" width="12" height="6" rx="3" fill="#B87A44" {W(2)}/>
<circle cx="18" cy="80" r="2" fill="#fff"/><circle cx="108" cy="78" r="2.4" fill="#fff"/><circle cx="102" cy="70" r="1.6" fill="#fff"/>
''')
SUBJ["cafe-danonna-chistova"] = ("седая итальянская бабушка-нонна в круглых очках и синем платье с белым фартуком",
                                 "раскатывает скалкой тесто для пасты на деревянном столе, вокруг облачка муки")

# 5. Му-Му (Семёновская) — винегрет едет по раздаче столовой
ICONS["cafe-mumu-semenovskaya"] = svg("h_izba", f'''
<rect x="0" y="0" width="128" height="58" fill="#FBF5EC" opacity=".6"/>
<path d="M0 98 H128 M0 108 H128" stroke="#B9C2D0" stroke-width="6"/><path d="M0 95 H128 M0 111 H128" {W(2)}/>
<rect x="18" y="82" width="92" height="16" rx="4" fill="#6FB7D8" {s()}/>
<path d="M30 82 Q30 56 64 56 Q98 56 98 82Z" fill="#DFF3FF" fill-opacity=".8" {s()}/>
<path d="M36 74 Q64 64 92 74 Q64 80 36 74Z" fill="#B8243A" {W(1.8)}/>
<g {W(1.4)}><rect x="40" y="62" width="7" height="7" fill="#B8243A"/><rect x="50" y="58" width="7" height="7" fill="#FF9A3C"/><rect x="62" y="56" width="7" height="7" fill="#F4E0B8"/><rect x="74" y="60" width="7" height="7" fill="#B8243A"/><circle cx="58" cy="68" r="3" fill="#7CD26E"/><circle cx="84" cy="66" r="3" fill="#7CD26E"/><rect x="44" y="68" width="6" height="5" fill="#5FAE4E"/></g>
{face(64, 76, d=8, k=0.6, mouth=False)}<path d="M60 80 Q64 83 68 80" fill="none" {W(2)}/>
<path d="M104 70 H120 L116 60 H108Z" fill="#FFF" {W(2)}/><path d="M106 66 h12" stroke="#E2B66E" stroke-width="3"/>
<path d="M8 40 H40 M8 30 H30" stroke="#E2B66E" stroke-width="4" stroke-linecap="round"/>
''')
SUBJ["cafe-mumu-semenovskaya"] = ("стеклянная салатница с винегретом — свёкла, морковка, огурчики, горошек",
    "едет на голубом подносе по металлическим рельсам столовской раздачи")

# 6. Сказка Востока 1001 ночь — медная восточная лампа с волшебным дымком
ICONS["cafe-skazka-vostoka-novotushinsky"] = svg("h_arabnight", f'''
<path d="M86 30 a14 14 0 1 0 10 -16 a11 11 0 1 1 -10 16z" fill="#FFE27A"/>
{sparkle(20, 22, 4)}{sparkle(50, 14, 3)}
<path d="M0 128 V100 H14 V86 Q22 74 30 86 V100 H98 V82 Q108 66 118 82 V100 H128 V128Z" fill="#241A55"/>
<path d="M76 84 Q70 62 84 52 Q100 42 92 26 Q108 34 104 52 Q100 66 82 70" fill="#C9A8FF" opacity=".75"/>
{sparkle(98, 46, 3.4)}{sparkle(88, 60, 2.6)}
<path d="M18 92 Q20 74 50 72 H74 Q86 72 92 66 L104 58 Q100 72 88 82 Q78 92 60 94 H34 Q18 94 18 92Z" fill="#E8A040" {s()}/>
<path d="M34 72 Q44 56 58 72" fill="#F2B84C" {W(2.4)}/><circle cx="46" cy="58" r="4" fill="#F2B84C" {W(2)}/>
<path d="M18 84 Q4 82 8 70 Q14 64 22 76" fill="none" {W(3)}/>
<path d="M36 94 L32 104 H66 L62 94" fill="#C9822C" {W(2.4)}/>
{face(48, 82, d=7, k=0.7)}
''')
SUBJ["cafe-skazka-vostoka-novotushinsky"] = ("медная восточная лампа с изогнутым носиком и крышечкой-куполом",
                                             "из носика клубится сиреневый волшебный дымок со звёздочками над ночным городом с минаретами")

# 7. Nalu Baloo — медвежонок-сёрфер на волне
ICONS["cafe-nalu-baloo-luzhniki"] = svg("h_surf", f'''
<circle cx="102" cy="26" r="12" fill="#FFE27A"/>
<path d="M-4 92 Q20 70 44 84 Q60 94 74 80 Q90 56 120 66 Q104 72 106 82 Q132 86 132 100 V132 H-4Z" fill="#2E8FD0" {s()}/>
<path d="M-4 104 Q30 92 60 104 T132 102 V132 H-4Z" fill="#1F6FB0"/>
<path d="M78 74 Q92 60 112 66" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M22 84 L98 70 Q108 70 100 78 L26 92 Q14 92 22 84Z" fill="#FF7A59" {s()}/><path d="M28 86 L96 73" stroke="#fff" stroke-width="3"/>
<ellipse cx="58" cy="60" rx="17" ry="16" fill="#A9774A" {s()}/>
<circle cx="58" cy="36" r="16" fill="#A9774A" {s()}/>
<circle cx="45" cy="24" r="6" fill="#A9774A" {W(2.4)}/><circle cx="71" cy="24" r="6" fill="#A9774A" {W(2.4)}/>
<ellipse cx="58" cy="42" rx="7" ry="5" fill="#E8C9A0" {W(1.8)}/><ellipse cx="58" cy="39.5" rx="2.6" ry="1.8" fill="{O}"/>
{eye(52, 32, 0.8)}{eye(64, 32, 0.8)}
<path d="M42 54 Q30 46 26 54 M74 54 Q86 46 92 52" fill="none" stroke="#A9774A" stroke-width="7" stroke-linecap="round"/>
<path d="M42 54 Q30 46 26 54 M74 54 Q86 46 92 52" fill="none" {W(2)}/>
<path d="M50 74 l-2 6 M66 74 l2 6" stroke="#A9774A" stroke-width="7" stroke-linecap="round"/>
''')
SUBJ["cafe-nalu-baloo-luzhniki"] = ("бурый медвежонок-сёрфер с раскинутыми лапами",
                                    "балансирует на коралловой доске на гребне синей волны под жарким солнцем")

# 8. Здрасте (Власова) — тарт-татен кувыркается над сковородкой
ICONS["cafe-zdraste-vlasova-71"] = svg("h_mint", f'''
<path d="M14 104 Q14 120 50 120 Q86 120 86 104Z" fill="#3A3A44" {s()}/><path d="M86 108 H120" stroke="#3A3A44" stroke-width="8" stroke-linecap="round"/>
<ellipse cx="50" cy="104" rx="36" ry="6" fill="#55555F" {W(2.4)}/>
<path d="M30 90 q-8 -20 6 -36 M96 84 q10 -16 -2 -32" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 6"/>
<g transform="rotate(-20 66 56)"><path d="M28 50 Q28 34 66 34 Q104 34 104 50 L98 70 Q66 80 34 70Z" fill="#E9B870" {s()}/>
<path d="M30 48 Q66 30 102 48 Q66 58 30 48Z" fill="#C8742A" {W(2.4)}/>
<g fill="#F2B84C" {W(1.6)}><path d="M40 46 q8 -8 16 0 q-8 4 -16 0z"/><path d="M58 42 q8 -8 16 0 q-8 4 -16 0z"/><path d="M76 46 q8 -8 16 0 q-8 4 -16 0z"/></g>
{face(66, 62, d=8, k=0.7)}</g>
{sparkle(108, 22, 5)}{sparkle(18, 30, 3.4)}
''')
SUBJ["cafe-zdraste-vlasova-71"] = ("перевёрнутый яблочный пирог тарт-татен с карамельными дольками",
    "кувыркается в воздухе над чёрной чугунной сковородкой, как блин")

# 9. Forte Bello — капучино-силач с бискотти-штангой
ICONS["cafe-forte-bello-crocus"] = svg("h_gym", f'''
<rect x="0" y="104" width="128" height="26" fill="#5A6B8A"/><path d="M0 104 H128" {W(2.4)}/>
<path d="M36 62 H92 L86 100 Q84 106 76 106 H52 Q44 106 42 100Z" fill="#fff" {s()}/>
<path d="M92 70 Q106 70 104 84 Q102 94 88 92" fill="none" {W(5)}/>
<ellipse cx="64" cy="62" rx="28" ry="7" fill="#C98A5A" {W(2.4)}/>
<path d="M58 60 q6 -6 12 0 q-6 6 -12 0z" fill="#FBEAD6"/>
{face(64, 82, d=8, k=0.75)}
<path d="M40 70 Q30 58 32 44 M88 70 Q98 58 96 44" fill="none" {W(5)}/>
<path d="M24 40 H104" stroke="#7A5232" stroke-width="5" stroke-linecap="round"/>
<rect x="14" y="24" width="18" height="32" rx="6" fill="#E9B870" {s()}/><rect x="96" y="24" width="18" height="32" rx="6" fill="#E9B870" {s()}/>
<circle cx="20" cy="32" r="2" fill="#B87A44"/><circle cx="26" cy="46" r="2" fill="#B87A44"/><circle cx="102" cy="32" r="2" fill="#B87A44"/><circle cx="108" cy="46" r="2" fill="#B87A44"/>
<path d="M22 70 l-6 -4 M20 78 l-8 0 M106 70 l6 -4 M108 78 l8 0" {W(2.4)}/>
''')
SUBJ["cafe-forte-bello-crocus"] = ("чашка капучино-силач с пенкой и сердечком",
                                   "поднимает над головой штангу, где вместо блинов — два печенья бискотти")

# 10. Здрасте (Красногорск) — кейк-попсы в букете
ICONS["cafe-zdraste-lipovoy-roshchi"] = svg("h_lilac", f'''
<path d="M40 128 L56 80 H72 L88 128Z" fill="#9ED3FF" {s()}/>
<path d="M50 96 Q64 104 78 96" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M60 82 L46 44 M64 82 L64 34 M68 82 L84 46" {W(3)}/>
<circle cx="44" cy="40" r="13" fill="#FF8FB1" {s()}/><path d="M34 36 q4 -4 8 0 M46 32 q4 -4 8 0" stroke="#fff" stroke-width="2.4" fill="none"/>
<circle cx="86" cy="42" r="13" fill="#7CD26E" {s()}/><circle cx="82" cy="36" r="1.8" fill="#FFE27A"/><circle cx="90" cy="38" r="1.8" fill="#E8554A"/><circle cx="86" cy="32" r="1.8" fill="#fff"/>
<circle cx="64" cy="30" r="17" fill="#6B3E26" {s()}/><path d="M50 24 Q64 12 78 24 Q72 28 64 24 Q56 30 50 24Z" fill="#fff" {W(2)}/>
{face(64, 33, d=6, k=0.6)}
{face(44, 42, d=4, k=0.45, mouth=False)}{face(86, 44, d=4, k=0.45, mouth=False)}
<path d="M56 80 Q64 72 72 80 L68 86 L64 80 L60 86Z" fill="#FFC93C" {W(2)}/>
''')
SUBJ["cafe-zdraste-lipovoy-roshchi"] = ("три кейк-попса на палочках — шоколадный, розовый и зелёный",
                                        "стоят букетом в голубом бумажном рожке, перевязанном жёлтым бантом")

# 11. Эрмитаж — кусочек торта «Прага» под музейным колпаком
ICONS["cafe-ermitazh-elektrostal"] = svg("h_museum", f'''
<rect x="0" y="0" width="128" height="20" fill="#8A5A34" opacity=".35"/>
<path d="M8 10 H120" stroke="#E2B66E" stroke-width="3"/>
<path d="M40 110 V96 H88 V110Z" fill="#E8E2D4" {s()}/><rect x="32" y="108" width="64" height="10" fill="#D4CBB8" {s()}/>
<path d="M36 96 V54 Q36 30 64 30 Q92 30 92 54 V96Z" fill="#CFEFFF" fill-opacity=".45" {s()}/>
<path d="M44 50 Q46 38 56 36" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M44 94 L84 94 L84 76 L44 64Z" fill="#7A4A2A" {s()}/>
<path d="M44 64 L84 76 L88 72 L50 60Z" fill="#4A2A1A" {W(2.4)}/>
<path d="M44 80 L84 86" stroke="#C99A6E" stroke-width="3"/>
<path d="M62 64 q2 -8 8 -6 q-1 6 -8 6z" fill="#fff" {W(1.6)}/>
{face(66, 86, d=6, k=0.55)}
<rect x="52" y="100" width="24" height="6" rx="2" fill="#E2B66E" {W(1.6)}/>
<path d="M10 118 V40 M118 118 V40" stroke="#D9C49A" stroke-width="6"/>
''')
SUBJ["cafe-ermitazh-elektrostal"] = ("треугольный кусочек шоколадного торта «Прага» с кремовым завитком",
                                     "стоит под стеклянным колпаком на музейном пьедестале с золотой табличкой")

# 12. Старик Хинкалыч (Коломна) — хинкали-альпинист на кремлёвской стене
ICONS["cafe-starik-khinkalych-kolomna"] = svg("h_kremlin", f'''
<rect x="62" y="34" width="70" height="98" fill="#C94A3A" {s()}/>
<path d="M62 34 V22 H74 V34 M86 34 V22 H98 V34 M110 34 V22 H122 V34" fill="#C94A3A" {W(2.6)}/>
<path d="M62 54 H132 M62 74 H132 M62 94 H132 M62 114 H132 M80 34 V54 M104 34 V54 M92 54 V74 M116 54 V74 M80 74 V94 M104 74 V94 M92 94 V114" stroke="#A8382C" stroke-width="2"/>
<path d="M70 22 L70 8" {W(2.4)}/><path d="M70 8 L84 12 L70 16Z" fill="#FFC93C" {W(1.8)}/>
<path d="M70 18 Q60 50 48 64" fill="none" stroke="#E8D8B0" stroke-width="3"/>
<path d="M22 100 Q14 72 36 64 Q46 60 54 66 Q72 80 58 104 Q40 116 22 100Z" fill="#F7EEDC" {s()}/>
<path d="M30 70 Q36 82 34 96 M42 66 Q46 82 46 100 M52 70 Q56 84 52 100" fill="none" stroke="#D9C9A8" stroke-width="2.4"/>
<path d="M40 64 Q44 52 52 50 Q50 58 46 64" fill="#F7EEDC" {W(2.4)}/>
{face(40, 88, d=7, k=0.7)}
<path d="M54 74 Q60 64 58 54" fill="none" {W(3)}/>
<path d="M24 104 l-6 10 M40 110 l-2 12" {W(3)}/>
''')
SUBJ["cafe-starik-khinkalych-kolomna"] = ("пухлый хинкали-альпинист со складочками",
                                          "карабкается по верёвке на красную зубчатую стену Коломенского кремля к флажку")

# 13. Здрасте (Одинцово, Бирюзова) — шакшука на игрушечной плите
ICONS["cafe-zdraste-odintsovo-biryuzova"] = svg("h_kitchen", f'''
<rect x="16" y="76" width="96" height="56" rx="6" fill="#FF7FA8" {s()}/>
<rect x="28" y="92" width="72" height="30" rx="5" fill="#FFD6E4" {W(2.4)}/><circle cx="38" cy="86" r="3" fill="#fff" {W(1.6)}/><circle cx="52" cy="86" r="3" fill="#fff" {W(1.6)}/>
<rect x="56" y="100" width="16" height="4" rx="2" fill="{O}"/>
<path d="M12 76 H116" {W(3)}/>
<path d="M98 64 H122" stroke="#3A3A3A" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="62" cy="64" rx="38" ry="14" fill="#2E2E3A" {s()}/>
<ellipse cx="62" cy="60" rx="32" ry="10" fill="#E8463A" {W(2)}/>
<ellipse cx="48" cy="60" rx="8" ry="5" fill="#fff" {W(1.6)}/><circle cx="48" cy="59" r="3" fill="#FFC21A"/>
<ellipse cx="74" cy="58" rx="8" ry="5" fill="#fff" {W(1.6)}/><circle cx="74" cy="57" r="3" fill="#FFC21A"/>
<circle cx="62" cy="66" r="1.8" fill="#5FB06A"/><circle cx="86" cy="62" r="1.8" fill="#5FB06A"/><circle cx="38" cy="64" r="1.8" fill="#5FB06A"/>
{face(61, 64, d=6, k=0.5, mouth=False)}
<path d="M48 40 q-4 -8 0 -14 M62 38 q-4 -8 0 -16 M76 40 q-4 -8 0 -14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-zdraste-odintsovo-biryuzova"] = ("чугунная сковородка шакшуки с двумя яйцами в томатном соусе",
                                            "шкворчит на розовой игрушечной плите в детской игровой")

# 14. Здрасте (Одинцово, Северная) — вишнёвый пай с решёткой
ICONS["cafe-zdraste-odintsovo-severnaya"] = svg("h_cherry", f'''
<rect x="0" y="0" width="128" height="40" fill="#fff" opacity=".35"/>
<path d="M0 40 H128" stroke="#fff" stroke-width="3"/>
<ellipse cx="64" cy="80" rx="50" ry="26" fill="#F0C080" {s()}/>
<ellipse cx="64" cy="74" rx="44" ry="20" fill="#C8243A" {W(2.4)}/>
<g stroke="#F4D49A" stroke-width="7" stroke-linecap="round"><path d="M36 60 L50 92 M58 56 L72 94 M80 58 L92 88"/><path d="M26 76 L100 64 M30 86 L104 76"/></g>
<g fill="none" {W(1.4)}><path d="M36 60 L50 92 M58 56 L72 94 M80 58 L92 88 M26 76 L100 64 M30 86 L104 76"/></g>
<path d="M14 80 Q14 108 64 108 Q114 108 114 80" fill="#E2A860" {s()}/>
{face(64, 96, d=9, k=0.75)}
<circle cx="98" cy="38" r="8" fill="#C8243A" {W(2)}/><path d="M98 30 q4 -10 12 -12" fill="none" {W(2)}/><path d="M106 22 q8 -2 8 4 q-6 2 -8 -4z" fill="#5FAE4E" {W(1.6)}/>
''')
SUBJ["cafe-zdraste-odintsovo-severnaya"] = ("круглый вишнёвый пай с плетёной решёткой из теста",
                                            "остывает на розовой скатерти, рядом спелая вишенка с листиком")

# 15. Терацца Колессео — песочный Колизей под зонтиком на террасе
ICONS["cafe-terracca-kolesseo-odintsovo"] = svg("h_sunset", f'''
<circle cx="64" cy="70" r="26" fill="#FFD25E" opacity=".7"/>
<rect x="0" y="104" width="128" height="26" fill="#E8C9A0"/><path d="M0 104 H128" {W(2.4)}/>
<path d="M22 104 V66 Q22 56 64 56 Q106 56 106 66 V104Z" fill="#F2C98A" {s()}/>
<path d="M22 78 H106" {W(2)}/>
<g fill="#C8874A" {W(1.8)}><path d="M30 104 V92 Q34 86 38 92 V104Z M46 104 V92 Q50 86 54 92 V104Z M74 104 V92 Q78 86 82 92 V104Z M90 104 V92 Q94 86 98 92 V104Z"/>
<path d="M30 74 V66 Q33 61 36 66 V74Z M44 74 V66 Q47 61 50 66 V74Z M78 74 V66 Q81 61 84 66 V74Z M92 74 V66 Q95 61 98 66 V74Z"/></g>
{face(64, 90, d=8, k=0.75)}
<path d="M64 56 V20" {W(3)}/>
<path d="M22 28 Q64 -2 106 28Z" fill="#fff" {s()}/>
<path d="M36 22 Q50 10 64 8 V28 H50Z M78 22 Q78 12 64 8 L92 22 V28 H78Z" fill="#3E9B57"/>
<path d="M22 28 Q64 -2 106 28" fill="none" {W(2.4)}/>
''')
SUBJ["cafe-terracca-kolesseo-odintsovo"] = ("Колизей из песочного печенья с арками",
                                            "стоит на летней террасе под бело-зелёным зонтиком на фоне закатного солнца")

# 16. Casa de Mammy — суп с вермишелью-звёздочками
ICONS["cafe-casa-de-mammy-domodedovo"] = svg("h_window", f'''
<path d="M0 0 H34 Q30 40 40 70 H0Z M128 0 H94 Q98 40 88 70 H128Z" fill="#FF8FB1" opacity=".55"/>
<path d="M0 0 L12 70 M24 0 L30 70 M104 0 L98 70 M118 0 L120 70" stroke="#fff" stroke-width="2"/>
<rect x="0" y="96" width="128" height="34" fill="#F7EEDC"/><path d="M0 96 H128" {W(2.4)}/>
<path d="M18 74 Q18 110 64 110 Q110 110 110 74Z" fill="#fff" {s()}/>
<path d="M30 92 Q64 100 98 92" fill="none" stroke="#9ED3FF" stroke-width="4"/>
<path d="M44 96 l4 4 l4 -4 M78 96 l4 4 l4 -4" fill="none" stroke="#FF8FB1" stroke-width="2.4"/>
<ellipse cx="64" cy="74" rx="46" ry="11" fill="#FFD25E" {W(2.6)}/>
<g fill="#FFF3B0" {W(1.2)}><path d="M42 72 l2 -5 l2 5 l5 0 l-4 3 l2 5 l-5 -3 l-5 3 l2 -5 l-4 -3z"/><path d="M78 70 l2 -5 l2 5 l5 0 l-4 3 l2 5 l-5 -3 l-5 3 l2 -5 l-4 -3z"/><path d="M62 78 l1.6 -4 l1.6 4 l4 0 l-3 2.4 l1.6 4 l-4 -2.4 l-4 2.4 l1.6 -4 l-3 -2.4z"/></g>
<circle cx="56" cy="70" r="2" fill="#FF8A3C"/><circle cx="96" cy="74" r="2" fill="#FF8A3C"/><circle cx="30" cy="74" r="2" fill="#5FB06A"/>
{face(64, 88, d=10, k=0.8)}
<path d="M84 40 Q96 24 112 40 Q100 52 84 40Z" fill="#B9C2D0" {s()}/><path d="M100 36 L104 74" {W(4)}/>
<path d="M50 54 q-4 -8 0 -14 M64 52 q-4 -8 0 -16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-casa-de-mammy-domodedovo"] = ("тарелка домашнего куриного супчика с вермишелью-звёздочками",
                                         "мамин половник подливает ещё у окна с розовыми занавесками")

# 17. Трюфель — свинка-трюфелеискательница под дубом
ICONS["cafe-tryufel-elektrostal"] = svg("h_oak", f'''
<path d="M84 128 V54" stroke="#7A5232" stroke-width="12"/><path d="M84 128 V54" {W(2.4)}/>
<circle cx="74" cy="28" r="22" fill="#5E9B44" {s()}/><circle cx="104" cy="32" r="20" fill="#6FAE50" {s()}/><circle cx="92" cy="12" r="16" fill="#6FAE50" {W(2.6)}/>
<path d="M66 40 q2 6 6 4 M104 46 q2 6 6 4" fill="#C8874A" {W(1.6)}/>
<rect x="0" y="100" width="128" height="30" fill="#8A5A34"/><path d="M0 100 Q64 94 128 100" fill="none" {W(2.4)}/>
<circle cx="96" cy="108" r="9" fill="#3A2A2A" {s()}/><circle cx="93" cy="105" r="1.4" fill="#8A6A5A"/><circle cx="99" cy="110" r="1.2" fill="#8A6A5A"/>
<ellipse cx="44" cy="84" rx="30" ry="20" fill="#FFB3C6" {s()}/>
<path d="M14 82 q-8 -6 -4 -12 q4 4 0 8" fill="none" {W(2.4)}/>
<path d="M34 66 l-4 -12 l10 6z M54 66 l4 -12 l-10 6z" fill="#FF9AB6" {W(2.2)}/>
<rect x="70" y="80" width="14" height="14" rx="6" fill="#FF9AB6" {W(2.4)}/><circle cx="75" cy="87" r="1.6" fill="{O}"/><circle cx="80" cy="87" r="1.6" fill="{O}"/>
{eye(50, 76, 0.8)}{eye(62, 76, 0.8)}
<ellipse cx="46" cy="86" rx="4" ry="2.4" fill="#FF7FA8"/>
<path d="M26 102 v8 M40 102 v8 M54 102 v8" {W(4)}/>
<path d="M88 92 q4 -2 6 2 M90 86 q4 -2 6 2" fill="none" {W(1.8)}/>
''')
SUBJ["cafe-tryufel-elektrostal"] = ("розовая свинка-трюфелеискательница с пятачком",
                                    "принюхивается у корней большого дуба, где из земли выглядывает чёрный трюфель")

# 18. Пататапа (Раменское) — тапочки шлёпают по следам в игровой
draw_icons.BG["h_playfloor"] = ("#F0FBFF", "#7CC8E8")
ICONS["cafe-patatapa-ramenskoe"] = svg("h_playfloor", f'''
<g opacity=".9"><ellipse cx="22" cy="40" rx="7" ry="10" fill="#FFC93C"/><ellipse cx="40" cy="26" rx="7" ry="10" fill="#7CD26E"/>
<ellipse cx="96" cy="30" rx="7" ry="10" fill="#A98BF0"/><ellipse cx="112" cy="50" rx="7" ry="10" fill="#FF8FB1"/>
<ellipse cx="20" cy="98" rx="7" ry="10" fill="#9ED3FF"/></g>
<g transform="rotate(-14 46 80)"><path d="M26 84 Q24 58 46 56 Q68 58 66 84 Q66 104 46 104 Q26 104 26 84Z" fill="#E8463A" {s()}/>
<path d="M30 76 Q46 66 62 76 Q62 92 46 92 Q30 92 30 76Z" fill="#FBEDE0" {W(2)}/>
<circle cx="46" cy="58" r="9" fill="#fff" {W(2.4)}/>{face(46, 80, d=6, k=0.6)}</g>
<g transform="rotate(12 86 72) translate(0 -14)"><path d="M66 84 Q64 58 86 56 Q108 58 106 84 Q106 104 86 104 Q66 104 66 84Z" fill="#E8463A" {s()}/>
<path d="M70 76 Q86 66 102 76 Q102 92 86 92 Q70 92 70 76Z" fill="#FBEDE0" {W(2)}/>
<circle cx="86" cy="58" r="9" fill="#fff" {W(2.4)}/>{face(86, 80, d=6, k=0.6)}</g>
<path d="M60 110 q4 -6 8 0 M74 112 q4 -6 8 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''')
SUBJ["cafe-patatapa-ramenskoe"] = ("пара красных детских тапочек с белыми помпонами",
                                   "весело шлёпают по разноцветным следам на полу детской игровой")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ICONS]
    lines += [f"{pid} — герой: {h} | сцена: {sc}" for pid, (h, sc) in SUBJ.items()]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
