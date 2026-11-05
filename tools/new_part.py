"""Создаёт пустую таблицу робота data/parts/<робот>.xlsx с теми же колонками, что и основная.
python3 tools/new_part.py cafes"""
import os, sys
import openpyxl
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = sys.argv[1]
dst = os.path.join(root, "data", "parts", f"{name}.xlsx")
if os.path.exists(dst): sys.exit(f"уже есть: {dst}")
os.makedirs(os.path.dirname(dst), exist_ok=True)
src = openpyxl.load_workbook(os.path.join(root, "data", "kuda-poiti-mesta.xlsx"))["Места"]
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Места"
for i, c in enumerate(src[1], 1):
    ws.cell(1, i, c.value)
wb.save(dst); print("создано:", dst)
