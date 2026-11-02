#!/usr/bin/env python3
"""
SS-2007-4 兩層不規則構架各柱有效長度係數 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2007-4.py [輸出目錄]

重繪依據：題目正本 SS-2007-4-problem.md §4 判讀清單（2026-11-02 已確認）。
只重繪圖三構架（依比例）；考卷所附對位圖（Sidesway Uninhibited）屬設計圖表，不重繪。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2007-4"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2007-4-problem.md §4，已確認）；單位 m
# ══════════════════════════════════════════════════════════
SPAN_AB, SPAN_BC = 6.0, 10.0       # #2 A-B 6 m、B-C 10 m
H1, H2 = 4.0, 3.0                  # #3 一層 4 m、二層 3 m
SUPPORT = {"A": "pin", "B": "fixed", "C": "fixed"}     # #1 A 鉸接、B、C 固接
XA, XB, XC = 0.0, SPAN_AB, SPAN_AB + SPAN_BC
NODES = {"A": (XA, 0), "B": (XB, 0), "C": (XC, 0),
         "D": (XA, H1), "E": (XB, H1), "F": (XC, H1),
         "G": (XB, H1 + H2), "H": (XC, H1 + H2)}       # #4 二層只在 B-C 跨上方
MEMBERS = ["AD", "BE", "CF", "EG", "FH", "DE", "EF", "GH"]
LABEL_DIR = {"A": (-22, -6), "B": (26, -10), "C": (-26, -10), "D": (-16, -14), "E": (-14, -14),
             "F": (16, -14), "G": (-14, -14), "H": (16, -14)}


def fig1_problem():
    W, H, sx = 760, 470, 30
    cv = Canvas(W, H, sx=sx, ox=130, oy=110)
    cv.panel("圖三　構架", "依比例；側移未束制")
    for m in MEMBERS:
        cv.line(NODES[m[0]], NODES[m[1]], C["member"], 4.2, cap="butt")
    for n, kind in SUPPORT.items():
        cv.support(NODES[n], kind, 0, size=16 if kind == "pin" else 20)
    for n, (dx, dy) in LABEL_DIR.items():
        cv.text(NODES[n], n, 16, C["text"], "middle", dx=dx, dy=dy, weight="700")
    cv.text((XA, 0), "hinge", 13, C["muted"], dy=46)
    cv.text((XB, 0), "Fixed", 13, C["muted"], dy=46)
    cv.text((XC, 0), "Fixed", 13, C["muted"], dy=46)
    cv.dim((XA, 0), (XB, 0), f"{SPAN_AB:g} m", off=70, label_off=16)
    cv.dim((XB, 0), (XC, 0), f"{SPAN_BC:g} m", off=70, label_off=16)
    cv.dim((XC, 0), (XC, H1), f"{H1:g} m", off=50, label_off=26)
    cv.dim((XC, H1), (XC, H1 + H2), f"{H2:g} m", off=50, label_off=26)
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2007-4 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#4；對位圖為設計圖表，不重繪",
            note="二層只在 B-C 跨上方（柱 EG、FH，梁 GH）；D 上方無柱",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "A 端讀成固接；D 上方多畫一根柱；跨度 6／10 m 對調"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
