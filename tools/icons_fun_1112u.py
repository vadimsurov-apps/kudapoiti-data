"""Иконки робота fun (2026-11-12, проход u): места из tools/add_fun_1112u.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1112u.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. МЕГА Тёплый Стан — тканевая корзинка-органайзер, обнимает сложенное полотенце и тюбик
I["chg-mega-teply-stan"] = ("#FFF1D6", "#E9A23B",
    "бирюзовая тканевая корзинка-органайзер с двумя петлями-ручками и мордашкой на боку",
    "крепко обнимает ручками свёрнутое в рулончик жёлтое полотенце и тюбик, из которых собирает всё для смены одежды малыша",
    # содержимое (за корзинкой)
    f'<rect x="34" y="30" width="26" height="40" rx="12" fill="#FFE07A" {W(3)}/>'
    f'<path d="M38 40 H56 M38 50 H56" stroke="#E9B93B" stroke-width="2.4"/>'
    f'<path d="M70 26 L84 26 L88 70 L66 70Z" fill="#FFFFFF" {W(3)}/>'
    f'<rect x="72" y="18" width="10" height="9" rx="2" fill="#FF8FB1" {W(2.6)}/>'
    # корзинка
    f'<path d="M16 62 H112 L104 112 Q102 118 96 118 H32 Q26 118 24 112Z" fill="#4FC9C0" {W(3.2)}/>'
    f'<path d="M20 74 H108" stroke="#2FA49B" stroke-width="2.6"/>'
    + "".join(f'<path d="M{x} 78 L{x+4} 114" stroke="#2FA49B" stroke-width="2" opacity=".7"/>' for x in (34, 50, 66, 82, 96))
    # ручки-петли как руки
    + f'<path d="M18 64 Q8 44 30 46" fill="none" {W(6)}/><path d="M18 64 Q8 44 30 46" fill="none" stroke="#4FC9C0" stroke-width="3"/>'
    f'<path d="M110 64 Q120 44 98 44" fill="none" {W(6)}/><path d="M110 64 Q120 44 98 44" fill="none" stroke="#4FC9C0" stroke-width="3"/>'
    + face(64, 92, d=12, k=0.8)
    + sparkle(104, 22, 5, "#fff") + sparkle(22, 26, 3.5, "#fff"))

# 3. «Гудзон» — ковшик для мытья головы льёт тёплую струйку-речку
I["chg-gudzon"] = ("#E2F1FF", "#3E7FD1",
    "жёлтый детский ковшик для мытья головы с мягким голубым бортиком-полумесяцем и мордашкой",
    "наклонился и льёт тёплую струйку, которая внизу разливается маленькой речкой с пузырьками",
    # речка внизу
    f'<path d="M0 104 Q22 96 44 104 T88 104 T132 104 V128 H0Z" fill="#7CC4FF" {W(2.6)}/>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(1.6)}/>' for x, y, r in ((30, 112, 3), (86, 116, 4), (100, 110, 2.5))) +
    # струйка
    f'<path d="M44 66 Q40 84 46 104" fill="none" stroke="#7CC4FF" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M44 66 Q40 84 46 104" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".7"/>'
    # ковшик (наклонён)
    f'<g transform="rotate(-24 70 48)">'
    f'<path d="M40 30 H96 L92 74 Q90 82 82 82 H54 Q46 82 44 74Z" fill="#FFD84D" {W(3.2)}/>'
    f'<path d="M38 30 Q68 18 98 30" fill="none" stroke="#5FB4FF" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M38 30 Q68 18 98 30" fill="none" {W(2.4)}/>'
    f'<path d="M96 40 Q114 42 112 58 Q110 68 94 64" fill="none" {W(7)}/>'
    f'<path d="M96 40 Q114 42 112 58 Q110 68 94 64" fill="none" stroke="#FFD84D" stroke-width="3.4"/>'
    + face(68, 56, d=10, k=0.7) + '</g>'
    + sparkle(110, 16, 4, "#fff"))

# 4. «Красный кит» — красный детский спальник на молнии сладко зевает
I["chg-krasny-kit-mytishchi"] = ("#FFE1DC", "#C9433C",
    "красный детский спальный мешок на молнии с капюшоном и мордашкой",
    "стоит столбиком и сладко зевает, прикрыв глазки, а над ним плывут три буквы «з» разного размера",
    f'<path d="M36 44 Q36 18 64 18 Q92 18 92 44 V104 Q92 118 78 118 H50 Q36 118 36 104Z" fill="#F0453C" {W(3.2)}/>'
    f'<path d="M44 46 Q44 28 64 28 Q84 28 84 46 V60 H44Z" fill="#FFD9C2" {W(2.8)}/>'
    # молния
    f'<path d="M64 62 V112" stroke="#B8302A" stroke-width="3"/>'
    + ''.join(f'<path d="M61 {y} H67" stroke="#FFE38A" stroke-width="2"/>' for y in range(66, 110, 6)) +
    f'<rect x="60" y="62" width="8" height="10" rx="2" fill="#FFE38A" {W(2)}/>'
    # сонное лицо
    f'<path d="M52 42 q4 3 8 0 M68 42 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="52" rx="4" ry="5" fill="#8A2E3B" {W(2)}/>'
    f'<ellipse cx="50" cy="48" rx="3.5" ry="2.2" fill="#FF7FA8" opacity=".7"/><ellipse cx="78" cy="48" rx="3.5" ry="2.2" fill="#FF7FA8" opacity=".7"/>'
    # з-з-з
    f'<text x="94" y="52" font-family="Arial" font-weight="bold" font-size="12" fill="#fff" stroke="{O}" stroke-width="1.2">з</text>'
    f'<text x="99" y="40" font-family="Arial" font-weight="bold" font-size="15" fill="#fff" stroke="{O}" stroke-width="1.2">з</text>'
    f'<text x="104" y="26" font-family="Arial" font-weight="bold" font-size="18" fill="#fff" stroke="{O}" stroke-width="1.2">з</text>')

# 5. ЕвроПарк — мягкое кресло для кормления ждёт маму
I["chg-europark"] = ("#F1E6FF", "#8C63D6",
    "сиреневое мягкое мамино кресло для кормления с высокими пухлыми подлокотниками",
    "радушно расставило подлокотники, как руки для объятий, а на сиденье лежит маленькая подушка-сердечко",
    # ножки
    f'<path d="M34 104 L30 118 M94 104 L98 118" {W(4)}/>'
    # спинка
    f'<path d="M30 60 Q28 24 64 24 Q100 24 98 60Z" fill="#B48CF0" {W(3.2)}/>'
    + face(64, 44, d=11, k=0.75) +
    # сиденье
    f'<rect x="30" y="72" width="68" height="32" rx="10" fill="#C9A9F7" {W(3.2)}/>'
    # подлокотники-руки (подняты)
    f'<path d="M30 96 Q10 96 12 74 Q14 58 26 54 Q36 54 36 66 L36 96Z" fill="#9F78E6" {W(3.2)}/>'
    f'<path d="M98 96 Q118 96 116 74 Q114 58 102 54 Q92 54 92 66 L92 96Z" fill="#9F78E6" {W(3.2)}/>'
    # подушка-сердечко
    f'<path d="M64 92 Q50 82 52 74 Q54 68 60 70 Q63 71 64 74 Q65 71 68 70 Q74 68 76 74 Q78 82 64 92Z" fill="#FF8FB1" {W(2.6)}/>'
    + sparkle(110, 26, 4, "#fff") + sparkle(18, 30, 3, "#fff"))

# 6. «Райкин Плаза» — низенькая детская раковина-умывальник, из крана бежит струйка
I["chg-raikin-plaza"] = ("#FFF5E0", "#E2873A",
    "низенькая белая детская раковина-умывальник на круглой ножке с мордашкой на чаше",
    "из изогнутого крана-хоботка бежит струйка, а на струйке, как на горке, катится мыльный пузырёк",
    # ножка
    f'<path d="M54 84 L50 120 H78 L74 84Z" fill="#F4F4F8" {W(3)}/>'
    # чаша
    f'<path d="M16 60 H112 Q110 92 64 92 Q18 92 16 60Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<path d="M22 60 H106" stroke="#C9E7FF" stroke-width="5"/>'
    + face(64, 76, d=12, k=0.72) +
    # кран
    f'<path d="M84 60 V40 Q84 26 70 26 Q58 26 56 36" fill="none" {W(9)}/>'
    f'<path d="M84 60 V40 Q84 26 70 26 Q58 26 56 36" fill="none" stroke="#C9CFDB" stroke-width="5.6"/>'
    f'<rect x="78" y="18" width="14" height="6" rx="3" fill="#FF7A59" {W(2.4)}/>'
    # струйка
    f'<path d="M56 40 Q52 50 56 60" fill="none" stroke="#6EC6FF" stroke-width="6" stroke-linecap="round"/>'
    # пузырёк
    f'<circle cx="46" cy="46" r="7" fill="#E6F6FF" {W(2)}/><path d="M43 43 q2 -2 4 -1" fill="none" stroke="#fff" stroke-width="2"/>'
    + sparkle(110, 30, 4, "#fff"))

# 7. «Филион» — деревянные плечики в форме мишкиной головы с запасной кофточкой
I["chg-filion"] = ("#E6FBF7", "#2FA59A",
    "деревянные детские плечики-вешалка с крючком и головой медвежонка посередине",
    "держат на плечиках крошечную запасную кофточку в оранжевую полоску и покачиваются на крючке",
    # крючок
    f'<path d="M64 30 V22 Q64 12 72 12 Q80 12 80 20" fill="none" {W(4)}/>'
    f'<path d="M64 30 V22 Q64 12 72 12 Q80 12 80 20" fill="none" stroke="#C9CFDB" stroke-width="1.8"/>'
    # кофточка
    f'<path d="M34 54 L18 68 L26 82 L36 76 V114 H92 V76 L102 82 L110 68 L94 54 Q78 62 64 62 Q50 62 34 54Z" fill="#FFB25E" {W(3.2)}/>'
    + ''.join(f'<path d="M36 {y} H92" stroke="#FFF2DE" stroke-width="5"/>' for y in (78, 92, 106)) +
    f'<path d="M34 54 L18 68 L26 82 L36 76 V114 H92 V76 L102 82 L110 68 L94 54 Q78 62 64 62 Q50 62 34 54Z" fill="none" {W(3.2)}/>'
    # плечики
    f'<path d="M14 58 Q40 40 64 40 Q88 40 114 58" fill="none" {W(9)}/>'
    f'<path d="M14 58 Q40 40 64 40 Q88 40 114 58" fill="none" stroke="#D99A5B" stroke-width="5.6"/>'
    # мишкина голова
    f'<circle cx="50" cy="28" r="7" fill="#D99A5B" {W(2.6)}/><circle cx="78" cy="28" r="7" fill="#D99A5B" {W(2.6)}/>'
    f'<circle cx="64" cy="40" r="16" fill="#E8B07A" {W(3)}/>'
    f'<ellipse cx="64" cy="46" rx="7" ry="5" fill="#FFE2C4" {W(2)}/>'
    + eye(57, 37, 0.6) + eye(71, 37, 0.6) +
    f'<circle cx="64" cy="44" r="2" fill="{O}"/>'
    + sparkle(110, 22, 4, "#fff"))

# 8. «Кунцево Плаза» — папа с малышкой на руках у таблички «мама и малыш»
I["chg-kuntsevo-plaza"] = ("#E9EEFF", "#5568C9",
    "бородатый папа в зелёной клетчатой рубашке с годовалой дочкой на руках",
    "стоит у двери с табличкой, где нарисованы мама, папа и малыш, и дочка радостно тычет в неё пальчиком",
    # дверь с табличкой
    f'<rect x="72" y="14" width="46" height="110" rx="4" fill="#DCE3FF" {W(3)}/>'
    f'<rect x="78" y="26" width="34" height="26" rx="4" fill="#FFFFFF" {W(2.4)}/>'
    f'<circle cx="86" cy="34" r="3" fill="#E85C8A"/><path d="M83 46 L86 38 L89 46Z" fill="#E85C8A"/>'
    f'<circle cx="95" cy="34" r="3" fill="#3E6FD9"/><rect x="92.5" y="38" width="5" height="8" fill="#3E6FD9"/>'
    f'<circle cx="104" cy="38" r="2.4" fill="#FFB020"/><rect x="102" y="41" width="4" height="5" fill="#FFB020"/>'
    # папа
    f'<path d="M8 128 Q8 88 34 84 Q60 88 62 128Z" fill="#5BBF7A" {W(3)}/>'
    f'<path d="M22 92 V128 M46 92 V128 M8 108 H62" stroke="#3A9A5B" stroke-width="2.4"/>'
    f'<circle cx="34" cy="62" r="17" fill="#F6C9A6" {W(3)}/>'
    f'<path d="M18 62 Q18 82 34 84 Q50 82 50 62 Q44 72 34 72 Q24 72 18 62Z" fill="#8A5A3B" {W(2.6)}/>'
    f'<path d="M18 56 Q20 42 34 42 Q48 42 50 56 Q42 50 34 50 Q26 50 18 56Z" fill="#8A5A3B" {W(2.6)}/>'
    + eye(28, 60, 0.55) + eye(40, 60, 0.55) +
    # дочка на руке
    f'<path d="M44 108 Q44 92 56 90 Q68 92 68 108Z" fill="#FF9EC4" {W(2.8)}/>'
    f'<circle cx="56" cy="80" r="11" fill="#FFE0C7" {W(2.8)}/>'
    f'<path d="M49 72 Q56 64 63 72" fill="none" stroke="#C8894E" stroke-width="3" stroke-linecap="round"/>'
    + face(56, 80, d=4.5, k=0.42) +
    f'<path d="M64 94 L78 70" {W(6)}/><path d="M64 94 L78 70" stroke="#FFE0C7" stroke-width="3.2" stroke-linecap="round"/>')

# 10. ИгроБаза VR — мальчик-серфер на неоновой волне-сетке VR-арены
I["fun-igrobaza-vr-rio"] = ("#FFE9F6", "#E0429A",
    "мальчик в белом VR-шлеме с жёлтым визором и раскинутыми руками",
    "серфит на гребне неоновой волны из голубой сетки-пола, которая вздыбилась посреди граффити-арены",
    # граффити-капли фона
    f'<path d="M6 30 Q20 14 34 26 Q44 36 30 44 Q16 48 6 30Z" fill="#FFD23F" opacity=".75"/>'
    f'<path d="M98 92 Q116 84 124 100 Q122 116 104 112Z" fill="#7CE36B" opacity=".7"/>'
    # волна-сетка
    f'<path d="M-4 118 Q20 118 34 96 Q50 66 78 70 Q100 74 98 92 Q92 84 82 88 Q70 94 72 118 H-4Z" fill="#2B2F7E" {W(3)}/>'
    + ''.join(f'<path d="M{x} 118 Q{x+8} 98 {x+22} {84 - (x // 8)}" fill="none" stroke="#5CF2FF" stroke-width="1.8"/>' for x in (6, 22, 38, 54))
    + ''.join(f'<path d="M0 {y} Q40 {y-18} 96 {y-10}" fill="none" stroke="#5CF2FF" stroke-width="1.8"/>' for y in (104, 114)) +
    # доска
    f'<path d="M36 82 Q62 70 90 76 Q76 86 40 88Z" fill="#FF7A3D" {W(2.8)}/>'
    # мальчик
    f'<path d="M54 80 L58 60 M70 78 L66 60" {W(5)}/>'
    f'<path d="M50 62 Q50 42 62 40 Q74 42 74 62Z" fill="#3E7BFA" {W(3)}/>'
    f'<path d="M50 48 L32 38 M74 48 L94 36" {W(5)}/>'
    f'<path d="M50 48 L32 38 M74 48 L94 36" stroke="#FFD9B8" stroke-width="2.4" stroke-linecap="round"/>'
    f'<circle cx="62" cy="28" r="12" fill="#FFD9B8" {W(3)}/>'
    f'<rect x="50" y="20" width="26" height="12" rx="5" fill="#F4F6FF" {W(2.6)}/>'
    f'<rect x="53" y="23" width="20" height="6" rx="3" fill="#FFD23F"/>'
    f'<path d="M57 35 Q62 39 67 35" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    + sparkle(104, 20, 5, "#fff") + sparkle(20, 66, 3, "#fff"))

# 11. «Забей ковёр» — тафтинг-пистолет настреливает пушистую радугу на раме
I["fun-zabey-kover-chertanovskaya"] = ("#FFF6CC", "#F2B91E",
    "серо-голубая тафтинговая машинка-пистолет с мордашкой и мотком пряжи за спиной",
    "«простреливает» пушистыми нитками радугу-коврик на белой ткани, натянутой на деревянную раму",
    # рама с тканью
    f'<rect x="10" y="14" width="78" height="100" rx="4" fill="#C98B4E" {W(3)}/>'
    f'<rect x="18" y="22" width="62" height="84" rx="2" fill="#FFFDF5" {W(2.4)}/>'
    # пушистая радуга
    + ''.join(f'<path d="M{24+i*5} 92 Q{24+i*5} {44+i*5} {49} {44+i*5} Q{74-i*5} {44+i*5} {74-i*5} 92" fill="none" stroke="{c}" stroke-width="5.4" stroke-dasharray="0.1 5.2" stroke-linecap="round"/>'
              for i, c in enumerate(("#FF5A5F", "#FFA53A", "#FFD93D", "#58C46B", "#4FA8FF"))) +
    # пряжа
    f'<circle cx="108" cy="102" r="12" fill="#FF7AB8" {W(2.8)}/>'
    f'<path d="M98 96 Q108 104 118 96 M98 106 Q108 112 118 106" fill="none" stroke="#E0549A" stroke-width="2"/>'
    f'<path d="M100 92 Q96 70 88 62" fill="none" stroke="#FF7AB8" stroke-width="2.4"/>'
    # пистолет
    f'<g transform="rotate(-18 92 56)">'
    f'<rect x="72" y="40" width="44" height="26" rx="10" fill="#8FA9C8" {W(3)}/>'
    f'<path d="M72 50 L60 50 L56 54 L60 58 L72 58" fill="#C9CFDB" {W(2.6)}/>'
    f'<path d="M96 66 L100 90 Q101 96 95 96 L90 96 Q86 96 86 90 L84 66" fill="#5E7799" {W(3)}/>'
    + face(96, 52, d=7, k=0.55) + '</g>'
    + sparkle(116, 20, 4, "#fff"))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
