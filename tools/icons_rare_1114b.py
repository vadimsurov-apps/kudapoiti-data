"""Иконки робота rare 2026-11-14 (1114b) — каждая придумана и нарисована отдельно (абсолютная уникальность).
Реестр строк — в SUBJ ниже (дописываются в icons-src/subjects.txt). Запуск: python3 tools/icons_rare_1114b.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons as d

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
SUBJ = {}
O = d.O


def save(pid, bg, body, hero, scene):
    open(os.path.join(OUT, pid + ".svg"), "w").write(d.svg(bg, body))
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def ice(y=100, col="#EAF8FF"):
    return f'<path d="M0 {y} Q64 {y - 8} 128 {y} V128 H0Z" fill="{col}" ' + d.s('stroke-width="2.4"') + '/>'


def skate(x, y, w=34, boot="#FFFFFF", blade="#AEB9CF", flip=False):
    """Маленький ботинок-конёк: x,y — левый нижний угол ботинка."""
    t = f' transform="translate({2 * x + w} 0) scale(-1 1)"' if flip else ""
    b = (f'<g{t}><path d="M{x} {y} V{y - 18} Q{x} {y - 22} {x + 4} {y - 22} H{x + 13} Q{x + 16} {y - 22} {x + 16} {y - 18} '
         f'V{y - 10} Q{x + w - 2} {y - 9} {x + w} {y - 3} Q{x + w} {y} {x + w - 4} {y}Z" fill="{boot}" ' + d.s('stroke-width="2.6"') + '/>')
    b += (f'<path d="M{x + 3} {y} V{y + 5} M{x + w - 8} {y} V{y + 5}" stroke="{O}" stroke-width="2.6"/>'
          f'<path d="M{x - 2} {y + 6} H{x + w} Q{x + w + 5} {y + 6} {x + w + 5} {y + 1}" fill="none" stroke="{blade}" stroke-width="4" stroke-linecap="round"/></g>')
    return b


# 1. Каток «Искра» (Ростокино): огненная искорка на льду
def iskra():
    b = ice(98)
    b += '<path d="M64 18 Q86 44 84 66 Q82 88 64 90 Q44 88 42 66 Q42 50 54 38 Q54 52 62 54 Q58 36 64 18Z" fill="#FF8A3D" ' + d.s() + '/>'
    b += '<path d="M64 46 Q76 60 74 72 Q72 84 64 84 Q54 84 54 72 Q54 62 64 46Z" fill="#FFD45E"/>'
    b += d.face(64, 68, d=7, k=0.75)
    b += skate(46, 92, w=36, boot="#FFFFFF")
    for x, y, r in [(18, 88, 4), (28, 80, 3), (106, 84, 4), (98, 74, 3), (112, 70, 2.5)]:
        b += d.sparkle(x, y, r, "#FFE08A")
    save("rink-iskra-rostokino", "night", b,
         "огненная оранжевая искорка-капелька с жёлтой серединкой и мордашкой",
         "встала на белый конёк и мчится по натуральному льду, разбрасывая вокруг золотые искры")


# 2. Каток в парке-усадьбе Михалково: готическая красная башенка усадьбы
def mikhalkovo():
    b = ice(104, "#F1FAFF")
    b += '<rect x="40" y="38" width="48" height="56" fill="#C8553D" ' + d.s() + '/>'
    b += '<path d="M40 38 V30 H48 V38 M56 38 V30 H64 V38 M72 38 V30 H80 V38 M80 30 H88 V38" fill="#C8553D" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M54 94 V78 Q64 66 74 78 V94" fill="#5B3A2E" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M44 46 H84 M44 56 H84" stroke="#FFFFFF" stroke-width="2" opacity=".7"/>'
    b += d.face(64, 60, d=9, k=0.8)
    b += '<path d="M64 30 V14" stroke="#3B3355" stroke-width="2.6"/><path d="M64 14 L80 18 L64 23Z" fill="#4E7BF2" ' + d.s('stroke-width="2"') + '/>'
    b += '<path d="M38 96 H90" stroke="#AEB9CF" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M46 94 V96 M82 94 V96" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M16 108 q8 -3 16 0 M96 110 q8 -3 16 0" stroke="#9DD6F5" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    save("rink-mikhalkovo-park", "sky", b,
         "красная кирпичная готическая башенка усадьбы Михалково с белыми зубцами и синим флажком",
         "встала на длинное коньковое лезвие и выкатилась на лёд усадебного парка")


# 3. Каток в Пионерском парке: гроздь рябины на коньке
def pionersky():
    b = ice(100)
    b += '<path d="M60 22 Q70 30 66 46" fill="none" stroke="#6B4A2E" stroke-width="3.2" stroke-linecap="round"/>'
    b += '<path d="M60 26 Q40 14 30 26 Q42 32 60 26Z" fill="#5BBF5E" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M66 28 Q86 14 98 24 Q84 34 66 28Z" fill="#5BBF5E" ' + d.s('stroke-width="2.4"') + '/>'
    for x, y in [(52, 52), (66, 50), (80, 54), (46, 64), (60, 64), (74, 66), (88, 66), (54, 76), (68, 78), (82, 78)]:
        b += f'<circle cx="{x}" cy="{y}" r="8" fill="#E8463C" ' + d.s('stroke-width="2.2"') + '/>'
    b += d.face(67, 64, d=8, k=0.7)
    b += skate(48, 94, w=38)
    b += '<path d="M14 112 Q30 104 40 112 Q50 120 60 112" fill="none" stroke="#9DD6F5" stroke-width="2.6" stroke-linecap="round"/>'
    save("rink-pionersky-park", "teal", b,
         "гроздь красной рябины с двумя зелёными листиками и мордашкой на средней ягодке",
         "катится на белом фигурном коньке по катку в парке и выписывает на льду завитушку")


# 4. Каток в парке Никулино: сугроб-толстячок на коньках
def nikulino():
    b = ice(104)
    b += '<path d="M22 92 Q18 60 44 52 Q50 30 72 34 Q96 36 98 60 Q112 70 104 92Z" fill="#FFFFFF" ' + d.s() + '/>'
    b += '<path d="M40 60 Q46 56 52 60 M80 46 Q86 44 90 48" fill="none" stroke="#C9EEFF" stroke-width="3" stroke-linecap="round"/>'
    b += d.face(64, 68, d=10, k=0.9)
    b += skate(28, 96, w=30, boot="#2E3A55") + skate(70, 96, w=30, boot="#2E3A55")
    for x, y in [(70, 22), (82, 16), (60, 14), (92, 26)]:
        b += f'<circle cx="{x}" cy="{y}" r="2.6" fill="#FFFFFF" ' + d.s('stroke-width="1.4"') + '/>'
    save("rink-nikulino-park", "blue", b,
         "пухлый белый сугроб-толстячок с румяной мордашкой",
         "надел два чёрных конька и неуклюже выехал на лёд, а с макушки сыплются снежинки")


# 5. Каток в парке Сосенки (Царицыно): рябчик на коньках
def sosenki():
    b = ice(102)
    b += '<path d="M10 30 L22 8 L34 30Z M14 46 L22 26 L30 46Z" fill="#3E8E55" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M22 46 V60" stroke="#6B4A2E" stroke-width="3"/>'
    b += '<ellipse cx="68" cy="66" rx="32" ry="24" fill="#A8794E" ' + d.s() + '/>'
    b += '<circle cx="88" cy="42" r="16" fill="#A8794E" ' + d.s() + '/>'
    b += '<path d="M84 26 L88 18 L92 26" fill="#8A5E3A" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M100 42 L110 46 L100 48Z" fill="#F2C14E" ' + d.s('stroke-width="2"') + '/>'
    b += d.eye(92, 40, 0.7) + '<path d="M86 34 Q92 31 97 35" fill="none" stroke="#E8463C" stroke-width="2.4"/>'
    b += '<path d="M40 62 L22 54 L26 70Z" fill="#8A5E3A" ' + d.s('stroke-width="2.4"') + '/>'
    for x, y in [(56, 60), (68, 70), (80, 62), (60, 76)]:
        b += f'<path d="M{x - 3} {y} Q{x} {y - 4} {x + 3} {y}" fill="none" stroke="#FFFFFF" stroke-width="2"/>'
    b += '<path d="M54 88 V94 M76 88 V94" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M46 96 H62 M68 96 H86" stroke="#AEB9CF" stroke-width="4" stroke-linecap="round"/>'
    save("rink-sosenki-tsaritsyno", "green", b,
         "пёстрый лесной рябчик с хохолком и красной бровью",
         "вышел из соснового бора на каток и скользит на двух коротких лезвиях вместо лапок")


# 6. Каток в Нагатинском затоне: ледобур-фигурист
def zaton():
    b = ice(96, "#DDF2FF")
    b += '<ellipse cx="64" cy="108" rx="34" ry="8" fill="none" stroke="#7FB8E6" stroke-width="2.6" stroke-dasharray="5 4"/>'
    b += '<path d="M64 98 V58" stroke="#9AA3B5" stroke-width="7"/>'
    b += '<path d="M56 96 L72 90 M56 88 L72 82 M56 80 L72 74 M56 72 L72 66" stroke="#3B3355" stroke-width="2.4"/>'
    b += '<path d="M60 98 L64 106 L68 98Z" fill="#9AA3B5" ' + d.s('stroke-width="2"') + '/>'
    b += '<rect x="44" y="24" width="40" height="34" rx="12" fill="#2DB37A" ' + d.s() + '/>'
    b += d.face(64, 40, d=8, k=0.75)
    b += '<path d="M22 30 H44 M84 30 H106" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    b += '<rect x="14" y="24" width="12" height="12" rx="4" fill="#E8463C" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<rect x="102" y="24" width="12" height="12" rx="4" fill="#E8463C" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M90 70 q6 -6 12 0 M26 72 q-6 -6 -12 0" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    save("rink-nagatinsky-zaton", "blue", b,
         "зелёный рыбацкий ледобур с мордашкой и красными ручками",
         "крутится на льду затона, как фигурист в волчке, и рисует пунктирный круг вокруг себя")


# 7. Каток в Левобережном районе у парка «Дружба»: гирлянда бумажных человечков
def druzhba():
    b = ice(102)
    cols = ["#FF9EC4", "#FFD45E", "#6CC0F2", "#7CD26E"]
    for i, c in enumerate(cols):
        x = 22 + i * 28
        b += (f'<path d="M{x} {48} a8 8 0 1 1 0.1 0 M{x - 12} 60 H{x + 12} M{x} 56 V78 M{x} 78 L{x - 8} 92 M{x} 78 L{x + 8} 92" '
              f'fill="none" stroke="{O}" stroke-width="2.6"/>')
        b += f'<circle cx="{x}" cy="48" r="9" fill="{c}" ' + d.s('stroke-width="2.4"') + '/>'
        b += f'<rect x="{x - 8}" y="56" width="16" height="24" rx="6" fill="{c}" ' + d.s('stroke-width="2.4"') + '/>'
        b += d.eye(x - 3, 47, 0.45) + d.eye(x + 3, 47, 0.45)
        b += f'<path d="M{x - 10} 94 H{x + 10}" stroke="#AEB9CF" stroke-width="3.4" stroke-linecap="round"/>'
    b += '<path d="M30 62 H42 M58 62 H70 M86 62 H98" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M64 16 C58 8 48 14 54 22 L64 30 L74 22 C80 14 70 8 64 16Z" fill="#E8463C" ' + d.s('stroke-width="2.2"') + '/>'
    save("rink-druzhba-levoberezhny", "yellow", b,
         "гирлянда из четырёх разноцветных бумажных человечков, держащихся за руки",
         "катится по льду катка у парка «Дружба» цепочкой на тонких лезвиях, а над ними красное сердечко")


# 8. Каток на улице Молостовых: ледяной замок
def molostovykh():
    b = ice(104)
    b += '<path d="M26 98 V50 H38 V42 H46 V50 H58 V36 H70 V50 H82 V42 H90 V50 H102 V98Z" fill="#BDE8FF" ' + d.s() + '/>'
    b += '<path d="M30 60 L40 70 M88 60 L98 70 M60 56 L68 64" stroke="#FFFFFF" stroke-width="2.4"/>'
    b += '<path d="M52 98 V80 Q64 68 76 80 V98" fill="#6CC0F2" ' + d.s('stroke-width="2.6"') + '/>'
    b += d.face(64, 60, d=10, k=0.8)
    b += '<path d="M64 36 V20" stroke="#3B3355" stroke-width="2.4"/><path d="M64 20 L78 24 L64 28Z" fill="#FF9EC4" ' + d.s('stroke-width="2"') + '/>'
    b += skate(56, 104, w=26, boot="#FF9EC4")
    save("rink-molostovykh", "purple", b,
         "голубой ледяной замок с зубчатыми башнями и розовым флажком",
         "распахнул ворота-арку, и из них прямо на лёд выезжает маленький розовый конёк")


# 9. Каток на Дегунинской улице: шуба переобувается в коньки
def degeninskaya():
    b = '<rect x="0" y="92" width="128" height="36" fill="#E6D3B8"/>'
    b += '<rect x="18" y="84" width="92" height="10" rx="4" fill="#B57A45" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M26 94 V110 M102 94 V110" stroke="#3B3355" stroke-width="4"/>'
    b += '<path d="M40 86 Q36 50 50 34 Q64 26 78 34 Q92 50 88 86Z" fill="#C89A6A" ' + d.s() + '/>'
    b += '<path d="M48 40 Q64 50 80 40 Q78 30 64 28 Q50 30 48 40Z" fill="#F3E3CC" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M64 50 V84" stroke="#8A5E3A" stroke-width="2.4"/><circle cx="64" cy="60" r="2.6" fill="#3B3355"/><circle cx="64" cy="72" r="2.6" fill="#3B3355"/>'
    b += d.face(64, 40, d=7, k=0.65)
    b += skate(84, 114, w=28, boot="#FFFFFF")
    b += '<path d="M86 66 Q98 80 96 96" fill="none" stroke="#C89A6A" stroke-width="6" stroke-linecap="round"/>'
    save("rink-degeninskaya", "orange", b,
         "пушистая бежевая шубка с меховым воротником и пуговицами",
         "сидит на деревянной скамейке тёплой раздевалки и тянется рукавом зашнуровать белый конёк")


# 10. Каток с искусственным покрытием в Можайском районе (Дорогобужская): цифра 8 рисует свою восьмёрку
def dorogobuzh():
    b = ice(96, "#F1FAFF")
    b += '<path d="M24 112 C24 100 44 100 64 108 C84 116 104 116 104 104 C104 92 84 92 64 100 C44 108 24 124 24 112Z" fill="none" stroke="#7FB8E6" stroke-width="2.6"/>'
    b += '<circle cx="64" cy="34" r="17" fill="#FF6F91" ' + d.s() + '/><circle cx="64" cy="34" r="6" fill="#FFDCEB" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<circle cx="64" cy="70" r="21" fill="#FF6F91" ' + d.s() + '/><circle cx="64" cy="70" r="8" fill="#FFDCEB" ' + d.s('stroke-width="2.4"') + '/>'
    b += d.eye(56, 58, 0.6) + d.eye(72, 58, 0.6)
    b += '<path d="M60 84 Q64 88 68 84" fill="none" stroke="#3B3355" stroke-width="2.2"/>'
    b += '<path d="M56 91 V97 M72 91 V97" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M48 99 H84 Q90 99 90 94" fill="none" stroke="#AEB9CF" stroke-width="4" stroke-linecap="round"/>'
    b += d.sparkle(100, 30, 6, "#FFFFFF") + d.sparkle(26, 46, 5, "#FFFFFF")
    save("rink-dorogobuzhskaya", "pink", b,
         "розовая пухлая цифра 8 с мордашкой на нижнем колечке",
         "встала на коньковое лезвие и сама выписывает на льду свою фигурную восьмёрку")


# 11. Каток в районе Матушкино (Зеленоград): ожившая ледяная скульптура
def matushkino():
    b = ice(104, "#F1FAFF")
    b += '<rect x="34" y="94" width="60" height="10" rx="3" fill="#9DD6F5" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<circle cx="64" cy="40" r="20" fill="#CDEFFF" ' + d.s() + '/>'
    b += '<circle cx="48" cy="24" r="7" fill="#CDEFFF" ' + d.s('stroke-width="2.6"') + '/><circle cx="80" cy="24" r="7" fill="#CDEFFF" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<ellipse cx="64" cy="74" rx="22" ry="20" fill="#CDEFFF" ' + d.s() + '/>'
    b += d.face(64, 40, d=7, k=0.7)
    b += '<ellipse cx="64" cy="48" rx="5" ry="3.5" fill="#3B3355"/>'
    b += '<path d="M42 70 L28 60 M86 70 L100 58" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M50 30 L56 36 M74 62 L80 70" stroke="#FFFFFF" stroke-width="2.4"/>'
    b += '<path d="M48 92 H80" stroke="#AEB9CF" stroke-width="4.5" stroke-linecap="round"/>'
    b += d.sparkle(104, 40, 6) + d.sparkle(22, 44, 5)
    save("rink-matushkino", "teal", b,
         "прозрачная ледяная скульптура медвежонка на постаменте",
         "ожила, раскинула лапы для равновесия и поехала со своего постамента на коньковом полозе")


# 12. Каток в конноспортивном комплексе «Битца»: тюк сена на коньках
def bitsa():
    b = ice(102)
    b += '<rect x="28" y="40" width="72" height="50" rx="10" fill="#EBC56A" ' + d.s() + '/>'
    for y in (50, 60, 70, 80):
        b += f'<path d="M32 {y} Q48 {y - 3} 64 {y} T96 {y}" fill="none" stroke="#C99A36" stroke-width="2"/>'
    b += '<path d="M48 40 V90 M80 40 V90" stroke="#B5552B" stroke-width="3.2"/>'
    b += d.face(64, 60, d=10, k=0.85)
    b += '<path d="M30 40 L24 30 M40 40 L38 28 M90 40 L96 30 M100 44 L108 38" stroke="#C99A36" stroke-width="2.4" stroke-linecap="round"/>'
    b += '<path d="M40 90 V96 M88 90 V96" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M30 98 H100" stroke="#AEB9CF" stroke-width="4.5" stroke-linecap="round"/>'
    b += '<path d="M104 72 q6 -4 12 0 M104 82 q6 -4 12 0" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>'
    save("rink-bitsa-ksk", "green", b,
         "золотистый тюк сена, перевязанный красной бечёвкой",
         "выкатился из конюшни на каток конноспортивного комплекса на широком коньковом полозе")


# 13. Каток «Ашхабад» (Чертаново Северное): дыня-торпеда на коньках
def ashkhabad():
    b = ice(102, "#F3FBFF")
    b += '<ellipse cx="64" cy="60" rx="42" ry="24" fill="#F7D65A" transform="rotate(-12 64 60)" ' + d.s() + '/>'
    b += '<path d="M28 66 Q64 44 100 50 M30 74 Q64 58 98 62" fill="none" stroke="#D9A93A" stroke-width="2.2" transform="rotate(-6 64 60)"/>'
    b += '<path d="M104 48 Q112 40 110 32" fill="none" stroke="#5BBF5E" stroke-width="3" stroke-linecap="round"/>'
    b += d.face(60, 58, d=9, k=0.8)
    b += '<path d="M40 82 V90 M84 76 V88" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M30 92 H52 M74 90 H96" stroke="#AEB9CF" stroke-width="4" stroke-linecap="round"/>'
    b += '<path d="M8 50 H24 M6 60 H20" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    save("rink-ashkhabad-chertanovo", "orange", b,
         "длинная жёлтая дыня-торпеда с зелёным хвостиком",
         "разогналась на двух коньках и летит по катку «Ашхабад» так, что за ней тянутся полоски ветра")


# 14. ФОК «Лидер» (Волоколамск, ДС «Лама»): ладья, которую волокут по льду
def lider_volokolamsk():
    b = ice(98)
    b += '<path d="M20 78 H104 Q100 94 84 94 H40 Q24 94 20 78Z" fill="#B5763C" ' + d.s() + '/>'
    b += '<path d="M104 78 Q114 70 110 60" fill="none" stroke="#B5763C" stroke-width="6" stroke-linecap="round"/>'
    b += '<circle cx="110" cy="58" r="4" fill="#B5763C" ' + d.s('stroke-width="2"') + '/>'
    b += '<path d="M60 78 V30" stroke="#3B3355" stroke-width="3.2"/>'
    b += '<path d="M62 32 Q86 44 62 70Z" fill="#FFFFFF" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M66 44 H76 M66 54 H78" stroke="#E8463C" stroke-width="3"/>'
    b += d.face(46, 84, d=8, k=0.7)
    b += '<path d="M28 100 H96" stroke="#AEB9CF" stroke-width="4.5" stroke-linecap="round"/>'
    b += '<path d="M28 94 V100 M92 94 V100" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M20 80 Q10 70 4 72" fill="none" stroke="#C99A36" stroke-width="2.6" stroke-dasharray="3 3"/>'
    save("rink-lider-volokolamsk", "sky", b,
         "деревянная древнерусская ладья с белым парусом в красную полоску",
         "её по старому волоку тянут за верёвку по льду крытого катка, а вместо днища — коньковый полоз")


# 15. FunГрад в Сокольниках: тарзанка
def fungrad_sokolniki():
    b = '<rect x="0" y="100" width="128" height="28" fill="#9BD47A"/>'
    b += '<rect x="8" y="20" width="12" height="90" rx="4" fill="#9A6B43" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<rect x="108" y="20" width="12" height="90" rx="4" fill="#9A6B43" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M20 28 Q64 40 108 28" fill="none" stroke="#3B3355" stroke-width="3.4"/>'
    b += '<path d="M64 36 L82 82" stroke="#E2A24E" stroke-width="4" stroke-linecap="round"/>'
    b += '<circle cx="86" cy="90" r="14" fill="#FF8A3D" ' + d.s() + '/>'
    b += '<circle cx="86" cy="90" r="5" fill="#FFD45E" ' + d.s('stroke-width="2"') + '/>'
    b += d.eye(80, 86, 0.6) + d.eye(92, 86, 0.6)
    b += '<path d="M81 96 Q86 100 91 96" fill="none" stroke="#3B3355" stroke-width="2.2"/>'
    b += '<path d="M40 70 q8 6 16 4 M36 82 q8 6 18 4" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    save("fungrad-sokolniki", "green", b,
         "оранжевая тарзанка — круглое сиденье-диск на длинной верёвке",
         "раскачивается между двумя деревьями верёвочного парка в Сокольниках и весело свистит на лету")


# 16. Хоккейная академия Фетисова (Домодедово): хоккейная крага даёт «пять» шайбе
def fetisov():
    b = ice(104)
    b += ('<path d="M30 92 V54 Q30 44 40 44 H72 Q82 44 82 54 V60 Q92 54 98 62 Q100 70 90 74 L82 80 V92Z" '
          'fill="#2F5BD3" ' + d.s() + '/>')
    b += '<path d="M40 44 V30 Q40 24 46 24 Q52 24 52 30 V44 M52 44 V26 Q52 20 58 20 Q64 20 64 26 V44 M64 44 V30 Q64 24 70 24 Q76 24 76 30 V44" fill="#2F5BD3" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<rect x="28" y="84" width="56" height="12" rx="4" fill="#E8463C" ' + d.s('stroke-width="2.6"') + '/>'
    b += d.face(56, 62, d=9, k=0.8)
    b += '<ellipse cx="106" cy="34" rx="14" ry="7" fill="#2E2E3A" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M92 34 V40 Q106 48 120 40 V34" fill="#2E2E3A" ' + d.s('stroke-width="2.4"') + '/>'
    b += d.eye(101, 35, 0.5) + d.eye(110, 35, 0.5)
    b += '<path d="M84 30 l-6 -4 M86 22 l-4 -6 M94 18 l-1 -7" stroke="#FFD45E" stroke-width="2.6" stroke-linecap="round"/>'
    save("fetisov-hockey-domodedovo", "purple", b,
         "синяя хоккейная крага с красной манжетой и мордашкой на ладони",
         "подняла пальцы и даёт «пять» прилетевшей чёрной шайбе — та тоже улыбается")


# 17. СК «Вершина» (парк Царицыно): хоккейная шторка-мишень
def vershina():
    b = ice(104)
    b += '<rect x="22" y="30" width="84" height="66" rx="6" fill="#E8463C" ' + d.s() + '/>'
    b += '<rect x="28" y="36" width="72" height="54" rx="4" fill="#FFFFFF" ' + d.s('stroke-width="2.2"') + '/>'
    for x, y in [(34, 42), (84, 42), (34, 74), (84, 74)]:
        b += f'<rect x="{x}" y="{y}" width="12" height="12" rx="3" fill="#2E3A55" ' + d.s('stroke-width="2"') + '/>'
    b += d.face(64, 60, d=10, k=0.85)
    b += '<path d="M22 96 V104 M106 96 V104" stroke="#3B3355" stroke-width="3.4"/>'
    b += '<ellipse cx="96" cy="114" rx="9" ry="4" fill="#2E2E3A" ' + d.s('stroke-width="2"') + '/>'
    b += '<path d="M60 18 L64 8 L68 18 Z" fill="#FFD45E" ' + d.s('stroke-width="1.8"') + '/>'
    save("rink-vershina-tsaritsyno", "orange", b,
         "красная хоккейная шторка-мишень с четырьмя тёмными окошками по углам",
         "стоит на льду бросковой зоны и улыбается, ожидая, что шайба влетит точно в «девятку»")


# 18. Каток в парке «Патриот»: жёлтый тюбинг
def patriot():
    b = '<path d="M0 70 L50 40 L128 82 V128 H0Z" fill="#FFFFFF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#DDF2FF" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<ellipse cx="62" cy="82" rx="34" ry="16" fill="#FFC93C" ' + d.s() + '/>'
    b += '<ellipse cx="62" cy="78" rx="14" ry="5" fill="#E09E1C" ' + d.s('stroke-width="2.2"') + '/>'
    b += d.eye(48, 86, 0.6) + d.eye(76, 86, 0.6)
    b += '<path d="M56 92 Q62 96 68 92" fill="none" stroke="#3B3355" stroke-width="2.2"/>'
    b += '<path d="M28 74 Q20 66 26 60" fill="none" stroke="#3B3355" stroke-width="2.6"/>'
    b += '<path d="M100 64 q8 -2 14 4 M98 54 q8 -2 14 4" fill="none" stroke="#9DD6F5" stroke-width="2.6" stroke-linecap="round"/>'
    b += '<path d="M40 104 H86" stroke="#AEB9CF" stroke-width="4" stroke-linecap="round"/>'
    save("rink-patriot-kubinka", "blue", b,
         "жёлтый надувной тюбинг-«ватрушка» с мордашкой на боку",
         "съехал с тюбинговой горки и прямо на ходу выкатился на большой каток")


# 19. Каток в парке 850-летия Москвы: фейерверк-ракета
def park850():
    b = ice(104)
    b += '<path d="M64 20 Q78 34 76 70 H52 Q50 34 64 20Z" fill="#4E7BF2" ' + d.s() + '/>'
    b += '<path d="M52 60 L40 76 L52 72Z M76 60 L88 76 L76 72Z" fill="#E8463C" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<circle cx="64" cy="40" r="7" fill="#FFFFFF" ' + d.s('stroke-width="2.2"') + '/>'
    b += d.eye(59, 54, 0.55) + d.eye(69, 54, 0.55)
    b += '<path d="M60 62 Q64 65 68 62" fill="none" stroke="#3B3355" stroke-width="2"/>'
    b += '<path d="M58 70 L56 84 M70 70 L72 84" stroke="#FFB13B" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M44 92 H84" stroke="#AEB9CF" stroke-width="4.5" stroke-linecap="round"/><path d="M58 84 V92 M70 84 V92" stroke="#3B3355" stroke-width="3"/>'
    for x, y, c in [(26, 30, "#FFD45E"), (100, 26, "#FF9EC4"), (18, 60, "#7CD26E"), (108, 58, "#FFD45E")]:
        b += d.sparkle(x, y, 7, c)
    save("rink-park-850", "night", b,
         "синяя праздничная ракета-фейерверк с красными крылышками и окошком-иллюминатором",
         "стоит на коньковом полозе посреди катка и вот-вот взлетит, а вокруг уже вспыхивают цветные звёзды")


# 20. Каток «Театральный» (Химки): афишная тумба
def teatralny():
    b = ice(104, "#F6F1FF")
    b += '<path d="M44 36 H84 V96 H44Z" fill="#FFF3D6" ' + d.s() + '/>'
    b += '<path d="M40 30 Q64 18 88 30 V36 H40Z" fill="#2DB37A" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M64 20 V12" stroke="#3B3355" stroke-width="2.4"/><circle cx="64" cy="10" r="3" fill="#FFD45E" ' + d.s('stroke-width="1.6"') + '/>'
    b += '<rect x="50" y="44" width="28" height="14" rx="2" fill="#FF9EC4" ' + d.s('stroke-width="2"') + '/>'
    b += '<rect x="50" y="78" width="28" height="12" rx="2" fill="#6CC0F2" ' + d.s('stroke-width="2"') + '/>'
    b += d.face(64, 66, d=7, k=0.65)
    b += '<path d="M40 98 H88" stroke="#AEB9CF" stroke-width="4.5" stroke-linecap="round"/><path d="M50 96 V98 M78 96 V98" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M14 60 q6 -8 12 0 M102 50 q6 -8 12 0" fill="none" stroke="#A98BF0" stroke-width="2.6" stroke-linecap="round"/>'
    save("rink-teatralny-khimki", "purple", b,
         "круглая афишная тумба с зелёной крышей и розовой и голубой афишами",
         "выехала на коньковом полозе из сквера перед театром прямо на каток")


# 21. Каток в парке «Сказка»: сапоги-скороходы
def skazka():
    b = ice(102)
    for x, c in [(26, "#C8553D"), (66, "#C8553D")]:
        b += (f'<path d="M{x} 40 H{x + 18} V80 Q{x + 34} 80 {x + 36} 90 Q{x + 36} 96 {x + 30} 96 H{x} Z" fill="{c}" ' + d.s() + '/>')
        b += f'<path d="M{x - 2} 40 H{x + 20}" stroke="#FFD45E" stroke-width="5" stroke-linecap="round"/>'
        b += f'<path d="M{x - 2} 102 H{x + 38}" stroke="#AEB9CF" stroke-width="4" stroke-linecap="round"/><path d="M{x + 4} 96 V102 M{x + 28} 96 V102" stroke="#3B3355" stroke-width="3"/>'
    b += d.eye(32, 62, 0.55) + d.eye(40, 62, 0.55) + d.eye(72, 62, 0.55) + d.eye(80, 62, 0.55)
    b += '<path d="M33 70 Q36 73 39 70 M73 70 Q76 73 79 70" fill="none" stroke="#3B3355" stroke-width="2"/>'
    b += '<path d="M8 56 H20 M6 68 H18 M6 80 H20" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    b += d.sparkle(108, 30, 7, "#FFD45E") + d.sparkle(96, 16, 4, "#FFFFFF")
    save("rink-park-skazka", "pink", b,
         "пара красных сказочных сапог-скороходов с золотыми отворотами",
         "встали на коньковые лезвия и мчатся по катку парка «Сказка» семимильными шагами")


# 22. Катки в парке «Яуза»: маленький снегоход везёт коньки
def yauza():
    b = ice(100)
    b += '<path d="M24 84 H84 Q96 84 98 72 L84 60 H44 Q30 60 24 72Z" fill="#FF8A3D" ' + d.s() + '/>'
    b += '<path d="M48 60 L56 44 H72 L78 60" fill="#BDE8FF" ' + d.s('stroke-width="2.6"') + '/>'
    b += d.face(60, 70, d=8, k=0.7)
    b += '<path d="M20 92 H100 Q108 92 108 84" fill="none" stroke="#3B3355" stroke-width="3.4" stroke-linecap="round"/>'
    b += '<path d="M36 84 V92 M80 84 V92" stroke="#3B3355" stroke-width="3"/>'
    b += '<rect x="2" y="70" width="18" height="12" rx="3" fill="#9A6B43" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M6 70 V60 H12 V66 Q18 66 18 70 M10 60 V58" fill="#FFFFFF" ' + d.s('stroke-width="1.8"') + '/>'
    b += '<path d="M20 76 H24" stroke="#3B3355" stroke-width="2.4"/>'
    b += '<path d="M104 30 l2 6 6 2 -6 2 -2 6 -2 -6 -6 -2 6 -2z" fill="#FFFFFF"/>'
    save("rink-yauza-park", "sky", b,
         "оранжевый снегоход-малыш с голубым ветровым стеклом и мордашкой",
         "тянет за собой деревянные санки с белым коньком к катку в парке у реки")


ALL = [iskra, mikhalkovo, pionersky, nikulino, sosenki, bitsa, vershina, lider_volokolamsk, patriot, fungrad_sokolniki,
       fetisov]
# Нарисованы, но места не добавлены (дворовые/районные катки, закрытые) — в ALL не входят: zaton, druzhba, molostovykh,
# degeninskaya, dorogobuzh, matushkino, ashkhabad, park850, teatralny, skazka, yauza.

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for f in ALL:
        f()
    for pid, line in SUBJ.items():
        if not only or pid in only:
            print(line)
