#!/usr/bin/env python3
"""
SS-2002-3 中間有弱軸側撐之固接－鉸接柱 — 題目附圖重繪腳本

用法：
    python3 gen_SS-2002-3.py [輸出目錄]

重繪依據：題目正本 SS-2002-3-problem.md §4 判讀清單（2026-11-02 已確認）。
只重繪柱立面與斷面方位；考卷所附「設計 K 值表」屬設計圖表，不重繪。
柱高依比例；斷面僅示意方位（W14×53 尺寸考卷未畫）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2002-3"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2002-3-problem.md §4，已確認）；單位 m
# ══════════════════════════════════════════════════════════
H = 10.0              # #1 柱長 10 m（兩個面皆是）
#                       #2 底部固接；#3 頂端鉸接（側向束制、不可平移）
BR_TOP = 4.0          # #4 中間側撐距頂 4.0 m、距底 6.0 m，只在 X-Z 面
BR_BOT = H - BR_TOP
#                       #5 X-Z 面＝繞弱軸 Y；Y-Z 面＝繞強軸 X，無中間側撐

PW, PH = 330, 520


def _elev(title, sub, brace):
    sx = (PH - 170) / H
    cv = Canvas(PW, PH, sx=sx, ox=PW / 2 + (45 if brace else 0), oy=70)
    cv.panel(title, sub)
    cv.line((0, 0), (0, H), C["member"], 4.5, cap="butt")
    cv.support((0, 0), "fixed", 0, size=22)
    cv.support((0, H), "pin", 90, size=14)            # 側向鉸支（三角形朝右）
    if brace:
        cv.support((0, BR_BOT), "pin", 90, size=14)
        cv.text((0, BR_BOT), "中間側撐", 12.5, C["accent"], "start", dx=34, weight="700")
        cv.dim((0, BR_BOT), (0, H), f"{BR_TOP:.1f} m", off=-62, label_off=-26)
        cv.dim((0, 0), (0, BR_BOT), f"{BR_BOT:.1f} m", off=-62, label_off=-26)
        cv.dim((0, 0), (0, H), f"{H:.1f} m", off=-112, label_off=-28)
    else:
        cv.dim((0, 0), (0, H), f"{H:.1f} m", off=-62, label_off=-28)
    return cv


def _section():
    cv = Canvas(PW, PH, sx=7.0, ox=PW / 2, oy=PH / 2 - 30)
    cv.panel("斷面方位", "W14×53（示意，未依比例）")
    bf, d, tf, tw = 20.0, 30.0, 2.0, 1.2
    for x0, x1, y0, y1 in ((-bf / 2, bf / 2, d / 2 - tf, d / 2),
                           (-bf / 2, bf / 2, -d / 2, -d / 2 + tf),
                           (-tw / 2, tw / 2, -d / 2 + tf, d / 2 - tf)):
        cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], C["fill_c"], C["member"], 1.8)
    cv.line((0, -d / 2 - 4), (0, d / 2 + 6), C["muted"], 1.4, dash="6 4")
    cv.line((-bf / 2 - 4, 0), (bf / 2 + 6, 0), C["muted"], 1.4, dash="6 4")
    cv.math((0, d / 2 + 8), "Y", 16, C["text"], weight="700")
    cv.math((bf / 2 + 8, 0), "X", 16, C["text"], weight="700")
    cv.text_px(PW / 2, PH - 70, "腹板沿 Y 軸、翼板水平", 12.5, C["muted"])
    cv.text_px(PW / 2, PH - 50, "X-Z 面彎曲＝繞弱軸 Y", 12.5, C["muted"])
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([_elev("X-Z 面", "繞弱軸 Y 挫屈", True),
             _elev("Y-Z 面", "繞強軸 X 挫屈", False),
             _section()], cols=3,
            title="SS-2002-3 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#5；設計 K 值表為設計圖表，不重繪",
            note="底部固接、頂端側向鉸支；中間側撐只在 X-Z 面（距頂 4.0 m、距底 6.0 m）",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "把側撐放到強軸方向；側撐位置上下顛倒（4.0／6.0 m）"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    assert BR_BOT == 6.0
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
