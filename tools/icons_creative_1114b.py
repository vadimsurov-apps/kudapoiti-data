"""Иконки робота creative, 14.11 (запуск 1114b). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1114b.py [--subjects] [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# «Баня», Чертаново: толстая кисть в войлочной банной шапке рисует на холсте волну
I["banya-chertanovo"] = ("толстая круглая кисть с мордашкой в войлочной банной шапке-колпаке",
    "распаренная, рисует на холсте-мольберте синюю волну, а над шапкой вьётся облачко пара",
    bg("#E7F5FF", "#4DABF7", f'''
<rect x="62" y="34" width="54" height="64" rx="3" fill="#fff" {s()}/>
<path d="M66 80 Q76 64 86 78 Q96 92 108 74" fill="none" {ln("#1971C2", 7)}/>
<path d="M68 92 Q80 84 92 92" fill="none" {ln("#74C0FC", 5)}/>
<path d="M70 98 L64 124 M108 98 L114 124" {ln("#8D6E63", 4)}/>
<path d="M30 118 L46 66" {ln(O, 14)}/><path d="M30 118 L46 66" {ln("#C08552", 10)}/>
<path d="M40 70 L54 74 L52 82 L38 78Z" fill="#ADB5BD" {s()}/>
<path d="M44 74 Q30 54 40 38 Q56 30 66 44 Q70 60 54 78Z" fill="#1971C2" {s()}/>
<path d="M50 74 Q58 72 64 80 Q60 86 54 84Z" fill="#1971C2" {s('stroke-width="2"')}/>
{eye(47, 58, 0.6)}{eye(57, 60, 0.6)}<path d="M48 66 Q52 70 56 67" fill="none" {s('stroke-width="1.8"')}/>
<ellipse cx="44" cy="64" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/>
<path d="M30 46 Q30 22 50 18 Q70 20 70 44 Q50 36 30 46Z" fill="#F1E3C6" {s()}/>
<path d="M30 46 Q50 34 70 44 L70 50 Q50 40 30 52Z" fill="#E0C9A0" {s('stroke-width="2.2"')}/>
<path d="M50 18 L52 8" {ln(O, 3)}/>
<path d="M58 12 q-4 -6 2 -10 q6 -4 2 -10" fill="none" {ln("#fff", 3)}/>
<path d="M68 18 q-4 -6 2 -10" fill="none" {ln("#fff", 3)}/>
'''))

# Академия детского мюзикла: нотка-восьмушка в балетной юбочке поёт в микрофон перед занавесом
I["adm-zhukovskogo"] = ("толстенькая чёрная нотка-восьмушка в розовой балетной юбочке с мордашкой",
    "поёт в серебряный микрофон и делает танцевальный шаг на краю сцены перед красным занавесом с золотой бахромой",
    bg("#FFE3E3", "#C92A2A", f'''
<path d="M-4 -4 H132 V22 Q100 34 64 22 Q28 34 -4 22Z" fill="#E03131" {s()}/>
<path d="M-4 22 Q28 34 64 22 Q100 34 132 22" fill="none" {ln("#FCC419", 4)}/>
<path d="M-4 30 V108 M12 30 V108 M116 30 V108 M132 30 V108" {ln("#A61E4D", 10)}/>
<rect x="-4" y="104" width="136" height="28" fill="#5F3DC4" {s()}/>
<path d="M-4 110 H132" {ln("#9775FA", 2)}/>
<path d="M72 26 V74" {ln(O, 7)}/>
<path d="M72 26 Q96 34 92 56 Q88 42 72 40" fill="#212529" {s()}/>
<ellipse cx="56" cy="76" rx="20" ry="16" fill="#212529" {s()} transform="rotate(-18 56 76)"/>
<path d="M32 86 Q56 72 80 86 Q84 96 76 96 Q56 90 36 96 Q28 96 32 86Z" fill="#FF8CC6" {s()}/>
<path d="M40 92 l2 4 M52 90 l1 5 M64 90 l-1 5 M74 92 l-2 4" {ln("#E64980", 1.6)}/>
{eye(50, 72, 0.6)}{eye(62, 70, 0.6)}<ellipse cx="56" cy="80" rx="3.4" ry="2.6" fill="#FF8787" {s('stroke-width="1.4"')}/>
<path d="M46 96 L40 104 M66 96 L74 100" {ln(O, 3)}/>
<path d="M34 102 h10 v3 h-10Z M72 98 l8 -2 1 3 -8 2Z" fill="#FF8CC6" {s('stroke-width="1.6"')}/>
<path d="M36 70 L24 60" {ln(O, 3)}/>
<rect x="14" y="48" width="12" height="14" rx="6" fill="#CED4DA" {s('stroke-width="2.2"')} transform="rotate(-38 20 55)"/>
{note(104, 70, 0.7, "#FCC419")}{note(112, 50, 0.55, "#FFE066")}{sparkle(30, 40, 4, "#FFE066")}
'''))

# «Актёр и Ко»: картонная корона-артист стоит на табурете в круге прожектора
I["akter-i-ko-shabolovka"] = ("картонная театральная корона с жёлтыми зубцами, цветными «самоцветами» из фольги и мордашкой",
    "стоит на деревянном табурете в круге прожектора посреди сцены и важно раскланивается, а сзади зелёный бархатный занавес",
    bg("#D3F9D8", "#2B8A3E", f'''
<path d="M-4 -4 H40 Q34 50 44 112 H-4Z M132 -4 H88 Q94 50 84 112 H132Z" fill="#2F9E44" {s()}/>
<path d="M12 0 Q8 56 16 112 M26 0 Q22 56 32 112 M116 0 Q120 56 112 112 M102 0 Q106 56 96 112" fill="none" {ln("#1B5E20", 3)}/>
<path d="M50 -4 L28 106 H100 L78 -4Z" fill="#FFF9DB" opacity=".55"/>
<rect x="-4" y="104" width="136" height="28" fill="#A47148" {s()}/>
<ellipse cx="64" cy="106" rx="34" ry="6" fill="#FFF3BF" opacity=".8"/>
<rect x="44" y="80" width="40" height="8" rx="2" fill="#C08552" {s()}/>
<path d="M50 88 L46 108 M78 88 L82 108" {ln("#8D6E63", 5)}/>
<path d="M38 78 L36 40 L48 54 L56 32 L64 50 L72 32 L80 54 L92 40 L90 78Z" fill="#FCC419" {s()}/>
<circle cx="36" cy="40" r="4" fill="#E03131" {s('stroke-width="2"')}/><circle cx="56" cy="32" r="4" fill="#4DABF7" {s('stroke-width="2"')}/>
<circle cx="72" cy="32" r="4" fill="#40C057" {s('stroke-width="2"')}/><circle cx="92" cy="40" r="4" fill="#E03131" {s('stroke-width="2"')}/>
<path d="M38 70 H90" {ln("#F08C00", 2.4)}/>
{face(64, 60, 9, 0.7)}
'''))

# Active Style, Уральская (эстрадный танец 5–7 и 8–11, хип-хоп 12–15): девочка в серебристом костюме делает «звёздочку»
I["active-style-uralskaya"] = ("кудрявая рыжая девочка в серебристом эстрадном костюме с бахромой",
    "в прыжке раскинула руки и ноги «звёздочкой» над сценой, а по краю сцены горят пять круглых огней рампы",
    bg("#E5DBFF", "#5F3DC4", f'''
<rect x="-4" y="102" width="136" height="30" fill="#343A40" {s()}/>
{''.join(f'<circle cx="{x}" cy="104" r="5" fill="#FFD43B" {s("stroke-width=\"2\"")}/>' for x in (16, 40, 64, 88, 112))}
{limb(56, 54, 30, 30, SKIN, 5)}{limb(72, 54, 98, 30, SKIN, 5)}
{limb(58, 78, 40, 98, SKIN, 6)}{limb(70, 78, 88, 98, SKIN, 6)}
<path d="M34 98 h10 l-2 5 h-10Z M84 98 h10 l2 5 h-10Z" fill="#CED4DA" {s('stroke-width="1.8"')}/>
<path d="M52 50 Q64 44 76 50 L78 80 Q64 86 50 80Z" fill="#DEE2E6" {s()}/>
<path d="M50 80 l2 6 M56 82 l1 6 M62 83 l0 6 M68 83 l0 6 M74 82 l-1 6 M78 80 l-2 6" {ln("#ADB5BD", 2)}/>
<path d="M56 58 l3 3 M66 64 l3 -3 M60 72 l2 2" {ln("#fff", 2)}/>
<circle cx="64" cy="34" r="13" fill="{SKIN}" {s()}/>
<path d="M51 32 Q48 18 58 16 Q62 10 70 14 Q80 14 80 26 Q84 34 77 36 Q76 26 64 24 Q54 26 52 34Z" fill="#E8590C" {s('stroke-width="2.4"')}/>
<circle cx="50" cy="26" r="5" fill="#E8590C" {s('stroke-width="2"')}/><circle cx="79" cy="22" r="5" fill="#E8590C" {s('stroke-width="2"')}/>
{eye(59, 35, 0.55)}{eye(69, 35, 0.55)}<path d="M60 41 Q64 45 68 41" fill="none" {s('stroke-width="1.8"')}/>
{sparkle(22, 20, 5)}{sparkle(108, 18, 4)}{sparkle(104, 60, 3)}
'''))

# «Джем», Щукино: банка клубничного джема раскланивается в луче прожектора
I["jam-aviatsionnaya"] = ("стеклянная банка клубничного джема с мордашкой и крышкой в красный горошек",
    "раскланивается в луче прожектора на сцене между половинками синего занавеса, к её ногам летит ромашка",
    bg("#DBE4FF", "#364FC7", f'''
<path d="M-4 -4 H34 Q28 50 36 110 H-4Z M132 -4 H94 Q100 50 92 110 H132Z" fill="#3B5BDB" {s()}/>
<path d="M10 0 Q6 56 14 110 M118 0 Q122 56 114 110" fill="none" {ln("#233A9E", 3)}/>
<path d="M54 -4 L36 104 H92 L74 -4Z" fill="#FFF9DB" opacity=".5"/>
<rect x="-4" y="102" width="136" height="30" fill="#8D6E63" {s()}/>
<path d="M44 46 Q42 38 50 38 H78 Q86 38 84 46 L86 94 Q86 104 76 104 H52 Q42 104 42 94Z" fill="#E03131" {s()}/>
<path d="M48 52 Q48 46 54 46" fill="none" {ln("#fff", 3)}/>
<rect x="46" y="58" width="36" height="22" rx="4" fill="#FFF9DB" {s('stroke-width="2.2"')}/>
{eye(57, 67, 0.55)}{eye(71, 67, 0.55)}<path d="M59 74 Q64 78 69 74" fill="none" {s('stroke-width="1.8"')}/>
<rect x="44" y="28" width="40" height="11" rx="3" fill="#fff" {s()}/>
<circle cx="52" cy="33" r="2.2" fill="#E03131"/><circle cx="62" cy="33" r="2.2" fill="#E03131"/><circle cx="72" cy="33" r="2.2" fill="#E03131"/><circle cx="80" cy="33" r="2" fill="#E03131"/>
<path d="M54 28 Q64 18 74 28" fill="none" {ln("#F59F00", 2.4)}/>
<circle cx="104" cy="86" r="6" fill="#FCC419" {s('stroke-width="2"')}/>
{''.join(f'<ellipse cx="{104 + 9 * c}" cy="{86 + 9 * d}" rx="4" ry="2.6" fill="#fff" {s("stroke-width=\"1.4\"")} transform="rotate({a} {104 + 9 * c} {86 + 9 * d})"/>' for c, d, a in ((1, 0, 0), (-1, 0, 0), (0, 1, 90), (0, -1, 90)))}
<circle cx="104" cy="86" r="5" fill="#FCC419" {s('stroke-width="1.6"')}/>
'''))

# «Живописная», Щукинская (группы 3–5, 6–7, 8–9 лет): три кисти разного роста рисуют радугу
I["zhivopisnaya-marshala-novikova"] = ("три кисточки-сестрички разного роста с мордашками — маленькая, средняя и большая",
    "встали лесенкой на краю бумажного листа и вместе ведут по нему три полосы радуги — красную, жёлтую и голубую",
    bg("#FFF9DB", "#FAB005", f'''
<path d="M-4 96 L132 70 L132 132 H-4Z" fill="#fff" {s()}/>
<path d="M-4 92 Q50 40 132 56" fill="none" {ln("#FA5252", 9)}/>
<path d="M-4 104 Q50 54 132 68" fill="none" {ln("#FCC419", 9)}/>
<path d="M-4 116 Q50 68 132 80" fill="none" {ln("#4DABF7", 9)}/>
<rect x="18" y="70" width="12" height="30" rx="5" fill="#F06595" {s()}/>
<path d="M18 70 Q24 58 30 70Z" fill="#FA5252" {s('stroke-width="2"')}/>
{eye(22, 82, 0.45)}{eye(27, 82, 0.45)}
<rect x="54" y="44" width="13" height="40" rx="5" fill="#20C997" {s()}/>
<path d="M54 44 Q60 28 67 44Z" fill="#FCC419" {s('stroke-width="2"')}/>
{eye(58, 58, 0.5)}{eye(64, 58, 0.5)}<path d="M58 65 Q61 68 64 65" fill="none" {s('stroke-width="1.6"')}/>
<rect x="94" y="16" width="15" height="52" rx="6" fill="#7950F2" {s()}/>
<path d="M94 16 Q101 -2 109 16Z" fill="#4DABF7" {s('stroke-width="2"')}/>
{eye(98, 34, 0.55)}{eye(105, 34, 0.55)}<path d="M98 42 Q101.5 45 105 42" fill="none" {s('stroke-width="1.6"')}/>
<path d="M94 52 h15 M54 72 h13" {ln("#ADB5BD", 3)}/>
'''))

# Академия балета Таранды: балетная пачка-«тарелка» с мордашкой крутит фуэте на одной пуанте
I["taranda-denisovsky"] = ("белоснежная классическая балетная пачка-«тарелка» с мордашкой на корсаже",
    "крутит фуэте на одной розовой пуанте, как юла, — вокруг завиваются серебряные линии вращения, сверху горит хрустальная люстра",
    bg("#F3F0FF", "#9775FA", f'''
<path d="M64 -4 V10" {ln(O, 2.4)}/>
<path d="M50 10 H78 L72 22 H56Z" fill="#FFE066" {s('stroke-width="2"')}/>
<path d="M54 22 l-2 6 M64 22 v7 M74 22 l2 6" {ln("#A5D8FF", 2)}/>
<path d="M18 74 Q64 52 110 74" fill="none" {ln("#fff", 3)}/>
<path d="M24 86 Q64 104 104 86" fill="none" {ln("#fff", 3)}/>
<path d="M50 40 Q64 34 78 40 L76 66 H52Z" fill="#FFDEEB" {s()}/>
<path d="M56 40 Q64 46 72 40" fill="none" {ln("#F783AC", 2)}/>
<path d="M14 72 Q64 54 114 72 Q118 78 108 80 Q64 90 20 80 Q10 78 14 72Z" fill="#fff" {s()}/>
<path d="M22 76 Q40 72 46 80 M56 82 Q64 74 72 82 M82 80 Q90 72 106 76" fill="none" {ln("#DEE2E6", 2)}/>
{face(64, 52, 6, 0.55)}
<path d="M64 84 L62 110" {ln(O, 9)}/><path d="M64 84 L62 110" {ln("#FFC9DE", 6)}/>
<path d="M57 108 Q62 120 67 108Z" fill="#F783AC" {s('stroke-width="2"')}/>
<path d="M60 96 L68 100 M60 102 L68 98" {ln("#F783AC", 1.6)}/>
{sparkle(26, 40, 4)}{sparkle(104, 40, 5)}{sparkle(96, 110, 3)}
'''))

# «Мир искусства», Тургеневская (живопись, скульптура малых форм): пластилиновый жирафик на скульпторской подставке
I["mir-iskusstva-ogorodnaya"] = ("оранжевый пластилиновый жирафик с коричневыми пятнышками и мордашкой",
    "стоит на круглой вращающейся подставке скульптора, а рядом в стакане с водой ждут две кисти и деревянная стека",
    bg("#E6FCF5", "#0CA678", f'''
<ellipse cx="54" cy="110" rx="34" ry="9" fill="#868E96" {s()}/>
<rect x="48" y="100" width="12" height="10" fill="#495057" {s('stroke-width="2"')}/>
<ellipse cx="54" cy="100" rx="30" ry="7" fill="#DEE2E6" {s()}/>
<path d="M40 98 L40 74 M50 98 V76 M60 98 V76 M70 98 V74" {ln(O, 7)}/><path d="M40 98 L40 74 M50 98 V76 M60 98 V76 M70 98 V74" {ln("#FF922B", 4)}/>
<ellipse cx="55" cy="72" rx="20" ry="11" fill="#FF922B" {s()}/>
<path d="M66 66 L72 30" {ln(O, 13)}/><path d="M66 66 L72 30" {ln("#FF922B", 9)}/>
<ellipse cx="78" cy="26" rx="12" ry="8" fill="#FF922B" {s()}/>
<path d="M70 20 L68 12 M76 18 L76 10" {ln(O, 2.4)}/><circle cx="68" cy="11" r="2.4" fill="#8D4F2A"/><circle cx="76" cy="9" r="2.4" fill="#8D4F2A"/>
{eye(76, 25, 0.5)}{eye(84, 25, 0.5)}<path d="M80 30 Q83 32 86 30" fill="none" {s('stroke-width="1.6"')}/>
<circle cx="48" cy="70" r="3" fill="#8D4F2A"/><circle cx="60" cy="74" r="2.6" fill="#8D4F2A"/><circle cx="69" cy="48" r="2.2" fill="#8D4F2A"/>
<path d="M98 82 h20 l-2 30 h-16Z" fill="#D0EBFF" opacity=".9" {s()}/>
<path d="M100 96 h16" {ln("#74C0FC", 3)}/>
<path d="M104 92 L100 52" {ln(O, 5)}/><path d="M104 92 L100 52" {ln("#E64980", 3)}/><path d="M98 48 l2 -6 3 6Z" fill="#FCC419" {s('stroke-width="1.6"')}/>
<path d="M112 92 L118 58" {ln(O, 5)}/><path d="M112 92 L118 58" {ln("#C08552", 3)}/>
<path d="M110 92 L108 62" {ln(O, 4)}/><path d="M110 92 L108 62" {ln("#7950F2", 2.4)}/><circle cx="108" cy="60" r="2.6" fill="#7950F2" {s('stroke-width="1.4"')}/>
'''))

# «Баня», Свиблово: деревянный банный ковш льёт на лист радугу
I["banya-sviblovo"] = ("деревянный банный ковш с длинной ручкой, обручем-ободком и мордашкой",
    "наклонился над чистым листом и вместо воды выливает на него радугу из красок, а на листе расцветает цветок",
    bg("#FFF0F6", "#F06595", f"""
