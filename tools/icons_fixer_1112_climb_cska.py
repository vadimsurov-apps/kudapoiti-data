"""fixer 12.11: перерисовка climb-cska по сообщению Вадима («не подходит к скалолазанию»).
Герой: девочка в красно-синей форме с хвостиками; сцена: на стене детского зала тянется к верхнему зацепу, её держит лента автостраховки."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, sparkle, O

wall = (f'<path d="M22 6 L106 6 L112 128 L16 128Z" fill="#F4E9D8" {s()}/>'
        # швы панелей стены
        '<path d="M19 66 L109 66" stroke="#D9C9B0" stroke-width="2"/><path d="M64 6 L64 128" stroke="#D9C9B0" stroke-width="2"/>')
holds = ''.join(f'<path d="M{x-r} {y} Q{x-r} {y-r} {x} {y-r} Q{x+r*1.1} {y-r*.8} {x+r} {y+r*.2} Q{x} {y+r*1.1} {x-r} {y}Z" fill="{c}" {s("stroke-width=\"2.4\"")}/>'
                for x, y, r, c in [(34, 26, 6, "#3FB4F0"), (92, 40, 6, "#7BD35F"), (30, 92, 6, "#FFC93C"),
                                   (98, 98, 6, "#B07CF0"), (40, 116, 5, "#FF8A3D"), (86, 70, 5, "#FF6B9A")])
top_hold = f'<path d="M58 22 Q60 12 70 13 Q80 15 78 24 Q70 29 58 22Z" fill="#FF4F4F" {s()}/>' + sparkle(86, 14, 5, "#FFD23F")
# лента автостраховки сверху до обвязки
strap = f'<path d="M64 0 L64 22" stroke="#2C2C2C" stroke-width="4"/><path d="M64 22 L62 70" stroke="#FFC400" stroke-width="5" stroke-linecap="round"/>' \
        f'<rect x="58" y="66" width="8" height="8" rx="2" fill="#9AA4B2" {s("stroke-width=\"2\"")}/>'
girl = (
    # ноги (синие лосины), упор в зацепы
    f'<path d="M56 86 Q50 98 40 104" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M56 86 Q50 98 40 104" fill="none" stroke="#2F5BD8" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M70 86 Q80 96 82 108" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M70 86 Q80 96 82 108" fill="none" stroke="#2F5BD8" stroke-width="7" stroke-linecap="round"/>'
    f'<ellipse cx="37" cy="106" rx="7" ry="4.5" fill="#FF4F4F" {s("stroke-width=\"2.4\"")}/>'
    f'<ellipse cx="84" cy="111" rx="7" ry="4.5" fill="#FF4F4F" {s("stroke-width=\"2.4\"")}/>'
    # левая рука вниз к зацепу, правая вверх к красному зацепу
    f'<path d="M54 60 Q42 52 36 30" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M54 60 Q42 52 36 30" fill="none" stroke="#FFD2B0" stroke-width="5.5" stroke-linecap="round"/>'
    f'<path d="M72 60 Q78 40 70 24" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M72 60 Q78 40 70 24" fill="none" stroke="#FFD2B0" stroke-width="5.5" stroke-linecap="round"/>'
    # туловище: красная футболка
    f'<path d="M50 58 Q63 52 76 58 L74 86 Q63 90 52 86Z" fill="#E8352E" {s()}/>'
    # обвязка
    f'<path d="M52 80 Q63 86 74 80" fill="none" stroke="#1F2A44" stroke-width="3.5"/>'
    # голова со спины-полуоборотом: смотрит вверх на зацеп
    f'<circle cx="63" cy="44" r="13" fill="#FFD2B0" {s()}/>'
    f'<path d="M50 42 Q52 29 64 30 Q76 30 77 42 Q70 36 63 37 Q55 37 50 42Z" fill="#8B4A2B" {s("stroke-width=\"2.4\"")}/>'
    f'<path d="M50 40 Q40 38 42 48 Q47 46 50 44Z" fill="#8B4A2B" {s("stroke-width=\"2.2\"")}/>'
    f'<path d="M77 40 Q87 38 85 48 Q80 46 77 44Z" fill="#8B4A2B" {s("stroke-width=\"2.2\"")}/>'
    + eye(58, 45, .8) + eye(68, 45, .8) +
    '<ellipse cx="54" cy="51" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="72" cy="51" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M60 51 Q63 54.5 66 51" fill="none" {s("stroke-width=\"2.2\"")}/>'
)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src", "climb-cska.svg"), "w").write(
    svg("teal", wall + holds + top_hold + strap + girl))
