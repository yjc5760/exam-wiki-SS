#!/usr/bin/env python3
"""
SS-2025-2 三面圍銲疊接受拉桿件之寬度 L — 題目附圖重繪腳本

用法：
    python3 gen_SS-2025-2.py [輸出目錄]

重繪依據：題目正本 SS-2025-2-problem.md §4 判讀清單（2026-11-02 已確認）。
只畫考卷給的東西；L 為待求符號，連接板外形與桿件長度為示意。單位 cm。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2025-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2025-2-problem.md §4，已確認）
# ══════════════════════════════════════════════════════════
L_OV = 3.0          # #2 疊接長＝縱向銲道長 3 cm
L_SYM = 8.0         # #3 桿件寬 L（符號；繪圖用寬度）
#                     #1 三面圍銲：上、下緣各 3 cm，端面一道長 L；#4 桿件厚 2 cm、連接板厚 1 cm


def fig1_problem():
    W, H, sx = 760, 460, 14
    cv = Canvas(W, H, sx=sx, ox=360, oy=H / 2 - 20)
    cv.panel("銲接結合", "連接板外形與桿件長度示意")
    gu = [(0, -6.5), (0, 6.5), (16, 11), (16, -11)]
    cv.polygon(gu, C["border"], C["member"], 1.8)
    h = L_SYM / 2
    cv.polygon([(-14, -h), (L_OV, -h), (L_OV, h), (-14, h)], C["fill_c"], C["member"], 1.8)
    for y in (-h, h):
        cv.line((0, y), (L_OV, y), C["load"], 5, cap="butt")
    cv.line((L_OV, -h), (L_OV, h), C["load"], 5, cap="butt")
    cv.arrow((-14.5, 0), (-19, 0), C["load"], 3.2, 12)
    cv.math((-19, 0), "P", 16, C["load"], "end", dx=-8, weight="700")
    cv.arrow((16.5, 0), (21, 0), C["load"], 3.2, 12)
    cv.math((21, 0), "P", 16, C["load"], "start", dx=8, weight="700")
    cv.text((-7, 0), "受拉桿件（厚 2 cm）", 13, C["text"], weight="700")
    cv.text((10, 5.5), "連接板（厚 1 cm）", 13, C["text"], weight="700")
    cv.dim((0, h), (L_OV, h), f"{L_OV:g} cm", off=-44, label_off=-14)
    cv.dim((L_OV, -h), (L_OV, h), "L", off=34, label_off=14)
    cv.text((L_OV / 2, -h), "三面圍銲（紅）", 12.5, C["load"], dy=22, weight="700")
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2025-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#4；L 為待求",
            note="銲道沿上緣 3 cm、端面 L、下緣 3 cm 三面圍銲；3 cm 為疊接長",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "漏看端面橫向銲道；把 3 cm 當成桿件寬或端距"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