<rect x="10" y="80" width="108" height="44" rx="4" fill="#fff" {s()} transform="rotate(-6 64 102)"/>
<path d="M60 52 Q56 72 62 96" fill="none" {ln("#FA5252", 6)}/>
<path d="M66 54 Q62 74 70 96" fill="none" {ln("#FCC419", 6)}/>
<path d="M72 54 Q70 74 78 94" fill="none" {ln("#4DABF7", 6)}/>
<circle cx="70" cy="104" r="6" fill="#FCC419" {s('stroke-width="2"')}/>
{''.join(f'<circle cx="{70 + dx}" cy="{104 + dy}" r="5" fill="#F06595" {s("stroke-width=\"1.8\"")}/>' for dx, dy in ((9, 0), (-9, 0), (0, 9), (0, -9)))}
<circle cx="70" cy="104" r="5" fill="#FCC419" {s('stroke-width="1.8"')}/>
<path d="M76 30 L118 4" {ln(O, 12)}/><path d="M76 30 L118 4" {ln("#C08552", 8)}/>
<path d="M40 24 Q38 50 56 58 Q76 62 86 44 Q90 32 84 24Z" fill="#D9A066" {s()} transform="rotate(20 62 40)"/>
<path d="M42 32 L86 38" {ln("#8D6E63", 3)} transform="rotate(20 62 40)"/>
<ellipse cx="62" cy="24" rx="23" ry="7" fill="#8D6E63" {s()} transform="rotate(20 62 40)"/>
{eye(54, 44, 0.55)}{eye(65, 48, 0.55)}<path d="M55 52 Q59 56 63 54" fill="none" {s('stroke-width="1.8"')}/>
<ellipse cx="50" cy="50" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/>
"""))

# Active Style, ул. Лазо (хип-хоп 7–11): кактус в кепке задом наперёд пускает «волну»
I["active-style-lazo"] = ("зелёный колючий кактус в красном горшке и в синей кепке козырьком назад",
    "танцует хип-хоп: пускает «волну» по рукам-отросткам, подпрыгивая вместе с горшком на чёрном танцполе с граффити-стрелкой",
    bg("#FFF4E6", "#FD7E14", f"""
