"""Иконки робота creative, 13.11 (запуск 1113g). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1113g.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 «Этуаль» (балет с 3 лет, Дмитровское ш.): балерина с каре делает гранд-батман у зеркала
I["etual-dmitrovskoe"] = ("девочка-балерина в лиловой пачке со стрижкой каре",
    "держится за деревянную перекладину у высокого зеркала и выбрасывает ножку в высокий гранд-батман выше головы", bg("#E6FCF5", "#63E6BE", f'''
<rect x="78" y="8" width="44" height="112" rx="6" fill="#C5F6FA" {s()}/>
<path d="M88 20 L100 12 M86 36 L112 18" {ln("#fff", 3)}/>
<path d="M4 70 H124" {ln(O, 8)}/><path d="M4 70 H124" {ln("#C08552", 5)}/>
{limb(56, 84, 54, 116, SKIN, 5)}<path d="M50 116 h8 l-2 5 h-6Z" fill="#F783AC" {s('stroke-width="2"')}/>
{limb(60, 82, 92, 34, SKIN, 5)}<path d="M90 32 l6 -6 3 3 -5 6Z" fill="#F783AC" {s('stroke-width="2"')}/>
<path d="M34 80 Q58 66 82 78 Q60 92 34 80Z" fill="#B197FC" {s()}/>
<path d="M50 54 Q58 50 66 54 L64 78 H52Z" fill="#7950F2" {s()}/>
{limb(64, 58, 76, 70, SKIN, 3.5)}{limb(52, 58, 36, 46, SKIN, 3.5)}
<circle cx="58" cy="40" r="11" fill="{SKIN}" {s()}/>
<path d="M46 42 Q46 26 58 26 Q70 26 70 42 L66 40 Q66 32 58 32 Q50 32 50 40Z" fill="#343A40" {s('stroke-width="2.2"')}/>
{eye(54, 41, 0.5)}{eye(62, 41, 0.5)}<path d="M55 47 Q58 49 61 47" fill="none" {s('stroke-width="1.6"')}/>
{sparkle(108, 100, 5)}
'''))

# 2 Театральная студия ДМТЮА (актёрское, вокал, хор, 4–17 лет, Цветной бульвар): Пьеро поёт на краю сцены
I["dmtya-studio-tsvetnoy"] = ("кукла-Пьеро в белом балахоне с длинными рукавами и чёрными помпонами",
    "сидит, свесив ноги, на краю маленькой сцены с огоньками рампы и поёт песенку, раскинув рукава", bg("#4C1D95", "#1E1036", f'''
<path d="M0 0 H40 Q30 50 34 92 H0Z" fill="#C2255C" {s()}/><path d="M128 0 H88 Q98 50 94 92 H128Z" fill="#C2255C" {s()}/>
<rect x="-4" y="90" width="136" height="40" fill="#8D5524" {s()}/>
<circle cx="20" cy="96" r="3" fill="#FFE066"/><circle cx="44" cy="96" r="3" fill="#FFE066"/><circle cx="84" cy="96" r="3" fill="#FFE066"/><circle cx="108" cy="96" r="3" fill="#FFE066"/>
{limb(56, 88, 52, 112, "#F8F9FA", 7)}{limb(70, 88, 74, 112, "#F8F9FA", 7)}
<path d="M46 56 Q64 48 82 56 L86 92 H42Z" fill="#F8F9FA" {s()}/>
<circle cx="64" cy="66" r="3" fill="#212529"/><circle cx="64" cy="78" r="3" fill="#212529"/>
<path d="M48 60 Q30 54 22 40 L30 36 Q38 48 50 52Z" fill="#F8F9FA" {s()}/>
<path d="M80 60 Q98 54 106 40 L98 36 Q90 48 78 52Z" fill="#F8F9FA" {s()}/>
<circle cx="64" cy="38" r="13" fill="#FFFFFF" {s()}/>
<path d="M51 34 Q64 18 77 34 Q64 28 51 34Z" fill="#212529" {s('stroke-width="2"')}/>
{eye(59, 38, 0.55)}{eye(69, 38, 0.55)}
<path d="M59 43 l0 5 M69 43 l0 5" stroke="#4DABF7" stroke-width="1.6" stroke-linecap="round"/>
<ellipse cx="64" cy="47" rx="3" ry="3.5" fill="#C92A2A"/>
{note(104, 24, 0.7, "#FFE066")}{note(22, 22, 0.6, "#FFE066")}
'''))

# 3 «Домик художника» (рисование 4–12 лет «От сказки к шедевру», керамика): малыш в огромном берете рисует кита
I["domik-hudozhnika-fabritsiusa"] = ("малыш в огромном красном берете, сползающем на брови",
    "рисует гуашью на мольберте синего кита, а нарисованный кит подмигивает ему с холста и пускает фонтанчик", bg("#FFF9DB", "#FFD43B", f'''
<path d="M70 120 L84 30 M114 120 L100 30 M92 30 V122" {ln(O, 6)}/><path d="M70 120 L84 30 M114 120 L100 30" {ln("#A0522D", 3)}/>
<rect x="66" y="22" width="56" height="54" rx="3" fill="#fff" {s()}/>
<path d="M74 58 Q78 40 96 42 Q112 44 112 56 Q112 66 96 66 Q80 66 74 58Z" fill="#339AF0" {s('stroke-width="2.2"')}/>
<path d="M74 58 l-6 -6 2 10Z" fill="#339AF0" {s('stroke-width="2"')}/>
<path d="M98 42 Q96 32 92 30 M98 42 Q100 32 106 30" fill="none" {ln("#74C0FC", 2.4)}/>
<path d="M100 52 q3 -3 6 0" fill="none" {s('stroke-width="1.8"')}/><circle cx="92" cy="52" r="1.6" fill="{O}"/>
<rect x="66" y="74" width="56" height="5" fill="#A0522D" {s('stroke-width="2"')}/>
<path d="M22 122 Q24 90 40 86 Q56 90 58 122Z" fill="#FAB005" {s()}/>
{limb(50, 94, 68, 62, SKIN, 4)}<path d="M68 62 L74 54" {ln(O, 3)}/><circle cx="75" cy="52" r="3" fill="#339AF0" {s('stroke-width="1.6"')}/>
<circle cx="40" cy="70" r="15" fill="{SKIN}" {s()}/>
{eye(35, 72, 0.6)}{eye(45, 72, 0.6)}<path d="M36 79 Q40 82 44 79" fill="none" {s('stroke-width="1.8"')}/>
<path d="M18 62 Q16 42 40 44 Q64 44 62 62 Q40 54 18 62Z" fill="#E03131" {s()}/>
<path d="M40 44 l-2 -6" {ln(O, 3)}/>
'''))

# 4 «Чудо цвета» (Дмитров, лепка из пластилина и глины 3–7 лет): пластилиновая гусеница на дощечке со стекой
I["chudo-tsveta-dmitrov"] = ("пластилиновая гусеница из шести разноцветных шариков",
    "только что вылеплена и ползёт по дощечке для лепки мимо деревянной стеки, гордо подняв улыбающуюся голову с усиками", bg("#F3F0FF", "#B197FC", f'''
<path d="M6 92 L122 92 L114 120 L14 120Z" fill="#FFE8CC" {s()}/>
<path d="M20 100 H108" stroke="#F4C38E" stroke-width="2"/>
<path d="M20 112 L92 104" {ln(O, 7)}/><path d="M20 112 L92 104" {ln("#C08552", 4)}/>
<circle cx="24" cy="86" r="9" fill="#40C057" {s()}/><circle cx="40" cy="80" r="10" fill="#FAB005" {s()}/>
<circle cx="57" cy="78" r="10" fill="#E64980" {s()}/><circle cx="74" cy="80" r="10" fill="#228BE6" {s()}/>
<circle cx="90" cy="76" r="10" fill="#FD7E14" {s()}/>
<circle cx="100" cy="54" r="16" fill="#FF6B6B" {s()}/>
{face(100, 55, 10, 0.7)}
<path d="M94 40 l-6 -14 M106 40 l6 -14" {ln(O, 2.4)}/><circle cx="87" cy="24" r="4" fill="#FAB005" {s('stroke-width="1.8"')}/><circle cx="113" cy="24" r="4" fill="#FAB005" {s('stroke-width="1.8"')}/>
<path d="M30 70 l-2 -6 M48 68 l0 -6 M66 66 l2 -6" {ln(O, 2)}/>
{sparkle(30, 34, 6)}{sparkle(56, 22, 4)}
'''))

# 5 «Динамо Чехов» (танцы для детей с 6 лет, актёрское мастерство): мальчик в бабочке танцует на стуле
I["dinamo-dance-chekhov"] = ("мальчик в синей бабочке и сером жилете",
    "сидит верхом на венском стуле посреди сцены и отбивает ритм ладошками по коленкам, вскинув одну ногу в сторону", bg("#FFE3E3", "#FF8787", f'''
<ellipse cx="64" cy="118" rx="44" ry="8" fill="#C92A2A" opacity=".35"/>
<path d="M40 70 V118 M84 70 V118" {ln(O, 6)}/><path d="M40 70 V118 M84 70 V118" {ln("#5C3317", 3)}/>
<path d="M36 72 Q62 78 88 72 L86 66 Q62 72 38 66Z" fill="#8B5A2B" {s()}/>
<path d="M44 40 Q38 20 62 20 Q86 20 80 40" fill="none" {ln(O, 6)}/><path d="M44 40 Q38 20 62 20 Q86 20 80 40" fill="none" {ln("#8B5A2B", 3)}/>
{limb(54, 70, 48, 100, "#343A40", 6)}<path d="M42 100 h10 v5 h-12Z" fill="#212529" {s('stroke-width="2"')}/>
{limb(70, 70, 106, 58, "#343A40", 6)}<path d="M106 54 l8 2 -2 6 -8 -1Z" fill="#212529" {s('stroke-width="2"')}/>
<path d="M50 44 Q62 40 74 44 L76 72 H48Z" fill="#fff" {s()}/>
<path d="M50 44 L58 72 H48Z M74 44 L66 72 H76Z" fill="#868E96" {s('stroke-width="2.2"')}/>
<path d="M56 46 l6 4 6 -4 v8 l-6 -4 -6 4Z" fill="#1971C2" {s('stroke-width="2"')}/>
{limb(52, 50, 44, 72, SKIN, 3.5)}{limb(72, 50, 76, 72, SKIN, 3.5)}
{head(62, 30, 12, "#5C3317", 0.55)}
<path d="M26 64 l-6 -4 M24 74 h-8 M98 80 l6 4" {ln("#FFF", 2.4)}/>
'''))

# 7 Sing & Play (Хорошёвское ш.: инструменты и вокал для детей от 4 лет): кларнет наискосок выдувает ноты-бусины
I["sing-play-khoroshevskoe"] = ("чёрный кларнет с серебряными клапанами и мордашкой на раструбе",
    "стоит наискосок раструбом вверх и выдувает цепочку разноцветных нот-бусин, которые улетают к облаку", bg("#E7F5FF", "#4DABF7", f'''
<ellipse cx="100" cy="26" rx="22" ry="10" fill="#fff"/><ellipse cx="86" cy="30" rx="12" ry="8" fill="#fff"/>
<path d="M26 112 L76 42" {ln(O, 18)}/><path d="M26 112 L76 42" {ln("#212529", 14)}/>
<path d="M22 118 L30 106" {ln(O, 8)}/><path d="M22 118 L30 106" {ln("#ADB5BD", 5)}/>
<g fill="#DEE2E6" stroke="{O}" stroke-width="1.4"><circle cx="40" cy="92" r="3.5"/><circle cx="48" cy="81" r="3.5"/><circle cx="56" cy="70" r="3.5"/><circle cx="64" cy="59" r="3.5"/></g>
<path d="M44 96 L58 76 M52 85 L66 65" stroke="#DEE2E6" stroke-width="1.6"/>
<path d="M68 48 Q70 30 86 30 Q96 44 84 58 Q76 56 68 48Z" fill="#212529" {s()}/>
<ellipse cx="84" cy="40" rx="6" ry="9" fill="#495057" transform="rotate(40 84 40)"/>
{eye(74, 50, 0.45)}{eye(80, 54, 0.45)}
<circle cx="96" cy="60" r="5" fill="#F03E3E" {s('stroke-width="2"')}/><circle cx="108" cy="70" r="5" fill="#FAB005" {s('stroke-width="2"')}/>
<circle cx="112" cy="86" r="5" fill="#40C057" {s('stroke-width="2"')}/><circle cx="104" cy="100" r="5" fill="#7048E8" {s('stroke-width="2"')}/>
{note(102, 48, 0.6, O)}
'''))

# 8 E.M. Dance (эстрадный танец и акробатика 3–18 лет, Волоколамское ш.): девочка делает колесо со шлейфом блёсток
I["em-dance-volokolamskoe"] = ("девочка-гимнастка в блестящем малиновом трико с хвостиком",
    "крутит колесо поперёк эстрадной сцены вверх ногами, а за ней по дуге тянется шлейф золотых блёсток", bg("#FFF4E6", "#FFA94D", f'''
<rect x="-4" y="104" width="136" height="28" fill="#5F3DC4" {s()}/>
<path d="M14 100 Q30 40 64 30" fill="none" stroke="#FFD43B" stroke-width="5" stroke-dasharray="1 7" stroke-linecap="round"/>
<path d="M20 96 Q34 52 60 40" fill="none" stroke="#FFF3BF" stroke-width="3" stroke-dasharray="1 9" stroke-linecap="round"/>
{limb(58, 76, 36, 102, SKIN, 5)}{limb(70, 76, 94, 102, SKIN, 5)}
{limb(58, 52, 40, 26, SKIN, 5)}{limb(70, 52, 92, 24, SKIN, 5)}
<path d="M54 48 Q64 44 74 48 L76 80 Q64 84 52 80Z" fill="#D6336C" {s()}/>
<circle cx="60" cy="58" r="1.6" fill="#fff"/><circle cx="68" cy="66" r="1.6" fill="#fff"/><circle cx="62" cy="72" r="1.6" fill="#fff"/>
<circle cx="64" cy="96" r="11" fill="{SKIN}" {s()}/>
<path d="M53 98 Q54 108 64 108 Q74 108 75 98 Q64 104 53 98Z" fill="#7F4F24" {s('stroke-width="2"')}/>
<path d="M64 108 Q60 118 66 124" fill="none" {ln("#7F4F24", 5)}/>
<g transform="rotate(180 64 94)">{eye(60, 94, 0.45)}{eye(68, 94, 0.45)}<path d="M61 99 Q64 101 67 99" fill="none" {s('stroke-width="1.6"')}/></g>
{sparkle(104, 40, 6, "#FFD43B")}{sparkle(26, 30, 4)}
'''))

# 9 Starset (Клин: вокал для детей с 6 лет, гитара, фортепиано, скрипка): скрипка играет под созвездием-нотой
I["starset-klin"] = ("рыжая скрипка-девочка с двумя косичками из завитков грифа",
    "играет смычком на ночной крыше-коньке, а звёзды над ней сами соединяются линиями в большую ноту", bg("#364FC7", "#0B1A4A", f'''
<path d="M-4 128 L40 98 L84 128Z" fill="#495057" {s()}/><path d="M60 128 L100 100 L132 124 V128Z" fill="#343A40" {s()}/>
<circle cx="86" cy="24" r="3" fill="#FFF"/><circle cx="106" cy="20" r="3" fill="#FFF"/><circle cx="104" cy="44" r="3" fill="#FFF"/>
<circle cx="84" cy="48" r="4" fill="#FFF"/><circle cx="92" cy="54" r="3" fill="#FFF"/>
<path d="M86 24 L106 20 L104 44 M86 24 L84 48 L92 54 L104 44" fill="none" stroke="#FFF3BF" stroke-width="1.4" opacity=".8"/>
<path d="M30 52 Q20 52 22 66 Q16 76 26 90 Q34 102 46 100 Q60 102 64 90 Q72 78 64 66 Q66 52 56 52 Q48 48 42 52 Q36 48 30 52Z" fill="#E8590C" {s()}/>
<path d="M36 70 q-3 4 0 8 M54 70 q3 4 0 8" fill="none" {ln(O, 2.4)}/>
<path d="M44 54 L50 18" {ln(O, 8)}/><path d="M44 54 L50 18" {ln("#212529", 5)}/>
<path d="M50 18 q-8 -6 -4 -12 q6 -2 6 6 M50 18 q8 -4 10 -12 q-6 -4 -8 4" fill="none" {ln(O, 2.6)}/>
<path d="M46 84 L48 98" {ln("#212529", 3)}/>
{eye(38, 64, 0.5)}{eye(50, 64, 0.5)}<path d="M41 86 Q44 89 47 86" fill="none" {s('stroke-width="1.6"')}/>
<path d="M12 40 L80 94" {ln(O, 4)}/><path d="M12 40 L80 94" {ln("#F1E3C3", 2)}/>
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
