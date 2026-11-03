#!/usr/bin/env python3
"""
SS-2019-2 合成梁（實心 RC 版＋H500×200×10×16）正彎矩塑性強度 Mn — 題目附圖重繪腳本

用法：
    python3 gen_SS-2019-2.py [輸出目錄]

重繪依據：題目正本 SS-2019-2-problem.md §4 判讀清單（待確認）。
只畫考卷給的東西（版厚 150 mm、版直接擱在上翼板、H 型鋼直立），不含任何解題結果（不畫中性軸、應力塊）。
H 型鋼依 H500×200×10×16 按比例，版厚 150 mm 與鋼梁同比例。
示意部分：樓版左右截斷（有效寬度 2.5 m 遠大於圖幅，以斷裂線表示並以文字標註）、骨材點。
不重繪：無。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2019-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2019-2-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
T_SLAB = 150.0              # #1 實心版厚 150 mm，直接擱在上翼板頂面（無鋼承板、無托肩）
D, BF, TW, TF = 500.0, 200.0, 10.0, 16.0   # #3 H500×200×10×16 = d×bf×tw×tf（mm）
B_EFF = "2.5 m"             # 題文 有效寬度 2.5 m（圖上截斷示意）
HALF_SHOWN = 330.0          # 圖上顯示的半版寬（示意，mm）

PW, PH = 680, 680


def _rect(cv, x0, x1, y0, y1, fill, stroke, w=1.6, op=1.0):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, stroke, w, op)


def _break(cv, x, y0, y1):
    """斷裂線（Z 字）"""
    ym = (y0 + y1) / 2
    a = 14.0
    cv.poly([(x, y0 + 12), (x, ym + a), (x - a, ym), (x + a, ym), (x, ym - a), (x, y1 - 12)],
            C["member"], 1.6)


def section_panel():
    sx = 0.62
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2 - 40, oy=80)
    cv.panel("合成梁斷面", "H 型鋼與版厚依比例；樓版左右截斷示意")
    yb = D                       # 版底＝上翼板頂
    yt = D + T_SLAB
    _rect(cv, -HALF_SHOWN, HALF_SHOWN, yb, yt, C["ghost"], "none", 0, 0.45)
    cv.line((-HALF_SHOWN, yb), (HALF_SHOWN, yb), C["member"], 2.0)
    cv.line((-HALF_SHOWN, yt), (HALF_SHOWN, yt), C["member"], 2.0)
    _break(cv, -HALF_SHOWN, yt, yb)
    _break(cv, HALF_SHOWN, yt, yb)
    for (x, y) in ((-280, 560), (-190, 600), (-90, 545), (30, 610), (120, 560), (220, 600), (290, 548)):
        cv.circle((x, y), 6, "none", C["member2"], 1.0)
    st = C["member"]
    _rect(cv, -BF / 2, BF / 2, D - TF, D, C["fill_c"], st)
    _rect(cv, -BF / 2, BF / 2, 0, TF, C["fill_c"], st)
    _rect(cv, -TW / 2, TW / 2, TF, D - TF, C["fill_c"], st)
    cv.dim((HALF_SHOWN, yb), (HALF_SHOWN, yt), f"{T_SLAB:.0f} mm", off=46, label_off=36,
           color=C["accent"])
    cv.text((0, yt), "混凝土樓版", 15, C["text"], dy=-22, weight="700")
    cv.text((0, yt), f"有效寬度 {B_EFF}（題文；圖幅截斷）", 12.5, C["muted"], dy=-44)
    cv.line((BF / 2 - 20, D / 2 + 60), (BF / 2 + 120, D / 2 + 60), C["muted"], 1.2)
    cv.line((TW / 2, D / 2 + 30), (BF / 2 - 20, D / 2 + 60), C["muted"], 1.2)
    cv.text((BF / 2 + 120, D / 2 + 60), "H500×200×10×16", 13, C["text"], "start", dx=4)
    cv.text((BF / 2 + 120, D / 2 + 60), "d×bf×tw×tf（mm）", 12, C["muted"], "start", dx=4, dy=18)
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([section_panel()], cols=1,
            title="SS-2019-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1、#3；只畫考卷所給條件",
            note="實心版直接擱在上翼板頂，無鋼承板、無托肩；版厚 150 mm",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "誤加鋼承板肋高或托肩；把 H500×200×10×16 的 10、16 對調（tw、tf 讀反）"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
