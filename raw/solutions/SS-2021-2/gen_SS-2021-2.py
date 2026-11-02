#!/usr/bin/env python3
"""
SS-2021-2 填角銲疊接拉力構材之斷裂與塊狀剪力模式 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2021-2.py [輸出目錄]

重繪依據：題目正本 SS-2021-2-problem.md §4 判讀清單（2026-11-02 已確認）。
只畫考卷給的東西；不畫破壞模式（那是本題所求）。節點板外形為示意，受拉板寬與疊接長依比例。單位 mm。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2021-2"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2021-2-problem.md §4，已確認）；單位 mm
# ══════════════════════════════════════════════════════════
T_PL, T_GU = 20, 25        # #1 t = 20 mm 受拉板（右端受 P）；t = 25 mm 梯形節點板（左端承接）
W_PL = 100.0               # #2 受拉板寬 100
L_OV = 150.0               # #3 疊接長＝縱向銲道長 150 mm
RET = 8.0                  # #4 板端兩角短回銲（長度示意）；板端無橫向銲


def fig1_problem():
    W, H, sx = 760, 470, 1.15
    cv = Canvas(W, H, sx=sx, ox=300, oy=H / 2 - 30)
    cv.panel("圖二　疊接", "節點板外形示意；受拉板寬與疊接長依比例")
    gu = [(-130, -150), (-130, 150), (L_OV, 85), (L_OV, -85)]
    cv.polygon(gu, C["border"], C["member"], 1.8)
    pl = [(0, -W_PL / 2), (L_OV + 120, -W_PL / 2), (L_OV + 120, W_PL / 2), (0, W_PL / 2)]
    cv.polygon(pl, C["fill_c"], C["member"], 1.8)
    cv.line((L_OV, -W_PL / 2), (L_OV, W_PL / 2), C["member"], 1.4, dash="6 4")   # 節點板右緣（被遮）
    for y in (-W_PL / 2, W_PL / 2):
        cv.line((0, y), (L_OV, y), C["load"], 5, cap="butt")                     # 縱向填角銲
        cv.line((0, y), (0, y - RET * (1 if y > 0 else -1)), C["load"], 5, cap="butt")  # 回銲
    cv.arrow((L_OV + 125, 0), (L_OV + 185, 0), C["load"], 3.2, 12)
    cv.math((L_OV + 185, 0), "P", 16, C["load"], "start", dx=8, weight="700")
    cv.arrow((-135, 0), (-195, 0), C["load"], 3.2, 12)
    cv.text((-60, 85), f"t={T_GU} mm", 13, C["text"], weight="700")
    cv.text((75, 0), f"t={T_PL} mm", 13, C["text"], weight="700")
    cv.dim((0, -W_PL / 2), (0, W_PL / 2), f"{W_PL:.0f}", off=-28, label_off=-18)
    cv.dim((0, -W_PL / 2), (L_OV, -W_PL / 2), f"{L_OV:.0f} mm", off=34, label_off=16)
    cv.text((L_OV / 2, W_PL / 2), "縱向填角銲（兩道）", 12.5, C["load"], dy=-14, weight="700")
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([cv], title="SS-2021-2 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#4；只畫考卷所給條件（破壞模式為本題所求，不畫）",
            note="銲道只沿受拉板上下兩緣（長 150 mm），板端只有兩角短回銲、無橫向銲",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把板端當成有橫向銲；把 t = 20、25 mm 的板對調"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
