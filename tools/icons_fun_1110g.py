"""Иконки робота fun (2026-11-10, дневной проход 3): места из tools/add_fun_1110g.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1110g.py"""
import os
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg, openbook

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. пр-т Мира, 198 — рядом Ростокинский акведук
I["lib-kids-mira-198"] = ("#FCEFE6", "#C9805E",
    "старый кирпичный Ростокинский акведук с арками и мордашкой на среднем пролёте",
    "по его каменному жёлобу, как по реке, плывёт раскрытая книжка-лодочка, а под арками течёт голубая Яуза",
    f'<path d="M-2 104 Q64 96 130 104 V130 H-2Z" fill="#6FB7E0" {W(3)}/>'
    f'<path d="M14 112 Q24 108 34 112 M90 114 Q100 110 110 114" fill="none" stroke="#fff" stroke-width="2.4"/>'
    f'<path d="M-2 58 H130 V104 H108 Q108 80 94 80 Q80 80 80 104 H48 Q48 80 34 80 Q20 80 20 104 H-2Z" fill="#D9774B" {W(3.2)}/>'
    f'<path d="M-2 58 H130 V50 H-2Z" fill="#B85C36" {W(2.8)}/>'
    + "".join(f'<path d="M{x} 68 h10 M{x+6} 76 h10" stroke="#B85C36" stroke-width="2"/>' for x in (2, 54, 104)) +
    face(64, 76, d=8, k=0.75) +
    openbook(64, 30, 34, 14, "#3E9E5A", tilt=3) +
    f'<path d="M40 50 Q52 44 64 48 Q76 52 88 46" fill="none" stroke="#9FD8F2" stroke-width="3"/>'
    + sparkle(108, 26, 6) + sparkle(22, 30, 4))

# 2. Задонский пр-д — плетёное кресло-качалка
I["lib153-zadonsky"] = ("#FFF7E0", "#D8A43C",
    "плетёное кресло-качалка с мордашкой на спинке",
    "покачивается у окна, а на сиденье лежит раскрытая книжка и клетчатый плед",
    f'<rect x="18" y="14" width="40" height="44" rx="4" fill="#BFE6FA" {W(2.6)}/>'
    f'<path d="M38 14 V58 M18 36 H58" stroke="{O}" stroke-width="2.4"/>'
    f'<path d="M50 30 Q42 8 64 6 Q90 6 88 34 L84 74 H54Z" fill="#E8B866" {W(3)}/>'
    + "".join(f'<path d="M{56+i*6} 14 Q{58+i*6} 44 {56+i*5} 72" fill="none" stroke="#C48A2E" stroke-width="2"/>' for i in range(5)) +
    face(70, 34, d=8, k=0.75) +
    f'<path d="M44 74 H96 L92 84 H48Z" fill="#D59A3E" {W(3)}/>'
    f'<path d="M50 84 L46 102 M90 84 L94 102" stroke="#A86E22" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M24 104 Q70 118 116 98" fill="none" stroke="#A86E22" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M84 72 L104 64 L108 86 L88 90Z" fill="#E2504A" {W(2.4)}/>'
    f'<path d="M90 70 L94 88 M98 66 L102 86 M86 78 L106 72" stroke="#fff" stroke-width="1.8"/>'
    + openbook(64, 62, 26, 9, "#4A7FD4", lines=False, tilt=2) + sparkle(104, 22, 5))

# 3. ул. Гончарова — бархатный диван (привет Обломову)
I["lib60-goncharova"] = ("#EAF7EE", "#4FA36E",
    "зелёный бархатный диван с мордашкой и кисточками на валиках",
    "сладко дремлет, на подлокотнике раскрытая книга, а внизу ждут мягкие домашние тапочки",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#B9845A" {W(3)}/>'
    f'<path d="M22 46 Q22 34 36 34 H92 Q106 34 106 46 V68 H22Z" fill="#2F8F57" {W(3)}/>'
    f'<path d="M14 66 H114 V90 H14Z" fill="#3DA867" {W(3)}/>'
    f'<ellipse cx="16" cy="66" rx="10" ry="12" fill="#2F8F57" {W(3)}/><ellipse cx="112" cy="66" rx="10" ry="12" fill="#2F8F57" {W(3)}/>'
    f'<path d="M6 76 l-2 8 M122 76 l2 8" stroke="#F2C44A" stroke-width="3"/>'
    f'<path d="M24 90 V100 M104 90 V100" stroke="#6E4A2A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M52 50 Q56 54 60 50 M68 50 Q72 54 76 50" fill="none" {W(2.6)}/>'
    f'<ellipse cx="48" cy="58" rx="5" ry="2.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="80" cy="58" rx="5" ry="2.8" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M60 60 Q64 63 68 60" fill="none" {W(2.4)}/>'
    + openbook(104, 40, 24, 9, "#C84A4A", lines=False, tilt=2) +
    f'<ellipse cx="44" cy="112" rx="11" ry="5" fill="#E86F8E" {W(2.4)}/><ellipse cx="66" cy="114" rx="11" ry="5" fill="#E86F8E" {W(2.4)}/>'
    f'<text x="84" y="26" font-family="Arial" font-weight="bold" font-size="13" fill="#fff" stroke="{O}" stroke-width="1">z</text>'
    f'<text x="96" y="16" font-family="Arial" font-weight="bold" font-size="10" fill="#fff" stroke="{O}" stroke-width="1">z</text>')

