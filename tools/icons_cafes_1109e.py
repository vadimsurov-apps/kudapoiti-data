"""Иконки робота cafes, 2026-11-09 (17 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по названию/кухне, своя сцена, своя компоновка и палитра фона). Сверено с icons-src/subjects.txt
(поиск по ключевым словам) и всеми листами icons-catalog.
Запуск: python3 tools/icons_cafes_1109e.py [id…]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k11_lagoon": ("#E8FFFB", "#2FA6A0"),
    "k11_moon": ("#3C3F86", "#0E1236"),
    "k11_ruby": ("#FFF1F0", "#C9465A"),
    "k11_board": ("#F4FFF0", "#7BB36A"),
    "k11_mint": ("#F0FFF8", "#8FD9C0"),
    "k11_cream": ("#FFFBEF", "#F2C66D"),
    "k11_candy": ("#FFF0FF", "#C98BE8"),
    "k11_nursery": ("#F3F1FF", "#8F9BE0"),
    "k11_neon": ("#5B2C6F", "#1C0B2B"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Aquarium — аквариум-супница: лапша вьётся, как водоросли, морковные кружочки плавают, как рыбки
add("cafe-aquarium-ryazansky",
    "пузатый стеклянный аквариум, полный куриного супа",
    "лапша колышется в нём, как водоросли, а морковные кружочки плавают, как рыбки", "k11_lagoon", f'''
<ellipse cx="64" cy="112" rx="44" ry="8" fill="#1F7D78" opacity=".35"/>
<path d="M28 44 Q20 76 34 100 Q46 114 64 114 Q82 114 94 100 Q108 76 100 44Z" fill="#DDF6FF" fill-opacity=".9" {s()}/>
<path d="M30 58 Q22 82 36 100 Q48 112 64 112 Q80 112 92 100 Q106 82 98 58 Q64 66 30 58Z" fill="#FFD976" {W(2)}/>
<ellipse cx="64" cy="44" rx="36" ry="7" fill="#C9EEFF" {s()}/>
<path d="M44 108 Q38 92 46 82 Q54 72 46 62 M60 110 Q66 94 58 84 Q50 74 58 62 M80 108 Q74 92 82 82 Q88 72 80 62"
 fill="none" stroke="#FFF6D6" stroke-width="4" stroke-linecap="round"/>
<circle cx="74" cy="78" r="6" fill="#FF9A3C" {W(2)}/><path d="M80 78 l5 -4 v8z" fill="#FF9A3C" {W(1.6)}/>
<circle cx="72.5" cy="76.5" r="1.3" fill="{O}"/>
<circle cx="48" cy="94" r="5" fill="#FF9A3C" {W(2)}/><path d="M43 94 l-4 -3 v6z" fill="#FF9A3C" {W(1.6)}/>
<circle cx="49.5" cy="92.5" r="1.2" fill="{O}"/>
<circle cx="88" cy="70" r="2.5" fill="#fff" opacity=".9"/><circle cx="92" cy="60" r="1.8" fill="#fff" opacity=".9"/>
<path d="M38 52 Q36 66 40 78" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".8"/>
''' + face(64, 86, d=10, k=0.7) + sparkle(18, 30, 5) + sparkle(110, 24, 4))

# 2. На Луне — головка сыра-луна с дырками-кратерами, к ней по лесенке лезет малыш в скафандре с ложкой
add("cafe-na-lune-nekrasovka",
    "круглая головка жёлтого сыра-луна с дырками-кратерами",
    "висит в звёздном небе, а к ней по верёвочной лесенке карабкается малыш в скафандре с ложкой", "k11_moon",
    sparkle(16, 20, 4) + sparkle(30, 56, 2.5) + sparkle(112, 102, 3) + sparkle(20, 92, 3, "#FFE48A") + f'''
<circle cx="78" cy="44" r="34" fill="#FFD95A" {s()}/>
<circle cx="64" cy="28" r="6" fill="#F2B93B" {W(2)}/><circle cx="96" cy="34" r="4.5" fill="#F2B93B" {W(2)}/>
<circle cx="98" cy="60" r="7" fill="#F2B93B" {W(2)}/><circle cx="58" cy="58" r="3.5" fill="#F2B93B" {W(2)}/>
''' + face(80, 44, d=9, k=0.75) + f'''
<path d="M50 70 L38 122 M62 74 L52 124" {W(2.6)}/>
<path d="M47 84 L58 86 M44 96 L55 99 M41 108 L53 111" {W(2.6)}/>
<circle cx="36" cy="94" r="11" fill="#E9F2FF" {s()}/>
<circle cx="36" cy="94" r="7" fill="#9CC9F5" {W(2)}/>
<circle cx="34" cy="94" r="1.8" fill="{O}"/><circle cx="39" cy="94" r="1.8" fill="{O}"/>
<rect x="27" y="104" width="18" height="16" rx="6" fill="#fff" {s()}/>
<path d="M44 106 L54 98" {W(3)}/>
<path d="M54 98 L64 86" stroke="#B8C0D0" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="66" cy="83" rx="4" ry="5.5" fill="#D9DEE8" {W(2)} transform="rotate(35 66 83)"/>''')

# 3. Нар Арт («нар» — гранат) — гранат-торт с коронкой, в срез видны рубиновые зёрнышки, к нему тянется ложка
add("cafe-nar-art-moskovsky",
    "торт в форме спелого граната с коронкой-чашечкой",
    "стоит на высокой подставке, в разрезанном боку блестят рубиновые зёрнышки-желе, к нему тянется детская ложка", "k11_ruby", f'''
<path d="M64 104 V116 M40 118 H88" {W(4)}/>
<ellipse cx="64" cy="104" rx="38" ry="6" fill="#F5F0F7" {s()}/>
<circle cx="64" cy="66" r="36" fill="#E2394F" {s()}/>
<path d="M50 34 L54 22 L60 30 L64 18 L68 30 L74 22 L78 34Z" fill="#E2394F" {s()}/>
<path d="M64 66 L100 60 Q102 78 92 90Z" fill="#FFF0E8" {s()}/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#B5122C" {W(1.4)}/>' for x, y in
               [(78, 68), (86, 66), (94, 64), (84, 74), (92, 72), (90, 80)]) + f'''
<path d="M40 50 Q46 42 54 42" fill="none" stroke="#FF8C9B" stroke-width="4" stroke-linecap="round"/>
''' + face(52, 70, d=8, k=0.7) + f'''
<path d="M118 112 L102 88" stroke="#C9D2E0" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="99" cy="84" rx="5" ry="7" fill="#E3E8F0" {W(2)} transform="rotate(-35 99 84)"/>''' + sparkle(22, 30, 5) + sparkle(108, 30, 3.5))

# 4. Хинкальная 5+ — хинкали-первоклашка у школьной доски, на которой огромная «5+»
add("cafe-khinkalnaya-5plus-kommunarka",
    "пухлый хинкали-школьник с рыжим ранцем за спиной",
    "гордо стоит у зелёной школьной доски, на которой мелом написана огромная пятёрка с плюсом", "k11_board", f'''
<rect x="10" y="14" width="108" height="56" rx="4" fill="#2F6B4F" {s()}/>
<rect x="10" y="70" width="108" height="6" fill="#B07A47" {W(2)}/>
<path d="M30 30 H48 M30 30 V44 Q40 40 46 46 Q50 56 40 60 Q32 62 28 56" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M62 40 H76 M69 33 V47" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<rect x="90" y="66" width="12" height="4" rx="1" fill="#fff"/>
<rect x="74" y="78" width="22" height="26" rx="5" fill="#FF8A3D" {s()}/>
<path d="M58 54 Q60 46 64 46 Q68 46 70 54" fill="#F3E3C3" {s()}/>
<path d="M42 104 Q36 72 64 56 Q92 72 86 104 Q64 112 42 104Z" fill="#F7EAD0" {s()}/>
<path d="M50 70 Q56 66 58 60 M78 70 Q72 66 70 60 M64 58 V68" fill="none" {W(2)}/>
''' + face(64, 86, d=8, k=0.7) + f'''
<path d="M44 92 Q34 84 36 74" fill="none" {W(3)}/>
<path d="M50 108 v8 M78 108 v8" {W(3.5)}/>''')

# 5. Pizza&Sushi hub — кусочек пиццы и ролл вместе мчатся на самокате, ролл держится за пиццу
add("cafe-pizza-sushi-hub-nekrasovka",
    "кусочек пиццы пепперони в паре с роллом «Филадельфия»",
    "вдвоём мчатся на красном самокате по дорожке двора, за ними вьются полоски ветра", "k11_mint", f'''
<path d="M-4 112 H132 V132 H-4Z" fill="#B9E7D3" {s()}/>
<path d="M6 54 H26 M2 66 H20 M8 78 H24" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>
<path d="M28 106 H96 L104 52" fill="none" stroke="#E8403E" stroke-width="5" stroke-linecap="round"/>
<path d="M96 52 H112" {W(4)}/>
<circle cx="34" cy="108" r="7" fill="#3B3355"/><circle cx="34" cy="108" r="3" fill="#fff"/>
<circle cx="92" cy="108" r="7" fill="#3B3355"/><circle cx="92" cy="108" r="3" fill="#fff"/>
<path d="M44 102 L60 40 L82 100Z" fill="#FFD36B" {s()}/>
<path d="M54 52 Q60 46 66 52" fill="#E9A84A" {W(2)}/>
<circle cx="62" cy="84" r="4" fill="#D9473E" {W(1.6)}/><circle cx="70" cy="94" r="3.4" fill="#D9473E" {W(1.6)}/>
''' + eye(57, 70, 0.55) + eye(67, 70, 0.55) + f'''<path d="M58 78 Q62 81 66 78" fill="none" {W(2)}/>
<path d="M76 80 L90 64" {W(3)}/>
<circle cx="94" cy="76" r="14" fill="#2E3A3F" {s()}/>
<circle cx="94" cy="76" r="10" fill="#fff"/>
<path d="M88 74 Q94 68 100 74 Q98 80 94 80 Q90 80 88 74Z" fill="#FF8A65"/>
<circle cx="91" cy="73" r="1.5" fill="{O}"/><circle cx="97" cy="73" r="1.5" fill="{O}"/>
<path d="M100 66 L104 56" {W(3)}/>''')

# 6. Катька-Запеканка — запеканка-девочка с косичками сидит в ванночке со сметаной и пускает кораблик-изюминку
add("cafe-katka-zapekanka-marfino",
    "квадратик творожной запеканки с двумя косичками и бантиками",
    "сидит в маленькой ванночке со сметаной и пускает кораблик с парусом-изюминкой", "k11_cream", f'''
<path d="M38 34 Q30 46 36 56 M90 34 Q98 46 92 56" fill="none" stroke="#C9893C" stroke-width="5" stroke-linecap="round"/>
<path d="M30 56 l-6 -4 l2 8z M98 56 l6 -4 l-2 8z" fill="#FF6F91" {W(1.8)}/>
<rect x="38" y="28" width="52" height="46" rx="8" fill="#FFE7A8" {s()}/>
<rect x="38" y="28" width="52" height="10" rx="5" fill="#E9A44A" {W(2)}/>
''' + face(64, 54, d=10, k=0.75) + f'''
<path d="M20 74 H108 L100 108 Q98 114 90 114 H38 Q30 114 28 108Z" fill="#FFFFFF" {s()}/>
<path d="M22 80 Q44 72 64 80 Q84 88 106 80" fill="none" stroke="#F3E5C9" stroke-width="4"/>
<path d="M34 114 l-4 8 M94 114 l4 8" {W(3.5)}/>
<path d="M70 86 H92 L88 94 H74Z" fill="#7FC4F5" {W(2)}/>
<path d="M80 86 V72" {W(2)}/>
<path d="M81 72 Q90 76 82 84Z" fill="#6A3A62" {W(1.6)}/>''' + sparkle(108, 30, 4) + sparkle(18, 32, 3))

# 7. Мэджик Лэнд — малыш в колпаке волшебника съезжает по мармеладной горке-спирали
add("cafe-magic-land-okskaya",
    "горка-спираль из полосатого мармелада",
    "по ней со смехом съезжает малыш в синем колпаке волшебника со звёздами", "k11_candy", f'''
<rect x="84" y="20" width="12" height="96" rx="4" fill="#FFD3F0" {s()}/>
<path d="M90 26 Q40 30 42 48 Q46 62 90 60 Q120 62 104 78 Q86 92 44 90 Q20 92 22 112"
 fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M90 26 Q40 30 42 48 Q46 62 90 60 Q120 62 104 78 Q86 92 44 90 Q20 92 22 112"
 fill="none" stroke="#FF7FB6" stroke-width="11" stroke-linecap="round"/>
<path d="M90 26 Q40 30 42 48 Q46 62 90 60 Q120 62 104 78 Q86 92 44 90 Q20 92 22 112"
 fill="none" stroke="#FFF2A0" stroke-width="4" stroke-dasharray="7 9" stroke-linecap="round"/>
<circle cx="56" cy="78" r="11" fill="#FFD7B8" {s()}/>
<path d="M44 72 L60 46 L68 72Z" fill="#4B5BC8" {s()}/>
''' + sparkle(58, 60, 3.5, "#FFE48A") + eye(52, 78, 0.5) + eye(60, 78, 0.5) + f'''
<path d="M52 84 Q56 88 60 84" fill="none" {W(2)}/>
<path d="M66 82 l10 -6 M46 84 l-8 -4" {W(3)}/>''' + sparkle(18, 28, 5) + sparkle(112, 106, 4) + sparkle(30, 60, 3))

# 8. Пикочино (piccolo — «маленький») — крошечная пицца-малышка спит в спичечном коробке-кроватке
add("cafe-pikochino-dmitrovskoe",
    "крошечная круглая пицца-малышка с листиком базилика на макушке",
    "сладко спит в кроватке из спичечного коробка под одеялом-салфеткой в клеточку, над ней плывут «з-з-з»", "k11_nursery", f'''
<rect x="16" y="66" width="96" height="34" rx="4" fill="#F6E1B9" {s()}/>
<rect x="16" y="66" width="96" height="8" fill="#E7C996" {W(2)}/>
<path d="M18 100 l-2 10 M110 100 l2 10" {W(3.5)}/>
<circle cx="42" cy="64" r="16" fill="#F7C46B" {s()}/>
<circle cx="42" cy="64" r="11" fill="#E8573F"/>
<circle cx="38" cy="60" r="2.4" fill="#FFF3C9"/><circle cx="47" cy="66" r="2.2" fill="#FFF3C9"/>
<path d="M42 48 Q48 40 54 44 Q48 50 42 48Z" fill="#4FB06A" {W(1.8)}/>
<path d="M35 64 Q38 66 41 64 M44 64 Q47 66 50 64" fill="none" {W(2)}/>
<path d="M50 70 H112 V92 H50Z" fill="#FFFFFF" {s()}/>
''' + "".join(f'<path d="M{x} 70 V92" stroke="#F08AA8" stroke-width="3"/>' for x in (62, 76, 90, 104)) + f'''
<path d="M50 80 H112" stroke="#F08AA8" stroke-width="3"/>
<path d="M66 36 h8 l-8 8 h8 M82 22 h10 l-10 10 h10 M100 10 h6 l-6 6 h6" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>''')

# 9. Старлайт Дайнер — бургер-официант на роликах везёт на подносе панкейки под неоновой звездой
add("cafe-starlite-korovy-val",
    "бургер-официант в бумажной пилотке на розовых роликах",
    "лихо катит по чёрно-белому шахматному полу дайнера с подносом панкейков под неоновой звездой", "k11_neon", f'''
<path d="M64 6 L70 20 L85 20 L73 29 L78 44 L64 35 L50 44 L55 29 L43 20 L58 20Z" fill="none" stroke="#FF5FD2" stroke-width="3.5" stroke-linejoin="round"/>
<path d="M64 6 L70 20 L85 20 L73 29 L78 44 L64 35 L50 44 L55 29 L43 20 L58 20Z" fill="none" stroke="#FFE1F7" stroke-width="1.2" stroke-linejoin="round"/>
''' + "".join(f'<rect x="{x}" y="{y}" width="16" height="12" fill="{"#F4F4F8" if (x//16 + y//12) % 2 else "#2A2340"}"/>'
              for x in range(-4, 132, 16) for y in (106, 118)) + f'''
<path d="M38 72 Q38 50 62 50 Q86 50 86 72Z" fill="#F2A54A" {s()}/>
<circle cx="52" cy="58" r="1.6" fill="#FFF3C9"/><circle cx="64" cy="55" r="1.6" fill="#FFF3C9"/><circle cx="74" cy="60" r="1.6" fill="#FFF3C9"/>
<path d="M50 52 L62 42 L74 52Z" fill="#fff" {W(2)}/>
<path d="M36 72 Q48 78 60 72 Q72 78 88 72 L88 76 H36Z" fill="#7BCB5C" {W(2)}/>
<rect x="36" y="76" width="52" height="8" rx="3" fill="#8A4B2E" {W(2)}/>
<path d="M38 84 H86 Q86 94 62 94 Q38 94 38 84Z" fill="#F2A54A" {s()}/>
''' + eye(54, 64, 0.5) + eye(70, 64, 0.5) + f'''<path d="M58 70 Q62 72 66 70" fill="none" {W(2)}/>
<path d="M86 80 L102 70" {W(3)}/>
<path d="M92 68 H118" {W(3)}/>
<ellipse cx="105" cy="64" rx="11" ry="3" fill="#F6C47A" {W(1.8)}/>
<ellipse cx="105" cy="59" rx="11" ry="3" fill="#F6C47A" {W(1.8)}/>
<path d="M102 55 Q105 50 108 55" fill="#FFE07A" {W(1.6)}/>
<path d="M52 94 V100 M72 94 V100" {W(3)}/>
<rect x="42" y="98" width="18" height="6" rx="3" fill="#FF8BC6" {W(2)}/>
<rect x="64" y="98" width="18" height="6" rx="3" fill="#FF8BC6" {W(2)}/>
<circle cx="46" cy="106" r="2.6" fill="#FFE07A" {W(1.4)}/><circle cx="56" cy="106" r="2.6" fill="#FFE07A" {W(1.4)}/>
<circle cx="68" cy="106" r="2.6" fill="#FFE07A" {W(1.4)}/><circle cx="78" cy="106" r="2.6" fill="#FFE07A" {W(1.4)}/>''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    path = os.path.join(OUT, "subjects.txt")
    lines = [l for l in open(path, encoding="utf-8").read().splitlines() if l.split(" — ")[0] not in ids]
    lines += [f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}" for pid in ids]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("ok", len(ids))
