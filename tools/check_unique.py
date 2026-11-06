"""Проверка АБСОЛЮТНОЙ уникальности иконок (правило Вадима 07.11: никаких повторов — ни героя, ни сцены,
ни компоновки, ни размера/позы, ни цветового решения).

1) Реестр icons-src/subjects.txt, новый формат строки:  id — герой: <кто/что> | сцена: <что делает и где>
   Герой и сцена должны быть уникальны во всём реестре (сравнение без регистра и ё/е).
2) Картинки: все иконки (icons/*.png и встроенные p/img/*.png) сравниваются попарно по уменьшенной копии 24×24
   (цвет + компоновка). Слишком похожие пары = повтор, даже если герои разные.

python3 tools/check_unique.py            — отчёт по всем
python3 tools/check_unique.py id1 id2 …  — проверить только эти иконки против всех (для роботов перед коммитом)
Код выхода 1, если у проверяемых есть повторы."""
import json, os, re, sys
import numpy as np
from PIL import Image
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
THRESH = 0.06    # средняя разница цвета пикселя 24×24 (0..1); меньше — «та же картинка» (подобрано на примерах 07.11)


def norm(s):
    return re.sub(r"\s+", " ", s.lower().replace("ё", "е")).strip(" .,;")


def registry():
    heroes, scenes, old = {}, {}, 0
    for line in open(os.path.join(ROOT, "icons-src", "subjects.txt"), encoding="utf-8"):
        if " — " not in line:
            continue
        pid, subj = line.rstrip("\n").split(" — ", 1)
        m = re.match(r"\s*герой:\s*(.+?)\s*\|\s*сцена:\s*(.+)$", subj)
        if not m:
            old += 1
            continue
        heroes.setdefault(norm(m.group(1)), []).append(pid)
        scenes.setdefault(norm(m.group(2)), []).append(pid)
    return heroes, scenes, old


def vectors(ids):
    vec = {}
    for pid in ids:
        for path in (f"icons/{pid}.png", f"p/img/{pid}.png"):
            p = os.path.join(ROOT, path)
            if os.path.exists(p):
                im = Image.open(p).convert("RGBA").resize((24, 24), Image.LANCZOS)
                a = np.asarray(im, dtype=np.float32) / 255.0
                vec[pid] = (a[..., :3] * a[..., 3:4]).reshape(-1)
                break
    return vec


def main():
    places = [p["id"] for p in json.load(open(os.path.join(ROOT, "places.json")))["places"]]
    check = sys.argv[1:] or places
    heroes, scenes, old = registry()
    bad = set()
    dup_h = {k: v for k, v in heroes.items() if len(v) > 1 and set(v) & set(check)}
    dup_s = {k: v for k, v in scenes.items() if len(v) > 1 and set(v) & set(check)}
    for k, v in list(dup_h.items())[:40]:
        print(f"ГЕРОЙ повторяется «{k}»: {', '.join(v)}")
    for k, v in list(dup_s.items())[:40]:
        print(f"СЦЕНА повторяется «{k}»: {', '.join(v)}")
    for v in list(dup_h.values()) + list(dup_s.values()):
        bad |= set(v) & set(check)
    vec = vectors(places)
    ids = [i for i in places if i in vec]
    M = np.stack([vec[i] for i in ids])
    idx = {i: n for n, i in enumerate(ids)}
    pairs = []
    for pid in check:
        if pid not in idx:
            continue
        d = np.abs(M - M[idx[pid]]).mean(axis=1)
        for j in np.where(d < THRESH)[0]:
            if ids[j] != pid and (ids[j] not in check or ids[j] > pid):
                pairs.append((float(d[j]), pid, ids[j]))
    pairs.sort()
    for d, a, b in pairs[:60]:
        print(f"ПОХОЖИ картинки ({d:.3f}): {a} ~ {b}")
    bad |= {a for _, a, _ in pairs} | {b for _, _, b in pairs if b in check}
    print(f"\nпроверено {len(check)}; повторов: героев {len(dup_h)}, сцен {len(dup_s)}, похожих пар картинок {len(pairs)}; "
          f"иконок с повтором: {len(bad)}; строк реестра в старом формате (без «герой: | сцена:»): {old}")
    json.dump(sorted(bad), open(os.path.join(ROOT, "auto", "icon-repeats.json"), "w"), ensure_ascii=False, indent=0)
    sys.exit(1 if bad and sys.argv[1:] else 0)


if __name__ == "__main__":
    main()
