#!/usr/bin/env python3
"""
SS-2003-3 雙角鋼－WT－柱 斜向受拉接合 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2003-3.py [輸出目錄]

重繪依據：題目正本 SS-2003-3-problem.md §4 判讀清單（2026-11-02 已確認）。
只畫考卷給的東西：拉力斜率 3:4、作用線通過 WT 翼板螺栓群、WT 翼板 2 列 × 4 顆螺栓
與 40／3@75／40 mm 配置。角鋼上的螺栓顆數為㈠所求，圖上不畫顆數。
WT 外形、角鋼長度與螺栓橫向間距考卷未標，僅示意。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2003-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2003-3-problem.md §4，已確認）；單位 mm
# ══════════════════════════════════════════════════════════
RISE, RUN = 3.0, 4.0            # #3 拉力斜率 垂直 3：水平 4，作用線通過 WT 翼板螺栓群
TW_WT, TF_WT = 12.4, 18.9       # #4 WT13.5x470，t_w = 12.4 mm、t_f = 18.9 mm
N_ROW, N_COL = 4, 2             # #5 8 顆 = 2 列 × 4 顆
EDGE, PITCH = 40.0, 75.0        # #5 上下端距 40 mm、垂直間距 3@75 = 225 mm
H_PL = 2 * EDGE + (N_ROW - 1) * PITCH          # WT 翼板高（推得值 305 mm）
YS = [H_PL / 2 - EDGE - k * PITCH for k in range(N_ROW)]
GAGE_SKETCH = 110.0             # 兩列螺栓橫向間距（考卷未標，示意）

PW, PH = 520, 520

_L = (RISE ** 2 + RUN ** 2) ** 0.5
UX, UY = RUN / _L, RISE / _L     # 拉力方向單位向量
NX, NY = -UY, UX


def _along(s, t=0.0):
    return (s * UX + t * NX, s * UY + t * NY)


def side_panel():
    W, H, sx = PW, PH, 0.7
    cv = Canvas(W, H, sx=sx, ox=100, oy=180)
    cv.panel("側視", "雙角鋼長肢背對背夾住 WT 腹板（外形示意）")
    # 柱翼板（斷開線示意）
    cv.polygon([(-30, -200), (0, -200), (0, 200), (-30, 200)], C["border"], C["member"], 1.6)
    cv.text((-15, 200), "W10 柱", 13, C["text"], "middle", dy=-14, weight="700")
    # WT 翼板
    cv.polygon([(0, -H_PL / 2), (TF_WT, -H_PL / 2), (TF_WT, H_PL / 2), (0, H_PL / 2)],
               C["fill_c"], C["member"], 1.6)
    for y in YS:
        cv.line((-8, y), (TF_WT + 8, y), C["member"], 3.4, cap="butt")
    # WT 腹板（外形示意）
    stem = [(TF_WT, H_PL / 2 - 20), _along(330, 55), _along(330, -55), (TF_WT, -H_PL / 2 + 20)]
    cv.polygon(stem, C["fill_c"], C["member"], 1.6)
    # 雙角鋼
    ang = [_along(150, 38), _along(470, 38), _along(470, -38), _along(150, -38)]
    cv.polygon(ang, C["border"], C["member"], 1.8)
    # 作用線（通過翼板螺栓群中心）與水平中心線
    cv.line(_along(0), _along(470), C["load"], 1.4, dash="10 4 2 4")
    cv.line((-60, 0), (260, 0), C["muted"], 1.2, dash="10 4 2 4")
    cv.arrow(_along(470), _along(560), C["load"], 3.0, 11)
    # 斜率三角形
    p0 = _along(530, -60)
    cv.poly([p0, (p0[0] + 80, p0[1]), (p0[0] + 80, p0[1] + 60)], C["text"], 1.4)
    cv.text((p0[0] + 40, p0[1]), "4", 13, C["text"], dy=12)
    cv.text((p0[0] + 80, p0[1] + 30), "3", 13, C["text"], "start", dx=6)
    cv.text(_along(330, -80), "角鋼螺栓一列（顆數為㈠所求）", 12, C["accent"], "start", weight="700")
    cv.text_px(W - 24, H - 74, "WT13.5x470", 13, C["text"], "end", weight="700")
    cv.math_px(W - 24, H - 52, f"t_{{w}} = {TW_WT} mm, t_{{f}} = {TF_WT} mm", 13, C["text"], "end")
    cv.text_px(W - 24, H - 30, "19 mm A325X 螺栓", 12.5, C["muted"], "end")
    return cv


def front_panel():
    W, H, sx = PW, PH, 0.95
    cv = Canvas(W, H, sx=sx, ox=W / 2 - 70, oy=H / 2 - 30)
    cv.panel("WT 翼板與柱接合（正視）", "2 列 × 4 顆；橫向間距示意")
    bw = GAGE_SKETCH + 2 * EDGE
    cv.line((-bw / 2 - 25, -200), (-bw / 2 - 25, 200), C["member"], 1.6)
    cv.line((bw / 2 + 25, -200), (bw / 2 + 25, 200), C["member"], 1.6)
    cv.polygon([(-bw / 2, -H_PL / 2), (bw / 2, -H_PL / 2), (bw / 2, H_PL / 2), (-bw / 2, H_PL / 2)],
               C["fill_c"], C["member"], 1.8)
    cv.line((-TW_WT / 2, -H_PL / 2), (-TW_WT / 2, H_PL / 2), C["member"], 1.4)
    cv.line((TW_WT / 2, -H_PL / 2), (TW_WT / 2, H_PL / 2), C["member"], 1.4)
    for y in YS:
        for x in (-GAGE_SKETCH / 2, GAGE_SKETCH / 2):
            cv.circle((x, y), 9.5, fill="#FFFFFF", stroke=C["member"], w=1.8)
    xr = bw / 2
    cv.dim((xr, YS[0]), (xr, H_PL / 2), f"{EDGE:.0f}mm", off=48, label_off=34)
    cv.dim((xr, YS[-1]), (xr, YS[0]), f"3@{PITCH:.0f}mm={3 * PITCH:.0f}mm", off=48, label_off=72)
    cv.dim((xr, -H_PL / 2), (xr, YS[-1]), f"{EDGE:.0f}mm", off=48, label_off=34)
    cv.text((0, -H_PL / 2), "W10 柱", 13, C["text"], dy=36, weight="700")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    a, b = side_panel(), front_panel()
    compose([a, b], cols=2,
            title="SS-2003-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1、#3–#5；只畫考卷所給條件",
            note="拉力斜率 3:4，作用線通過 WT 翼板 8 顆螺栓的中心",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "拉力斜率讀反（4:3）；WT 翼板螺栓配置與端距讀錯"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    assert H_PL == 305
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
