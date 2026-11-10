"""Иконки робота fun (2026-11-10, ночной проход j): места из tools/add_fun_1110j.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1110j.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# --- детские библиотеки ---
I["lib1-andersen-kids"] = ("#FFF4E0", "#E0883A",
    "пара блестящих чёрных калош с мордашками — калоши счастья из сказки Андерсена",
    "шлёпают по огромной раскрытой книге сказок, разбрызгивая капли из лужицы на странице",
    f'<path d="M4 96 Q34 80 64 92 Q94 80 124 96 L124 130 H4Z" fill="#B0412E" {W(3)}/>'
    f'<path d="M10 92 Q36 74 64 88 L64 118 Q36 104 10 116Z" fill="#FFFDF5" {W(2.6)}/>'
    f'<path d="M118 92 Q92 74 64 88 L64 118 Q92 104 118 116Z" fill="#FFFDF5" {W(2.6)}/>'
    f'<ellipse cx="88" cy="96" rx="20" ry="5" fill="#8FD0F2" {W(2)}/>'
    f'<path d="M16 76 Q16 56 34 54 Q50 54 52 66 L58 72 Q60 80 50 80 H20 Q16 80 16 76Z" fill="#2B2B3A" {W(3)}/>'
    f'<path d="M22 60 Q30 56 40 58" stroke="#fff" stroke-width="2.4" fill="none" opacity=".7"/>'
    + face(36, 68, d=6, k=0.55) +
    f'<path d="M70 70 Q70 48 90 46 Q106 46 108 58 L114 64 Q116 72 106 72 H74 Q70 72 70 70Z" fill="#2B2B3A" {W(3)}/>'
    f'<path d="M76 52 Q84 48 94 50" stroke="#fff" stroke-width="2.4" fill="none" opacity=".7"/>'
    + face(92, 60, d=6, k=0.55) +
    "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#8FD0F2" {W(1.4)}/>' for x, y in ((70, 84), (106, 80), (112, 88), (64, 78)))
    + stars(((22, 30), (64, 24), (104, 30)), 4, "#FFD84A"))

I["lib-griboedov-kids"] = ("#EAF4FF", "#5476B8",
    "старинная дорожная карета на высоких колёсах с мордашкой на дверце",
    "мчится по снежной дороге в метель, из-под колёс летят снежные брызги",
    f'<path d="M-2 98 Q40 90 64 96 Q96 102 130 94 V130 H-2Z" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff"/>' for x, y in ((18, 20), (40, 34), (96, 18), (110, 40), (70, 14), (24, 54)))
    + f'<path d="M30 46 H98 Q104 46 104 54 V80 H24 V54 Q24 46 30 46Z" fill="#7A3C8C" {W(3.2)}/>'
    f'<path d="M34 46 Q64 30 94 46" fill="#5A2A6A" {W(3)}/>'
    f'<rect x="50" y="54" width="28" height="22" rx="4" fill="#FFE9A6" {W(2.6)}/>' + face(64, 63, d=6, k=0.5) +
    f'<circle cx="38" cy="88" r="14" fill="#E3B23C" {W(3)}/><circle cx="38" cy="88" r="4" fill="{O}"/>'
    f'<path d="M38 74 V102 M24 88 H52 M28 78 L48 98 M48 78 L28 98" stroke="{O}" stroke-width="1.8"/>'
    f'<circle cx="92" cy="88" r="14" fill="#E3B23C" {W(3)}/><circle cx="92" cy="88" r="4" fill="{O}"/>'
    f'<path d="M92 74 V102 M78 88 H106 M82 78 L102 98 M102 78 L82 98" stroke="{O}" stroke-width="1.8"/>'
    f'<path d="M110 92 Q120 84 126 90 M112 100 Q122 98 128 102" stroke="#fff" stroke-width="4" fill="none"/>')

I["lib23-gorky-kids"] = ("#FFF1F6", "#D06A92",
    "пухлый рыжий хомяк в круглых очках с набитыми щеками",
    "сидит на высокой стопке книг и набивает щёки вылетающими из книжки буквами",
    f'<rect x="30" y="98" width="70" height="12" rx="2" fill="#3F7FD8" {W(2.6)}/>'
    f'<rect x="36" y="86" width="60" height="12" rx="2" fill="#4CB07A" {W(2.6)}/>'
    f'<rect x="28" y="110" width="74" height="14" rx="2" fill="#E8434A" {W(2.6)}/>'
    f'<ellipse cx="64" cy="64" rx="30" ry="26" fill="#F2A65A" {W(3.2)}/>'
    f'<ellipse cx="64" cy="72" rx="18" ry="14" fill="#FFE2C2"/>'
    f'<circle cx="40" cy="42" r="8" fill="#F2A65A" {W(2.6)}/><circle cx="88" cy="42" r="8" fill="#F2A65A" {W(2.6)}/>'
    f'<circle cx="40" cy="42" r="4" fill="#FF9FB8"/><circle cx="88" cy="42" r="4" fill="#FF9FB8"/>'
    f'<ellipse cx="44" cy="70" rx="10" ry="9" fill="#FFD3A8" {W(2)}/><ellipse cx="84" cy="70" rx="10" ry="9" fill="#FFD3A8" {W(2)}/>'
    + eye(55, 56, 0.7) + eye(73, 56, 0.7) +
    f'<circle cx="55" cy="56" r="7" fill="none" {W(2)}/><circle cx="73" cy="56" r="7" fill="none" {W(2)}/><path d="M62 56 H66" {W(2)}/>'
    f'<ellipse cx="64" cy="66" rx="3" ry="2" fill="#E8434A"/>'
    f'<text x="98" y="34" font-family="Arial" font-weight="bold" font-size="16" fill="#3F7FD8" stroke="{O}" stroke-width="1">А</text>'
    f'<text x="14" y="34" font-family="Arial" font-weight="bold" font-size="14" fill="#4CB07A" stroke="{O}" stroke-width="1">Б</text>'
    f'<text x="104" y="60" font-family="Arial" font-weight="bold" font-size="12" fill="#E8434A" stroke="{O}" stroke-width="1">В</text>')

I["lib31-kids-sao"] = ("#E9F9FF", "#3C9CC8",
    "белый аист с красным клювом и мордашкой",
    "летит над черепичными крышами и несёт в клюве на ленточке раскрытую книжку",
    f'<path d="M-2 110 L14 96 L30 110 L46 98 L62 110 L80 96 L98 110 L114 98 L130 110 V130 H-2Z" fill="#D8643A" {W(2.6)}/>'
    f'<rect x="20" y="88" width="6" height="12" fill="#8A5A3C" {W(2)}/>'
    f'<path d="M34 54 Q20 34 6 40 Q22 46 30 62Z" fill="#fff" {W(2.6)}/><path d="M6 40 L14 44" stroke="{O}" stroke-width="5"/>'
    f'<path d="M80 54 Q98 30 120 36 Q104 46 90 64Z" fill="#fff" {W(2.6)}/><path d="M112 38 L120 36" stroke="{O}" stroke-width="5"/>'
    f'<ellipse cx="58" cy="60" rx="30" ry="14" fill="#fff" {W(3)}/>'
    f'<path d="M30 62 L16 72 M32 66 L22 78" stroke="#E8434A" stroke-width="3"/>'
    f'<circle cx="88" cy="48" r="11" fill="#fff" {W(2.8)}/>' + eye(91, 46, 0.55) +
    f'<ellipse cx="84" cy="53" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M98 48 L120 56 L98 54Z" fill="#E8434A" {W(2.2)}/>'
    f'<path d="M110 56 V70" stroke="#E8434A" stroke-width="2"/>'
    f'<path d="M110 70 L98 76 L98 92 L110 86Z" fill="#FFE27A" {W(2.2)}/><path d="M110 70 L122 76 L122 92 L110 86Z" fill="#FFE27A" {W(2.2)}/>')

I["lib45-kids"] = ("#F3FFE6", "#6FA83C",
    "медный флюгер-петушок на шпиле с мордашкой",
    "крутится на ветру на крыше, а ветер уносит из открытой форточки листочки-страницы",
    f'<path d="M30 130 V96 L64 70 L98 96 V130Z" fill="#E8D7B0" {W(3)}/>'
    f'<path d="M24 98 L64 66 L104 98" fill="none" stroke="#B0412E" stroke-width="7" stroke-linejoin="round"/>'
    f'<rect x="54" y="100" width="20" height="16" fill="#8FD0F2" {W(2.4)}/>'
    f'<path d="M64 66 V30" stroke="{O}" stroke-width="3"/><path d="M50 30 H78" stroke="{O}" stroke-width="2.4"/>'
    f'<path d="M48 26 Q48 8 64 10 Q72 4 76 12 Q86 12 84 22 L92 18 Q96 30 82 30 H52 Q46 30 48 26Z" fill="#E09A3A" {W(2.8)}/>'
    f'<path d="M62 8 Q64 2 68 6" fill="#E8434A" {W(2)}/>'
    + eye(70, 18, 0.55) + f'<path d="M78 18 L84 20 L78 22Z" fill="#FFD84A" {W(1.4)}/>'
    + "".join(f'<g transform="rotate({r} {x} {y})"><rect x="{x-7}" y="{y-9}" width="14" height="18" rx="1.5" fill="#fff" {W(2)}/>'
              f'<path d="M{x-4} {y-4} H{x+4} M{x-4} {y} H{x+4} M{x-4} {y+4} H{x+2}" stroke="#B9AFA0" stroke-width="1.4"/></g>'
              for x, y, r in ((96, 72, 20), (110, 52, -15), (22, 58, 10)))
    + f'<path d="M4 40 Q20 34 34 40 M90 88 Q104 82 118 88" stroke="#fff" stroke-width="3" fill="none"/>')

I["lib125-kids"] = ("#EEE8FF", "#6A58B8",
    "круглый будильник с двумя звонками в ночном колпаке с помпоном",
    "задремал на тумбочке, уронив голову на раскрытую книжку сказок, над ним плывут «Zzz»",
    f'<rect x="10" y="100" width="108" height="30" fill="#A86E3C" {W(3)}/>'
    f'<path d="M30 104 L64 98 L98 104 L98 110 L64 106 L30 110Z" fill="#FFFDF5" {W(2.4)}/>'
    f'<circle cx="60" cy="66" r="28" fill="#4CB07A" {W(3.2)}/><circle cx="60" cy="66" r="21" fill="#FFFDF5" {W(2.4)}/>'
    f'<circle cx="38" cy="40" r="8" fill="#E3B23C" {W(2.6)}/><circle cx="82" cy="40" r="8" fill="#E3B23C" {W(2.6)}/>'
    f'<path d="M44 92 L38 100 M76 92 L82 100" stroke="{O}" stroke-width="3"/>'
    f'<path d="M50 64 Q54 68 58 64 M62 64 Q66 68 70 64" fill="none" {W(2.2)}/>'
    f'<path d="M56 74 Q60 77 64 74" fill="none" {W(2)}/>'
    f'<ellipse cx="46" cy="72" rx="3.5" ry="2" fill="#FF7FA8" opacity=".6"/><ellipse cx="74" cy="72" rx="3.5" ry="2" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M36 46 Q50 18 86 20 Q78 30 84 44 Q60 36 36 46Z" fill="#E8434A" {W(2.6)}/>'
    f'<circle cx="88" cy="20" r="6" fill="#fff" {W(2.2)}/>'
    f'<text x="94" y="56" font-family="Arial" font-weight="bold" font-size="12" fill="#fff">z</text>'
    f'<text x="102" y="44" font-family="Arial" font-weight="bold" font-size="16" fill="#fff">Z</text>')

I["lib136-kids"] = ("#0F2350", "#2B4C8C",
    "медный телескоп на деревянной треноге с мордашкой на трубе",
    "смотрит из открытого круглого окна библиотеки на ночное небо, где звёзды сложились в буквы",
    f'<circle cx="64" cy="64" r="58" fill="none" stroke="#7A8FB8" stroke-width="10"/>'
    f'<text x="70" y="36" font-family="Arial" font-weight="bold" font-size="14" fill="#FFE27A">А Б</text>'
    + stars(((30, 30), (98, 52), (52, 20), (106, 26)), 3, "#FFE27A") +
    f'<path d="M50 120 L62 82 L74 120 M62 82 V120" stroke="#A86E3C" stroke-width="4" stroke-linecap="round"/>'
    f'<g transform="rotate(-30 62 76)"><rect x="34" y="66" width="62" height="18" rx="6" fill="#E3B23C" {W(3)}/>'
    f'<rect x="92" y="62" width="10" height="26" rx="3" fill="#C98A2A" {W(2.6)}/>'
    f'<rect x="26" y="70" width="10" height="10" rx="2" fill="#C98A2A" {W(2.4)}/></g>'
    + face(58, 72, d=6, k=0.5))

I["lib82-kids"] = ("#E0FBFF", "#2A8FA8",
    "розовая медуза с колпачком-куполом и лентами-щупальцами",
    "читает под водой раскрытую книжку, придерживая её щупальцами, вокруг поднимаются пузырьки",
    f'<path d="M-2 112 Q20 104 40 112 Q64 120 88 110 Q108 104 130 112 V130 H-2Z" fill="#F2D49A" {W(2.6)}/>'
    f'<path d="M100 112 Q96 92 104 80 M108 112 Q112 96 106 86" stroke="#4CB07A" stroke-width="4" fill="none"/>'
    f'<path d="M30 58 Q30 22 64 22 Q98 22 98 58 Q90 54 82 58 Q72 54 64 58 Q56 54 46 58 Q38 54 30 58Z" fill="#FF9FC6" {W(3)}/>'
    f'<path d="M40 34 Q50 28 58 30" stroke="#fff" stroke-width="3" fill="none" opacity=".7"/>'
    + face(64, 42, d=8, k=0.6) +
    "".join(f'<path d="M{x} 58 Q{x+6} 72 {x-2} 84 Q{x+4} 94 {x} 104" stroke="#F06FA8" stroke-width="3" fill="none"/>' for x in (36, 50, 78, 92))
    + f'<path d="M64 84 L44 76 L44 96 L64 102Z" fill="#FFFDF5" {W(2.4)}/><path d="M64 84 L84 76 L84 96 L64 102Z" fill="#FFFDF5" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="2"/>' for x, y, r in ((106, 40, 5), (112, 24, 3), (18, 50, 4), (22, 32, 2.5))))

I["gaidar-kids-library"] = ("#FFF8E8", "#4C9A5A",
    "деревянная голубятня на столбе с красной звездой на крыше и мордашкой в окошке",
    "стоит в летнем дачном саду, а над ней кружат три белых голубя",
    f'<path d="M-2 104 Q40 96 64 102 Q96 108 130 98 V130 H-2Z" fill="#7CC46A" {W(3)}/>'
    f'<rect x="60" y="72" width="8" height="40" fill="#8A5A3C" {W(2.6)}/>'
    f'<rect x="40" y="46" width="48" height="30" fill="#D9A066" {W(3)}/>'
    f'<path d="M34 48 L64 26 L94 48Z" fill="#B0412E" {W(3)}/>'
    f'<path d="M64 30 L66.5 36 L73 36 L68 40 L70 46 L64 42 L58 46 L60 40 L55 36 L61.5 36Z" fill="#E8434A" {W(1.6)}/>'
    f'<rect x="52" y="54" width="24" height="16" rx="8" fill="#3B3355"/>' + face(64, 61, d=5, k=0.45) +
    f'<path d="M36 76 H92" stroke="{O}" stroke-width="3"/>'
    + "".join(f'<path d="M{x-10} {y} Q{x-4} {y-8} {x} {y} Q{x+4} {y-8} {x+10} {y} Q{x} {y+4} {x-10} {y}Z" fill="#fff" {W(1.8)}/>' for x, y in ((24, 30), (104, 22), (100, 52))))

I["lib14-kids-central"] = ("#1E2A5A", "#5A4CA8",
    "дирижабль, оболочка которого — книжный переплёт с корешком и закладкой",
    "плывёт над ночными крышами города, из гондолы машет фонариком",
    f'<path d="M-2 110 H20 V92 H34 V104 H50 V86 H66 V108 H84 V94 H100 V104 H130 V130 H-2Z" fill="#2B2B4A" {W(2.4)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="#FFE27A"/>' for x, y in ((24, 98), (54, 92), (88, 100), (70, 112)))
    + f'<ellipse cx="64" cy="46" rx="44" ry="22" fill="#2E8F6A" {W(3.2)}/>'
    f'<path d="M64 24 V68" stroke="#E3B23C" stroke-width="5"/>'
    f'<path d="M28 34 Q46 30 58 34 M70 34 Q84 30 100 34" stroke="#FFFDF5" stroke-width="2" fill="none"/>'
    + face(42, 48, d=6, k=0.5) +
    f'<path d="M66 68 L64 86 L70 80 L74 88 L72 68" fill="#E8434A" {W(2)}/>'
    f'<path d="M50 66 L54 76 H78 L82 66" fill="none" stroke="{O}" stroke-width="2"/>'
    f'<rect x="52" y="76" width="28" height="10" rx="3" fill="#E3B23C" {W(2.4)}/>'
    f'<circle cx="86" cy="80" r="3" fill="#FFE27A"/><path d="M86 80 L104 92 L98 72Z" fill="#FFE27A" opacity=".35"/>'
    + stars(((14, 22), (110, 18), (60, 12)), 3, "#FFE27A"))

I["reutov-kids-central-library"] = ("#EFFFF8", "#3CA88C",
    "белый школьный микроскоп в круглых очках с мордашкой на тубусе",
    "склонился над раскрытой книгой и разглядывает огромную букву «А» на странице",
    f'<path d="M20 108 L64 98 L108 108 L108 118 L64 110 L20 118Z" fill="#FFFDF5" {W(2.6)}/>'
    f'<path d="M64 98 V110" stroke="{O}" stroke-width="2"/>'
    f'<text x="76" y="110" font-family="Arial" font-weight="bold" font-size="14" fill="#E8434A" stroke="{O}" stroke-width="1">А</text>'
    f'<rect x="26" y="88" width="40" height="10" rx="3" fill="#5A6A80" {W(2.6)}/>'
    f'<path d="M40 88 Q30 70 40 54" fill="none" stroke="#5A6A80" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M40 88 Q30 70 40 54" fill="none" {W(2)}/>'
    f'<g transform="rotate(30 60 46)"><rect x="50" y="16" width="22" height="50" rx="6" fill="#fff" {W(3)}/>'
    f'<rect x="54" y="66" width="14" height="12" fill="#C9D2DE" {W(2.4)}/>'
    f'<rect x="48" y="10" width="26" height="8" rx="3" fill="#5A6A80" {W(2.4)}/></g>'
    + eye(58, 40, 0.55) + eye(70, 46, 0.55) +
    f'<circle cx="58" cy="40" r="6" fill="none" {W(2)}/><circle cx="70" cy="46" r="6" fill="none" {W(2)}/>'
    f'<circle cx="86" cy="96" r="12" fill="#BFE3FF" opacity=".5" {W(1.6)}/>'
    + sparkle(104, 30, 5) + sparkle(20, 34, 4))

# --- музеи ---
I["kolomenskoe-water-mill"] = ("#E9FFF2", "#3E9E77",
    "деревянное мельничное водяное колесо с лопатками и мордашкой на ступице",
    "крутится в бегущем ручье у бревенчатой стенки мельницы, разбрызгивая капли",
    f'<rect x="76" y="20" width="56" height="90" fill="#A86E3C" {W(3)}/>'
    + "".join(f'<path d="M76 {y} H132" stroke="#8A5428" stroke-width="2.4"/>' for y in (36, 52, 68, 84, 100))
    + f'<path d="M-2 100 Q20 92 40 100 Q60 108 80 100 Q100 92 130 100 V130 H-2Z" fill="#3F8FD8" {W(3)}/>'
    f'<circle cx="52" cy="70" r="34" fill="none" stroke="#C98A4A" stroke-width="8"/>'
    f'<circle cx="52" cy="70" r="34" fill="none" {W(2)}/><circle cx="52" cy="70" r="26" fill="none" {W(2)}/>'
    + "".join(f'<path d="M52 70 L{52+34*c:.1f} {70+34*sn:.1f}" stroke="#A86E3C" stroke-width="4"/>' for c, sn in ((1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)))
    + f'<circle cx="52" cy="70" r="13" fill="#E8B878" {W(2.8)}/>' + face(52, 69, d=4.5, k=0.42) +
    "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#BFE3FF" {W(1.2)}/>' for x, y in ((14, 82), (20, 70), (90, 92), (30, 96)))
    + sparkle(22, 24, 5))

I["peter-dutch-house"] = ("#E8F1FF", "#3A62B0",
    "высокий кожаный ботфорт Петра Первого с медной шпорой и мордашкой на голенище",
    "широко шагает по сине-белой голландской плитке с нарисованной мельницей",
    "".join(f'<rect x="{x}" y="{y}" width="22" height="22" fill="#FFFFFF" {W(1.8)}/>' for x in (-2, 20, 42, 64, 86, 108) for y in (96, 118))
    + "".join(f'<circle cx="{x+11}" cy="{y+11}" r="5" fill="none" stroke="#3A62B0" stroke-width="2"/>' for x in (-2, 42, 86) for y in (96,))
    + f'<path d="M44 14 H86 L84 70 Q84 80 92 82 L110 86 Q118 88 116 96 H44 Z" fill="#3B2A22" {W(3.2)}/>'
    f'<path d="M40 14 H90 L88 30 H42Z" fill="#5A3C2C" {W(3)}/>'
    f'<path d="M50 20 Q56 18 60 22" stroke="#fff" stroke-width="2" opacity=".5" fill="none"/>'
    + face(64, 50, d=8, k=0.65) +
    f'<path d="M44 92 L30 88" stroke="{O}" stroke-width="3"/><circle cx="26" cy="88" r="6" fill="#E3B23C" {W(2.4)}/>'
    f'<path d="M26 80 V96 M18 88 H34" stroke="{O}" stroke-width="1.6"/>')

I["liskun-livestock-museum"] = ("#F3FFE8", "#7AB04C",
    "пятнистая корова-рекордсменка с золотой медалью на ленте и колокольчиком",
    "гордо стоит на трёхступенчатом пьедестале с цифрой 1 под музейной табличкой",
    f'<rect x="34" y="100" width="60" height="30" fill="#E3B23C" {W(3)}/>'
    f'<rect x="10" y="110" width="26" height="20" fill="#C9D2DE" {W(2.6)}/><rect x="92" y="114" width="26" height="16" fill="#E8A86A" {W(2.6)}/>'
    f'<text x="58" y="122" font-family="Arial" font-weight="bold" font-size="16" fill="{O}">1</text>'
    f'<rect x="38" y="74" width="8" height="26" fill="#fff" {W(2.4)}/><rect x="82" y="74" width="8" height="26" fill="#fff" {W(2.4)}/>'
    f'<ellipse cx="64" cy="70" rx="34" ry="20" fill="#fff" {W(3)}/>'
    f'<path d="M44 58 Q52 52 58 62 Q50 70 44 64Z M76 72 Q86 66 92 76 Q84 84 76 78Z" fill="#3B3355"/>'
    f'<ellipse cx="64" cy="40" rx="18" ry="16" fill="#fff" {W(3)}/>'
    f'<path d="M46 32 L38 26 M82 32 L90 26" stroke="{O}" stroke-width="3"/>'
    f'<path d="M50 26 Q46 18 52 16 M78 26 Q82 18 76 16" stroke="#E8D7B0" stroke-width="4" fill="none"/>'
    f'<ellipse cx="64" cy="48" rx="11" ry="7" fill="#FFB8C8" {W(2.4)}/>'
    + eye(57, 36, 0.6) + eye(71, 36, 0.6) +
    f'<path d="M50 52 L64 66 L78 52" fill="none" stroke="#3F7FD8" stroke-width="3"/>'
    f'<circle cx="64" cy="68" r="7" fill="#FFD84A" {W(2.2)}/>' + sparkle(100, 30, 5) + sparkle(24, 40, 4))

I["guns-interactive-museum"] = ("#F2EEE8", "#8C6A4A",
    "рыцарские латы с узким забралом и красным плюмажем, в прорези забрала — мордашка",
    "стоят в каменном зале на фоне гобелена и держат деревянный тренировочный меч",
    f'<rect x="8" y="12" width="40" height="56" fill="#3F7FD8" {W(2.6)}/><path d="M8 68 L18 60 L28 68 L38 60 L48 68" fill="none" {W(2)}/>'
    f'<path d="M28 24 L32 34 L28 44 L24 34Z" fill="#FFD84A" {W(1.6)}/>'
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#B9AFA0" {W(2.6)}/>'
    f'<rect x="46" y="66" width="36" height="40" rx="8" fill="#C9D2DE" {W(3)}/>'
    f'<path d="M50 80 H78 M50 92 H78" stroke="#8C98AA" stroke-width="2"/>'
    f'<path d="M46 40 Q46 18 64 18 Q82 18 82 40 V60 Q82 68 64 68 Q46 68 46 60Z" fill="#DDE3EC" {W(3)}/>'
    f'<rect x="50" y="36" width="28" height="12" rx="4" fill="#3B3355"/>' + eye(58, 42, 0.5) + eye(70, 42, 0.5) +
    f'<path d="M64 18 Q74 2 92 8 Q78 10 70 20Z" fill="#E8434A" {W(2.4)}/>'
    f'<path d="M96 30 V100" stroke="#C98A4A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M86 88 H106" stroke="#8A5428" stroke-width="6" stroke-linecap="round"/>'
    f'<circle cx="90" cy="92" r="5" fill="#C9D2DE" {W(2)}/>')

I["gorky-park-museum"] = ("#FFF0E6", "#D8643A",
    "парадная белая арка главного входа Парка Горького с колоннами, флагами и мордашкой на фронтоне",
    "встречает гостей над аллеей, а сквозь пролёт виден круглый фонтан с брызгами",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#E8D7B0" {W(2.6)}/><path d="M48 104 L40 130 M80 104 L88 130" stroke="#C9B58A" stroke-width="2"/>'
    f'<rect x="8" y="44" width="112" height="16" fill="#FFFDF5" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="60" width="10" height="44" fill="#FFFDF5" {W(2.6)}/>' for x in (12, 28, 90, 106))
    + f'<rect x="44" y="60" width="40" height="44" fill="#BFE3FF" {W(2.6)}/>'
    f'<ellipse cx="64" cy="98" rx="14" ry="4" fill="#3F8FD8" {W(2)}/><path d="M64 96 V80 M58 84 Q64 74 70 84" stroke="#3F8FD8" stroke-width="2.6" fill="none"/>'
    f'<path d="M20 44 L64 20 L108 44Z" fill="#FFFDF5" {W(3)}/>' + face(64, 34, d=6, k=0.5) +
    f'<path d="M22 44 V14 M106 44 V14" stroke="{O}" stroke-width="2.4"/>'
    f'<path d="M22 14 L38 18 L22 24Z" fill="#E8434A" {W(1.8)}/><path d="M106 14 L122 18 L106 24Z" fill="#3F7FD8" {W(1.8)}/>')

I["zhukovsky-aviation-blagovest"] = ("#DFF1FF", "#3A7FC0",
    "серебристый реактивный истребитель со стреловидными крыльями и мордашкой на носу",
    "взмывает свечкой вверх из облаков, оставляя за собой белый пушистый след",
    f'<path d="M28 128 Q22 112 34 108 Q30 96 44 96 Q50 84 62 92 Q74 88 74 100 Q86 100 84 112 Q96 116 92 128Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M58 100 Q60 80 64 66" stroke="#fff" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M64 10 Q74 24 74 44 L74 70 H54 L54 44 Q54 24 64 10Z" fill="#C9D2DE" {W(3)}/>'
    f'<path d="M54 44 L22 66 L22 72 L54 62Z M74 44 L106 66 L106 72 L74 62Z" fill="#AEB8C6" {W(3)}/>'
    f'<path d="M56 66 L44 80 L56 76Z M72 66 L84 80 L72 76Z" fill="#AEB8C6" {W(2.4)}/>'
    f'<path d="M60 22 Q64 16 68 22 V30 H60Z" fill="#3F7FD8" {W(2.2)}/>'
    + face(64, 40, d=5, k=0.45) +
    f'<path d="M58 70 L64 82 L70 70Z" fill="#FFB43A" {W(2)}/>'
    f'<path d="M30 64 L34 64" stroke="#E8434A" stroke-width="3"/><circle cx="96" cy="64" r="2.6" fill="#E8434A"/>'
    + sparkle(100, 24, 5) + sparkle(24, 30, 4))

I["money-museum"] = ("#FFFBE6", "#C8A03A",
    "медная копейка с мордашкой и Георгием на коне на аверсе",
    "катится по ступенькам из столбиков монет прямо к щели в синей копилке-сундучке",
    f'<rect x="80" y="84" width="40" height="30" rx="4" fill="#3F7FD8" {W(3)}/><path d="M80 94 H120" stroke="{O}" stroke-width="2.4"/>'
    f'<rect x="92" y="80" width="16" height="4" rx="2" fill="#3B3355"/>'
    + "".join(f'<rect x="{x}" y="{114-h}" width="18" height="{h}" fill="#F2C94C" {W(2.4)}/>' for x, h in ((8, 18), (26, 30), (44, 42)))
    + "".join(f'<path d="M{x} {y} H{x+18}" stroke="#C8A03A" stroke-width="1.6"/>' for x, y in ((8, 104), (26, 94), (26, 104), (44, 82), (44, 92), (44, 102)))
    + f'<path d="M-2 114 H130 V130 H-2Z" fill="#E8D7B0" {W(2.6)}/>'
    f'<circle cx="72" cy="48" r="24" fill="#D8843A" {W(3.2)}/><circle cx="72" cy="48" r="18" fill="none" stroke="#B0602A" stroke-width="2"/>'
    + face(72, 46, d=7, k=0.6) +
    f'<path d="M46 70 Q52 76 58 72 M38 62 Q44 68 50 64" stroke="#C8A03A" stroke-width="2.4" fill="none"/>'
    + sparkle(104, 22, 5) + sparkle(30, 30, 4, "#FFD84A"))

I["mirek-accordion-museum"] = ("#FFEFF0", "#C04A5A",
    "кнопочный баян с перламутровыми пуговками и мордашкой на гармошке мехов",
    "широко растягивает меха на деревенской завалинке, а из мехов вылетают ноты",
    f'<rect x="-2" y="100" width="132" height="12" fill="#A86E3C" {W(2.6)}/><rect x="-2" y="112" width="132" height="18" fill="#8A5428" {W(2.6)}/>'
    f'<rect x="12" y="40" width="26" height="60" rx="4" fill="#2B2B3A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#FFF6E8" {W(1.2)}/>' for x in (20, 30) for y in (50, 60, 70, 80, 90))
    + f'<path d="M38 44 L48 40 L56 44 L64 40 L72 44 L80 40 L90 44 V96 L80 100 L72 96 L64 100 L56 96 L48 100 L38 96Z" fill="#E8434A" {W(3)}/>'
    + "".join(f'<path d="M{x} 42 V98" stroke="#B0302A" stroke-width="2"/>' for x in (48, 56, 64, 72, 80))
    + f'<rect x="90" y="40" width="26" height="60" rx="4" fill="#2B2B3A" {W(3)}/>'
    + "".join(f'<rect x="96" y="{y}" width="14" height="5" rx="1" fill="#FFF6E8" {W(1)}/>' for y in (48, 58, 68, 78, 88))
    + f'<ellipse cx="64" cy="70" rx="16" ry="12" fill="#FFE2C2" {W(2.2)}/>' + face(64, 68, d=6, k=0.5) +
    f'<text x="46" y="28" font-family="Arial" font-size="18" fill="{O}">♪</text><text x="72" y="20" font-family="Arial" font-size="16" fill="{O}">♫</text>')

I["mchs-museum-center"] = ("#FFF0E0", "#D8543A",
    "красный огнетушитель с чёрным шлангом и мордашкой на баллоне",
    "стоит по стойке смирно рядом со свёрнутым пожарным рукавом и пускает струю белой пены",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#C9D2DE" {W(2.6)}/>'
    f'<circle cx="98" cy="96" r="16" fill="#F2C94C" {W(3)}/><circle cx="98" cy="96" r="10" fill="none" {W(2)}/><circle cx="98" cy="96" r="4" fill="#F2C94C" {W(2)}/>'
    f'<rect x="38" y="40" width="34" height="68" rx="14" fill="#E8434A" {W(3.2)}/>'
    f'<rect x="38" y="70" width="34" height="14" fill="#fff" {W(2)}/>'
    + face(55, 56, d=6, k=0.55) +
    f'<rect x="48" y="28" width="14" height="12" fill="#5A6A80" {W(2.4)}/><path d="M50 28 L62 20" stroke="{O}" stroke-width="4"/>'
    f'<path d="M62 32 Q86 26 88 46 Q90 60 82 66" stroke="#2B2B3A" stroke-width="4" fill="none"/>'
    f'<path d="M82 66 Q100 58 112 70 Q120 62 124 74 Q116 84 104 80 Q92 84 86 74Z" fill="#fff" {W(2.2)}/>'
    + sparkle(20, 30, 5) + sparkle(24, 80, 4))

I["vorobyovy-ecocenter"] = ("#F0FFE0", "#5E9A3C",
    "рыжая белка-экскурсовод с пушистым хвостом и указкой",
    "стоит на склоне Воробьёвых гор и показывает указкой на изгиб реки внизу",
    f'<path d="M-2 70 Q30 64 50 76 Q80 92 130 80 V130 H-2Z" fill="#6FB84A" {W(3)}/>'
    f'<path d="M-2 98 Q40 88 80 104 Q104 112 130 104 V130 H-2Z" fill="#3F8FD8" {W(2.8)}/>'
    f'<path d="M100 46 Q118 30 112 12 Q104 4 100 14" fill="#4CB07A" {W(2.4)}/><path d="M104 46 V68" stroke="#8A5428" stroke-width="4"/>'
    f'<path d="M30 92 Q8 80 14 56 Q20 36 36 44 Q24 60 40 78Z" fill="#E07A2A" {W(3)}/>'
    f'<ellipse cx="46" cy="80" rx="14" ry="16" fill="#F29A3A" {W(3)}/><ellipse cx="46" cy="84" rx="8" ry="10" fill="#FFE2C2"/>'
    f'<circle cx="50" cy="56" r="13" fill="#F29A3A" {W(3)}/>'
    f'<path d="M40 46 L42 36 L48 44 M56 44 L60 36 L62 46" fill="#F29A3A" {W(2.2)}/>'
    + eye(46, 55, 0.55) + eye(56, 55, 0.55) +
    f'<ellipse cx="51" cy="62" rx="2" ry="1.4" fill="{O}"/>'
    f'<path d="M58 74 L94 92" stroke="#A86E3C" stroke-width="3" stroke-linecap="round"/><circle cx="94" cy="92" r="3" fill="#E8434A"/>'
    + sparkle(80, 24, 5))

I["vysotsky-house-taganka"] = ("#EDE6F8", "#5A4A7A",
    "семиструнная гитара цвета вишни с бантом на грифе и мордашкой на деке",
    "прислонилась к кирпичной стене рядом с наклеенной театральной афишей",
    "".join(f'<rect x="{x + (8 if y % 2 else 0)}" y="{y*12}" width="16" height="12" fill="#C46A4A" {W(1.4)}/>' for y in range(11) for x in range(-8, 130, 16))
    + f'<rect x="78" y="22" width="40" height="54" fill="#FFF6DC" {W(2.6)}/>'
    f'<path d="M84 32 H112 M84 40 H108 M84 48 H112" stroke="#3B3355" stroke-width="2.4"/>'
    f'<rect x="86" y="56" width="24" height="12" fill="#E8434A" {W(1.6)}/>'
    f'<path d="M-2 112 H130 V130 H-2Z" fill="#6A5A50" {W(2.4)}/>'
    f'<g transform="rotate(-14 48 70)"><rect x="44" y="6" width="10" height="56" fill="#5A3C2C" {W(2.6)}/>'
    f'<rect x="40" y="0" width="18" height="12" rx="3" fill="#3B2A22" {W(2.4)}/>'
    f'<path d="M30 84 Q26 66 38 60 Q34 50 49 50 Q64 50 60 60 Q72 66 68 84 Q66 106 49 106 Q32 106 30 84Z" fill="#A0303A" {W(3)}/>'
    f'<circle cx="49" cy="76" r="7" fill="#3B2A22"/></g>'
    + face(44, 92, d=6, k=0.5) +
    f'<path d="M44 20 Q36 14 34 22 Q40 26 44 20 Q50 12 54 20 Q50 26 44 20Z" fill="#3F7FD8" {W(1.8)}/>')

I["tsvetaeva-house-borisoglebsky"] = ("#F4F0FF", "#7A68B8",
    "старинная стеклянная чернильница с гусиным пером и мордашкой на баночке",
    "стоит на подоконнике у окна с наличником, а перо само выводит строчку на листке",
    f'<rect x="10" y="10" width="108" height="76" fill="#BFD8F2" {W(3)}/>'
    f'<path d="M64 10 V86 M10 48 H118" stroke="#FFFDF5" stroke-width="5"/>'
    f'<path d="M4 12 Q64 -6 124 12 L118 18 Q64 4 10 18Z" fill="#C46A4A" {W(2.4)}/>'
    f'<rect x="-2" y="86" width="132" height="14" fill="#E8D7B0" {W(2.8)}/>'
    f'<rect x="-2" y="100" width="132" height="30" fill="#8A5A3C" {W(2.6)}/>'
    f'<path d="M66 92 L118 80 L120 90 L68 100Z" fill="#FFFDF5" {W(2.2)}/>'
    f'<path d="M76 92 Q84 86 90 92 Q96 86 104 88" stroke="#3F3F8F" stroke-width="2" fill="none"/>'
    f'<path d="M24 64 H56 L58 90 H22Z" fill="#9FC8E8" {W(3)}/><rect x="30" y="56" width="20" height="10" fill="#5A6A80" {W(2.4)}/>'
    f'<path d="M26 74 H56 L57 88 H24Z" fill="#2E3E8F" opacity=".7"/>'
    + face(40, 72, d=6, k=0.5) +
    f'<path d="M44 58 Q70 24 100 22 Q86 34 80 46 Q66 54 44 58Z" fill="#fff" {W(2.4)}/><path d="M44 58 L86 30" stroke="#B9AFA0" stroke-width="1.6"/>')

# --- творчество и природа ---
I["krasnaya-sosna-eco-center"] = ("#FFF6E8", "#B86A3A",
    "сосновая шишка с мордашкой и зелёным хвойным чубчиком",
    "катится по лесной тропинке между красными стволами сосен, подпрыгивая на корнях",
    "".join(f'<rect x="{x}" y="-2" width="14" height="110" fill="#C4603A" {W(2.6)}/>' for x in (6, 104))
    + f'<path d="M-2 22 Q20 4 40 20 Q30 0 64 -4 M88 20 Q108 4 130 22" fill="#3E8E4A" {W(2.4)}/>'
    f'<path d="M-2 104 Q40 94 64 102 Q96 110 130 100 V130 H-2Z" fill="#C9A06A" {W(3)}/>'
    f'<path d="M30 110 Q48 104 64 112 Q80 120 100 112" stroke="#A8804A" stroke-width="3" fill="none"/>'
    f'<ellipse cx="64" cy="70" rx="24" ry="30" fill="#A0602A" {W(3.2)}/>'
    + "".join(f'<path d="M{x-8} {y} Q{x} {y+6} {x+8} {y}" stroke="#6A3A1A" stroke-width="2.4" fill="none"/>' for x, y in ((56, 52), (72, 52), (50, 66), (64, 64), (78, 66), (56, 84), (72, 84)))
    + f'<path d="M64 40 L56 26 M64 40 L64 22 M64 40 L72 26" stroke="#3E8E4A" stroke-width="4" stroke-linecap="round"/>'
    + face(64, 72, d=8, k=0.6) +
    f'<path d="M30 92 Q36 88 40 92 M90 90 Q96 86 100 90" stroke="#fff" stroke-width="2.4" fill="none"/>')

I["ddt-sokolniki-mitkovsky"] = ("#FFF0FA", "#C05AA0",
    "радужный клубок пряжи с мордашкой и двумя вязальными спицами-ручками",
    "сидит на табурете в кружке рукоделия и сам себе вяжет полосатый шарфик, свисающий до пола",
    f'<path d="M-2 112 H130 V130 H-2Z" fill="#E8D7B0" {W(2.6)}/>'
    f'<rect x="34" y="84" width="60" height="8" rx="3" fill="#A86E3C" {W(2.6)}/>'
    f'<path d="M40 92 L36 116 M88 92 L92 116" stroke="#8A5428" stroke-width="5"/>'
    f'<circle cx="64" cy="58" r="26" fill="#FF9FC6" {W(3.2)}/>'
    + "".join(f'<path d="M{a} Q64 {b} {c}" stroke="{col}" stroke-width="3" fill="none"/>' for a, b, c in
              (("40 50", 36, "88 50"), ("40 62", 46, "88 62"), ("44 74", 58, "84 74")) for col in ("#C05AA0",))
    + face(64, 58, d=8, k=0.6) +
    f'<path d="M36 48 L22 26 M92 48 L106 26" stroke="#E3B23C" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="22" cy="26" r="4" fill="#E8434A" {W(1.8)}/><circle cx="106" cy="26" r="4" fill="#3F7FD8" {W(1.8)}/>'
    + "".join(f'<rect x="96" y="{y}" width="16" height="9" fill="{c}" {W(1.8)}/>' for y, c in ((60, "#3F7FD8"), (69, "#FFD84A"), (78, "#4CB07A"), (87, "#E8434A"), (96, "#3F7FD8"), (105, "#FFD84A")))
    + f'<path d="M88 56 L96 60" stroke="{O}" stroke-width="2"/>')

I["kids-culture-center-alekseevskaya"] = ("#FFF8E0", "#D89A2A",
    "деревянная кукла-марионетка-скоморох в колпаке с бубенчиками на ниточках",
    "пляшет на маленькой сцене дома культуры, а нитки тянутся к кресту-ваге наверху",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#A86E3C" {W(2.6)}/>'
    f'<path d="M-2 -2 H22 Q18 50 26 104 H-2Z M130 -2 H106 Q110 50 102 104 H130Z" fill="#C0303A" {W(2.6)}/>'
    f'<path d="M44 12 H84 M64 6 V18" stroke="#8A5428" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M46 12 L44 72 M82 12 L84 72 M64 18 V32" stroke="#5A5A6A" stroke-width="1.2"/>'
    f'<path d="M52 42 Q46 30 64 28 Q82 30 76 42Z" fill="#3F7FD8" {W(2.4)}/>'
    f'<path d="M52 40 L40 30 M76 40 L88 30" stroke="{O}" stroke-width="2"/>'
    f'<circle cx="40" cy="30" r="3.4" fill="#FFD84A" {W(1.4)}/><circle cx="88" cy="30" r="3.4" fill="#FFD84A" {W(1.4)}/>'
    f'<circle cx="64" cy="50" r="11" fill="#FFE2C2" {W(2.6)}/>' + face(64, 50, d=4.5, k=0.42) +
    f'<path d="M52 62 H76 L80 92 H48Z" fill="#E8434A" {W(2.8)}/><path d="M64 62 V92" stroke="#FFD84A" stroke-width="3"/>'
    f'<path d="M52 66 L44 72 M76 66 L84 72" stroke="#E8B878" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M56 92 L50 102 M72 92 L80 100" stroke="#3F7FD8" stroke-width="6" stroke-linecap="round"/>')

I["exotic-park-zoo"] = ("#E6FFF0", "#2E9E6A",
    "зелёная игуана с гребнем на спине и мордашкой",
    "греется, растянувшись на корявой ветке под оранжевой лампой террариума",
    f'<circle cx="96" cy="14" r="14" fill="#FFB43A" {W(2.6)}/><path d="M84 28 L60 70 L130 70 L108 28Z" fill="#FFE27A" opacity=".35"/>'
    f'<path d="M96 0 V-2" stroke="{O}"/>'
    f'<path d="M-2 92 Q30 78 60 86 Q90 94 130 78" stroke="#8A5428" stroke-width="12" fill="none" stroke-linecap="round"/>'
    f'<path d="M-2 92 Q30 78 60 86 Q90 94 130 78" stroke="{O}" stroke-width="1.6" fill="none"/>'
    f'<path d="M22 84 Q8 96 14 110 Q20 116 26 108" fill="none" stroke="#4CB07A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M24 80 Q50 60 86 70 Q102 74 106 66 Q112 58 104 54 Q94 50 88 58 L82 66 Q50 56 24 80Z" fill="#4CB07A" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} L{x+3} {y-7} L{x+6} {y}" fill="#2E8F5A" {W(1.6)}/>' for x, y in ((40, 70), (50, 65), (60, 63), (70, 63), (80, 64)))
    + eye(98, 58, 0.55) + f'<ellipse cx="94" cy="66" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M100 64 Q104 66 106 64" fill="none" {W(1.6)}/>'
    f'<path d="M44 76 L40 88 M70 72 L72 86" stroke="#4CB07A" stroke-width="5" stroke-linecap="round"/>'
    + sparkle(30, 30, 5))

I["smile-theatre"] = ("#FDEBFF", "#9A4AB8",
    "театральный бинокль из перламутра на ручке-лорнете с мордашкой на перемычке",
    "выглядывает из-за бархатного бортика балкона и смотрит на освещённую сцену с красным занавесом",
    f'<path d="M14 6 H114 V60 H14Z" fill="#FFE27A" {W(2.6)}/>'
    f'<path d="M14 6 Q30 40 14 60 M114 6 Q98 40 114 60" fill="#C0303A" {W(2.6)}/>'
    f'<path d="M14 6 H114 V16 Q64 24 14 16Z" fill="#C0303A" {W(2.6)}/>'
    f'<path d="M-2 92 Q64 80 130 92 V130 H-2Z" fill="#8A2A4A" {W(3)}/>'
    f'<path d="M-2 92 Q64 80 130 92" stroke="#E3B23C" stroke-width="4" fill="none"/>'
    f'<circle cx="48" cy="70" r="14" fill="#F4ECF8" {W(3)}/><circle cx="80" cy="70" r="14" fill="#F4ECF8" {W(3)}/>'
    f'<circle cx="48" cy="70" r="8" fill="#8FD0F2" {W(2)}/><circle cx="80" cy="70" r="8" fill="#8FD0F2" {W(2)}/>'
    + eye(48, 70, 0.6) + eye(80, 70, 0.6) +
    f'<rect x="58" y="64" width="12" height="10" rx="3" fill="#E3B23C" {W(2.2)}/>'
    f'<path d="M64 84 Q64 92 60 96" fill="none" stroke="#3B2A22" stroke-width="2.4"/>'
    f'<path d="M86 86 L104 112" stroke="#E3B23C" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="80" rx="5" ry="2.4" fill="#FF7FA8" opacity=".7"/>')

I["masterskaya-12"] = ("#FFF2E6", "#B8603A",
    "суфлёрская будка-раковина у края сцены с мордашкой в глубине и раскрытой пьесой",
    "шепчет текст из-под рампы, перед ней в ряд светят тёплые лампочки",
    f'<path d="M-2 -2 H130 V70 H-2Z" fill="#7A1E2A"/>'
    + "".join(f'<path d="M{x} -2 Q{x+6} 34 {x} 70" stroke="#5A1420" stroke-width="2.4" fill="none"/>' for x in (12, 32, 52, 72, 92, 112))
    + f'<path d="M-2 70 H130 V130 H-2Z" fill="#B07A4A" {W(3)}/>'
    + "".join(f'<path d="M{x} 70 L{x-6} 130" stroke="#8A5428" stroke-width="2"/>' for x in (20, 50, 80, 110))
    + "".join(f'<circle cx="{x}" cy="80" r="4" fill="#FFE27A" {W(1.6)}/>' for x in (8, 22, 106, 120))
    + f'<path d="M30 112 Q30 62 64 60 Q98 62 98 112Z" fill="#E8D7B0" {W(3.2)}/>'
    + "".join(f'<path d="M64 112 L{x} {y}" stroke="#C9B58A" stroke-width="2"/>' for x, y in ((38, 86), (50, 70), (64, 64), (78, 70), (90, 86)))
    + f'<path d="M42 112 Q42 82 64 80 Q86 82 86 112Z" fill="#3B3355"/>'
    + face(64, 94, d=6, k=0.55) +
    f'<path d="M48 112 L64 106 L80 112 V118 L64 112 L48 118Z" fill="#FFFDF5" {W(2)}/>'
    f'<path d="M92 50 Q100 44 106 50 M96 40 Q106 34 114 42" stroke="#FFE27A" stroke-width="2.4" fill="none"/>')

I["theatre-na-melnikova"] = ("#1A1440", "#4A2A8A",
    "пара лакированных чечёточных туфель с металлическими набойками и мордашками",
    "отбивают степ в круглом луче прожектора, от набоек разлетаются золотые искры",
    f'<path d="M48 -2 H80 L118 112 H10Z" fill="#FFF6C8" opacity=".25"/>'
    f'<ellipse cx="64" cy="108" rx="54" ry="12" fill="#FFF6C8" opacity=".5"/>'
    f'<path d="M14 84 Q14 66 32 66 L50 70 Q60 72 60 82 V92 H14Z" fill="#1E1E2A" {W(3)}/>'
    f'<path d="M20 70 Q30 68 36 72" stroke="#fff" stroke-width="2.4" fill="none" opacity=".7"/>'
    f'<rect x="12" y="92" width="50" height="5" fill="#C9D2DE" {W(1.8)}/>'
    + face(36, 80, d=6, k=0.5) +
    f'<g transform="rotate(-18 92 74)"><path d="M68 74 Q68 56 86 56 L104 60 Q114 62 114 72 V82 H68Z" fill="#1E1E2A" {W(3)}/>'
    f'<path d="M74 60 Q84 58 90 62" stroke="#fff" stroke-width="2.4" fill="none" opacity=".7"/>'
    f'<rect x="66" y="82" width="50" height="5" fill="#C9D2DE" {W(1.8)}/></g>'
    + face(90, 68, d=6, k=0.5) +
    stars(((20, 104), (108, 100), (64, 118), (30, 30), (100, 26)), 4, "#FFD84A"))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
