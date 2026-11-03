#!/usr/bin/env python3
"""
SS-2008-3 簡支 H 型鋼梁（兩端局部均佈、四點側撐）LRFD 容許標稱載重 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2008-3.py [輸出目錄]

重繪依據：題目正本 SS-2008-3-problem.md §4 判讀清單（待確認）。
圖上每個支承、載重範圍、側撐都對應清單一項；只畫考卷給的東西，不含任何解題結果
（不畫彎矩圖、不標 Cb、Lb 判定）。
立面與平面的跨度依比例（L = 18 m 三等分）；載重箭頭高度、梁線寬為示意；
右側斷面依題給 d、bf、tf、tw 按比例放大繪製（只表達座標方位）。
不重繪：第 3–4 頁參考公式（已照錄於 problem.md §2）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2008-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2008-3-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
L = 18.0                        # 題文 L = 18 m
NSEG = 3                        # 圖 2：三等分 L/3
SUP_A, SUP_D = "roller", "pin"  # #1 A 滾支、D 鉸支
LOADED = (0, 2)                 # #2 w 只在 AB（第 0 段）、CD（第 2 段）；BC 無載重
BRACED = ("A", "B", "C", "D")   # #3 四點兩側側撐
#                                 #4 繞強軸 x，y 向下為載重方向
D, BF, TF, TW = 54.43, 21.22, 2.12, 1.31   # 題文斷面尺寸（cm），僅畫斷面方位

PW, PH = 820, 320
SEG = L / NSEG
NAMES = ["A", "B", "C", "D"]


def _sec(cv, x0, y0, k):
    """在 (x0, y0)（模型單位 m）畫 I 斷面，k = 每 cm 對應的模型長度；回傳半寬、半高"""
    bf, d = BF * k, D * k
    for xa, xb, ya, yb in ((-BF / 2, BF / 2, D / 2 - TF, D / 2), (-BF / 2, BF / 2, -D / 2, -D / 2 + TF),
                           (-TW / 2, TW / 2, -D / 2 + TF, D / 2 - TF)):
        cv.polygon([(x0 + xa * k, y0 + ya * k), (x0 + xb * k, y0 + ya * k),
                    (x0 + xb * k, y0 + yb * k), (x0 + xa * k, y0 + yb * k)],
                   C["fill_c"], C["member"], 1.4)
    return bf / 2, d / 2


def elev_panel():
    sx = 32.0
    cv = Canvas(PW, PH, sx=sx, ox=70, oy=140)
    cv.panel("立面", "A 滾支、D 鉸支；w 只作用於 AB、CD 兩段（BC 無載重）")
    cv.line((0, 0), (L, 0), C["member"], 4.5, cap="butt")
    cv.support((0, 0), SUP_A, 0, size=13)
    cv.support((L, 0), SUP_D, 0, size=13)
    for k in LOADED:
        x0, x1 = k * SEG, (k + 1) * SEG
        cv.udl((x0, 0), (x1, 0), 1.6, n=7, label="w")
    for j, nm in enumerate(NAMES):
        x = j * SEG
        dx = -20 if j == 0 else (24 if j == NSEG else 12)
        dy = -12 if j == 0 else (26 if j == NSEG else 18)
        cv.text((x, 0), nm, 15, C["text"], "end" if j == 0 else "start", dx=dx, dy=dy,
                weight="700")
        if 0 < j < NSEG:
            cv.line((x, -0.15), (x, 0.15), C["member"], 2)
    for k in range(NSEG):
        cv.dim((k * SEG, 0), ((k + 1) * SEG, 0), "L/3", off=58, label_off=14)
    cv.text_px(cv.X(L / 2), cv.Y(0) + 96, f"L = {L:.0f} m（題文）", 13, C["muted"])
    # 座標：z 向右、y 向下
    cv.arrow((L + 0.25, 0), (L + 1.6, 0), C["text"], 1.6, 8)
    cv.math((L + 1.6, 0), "z", 15, C["text"], "start", dx=6)
    cv.arrow((-1.1, -0.5), (-1.1, -2.4), C["text"], 1.6, 8)
    cv.math((-1.1, -2.4), "y", 15, C["text"], "end", dx=-6, dy=4)
    # 斷面方位（x 向左、y 向下）
    sx0, sy0 = L + 3.6, 1.3
    hb, hd = _sec(cv, sx0, sy0, 0.040)
    cv.arrow((sx0, sy0), (sx0 - hb - 1.0, sy0), C["text"], 1.6, 8)
    cv.math((sx0 - hb - 1.0, sy0), "x", 15, C["text"], "end", dx=-6)
    cv.arrow((sx0, sy0), (sx0, sy0 - hd - 0.9), C["text"], 1.6, 8)
    cv.math((sx0, sy0 - hd - 0.9), "y", 15, C["text"], dy=14)
    return cv


def plan_panel():
    sx = 32.0
    cv = Canvas(PW, PH, sx=sx, ox=70, oy=140)
    cv.panel("平面（側撐補強）", "A、B、C、D 四點兩側皆有側撐")
    cv.line((0, 0), (L, 0), C["member"], 4.5, cap="butt")
    for j, nm in enumerate(NAMES):
        x = j * SEG
        if nm in BRACED:
            cv.support((x, 0), "roller", 0, size=11)
            cv.support((x, 0), "roller", 180, size=11)
        cv.text((x, 0), nm, 15, C["text"], dy=-52, weight="700")
    cv.arrow((L + 0.6, 0), (L + 2.0, 0), C["text"], 1.6, 8)
    cv.math((L + 2.0, 0), "z", 15, C["text"], "start", dx=6)
    cv.arrow((-1.1, -0.3), (-1.1, -2.2), C["text"], 1.6, 8)
    cv.math((-1.1, -2.2), "x", 15, C["text"], "end", dx=-6, dy=4)
    cv.text((L, 0), "（側撐補強）", 13, C["muted"], "end", dy=60)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([elev_panel(), plan_panel()], cols=1,
            title="SS-2008-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#4；只畫考卷所給條件（圖 2）",
            note="w 只在兩端各 L/3（AB、CD），中段 BC 無載重；四點側撐把梁分成三段 L/3",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把「兩側」讀成全跨均佈（BC 也有 w）；側撐只看兩端而以 L 當無支長度；A、D 支承讀反"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
