#!/usr/bin/env python3
"""
SS-2009-3 H 型鋼斷面之 Mp/My、Vn 與弱軸 λc — 題目附圖重繪腳本

用法：
    python3 gen_SS-2009-3.py [輸出目錄]

重繪依據：題目正本 SS-2009-3-problem.md §4 判讀清單（2026-11-02 已確認）。
考卷原圖為無尺寸線的示意圖；本圖依標示 H 500 × 304 × 15 × 24 按比例繪出並標上各尺寸對應位置
（#1 標示順序 d × b_f × t_w × t_f），不含任何解題結果。圓角不計（#3）。單位 mm。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2009-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2009-3-problem.md §4，已確認）；單位 mm
# ══════════════════════════════════════════════════════════
D, BF, TW, TF = 500.0, 304.0, 15.0, 24.0    # #1 d × b_f × t_w × t_f
#                                             #3 圓角未給，以三塊矩形計


def fig1_problem():
    W, H, sx = 560, 560, 0.72
    cv = Canvas(W, H, sx=sx, ox=W / 2 - 30, oy=H / 2 - 30)
    cv.panel("H 500 × 304 × 15 × 24", "依標示按比例；原圖為無尺寸線示意圖")
    h, b = D / 2, BF / 2
    for x0, x1, y0, y1 in ((-b, b, h - TF, h), (-b, b, -h, -h + TF), (-TW / 2, TW / 2, -h + TF, h - TF)):
        cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], C["fill_c"], C["member"], 1.8)
    cv.dim((-b, h), (b, h), f"b_{{f}} = {BF:g}", off=-24, label_off=-14)
    cv.dim((-b, -h), (-b, h), f"d = {D:g}", off=-30, label_off=-44)
    cv.dim((b, h - TF), (b, h), f"t_{{f}} = {TF:g}", off=26, label_off=44)
    cv.arrow((TW / 2 + 70, 0), (TW / 2, 0), C["dim"], 1.2, 7)
    cv.arrow((-TW / 2 - 40, 0), (-TW / 2, 0), C["dim"], 1.2, 7)
    cv.math((TW / 2 + 70, 0), f"t_{{w}} = {TW:g}", 14, C["dim"], "start", dx=6)
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2009-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#3；單位 mm",
            note="標示順序為 d × b_f × t_w × t_f；翼板厚 24 大於腹板厚 15",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把標示順序讀錯（例如 15 當翼板厚、24 當腹板厚，或 304 當深度）"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
