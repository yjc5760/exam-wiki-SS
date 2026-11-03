#!/usr/bin/env python3
"""
SS-2002-4 托架板偏心螺栓接合（ASD 彈性法）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2002-4.py [輸出目錄]

重繪依據：題目正本 SS-2002-4-problem.md §4 判讀清單（待確認）。
圖上只畫考卷給的東西：螺栓配置、5／7／21／25 cm 尺寸、P 的作用點與 3:4 斜率，不含任何解題結果。
螺栓群與 25 cm 依比例；鋼板左緣（與翼板左緣齊）、右下斜切的轉折位置、柱的上下延伸長度為示意（考卷未標）。
附表（容許應力、承壓公式）已照錄於題目正本 §2，不重繪。
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2002-4"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2002-4-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
G = 7.0             # #2 行距 7 cm（兩行分居腹板兩側）
S = 7.0             # #2 列距 7 cm（3@7 cm = 21 cm）
NROW = 4            # #2 2 行 × 4 列 = 8 顆
EDGE = 5.0          # #4 鋼板上、下緣至最外列螺栓 5 cm
A25 = 25.0          # #3 右側螺栓行至鋼板右緣 25 cm（P 作用點水平位置）
PV, PH = 4.0, 3.0   # #5 P 向左下，垂直 4：水平 3，作用於鋼板右上角
DB = 2.2            # 題文 螺栓標稱直徑 22 mm
BF, TW = 15.44, 0.813   # §2 W6×25：bf、tw（#1 翼板面向讀者，虛線為腹板）
# 示意（考卷未標）：鋼板左緣取翼板左緣；右緣垂直段約占板高 40%
CHAMF = 0.40
COL_EXT = 12.0      # 柱在鋼板上下各延伸（示意）

X_R = G / 2 + A25                      # 鋼板右緣
Y_T = (NROW - 1) * S + EDGE            # 鋼板上緣（原點：最下列螺栓、腹板中心）
Y_B = -EDGE
H_PL = Y_T - Y_B

PW, PHT = 860, 700


def _wave(cv, x0, x1, y, amp=0.9, n=40):
    pts = [(x0 + (x1 - x0) * i / n, y + amp * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]
    cv.poly(pts, C["member"], 1.8)


def panel():
    sx = 9.0
    cv = Canvas(PW, PHT, sx=sx, ox=330, oy=210)
    cv.panel("托架板螺栓接合立面", "W6×25 翼板面向讀者；鋼板厚 15 mm")
    xl, xr = -BF / 2, BF / 2
    # 柱（翼板外框）：鋼板以外的可見部分
    top, bot = Y_T + COL_EXT, Y_B - COL_EXT
    cv.line((xl, Y_T), (xl, top), C["member"], 2.2)
    cv.line((xr, Y_T), (xr, top), C["member"], 2.2)
    cv.line((xl, Y_B), (xl, bot), C["member"], 2.2)
    cv.line((xr, Y_B), (xr, bot), C["member"], 2.2)
    _wave(cv, xl, xr, top)
    _wave(cv, xl, xr, bot)
    for sg in (-1, 1):                                   # 腹板（虛線）
        cv.line((sg * TW / 2, Y_T), (sg * TW / 2, top - 1.5), C["member"], 1.4, dash="5 4")
        cv.line((sg * TW / 2, Y_B), (sg * TW / 2, bot + 1.5), C["member"], 1.4, dash="5 4")
    # 鋼板
    y_k = Y_T - CHAMF * H_PL
    plate = [(xl, Y_B), (xr, Y_B), (X_R, y_k), (X_R, Y_T), (xl, Y_T)]
    cv.polygon(plate, C["fill_c"], C["member"], 2.2)
    # 螺栓
    for j in range(NROW):
        for sg in (-1, 1):
            cv.circle((sg * G / 2, j * S), DB / 2, "#FFFFFF", C["member"], 1.8)
    # 尺寸：左側 5／3@7=21／5
    xd = xl
    for ya, yb_, lab, lo in ((Y_T, (NROW - 1) * S, f"{EDGE:.0f} cm", 30),
                             ((NROW - 1) * S, 0, f"3@{S:.0f} cm = {(NROW - 1) * S:.0f} cm", 66),
                             (0, Y_B, f"{EDGE:.0f} cm", 30)):
        cv.dim((xd, ya), (xd, yb_), lab, off=48, label_off=lo)
    for yy in ((NROW - 1) * S, 0):                       # 延伸線拉到螺栓中心
        cv.line((xd, yy), (-G / 2, yy), C["dim"], 1, dash="3 3")
    # 尺寸：下方 7 cm、25 cm
    yb = Y_B - 5.0
    cv.line((-G / 2, 0), (-G / 2, yb - 0.6), C["dim"], 1, dash="3 3")
    cv.line((G / 2, 0), (G / 2, yb - 0.6), C["dim"], 1, dash="3 3")
    cv.line((X_R, y_k), (X_R, yb - 0.6), C["dim"], 1, dash="3 3")
    cv.dim((-G / 2, yb), (G / 2, yb), f"{G:.0f} cm", label_off=17)
    cv.dim((G / 2, yb), (X_R, yb), f"{A25:.0f} cm", label_off=17)
    lx, ly = cv.P((0, yb))
    cv.rect_px(lx - 17, ly + 8, 34, 18, C["panel"], rx=3)   # 讓腹板虛線不穿過標字
    cv.math_px(lx, ly + 17, f"{G:.0f} cm", 14, C["dim"])
    # P：鋼板右上角，向左下 3:4
    k = 2.6
    tail = (X_R + PH * k, Y_T + PV * k)
    cv.arrow(tail, (X_R, Y_T), C["load"], 3.2, 12)
    cv.text(tail, "P = 20 tonf", 15, C["load"], "start", dx=6, dy=-10, weight="700")
    s = 0.75                                              # 斜率三角形（貼在箭線右側）
    t0 = (X_R + PH * 1.0 + 1.2, Y_T + PV * 1.0)
    t1 = (t0[0] + PH * s * 2, t0[1] + PV * s * 2)
    cn = (t1[0], t0[1])
    cv.poly([t0, cn, t1], C["load"], 1.4)
    cv.text(((t0[0] + cn[0]) / 2, t0[1]), "3", 13, C["load"], dy=11)
    cv.text((cn[0], (cn[1] + t1[1]) / 2), "4", 13, C["load"], "start", dx=6)
    # 文字標註
    lp = (X_R - 3, y_k + 2)
    cv.line(lp, (X_R + 6, y_k - 3), C["muted"], 1.1)
    cv.text((X_R + 6, y_k - 3), "厚度 15 mm 之鋼板", 13.5, C["text"], "start", dx=4)
    lc = (xr - 2, bot + 4)
    cv.line(lc, (xr + 10, bot + 2), C["muted"], 1.1)
    cv.text((xr + 10, bot + 2), "W6×25 型鋼", 13.5, C["text"], "start", dx=4)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([panel()], cols=1,
            title="SS-2002-4 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#5；螺栓群與 25 cm 依比例，鋼板外形與柱長為示意",
            note="25 cm 由右側螺栓行量到鋼板右緣（P 作用點），不是由腹板中心或左行量起",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "25 cm 起點讀成腹板中心或左行（偏心差 3.5 或 7 cm）；P 斜率 3:4 讀反成水平 4、垂直 3"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
