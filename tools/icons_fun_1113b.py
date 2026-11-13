"""Иконки робота fun (2026-11-13, проход b): места из tools/add_fun_1113b.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1113b.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Пеленальная в ТРЦ «Саларис» — махровое полотенце-уголок с медвежьими ушками сушится на круглой сушилке с прищепками
I["chg-trc-salaris"] = ("#FFF1DC", "#E89A5C",
    "махровое персиковое полотенце-уголок с капюшоном и медвежьими ушками",
    "сушится, свесившись с круглой белой сушилки-вертушки на прищепках",
    # сушилка: кольцо и крючок
    f'<path d="M64 6 V20" stroke="{O}" stroke-width="3"/>'
    f'<path d="M58 8 Q64 0 70 8" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="26" rx="44" ry="8" fill="none" stroke="#FFFFFF" stroke-width="7"/>'
    f'<ellipse cx="64" cy="26" rx="44" ry="8" fill="none" stroke="{O}" stroke-width="2.4"/>'
    f'<path d="M64 20 L28 26 M64 20 L100 26" stroke="{O}" stroke-width="2"/>'
    # полотенце-треугольник с капюшоном
    f'<path d="M22 30 L106 30 Q100 74 64 118 Q28 74 22 30Z" fill="#FFC79A" {W(3.2)}/>'
    f'<path d="M30 40 L98 40 M36 56 L92 56 M44 74 L84 74" stroke="#F0A672" stroke-width="2.4" stroke-dasharray="3 4"/>'
    # прищепки
    f'<rect x="30" y="20" width="8" height="16" rx="2" fill="#7FD3F0" {W(2.2)}/>'
    f'<rect x="90" y="20" width="8" height="16" rx="2" fill="#7FD3F0" {W(2.2)}/>'
    # капюшон с ушками
    f'<circle cx="46" cy="58" r="8" fill="#FFC79A" {W(2.8)}/><circle cx="82" cy="58" r="8" fill="#FFC79A" {W(2.8)}/>'
    f'<circle cx="46" cy="58" r="4" fill="#F59A8A"/><circle cx="82" cy="58" r="4" fill="#F59A8A"/>'
    f'<path d="M42 70 Q64 52 86 70 Q88 94 64 100 Q40 94 42 70Z" fill="#FFDDBE" {W(3)}/>'
    + face(64, 80, d=8, k=0.8) + sparkle(112, 70, 5, "#fff") + sparkle(14, 84, 4, "#fff"))

# 2. Пеленальная в ТРЦ «Кузьминки Молл» — ночник-полумесяц с колпачком светит, на стене пятнышки-звёзды
I["chg-kuzminki-mall"] = ("#4B4F9E", "#1F2260",
    "детский ночник-полумесяц из матового стекла на деревянной подставке",
    "сонно щурится и светит тёплым светом, рассыпая по тёмной стене маленькие звёздочки",
    # звёздочки
    "".join(sparkle(x, y, r, "#FFF3C2") for x, y, r in ((22, 30, 5), (104, 26, 4), (108, 70, 5), (18, 74, 3.5), (88, 14, 3)))
    # подставка
    + f'<rect x="34" y="100" width="60" height="14" rx="5" fill="#C98A4B" {W(3)}/>'
    f'<path d="M58 100 V92 H70 V100" fill="#B5763A" {W(2.6)}/>'
    # полумесяц
    f'<path d="M80 28 A34 34 0 1 0 80 92 A26 26 0 1 1 80 28Z" fill="#FFE07A" {W(3.2)}/>'
    f'<path d="M36 44 Q34 52 36 58" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    # сонные глазки-дуги и улыбка
    f'<path d="M42 62 q4 4 8 0 M56 66 q4 4 8 0" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M48 76 q5 4 10 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    f'<ellipse cx="42" cy="72" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
    f'<text x="88" y="50" font-family="Arial" font-weight="bold" font-size="12" fill="#FFF3C2">z</text>'
    f'<text x="96" y="40" font-family="Arial" font-weight="bold" font-size="9" fill="#FFF3C2">z</text>')

# 3. Пеленальная в ТРЦ «Ботаника» — непромокаемая пелёнка в виде листа лопуха расстелена, на ней лежит свёрнутый подгузник
I["chg-botanica"] = ("#EAFBE0", "#5FB35A",
    "непромокаемая пеленальная клеёнка в виде огромного зелёного листа лопуха с прожилками",
    "расстелена на белом столике, а в серединке лежит подгузник, свёрнутый бутоном с розовой ленточкой",
    # столик
    f'<rect x="8" y="94" width="112" height="10" rx="5" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M22 104 V126 M106 104 V126" stroke="{O}" stroke-width="4"/>'
    # лист лопуха наискосок, острым кончиком вверх-вправо, черешок вниз-влево
    f'<path d="M14 100 Q10 50 50 30 Q86 12 120 10 Q118 50 96 78 Q66 106 14 100Z" fill="#9BE07A" {W(3.2)}/>'
    f'<path d="M14 100 L112 18 M40 78 L30 52 M40 78 L64 86 M60 62 L54 34 M60 62 L88 70 M82 44 L80 22 M82 44 L104 48" '
    f'fill="none" stroke="#5DAF4A" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M14 100 Q8 112 2 118" fill="none" stroke="#5DAF4A" stroke-width="6" stroke-linecap="round"/>'
    # подгузник-бутон
    f'<path d="M50 60 Q48 40 64 34 Q80 40 78 60 Q64 68 50 60Z" fill="#FFFFFF" {W(2.8)}/>'
    f'<path d="M56 56 Q58 44 64 40 Q70 44 72 56" fill="none" stroke="#C9C2D8" stroke-width="2"/>'
    f'<path d="M52 56 Q64 62 76 56" fill="none" stroke="#FF8FB8" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M64 58 l-6 8 M64 58 l6 8" stroke="#FF8FB8" stroke-width="3" stroke-linecap="round"/>'
    + face(64, 48, d=5, k=0.5, mouth=False)
    + sparkle(24, 22, 5, "#fff") + sparkle(108, 96, 3.5, "#fff"))

# 4. Пеленальная в ТРЦ «Щёлковский» (комнаты на 4 этажах) — прозрачный лифт с мордашкой везёт вверх коляску
I["chg-trc-shchelkovsky"] = ("#FDE3F0", "#C46BA6",
    "прозрачная кабина панорамного лифта с золотой рамкой и мордашкой на табло",
    "плавно везёт вверх по стеклянной шахте маленькую голубую коляску, а сбоку светятся цифры этажей 1, 2, 4, 5",
    # шахта
    f'<rect x="34" y="4" width="60" height="124" fill="#FFFFFF" opacity=".35" {W(2.4)}/>'
    f'<path d="M64 4 V22" stroke="{O}" stroke-width="2.6"/>'
    # цифры этажей
    + "".join(f'<circle cx="108" cy="{y}" r="7" fill="{c}" {W(2)}/><text x="108" y="{y+4}" text-anchor="middle" '
              f'font-family="Arial" font-weight="bold" font-size="10" fill="{O}">{n}</text>'
              for y, n, c in ((106, 1, "#FFFFFF"), (84, 2, "#FFFFFF"), (62, 4, "#FFE07A"), (40, 5, "#FFFFFF")))
    # кабина
    + f'<rect x="30" y="22" width="68" height="84" rx="6" fill="#DFF4FF" opacity=".9" {W(3.2)}/>'
    f'<rect x="30" y="22" width="68" height="16" rx="6" fill="#F2C14E" {W(3)}/>'
    + face(64, 29, d=7, k=0.55) +
    f'<path d="M40 44 L46 98 M88 44 L82 98" stroke="#fff" stroke-width="3" opacity=".8"/>'
    f'<path d="M64 6 l-5 6 h10z" fill="#5CC56F" {W(1.8)}/>'
    # коляска
    f'<path d="M42 66 Q42 54 54 52 L60 52 L60 72 L86 72 Q86 84 72 86 H52 Q42 84 42 72Z" fill="#7DC4F5" {W(2.8)}/>'
    f'<path d="M60 52 Q76 50 82 66 L60 66Z" fill="#4F9FDB" {W(2.6)}/>'
    f'<path d="M86 72 L94 60" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="52" cy="94" r="6" fill="#fff" {W(2.6)}/><circle cx="78" cy="94" r="6" fill="#fff" {W(2.6)}/>'
    + sparkle(16, 30, 5, "#fff") + sparkle(18, 96, 3.5, "#fff"))

# 5. Пеленальная в ТРК «Vegas» (Каширское) — детские весы-люлька, стрелка на сердечке, в чаше подушка-звёздочка
I["chg-vegas-kashirskoe"] = ("#E3F6F2", "#3FA597",
    "белые детские весы для новорождённых с овальной чашей-люлькой и круглым циферблатом-мордашкой",
    "стоят на пеленальном столике: стрелка показывает на сердечко, а в чаше лежит пухлая жёлтая подушечка-звёздочка",
    # основание
    f'<path d="M24 112 H104 L96 88 H32Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<path d="M14 118 H114" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    # циферблат
    f'<circle cx="64" cy="94" r="12" fill="#FFF7E0" {W(2.6)}/>'
    f'<path d="M58 92 c0 -4 6 -4 6 0 c0 -4 6 -4 6 0 c0 4 -6 8 -6 8 c0 0 -6 -4 -6 -8z" fill="#FF7FA8" transform="translate(0 -4) scale(1)"/>'
    f'<path d="M64 100 L70 90" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + eye(50, 100, 0.55) + eye(78, 100, 0.55) +
    # стойка и чаша
    f'<path d="M58 88 V78 H70 V88" fill="#E7E3F0" {W(2.4)}/>'
    f'<path d="M12 54 Q16 82 64 82 Q112 82 116 54Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<path d="M20 58 Q24 74 64 74 Q104 74 108 58" fill="none" stroke="#9EDCD2" stroke-width="3"/>'
    # подушка-звёздочка
    f'<path d="M64 22 L72 40 L92 42 L77 55 L82 74 L64 64 L46 74 L51 55 L36 42 L56 40Z" fill="#FFD84D" {W(3)}/>'
    + face(64, 50, d=6, k=0.6) + sparkle(104, 24, 5, "#fff") + sparkle(22, 30, 4, "#fff"))

# 6. Квест «НеДетские Прятки» (Подольск) — мальчик со светящимся браслетом выглядывает из-за коробки в тёмной комнате
I["fun-nedetskie-pryatki-podolsk"] = ("#3A2F6B", "#140F33",
    "мальчик в оранжевой толстовке со светящимся зелёным неоновым браслетом",
    "прячется в тёмной комнате за большой картонной коробкой — видны только макушка, глаза и рука с браслетом",
    # луч фонарика ищущего
    f'<path d="M128 10 L40 40 L56 70 Z" fill="#FFF7B0" opacity=".18"/>'
    + "".join(sparkle(x, y, r, "#B9F7FF") for x, y, r in ((20, 22, 3), (100, 96, 3), (14, 60, 2.5)))
    # голова за коробкой
    + f'<circle cx="62" cy="58" r="22" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M40 54 Q42 30 64 32 Q86 32 86 54 Q78 42 64 44 Q50 42 40 54Z" fill="#6B4226" {W(2.6)}/>'
    + eye(54, 60, 0.85) + eye(72, 60, 0.85) +
    # рука с браслетом на краю коробки
    f'<circle cx="94" cy="72" r="6" fill="#FFD9B8" {W(2.6)}/>'
    f'<path d="M86 74 h10" stroke="#5CFF8A" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="91" cy="74" r="9" fill="#5CFF8A" opacity=".25"/>'
    # коробка
    f'<path d="M18 74 H110 L106 126 H22Z" fill="#D69A55" {W(3.2)}/>'
    f'<path d="M18 74 L10 62 H50 L58 74 M110 74 L118 62 H78 L70 74" fill="#E8B36E" {W(2.6)}/>'
    f'<path d="M64 74 V126" stroke="#B57A3A" stroke-width="3"/>'
    f'<path d="M30 96 h18 M30 104 h12" stroke="#B57A3A" stroke-width="2.4" stroke-linecap="round"/>'
    f'<text x="88" y="108" font-family="Arial" font-weight="bold" font-size="14" fill="{O}">?</text>')

# 7. VR-клуб OASIS (Подольск) — пальма оазиса в VR-шлеме у голубого озерца среди дюн
I["fun-oasis-vr-podolsk"] = ("#FFF2C9", "#F2A33A",
    "финиковая пальма с мордашкой на стволе, в фиолетовом VR-шлеме на кроне",
    "стоит у голубого озерца среди песчаных дюн и тянет листья к пиксельным звёздам из виртуальности",
    # дюны и озеро
    f'<path d="M0 100 Q30 84 60 96 Q92 84 128 98 V128 H0Z" fill="#F7C873" {W(3)}/>'
    f'<ellipse cx="88" cy="108" rx="28" ry="7" fill="#6CCBF0" {W(2.6)}/>'
    # пиксели
    + "".join(f'<rect x="{x}" y="{y}" width="7" height="7" fill="{c}" {W(1.6)}/>'
              for x, y, c in ((14, 22, "#7FE0FF"), (24, 12, "#C79BFF"), (104, 18, "#7FE0FF"), (112, 32, "#FF9AD5")))
    # ствол
    + f'<path d="M50 104 Q46 80 54 54 L66 54 Q60 80 64 104Z" fill="#B97A45" {W(3)}/>'
    f'<path d="M50 90 h13 M51 78 h12 M53 66 h11" stroke="#8C5A30" stroke-width="2.2"/>'
    f'<ellipse cx="50" cy="86" rx="3" ry="2" fill="#FF7FA8" opacity=".7"/>'
    f'<path d="M54 94 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    # листья
    f'<path d="M60 52 Q30 34 12 48 Q34 42 58 56Z M60 52 Q90 32 114 46 Q90 42 62 58Z M60 50 Q44 22 26 22 Q46 30 58 52Z '
    f'M60 50 Q78 20 100 22 Q80 30 62 52Z" fill="#4FBF5F" {W(2.6)}/>'
    # VR-шлем на кроне
    f'<rect x="40" y="38" width="42" height="20" rx="9" fill="#8B5CF6" {W(3)}/>'
    f'<rect x="46" y="42" width="30" height="12" rx="6" fill="#7FE0FF" {W(2)}/>'
    f'<path d="M50 46 h6 M62 46 h8" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    + sparkle(30, 70, 4, "#fff"))

# 8. VR-клуб VrRealTeam (Новокосино) — девочка с косой в VR-шлеме балансирует на светящейся доске над пиксельной пропастью
I["fun-vrrealteam-novokosino"] = ("#D7F3FF", "#2E6FB8",
    "девочка с рыжей косой-колоском в бирюзовом VR-шлеме и с двумя светящимися контроллерами",
    "балансирует, раскинув руки, на узкой светящейся доске над пропастью из голубых пикселей",
    # пропасть из пикселей
    "".join(f'<rect x="{x}" y="{y}" width="10" height="10" fill="{c}" opacity=".85"/>'
            for x, y, c in ((6, 104, "#1B3F7A"), (18, 112, "#24539B"), (98, 106, "#1B3F7A"), (110, 114, "#24539B"),
                            (30, 120, "#1B3F7A"), (84, 120, "#24539B"), (56, 122, "#1B3F7A")))
    # доска
    + f'<rect x="20" y="92" width="88" height="8" rx="4" fill="#7FFFE0" {W(2.8)}/>'
    f'<rect x="16" y="88" width="96" height="16" rx="8" fill="#7FFFE0" opacity=".25"/>'
    # ноги
    f'<path d="M58 92 L56 76 M70 92 L72 76" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    # платье
    f'<path d="M48 78 L54 52 H74 L80 78Z" fill="#FF8FB8" {W(3)}/>'
    # руки с контроллерами
    f'<path d="M56 56 L30 50 M72 56 L98 50" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M56 56 L30 50 M72 56 L98 50" stroke="#FFD9B8" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="26" cy="48" r="6" fill="#2B2B3A" {W(2)}/><circle cx="26" cy="48" r="9" fill="none" stroke="#7FFFE0" stroke-width="2.4"/>'
    f'<circle cx="102" cy="48" r="6" fill="#2B2B3A" {W(2)}/><circle cx="102" cy="48" r="9" fill="none" stroke="#7FFFE0" stroke-width="2.4"/>'
    # голова и коса
    f'<path d="M78 32 Q92 40 90 58 Q88 66 94 72" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M78 32 Q92 40 90 58 Q88 66 94 72" fill="none" stroke="#F08A3A" stroke-width="4.5" stroke-linecap="round"/>'
    f'<circle cx="64" cy="34" r="16" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M48 30 Q50 16 64 16 Q78 16 80 30 Q70 24 64 26 Q56 24 48 30Z" fill="#F08A3A" {W(2.4)}/>'
    f'<rect x="48" y="28" width="32" height="12" rx="6" fill="#3EC6C0" {W(2.6)}/>'
    f'<path d="M54 34 h20" stroke="#E0FFFB" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M58 44 q6 4 12 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(110, 20, 5, "#fff") + sparkle(16, 22, 3.5, "#fff"))

# 9. Игровое пространство Wonderland (Королёв) — девочка выныривает из сухого бассейна, подбрасывая шарики
I["fun-wonderland-korolev"] = ("#FFF0F5", "#F27BA8",
    "девочка с двумя светлыми косичками в жёлтом платье",
    "выныривает по пояс из сухого бассейна с мягким бортиком и подбрасывает вверх пригоршню разноцветных шариков",
    # летящие шарики
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(2)}/>'
            for x, y, r, c in ((24, 26, 6, "#5BC0F8"), (44, 12, 5, "#FFD23F"), (86, 14, 6, "#7BE87B"), (106, 30, 5, "#FF6B6B"),
                               (100, 52, 4.5, "#B98BFF"), (20, 50, 4.5, "#FF9F43")))
    # руки вверх
    + f'<path d="M50 74 L36 44 M78 74 L92 44" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M50 74 L36 44 M78 74 L92 44" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    # туловище
    f'<path d="M46 98 L50 72 H78 L82 98Z" fill="#FFD84D" {W(3)}/>'
    # голова и косички
    f'<path d="M44 58 Q32 66 36 80 M84 58 Q96 66 92 80" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M44 58 Q32 66 36 80 M84 58 Q96 66 92 80" fill="none" stroke="#F7D57A" stroke-width="3.6" stroke-linecap="round"/>'
    f'<circle cx="64" cy="56" r="17" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M47 52 Q50 36 64 36 Q78 36 81 52 Q72 44 64 46 Q56 44 47 52Z" fill="#F7D57A" {W(2.4)}/>'
    + face(64, 58, d=6, k=0.6) +
    # бассейн с шариками
    f'<rect x="6" y="90" width="116" height="34" rx="12" fill="#FFFFFF" {W(3.2)}/>'
    f'<rect x="14" y="96" width="100" height="24" rx="8" fill="#FFE3EE"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6.5" fill="{c}" {W(1.8)}/>'
              for x, y, c in ((22, 100, "#5BC0F8"), (34, 98, "#FF6B6B"), (46, 101, "#7BE87B"), (82, 101, "#FFD23F"),
                              (94, 98, "#B98BFF"), (106, 100, "#5BC0F8"), (30, 110, "#FFD23F"), (98, 110, "#FF6B6B"),
                              (64, 108, "#5BC0F8"), (52, 112, "#FF9F43"), (76, 112, "#7BE87B"))))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