<rect x="-4" y="104" width="136" height="28" fill="#212529" {s()}/>
<path d="M20 116 H52 L46 110 M52 116 L46 122" fill="none" {ln("#E64980", 3)}/>
<path d="M44 82 H84 L80 106 H48Z" fill="#E03131" {s()}/>
<rect x="40" y="76" width="48" height="10" rx="3" fill="#FA5252" {s()}/>
<path d="M50 78 Q48 40 64 36 Q80 40 78 78Z" fill="#40C057" {s()}/>
<path d="M52 60 Q34 62 30 48 Q28 38 22 36" fill="none" {ln(O, 14)}/><path d="M52 60 Q34 62 30 48 Q28 38 22 36" fill="none" {ln("#40C057", 10)}/>
<path d="M76 56 Q92 52 96 64 Q100 72 108 70" fill="none" {ln(O, 14)}/><path d="M76 56 Q92 52 96 64 Q100 72 108 70" fill="none" {ln("#40C057", 10)}/>
<path d="M58 46 v4 M70 46 v4 M56 70 v4 M72 70 v4 M64 74 v3" {ln("#2B8A3E", 2)}/>
<path d="M50 40 Q50 22 64 22 Q78 22 78 40Z" fill="#1971C2" {s()}/>
<path d="M50 40 Q38 42 34 36 Q40 32 52 34" fill="#1864AB" {s('stroke-width="2.2"')}/>
{eye(59, 52, 0.6)}{eye(70, 52, 0.6)}<path d="M60 60 Q64 64 69 60" fill="none" {s('stroke-width="2"')}/>
<path d="M14 26 q4 -4 8 0 M106 30 q4 -4 8 0 M110 46 q4 -4 8 0" fill="none" {ln("#fff", 2.4)}/>
"""))

# Active Style, Открытое шоссе (4–6 и 12–15): старшая сестра и малыш танцуют одно движение
I["active-style-otkrytoe"] = ("девочка-подросток с высоким хвостом в бирюзовой футболке и малыш в голубом комбинезоне",
    "стоят рядом на сцене и одновременно делают одно и то же танцевальное движение — рука вверх, колено в сторону, малыш старательно повторяет",
    bg("#E3FAFC", "#15AABF", f"""
