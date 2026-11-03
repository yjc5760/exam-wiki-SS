#!/usr/bin/env python3
"""
SS-2002-2 A36 簡支梁 W12×65 移動集中載重之容許 P（ASD）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2002-2.py [輸出目錄]

重繪依據：題目正本 SS-2002-2-problem.md §4 判讀清單（待確認）。
圖上每個支承、側撐、載重都對應清單一項；只畫考卷給的東西，不含任何解題結果。
示意部分：P 的位置（移動載重，畫在跨中只是示意）、梁立面高度與載重箭頭長度；
斷面依 W12×65 題給尺寸（d、bf、tf、tw）按比例繪製。
不重繪：無（本題附圖只有梁立面與斷面座標）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2002-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2002-2-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
SPAN = 14.0                 # 題文／附圖 跨長 14 m
LEFT, RIGHT = "pin", "roller"   # #1 左端鉸支、右端滾支
BRACE_N = 4                 # #3 兩端及每 1/4 跨設弱軸側撐
P_AT = 0.5                  # #4 P 為移動載重；跨中位置僅為示意
SW = "97 kg/m"              # #5 自重全跨均佈
#                             #2 工字形直立，繞強軸 x 彎曲
D, BF, TF, TW = 30.3, 30.0, 1.5, 1.0    # 題文 W12×65：d、bf、tf、tw（cm）

PW, PH = 560, 400
SW_, SH_ = PW, PH


def _rect(cv, x0, x1, y0, y1):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], C["fill_c"], C["member"], 1.8)


def beam_panel():
    sx = (PW - 140) / SPAN
    cv = Canvas(PW, PH, sx=sx, ox=70, oy=150)
    cv.panel("梁立面", "左端鉸支、右端滾支；P 位置可移動（示意）")
    cv.line((0, 0), (SPAN, 0), C["member"], 5, cap="butt")
    cv.support((0, 0), LEFT, 0, size=15)
    cv.support((SPAN, 0), RIGHT, 0, size=15)
    # #5 自重（全跨均佈）
    cv.udl((0, 0), (SPAN, 0), 0.9, n=12, color=C["load"], w=1.4)
    cv.text((SPAN, 0.9), f"自重 {SW}（全跨）", 12.5, C["load"], "end", dy=-12)
    # #4 移動集中載重 P
    xp = P_AT * SPAN
    cv.arrow((xp, 3.3), (xp, 0.95), C["load"], 3.0, 11)
    cv.math((xp, 3.3), "P", 17, C["load"], dy=-12, weight="700")
    cv.double_arrow((xp - 1.6, 3.0), (xp + 1.6, 3.0), C["muted"], 1.6, 8)
    cv.text((xp + 1.9, 3.0), "移動", 12.5, C["muted"], "start")
    # #3 側撐：兩端及每 1/4 跨
    for k in range(BRACE_N + 1):
        x = SPAN * k / BRACE_N
        cv.text((x, 0), "×", 20, C["accent"], weight="700", dy=-1)
    cv.text_px(PW / 2, 88, "× 弱軸方向側向支撐：兩端及每 1/4 跨", 12.5, C["accent"])
    cv.line((SPAN * 0.80, -0.15), (SPAN * 0.86, -1.6), C["muted"], 1.2)
    cv.text((SPAN * 0.86, -1.6), "W12×65", 13, C["text"], "start", dx=4, dy=4)
    cv.dim((0, 0), (SPAN, 0), f"{SPAN:.0f} m", off=80, label_off=16)
    return cv


def section_panel():
    sx = 6.0
    cv = Canvas(SW_, SH_, sx=sx, ox=SW_ / 2 - 10, oy=60)
    cv.panel("斷面座標", "W12×65 依比例")
    _rect(cv, -BF / 2, BF / 2, D - TF, D)
    _rect(cv, -BF / 2, BF / 2, 0, TF)
    _rect(cv, -TW / 2, TW / 2, TF, D - TF)
    yc = D / 2
    cv.arrow((0, yc), (0, D + 9), C["text"], 1.6, 9)
    cv.arrow((0, yc), (BF / 2 + 9, yc), C["text"], 1.6, 9)
    cv.math((0, D + 9), "y", 16, C["text"], dy=-12, weight="700")
    cv.math((BF / 2 + 9, yc), "x", 16, C["text"], "start", dx=6, weight="700")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([beam_panel(), section_panel()], cols=2,
            title="SS-2002-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#5；只畫考卷所給條件（跨長、自重、側撐取自題文）",
            note="P 是移動載重，圖上位置只是示意；側撐在兩端與每 1/4 跨，不是只在兩端",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把移動載重固定在圖上位置；漏看每 1/4 跨側撐而以全跨 14 m 當無支長度；兩端支承讀反"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