# 4. пр-т Андропова — медный ключ отпирает книгу-сундучок
I["lib122-andropova"] = ("#F3ECFF", "#7A5BC8",
    "старинный медный ключ с узорной головкой-мордашкой",
    "сам повернулся в замочке толстой книги-сундучка, и из щели между страницами полился золотой свет",
    f'<path d="M20 76 H98 V108 H20Z" fill="#8C3B2E" {W(3)}/>'
    f'<path d="M24 70 H102 L98 76 H20Z" fill="#FFF6DA" {W(2.4)}/>'
    f'<path d="M20 66 H98 V72 H20Z" fill="#8C3B2E" {W(2.6)}/>'
    f'<path d="M30 70 L10 30 M54 70 L48 20 M78 70 L92 22 M96 70 L118 38" stroke="#FFE27A" stroke-width="5" opacity=".7"/>'
    f'<rect x="52" y="80" width="18" height="20" rx="3" fill="#E2B34A" {W(2.4)}/>'
    f'<path d="M61 86 V94" stroke="{O}" stroke-width="3"/>'
    f'<path d="M66 90 H96" stroke="#C88A3A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M90 90 V98 M84 90 V96" stroke="#C88A3A" stroke-width="4"/>'
    f'<circle cx="104" cy="90" r="15" fill="#D99A44" {W(3)}/>'
    + face(104, 88, d=5, k=0.5) + sparkle(64, 46, 7, "#FFF3B0") + sparkle(30, 40, 4, "#FFF3B0"))

# 5. Балтийская ул. — соломенный улей и пчёлки-буквы
I["lib31-baltiyskaya"] = ("#FFFBE0", "#E3B72C",
    "соломенный улей-колпак с мордашкой",
    "из летка вылетают пчёлки, каждая несёт по букве, и они складывают слово «МИР» над раскрытой книгой",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#8DC45A" {W(3)}/>'
    f'<path d="M30 106 Q26 50 64 40 Q102 50 98 106Z" fill="#F0C565" {W(3.2)}/>'
    + "".join(f'<path d="M{34-i} {58+i*12} Q64 {52+i*12} {94+i} {58+i*12}" fill="none" stroke="#C99A32" stroke-width="2.6"/>' for i in range(4)) +
    face(64, 70, d=10, k=0.8) +
    f'<ellipse cx="64" cy="96" rx="8" ry="5" fill="#5A3A1A" {W(2.2)}/>'
    + openbook(64, 100, 44, 10, "#3A7BD5", lines=False, tilt=2) +
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="4" fill="#F7C934" {W(1.8)}/><path d="M{x-2} {y-4} v8 M{x+2} {y-4} v8" stroke="{O}" stroke-width="1.6"/>'
            f'<ellipse cx="{x-2}" cy="{y-6}" rx="3" ry="2" fill="#fff" opacity=".85"/>'
            f'<text x="{x-5}" y="{y-9}" font-family="Arial" font-weight="bold" font-size="11" fill="#D2452E">{ch}</text>'
            for x, y, ch in ((36, 30, "М"), (64, 22, "И"), (92, 30, "Р"))))

