#!/usr/bin/env python3
"""
SS-2024-2 圓管與十字形連接板之縱向填角銲接頭 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2024-2.py [輸出目錄]

重繪依據：題目正本 SS-2024-2-problem.md §4 判讀清單（2026-11-02 已確認）。
只畫考卷給的東西；銲腳尺寸為㈡所求，不標數值。附圖內的填角銲最小尺寸表已照錄於題目正本 §2，不重繪。
斷面依比例；側視圖連接板外形與管長為示意。單位 mm。
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2024-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2024-2-problem.md §4，已確認）；單位 mm
# ══════════════════════════════════════════════════════════
D = 273.0                 # 題文 D = 273
T_PIPE = 10.0             # #4 管壁厚 10（STK273×10）
T_G = 20.0                # 題文 t_g = 20
N_WELD = 8                # #1 十字板四支 × 管外兩側 = 8 道
L_W = D                   # #2 每道 L = D
SLOT = 22.0               # #3 槽端半圓孔徑 22，槽端在銲道區之外
ARM = 165.0               # 十字板伸出長度（示意）
LEG = 18.0                # 銲道三角形大小（示意；銲腳為㈡所求）


def section_panel():
    W, H, sx = 460, 480, 0.9
    cv = Canvas(W, H, sx=sx, ox=W / 2, oy=H / 2 - 30)
    cv.panel("斷面", "依比例；黑色三角形為填角銲（8 道）")
    R = D / 2
    cv.circle((0, 0), R, fill=C["fill_c"], stroke=C["member"], w=1.8)
    cv.circle((0, 0), R - T_PIPE, fill=C["panel"], stroke=C["member"], w=1.8)
    for ang in (0, 90):
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a)
        nx, ny = -uy, ux
        p = [(-ARM * ux + T_G / 2 * nx, -ARM * uy + T_G / 2 * ny), (ARM * ux + T_G / 2 * nx, ARM * uy + T_G / 2 * ny),
             (ARM * ux - T_G / 2 * nx, ARM * uy - T_G / 2 * ny), (-ARM * ux - T_G / 2 * nx, -ARM * uy - T_G / 2 * ny)]
        cv.polygon(p, C["border"], C["member"], 1.6)
    k = 0
    for ang in (0, 90, 180, 270):
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a)
        nx, ny = -uy, ux
        for s in (1, -1):
            bx, by = R * ux + s * T_G / 2 * nx, R * uy + s * T_G / 2 * ny
            tri = [(bx, by), (bx + LEG * ux, by + LEG * uy), (bx + s * LEG * nx, by + s * LEG * ny)]
            cv.polygon(tri, C["text"], C["text"], 1)
            k += 1
    assert k == N_WELD
    cv.dim((-R, R), (R, R), "D", off=-60, label_off=-14)
    cv.arrow((-40, -60), (-T_G / 2, -60), C["dim"], 1.2, 7)
    cv.arrow((40, -60), (T_G / 2, -60), C["dim"], 1.2, 7)
    cv.math((40, -60), "t_{g}", 14, C["dim"], "start", dx=6)
    cv.text_px(W / 2, H - 30, "STK273×10", 13, C["muted"])
    return cv


def side_panel():
    W, H, sx = 460, 480, 0.72
    cv = Canvas(W, H, sx=sx, ox=100, oy=H / 2 - 20)
    cv.panel("側視", "連接板插入管端開槽；粗黑線為銲道")
    R = D / 2
    cv.polygon([(-90, -R - 30), (L_W + SLOT, -R - 30), (L_W + SLOT, R + 30), (-90, R + 30)],
               C["border"], C["member"], 1.4)
    for y in (-R, R):
        cv.line((0, y), (L_W + 130, y), C["member"], 1.8)
    for y in (-R, R):
        cv.line((L_W + SLOT / 2, y), (L_W + 130, y), C["muted"], 1.0, dash="5 4")
    for y in (-R + 6, -T_G / 2 - 6, T_G / 2 + 6, R - 6):
        cv.line((0, y), (L_W, y), C["text"], 8, cap="butt")
    cv.circle((L_W + SLOT / 2, 0), SLOT / 2, stroke=C["member"], w=1.4)
    cv.dim((0, R + 30), (L_W, R + 30), "L = D", off=-22, label_off=-14)
    cv.text((L_W + SLOT / 2, 0), "半圓孔徑 = 22mm", 12.5, C["accent"], "middle", dy=-28, weight="700")
    cv.text((-45, 0), "十字形連接板", 12.5, C["text"], dy=-60, weight="700")
    cv.text((L_W + 80, -R), "圓管", 13, C["text"], dy=-16, weight="700")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([section_panel(), side_panel()], cols=2,
            title="SS-2024-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#4；填角銲最小尺寸表已照錄於題目正本 §2",
            note="十字板四支、每支管外兩側各一道，共 8 道；每道長 L = D = 273 mm；槽端在銲道區之外",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "銲道數算成 4 道；銲長不等於 D；把開槽當成在銲道區內"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