<rect x="-4" y="108" width="136" height="24" fill="#0B7285" {s()}/>
{limb(46, 52, 30, 26, SKIN, 5)}{limb(54, 54, 66, 66, SKIN, 5)}
{limb(44, 82, 34, 94, "#343A40", 6)}{limb(34, 94, 42, 108, "#343A40", 6)}{limb(52, 82, 54, 108, "#343A40", 6)}
<path d="M38 50 Q48 44 58 50 L56 84 H40Z" fill="#20C997" {s()}/>
<circle cx="48" cy="36" r="11" fill="{SKIN}" {s()}/>
<path d="M37 34 Q38 22 48 22 Q58 22 59 34 Q52 28 37 34Z" fill="#5C3D2E" {s('stroke-width="2.2"')}/>
<path d="M56 24 Q70 14 66 34" fill="none" {ln(O, 7)}/><path d="M56 24 Q70 14 66 34" fill="none" {ln("#5C3D2E", 4)}/>
{eye(44, 37, 0.5)}{eye(52, 37, 0.5)}<path d="M45 42 Q48 45 51 42" fill="none" {s('stroke-width="1.6"')}/>
{limb(90, 76, 80, 58, SKIN, 4)}{limb(96, 78, 104, 86, SKIN, 4)}
{limb(88, 96, 80, 102, "#4DABF7", 5)}{limb(80, 102, 86, 108, "#4DABF7", 5)}{limb(96, 96, 98, 108, "#4DABF7", 5)}
<path d="M84 74 Q93 70 102 74 L100 98 H86Z" fill="#74C0FC" {s()}/>
<circle cx="93" cy="64" r="9" fill="{SKIN}" {s()}/>
<path d="M85 60 Q90 52 99 58" fill="none" {ln("#F59F00", 3)}/>
{eye(90, 65, 0.42)}{eye(96, 65, 0.42)}<path d="M91 69 Q93 71 95 69" fill="none" {s('stroke-width="1.4"')}/>
{sparkle(104, 30, 5)}{sparkle(20, 60, 3)}
"""))

# Active Style, 2-я Пугачёвская (K-pop и хип-хоп 7–15): пухлое сердечко-айдол в клетчатой юбочке показывает «V»
I["active-style-pugachevskaya"] = ("пухлое розовое сердечко-айдол в красной клетчатой юбочке и с синим бантом-галстуком",
    "подмигивает и показывает «V» ручкой в K-pop-позе на сцене, над ним сыплется разноцветное конфетти",
    bg("#F8F0FC", "#BE4BDB", f"""
