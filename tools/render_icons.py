"""Рендерит SVG-иконки новых мест в icons/<id>.png (192×192) и обновляет icons/index.json.
Запуск из корня репозитория:  python3 tools/render_icons.py id1 id2 ...
Иконки первых 691 места встроены в приложение — их сюда класть не нужно."""
import json, os, sys
import cairosvg

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for pid in sys.argv[1:]:
    src = os.path.join(root, "icons-src", f"{pid}.svg")
    cairosvg.svg2png(url=src, write_to=os.path.join(root, "icons", f"{pid}.png"), output_width=192, output_height=192)
ids = sorted(f[:-4] for f in os.listdir(os.path.join(root, "icons")) if f.endswith(".png"))
json.dump(ids, open(os.path.join(root, "icons", "index.json"), "w"))
# версии: хэш картинки — если иконку перерисовали, приложение скачает её заново
import hashlib
ver = {i: hashlib.md5(open(os.path.join(root, "icons", i + ".png"), "rb").read()).hexdigest()[:8] for i in ids}
json.dump(ver, open(os.path.join(root, "icons", "versions.json"), "w"), indent=0)
print("иконок на GitHub:", len(ids))
