#!/usr/bin/env python3
"""
SS-2024-3 RH488×300×11×18 外伸梁強軸／弱軸受集中載重之 LRFD 檢核 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2024-3.py [輸出目錄]

重繪依據：題目正本 SS-2024-3-problem.md §4 判讀清單（待確認）。
圖上每個支承、側撐、載重都對應清單一項；只畫考卷給的東西，不含任何解題結果（不畫彎矩圖、不標 Cb）。
梁跨度與梁深依比例（mm：3 m＋3 m；圖(a) 梁深 488、圖(b) 梁深 300）；左側斷面小圖依比例放大表方位。
示意部分：載重箭頭長度、支承符號大小；C 處豎線照考卷附圖照描（圖(a) 實線、圖(b) 虛線），清單未判讀其意義。
不重繪：題內參考公式（圖片，已照錄於 problem.md §2）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2024-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2024-3-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
X_A, X_C, X_B = 0.0, 3000.0, 6000.0    # #1 A 鉸支、C 滾支（距 A 3 m）、B 外伸自由端（距 C 3 m）
LOAD = "DL=5tf　LL=5tf"                # #1 集中載重在 B（題文 DL = LL = 5 tf）
BRACES = (X_A, X_B)                    # #2 「×」側向及扭轉支撐只在 A、B（上下翼板）；C 無面外束制
D, BF, TW, TF = 488.0, 300.0, 11.0, 18.0   # 題文 RH488×300×11×18（mm）
#                                        #3 圖(a) 強軸（腹板垂直）、圖(b) 弱軸（腹板水平）

PW, PH = 900, 290


def _rect(cv, x0, x1, y0, y1, fill, stroke, w=1.4):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, stroke, w)


def _icon(cv, cx, cy, k, strong):
    """左側斷面方位小圖（model 單位 mm；k = 放大倍數）"""
    if strong:
        parts = ((-BF / 2, BF / 2, D / 2 - TF, D / 2), (-BF / 2, BF / 2, -D / 2, -D / 2 + TF),
                 (-TW / 2, TW / 2, -D / 2 + TF, D / 2 - TF))
    else:   # 腹板水平：翼板直立
        parts = ((D / 2 - TF, D / 2, -BF / 2, BF / 2), (-D / 2, -D / 2 + TF, -BF / 2, BF / 2),
                 (-D / 2 + TF, D / 2 - TF, -TW / 2, TW / 2))
    for xa, xb, ya, yb in parts:
        _rect(cv, cx + xa * k, cx + xb * k, cy + ya * k, cy + yb * k, C["fill_c"], C["member"], 1.2)
    half = (D / 2 if not strong else BF / 2) * k + 120
    cv.line((cx - half, cy), (cx + half, cy), C["muted"], 1.0, dash="8 3 2 3")


def _x(cv, p):
    cv.text(p, "×", 22, C["accent"], weight="700", dy=-1)


def beam_panel(strong):
    sx = 0.092
    cv = Canvas(PW, PH, sx=sx, ox=300, oy=110)
    tag = "圖(a)" if strong else "圖(b)"
    cv.panel(f"{tag}　{'強軸受彎（腹板垂直）' if strong else '弱軸受彎（腹板水平）'}",
             "A 鉸支、C 滾支、B 外伸自由端；支承與載重兩圖相同")
    h = D if strong else BF
    # 梁外形
    _rect(cv, X_A, X_B, 0, h, "none", C["member"], 2.2)
    if strong:
        cv.line((X_A, TF), (X_B, TF), C["member"], 1.0)
        cv.line((X_A, h - TF), (X_B, h - TF), C["member"], 1.0)
        cv.line((X_C, TF), (X_C, h - TF), C["member"], 1.6)
    else:
        for y in (h / 2 - TW / 2, h / 2 + TW / 2):
            cv.line((X_A, y), (X_B, y), C["member"], 1.2, dash="7 4")
        cv.line((X_C, 0), (X_C, h), C["member"], 1.2, dash="5 4")
    # 支承
    cv.support((X_A, 0), "pin", 0, size=14)
    cv.support((X_C, 0), "roller", 0, size=14)
    # 側向及扭轉支撐（A、B 上下翼板）
    for x in BRACES:
        _x(cv, (x, 0)); _x(cv, (x, h))
    # 載重（B 端）
    cv.arrow((X_B, h + 760), (X_B, h + 60), C["load"], 4.0, 13)
    cv.text((X_B, h + 760), "集中載重", 13, C["load"], "end", dx=-12, dy=4)
    cv.text((X_B, h + 760), LOAD, 13, C["load"], "end", dx=-12, dy=22)
    # 點名
    cv.text((X_A, h), "A", 15, C["text"], "end", dx=-12, dy=-14, weight="700")
    cv.text((X_C, h), "C", 15, C["text"], dy=-16, weight="700")
    cv.text((X_B, h), "B", 15, C["text"], "start", dx=12, dy=-14, weight="700")
    # 尺寸
    cv.dim((X_A, 0), (X_C, 0), f"{(X_C - X_A) / 1000:.0f} m", off=52, label_off=14)
    cv.dim((X_C, 0), (X_B, 0), f"{(X_B - X_C) / 1000:.0f} m", off=52, label_off=14)
    # 左側斷面方位
    _icon(cv, -1700, h / 2, 1.4, strong)
    cv.text_px(cv.X(-1700), cv.Y(h / 2) + 52, "RH488×300×11×18", 12, C["muted"])
    if strong:
        cv.text_px(30, 92, "× 側向及扭轉支撐點", 13, C["accent"], "start")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([beam_panel(True), beam_panel(False)], cols=1,
            title="SS-2024-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#3；只畫考卷所給條件",
            note="× 只在 A、B：C 雖為滾支承，但無面外束制，不是側撐點",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把 C 滾支承當成側撐點而把無支長度切成兩段 3 m；強軸、弱軸兩圖的斷面方位對調"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