<rect x="-4" y="108" width="136" height="24" fill="#862E9C" {s()}/>
<path d="M64 94 Q28 70 30 46 Q32 28 48 28 Q60 28 64 40 Q68 28 80 28 Q96 28 98 46 Q100 70 64 94Z" fill="#FF8CC6" {s()}/>
<path d="M44 80 Q64 96 84 80 L90 96 Q64 104 38 96Z" fill="#E03131" {s()}/>
<path d="M46 84 L42 98 M56 90 L54 102 M72 90 L74 102 M82 84 L86 98 M40 92 Q64 102 88 92" fill="none" {ln("#FFC9C9", 2)}/>
<path d="M58 66 L64 70 L70 66 L66 78 H62Z" fill="#1971C2" {s('stroke-width="2"')}/>
{eye(53, 54, 0.6)}<path d="M70 54 q5 -4 10 0" fill="none" {s('stroke-width="2.4"')}/>
<path d="M59 62 Q64 66 69 62" fill="none" {s('stroke-width="1.8"')}/>
<ellipse cx="46" cy="60" rx="3.4" ry="2" fill="#F03E3E" opacity=".5"/><ellipse cx="84" cy="60" rx="3.4" ry="2" fill="#F03E3E" opacity=".5"/>
{limb(96, 56, 108, 40, "#FF8CC6", 5)}
<path d="M106 40 L102 26 M110 40 L116 28" {ln(O, 6)}/><path d="M106 40 L102 26 M110 40 L116 28" {ln("#FF8CC6", 3)}/>
{limb(32, 58, 22, 70, "#FF8CC6", 5)}
<path d="M54 98 L52 110 M74 98 L76 110" {ln(O, 4)}/>
<path d="M46 110 h10 v3 h-10Z M72 110 h10 v3 h-10Z" fill="#fff" {s('stroke-width="1.6"')}/>
<rect x="18" y="20" width="6" height="6" fill="#FCC419" transform="rotate(20 21 23)"/><rect x="104" y="72" width="6" height="6" fill="#74C0FC" transform="rotate(-20 107 75)"/>
<rect x="40" y="10" width="5" height="5" fill="#69DB7C" transform="rotate(30 42 12)"/><rect x="84" y="12" width="5" height="5" fill="#fff" transform="rotate(10 86 14)"/>
<rect x="14" y="88" width="5" height="5" fill="#FF922B" transform="rotate(40 16 90)"/>
"""))

# Active Style, 1-я Владимирская (головной зал, 4–15): ёжик в полосатых гетрах танцует на паркете зала
I["active-style-vladimirskaya"] = ("коричневый ёжик в красно-белых полосатых гетрах",
    "танцует на светлом паркете танцзала: стоит на одной ножке, другую выставил в сторону, лапки вскинул вверх, как на финальной позе",
    bg("#FFF9DB", "#E8590C", f"""
