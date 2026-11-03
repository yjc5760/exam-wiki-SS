#!/usr/bin/env python3
"""
SS-2015-1 簡支鋼梁三分點載重之 BH 斷面選擇、剪力與撓度檢核（LRFD）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2015-1.py [輸出目錄]

重繪依據：題目正本 SS-2015-1-problem.md §4 判讀清單（待確認）。
只重繪圖 1(a)（簡支梁和斷面）；只畫考卷給的東西，不含任何解題結果（不標所選 BH 斷面）。
梁跨度依比例（3@2.8 m）；載重箭頭長度、梁高為示意；右側 BH 斷面為符號示意（H、B、tw、tf 為所求斷面之代號）。
不重繪：圖 1(b) 梁設計彎矩強度曲線（設計圖表，曲線讀值已照錄於 problem.md §2）、第 3 頁參考公式。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2015-1"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2015-1-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
NSEG, SEG = 3, 2.8          # 圖 1(a) 3@2.8 = 8.4 m
SPAN = NSEG * SEG
LOAD_AT = (1, 2)            # 題文 三分點各受 P_D、P_L
BRACE_AT = (0, 1, 2, 3)     # #1 側撐在兩支承與兩載重點（⊗）
#                             題文 P_D = 22 tf、P_L = 35 tf（圖上只標符號，數值照題文另列）
PD, PL = 22, 35

PW, PH = 640, 420


def _otimes(cv, p, r=7):
    x, y = cv.P(p)
    m = C["accent"]
    cv.parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#FFFFFF" stroke="{m}" stroke-width="1.8"/>')
    d = r * 0.7
    for sx_, sy_ in ((1, 1), (1, -1)):
        cv.parts.append(f'<line x1="{x-d*sx_:.1f}" y1="{y-d*sy_:.1f}" x2="{x+d*sx_:.1f}" y2="{y+d*sy_:.1f}" '
                        f'stroke="{m}" stroke-width="1.6"/>')


def beam_panel():
    sx = (PW - 140) / SPAN
    cv = Canvas(PW, PH, sx=sx, ox=70, oy=170)
    cv.panel("簡支梁", "左端鉸支、右端滾支；三分點受集中載重")
    h = 0.32                    # 梁高（示意）
    cv.polygon([(0, 0), (SPAN, 0), (SPAN, h), (0, h)], C["fill_c"], C["member"], 1.8)
    cv.support((0, 0), "pin", 0, size=14)
    cv.support((SPAN, 0), "roller", 0, size=14)
    for k in LOAD_AT:
        x = k * SEG
        cv.arrow((x, h + 2.0), (x, h + 0.05), C["load"], 2.6, 10)
        cv.math((x, h + 2.0), "P_{D}", 15, C["load"], "end", dx=-8, dy=6, weight="700")
        cv.math((x, h + 1.2), "P_{L}", 15, C["load"], "end", dx=-8, dy=6, weight="700")
    for k in BRACE_AT:
        _otimes(cv, (k * SEG, h / 2))
    _otimes(cv, (SPAN - 1.6, h + 1.7))
    cv.text((SPAN - 1.6, h + 1.7), "：側撐", 13, C["accent"], "start", dx=10)
    cv.text_px(PW / 2, 88, f"題文：P_D = {PD} tf、P_L = {PL} tf（各三分點）", 12.5, C["muted"])
    cv.dim((0, 0), (SPAN, 0), f"3@{SEG} = {SPAN:.1f} m", off=56, label_off=16)
    return cv


def section_panel():
    cv = Canvas(PW, PH, sx=1.0, ox=0, oy=0)
    cv.panel("斷面（符號示意）", "BH H×B×tw×tf，單位：mm")
    cx, top, bot = PW / 2 - 20, PH - 110, 110      # 像素座標排版（y 向上）
    B, TF, TW = 150, 18, 12
    for xa, xb, ya, yb in ((cx - B / 2, cx + B / 2, top - TF, top), (cx - B / 2, cx + B / 2, bot, bot + TF),
                           (cx - TW / 2, cx + TW / 2, bot + TF, top - TF)):
        cv.polygon([(xa, ya), (xb, ya), (xb, yb), (xa, yb)], C["fill_c"], C["member"], 1.6)
    cv.dim((cx + B / 2, bot), (cx + B / 2, top), "H", off=36, label_off=16)
    cv.dim((cx - B / 2, bot), (cx + B / 2, bot), "B", off=30, label_off=16)
    cv.dim((cx - B / 2, top - TF), (cx - B / 2, top), "t_{f}", off=-26, label_off=-16)
    cv.arrow((cx - 50, (top + bot) / 2), (cx - TW / 2 - 1, (top + bot) / 2), C["dim"], 1.2, 8)
    cv.arrow((cx + 50, (top + bot) / 2), (cx + TW / 2 + 1, (top + bot) / 2), C["dim"], 1.2, 8)
    cv.math((cx - 54, (top + bot) / 2), "t_{w}", 15, C["dim"], "end")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([beam_panel(), section_panel()], cols=2,
            title="SS-2015-1 題目附圖 1(a)（重繪）",
            sub="依題目正本判讀清單 #1；只畫考卷所給條件；圖 1(b) 設計彎矩強度曲線不重繪",
            note="⊗ 側撐在兩支承與兩載重點：每段無側撐長度都是一個三分段",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "漏看載重點的 ⊗ 側撐而以全跨 8.4 m 查圖 1(b)；P_D、P_L 誤當只作用一點"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
