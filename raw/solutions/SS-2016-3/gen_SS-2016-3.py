#!/usr/bin/env python3
"""
SS-2016-3 矩形板殘餘應力分布 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2016-3.py [輸出目錄]

重繪依據：題目正本 SS-2016-3-problem.md §4 判讀清單（2026-11-02 已確認）。
只重繪圖 1（斷面與殘餘應力分布）；圖 2 為材料應力–應變曲線，屬曲線圖，不重繪。
b、t 為符號，比例示意；三段寬度與應力大小依圖面數值。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2016-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2016-3-problem.md §4，已確認）
# ══════════════════════════════════════════════════════════
B_DRAW, T_DRAW = 3.0, 0.45    # #1 單一實心矩形板，寬 b、厚 t（繪圖比例）
SEG = [("壓", 0.25), ("拉", 0.25), ("壓", 0.25)]   # #2 三段各 b/3；#3 左右 F_y/4 壓、中段 F_y/4 拉，塊狀
SIG_DRAW = 1.6                # F_y/4 對應的繪圖高度


def fig1_problem():
    W, H, sx = 640, 520, 140
    cv = Canvas(W, H, sx=sx, ox=(W - B_DRAW * sx) / 2, oy=185)
    cv.panel("圖 1　斷面與殘餘應力", "b、t 比例示意；基線上方為壓、下方為拉")
    y0 = 1.25
    cv.polygon([(0, y0), (B_DRAW, y0), (B_DRAW, y0 + T_DRAW), (0, y0 + T_DRAW)],
               C["border"], C["member"], 1.8)
    cv.dim((B_DRAW, y0), (B_DRAW, y0 + T_DRAW), "t", off=24, label_off=14)
    cv.dim((0, y0), (B_DRAW, y0), "b", off=18, label_off=14)
    seg = B_DRAW / len(SEG)
    cv.line((-0.15, 0), (B_DRAW + 0.15, 0), C["muted"], 1.4)
    for k, (kind, frac) in enumerate(SEG):
        x0, x1 = k * seg, (k + 1) * seg
        h = SIG_DRAW * frac / 0.25 * 0.38
        y1 = h if kind == "壓" else -h
        col, fill = (C["compr"], C["fill_c"]) if kind == "壓" else (C["tension"], C["fill_t"])
        cv.polygon([(x0, 0), (x1, 0), (x1, y1), (x0, y1)], fill, col, 1.8)
        cv.text(((x0 + x1) / 2, y1 / 2), f"（{kind}）", 12.5, col, dx=18, weight="700")
        cv.math(((x0 + x1) / 2, y1 / 2), "F_{y}/4", 14, col, "end", dx=-4)
        cv.dim((x0, y1 if kind == "拉" else 0), (x1, y1 if kind == "拉" else 0), "b/3",
               off=34 if kind == "拉" else -0, label_off=16)
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2016-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#3；圖 2 應力–應變曲線不重繪",
            note="圖面數值不自平衡：壓力合力為拉力合力的 2 倍（判讀清單 #4）",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把斷面讀成 H 型鋼；把壓、拉段位置對調；忽略圖面數值不自平衡"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