<rect x="-4" y="104" width="136" height="28" fill="#E9C46A" {s()}/>
<path d="M10 104 L-4 132 M40 104 L32 132 M70 104 L68 132 M100 104 L104 132 M126 104 L134 132" {ln("#C9A227", 2)}/>
{''.join(f'<path d="M{64 + 30 * c:.0f} {58 + 26 * d:.0f} L{64 + 42 * c:.0f} {58 + 38 * d:.0f}" {ln(O, 7)}/><path d="M{64 + 30 * c:.0f} {58 + 26 * d:.0f} L{64 + 42 * c:.0f} {58 + 38 * d:.0f}" {ln("#5C3D2E", 4)}/>' for c, d in ((-1, -.2), (-.85, -.7), (-.45, -1.05), (0, -1.15), (.45, -1.05), (.85, -.7), (1, -.2), (-.95, .35), (.95, .35)))}
<ellipse cx="64" cy="62" rx="30" ry="28" fill="#8D6E63" {s()}/>
<path d="M44 66 Q44 46 64 44 Q84 46 84 66 Q84 84 64 86 Q44 84 44 66Z" fill="#F1E3C6" {s()}/>
{eye(57, 62, 0.6)}{eye(71, 62, 0.6)}<circle cx="64" cy="70" r="3.4" fill="{O}"/>
<path d="M58 76 Q64 80 70 76" fill="none" {s('stroke-width="1.8"')}/>
{limb(40, 56, 24, 34, "#8D6E63", 5)}{limb(88, 56, 104, 34, "#8D6E63", 5)}
<path d="M56 86 L56 106" {ln(O, 11)}/><path d="M56 86 L56 106" {ln("#fff", 7)}/>
<path d="M52 92 h8 M52 98 h8" {ln("#E03131", 3.4)}/>
<path d="M72 86 L94 96" {ln(O, 11)}/><path d="M72 86 L94 96" {ln("#fff", 7)}/>
<path d="M78 86 l-2 5 M86 90 l-2 5" {ln("#E03131", 3.4)}/>
<ellipse cx="54" cy="108" rx="7" ry="3.4" fill="#5C3D2E" {s('stroke-width="2"')}/><ellipse cx="98" cy="98" rx="5" ry="4" fill="#5C3D2E" {s('stroke-width="2"')}/>
{sparkle(20, 20, 5)}{sparkle(110, 18, 4)}
"""))

# Первая школа ТВ и эстрады, Ташкентская: табло «В ЭФИРЕ» загорелось над сценой
I["schooltv-tashkentskaya"] = ("красное студийное табло «В ЭФИРЕ» с мордашкой и двумя лампочками-ушками",
    "загорелось над маленькой сценой студии, а под ним кружатся нотка, кисточка и балетная туфелька",
    bg("#FFF5F5", "#FA5252", f"""