# 6. Вятская ул. — дымковская барыня
I["lib40-vyatskaya"] = ("#E9F1FF", "#3E6FCF",
    "дымковская глиняная барыня в пышной юбке в кружочек и высоком кокошнике",
    "стоит на подставке и, как веером, раскрыла над головой маленькую книжку со сказками",
    f'<ellipse cx="64" cy="112" rx="34" ry="7" fill="#7E9BD6" {W(2.4)}/>'
    f'<path d="M30 110 Q34 66 64 62 Q94 66 98 110Z" fill="#FFFFFF" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}" {W(1.4)}/>' for x, y, c in
              ((44, 98, "#E8434A"), (58, 102, "#F2B33A"), (72, 102, "#3B7DD8"), (86, 98, "#E8434A"),
               (50, 84, "#3B7DD8"), (64, 86, "#E8434A"), (78, 84, "#F2B33A"), (64, 72, "#3B7DD8"))) +
    f'<path d="M30 110 Q64 116 98 110" fill="none" stroke="#E8434A" stroke-width="3"/>'
    f'<path d="M52 66 Q52 50 64 50 Q76 50 76 66Z" fill="#F2B33A" {W(2.6)}/>'
    f'<circle cx="64" cy="40" r="12" fill="#FFF6EE" {W(2.8)}/>'
    + eye(59, 39, 0.5) + eye(69, 39, 0.5) +
    f'<circle cx="57" cy="45" r="2.6" fill="#E8434A"/><circle cx="71" cy="45" r="2.6" fill="#E8434A"/>'
    f'<path d="M50 30 Q52 12 64 10 Q76 12 78 30 Q64 24 50 30Z" fill="#E8434A" {W(2.6)}/>'
    f'<circle cx="64" cy="18" r="3" fill="#F2B33A"/>'
    f'<path d="M54 56 L34 34 M74 56 L94 34" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    + openbook(64, 14, 64, 14, "#2FA36B", tilt=5, lines=False) + sparkle(110, 70, 5))

# 7. Саянская ул. — кедровка с орешком
I["lib74-sayanskaya"] = ("#E6F6F0", "#2E8A6E",
    "пёстрая птица-кедровка в белых крапинках с длинным клювом",
    "сидит на ветке сибирского кедра и вместо шишки раскалывает клювом обложку книги «Саяны»",
    f'<path d="M-4 84 Q60 74 132 66" fill="none" stroke="#6E4628" stroke-width="10" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} l-10 -14 M{x} {y} l0 -18 M{x} {y} l10 -14" stroke="#2F7A3E" stroke-width="3" stroke-linecap="round"/>'
              for x, y in ((14, 80), (104, 68), (122, 64))) +
    f'<path d="M40 76 Q34 44 58 36 Q80 34 82 58 Q82 78 62 82Z" fill="#6B4A32" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in ((50, 54), (58, 62), (66, 52), (48, 68), (70, 68), (60, 74), (56, 46))) +
    f'<path d="M34 76 L20 98 L44 82Z" fill="#3E2A1E" {W(2.6)}/>'
    f'<circle cx="68" cy="40" r="13" fill="#5A3E2A" {W(2.8)}/>'
    + eye(72, 37, 0.6) +
    f'<path d="M80 40 L104 46 L80 48Z" fill="#2A2A2A" {W(2)}/>'
    f'<rect x="92" y="44" width="26" height="20" rx="2" fill="#E9563A" {W(2.4)}/>'
    f'<path d="M96 50 H114 M96 56 H110" stroke="#fff" stroke-width="2"/>'
    f'<path d="M58 82 l-4 8 M66 82 l2 8" stroke="#3E2A1E" stroke-width="3"/>' + sparkle(20, 30, 5))

# 8. Химкинский б-р — сенсорная комната: пузырьковая колонна
I["lib226-khimkinsky"] = ("#2A2C5E", "#121236",
    "высокая светящаяся пузырьковая колонна сенсорной комнаты с рыбками и мордашкой",
    "переливается то розовым, то голубым, а у подножия на мягком пуфе лежит раскрытая книжка",
    f'<ellipse cx="64" cy="112" rx="40" ry="8" fill="#3E3F7A" {W(2.4)}/>'
    f'<rect x="46" y="14" width="36" height="88" rx="16" fill="#7FD8F0" {W(3.2)}/>'
    f'<path d="M48 60 H80 V86 Q80 100 64 100 Q48 100 48 86Z" fill="#E87FD0" opacity=".6"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x, y, r in
              ((56, 90, 3), (70, 80, 2.4), (60, 66, 2), (72, 52, 3), (56, 40, 2.2), (66, 26, 2.6))) +
    f'<path d="M58 72 q6 -6 12 0 q-6 6 -12 0Z M70 72 l5 -4 v8Z" fill="#F7A72E" {W(1.6)}/>'
    + face(64, 46, d=7, k=0.65) +
    f'<rect x="44" y="96" width="40" height="12" rx="4" fill="#5A5BB0" {W(2.6)}/>'
    f'<ellipse cx="102" cy="104" rx="18" ry="9" fill="#F0B23A" {W(2.6)}/>'
    + openbook(102, 88, 26, 8, "#E8434A", lines=False, tilt=2) +
    sparkle(22, 30, 5, "#FFE680") + sparkle(108, 26, 4, "#9FE6FF") + sparkle(26, 80, 3, "#FF9FD8"))

