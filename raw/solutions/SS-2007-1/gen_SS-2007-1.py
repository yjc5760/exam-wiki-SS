#!/usr/bin/env python3
"""
SS-2007-1 角鋼平衡填角焊設計（ASD）— 題目附圖重繪腳本

用法：
    python3 gen_SS-2007-1.py [輸出目錄]

重繪依據：題目正本 SS-2007-1-problem.md §4 判讀清單（待確認）。
只畫考卷圖一所示：L150×100×15 的 150 mm 肢平貼 15 mm 連接板，三段填角焊（上緣 a、下緣 b、端部 15 cm），
P 作用線距上緣 10 cm。考卷為斜向透視圖，本圖改為正視平面圖（角鋼水平放置）。
肢寬 15 cm、肢背稜線（另一肢厚 1.5 cm）、10 cm 依比例；焊道長 a、b 為所求，長度只示意，不代表答案；
連接板外形與角鋼伸出長度為示意。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "skills", "struct-diagram", "scripts"))

from structdraw import Canvas, C, compose

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"
TAG = "SS-2007-1"

# ══════════════════════════════════════════════════════════
# 判讀清單（SS-2007-1-problem.md §4，待確認）
# ══════════════════════════════════════════════════════════
BL = 15.0           # #1 150 mm 肢平貼連接板（端部橫向焊標 15 cm）
T = 1.5             # 題文 角鋼厚 15 mm（#3 下緣平行線＝另一肢稜線 → b 側為肢背）
EP = 10.0           # #4 由上緣（a 側、趾）量到 P 作用線 10 cm
W = 1.2             # 題文 腳長 1.2 cm（斜線區寬）
#                     #2 三段焊：上緣縱向 a、下緣縱向 b、端部橫向 15 cm
# 示意（所求或考卷未標）：
A_SK, B_SK = 20.0, 34.0     # a、b 長度示意（為所求）
L_ANG = 72.0                # 角鋼畫出長度

PW, PHT = 1000, 560


def _hatched(cv, x0, x1, y0, y1, step=0.75):
    cv.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], C["fill_t"], C["load"], 1.2)
    xa, xb, ya, yb = min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1)
    h = yb - ya
    k = xa - h
    while k < xb:
        p0 = (max(k, xa), ya + max(0, xa - k))
        p1 = (min(k + h, xb), ya + min(h, xb - k))
        if p1[0] > p0[0]:
            cv.line(p0, p1, C["load"], 1.0)
        k += step


def panel():
    sx = 8.0
    cv = Canvas(PW, PHT, sx=sx, ox=215, oy=230)
    cv.panel("角鋼與連接板（平面）", "L 150×100×15，Unit = mm；150 mm 肢平貼連接板")
    # 連接板（不規則外形，示意）
    plate = [(-20, 22), (42, 22), (44, -6), (40, -19), (10, -21), (-14, -19), (-21, -8), (-19, 6)]
    cv.polygon(plate, "rgba(63,74,90,0.08)", C["member"], 1.6)
    cv.text((10, -13), "15 mm-plate", 17, C["text"])
    # 角鋼（150 肢平貼；下緣為肢背，另一肢厚 1.5 cm 的稜線）
    cv.polygon([(0, 0), (L_ANG, 0), (L_ANG, BL), (0, BL)], C["fill_c"], C["member"], 2.2)
    cv.line((0, T), (L_ANG, T), C["member"], 1.4)
    # 焊道（斜線區）
    _hatched(cv, 0, A_SK, BL, BL + W)
    _hatched(cv, 0, B_SK, -W, 0)
    _hatched(cv, -W, 0, -W, BL + W)
    # a、b、15 cm
    cv.dim((0, BL + W), (A_SK, BL + W), "a", off=-26, label_off=-14, size=18)
    cv.dim((0, -W), (B_SK, -W), "b", off=26, label_off=16, size=18)
    cv.dim((-W, 0), (-W, BL), f"{BL:.0f} cm", off=-30, label_off=-36)
    # P 與 10 cm
    yp = BL - EP
    cv.line((L_ANG - 6, yp), (L_ANG, yp), C["load"], 1.0, dash="4 3")
    cv.arrow((L_ANG, yp), (L_ANG + 10, yp), C["load"], 3.2, 12)
    cv.math((L_ANG + 10, yp), "P", 18, C["load"], "start", dx=8, weight="700")
    xd = L_ANG + 4
    cv.line((L_ANG, BL), (xd + 0.6, BL), C["dim"], 1, dash="3 3")
    cv.dim((xd, BL), (xd, yp), f"{EP:.0f} cm", label_off=-30)
    # 標註
    cv.line((L_ANG * 0.55, BL), (L_ANG * 0.55 + 4, BL + 9), C["muted"], 1.1)
    cv.text((L_ANG * 0.55 + 4, BL + 9), "L 150×100×15", 16, C["text"], "start", dx=4)
    cv.line((L_ANG * 0.75, T / 2), (L_ANG * 0.75 + 3, -7), C["muted"], 1.1)
    cv.text((L_ANG * 0.75 + 3, -7), "肢背（另一肢稜線）", 13, C["muted"], "start", dx=4)
    cv.text_px(PW - 24, PHT - 34, "斜線區＝填角焊（腳長 1.2 cm）", 12.5, C["load"], "end")
    return cv


def fig1_problem():
    path = os.path.join(OUT, f"{TAG}-fig-1-problem.svg")
    compose([panel()], cols=1,
            title="SS-2007-1 題目附圖（重繪）",
            sub="依題目正本判讀清單 #1–#4；由斜向透視改為平面正視，a、b 長度為所求（示意）",
            note="10 cm 由趾側（a 側上緣）量到 P，P 距肢背（b 側）只有 5 cm；端部橫向焊 15 cm 也是焊道",
            path=path)
    return path


FIGURES = [
    (fig1_problem, "§1（題目正本 §4）",
     "10 cm 誤當成距肢背，a、b 分配對調；漏算端部橫向焊 15 cm"),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, section, catches in FIGURES:
        print(f"{os.path.basename(fn()):<34} {section:<20} 攔：{catches}")
