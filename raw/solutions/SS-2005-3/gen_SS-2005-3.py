#!/usr/bin/env python3
"""
SS-2005-3 箱型懸臂梁銲接於柱（ASD 彈性法，彎矩＋扭矩）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2005-3.py [輸出目錄]

重繪依據：題目正本 SS-2005-3-problem.md §4 判讀清單（待確認）。
只畫考卷附圖所示：立面（柱、箱型梁、兩個銲接符號、50 cm、A-A 剖切記號）與 A-A 斷面（P 偏心 14 cm）。
箱型梁 300×300×18 與 50 cm、14 cm 依比例；柱深、柱翼板厚、柱內加勁板厚與柱長為示意（考卷未標）。
銲接符號照考卷：現場銲旗＋雙面填角（10／10；12–200／12–200，尾註「對稱於梁中心線」）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2005-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2005-3-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
B, T = 30.0, 1.8        # 題文 箱型梁 300×300×18×18 mm
E_M = 50.0              # #5 P 距柱面 50 cm（立面）
E_T = 14.0              # #5 P 距梁垂直中心線 14 cm（A-A 斷面），位於中心線左側
W1 = "10"               # #1 上翼板與柱面：10 mm 填角銲，雙面（符號 10/10），未標長度
W2, L2 = "12", "200"    # #2 腹板與柱面：12 mm 填角銲，雙面，每道 200 mm，對稱於梁中心線
#                         #3 下翼板無銲接符號（照考卷不畫符號）
# 示意（考卷未標）：
DC, TFC = 30.0, 1.6     # 柱深、柱翼板厚
TST = 1.6               # 柱內加勁板厚
HC = 46.0               # 柱自梁中心線上下各畫出長度
X_SEC = 100.0           # A-A 斷面在同一畫布上的水平位置（排版用）

PW, PHT = 1120, 720


def _zig(cv, x0, x1, y):
    xm = (x0 + x1) / 2
    cv.poly([(x0, y), (xm - 1.2, y), (xm - 0.4, y + 2.0), (xm + 0.4, y - 2.0), (xm + 1.2, y), (x1, y)],
            C["member"], 1.8)


def _weld_symbol(cv, tip, knee, ref_px, tri_px, top_l, bot_l, top_r=None, bot_r=None, tail=None):
    """銲接符號（像素排版）：箭頭→折點→基線；折點處現場銲旗；tri_px 處畫雙面填角三角形。"""
    m = C["text"]
    kx, ky = cv.P(knee)
    tx, ty = cv.P(tip)
    cv.parts.append(f'<line x1="{kx:.1f}" y1="{ky:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" '
                    f'stroke="{m}" stroke-width="1.5"/>')
    import math
    ang = math.atan2(ty - ky, tx - kx)
    hl, hw = 11, 4
    pts = [(tx, ty), (tx - hl * math.cos(ang) + hw * math.sin(ang), ty - hl * math.sin(ang) - hw * math.cos(ang)),
           (tx - hl * math.cos(ang) - hw * math.sin(ang), ty - hl * math.sin(ang) + hw * math.cos(ang))]
    cv.parts.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{m}"/>')
    cv.parts.append(f'<line x1="{kx:.1f}" y1="{ky:.1f}" x2="{kx + ref_px:.1f}" y2="{ky:.1f}" '
                    f'stroke="{m}" stroke-width="1.5"/>')
    # 現場銲旗
    cv.parts.append(f'<line x1="{kx:.1f}" y1="{ky:.1f}" x2="{kx:.1f}" y2="{ky - 34:.1f}" '
                    f'stroke="{m}" stroke-width="1.5"/>')
    cv.parts.append(f'<polygon points="{kx:.1f},{ky - 34:.1f} {kx + 12:.1f},{ky - 29:.1f} '
                    f'{kx:.1f},{ky - 24:.1f}" fill="{m}"/>')
    # 雙面填角：基線上下各一個直角三角形（垂直邊在左）
    x0 = kx + tri_px
    for sg in (-1, 1):
        cv.parts.append(f'<polygon points="{x0:.1f},{ky:.1f} {x0:.1f},{ky + sg * 13:.1f} '
                        f'{x0 + 13:.1f},{ky:.1f}" fill="#FFFFFF" stroke="{m}" stroke-width="1.5"/>')
    cv.text_px(x0 - 6, ky - 11, top_l, 14, m, "end")
    cv.text_px(x0 - 6, ky + 12, bot_l, 14, m, "end")
    if top_r:
        cv.text_px(x0 + 18, ky - 11, top_r, 14, m, "start")
        cv.text_px(x0 + 18, ky + 12, bot_r, 14, m, "start")
    if tail:
        ex = kx + ref_px
        cv.parts.append(f'<polyline points="{ex + 12:.1f},{ky - 10:.1f} {ex:.1f},{ky:.1f} '
                        f'{ex + 12:.1f},{ky + 10:.1f}" fill="none" stroke="{m}" stroke-width="1.5"/>')
        for i, line in enumerate(tail):
            cv.text_px(ex + 18, ky - 10 + 21 * i, line, 14, m, "start")


def _cut_mark(cv, p, up=True):
    x, y = cv.P(p)
    s = -1 if up else 1
    m = C["text"]
    cv.parts.append(f'<polyline points="{x:.1f},{y:.1f} {x:.1f},{y + s * 16:.1f} {x - 26:.1f},{y + s * 16:.1f}" '
                    f'fill="none" stroke="{m}" stroke-width="1.5"/>')
    cv.parts.append(f'<polygon points="{x - 34:.1f},{y + s * 16:.1f} {x - 24:.1f},{y + s * 16 - 4:.1f} '
                    f'{x - 24:.1f},{y + s * 16 + 4:.1f}" fill="{m}"/>')
    cv.text_px(x - 16, y + s * 16 + 14, "A", 15, m)


def _rect(cv, x0, x1, y0, y1, fill="none", w=2.0):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, C["member"], w)


def panel():
    sx = 6.4
    cv = Canvas(PW, PHT, sx=sx, ox=250, oy=PHT / 2 - 10)
    cv.panel("立面與 A-A 斷面", "註：銲接符號單位為 mm")
    h = B / 2
    # ── 柱（兩翼板＋梁翼高度之加勁板）──
    for x0 in (-DC, -TFC):
        _rect(cv, x0, x0 + TFC, -HC, HC, "#FFFFFF", 1.8)
    for yy in (h, -h):
        _rect(cv, -DC + TFC, -TFC, yy - TST, yy, "#FFFFFF", 1.6)
    _zig(cv, -DC - 1.5, 1.5, HC)
    _zig(cv, -DC - 1.5, 1.5, -HC)
    cv.line((-DC + TFC / 2, -HC + 4), (-DC - 4, -HC - 3), C["muted"], 1.1)
    cv.text((-DC - 4, -HC - 3), "鋼柱", 14, C["text"], "end", dx=-4)
    # ── 箱型梁立面 ──
    _rect(cv, 0, E_M, -h, h, C["fill_c"], 2.0)
    for yy in (h - T, -h + T):
        cv.line((0, yy), (E_M, yy), C["member"], 1.3, dash="6 4")
    cv.line((-6, 0), (E_M + 8, 0), C["muted"], 1.1, dash="12 3 2 3")
    # P（立面）
    cv.arrow((E_M, h + 11), (E_M, h + 0.4), C["load"], 5, 14)
    cv.math((E_M, h + 11), "P", 17, C["load"], dy=-12, weight="700")
    # A-A 剖切記號
    _cut_mark(cv, (E_M + 9, h + 2), up=True)
    _cut_mark(cv, (E_M + 9, -h - 2), up=False)
    # 50 cm
    yd = -h - 15
    cv.line((E_M, -h), (E_M, yd - 1.5), C["dim"], 1, dash="3 3")
    cv.dim((0, yd), (E_M, yd), f"{E_M:.0f} cm", label_off=-15)
    # ── 銲接符號 ──
    _weld_symbol(cv, (0, h), (9, h + 18), 120, 74, W1, W1)
    _weld_symbol(cv, (0, 0), (8, -h - 7), 110, 58, W2, W2, L2, L2,
                 tail=("對稱於梁", "中心線"))
    # ── A-A 斷面 ──
    xc = X_SEC + B / 2
    _rect(cv, X_SEC, X_SEC + B, -h, h, C["fill_c"], 2.0)
    _rect(cv, X_SEC + T, X_SEC + B - T, -h + T, h - T, "#FFFFFF", 1.6)
    cv.line((xc, h + 12), (xc, -h - 5), C["muted"], 1.1, dash="12 3 2 3")
    xp = xc - E_T
    cv.arrow((xp, h + 11), (xp, h + 0.4), C["load"], 5, 14)
    cv.math((xp, h + 11), "P", 17, C["load"], dy=-12, weight="700")
    cv.dim((xp, h + 7), (xc, h + 7), f"{E_T:.0f} cm", label_off=-14)
    cv.text((xc, -h - 9), "A-A 斷面", 15, C["text"], weight="700")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([panel()], cols=1,
            title="SS-2005-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#5；箱型梁與 50、14 cm 依比例，柱深與柱內加勁板為示意",
            note="只有兩個銲接符號（上翼板 10/10、腹板 12–200 對稱中心線），下翼板沒有符號；P 另有 14 cm 側向偏心",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "漏看 A-A 斷面的 14 cm 扭矩偏心；把 200 讀成銲腳或把下翼板也當有銲"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
