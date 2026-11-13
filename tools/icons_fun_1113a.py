"""Иконки робота fun (2026-11-13, проход a): места из tools/add_fun_1113a.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1113a.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Пеленальная в ТРЦ «Капитолий» — малыш в слипе с ушками на пеленальном столике тянется к карусели-облачкам
I["chg-trc-kapitoliy-vernadskogo"] = ("#E2F7EE", "#4FB58E",
    "малыш-карапуз в розовом слипе с капюшоном-ушками",
    "лежит на пеленальном столике и тянет ручки к подвесной карусельке с облачками",
    # карусель
    f'<path d="M64 6 V20" stroke="{O}" stroke-width="2.6"/>'
    f'<path d="M36 26 Q64 14 92 26" fill="none" stroke="{O}" stroke-width="3"/>'
    f'<path d="M36 26 V34 M64 20 V30 M92 26 V34" stroke="{O}" stroke-width="2"/>'
    f'<path d="M28 40 q0 -7 8 -7 q3 -5 9 -2 q7 0 6 8z" fill="#fff" {W(2.4)}/>'
    f'<path d="M84 40 q0 -7 8 -7 q3 -5 9 -2 q7 0 6 8z" fill="#fff" {W(2.4)}/>'
    f'<circle cx="64" cy="34" r="5" fill="#FFD23F" {W(2.2)}/>'
    # столик
    f'<rect x="10" y="98" width="108" height="12" rx="6" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M20 110 V126 M108 110 V126" stroke="{O}" stroke-width="4"/>'
    # малыш лежит
    f'<ellipse cx="72" cy="86" rx="34" ry="14" fill="#FFA3C7" {W(3)}/>'
    f'<path d="M88 84 Q104 80 108 70" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M88 84 Q104 80 108 70" fill="none" stroke="#FFA3C7" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M58 80 Q54 64 60 54" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M58 80 Q54 64 60 54" fill="none" stroke="#FFA3C7" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="60" cy="52" r="4" fill="#FFE0C7" {W(2)}/><circle cx="108" cy="68" r="4" fill="#FFE0C7" {W(2)}/>'
    # голова с капюшоном-ушками
    f'<circle cx="34" cy="78" r="20" fill="#FFA3C7" {W(3)}/>'
    f'<ellipse cx="20" cy="60" rx="6" ry="9" fill="#FFA3C7" {W(2.6)}/><ellipse cx="44" cy="58" rx="6" ry="9" fill="#FFA3C7" {W(2.6)}/>'
    f'<circle cx="35" cy="80" r="13" fill="#FFE0C7" {W(2.4)}/>'
    + face(35, 79, d=5, k=0.55) + sparkle(112, 44, 4, "#fff") + sparkle(16, 22, 3, "#fff"))

# 2. Пеленальная в ТЦ «Щука» — добрая щука в фартуке несёт в зубах сложенный подгузник
I["chg-trk-shchuka"] = ("#DDF3FF", "#3E8FC7",
    "добрая зелёная щука в белом фартучке",
    "плывёт по воздуху и бережно несёт в зубах чистый сложенный подгузник с сердечком",
    # хвост
    f'<path d="M100 64 L122 46 L118 64 L122 82Z" fill="#6CC56F" {W(3)}/>'
    # тело
    f'<path d="M14 64 Q30 40 70 42 Q100 44 104 64 Q100 84 70 86 Q30 88 14 64Z" fill="#8ED97A" {W(3.2)}/>'
    f'<path d="M50 44 L58 30 L68 43" fill="#6CC56F" {W(2.6)}/>'
    f'<path d="M60 84 L64 96 L74 85" fill="#6CC56F" {W(2.6)}/>'
    # пятнышки
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="2.4" fill="#5BAE5E"/>' for x, y in ((74, 52), (86, 58), (80, 70), (92, 70)))
    # фартук
    + f'<path d="M48 50 Q62 48 70 52 L68 82 Q56 86 46 80Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M50 52 Q42 46 38 50" fill="none" stroke="{O}" stroke-width="2"/>'
    + eye(30, 56, 0.75) +
    f'<ellipse cx="30" cy="64" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
    # подгузник в зубах
    f'<path d="M4 70 L22 70 L24 92 Q14 98 4 92Z" fill="#FFF6D6" {W(2.6)}/>'
    f'<path d="M10 80 c0 -3 4 -3 4 0 c0 -3 4 -3 4 0 c0 3 -4 6 -4 6 c0 0 -4 -3 -4 -6z" fill="#FF7FA8"/>'
    f'<path d="M14 66 Q20 70 26 66" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(40, 22, 5, "#fff") + sparkle(92, 104, 4, "#fff"))

# 7. Barabaka Quests — рыжая лохматая собака-сыщик в клетчатой кепке идёт по светящимся следам к запертой двери
I["fun-barabaka-quests-chistoprudny"] = ("#E9E2FF", "#5B4BB0",
    "рыжая лохматая собака-сыщик в клетчатой кепке",
    "принюхивается к светящимся следам-лапкам, которые ведут к таинственной запертой двери",
    # дверь
    f'<path d="M86 116 V36 Q86 20 104 20 Q122 20 122 36 V116Z" fill="#6B4A3A" {W(3)}/>'
    f'<circle cx="94" cy="72" r="3.4" fill="#FFD23F" {W(1.6)}/>'
    f'<path d="M100 60 L108 60 L104 52Z" fill="#FFD23F" {W(1.6)}/>'
    # следы
    + "".join(f'<g fill="#9DF2FF" opacity=".95"><ellipse cx="{x}" cy="{y}" rx="4" ry="3"/><circle cx="{x-4}" cy="{y-5}" r="1.6"/><circle cx="{x}" cy="{y-6}" r="1.6"/><circle cx="{x+4}" cy="{y-5}" r="1.6"/></g>'
              for x, y in ((62, 118), (74, 110), (84, 118)))
    # собака
    + f'<ellipse cx="38" cy="96" rx="26" ry="18" fill="#E8893E" {W(3)}/>'
    f'<path d="M14 92 q-8 -4 -6 -12" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="46" cy="66" r="20" fill="#F29A4C" {W(3)}/>'
    f'<path d="M28 58 Q18 70 26 84 Q34 76 32 62Z" fill="#B85E25" {W(2.6)}/>'
    f'<ellipse cx="64" cy="74" rx="8" ry="6" fill="#FFD3A8" {W(2.4)}/><circle cx="70" cy="72" r="3" fill="{O}"/>'
    + eye(42, 64, 0.65) + eye(54, 62, 0.65) +
    # кепка
    f'<path d="M28 52 Q44 34 64 48 L72 50 Q60 54 30 56Z" fill="#C9D3E8" {W(2.6)}/>'
    f'<path d="M36 48 L58 44 M40 54 L44 40 M52 54 L54 40" stroke="#7A86A8" stroke-width="1.6"/>'
    + sparkle(64, 22, 5, "#fff") + sparkle(16, 30, 3, "#9DF2FF"))

# 9. «Хокинг», квест «Утерянная библиотека Ивана Грозного» — старинная книга в нише со свечой, из неё вылетает ключ
I["fun-hoking-quests-leninsky"] = ("#F6E7CF", "#9A6A3A",
    "старинная книга в кожаном переплёте с медными уголками",
    "лежит в каменной нише рядом с горящей свечой, а из страниц вылетает золотой ключ",
    # ниша
    f'<path d="M14 120 V50 Q14 14 64 14 Q114 14 114 50 V120Z" fill="#CDB89A" {W(3)}/>'
    f'<path d="M26 120 V56 Q26 28 64 28 Q102 28 102 56 V120Z" fill="#6E5440" {W(2.6)}/>'
    f'<path d="M14 72 H26 M102 72 H114 M14 96 H26 M102 96 H114 M40 20 L42 28 M88 20 L86 28" stroke="#A8916F" stroke-width="2"/>'
    # книга
    f'<path d="M30 112 L36 84 H92 L98 112Z" fill="#9C3B2E" {W(3)}/>'
    f'<path d="M38 86 Q64 78 64 92 Q64 78 90 86" fill="#FFF3D6" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 110 l4 -6 l4 6z" fill="#E0A848" {W(1.6)}/>' for x in (34, 86))
    + face(64, 102, d=8, k=0.6) +
    # свеча
    f'<rect x="88" y="58" width="10" height="26" rx="2" fill="#FFF6E0" {W(2.2)}/>'
    f'<path d="M93 46 q-6 8 0 12 q6 -4 0 -12z" fill="#FFB020" {W(1.8)}/>'
    # ключ
    f'<g transform="rotate(-30 56 54)"><circle cx="46" cy="54" r="7" fill="none" stroke="#FFD23F" stroke-width="4"/>'
    f'<path d="M53 54 H74 M68 54 V60 M72 54 V59" stroke="#FFD23F" stroke-width="4" stroke-linecap="round"/></g>'
    + sparkle(40, 40, 4, "#FFE680") + sparkle(76, 36, 3, "#FFE680"))

# 14. Галерея «Дали Пикассо» — мягкие стекающие часы с закрученными усами висят на сухой ветке в жёлтой пустыне
I["fun-dali-picasso-basmannaya"] = ("#FFE9A8", "#E08A2E",
    "мягкие стекающие карманные часы с закрученными усами",
    "свисают с ветки сухого деревца посреди жаркой жёлтой пустыни",
    f'<path d="M0 96 Q64 86 128 96 V128 H0Z" fill="#F2C35B" {W(3)}/>'
    f'<path d="M86 116 Q80 70 92 40 M90 58 Q100 50 108 52" fill="none" stroke="#7A4A2A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M92 40 Q60 36 40 42" fill="none" stroke="#7A4A2A" stroke-width="4" stroke-linecap="round"/>'
    # часы стекают
    f'<path d="M30 42 Q30 26 52 28 Q72 30 70 46 Q68 60 62 70 Q58 82 50 84 Q46 74 44 66 Q30 60 30 42Z" fill="#9EC9FF" {W(3)}/>'
    f'<circle cx="52" cy="28" r="4" fill="#FFD23F" {W(2)}/>'
    f'<path d="M50 44 L50 36 M50 44 L58 48" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + eye(42, 52, 0.55) + eye(58, 52, 0.55) +
    f'<path d="M50 58 q-6 -4 -12 2 q4 -6 12 -6 q8 0 12 6 q-6 -6 -12 -2z" fill="{O}"/>'
    f'<circle cx="100" cy="22" r="10" fill="#FF8A3A" opacity=".9"/>'
    + sparkle(16, 24, 4, "#fff"))

# 15. Клуб «Молоточек» — юный столяр в очках и фартуке собирает деревянный кораблик на верстаке
I["fun-molotochek-khovrino"] = ("#E8F5DA", "#6E9E46",
    "мальчик-столяр в жёлтых защитных очках и кожаном фартуке",
    "стучит маленьким молотком, собирая деревянный кораблик на верстаке",
    # верстак
    f'<rect x="6" y="90" width="116" height="12" rx="3" fill="#C98A4B" {W(3)}/>'
    f'<path d="M16 102 V126 M112 102 V126" stroke="{O}" stroke-width="5"/>'
    # кораблик
    f'<path d="M70 74 H118 L110 90 H78Z" fill="#E0A060" {W(2.8)}/>'
    f'<path d="M94 74 V44 L114 70Z" fill="#FFF6E0" {W(2.4)}/>'
    f'<path d="M94 50 L80 70 H94" fill="#FFE0A0" {W(2.2)}/>'
    # мальчик
    f'<path d="M20 90 Q20 62 40 60 Q58 62 58 90Z" fill="#7A5236" {W(3)}/>'
    f'<path d="M30 70 H50" stroke="#5A3A24" stroke-width="2"/>'
    f'<circle cx="40" cy="42" r="16" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M24 36 Q28 22 42 24 Q54 26 56 36 Q44 30 24 36Z" fill="#2E2E3A" {W(2.4)}/>'
    f'<rect x="28" y="38" width="10" height="7" rx="3" fill="#FFE14F" {W(2)}/><rect x="42" y="38" width="10" height="7" rx="3" fill="#FFE14F" {W(2)}/>'
    f'<path d="M38 41 H42" stroke="{O}" stroke-width="2"/>'
    f'<path d="M36 50 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    # рука с молотком
    f'<path d="M52 72 L70 60" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M52 72 L70 60" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M68 62 L74 48" stroke="#8C5A30" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="66" y="40" width="18" height="9" rx="2" fill="#8A93A6" {W(2.4)} transform="rotate(20 75 44)"/>'
    f'<path d="M86 30 l4 -6 M92 36 l7 -3" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(110, 18, 5, "#fff"))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
