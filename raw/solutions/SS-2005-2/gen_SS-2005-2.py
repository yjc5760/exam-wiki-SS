#!/usr/bin/env python3
"""
SS-2005-2 混凝土包覆鋼梁（SRC 梁）塑性應力分析 Mn — 題目附圖重繪腳本

用法：
    python3 gen_SS-2005-2.py [輸出目錄]

重繪依據：題目正本 SS-2005-2-problem.md §4 判讀清單（待確認）。
只畫考卷給的東西（斷面外形、H 型鋼、四支主筋、8 cm 尺寸），不含任何解題結果（不畫中性軸、應力塊）。
斷面、H 型鋼與主筋直徑依比例繪製。
示意部分：主筋水平位置（考卷未標，取與上下相同之 8 cm 內縮）、箍筋框線、骨材點。
不重繪：無。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2005-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2005-2-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
B, H = 50.0, 70.0           # #1 斷面寬 50 cm、高 70 cm
COVER = 8.0                 # #2 上、下緣至主筋「中心」8 cm
N_TOP, N_BOT = 2, 2         # #3 上 2 支、下 2 支，位於四角
DB = 3.2                    # 題文 D32（直徑約 3.2 cm，僅供依比例畫圓）
D, BF, TW, TF = 48.8, 30.0, 1.1, 1.8   # 題文 H488×300×11×18（mm → cm）
#                             #4 鋼梁直立置中
X_BAR = COVER               # 主筋水平內縮：考卷未標，示意取 8 cm
STIR = COVER - DB / 2 - 0.6 # 箍筋框線（示意）

PW, PH = 640, 620


def _rect(cv, x0, x1, y0, y1, fill, stroke, w=1.6, op=1.0):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, stroke, w, op)


def section_panel():
    sx = 5.6
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2 - B / 2 * sx - 40, oy=90)
    cv.panel("混凝土包覆梁斷面", "斷面、H 型鋼、主筋依比例；箍筋與骨材為示意")
    # 混凝土
    _rect(cv, 0, B, 0, H, C["ghost"], "none", 0, op=0.40)
    _rect(cv, 0, B, 0, H, "none", C["member"], 2.2)
    for (x, y) in ((6, 52), (12, 30), (38, 58), (41, 22), (9, 14), (30, 6.5), (20, 63),
                   (44, 44), (5, 40), (33, 40)):
        cv.circle((x, y), 0.45, "none", C["member2"], 1.0)
    # 箍筋（示意）
    _rect(cv, STIR, B - STIR, STIR, H - STIR, "none", C["member2"], 1.4)
    # H 型鋼（置中、直立）
    xc, yc = B / 2, H / 2
    st = C["member"]
    _rect(cv, xc - BF / 2, xc + BF / 2, yc + D / 2 - TF, yc + D / 2, C["fill_c"], st, 1.6)
    _rect(cv, xc - BF / 2, xc + BF / 2, yc - D / 2, yc - D / 2 + TF, C["fill_c"], st, 1.6)
    _rect(cv, xc - TW / 2, xc + TW / 2, yc - D / 2 + TF, yc + D / 2 - TF, C["fill_c"], st, 1.6)
    # 主筋（四角）
    bars = [(X_BAR, H - COVER), (B - X_BAR, H - COVER), (X_BAR, COVER), (B - X_BAR, COVER)]
    for p in bars:
        cv.circle(p, DB / 2, C["member"], C["member"], 1.0)
    # 尺寸
    cv.dim((0, H), (B, H), f"{B:.0f} cm", off=-34, label_off=-14)
    cv.dim((0, 0), (0, H), f"{H:.0f} cm", off=-46, label_off=-30)
    cv.dim((B, H - COVER), (B, H), f"{COVER:.0f} cm", off=46, label_off=30, color=C["accent"])
    cv.dim((B, 0), (B, COVER), f"{COVER:.0f} cm", off=46, label_off=30, color=C["accent"])
    # 標示
    cv.line((xc + TW / 2, yc + 4), (B + 14, yc + 6), C["muted"], 1.2)
    cv.text((B + 14, yc + 6), "鋼梁", 14, C["text"], "start", dx=4)
    cv.text((B + 14, yc + 6), "H488×300×11×18", 12, C["muted"], "start", dx=4, dy=20)
    for p in bars[2:]:
        cv.line(p, (B / 2, -9), C["muted"], 1.2)
    cv.text((B / 2, -9), "主筋 4-D32", 14, C["text"], dy=14)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([section_panel()], cols=1,
            title="SS-2005-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#4；只畫考卷所給條件",
            note="8 cm 量到主筋中心（不是箍筋線）；H 型鋼置於斷面正中",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把 8 cm 讀成保護層（量到鋼筋外緣或箍筋），使主筋深度差一個半徑；H 型鋼未置中"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
