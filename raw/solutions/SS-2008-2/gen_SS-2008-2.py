#!/usr/bin/env python3
"""
SS-2008-2 靠桿效應與萊梅厥公式 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2008-2.py [輸出目錄]

重繪依據：題目正本 SS-2008-2-problem.md §4 判讀清單（2026-11-02 已確認）。
只畫考卷給的東西（支承、節點、EI、載重、L、L_b）；不含任何解題結果。
L、L_b 為符號，圖形比例示意。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2008-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2008-2-problem.md §4，已確認）
# ══════════════════════════════════════════════════════════
SINGLE_BASE = "pin"        # #1 單根柱底部鉸支
SINGLE_TOP = "guided"      # #2 頂部導槽滾支：可水平移動、不可轉動
K_SINGLE = 2.0             # 題文 K = 2.0（圖面文字 K=2）
A_KIND = D_KIND = "pin"    # #4 A 鉸支、#7 D 鉸支
B_RIGID = True             # #5 B 剛接（無鉸圓）
C_HINGE = True             # #6 C 鉸接（鉸圓）；#8 CD 為靠桿
#                            #9 梁 BC EI = ∞；#10 B、C 各受垂直 P
L_DRAW, LB_DRAW = 1.0, 1.25   # 繪圖比例（L、L_b 為符號）

PW, PH = 520, 470


def _guided_top(cv, p):
    """導槽滾支：柱頂板＋兩個滾輪＋上方固定面（可平移、不可轉動）"""
    x, y = cv.P(p)
    cv.parts.append(f'<line x1="{x-20:.1f}" y1="{y:.1f}" x2="{x+20:.1f}" y2="{y:.1f}" '
                    f'stroke="{C["member"]}" stroke-width="4" stroke-linecap="butt"/>')
    for dx in (-9, 9):
        cv.parts.append(f'<circle cx="{x+dx:.1f}" cy="{y-7:.1f}" r="5" fill="#FFFFFF" '
                        f'stroke="{C["member"]}" stroke-width="2"/>')
    cv.parts.append(f'<line x1="{x-24:.1f}" y1="{y-14:.1f}" x2="{x+24:.1f}" y2="{y-14:.1f}" '
                    f'stroke="{C["member"]}" stroke-width="2.6" stroke-linecap="round"/>')
    for k in range(6):
        bx = x - 22 + k * 9
        cv.parts.append(f'<line x1="{bx:.1f}" y1="{y-14:.1f}" x2="{bx+7:.1f}" y2="{y-23:.1f}" '
                        f'stroke="{C["member"]}" stroke-width="1.8" stroke-linecap="round"/>')


def single_panel():
    sx = 250
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2, oy=110)
    cv.panel("單根柱", "底部鉸支、頂部導槽滾支")
    cv.line((0, 0), (0, L_DRAW), C["member"], 4, cap="butt")
    cv.support((0, 0), SINGLE_BASE, 0, size=14)
    _guided_top(cv, (0, L_DRAW))
    cv.dim((0, 0), (0, L_DRAW), "L", off=-70, label_off=-16)
    cv.math((0, L_DRAW / 2), "EI", 15, C["text"], "end", dx=-14)
    cv.math((0, L_DRAW / 2), f"K = {K_SINGLE:g}", 15, C["text"], "start", dx=14)
    return cv


def frame_panel():
    sx = 220
    cv = Canvas(PW, PH, sx=sx, ox=120, oy=110)
    cv.panel("鋼架", "CD 柱為靠桿")
    A, D = (0, 0), (LB_DRAW, 0)
    B, Cn = (0, L_DRAW), (LB_DRAW, L_DRAW)
    cv.line(A, B, C["member"], 4, cap="butt")
    cv.line(D, Cn, C["member"], 4, cap="butt")
    cv.line(B, Cn, C["member"], 9, cap="butt")                    # EI = ∞ 梁
    cv.support(A, A_KIND, 0, size=14)
    cv.support(D, D_KIND, 0, size=14)
    cv.dot(Cn, 7, fill="#FFFFFF", stroke=C["member"], w=2.6)       # C 鉸圓
    for p in (B, Cn):
        cv.arrow((p[0], p[1] + 0.32), (p[0], p[1] + 0.03), C["load"], 3.0, 11)
        cv.math((p[0], p[1] + 0.32), "P", 16, C["load"], "start", dx=10, weight="700")
    cv.math(((B[0] + Cn[0]) / 2, L_DRAW), "EI = ∞", 15, C["text"], dy=-20)
    for p, n, dx in ((A, "A", -16), (B, "B", -16), (Cn, "C", 18), (D, "D", 18)):
        cv.text(p, n, 15, C["text"], "middle", dx=dx, dy=-14 if p[1] else -8, weight="700")
    cv.math((0, L_DRAW / 2), "EI", 15, C["text"], "end", dx=-12)
    cv.math((0, L_DRAW / 2), "K = ?", 15, C["text"], "start", dx=12)
    cv.math((LB_DRAW, L_DRAW / 2), "EI", 15, C["text"], "start", dx=12)
    cv.dim(A, B, "L", off=-62, label_off=-16)
    cv.dim(A, D, "L_{b}", off=58, label_off=16)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([single_panel(), frame_panel()], cols=2,
            title="SS-2008-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1、#2、#4–#10；只畫考卷所給條件",
            note="A、D 為鉸支；B 剛接、C 鉸接（CD 為靠桿）；梁 EI = ∞",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "A 或單根柱底讀成固定端；B、C 的剛接／鉸接對調"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
