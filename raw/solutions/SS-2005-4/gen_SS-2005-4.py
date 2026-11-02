#!/usr/bin/env python3
"""
SS-2005-4 固接－簡支 T 型鋼梁塑性設計 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2005-4.py [輸出目錄]

重繪依據：題目正本 SS-2005-4-problem.md §4 判讀清單（2026-11-02 已確認）。
圖上每個支承、尺寸、載重都對應清單一項；只畫考卷給的東西，不含任何解題結果。
斷面依比例繪製；梁立面跨度與載重高度為示意比例。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2005-4"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2005-4-problem.md §4，已確認）
# ══════════════════════════════════════════════════════════
SPAN = 600.0        # #1 跨度 600 cm
LEFT = "fixed"      # #2 左端固接
RIGHT = "pin"       # #3 右端鉸支（簡支）
#                     #4 均布 w_u，向下，滿跨
BF, TF = 40.0, 2.6  # #6 翼板寬 40 cm、#7 翼板厚 2.6 cm
D = 24.0            # #8 全深 24 cm（翼板頂至腹板底）
TW = 2.4            # #9 腹板厚 2.4 cm
#                     #5 T 型，翼板在上、腹板向下
HW = D - TF         # 腹板淨高（推得值 21.4 cm）

PW, PH = 520, 380


def _rect(cv, x0, x1, y0, y1):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], C["fill_c"], C["member"], 1.8)


def beam_panel():
    sx = (PW - 150) / SPAN
    cv = Canvas(PW, PH, sx=sx, ox=80, oy=170)
    cv.panel("梁立面", "左端固接、右端簡支（跨度示意）")
    cv.line((0, 0), (SPAN, 0), C["member"], 5, cap="butt")
    cv.support((0, 0), LEFT, -90, size=26)   # 牆在左側（剖線朝外）
    cv.support((SPAN, 0), RIGHT, 0, size=16)
    cv.dot((SPAN, 0), 5.5, fill="#FFFFFF", stroke=C["member"], w=2.2)
    cv.udl((0, 0), (SPAN, 0), 0.11 * SPAN, n=11, label="w_{u}")
    cv.dim((0, 0), (SPAN, 0), f"{SPAN:.0f} cm", off=70, label_off=16)
    return cv


def section_panel():
    sx = 7.2
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2, oy=78)
    cv.panel("鋼梁斷面", "依比例；全深量至腹板底")
    _rect(cv, -BF / 2, BF / 2, D - TF, D)          # 翼板
    _rect(cv, -TW / 2, TW / 2, 0, D - TF)          # 腹板
    cv.dim((-BF / 2, D), (BF / 2, D), f"{BF:.0f} cm", off=-26, label_off=-14)
    cv.dim((BF / 2, D - TF), (BF / 2, D), f"{TF} cm", off=26, label_off=30)
    cv.dim((-TW / 2, 0), (-TW / 2, D), f"{D:.0f} cm", off=-(BF / 2 - TW / 2) * sx - 30,
           label_off=-30, color=C["accent"])
    cv.dim((-TW / 2, 0), (TW / 2, 0), f"{TW} cm", off=26, label_off=16)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([beam_panel(), section_panel()], cols=2,
            title="SS-2005-4 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#9；只畫考卷所給條件",
            note="24 cm 為全深（翼板頂至腹板底），腹板淨高 21.4 cm 為推得值",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把 24 cm 讀成腹板高（全深變 26.6 cm）；右端當成固定端"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    assert abs(HW - 21.4) < 1e-9
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
