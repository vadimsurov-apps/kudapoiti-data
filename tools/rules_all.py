"""Полный свод правил одним текстом: CLAUDE.md (ядро) + rules/*.md в порядке таблицы из CLAUDE.md."""
import os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def full():
    core = open(os.path.join(ROOT, "CLAUDE.md"), encoding="utf-8").read()
    names = []
    for n in re.findall(r"`rules/([\w-]+\.md)`", core):
        if n not in names: names.append(n)
    for n in sorted(os.listdir(os.path.join(ROOT, "rules"))):
        if n.endswith(".md") and n not in names: names.append(n)
    return core.rstrip() + "\n\n" + "\n".join(open(os.path.join(ROOT, "rules", n), encoding="utf-8").read().rstrip() + "\n" for n in names)


if __name__ == "__main__":
    print(full())