<rect x="-4" y="104" width="136" height="28" fill="#495057" {s()}/>
<path d="M64 -4 V18" {ln(O, 3)}/>
<rect x="22" y="18" width="84" height="44" rx="10" fill="#E03131" {s()}/>
<rect x="28" y="24" width="72" height="32" rx="6" fill="#FF6B6B" {s('stroke-width="2"')}/>
<text x="64" y="38" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="11" fill="#fff">В ЭФИРЕ</text>
{eye(54, 47, 0.45)}{eye(74, 47, 0.45)}<path d="M60 51 Q64 54 68 51" fill="none" {s('stroke-width="1.6"')}/>
<circle cx="18" cy="40" r="6" fill="#FFE066" {s('stroke-width="2"')}/><circle cx="110" cy="40" r="6" fill="#FFE066" {s('stroke-width="2"')}/>
<path d="M8 40 h-6 M120 40 h8 M12 30 l-5 -4 M116 30 l5 -4" {ln("#FFE066", 2.4)}/>
{note(36, 92, 0.9, "#7048E8")}
<path d="M58 98 L74 74" {ln(O, 6)}/><path d="M58 98 L74 74" {ln("#FAB005", 3.4)}/><path d="M74 74 l4 -8 2 9Z" fill="#20C997" {s('stroke-width="1.6"')}/>
<path d="M92 96 Q90 84 98 82 Q104 84 104 94 Q100 100 92 96Z" fill="#FFC9DE" {s('stroke-width="2"')}/>
<path d="M96 84 L90 76 M100 84 L106 76" {ln("#F783AC", 1.8)}/>
"""))

# Kidance, Тропарёво (5–15): собачка из воздушных шариков танцует
I["kidance-anokhina"] = ("бирюзовая собачка, скрученная из длинных воздушных шариков, с мордашкой",
    "танцует на задних лапках, вскинув переднюю лапку вверх, на сцене под гирляндой из флажков",
    bg("#FFF9DB", "#20C997", f"""
<path d="M-4 18 Q64 36 132 18" fill="none" {ln(O, 2)}/>
{''.join(f'<path d="M{x} {18 + int(18 * (1 - ((x - 64) / 68) ** 2))} l6 12 6 -12Z" fill="{c}" {s("stroke-width=\"1.6\"")}/>' for x, c in ((8, "#FA5252"), (28, "#FCC419"), (48, "#4DABF7"), (68, "#E64980"), (88, "#40C057"), (108, "#7950F2")))}
<rect x="-4" y="108" width="136" height="24" fill="#E8590C" {s()}/>
<ellipse cx="58" cy="76" rx="22" ry="11" fill="#38D9A9" {s()} transform="rotate(-70 58 76)"/>
<ellipse cx="50" cy="100" rx="6" ry="10" fill="#38D9A9" {s()} transform="rotate(10 50 100)"/>
<ellipse cx="68" cy="100" rx="6" ry="10" fill="#38D9A9" {s()} transform="rotate(-10 68 100)"/>
<ellipse cx="80" cy="50" rx="6" ry="14" fill="#38D9A9" {s()} transform="rotate(40 80 50)"/>
<ellipse cx="40" cy="80" rx="6" ry="12" fill="#38D9A9" {s()} transform="rotate(-50 40 80)"/>
<ellipse cx="62" cy="46" rx="14" ry="11" fill="#38D9A9" {s()}/>
<ellipse cx="50" cy="38" rx="5" ry="11" fill="#38D9A9" {s()} transform="rotate(-20 50 38)"/>
<ellipse cx="72" cy="36" rx="5" ry="11" fill="#38D9A9" {s()} transform="rotate(20 72 36)"/>
<ellipse cx="62" cy="52" rx="5" ry="3.4" fill="#0CA678" {s('stroke-width="1.6"')}/>
{eye(57, 45, 0.5)}{eye(67, 45, 0.5)}
<path d="M54 42 Q50 50 56 52 M30 70 q-4 -6 2 -8" fill="none" {ln("#fff", 2.4)}/>
<path d="M40 90 Q30 96 34 106" fill="none" {ln(O, 2)}/>
{sparkle(104, 66, 5)}{sparkle(20, 50, 4)}
"""))

# «Альтернатива», Истра (эстрадно-театральная, 4–18): гримёрная пудреница-персонаж перед выходом на сцену
I["alternativa-istra"] = ("круглая золотая гримёрная пудреница с откинутой зеркальной крышкой и мордашкой",
    "держит пушистую розовую пуховку и прихорашивается перед выходом, за ней виден край синего занавеса и звёздочка на двери гримёрки",
    bg("#E7F5FF", "#1C7ED6", f"""
