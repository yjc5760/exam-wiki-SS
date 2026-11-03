#!/usr/bin/env python3
"""
SS-2012-4 梁柱接頭剪力板栓接設計（LRFD）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2012-4.py [輸出目錄]

重繪依據：題目正本 SS-2012-4-problem.md §4 判讀清單（待確認）。
只畫考卷附圖所示：柱、梁（翼板延伸至柱面）、剪力板 180 mm（沿梁深）× 80 mm（自柱面向外）。
剪力板依比例；梁深、柱深、翼板厚與構材長度為示意（考卷未給）。
螺栓數目與配置為所求，考卷附圖未畫，本圖亦不畫（題文另指定螺栓線距柱面 40 mm）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2012-4"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2012-4-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
HP = 180.0          # #1 剪力板沿梁深方向 180 mm（「長」）
WP = 80.0           # #1 剪力板自柱面向外 80 mm（「寬」）
#                     #2 螺栓單行、距柱面 40 mm（題文；為考生配置，不畫）
# 示意（考卷未給）：
DB, TFB = 280.0, 12.0   # 梁深、梁翼板厚
DC, TFC = 175.0, 12.0   # 柱深、柱翼板厚
LB = 260.0              # 梁畫出長度
HC = 40.0               # 柱伸出梁翼外的長度

PW, PHT = 900, 700


def _rect(cv, x0, x1, y0, y1, fill="#FFFFFF", w=1.8):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, C["member"], w)


def panel():
    sx = 1.25
    cv = Canvas(PW, PHT, sx=sx, ox=360, oy=170)
    cv.panel("梁柱接頭立面", "單位：mm")
    top, bot = DB + HC, -HC
    # 柱兩翼板（雙線）
    for x0 in (-DC, -TFC):
        _rect(cv, x0, x0 + TFC, bot, top)
    for yy in (top, bot):
        xm = -DC / 2
        cv.poly([(-DC - 15, yy), (xm - 10, yy), (xm - 3, yy + 18), (xm + 3, yy - 18), (xm + 10, yy),
                 (15, yy)], C["member"], 1.8)
    # 梁翼板：延伸穿過柱（柱內為連續板）至梁端
    for y0 in (0.0, DB - TFB):
        _rect(cv, -DC + TFC, -TFC, y0, y0 + TFB)
        _rect(cv, 0, LB, y0, y0 + TFB)
    # 梁端斷裂線
    ym = DB / 2
    cv.poly([(LB, -6), (LB, ym - 18), (LB + 12, ym - 6), (LB - 12, ym + 6), (LB, ym + 18), (LB, DB + 6)],
            C["member"], 1.8)
    # 剪力板
    y0 = (DB - HP) / 2
    _rect(cv, 0, WP, y0, y0 + HP, C["fill_c"], 2.2)
    # 尺寸
    xd = WP + 40
    for yy in (y0, y0 + HP):
        cv.line((WP, yy), (xd + 8, yy), C["dim"], 1, dash="3 3")
    cv.dim((xd, y0 + HP), (xd, y0), f"{HP:.0f}", label_off=-24, size=16)
    yd = bot - 10
    cv.line((0, bot), (0, yd - 6), C["dim"], 1, dash="3 3")
    cv.line((WP, y0), (WP, yd - 6), C["dim"], 1, dash="3 3")
    cv.dim((0, yd), (WP, yd), f"{WP:.0f}", label_off=18, size=16)
    # 標註
    cv.line((WP * 0.55, y0 + HP), (WP * 0.9, DB + HC + 10), C["muted"], 1.1)
    cv.text((WP * 0.9, DB + HC + 10), "剪力板", 16, C["text"], "start", dx=4)
    cv.line((-DC + TFC / 2, DB * 0.35), (-DC - 45, DB * 0.2), C["muted"], 1.1)
    cv.text((-DC - 45, DB * 0.2), "柱", 16, C["text"], "end", dx=-4)
    cv.line((LB * 0.7, 0), (LB * 0.7 + 20, -40), C["muted"], 1.1)
    cv.text((LB * 0.7 + 20, -40), "梁", 16, C["text"], "start", dx=4)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([panel()], cols=1,
            title="SS-2012-4 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1；剪力板依比例，梁深、柱深與構材長度為示意；螺栓配置為所求（不畫）",
            note="180 mm 是沿梁深的板長、80 mm 是自柱面向外的板寬；螺栓線距柱面 40 mm（題文）",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "180／80 對調（把 80 當板長而排不下螺栓）；把螺栓配成兩行"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
