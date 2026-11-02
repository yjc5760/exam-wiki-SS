#!/usr/bin/env python3
"""
SS-2021-3 耐震固接－滾支鋼梁之選斷面與塑性極限強度 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2021-3.py [輸出目錄]

重繪依據：題目正本 SS-2021-3-problem.md §4 判讀清單（2026-11-02 已確認）。
只畫考卷給的東西；表一已照錄於題目正本 §2，不重繪。跨度依比例、載重高度示意。單位 cm。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2021-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2021-3-problem.md §4，已確認）；單位 cm
# ══════════════════════════════════════════════════════════
SEG = [600.0, 600.0]      # #3 跨度 600 + 600 = 1200 cm；#4 中間黑點只是尺寸線分段點
SPAN = sum(SEG)
#                           #1 A 固接（與鋼柱彎矩接合）；#2 B 滾支；#5 側撐只在 A、B；#6 均布 w 滿跨


def fig1_problem():
    W, H, sx = 760, 400, 0.5
    cv = Canvas(W, H, sx=sx, ox=(W - SPAN * sx) / 2, oy=190)
    cv.panel("圖三", "A 固接、B 滾支；側向支撐只在 A、B")
    cv.line((0, 0), (SPAN, 0), C["member"], 5, cap="butt")
    cv.support((0, 0), "fixed", -90, size=30)
    cv.support((SPAN, 0), "roller", 0, size=15)
    cv.udl((0, 0), (SPAN, 0), 90, n=15, label="w")
    cv.text((0, 0), "A", 16, C["text"], dx=-14, dy=-34, weight="700")
    cv.text((SPAN, 0), "B", 16, C["text"], dx=20, dy=-34, weight="700")
    x = 0.0
    for s in SEG:
        cv.dim((x, 0), (x + s, 0), f"{s:g} cm", off=78, label_off=16)
        x += s
    cv.dot((SEG[0], 0), 4, fill=C["dim"], stroke=C["dim"], w=1)
    cv.text((SEG[0], 0), "（尺寸分段點，非支承、非側撐）", 12, C["muted"], dy=112)
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2021-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#6；表一已照錄於題目正本 §2",
            note="跨度 1200 cm；跨中黑點只是尺寸線分段點，未支撐長度 L_b = 1200 cm",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把跨中黑點當成側撐（L_b 誤取 600 cm）；B 端讀成鉸支或固接"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
