#!/usr/bin/env python3
"""
SS-2011-2 兩鋼架之靠桿效應（萊梅厥公式） — 題目附圖重繪腳本

用法：
    python3 gen_SS-2011-2.py [輸出目錄]

重繪依據：題目正本 SS-2011-2-problem.md §4 判讀清單（2026-11-02 已確認）。
只畫考卷給的東西（支承、節點、EI、載重、L、L_b）；不含任何解題結果。
L、L_b 為符號，圖形比例示意。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2011-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2011-2-problem.md §4，已確認）
# ══════════════════════════════════════════════════════════
#   #4 B 固接；#5 A 鉸圓（AB 頂與頂梁鉸接）；#6 C、E、G 鉸圓；#7 D、F、H 鉸支
#   #8 靠桿 EI = ∞、兩端鉸；#9 頂梁 EI = ∞；#10 每根柱頂一個 P，柱高皆 L
FRAMES = {"(I)": [("A", "B")] + [("C", "D")],
          "(II)": [("A", "B"), ("C", "D"), ("E", "F"), ("G", "H")]}
L_DRAW, LB_DRAW = 1.0, 1.3        # 繪圖比例（L、L_b 為符號）
W, PH = 860, 420


def frame_panel(name, cols):
    n = len(cols)
    span = (n - 1) * LB_DRAW
    sx = min(165, (W - 240) / max(span, 1e-9))
    cv = Canvas(W, PH, sx=sx, ox=(W - span * sx) / 2 + 10, oy=95)
    cv.panel(f"鋼架 {name}", "頂梁 EI = ∞；AB 以外皆為靠桿")
    xs = [k * LB_DRAW for k in range(n)]
    cv.line((0, L_DRAW), (xs[-1], L_DRAW), C["member"], 9, cap="butt")
    cv.math(((xs[-1]) / 2 if n > 2 else xs[-1] / 2, L_DRAW), "EI = ∞", 14, C["text"], dy=-18)
    for k, (top, bot) in enumerate(cols):
        x = xs[k]
        lean = k > 0
        cv.line((x, 0), (x, L_DRAW), C["member"], 7 if lean else 3.6, cap="butt")
        cv.support((x, 0), "pin" if lean else "fixed", 0, size=14 if lean else 20)
        cv.dot((x, L_DRAW), 6.5, fill="#FFFFFF", stroke=C["member"], w=2.6)
        cv.arrow((x, L_DRAW + 0.30), (x, L_DRAW + 0.05), C["load"], 2.8, 10)
        cv.math((x, L_DRAW + 0.30), "P", 15, C["load"], "start", dx=8, weight="700")
        cv.text((x, L_DRAW), top, 14, C["text"], "start", dx=10, dy=16, weight="700")
        cv.text((x, 0), bot, 14, C["text"], "start", dx=12, dy=-12, weight="700")
        cv.math((x, L_DRAW / 2), "EI = ∞" if lean else "EI", 14, C["text"], "start", dx=12)
        if not lean:
            cv.math((x, L_DRAW / 2), "K = ?", 14, C["text"], "end", dx=-12)
        if k:
            cv.dim((xs[k - 1], 0), (x, 0), "L_{b}", off=52, label_off=16)
    cv.dim((0, 0), (0, L_DRAW), "L", off=-66, label_off=-16)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([frame_panel(k, v) for k, v in FRAMES.items()], cols=1,
            title="SS-2011-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #4–#10；只畫考卷所給條件",
            note="B 固接、A 為鉸圓；靠桿 C-D、E-F、G-H 頂端鉸圓、底端鉸支",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "B 讀成鉸支或 A 讀成剛接（AB 自身 K 判錯）；把 EI = ∞ 的靠桿當成有側向勁度"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
