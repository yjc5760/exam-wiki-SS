#!/usr/bin/env python3
"""
SS-2019-4 組合斷面蓋板之斷續填角銲（LRFD，剪力流）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2019-4.py [輸出目錄]

重繪依據：題目正本 SS-2019-4-problem.md §4 判讀清單（待確認）。
只畫考卷附圖所示：H500×200×9×16 上翼板頂面疊 PL25×300，鋼板底面與翼板兩側邊緣交角各一道填角銲，
銲接符號 8 ▷ L-150（基線上下對稱）。
斷面依比例（題文尺寸）；銲道三角形放大示意（實際銲腳 8 mm）。L 為所求，符號照考卷寫「L」。
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2019-4"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2019-4-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
D, BF, TW, TF = 500.0, 200.0, 9.0, 16.0   # 題文 H500×200×9×16
TP, BP = 25.0, 300.0                      # 題文 PL25×300（圖上標 300 mm）
WS = "8"                                  # #2 填角銲腳長 8 mm
PITCH = "L-150"                           # #2 每段長 L（所求）－中心距 150 mm，上下對稱（鏈式）
#                                           #1 銲道：鋼板底面與翼板左右兩側邊緣交角各一道
W_DRAW = 16.0                             # 銲道三角形繪製尺寸（放大示意，實際 8 mm）

PW, PHT = 820, 730


def _rect(cv, x0, x1, y0, y1, fill=C["fill_c"], w=1.8):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, C["member"], w)


def panel():
    sx = 0.95
    cv = Canvas(PW, PHT, sx=sx, ox=300, oy=60)
    cv.panel("組合斷面", "H500×200×9×16 ＋ PL25×300（上翼板頂面）")
    _rect(cv, -BF / 2, BF / 2, 0, TF)
    _rect(cv, -TW / 2, TW / 2, TF, D - TF)
    _rect(cv, -BF / 2, BF / 2, D - TF, D)
    _rect(cv, -BP / 2, BP / 2, D, D + TP, "rgba(180,83,9,0.16)")
    for sg in (-1, 1):                        # 填角銲：鋼板底面 × 翼板側緣
        x = sg * BF / 2
        cv.polygon([(x, D), (x + sg * W_DRAW, D), (x, D - W_DRAW)], C["member"], C["member"], 1)
    cv.dim((-BP / 2, D + TP), (BP / 2, D + TP), "300 mm", off=-30, label_off=-16, size=16)
    # 銲接符號：箭頭指右側銲道
    m = C["text"]
    tx, ty = cv.P((BF / 2 + W_DRAW * 0.45, D - W_DRAW * 0.45))
    kx, ky = tx + 70, ty + 75
    cv.parts.append(f'<line x1="{kx:.1f}" y1="{ky:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="{m}" stroke-width="1.5"/>')
    ang = math.atan2(ty - ky, tx - kx)
    hl, hw = 11, 4
    pts = [(tx, ty), (tx - hl * math.cos(ang) + hw * math.sin(ang), ty - hl * math.sin(ang) - hw * math.cos(ang)),
           (tx - hl * math.cos(ang) - hw * math.sin(ang), ty - hl * math.sin(ang) + hw * math.cos(ang))]
    cv.parts.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{m}"/>')
    cv.parts.append(f'<line x1="{kx:.1f}" y1="{ky:.1f}" x2="{kx + 210:.1f}" y2="{ky:.1f}" stroke="{m}" stroke-width="1.5"/>')
    x0 = kx + 62
    for sg in (-1, 1):
        cv.parts.append(f'<polygon points="{x0:.1f},{ky:.1f} {x0:.1f},{ky + sg * 15:.1f} {x0 + 15:.1f},{ky:.1f}" '
                        f'fill="#FFFFFF" stroke="{m}" stroke-width="1.5"/>')
        cv.text_px(x0 - 8, ky + sg * 13, WS, 17, m, "end")
        cv.text_px(x0 + 22, ky + sg * 13, PITCH, 17, m, "start")
    cv.text_px(PW - 24, PHT - 34, "黑色三角＝填角銲（放大示意）", 12.5, C["muted"], "end")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([panel()], cols=1,
            title="SS-2019-4 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1、#2；斷面依比例，銲道三角形放大示意；L 為所求",
            note="兩道銲在鋼板底面與翼板側緣交角；L-150 為每段長 L、中心距 150 mm，基線上下對稱＝兩側並列",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "只算一道銲（漏另一側）；把 150 當成段長或淨距；上下對稱誤讀成交錯"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
