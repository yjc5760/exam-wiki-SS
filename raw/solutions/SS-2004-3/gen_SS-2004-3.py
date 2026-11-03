#!/usr/bin/env python3
"""
SS-2004-3 托架偏心載重之填角銲（LRFD 彈性法）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2004-3.py [輸出目錄]

重繪依據：題目正本 SS-2004-3-problem.md §4 判讀清單（待確認）。
只畫考卷附圖所示：托架板搭於柱翼板、上下兩組 L 形填角銲（斜線區）、7.5／10／5／15／5 cm 尺寸、Pu 1:1 斜向。
托架板與銲道依比例（銲道寬以 10 mm 銲腳示意）；柱翼板寬、托架右緣位置與斜切轉折為示意（考卷未標）。
附表（表 10.2.5 銲接設計強度）已照錄於題目正本 §2，不重繪。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2004-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2004-3-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
LAP = 7.5           # #2 托架左緣至柱翼板右緣 7.5 cm（＝水平銲道長）
EP = 10.0           # #3 柱翼板右緣至 Pu 作用點 10 cm
HV = 5.0            # #1 垂直銲道各 5 cm（沿托架左緣，上下各一）
HM = 15.0           # #1 中段 15 cm 不銲
H = 2 * HV + HM     # 托架總高 25 cm
#                     #4 Pu 作用於托架上緣，1:1 向左下
#                     #5 只畫一面（單面填角銲，待確認）
W = 1.0             # 題文 銲腳 10 mm（斜線區寬度）
# 示意（考卷未標）：
BF = 14.0           # 柱翼板寬
X_RE = EP + 2.5     # 托架右緣
Y_K = H - 6.5       # 右緣垂直段下端（斜切起點）
COL_EXT = 5.0

PW, PHT = 760, 680


def _hatched(cv, x0, x1, y0, y1, step=0.55):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], C["fill_t"], C["load"], 1.2)
    xa, xb = min(x0, x1), max(x0, x1)
    ya, yb = min(y0, y1), max(y0, y1)
    h = yb - ya
    k = xa - h
    while k < xb:
        p0 = (max(k, xa), ya + max(0, xa - k))
        p1 = (min(k + h, xb), ya + min(h, xb - k))
        if p1[0] > p0[0]:
            cv.line(p0, p1, C["load"], 1.0)
        k += step


def _zig(cv, x0, x1, y):
    xm = (x0 + x1) / 2
    cv.poly([(x0, y), (xm - 0.6, y), (xm - 0.2, y + 1.0), (xm + 0.2, y - 1.0), (xm + 0.6, y), (x1, y)],
            C["member"], 1.8)


def panel():
    sx = 14.0
    cv = Canvas(PW, PHT, sx=sx, ox=380, oy=105)
    cv.panel("托架立面", "托架板搭接於柱翼板（翼板面向讀者）")
    # 柱翼板（托架以外可見部分）
    top, bot = H + COL_EXT, -COL_EXT
    cv.line((-BF, bot), (-BF, top), C["member"], 2.0)
    cv.line((0, H), (0, top), C["member"], 2.0)
    cv.line((0, 0), (0, bot), C["member"], 2.0)
    _zig(cv, -BF - 1, 1, top)
    _zig(cv, -BF - 1, 1, bot)
    # 托架板
    cv.polygon([(-LAP, 0), (0, 0), (X_RE, Y_K), (X_RE, H), (-LAP, H)], C["fill_c"], C["member"], 2.2)
    # 銲道（斜線區）：上組＝上緣水平 7.5＋左緣垂直 5；下組對稱
    _hatched(cv, -LAP, 0, H, H + W)
    _hatched(cv, -LAP - W, -LAP, H - HV, H + W)
    _hatched(cv, -LAP, 0, -W, 0)
    _hatched(cv, -LAP - W, -LAP, -W, HV)
    # 尺寸：上方 7.5、10
    yd = H + COL_EXT + 3.0
    cv.line((-LAP, H + W), (-LAP, yd + 0.5), C["dim"], 1, dash="3 3")
    cv.line((0, top), (0, yd + 0.5), C["dim"], 1, dash="3 3")
    cv.line((EP, H), (EP, yd + 0.5), C["muted"], 1.2, dash="5 4")
    cv.dim((-LAP, yd), (0, yd), f"{LAP} cm", label_off=-15)
    cv.dim((0, yd), (EP, yd), f"{EP:.0f} cm", label_off=-15)
    # 尺寸：左側 5／15／5
    xd = -BF - 3.0
    for ya, yb, lab in ((H, H - HV, f"{HV:.0f} cm"), (H - HV, HV, f"{HM:.0f} cm"), (HV, 0, f"{HV:.0f} cm")):
        cv.dim((xd, ya), (xd, yb), lab, label_off=30)
    for yy in (H, H - HV, HV, 0):
        cv.line((xd - 0.6, yy), (-LAP - W - 0.3, yy), C["dim"], 1, dash="3 3")
    # Pu：托架上緣、距翼板右緣 10 cm，1:1 向左下
    L = 7.5
    tail = (EP + L, H + L)
    cv.arrow(tail, (EP, H), C["load"], 3.2, 12)
    cv.math(tail, "P_{u}", 17, C["load"], "start", dx=6, dy=-8, weight="700")
    s = 1.6
    t0 = (EP + 2.6, H + 2.6 - 0.0)
    t0 = (t0[0] + 0.5, t0[1] - 0.5)
    t1 = (t0[0] + s, t0[1] + s)
    cn = (t1[0], t0[1])
    cv.poly([t0, cn, t1], C["load"], 1.4)
    cv.text(((t0[0] + cn[0]) / 2, t0[1]), "1", 13, C["load"], dy=11)
    cv.text((cn[0], (cn[1] + t1[1]) / 2), "1", 13, C["load"], "start", dx=6)
    # 銲道說明
    cv.text_px(PW - 24, PHT - 40, "斜線區＝填角銲（銲腳 10 mm）", 12.5, C["load"], "end")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([panel()], cols=1,
            title="SS-2004-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#5；托架與銲道依比例，柱翼板寬與托架右緣外形為示意",
            note="每組銲道是水平 7.5 cm＋垂直 5 cm 的 L 形，中段 15 cm 不銲；10 cm 由翼板右緣量到 Pu",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "漏掉垂直 5 cm 段或把中段 15 cm 也當銲道；10 cm 誤由托架左緣量起"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
