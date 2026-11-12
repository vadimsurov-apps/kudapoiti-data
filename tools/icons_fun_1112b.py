"""Иконки робота fun (2026-11-12, проход b): места из tools/add_fun_1112b.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1112b.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Лапки Парк — розовая лапка-подушечка даёт «пять» детской ладошке
I["fun-lapki-park"] = ("#E9FFE0", "#6FBF5A",
    "мягкая розовая лапка-подушечка с четырьмя пальчиками и мордашкой",
    "даёт «пять» маленькой детской ладошке над зелёной травой контактного зоопарка",
    f'<path d="M0 104 Q32 96 64 104 T128 102 V128 H0Z" fill="#3E9A3A"/>'
    f'<ellipse cx="54" cy="74" rx="30" ry="26" fill="#FF9EC0" {W(3.4)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="11" fill="#FF9EC0" {W(3)}/>' for x, y in ((26, 40), (44, 30), (64, 30), (82, 40)))
    + face(54, 74, d=9, k=0.85) +
    f'<path d="M100 98 Q94 86 96 74 Q98 66 104 70 L104 52 Q104 46 108 46 Q112 46 112 52 L112 48 Q112 42 116 42 Q120 42 120 48 L120 54 Q120 48 124 50 Q127 52 126 58 L124 84 Q122 96 112 100Z" fill="#FFD9B8" {W(2.8)}/>'
    f'<path d="M112 52 V68 M120 54 V68" stroke="#3B3355" stroke-width="1.4"/>'
    + sparkle(92, 50, 5, "#FFE14D") + sparkle(108, 26, 3, "#fff") + sparkle(14, 80, 3, "#fff"))

# 2. Жучки-паучки — красная лягушка-помидор в террариуме ловит жучка
I["fun-zhuchki-pauchki"] = ("#D8F5E8", "#2F8A6A",
    "круглая красно-оранжевая лягушка-помидор",
    "сидит на большом листе в стеклянном террариуме и выстреливает языком в маленького жучка",
    f'<rect x="12" y="20" width="104" height="92" rx="6" fill="#BFF0E0" opacity=".55" {W(3)}/>'
    f'<path d="M12 30 H116" stroke="#3B3355" stroke-width="2.4"/>'
    f'<path d="M16 108 Q40 76 76 86 Q100 92 112 108Z" fill="#4CB050" {W(2.8)}/>'
    f'<path d="M30 104 Q56 88 96 100" fill="none" stroke="#2E7A34" stroke-width="2.2"/>'
    f'<ellipse cx="58" cy="78" rx="28" ry="22" fill="#FF5A2E" {W(3.4)}/>'
    f'<circle cx="44" cy="58" r="9" fill="#FF5A2E" {W(3)}/><circle cx="70" cy="58" r="9" fill="#FF5A2E" {W(3)}/>'
    + eye(44, 58, 0.9) + eye(70, 58, 0.9) +
    f'<path d="M50 84 Q58 90 66 84" fill="none" {W(2.6)}/>'
    f'<path d="M66 86 Q86 70 96 50" fill="none" stroke="#FF8FB0" stroke-width="3.4" stroke-linecap="round"/>'
    f'<ellipse cx="99" cy="46" rx="7" ry="5.5" fill="#2E2A4A" {W(2)}/><path d="M99 41 V51" stroke="#FFD23F" stroke-width="1.6"/>'
    f'<ellipse cx="38" cy="98" rx="9" ry="4" fill="#FF5A2E" {W(2.4)}/><ellipse cx="78" cy="98" rx="9" ry="4" fill="#FF5A2E" {W(2.4)}/>'
    + sparkle(104, 76, 3, "#fff"))

# 3. Театр «Бенефис» — софит-прожектор светит на сцену между бархатных кулис
I["fun-teatr-benefis"] = ("#3A1F4E", "#14081F",
    "чёрный театральный прожектор-софит с мордашкой на корпусе",
    "висит над сценой между вишнёвых кулис и светит жёлтым лучом в круг на полу",
    f'<path d="M0 0 H30 Q24 60 34 128 H0Z" fill="#B0203E" {W(2.6)}/>'
    f'<path d="M128 0 H98 Q104 60 94 128 H128Z" fill="#B0203E" {W(2.6)}/>'
    f'<path d="M48 44 L80 44 L104 112 L24 112Z" fill="#FFE680" opacity=".45"/>'
    f'<ellipse cx="64" cy="110" rx="40" ry="8" fill="#FFF2A8" opacity=".8"/>'
    f'<rect x="0" y="112" width="128" height="16" fill="#7A4A2A"/>'
    f'<path d="M64 6 V18" {W(3)}/>'
    f'<rect x="40" y="16" width="48" height="30" rx="8" fill="#2E2E3E" {W(3.4)}/>'
    f'<ellipse cx="64" cy="46" rx="18" ry="6" fill="#FFF6B0" {W(2.6)}/>'
    + face(64, 28, d=10, k=0.7).replace('fill="#3B3355"', 'fill="#fff"') +
    sparkle(26, 20, 3, "#FFE14D") + sparkle(104, 26, 3, "#FFE14D"))

# 5. Дом попугаев — зелёный волнистый попугайчик качается в круглой золотой клетке
I["fun-dom-popugaev-vavilova"] = ("#FFF1C8", "#E8A93A",
    "салатовый волнистый попугайчик с жёлтой головкой",
    "качается на кольце-качелях внутри круглой золотой клетки с куполом",
    f'<path d="M24 112 V56 Q24 18 64 16 Q104 18 104 56 V112" fill="#FFF8E0" fill-opacity=".5" {W(3)}/>'
    + "".join(f'<path d="M{x} 112 V{40 if 36<x<92 else 56}" stroke="#C9952A" stroke-width="2.2"/>' for x in (36, 50, 64, 78, 92))
    + f'<rect x="18" y="108" width="92" height="10" rx="3" fill="#D9A33A" {W(2.8)}/>'
    f'<circle cx="64" cy="12" r="5" fill="#D9A33A" {W(2.4)}/>'
    f'<path d="M64 20 V44" {W(2.2)}/><circle cx="64" cy="76" r="30" fill="none" stroke="#B84AE0" stroke-width="3.6"/>'
    f'<path d="M58 104 Q50 82 56 62 Q62 46 72 50 Q82 56 78 76 Q74 94 66 104Z" fill="#7EDB4A" {W(3)}/>'
    f'<path d="M58 62 Q62 44 72 48 Q80 52 78 62 Q70 66 58 62Z" fill="#FFE14D" {W(2.6)}/>'
    f'<path d="M64 104 L60 118 L68 118Z" fill="#3E9AD8" {W(2.2)}/>'
    + eye(70, 56, 0.75) + f'<path d="M76 58 Q82 60 78 64" fill="#FF9A3C" {W(2)}/>'
    + sparkle(100, 28, 3, "#fff"))

# 6. 101 Попугай — серый жако на перчатке говорит «101!»
I["fun-101-popugay"] = ("#FFE3E3", "#D8584A",
    "серый попугай жако с ярко-красным хвостом",
    "сидит на кожаной перчатке посетителя и громко произносит «101!» в облачке",
    f'<path d="M0 100 Q40 92 70 98 L70 128 H0Z" fill="#B97A45" {W(3)}/>'
    f'<path d="M30 104 Q20 70 34 48 Q48 30 64 36 Q80 44 74 70 Q70 92 56 104Z" fill="#A8AEB8" {W(3.4)}/>'
    f'<path d="M36 102 L28 124 L48 118Z" fill="#E8332A" {W(2.6)}/>'
    f'<path d="M48 54 Q40 54 38 46" fill="none" stroke="#7E8590" stroke-width="2"/>'
    + eye(56, 48, 0.8) +
    f'<path d="M66 48 Q78 50 72 62 Q66 58 66 48Z" fill="#2E2E3E" {W(2)}/>'
    f'<path d="M78 14 H120 Q124 14 124 20 V42 Q124 48 118 48 H92 L82 58 L84 48 H78 Q72 48 72 42 V20 Q72 14 78 14Z" fill="#fff" {W(2.8)}/>'
    f'<text x="98" y="39" font-family="Arial" font-weight="bold" font-size="18" text-anchor="middle" fill="#E8332A">101</text>'
    + sparkle(110, 70, 4, "#fff"))

# 12. ХатаСуриката — трое сурикатов спят обнявшись в кресле под пледом
I["fun-hata-surikata"] = ("#FCE9D6", "#C47A4A",
    "трое пушистых сурикатов-малышей",
    "уютно сидят рядышком в большом зелёном кресле под клетчатым пледом в домашней «хате»",
    f'<rect x="10" y="40" width="108" height="70" rx="20" fill="#3E9A6A" {W(3.4)}/>'
    f'<rect x="4" y="62" width="20" height="50" rx="8" fill="#4CB07A" {W(3)}/><rect x="104" y="62" width="20" height="50" rx="8" fill="#4CB07A" {W(3)}/>'
    + "".join(f'<path d="M{x-11} 92 Q{x-12} 64 {x-6} 54 Q{x} 46 {x+6} 54 Q{x+12} 64 {x+11} 92Z" fill="#D9A866" {W(2.8)}/>'
              f'<ellipse cx="{x-4}" cy="62" rx="3" ry="3.6" fill="#4A3020"/><ellipse cx="{x+4}" cy="62" rx="3" ry="3.6" fill="#4A3020"/>'
              f'<circle cx="{x-3.4}" cy="61.4" r="1" fill="#fff"/><circle cx="{x+4.6}" cy="61.4" r="1" fill="#fff"/>'
              f'<ellipse cx="{x}" cy="68" rx="2" ry="1.4" fill="#3B3355"/>' for x in (40, 64, 88))
    + f'<path d="M18 84 H110 L104 116 H24Z" fill="#E8453A" {W(3)}/>'
    + "".join(f'<path d="M{x} 84 L{x-2} 116" stroke="#FFD9A0" stroke-width="3"/>' for x in (36, 56, 76, 96))
    + f'<path d="M20 98 H108" stroke="#FFD9A0" stroke-width="3"/>'
    + sparkle(64, 22, 4, "#fff"))

# 15. Зайкафе — белый кролик с морковкой сидит в чашке чая
I["fun-zaykafe"] = ("#E6F7FF", "#7AB8E8",
    "белый вислоухий кролик с розовым носиком",
    "сидит в большой голубой чайной чашке антикафе и хрумкает оранжевую морковку",
    f'<ellipse cx="64" cy="112" rx="50" ry="8" fill="#fff" {W(2.6)}/>'
    f'<path d="M30 80 Q30 112 64 112 Q98 112 98 80Z" fill="#5AB8F0" {W(3.4)}/>'
    f'<path d="M98 84 Q116 84 112 96 Q108 104 96 102" fill="none" {W(3.2)}/>'
    f'<ellipse cx="64" cy="66" rx="24" ry="20" fill="#FFFFFF" {W(3.2)}/>'
    f'<path d="M44 58 Q26 60 24 82 Q36 80 46 66Z" fill="#FFFFFF" {W(2.8)}/><path d="M84 58 Q102 60 104 82 Q92 80 82 66Z" fill="#FFFFFF" {W(2.8)}/>'
    + eye(56, 62, 0.75) + eye(72, 62, 0.75) +
    f'<ellipse cx="64" cy="70" rx="3" ry="2.2" fill="#FF7FA8"/>'
    f'<path d="M30 80 H98" {W(3)}/>'
    f'<path d="M74 78 L96 52" stroke="#FF8A2A" stroke-width="7" stroke-linecap="round"/><path d="M74 78 L96 52" fill="none" {W(1.4)}/>'
    f'<path d="M96 52 l2 -10 M96 52 l8 -6 M96 52 l9 1" stroke="#4CB050" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(22, 30, 4, "#fff") + sparkle(106, 22, 3, "#fff"))

# 16. Минипиг (Байкальская) — пятнистый минипиг в шапке-ушанке
I["fun-minipig-baykalskaya"] = ("#E8FFF4", "#6ACBA0",
    "чёрно-розовый пятнистый минипиг в синей шапке-ушанке",
    "стоит на мягком коврике и тянется пятачком к печенью на блюдце",
    f'<rect x="8" y="100" width="112" height="20" rx="10" fill="#FFCE6A" {W(2.6)}/>'
    f'<ellipse cx="60" cy="76" rx="36" ry="24" fill="#FFC6D8" {W(3.4)}/>'
    f'<ellipse cx="44" cy="80" rx="10" ry="8" fill="#3B3355" opacity=".85"/><ellipse cx="74" cy="66" rx="8" ry="6" fill="#3B3355" opacity=".85"/>'
    + "".join(f'<rect x="{x}" y="94" width="8" height="12" rx="3" fill="#FFC6D8" {W(2.4)}/>' for x in (34, 48, 70, 82))
    + f'<circle cx="92" cy="66" r="18" fill="#FFC6D8" {W(3.2)}/>'
    f'<path d="M76 58 Q78 40 92 40 Q106 40 108 58Z" fill="#2F5FD0" {W(2.8)}/><path d="M74 58 L72 72 L80 70Z" fill="#2F5FD0" {W(2.4)}/>'
    f'<circle cx="92" cy="38" r="4" fill="#fff" {W(2)}/>'
    + eye(88, 66, 0.65) + eye(100, 66, 0.65) +
    f'<ellipse cx="108" cy="76" rx="7" ry="6" fill="#FF8AB0" {W(2.4)}/>'
    f'<ellipse cx="114" cy="98" rx="12" ry="3" fill="#fff" {W(2)}/><circle cx="114" cy="94" r="4.5" fill="#D99A4A" {W(1.6)}/>'
    f'<path d="M24 70 q-8 -6 -4 -12" fill="none" {W(2.4)}/>'
    + sparkle(24, 28, 4, "#fff"))

# 17. Котя Мотя — рыжий и серый котята играют клубком на подоконнике
I["fun-kotya-motya"] = ("#E8E0FF", "#8A70D8",
    "два котёнка — рыжий и серо-полосатый",
    "катают по подоконнику большой розовый клубок, а за окном светит луна над новостройками",
    f'<rect x="10" y="14" width="108" height="72" rx="6" fill="#2E2A6A" {W(3)}/><path d="M64 14 V86" stroke="#3B3355" stroke-width="3"/>'
    f'<circle cx="94" cy="34" r="8" fill="#FFF2A8"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="12" height="{86-y}" fill="#4A4590"/>' for x, y in ((16, 54), (32, 46), (70, 58), (102, 50)))
    + f'<rect x="0" y="86" width="128" height="10" fill="#FFF" {W(2.6)}/>'
    f'<rect x="0" y="96" width="128" height="32" fill="#C8B8F0"/>'
    f'<path d="M14 92 Q12 64 30 62 Q48 64 46 92Z" fill="#FF9A3C" {W(3)}/><path d="M18 66 L20 52 L28 62 M42 66 L40 52 L32 62" fill="#FF9A3C" {W(2.4)}/>'
    + eye(25, 74, 0.55) + eye(36, 74, 0.55) +
    f'<path d="M84 92 Q82 64 100 62 Q118 64 116 92Z" fill="#9AA0B0" {W(3)}/><path d="M88 66 L90 52 L98 62 M112 66 L110 52 L102 62" fill="#9AA0B0" {W(2.4)}/>'
    f'<path d="M90 80 h6 M104 80 h6" stroke="#5A6070" stroke-width="2"/>'
    + eye(95, 74, 0.55) + eye(106, 74, 0.55) +
    f'<circle cx="64" cy="82" r="11" fill="#FF7FB8" {W(2.8)}/><path d="M56 78 Q64 86 72 76 M56 86 Q64 78 72 88" fill="none" stroke="#C04A80" stroke-width="1.6"/>'
    f'<path d="M64 93 Q60 104 70 110" fill="none" stroke="#FF7FB8" stroke-width="2.4"/>')

# 19. Дом сказок «Жили-были» — русская печка открыла заслонку с пирожками
I["fun-dom-skazok-izmaylovo"] = ("#FFE6D0", "#E0703A",
    "белёная русская печка с мордашкой и расписным узором",
    "открыла заслонку, а из горячего устья выкатываются румяные пирожки и сказочные звёздочки",
    f'<rect x="0" y="108" width="128" height="20" fill="#9A5A2E"/>'
    f'<rect x="24" y="44" width="80" height="66" rx="6" fill="#FFF8F0" {W(3.4)}/>'
    f'<rect x="56" y="14" width="18" height="32" fill="#FFF8F0" {W(3)}/>'
    f'<path d="M44 108 V84 Q64 66 84 84 V108Z" fill="#3A1A10" {W(3)}/>'
    f'<path d="M50 104 Q64 88 78 104Z" fill="#FF8A2A"/>'
    + face(64, 58, d=10, k=0.7) +
    f'<path d="M30 74 q6 -6 12 0 q-6 6 -12 0Z M86 74 q6 -6 12 0 q-6 6 -12 0Z" fill="#3A7BE0"/>'
    f'<rect x="88" y="84" width="22" height="16" rx="3" fill="#6A6A7A" {W(2.4)}/>'
    f'<ellipse cx="22" cy="114" rx="11" ry="6" fill="#E8A040" {W(2.4)}/><ellipse cx="40" cy="120" rx="10" ry="5.5" fill="#E8A040" {W(2.4)}/>'
    + sparkle(96, 30, 5, "#FFE14D") + sparkle(28, 26, 4, "#FFE14D") + sparkle(110, 54, 3, "#fff"))

# 20. Пушистая братва — енот полощет в тазике плюшевую игрушку
I["fun-pushistaya-bratva"] = ("#DDF2FF", "#4F8FB8",
    "полосатохвостый енот в повязке-бандане",
    "старательно полощет в голубом тазике плюшевого мишку, разбрызгивая капли",
    f'<path d="M14 92 H114 L104 118 H24Z" fill="#7AD0FF" {W(3.2)}/><ellipse cx="64" cy="92" rx="50" ry="8" fill="#BFF0FF" {W(2.8)}/>'
    f'<path d="M40 90 Q34 56 46 40 Q56 28 64 28 Q72 28 82 40 Q94 56 88 90Z" fill="#9AA0AA" {W(3.4)}/>'
    f'<path d="M44 48 Q64 40 84 48 Q84 60 64 60 Q44 60 44 48Z" fill="#3B3355"/>'
    f'<circle cx="55" cy="52" r="4" fill="#fff"/><circle cx="73" cy="52" r="4" fill="#fff"/><circle cx="55" cy="52" r="2" fill="#3B3355"/><circle cx="73" cy="52" r="2" fill="#3B3355"/>'
    f'<ellipse cx="64" cy="66" rx="10" ry="7" fill="#F0F0F4" {W(2)}/><ellipse cx="64" cy="64" rx="3" ry="2" fill="#3B3355"/>'
    f'<path d="M44 34 L38 22 L52 30 M84 34 L90 22 L76 30" fill="#9AA0AA" {W(2.4)}/>'
    f'<path d="M46 38 Q64 26 82 38 L80 44 Q64 34 48 44Z" fill="#E8453A" {W(2.2)}/>'
    f'<circle cx="64" cy="88" r="9" fill="#C8884A" {W(2.4)}/><circle cx="57" cy="81" r="3.5" fill="#C8884A" {W(1.8)}/><circle cx="71" cy="81" r="3.5" fill="#C8884A" {W(1.8)}/>'
    f'<path d="M100 94 Q114 80 112 60 Q122 76 118 96" fill="#9AA0AA" {W(2.6)}/><path d="M104 88 L116 84 M110 74 L118 72" stroke="#3B3355" stroke-width="3"/>'
    + "".join(f'<path d="M{x} {y} q3 -6 6 0 q-3 4 -6 0Z" fill="#3CA8FF"/>' for x, y in ((18, 80), (30, 70), (98, 70), (22, 60))))

# 22. Дом попугаев (РИО) — красный ара приземлился на голову ребёнку, раскинув крылья
I["fun-dom-popugaev-rio"] = ("#D8F4FF", "#3FA0D8",
    "ярко-красный ара с сине-жёлтыми крыльями и длинным хвостом",
    "приземлился на макушку смеющегося ребёнка и раскинул крылья, как корону",
    f'<path d="M30 128 Q30 104 64 100 Q98 104 98 128Z" fill="#7EDB4A" {W(3)}/>'
    f'<circle cx="64" cy="82" r="22" fill="#FFD9B8" {W(3.2)}/>'
    f'<path d="M42 78 Q44 58 64 58 Q84 58 86 78 Q76 68 64 68 Q52 68 42 78Z" fill="#7A4A26" {W(2.4)}/>'
    + eye(56, 84, 0.7) + eye(72, 84, 0.7) +
    f'<path d="M57 92 Q64 99 71 92Z" fill="#E8453A" {W(2)}/>'
    f'<path d="M58 56 Q36 40 10 46 Q22 54 26 60 Q40 58 58 60Z" fill="#2F7BE0" {W(2.8)}/>'
    f'<path d="M14 48 Q30 50 40 56" fill="none" stroke="#FFE14D" stroke-width="3"/>'
    f'<path d="M70 56 Q92 40 118 46 Q106 54 102 60 Q88 58 70 60Z" fill="#2F7BE0" {W(2.8)}/>'
    f'<path d="M114 48 Q98 50 88 56" fill="none" stroke="#FFE14D" stroke-width="3"/>'
    f'<path d="M54 60 Q52 34 64 26 Q76 34 74 60Z" fill="#E8332A" {W(3.2)}/>'
    f'<path d="M58 30 Q50 18 56 10 Q60 20 64 26Z" fill="#E8332A" {W(2.4)}/>'
    f'<circle cx="64" cy="20" r="9" fill="#E8332A" {W(2.8)}/><circle cx="66" cy="19" r="4" fill="#fff"/><circle cx="67" cy="19" r="2" fill="#3B3355"/>'
    f'<path d="M72 18 Q82 20 76 30 Q72 26 70 24Z" fill="#F2E6C8" {W(2)}/>'
    + sparkle(22, 90, 4, "#fff") + sparkle(108, 86, 3, "#FFE14D"))

# 23. Жучки-паучки: ночной мир — скорпион светится бирюзой под ультрафиолетовым фонариком
I["fun-zhuchki-nochnoy-mir"] = ("#2A1A4A", "#0A0618",
    "скорпион, светящийся бирюзой в ультрафиолете",
    "сидит на камне в тёмном террариуме, а сверху его освещает фиолетовый луч маленького фонарика",
    f'<path d="M86 0 L118 0 L94 60 L58 60Z" fill="#9B5CFF" opacity=".35"/>'
    f'<rect x="92" y="2" width="22" height="14" rx="4" fill="#5A5A6A" {W(2.6)}/><circle cx="103" cy="16" r="5" fill="#C89BFF"/>'
    f'<path d="M0 108 Q30 92 64 100 T128 104 V128 H0Z" fill="#3A2A5A"/>'
    f'<ellipse cx="62" cy="98" rx="40" ry="12" fill="#6A5A7A" {W(2.8)}/>'
    f'<ellipse cx="62" cy="80" rx="20" ry="13" fill="#3CFFE0" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} q{dx} 4 {dx*1.6:.0f} 12" fill="none" stroke="#3CFFE0" stroke-width="3" stroke-linecap="round"/>'
              for x, y, dx in ((48, 86, -8), (54, 90, -6), (70, 90, 6), (76, 86, 8)))
    + f'<path d="M78 76 Q96 70 98 52 Q100 36 88 34" fill="none" stroke="#3CFFE0" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M78 76 Q96 70 98 52 Q100 36 88 34" fill="none" stroke="#3B3355" stroke-width="1.6" stroke-dasharray="4 4"/>'
    f'<path d="M88 34 L80 30 L86 40Z" fill="#3CFFE0" {W(2)}/>'
    f'<path d="M44 76 Q30 70 28 60 M44 82 Q28 84 22 76" fill="none" stroke="#3CFFE0" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M24 56 l4 4 l4 -6 M18 72 l4 4 l4 -6" fill="none" stroke="#3CFFE0" stroke-width="3"/>'
    + face(58, 80, d=6, k=0.6)
    + sparkle(20, 24, 3, "#C89BFF") + sparkle(40, 40, 2.5, "#fff"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
