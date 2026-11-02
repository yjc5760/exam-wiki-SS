#!/usr/bin/env python3
"""
SS-2020-2 滾支－固定端非對稱 I 型鋼梁塑性分析 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2020-2.py [輸出目錄]

重繪依據：題目正本 SS-2020-2-problem.md §4 判讀清單（2026-11-02 已確認）。
圖上每個支承、尺寸、載重都對應清單一項；只畫考卷給的東西，不含任何解題結果。
斷面依比例繪製；梁立面跨度與載重高度為示意比例。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2020-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2020-2-problem.md §4，已確認）
# ══════════════════════════════════════════════════════════
SPAN = 8.0                # #1 跨度 8 m
A_KIND = "roller"         # #2 A 端滾支（左）
B_KIND = "fixed"          # #3 B 端固定端（右）
#                           #4 均佈 w_u，向下，滿跨
BT, TT = 300.0, 25.0      # #5 上翼板寬 300、厚 25 mm
BB, TB = 200.0, 25.0      # #6 下翼板寬 200、厚 25 mm
TW = 15.0                 # #7 腹板厚 15 mm
D = 600.0                 # #8 全深 600 mm（上翼板頂至下翼板底）
#                           #9 寬 300 在上、窄 200 在下
HW = D - TT - TB          # 腹板淨高（推得值 550 mm）

PW, PH = 520, 420


def _rect(cv, x0, x1, y0, y1):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], C["fill_c"], C["member"], 1.8)


def beam_panel():
    sx = (PW - 160) / SPAN
    cv = Canvas(PW, PH, sx=sx, ox=80, oy=190)
    cv.panel("梁立面", "A 端滾支、B 端固定（跨度示意）")
    cv.line((0, 0), (SPAN, 0), C["member"], 5, cap="butt")
    cv.support((0, 0), A_KIND, 0, size=16)
    cv.support((SPAN, 0), B_KIND, 90, size=28)      # 牆在右側（剖線朝外）
    cv.udl((0, 0), (SPAN, 0), 0.11 * SPAN, n=11, label="w_{u}")
    cv.text((0, 0), "A", 16, C["text"], weight="700", dx=-24, dy=-14)
    cv.text((SPAN, 0), "B", 16, C["text"], weight="700", dx=30, dy=-14)
    cv.dim((0, 0), (SPAN, 0), f"{SPAN:.0f} m", off=80, label_off=16)
    return cv


def section_panel():
    sx = 0.38
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2, oy=66)
    cv.panel("梁斷面", "依比例；600 mm 為全深")
    _rect(cv, -BT / 2, BT / 2, D - TT, D)            # 上翼板
    _rect(cv, -TW / 2, TW / 2, TB, D - TT)           # 腹板
    _rect(cv, -BB / 2, BB / 2, 0, TB)                # 下翼板
    cv.dim((-BT / 2, D), (BT / 2, D), f"{BT:.0f} mm", off=-22, label_off=-14)
    cv.dim((-BB / 2, 0), (BB / 2, 0), f"{BB:.0f} mm", off=22, label_off=16)
    cv.dim((-BT / 2, D - TT), (-BT / 2, D), f"{TT:.0f} mm", off=-22, label_off=-34)
    cv.dim((-BB / 2, 0), (-BB / 2, TB), f"{TB:.0f} mm", off=-22, label_off=-34)
    ym = D / 2                                       # 腹板厚：兩側箭頭夾腹板
    cv.arrow((-TW / 2 - 70, ym), (-TW / 2, ym), C["dim"], 1.2, 7)
    cv.arrow((TW / 2 + 70, ym), (TW / 2, ym), C["dim"], 1.2, 7)
    cv.math_px(cv.X(-TW / 2 - 70) - 6, cv.Y(ym), f"{TW:.0f} mm", 14, C["dim"], "end")
    cv.dim((BB / 2, 0), (BB / 2, D), f"{D:.0f} mm", off=(BT - BB) / 2 * sx + 34,
           label_off=34, color=C["accent"])
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([beam_panel(), section_panel()], cols=2,
            title="SS-2020-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#9；只畫考卷所給條件",
            note="600 mm 為全深（上翼板頂至下翼板底），腹板淨高 550 mm 為推得值",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把 600 mm 讀成腹板高；上下翼板對調；A、B 支承互換"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    assert abs(HW - 550) < 1e-9
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
