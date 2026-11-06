"""Перерисовка 3 падел-академий (06.11, замечание Вадима: йо-йо, ходули, мешок не подходят).
Сюжеты: падел-корт сверху со стеклянными стенами, кроссовок для падела, кубок турнира по паделу."""
import os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
I = {
    "a-padel-khodynka": ("blue",
        f'<rect x="26" y="18" width="76" height="92" rx="6" fill="#3E9BE0" {s()}/>'
        f'<rect x="26" y="18" width="76" height="92" rx="6" fill="none" stroke="#DFF3FF" stroke-width="7" opacity=".85"/>'
        f'<rect x="26" y="18" width="76" height="92" rx="6" fill="none" {W(3)}/>'
        f'<path d="M26 64 H102" stroke="#fff" stroke-width="4"/><path d="M26 64 H102" {W(1.6)} stroke-dasharray="3 3"/>'
        f'<path d="M64 30 V52 M64 76 V98 M36 42 H92 M36 86 H92" stroke="#fff" stroke-width="2.6"/>'
        + f'<circle cx="80" cy="50" r="7" fill="#D7F25A" {W(2.4)}/>' + face(80, 50, d=2.6, k=0.25, blush=False)
        + sparkle(112, 24, 6)),
    "padlhub-yasenevo": ("orange",
        f'<path d="M18 86 Q18 60 40 56 L60 52 Q70 38 84 44 L100 66 Q112 70 112 84 V92 H18Z" fill="#fff" {s()}/>'
        f'<path d="M18 92 H112 V100 Q112 106 106 106 H24 Q18 106 18 100Z" fill="#5CB7F2" {W(3)}/>'
        f'<path d="M52 56 L60 72 M62 52 L70 68 M72 48 L80 64" {W(2.6)}/>'
        f'<path d="M86 70 Q96 74 104 74" fill="none" stroke="#FF8A3D" stroke-width="5" stroke-linecap="round"/>'
        + face(40, 74, d=6, k=0.5) + sparkle(30, 30, 6) + sparkle(104, 28, 5)),
    "padlhub-terekhovo": ("yellow",
        f'<path d="M36 22 H92 V52 Q92 78 64 80 Q36 78 36 52Z" fill="#FFC93C" {s()}/>'
        f'<path d="M36 30 Q16 30 18 46 Q20 60 38 60 M92 30 Q112 30 110 46 Q108 60 90 60" fill="none" {W(4)}/>'
        f'<path d="M58 80 H70 V94 H58Z" fill="#E0A830" {W(3)}/><path d="M40 94 H88 V108 H40Z" fill="#8A5530" {W(3)}/>'
        f'<rect x="54" y="30" width="20" height="24" rx="9" fill="#fff" {W(2.4)}/><path d="M64 54 V66" {W(4)}/>'
        f'<circle cx="60" cy="38" r="1.8" fill="{O}"/><circle cx="68" cy="38" r="1.8" fill="{O}"/><circle cx="64" cy="46" r="1.8" fill="{O}"/>'
        + sparkle(22, 20, 6) + sparkle(108, 90, 5)),
}
for pid, (bg, body) in I.items():
    open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
print(len(I))
