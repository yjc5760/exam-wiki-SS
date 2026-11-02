#!/usr/bin/env python3
"""
SS-2011-4 無側撐鋼架柱 DE、EF 之有效長度係數 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2011-4.py [輸出目錄]

重繪依據：題目正本 SS-2011-4-problem.md §4 判讀清單（2026-11-02 已確認）。
只重繪構架（依比例）；考卷所附對位圖（Sidesway not prevented）屬設計圖表，不重繪。
各構材 I 值在考卷表格中（題目正本 §1），圖上不重複。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2011-4"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2011-4-problem.md §4，已確認）；單位 m
# ══════════════════════════════════════════════════════════
H_UP, H_LO = 4.0, 5.0           # #11 上層 4 m（AB、DE）、下層 5 m（BC、EF）
SP_L, SP_R = 6.0, 8.0           # #11 左跨 6 m（AD、BE）、右跨 8 m（DG、EH）
X0, X1, X2 = 0.0, SP_L, SP_L + SP_R
Y0, Y1, Y2 = 0.0, H_LO, H_LO + H_UP
N = {"A": (X0, Y2), "B": (X0, Y1), "C": (X0, Y0), "D": (X1, Y2), "E": (X1, Y1),
     "F": (X1, Y0), "G": (X2, Y2), "H": (X2, Y1)}
MEMBERS = ["AB", "BC", "DE", "EF", "AD", "DG", "BE", "EH"]   # #10 D 上方無柱
#   #4 A 鉸圓；#5 B 剛接；#6 C 固接；#7 F 鉸支；#8 G 導槽（可平移、不可轉）；#9 H 滾支（可轉）


def _guided(cv, p):
    """G：方塊上下各一排滾輪、外側固定面 → 可水平移動、不可轉動、不可垂直移動"""
    x, y = cv.P(p)
    m = C["member"]
    cv.parts.append(f'<rect x="{x:.1f}" y="{y-6:.1f}" width="22" height="12" fill="{m}"/>')
    for sgn in (-1, 1):
        for dx in (6, 16):
            cv.parts.append(f'<circle cx="{x+dx:.1f}" cy="{y+sgn*11:.1f}" r="4.6" fill="#FFFFFF" '
                            f'stroke="{m}" stroke-width="1.8"/>')
        yy = y + sgn * 17
        cv.parts.append(f'<line x1="{x-2:.1f}" y1="{yy:.1f}" x2="{x+26:.1f}" y2="{yy:.1f}" '
                        f'stroke="{m}" stroke-width="2.4"/>')
        for k in range(4):
            bx = x + k * 8
            cv.parts.append(f'<line x1="{bx:.1f}" y1="{yy:.1f}" x2="{bx+6:.1f}" y2="{yy+sgn*7:.1f}" '
                            f'stroke="{m}" stroke-width="1.6"/>')


def fig1_problem():
    W, H, sx = 700, 560, 34
    cv = Canvas(W, H, sx=sx, ox=150, oy=120)
    cv.panel("構架", "依比例；無側撐")
    for m in MEMBERS:
        cv.line(N[m[0]], N[m[1]], C["member"], 4.0, cap="butt")
    cv.dot(N["A"], 6, fill="#FFFFFF", stroke=C["member"], w=2.4)      # A 鉸圓
    cv.support(N["C"], "fixed", 0, size=20)
    cv.support(N["F"], "pin", 0, size=14)
    _guided(cv, N["G"])
    cv.support(N["H"], "roller", 0, size=14)
    off = {"A": (-16, -14), "B": (-16, -14), "C": (-16, -14), "D": (0, -18), "E": (-16, -14),
           "F": (-16, -14), "G": (-14, -16), "H": (0, -22)}
    for n, (dx, dy) in off.items():
        cv.text(N[n], n, 15, C["text"], "middle", dx=dx, dy=dy, weight="700")
    cv.dim(N["B"], N["A"], f"{H_UP:g}m", off=-50, label_off=-24)
    cv.dim(N["C"], N["B"], f"{H_LO:g}m", off=-50, label_off=-24)
    cv.dim((X0, Y0), (X1, Y0), f"{SP_L:g}m", off=62, label_off=16)
    cv.dim((X1, Y0), (X2, Y0), f"{SP_R:g}m", off=62, label_off=16)
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2011-4 題目附圖（重繪）",
            sub="依題目正本判讀清單 #4–#11；對位圖為設計圖表，不重繪",
            note="A 鉸接、C 固接、F 鉸支；G 可平移不可轉、H 可轉；D 上方無柱",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "A 讀成剛接、F 讀成固接；G、H 遠端條件對調（梁遠端修正係數用錯）"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
