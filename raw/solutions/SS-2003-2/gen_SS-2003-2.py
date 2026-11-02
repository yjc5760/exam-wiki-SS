#!/usr/bin/env python3
"""
SS-2003-2 混凝土包覆型鋼合成柱 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2003-2.py [輸出目錄]

重繪依據：題目正本 SS-2003-2-problem.md §4 判讀清單（2026-11-02 已確認）與 §1 題文
（H312×303×13×21）。混凝土外廓與型鋼依比例；鋼筋位置考卷未標，僅示意四角。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2003-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2003-2-problem.md §4，已確認）；單位 mm
# ══════════════════════════════════════════════════════════
B, H = 500.0, 600.0                     # #1 混凝土寬 500（水平）× 高 600（垂直）
D, BF, TW, TF = 312.0, 303.0, 13.0, 21.0   # §1 題文 H312×303×13×21；#2 翼板水平、腹板垂直、置中
N_BAR = 4                               # #4 4 根 D32，四角各 1 根
COVER_SKETCH = 55.0                     # 鋼筋位置示意用（考卷未標，非題給）


def _rect(cv, x0, x1, y0, y1, fill, stroke=C["member"], w=1.6):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, stroke, w)


def fig1_problem():
    W, Hc, sx = 520, 540, 0.56
    cv = Canvas(W, Hc, sx=sx, ox=W / 2 + 20, oy=Hc / 2 - 30)
    cv.panel("合成柱斷面", "混凝土與型鋼依比例；鋼筋位置示意")
    _rect(cv, -B / 2, B / 2, -H / 2, H / 2, C["border"], C["member"], 2.0)
    _rect(cv, -BF / 2, BF / 2, D / 2 - TF, D / 2, C["member"], C["member"])
    _rect(cv, -BF / 2, BF / 2, -D / 2, -D / 2 + TF, C["member"], C["member"])
    _rect(cv, -TW / 2, TW / 2, -D / 2 + TF, D / 2 - TF, C["member"], C["member"])
    c = COVER_SKETCH
    for sxg in (-1, 1):
        for syg in (-1, 1):
            cv.dot((sxg * (B / 2 - c), syg * (H / 2 - c)), 6.5, fill=C["text"], stroke=C["text"], w=1)
    cv.dim((-B / 2, H / 2), (B / 2, H / 2), f"{B:.0f} mm", off=-24, label_off=-14)
    cv.dim((-B / 2, -H / 2), (-B / 2, H / 2), f"{H:.0f} mm", off=-28, label_off=-34)
    cv.text_px(W / 2, Hc - 26, "H312×303×13×21 置中；4 根 D32 於四角", 12.5, C["muted"])
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2003-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1、#2、#4；只畫考卷所給條件",
            note="強軸（水平軸）挫屈沿 600 mm 方向、弱軸挫屈沿 500 mm 方向",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "500／600 mm 方向對調（r_m 下限取錯邊）；鋼筋根數讀錯"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