# 9. Домодедовская ул. — гном-книжник
I["lib-kids-domodedovskaya-44"] = ("#FFEFEF", "#D0565E",
    "маленький гном с белой бородой до пояса в красном колпаке",
    "поднимается по деревянной стремянке к верхней полке и несёт книгу больше себя",
    f'<rect x="78" y="8" width="44" height="110" fill="#A4693E" {W(3)}/>'
    + "".join(f'<path d="M78 {y} H122" stroke="{O}" stroke-width="3"/>' for y in (40, 74)) +
    "".join(f'<rect x="{x}" y="{y}" width="7" height="24" rx="1.5" fill="{c}" {W(1.6)}/>' for x, y, c in
            ((82, 15, "#3B7DD8"), (90, 15, "#F2B33A"), (98, 18, "#2FA36B"), (106, 15, "#9C5BD6"),
             (82, 49, "#E8434A"), (90, 52, "#3B7DD8"), (98, 49, "#F2B33A"), (106, 49, "#2FA36B"), (114, 52, "#E8434A"))) +
    f'<path d="M30 122 L62 20 M52 122 L80 30" stroke="#D9A160" stroke-width="5" stroke-linecap="round"/>'
    + "".join(f'<path d="M{34+i*7.5} {110-i*21} H{57+i*6}" stroke="#D9A160" stroke-width="4" stroke-linecap="round"/>' for i in range(4)) +
    f'<path d="M38 78 Q36 56 50 54 Q64 56 62 80Z" fill="#3A6FC2" {W(2.6)}/>'
    f'<path d="M42 50 Q38 66 50 74 Q62 66 58 50Z" fill="#FFFFFF" {W(2.4)}/>'
    f'<circle cx="50" cy="44" r="9" fill="#FFD9C0" {W(2.4)}/>'
    + eye(46, 43, 0.45) + eye(54, 43, 0.45) +
    f'<path d="M40 40 Q46 14 66 24 Q54 30 60 40Z" fill="#E8434A" {W(2.6)}/>'
    f'<rect x="54" y="56" width="22" height="28" rx="2" fill="#2FA36B" {W(2.6)}/>'
    f'<path d="M58 62 H72 M58 68 H70" stroke="#fff" stroke-width="2"/>'
    f'<path d="M44 80 L42 92 M56 80 L58 90" stroke="#5A3A1A" stroke-width="4" stroke-linecap="round"/>')

# 10. Музей ВМФ в Северном Тушине — экраноплан «Орлёнок»
I["vmf-museum-tushino"] = ("#E4F4FF", "#2C7FC0",
    "серо-голубой экраноплан «Орлёнок» с мордашкой-кабиной и высоким килем",
    "стоит на причале у реки, расправив короткие крылья, а рядом из воды выглядывает чёрная рубка подлодки",
    f'<path d="M-2 96 Q64 90 130 96 V130 H-2Z" fill="#2F6EA8" {W(3)}/>'
    f'<path d="M8 108 Q18 104 28 108 M86 116 Q96 112 106 116" fill="none" stroke="#9FD3F5" stroke-width="2.4"/>'
    f'<path d="M92 96 V78 Q92 72 100 72 H112 Q118 72 118 80 V96Z" fill="#2E2E36" {W(2.8)}/>'
    f'<path d="M104 72 V60 M100 62 H108" stroke="#2E2E36" stroke-width="3"/>'
    f'<path d="M10 74 Q14 60 30 58 H76 Q90 60 92 70 Q90 78 76 80 H22 Q10 80 10 74Z" fill="#9FB6CB" {W(3)}/>'
    f'<path d="M66 58 L74 26 L84 26 L82 60Z" fill="#9FB6CB" {W(2.8)}/>'
    f'<path d="M70 30 L90 22 L92 28 L74 34Z" fill="#7F98B0" {W(2.4)}/>'
    f'<path d="M30 74 L18 90 L50 88 L54 76Z" fill="#7F98B0" {W(2.6)}/>'
    f'<path d="M14 66 Q22 58 36 60 L34 70 Q22 70 14 66Z" fill="#CFE8F7" {W(2.2)}/>'
    + eye(22, 65, 0.45) + eye(30, 65, 0.45) +
    f'<path d="M42 70 H62" stroke="#E8434A" stroke-width="3"/>'
    f'<circle cx="78" cy="42" r="3" fill="#E8434A"/>'
    f'<path d="M4 82 H96" stroke="#7A5A3A" stroke-width="4"/>' + sparkle(108, 22, 5) + sparkle(24, 24, 4))

if __name__ == "__main__":
    for pid, v in I.items():
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
