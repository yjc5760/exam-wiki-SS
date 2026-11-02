#!/usr/bin/env python3
"""
SS-2010-3 四角鋼組合受壓柱 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2010-3.py [輸出目錄]

重繪依據：題目正本 SS-2010-3-problem.md §4 判讀清單（2026-11-02 已確認）與 §2 單角鋼性質。
組合斷面與單角鋼依比例；柱側視僅示意兩端鉸接。不含任何解題結果。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2010-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2010-3-problem.md §4，已確認）；單位 cm
# ══════════════════════════════════════════════════════════
LL, LS, T = 15.0, 10.0, 1.5   # §2 L 15 × 10 × 1.5；#3 長肢 15 垂直、短肢 10 水平
CX, CY = 5.0, 2.53            # #4 c_x 垂直（水平肢外緣至形心）；#5 c_y 水平（垂直肢背至形心）
IX, IY, A1 = 782, 276, 35.3   # §2 單角鋼 I_x、I_y、A（照錄）
OUT_W = 40.0                  # #6、#7 四角配置，外廓 40 × 40 量到角鋼外緣
KL = 25.0                     # #8 有效長度 25 m，兩端鉸接（題文）

PW, PH = 440, 500


def _angle(sx_, sy_):
    """角鋼外緣頂點（heel 在外廓角落），sx_、sy_ = ±1 決定所在象限"""
    h = OUT_W / 2
    pts = [(h, h), (h - LS, h), (h - LS, h - T), (h - T, h - T), (h - T, h - LL), (h, h - LL)]
    return [(sx_ * x, sy_ * y) for x, y in pts]


def side_panel():
    cv = Canvas(PW, PH, sx=1, ox=PW / 2, oy=0)
    cv.panel("柱", "兩端鉸接")
    top, bot = PH - 130, 110
    cv.line((0, bot), (0, top), C["member"], 3, cap="butt")
    cv.support((0, bot), "pin", 0, size=13)
    cv.support((0, top), "pin", 180, size=13)
    cv.arrow((0, top + 70), (0, top + 24), C["load"], 2.6, 10)
    cv.arrow((0, bot - 70), (0, bot - 24), C["load"], 2.6, 10)
    cv.math_px(cv.X(0) + 12, cv.Y((top + bot) / 2), f"KL = {KL:g} m", 13, C["text"], "start")
    return cv


def composite_panel():
    sx = 7.0
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2 - 20, oy=PH / 2 - 10)
    cv.panel("組合斷面", "依比例；虛線為繫板／繫條")
    h = OUT_W / 2
    g = h + 1.2
    cv.poly([(-g, -g), (g, -g), (g, g), (-g, g), (-g, -g)], C["muted"], 1.3, dash="6 4")
    for a in (-1, 1):
        for b in (-1, 1):
            cv.polygon(_angle(a, b), C["fill_c"], C["member"], 1.8)
    cv.circle((0, 0), 0.9, stroke=C["text"], w=1.6)
    cv.line((-0.9, 0), (0.9, 0), C["text"], 1.4)
    cv.line((0, -0.9), (0, 0.9), C["text"], 1.4)
    cv.text((0, 0), "C.G.", 13, C["text"], dy=-18, weight="700")
    cv.dim((h, -h), (h, h), f"{OUT_W:g} cm", off=40, label_off=30)
    cv.dim((-h, -h), (h, -h), f"{OUT_W:g} cm", off=40, label_off=16)
    return cv


def single_panel():
    sx = 11.0
    cv = Canvas(PW, PH, sx=sx, ox=150, oy=PH - 320)
    cv.panel("單角鋼斷面尺寸及性質", "依比例；長肢垂直、短肢水平")
    pts = [(0, 0), (LS, 0), (LS, T), (T, T), (T, LL), (0, LL)]
    cv.polygon(pts, C["fill_c"], C["member"], 1.8)
    cv.line((-2.5, CX), (LS + 2.5, CX), C["muted"], 1.3, dash="8 3 2 3")
    cv.line((CY, -4.5), (CY, LL + 2.0), C["muted"], 1.3, dash="8 3 2 3")
    cv.math((-2.5, CX), "X", 15, C["text"], "end", dx=-4, weight="700")
    cv.math((LS + 2.5, CX), "X", 15, C["text"], "start", dx=4, weight="700")
    cv.math((CY, LL + 2.0), "Y", 15, C["text"], dy=-10, weight="700")
    cv.math((CY, -4.5), "Y", 15, C["text"], "start", dx=8, weight="700")
    cv.circle((CY, CX), 0.45, stroke=C["text"], w=1.5)
    cv.dim((0, 0), (0, CX), "c_{x}", off=-26, label_off=-18, color=C["accent"])
    cv.dim((0, 0), (CY, 0), "c_{y}", off=26, label_off=16, color=C["accent"])
    x0, y0 = 40, PH - 92
    lines = [f"L {LL:g} cm × {LS:g} cm × {T:g} cm",
             f"c_{{x}} = {CX:.1f} cm, c_{{y}} = {CY:.2f} cm",
             f"I_{{x}} = {IX} cm^{{4}}, I_{{y}} = {IY} cm^{{4}}",
             f"A = {A1:g} cm^{{2}}"]
    for k, t in enumerate(lines):
        cv.math_px(x0, y0 + 22 * k, t, 14, C["text"], "start")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    panels = [side_panel(), composite_panel(), single_panel()]
    compose(panels, cols=3,
            title="SS-2010-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #3–#8；只畫考卷所給條件",
            note="cx 為垂直尺寸（對 X 軸）、cy 為水平尺寸（對 Y 軸）；外廓 40 cm 量到角鋼外緣",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "角鋼長短肢方向放錯；c_x、c_y 對應的軸對調；40 cm 當成形心間距"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
