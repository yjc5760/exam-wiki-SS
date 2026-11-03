#!/usr/bin/env python3
"""
SS-2004-2 H 型鋼拉力構材翼板續接（摩阻型螺栓設計）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2004-2.py [輸出目錄]

重繪依據：題目正本 SS-2004-2-problem.md §4 判讀清單（待確認）。
只畫考卷附圖所示：兩段 H150×150×7×10 對接、間隙 5 mm、翼板外側外連接板、內側內連接板。
構材深度、翼板厚與 5 mm 間隙依比例；連接板厚度與長度為所求，只示意位置，不標尺寸；
考卷附圖未畫螺栓（螺栓直徑、個數、配置皆為所求），本圖亦不畫。
附表（聯結物容許應力）已照錄於題目正本 §2，不重繪。
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2004-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2004-2-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
D, TF = 150.0, 10.0     # 題文 H150×150×7×10：全深 150 mm、翼板厚 10 mm
GAP = 5.0               # #2 兩段構材端面間隙 5 mm
#                         #1 每片翼板：外側一片外連接板、內側（腹板兩側）內連接板
# 示意（為所求，考卷未給）：
T_PL = 9.0              # 連接板厚（示意）
L_PL = 300.0            # 連接板全長（示意）
L_MEM = 380.0           # 每段構材畫出長度（示意）

PW, PH = 1000, 470


def _rect(cv, x0, x1, y0, y1, fill=C["fill_c"], w=1.8):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, C["member"], w)


def _break_end(cv, x, sgn):
    """構材斷裂端：S 形曲線（同考卷）"""
    n = 40
    pts = [(x + sgn * 12 * math.sin(2 * math.pi * i / n), D + 4 - (D + 8) * i / n)
           for i in range(n + 1)]
    cv.poly(pts, C["member"], 2.0)


def panel():
    sx = 1.18
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2, oy=150)
    cv.panel("翼板續接立面", "兩段 H150×150×7×10 對接；本設計僅在翼板連結")
    g = GAP / 2
    for sg in (-1, 1):
        xa, xb = sg * g, sg * L_MEM
        # 翼板（上、下）與構材外輪廓
        for y0 in (0.0, D - TF):
            _rect(cv, min(xa, xb), max(xa, xb), y0, y0 + TF, "rgba(63,74,90,0.10)", 1.6)
        cv.line((xa, TF), (xa, D - TF), C["member"], 1.6)      # 端面
        _break_end(cv, xb, sg)
    # 外連接板（翼板外側）
    _rect(cv, -L_PL / 2, L_PL / 2, D, D + T_PL)
    _rect(cv, -L_PL / 2, L_PL / 2, -T_PL, 0)
    # 內連接板（翼板內側；立面上腹板兩側的兩片重疊成一條）
    _rect(cv, -L_PL / 2, L_PL / 2, D - TF - T_PL, D - TF)
    _rect(cv, -L_PL / 2, L_PL / 2, TF, TF + T_PL)
    # 標註
    p_out = (-L_PL / 2 + 30, D + T_PL)
    q_out = (-L_PL / 2 - 40, D + 60)
    cv.line(p_out, q_out, C["muted"], 1.2)
    cv.dot(p_out, 3, C["muted"], C["muted"], 0)
    cv.text(q_out, "外連接板", 15, C["text"], "end", dx=-6)
    p_in = (L_PL / 2 - 30, D - TF - T_PL / 2)
    q_in = (L_PL / 2 + 50, D + 60)
    cv.line(p_in, q_in, C["muted"], 1.2)
    cv.dot(p_in, 3, C["muted"], C["muted"], 0)
    cv.text(q_in, "內連接板", 15, C["text"], "start", dx=6)
    # 5 mm 間隙（外側箭頭）
    yd = -T_PL - 32
    for sg in (-1, 1):
        cv.line((sg * g, 0), (sg * g, yd - 6), C["dim"], 1, dash="3 3")
        cv.arrow((sg * (g + 28), yd), (sg * g, yd), C["dim"], 1.4, 8)
    cv.math((0, yd), f"{GAP:.0f} mm", 15, C["text"], dy=24)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([panel()], cols=1,
            title="SS-2004-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1、#2；梁深、翼板厚與間隙依比例，連接板厚度與長度為所求（示意）",
            note="每片翼板上下兩面都有連接板（外＋內）→ 螺栓雙剪；內連接板在腹板兩側各一片",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "只看到外連接板而按單剪設計；把內連接板當成腹板續接板"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
