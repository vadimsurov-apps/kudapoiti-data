"""Просмотр первой секции карточки Яндекс Карт: python3 tools/creative_1114i_card.py <tag> <n> [chars]."""
import glob, sys, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
tag, n = sys.argv[1], sys.argv[2]; lim = int(sys.argv[3]) if len(sys.argv) > 3 else 3000
fs = glob.glob(os.path.join(ROOT, f"auto/pages/*-cc{n}-{tag}c-*.txt"))
if fs:
    T = open(fs[0]).read().split("\n### ")[0]
    print(" | ".join(l.strip() for l in T.splitlines() if l.strip())[:lim])
