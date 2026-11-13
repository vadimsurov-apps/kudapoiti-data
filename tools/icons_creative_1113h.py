"""Иконки робота creative, 13.11 (запуск 1113h). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1113h.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 Soul (Пресненский Вал: фортепиано, вокал с 5 лет, гитара, барабаны, саксофон): чёрный рояль-малыш поёт в микрофон
I["soul-presnensky-val"] = ("чёрный кабинетный рояль-малыш с поднятой крышкой-крылом и улыбкой из белых клавиш",
    "поёт в серебряный микрофон на стойке, а над поднятой крышкой кружатся золотые ноты", bg("#FFE8CC", "#FF922B", f'''
<path d="M18 74 L30 30 Q34 22 44 24 L96 46 Z" fill="#343A40" {s()}/>
<path d="M30 30 L40 74" {ln("#868E96", 2.5)}/>
<path d="M14 74 H102 Q108 74 108 80 V92 H14Z" fill="#212529" {s()}/>
<rect x="20" y="78" width="76" height="9" rx="2" fill="#fff" {s('stroke-width="2"')}/>
<path d="M28 78 V84 M36 78 V84 M48 78 V84 M56 78 V84 M64 78 V84 M76 78 V84 M84 78 V84" {ln(O, 2.6)}/>
<path d="M20 92 V116 M98 92 V116" {ln(O, 7)}/><path d="M20 92 V116 M98 92 V116" {ln("#495057", 4)}/>
{eye(46, 64, 0.8)}{eye(66, 64, 0.8)}
<ellipse cx="38" cy="70" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/><ellipse cx="74" cy="70" rx="4" ry="2.4" fill="#FF8787" opacity=".8"/>
<path d="M114 124 V70" {ln(O, 5)}/><path d="M114 124 V70" {ln("#ADB5BD", 3)}/>
<path d="M100 124 H124" {ln(O, 5)}/>
<path d="M114 70 Q100 66 92 72" fill="none" {ln(O, 3)}/>
<rect x="84" y="64" width="12" height="16" rx="6" fill="#CED4DA" {s()}/>
{note(70, 22, 0.8, "#FCC419")}{note(96, 14, 0.6, "#FCC419")}{note(110, 36, 0.55, "#FFF3BF")}
'''))

# 2 «Мы рисуем!» (Бутово, группы 5–6 и 7–9 лет, старшие): фартук-халатик для рисования в отпечатках красок
I["my-risuem-rudneva"] = ("зелёный клеёнчатый детский фартук для рисования с нарукавниками и мордашкой на кармашке",
    "весь в разноцветных отпечатках ладошек и брызгах, из кармашка торчат три кисточки, а нарукавники машут от радости", bg("#F3F0FF", "#9775FA", f'''
<path d="M40 30 Q64 22 88 30 L96 112 Q64 120 32 112Z" fill="#40C057" {s()}/>
<path d="M44 30 Q52 12 64 12 Q76 12 84 30" fill="none" {ln(O, 4)}/>
<path d="M40 40 Q22 44 14 30" fill="none" {ln(O, 9)}/><path d="M40 40 Q22 44 14 30" fill="none" {ln("#69DB7C", 6)}/>
<path d="M88 40 Q106 44 114 30" fill="none" {ln(O, 9)}/><path d="M88 40 Q106 44 114 30" fill="none" {ln("#69DB7C", 6)}/>
<circle cx="12" cy="28" r="5" fill="{SKIN}" {s('stroke-width="2"')}/><circle cx="116" cy="28" r="5" fill="{SKIN}" {s('stroke-width="2"')}/>
<rect x="46" y="76" width="36" height="26" rx="5" fill="#2F9E44" {s()}/>
<path d="M54 74 L50 52 M64 74 V48 M74 74 L80 52" {ln(O, 5)}/><path d="M54 74 L50 52 M64 74 V48 M74 74 L80 52" {ln("#E8C07A", 3)}/>
<ellipse cx="50" cy="50" rx="3" ry="4" fill="#F03E3E" {s('stroke-width="1.6"')}/><ellipse cx="64" cy="46" rx="3" ry="4" fill="#FAB005" {s('stroke-width="1.6"')}/><ellipse cx="80" cy="50" rx="3" ry="4" fill="#228BE6" {s('stroke-width="1.6"')}/>
{eye(58, 86, 0.55)}{eye(70, 86, 0.55)}<path d="M60 93 Q64 96 68 93" fill="none" {s('stroke-width="1.8"')}/>
<g opacity=".9"><circle cx="40" cy="62" r="5" fill="#F03E3E"/><circle cx="36" cy="56" r="2" fill="#F03E3E"/><circle cx="43" cy="55" r="2" fill="#F03E3E"/>
<circle cx="88" cy="66" r="5" fill="#FAB005"/><circle cx="92" cy="59" r="2" fill="#FAB005"/><circle cx="85" cy="59" r="2" fill="#FAB005"/>
<circle cx="42" cy="104" r="3" fill="#228BE6"/><circle cx="86" cy="100" r="3" fill="#E64980"/></g>
'''))

# 3 Didance lab (ул. Дмитриевского: хип-хоп, вог, контемпорари, бэйбидэнс 3–7): колба из «лаборатории» крутит брейк
I["didance-lab-dmitrievskogo"] = ("круглодонная лабораторная колба с фиолетовым зельем и мордашкой на тонких белых ножках",
    "танцует хип-хоп, вскинув обе руки в зелёных перчатках, а вокруг неё пунктиром закручивается вихрь движения и летят фиолетовые нотки", bg("#C3FAE8", "#0CA678", f'''
<ellipse cx="64" cy="118" rx="30" ry="6" fill="#087F5B" opacity=".5"/>
<path d="M56 112 V96 M72 112 V96" {ln(O, 9)}/><path d="M56 112 V96 M72 112 V96" {ln("#E9ECEF", 6)}/>
<circle cx="64" cy="66" r="30" fill="#E7F5FF" {s()}/>
<path d="M36 76 Q64 64 92 76 Q88 94 64 96 Q40 94 36 76Z" fill="#9C36B5" {s('stroke-width="2"')}/>
<path d="M56 34 V20 M72 34 V20" {ln(O, 3)}/><rect x="54" y="12" width="20" height="24" fill="#E7F5FF" {s()}/>
<path d="M30 52 L12 40 M98 52 L116 40" {ln(O, 9)}/><path d="M30 52 L12 40 M98 52 L116 40" {ln("#E9ECEF", 6)}/>
<path d="M4 34 q8 -2 12 6 l-4 6 q-8 -2 -10 -8Z" fill="#40C057" {s('stroke-width="2.2"')}/>
<path d="M124 34 q-8 -2 -12 6 l4 6 q8 -2 10 -8Z" fill="#40C057" {s('stroke-width="2.2"')}/>
{eye(54, 58, 0.7)}{eye(74, 58, 0.7)}<path d="M57 68 Q64 73 71 68" fill="none" {s('stroke-width="2"')}/>
<circle cx="48" cy="84" r="3" fill="#E599F7"/><circle cx="76" cy="86" r="2.5" fill="#E599F7"/>
<path d="M20 74 a26 26 0 0 0 10 26 M108 74 a26 26 0 0 1 -10 26" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 5"/>
{note(100, 14, 0.6, "#862E9C")}{note(24, 16, 0.55, "#862E9C")}
'''))

# 4 Арт-студия Натальи Кузнецовой (Свиблово: рисование с 5 лет, мини-группы, перерыв на чай с баранками)
I["kuznetsova-art-sedova"] = ("румяная баранка с маком и мордашкой, в маленьком синем берете",
    "стоит на табуретке у мольберта и кистью дорисовывает на холсте дымящуюся чашку чая", bg("#FFF4E6", "#E8590C", f'''
<path d="M66 122 L78 34 M118 122 L106 34 M92 34 V124" {ln(O, 6)}/><path d="M66 122 L78 34 M118 122 L106 34" {ln("#8D5524", 3)}/>
<rect x="70" y="24" width="46" height="46" rx="3" fill="#FFFDF8" {s()}/>
<path d="M80 46 H102 V56 Q102 62 96 62 H86 Q80 62 80 56Z" fill="#F783AC" {s('stroke-width="2"')}/>
<path d="M102 49 q7 0 7 5 q0 5 -7 5" fill="none" {s('stroke-width="2"')}/>
<path d="M86 42 q-3 -4 0 -8 M92 42 q-3 -4 0 -8 M98 42 q-3 -4 0 -8" fill="none" {ln("#ADB5BD", 2)}/>
<rect x="70" y="68" width="46" height="5" fill="#8D5524" {s('stroke-width="2"')}/>
<rect x="18" y="104" width="40" height="6" rx="2" fill="#A0522D" {s()}/><path d="M24 110 V126 M52 110 V126" {ln(O, 5)}/>
<circle cx="38" cy="76" r="24" fill="#E0A458" {s()}/><circle cx="38" cy="76" r="9" fill="#FFF4E6" {s()}/>
<g fill="#343A40"><circle cx="24" cy="66" r="1.3"/><circle cx="30" cy="94" r="1.3"/><circle cx="50" cy="92" r="1.3"/><circle cx="56" cy="70" r="1.3"/><circle cx="20" cy="82" r="1.3"/></g>
<path d="M18 58 Q36 42 56 56 Q40 52 18 58Z" fill="#1C7ED6" {s('stroke-width="2.2"')}/><path d="M38 47 l2 -6" {ln(O, 3)}/>
{eye(30, 64, 0.5)}{eye(46, 64, 0.5)}<ellipse cx="25" cy="88" rx="3.5" ry="2" fill="#FF6B6B" opacity=".7"/>
<path d="M56 78 L80 52" {ln(O, 4)}/><path d="M56 78 L80 52" {ln("#FFD43B", 2)}/><circle cx="81" cy="50" r="2.6" fill="#F783AC" {s('stroke-width="1.4"')}/>
'''))

# 5 «ДансЛенд» (спортивные бальные танцы с 3 лет): малыш с номерком на спине выводит партнёршу на паркет турнира
I["danceland-sharikopodshipnikovskaya"] = ("мальчик-малыш в белой рубашке, чёрных брючках и с белым номерком «3» на спине (вид со спины)",
    "ведёт за руку девочку в пышном коралловом платье на блестящий паркет турнира по спортивным бальным танцам под лучи прожекторов", bg("#FFF0F6", "#A61E4D", f'''
<path d="M44 0 L20 128 H44Z M84 0 L108 128 H84Z" fill="#FFF" opacity=".18"/>
<path d="M-4 104 H132 V132 H-4Z" fill="#C08552" {s()}/><path d="M10 104 L2 128 M40 104 L36 128 M70 104 V128 M100 104 L104 128" {ln("#8D5524", 2)}/>
{limb(36, 82, 34, 108, "#212529", 6)}{limb(46, 82, 48, 108, "#212529", 6)}
<path d="M28 54 Q41 48 54 54 L52 84 H30Z" fill="#fff" {s()}/>
<rect x="33" y="60" width="16" height="14" rx="2" fill="#fff" {s('stroke-width="2"')}/>
<path d="M38 64 q4 -3 6 0 q1 3 -3 4 q4 1 3 4 q-2 3 -6 0" fill="none" {ln(O, 2)}/>
<circle cx="41" cy="40" r="12" fill="#6F4E37" {s()}/>
<path d="M52 60 L72 66" {ln(O, 7)}/><path d="M52 60 L72 66" {ln("#fff", 4)}/>
<path d="M74 54 Q80 50 86 54 L88 66 Q104 92 102 104 Q84 110 66 104 Q66 90 76 66Z" fill="#FF8787" {s()}/>
<path d="M70 96 Q84 100 98 96" fill="none" {ln("#fff", 2)}/>
<circle cx="80" cy="40" r="11" fill="{SKIN}" {s()}/><path d="M69 38 Q70 26 80 27 Q92 27 91 40 Q84 32 69 38Z" fill="#F59F00" {s('stroke-width="2"')}/><circle cx="90" cy="28" r="5" fill="#F59F00" {s('stroke-width="2"')}/>
{eye(76, 42, 0.5)}{eye(84, 42, 0.5)}<path d="M77 47 Q80 49 83 47" fill="none" {s('stroke-width="1.6"')}/>
{sparkle(112, 22, 6)}{sparkle(16, 30, 5)}
'''))

def _pencils():
    out = ""
    for i, c in enumerate(["#1C7ED6", "#7048E8", "#2F9E44", "#FAB005", "#FD7E14", "#E64980", "#F03E3E"]):
        x, t = 14 + i * 14, 40 + i * 8
        out += (f'<path d="M{x} 100 V{t} L{x+6} {t-10} L{x+12} {t} V100Z" fill="{c}" {s()}/>'
                f'<path d="M{x} {t} L{x+6} {t-10} L{x+12} {t}Z" fill="#FFE8CC" {s("stroke-width=\"2\"")}/>'
                f'<path d="M{x+4} {t-7} L{x+6} {t-10} L{x+8} {t-7}Z" fill="{c}"/>'
                f'{eye(x+3, t+14, 0.42)}{eye(x+9, t+14, 0.42)}'
                f'<path d="M{x+4} {t+20} Q{x+6} {t+22} {x+8} {t+20}" fill="none" {s("stroke-width=\"1.4\"")}/>')
    return out


# 6 Детская художественная студия (Егорьевск, дети с 5 лет, живопись, рисунок, дизайн, керамика): карандаши строятся по росту
I["dhs-egoryevsk-tupitsyna"] = ("семь цветных карандашей-ребят с мордашками, выстроенных по росту от длинного синего до крошечного красного",
    "стоят в ряд на подоконнике студии, и самый маленький тянется к жёлтой кляксе-солнышку", bg("#E3FAFC", "#3BC9DB", f'''
<rect x="-4" y="100" width="136" height="30" fill="#E9ECEF" {s()}/>
<circle cx="108" cy="30" r="13" fill="#FFD43B" {s()}/><circle cx="94" cy="20" r="4" fill="#FFD43B"/><circle cx="121" cy="42" r="3" fill="#FFD43B"/>
{_pencils()}
'''))

# 7 «Танц-премьер» (просп. Вернадского, цокольный зал; современные, восточные, фламенко, с 4 лет): гвоздика отбивает сапатеадо
I["tants-premier-vernadskogo"] = ("алая гвоздика с мордашкой в чёрных танцевальных туфельках на каблучке, листья подняты как руки",
    "отбивает фламенко-сапатеадо на деревянном полу, а из-под каблучков вылетают жёлтые звёздочки ритма", bg("#FFF5F5", "#C92A2A", f'''
<rect x="-4" y="102" width="136" height="30" fill="#B07D48" {s()}/><path d="M20 102 V130 M56 102 V130 M92 102 V130" {ln("#8D5524", 2)}/>
<path d="M64 98 V58" {ln(O, 8)}/><path d="M64 98 V58" {ln("#2F9E44", 5)}/>
<path d="M64 74 Q46 66 34 44 Q50 50 62 66Z" fill="#51CF66" {s('stroke-width="2.2"')}/>
<path d="M64 74 Q82 66 94 44 Q78 50 66 66Z" fill="#51CF66" {s('stroke-width="2.2"')}/>
<path d="M58 96 L50 104 M70 96 L78 100" {ln(O, 6)}/><path d="M58 96 L50 104 M70 96 L78 100" {ln("#2F9E44", 3.5)}/>
<path d="M40 104 h14 l-2 4 h-12Z M74 98 h14 l-2 4 h-12Z" fill="#212529" {s('stroke-width="2"')}/>
<path d="M53 108 v5 M86 102 v5" {ln(O, 3)}/>
<path d="M38 40 Q36 18 50 22 Q54 8 64 16 Q74 8 78 22 Q92 18 90 40 Q86 56 64 58 Q42 56 38 40Z" fill="#F03E3E" {s()}/>
<path d="M44 30 l6 4 M84 30 l-6 4 M54 18 l2 6 M74 18 l-2 6" {ln("#FFA8A8", 2)}/>
{eye(56, 40, 0.65)}{eye(72, 40, 0.65)}<path d="M59 48 Q64 52 69 48" fill="none" {s('stroke-width="1.8"')}/>
{sparkle(30, 96, 5)}{sparkle(100, 92, 5)}{sparkle(110, 112, 4)}
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
