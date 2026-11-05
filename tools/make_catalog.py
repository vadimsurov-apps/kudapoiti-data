"""Каталог всех иконок: icons-catalog/sheet-NN.png (по 80 штук, с подписями id).
Перед рисованием новых иконок ОБЯЗАТЕЛЬНО просмотреть все листы (Read), чтобы не повторить сюжет.
Запуск из корня: python3 tools/make_catalog.py"""
import io, os
import cairosvg
from PIL import Image, ImageDraw

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = sorted(f[:-4] for f in os.listdir(os.path.join(root, "icons-src")) if f.endswith(".svg"))
out = os.path.join(root, "icons-catalog"); os.makedirs(out, exist_ok=True)
for f in os.listdir(out): os.remove(os.path.join(out, f))
N, C, S = 80, 10, 120
for k in range(0, len(ids), N):
    part = ids[k:k + N]
    sheet = Image.new("RGB", (C * S, ((len(part) + C - 1) // C) * (S + 14)), "white"); d = ImageDraw.Draw(sheet)
    for i, pid in enumerate(part):
        png = cairosvg.svg2png(url=os.path.join(root, "icons-src", pid + ".svg"), output_width=S - 8, output_height=S - 8)
        im = Image.open(io.BytesIO(png)).convert("RGBA"); x, y = (i % C) * S, (i // C) * (S + 14)
        sheet.paste(im, (x + 4, y + 2), im); d.text((x + 2, y + S - 4), pid[:20], fill="black")
    sheet.save(os.path.join(out, f"sheet-{k // N + 1:02d}.png"), optimize=True)
print("иконок:", len(ids), "листов:", (len(ids) + N - 1) // N)