<path d="M-4 -4 H30 Q24 50 32 132 H-4Z" fill="#1864AB" {s()}/>
<path d="M10 0 Q6 60 14 132" fill="none" {ln("#0B4F8A", 3)}/>
<path d="M106 10 l4 9 10 1 -8 6 3 10 -9 -6 -9 6 3 -10 -8 -6 10 -1Z" fill="#FCC419" {s('stroke-width="2"')}/>
<ellipse cx="66" cy="96" rx="36" ry="14" fill="#E8A33D" {s()}/>
<path d="M30 96 V84 Q30 70 66 70 Q102 70 102 84 V96" fill="#FCC419" {s()}/>
<ellipse cx="66" cy="82" rx="30" ry="9" fill="#F3D9B1" {s('stroke-width="2"')}/>
<path d="M36 76 Q34 40 66 32 Q98 40 96 76" fill="#FCC419" {s()}/>
<path d="M42 72 Q42 46 66 40 Q90 46 90 72Z" fill="#D0EBFF" {s('stroke-width="2.2"')}/>
<path d="M50 50 L58 44 M50 58 L64 46" {ln("#fff", 2.4)}/>
{eye(58, 92, 0.55)}{eye(74, 92, 0.55)}<path d="M62 100 Q66 103 70 100" fill="none" {s('stroke-width="1.8"')}/>
<circle cx="110" cy="72" r="12" fill="#FFC9DE" {s()}/>
<path d="M102 66 q4 -4 8 0 q4 -4 8 0 M102 76 q4 4 8 0 q4 4 8 0" fill="none" {ln("#fff", 2)}/>
<path d="M100 82 L96 92" {ln(O, 3)}/>
"""))

# «Ди Дэнс Хаус», Трусово (деревня под Истрой): рулон сена в розовых кроссовках танцует
I["didance-trusovo"] = ("круглый золотой рулон сена с мордашкой на торце и в розовых кроссовках",
    "танцует хип-хоп посреди деревенского луга у штакетника, вскинув соломинки-руки, а над ним кружат две бабочки",
    bg("#E9FAC8", "#74B816", f"""
<rect x="-4" y="98" width="136" height="34" fill="#94D82D" {s()}/>
{''.join(f'<rect x="{x}" y="74" width="8" height="30" fill="#fff" {s("stroke-width=\"1.8\"")}/><path d="M{x} 74 l4 -6 4 6" fill="#fff" {s("stroke-width=\"1.8\"")}/>' for x in (-2, 12, 108, 122))}
<path d="M-4 86 H20 M106 86 H132" {ln("#ADB5BD", 3)}/>
<circle cx="64" cy="64" r="30" fill="#F2C94C" {s()}/>
<circle cx="64" cy="64" r="22" fill="none" {ln("#D9A520", 2)}/><circle cx="64" cy="64" r="13" fill="none" {ln("#D9A520", 2)}/>
<path d="M40 50 l-6 -3 M88 50 l6 -3 M36 76 l-6 2 M92 76 l6 2" {ln("#D9A520", 2)}/>
{face(64, 62, 8, 0.65)}
<path d="M36 56 L18 36 M92 56 L110 34" {ln(O, 6)}/><path d="M36 56 L18 36 M92 56 L110 34" {ln("#F2C94C", 3)}/>
<path d="M18 36 l-4 -6 M18 36 l-6 -2 M110 34 l2 -7 M110 34 l7 -2" {ln("#D9A520", 2)}/>
<path d="M54 92 L50 104 M74 92 L80 102" {ln(O, 4)}/>
<path d="M40 102 h14 q2 6 -2 7 h-12Z M76 100 h12 q4 4 0 7 h-12Z" fill="#F783AC" {s('stroke-width="2"')}/>
<path d="M30 20 q-4 -6 0 -8 q4 2 0 8 q4 -6 8 -4 q0 6 -8 4Z" fill="#FF922B" {s('stroke-width="1.4"')}/>
<path d="M98 16 q-4 -6 0 -8 q4 2 0 8 q4 -6 8 -4 q0 6 -8 4Z" fill="#748FFC" {s('stroke-width="1.4"')}/>
"""))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
