"""Сайты центров (робот edu, девятый запуск) → в начало auto/fetch-queue.txt."""
import os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
q = open(os.path.join(R, "auto/fetch-queue.txt")).read(); s = open(os.path.join(R, "tools/edu_1119_sites.txt")).read()
if s.split()[0] not in q: open(os.path.join(R, "auto/fetch-queue.txt"), "w").write(s + q)
