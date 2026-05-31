# ASD 梁容許彎曲應力 Fb 推導

**Code-Ref ID：** asd-beam-fb-derivation
**對應方法頁：** [[asd-beam]]（`wiki/methods/asd-beam.md`）
**相關概念：** [[LATERAL-TORSIONAL-BUCKLING]] [[BENDING-MODIFICATION-FACTOR-CB]]

---

## 一、公式全覽

ASD（AISC ASD 9th Edition）梁容許彎曲應力 $F_b$ 依受壓翼板側向支撐間距 $L$ 分三段：

### 緊密撐（$L \leq L_c$）

$$\boxed{F_b = 0.66 F_y}$$

### 中等細長（$L_c < L \leq L_u$，使用較大值）

$$\boxed{F_b = \left[0.79 - 0.002\frac{L/r_T}{\sqrt{F_y/C_b}}\right] F_y \cdot C_b}$$

或

$$\boxed{F_b = \left[\frac{2}{3} - \frac{F_y(L/r_T)^2}{10.55 \times 10^6 C_b}\right] F_y \cdot C_b}$$（SI 系統依規範）

### 彈性 LTB（$L > L_u$）

$$\boxed{F_b = \frac{170\,000\,C_b}{(L/r_T)^2}}$$（ksi；SI 系統係數不同）

---

## 二、分界點定義

### $L_c$（緊密撐上限）

$$L_c = \min\left(\frac{200 b_f}{F_y},\ \frac{137900}{(d/A_f)F_y}\right) \text{ (cm, kgf/cm² 制)}$$

- $b_f$：受壓翼板寬度
- $d/A_f$：梁深除以受壓翼板面積

物理意義：$L \leq L_c$ 時，側向扭轉挫屈不控制，梁可達塑性強度 $F_b = 0.66F_y$。

### $L_u$（彈性 LTB 起始點）

$L_u$ 定義為「非彈性 LTB 與彈性 LTB 的分界」，即：

非彈性段上限公式 = 彈性段公式，解出 $L/r_T$。

---

## 三、各段推導邏輯

### 段 1：$F_b = 0.66 F_y$（緊密撐）

- 梁有充分側向支撐，不發生 LTB
- $M_n = M_p = Z_x F_y$（塑性彎矩）
- ASD 安全係數 FS ≈ 1/0.66 ≈ 1.515（取偏保守值）
- $F_b = M_p / (S_x \cdot \text{FS}) \approx \frac{Z_x}{S_x} \cdot \frac{F_y}{1.515}$
- 對 I 型鋼 $Z_x/S_x \approx 1.10 \sim 1.15$，近似得 $F_b \approx 0.66F_y$

### 段 2：非彈性 LTB 段（線性內插）

彈性 LTB 臨界應力（Timoshenko & Gere）：

$$F_{cr} = \frac{\pi}{L/r_T}\sqrt{\frac{E^2 C_b^2}{(L/r_T)^2} + \text{GJ 項}}$$

規範簡化為二次拋物線形式（非彈性段）：

$$F_b = C_b \left[\frac{2F_y}{3} - \frac{F_y^2(L/r_T)^2}{1055\,000\,C_b}\right] \leq 0.60F_y$$

此拋物線在 $L/r_T = 0$ 時給出 $F_b = 0.66F_y$（應與緊密撐段接續），在 $L/r_T = L_u/r_T$ 時與彈性段接續。

> ⚠️ **注意：** 兩個非彈性段公式（大板長式與小板長式）取**較大值**，非較小值。

### 段 3：彈性 LTB 段

純 Euler 型挫屈，忽略 GJ 貢獻（細長梁假設 $J \to 0$）：

$$F_{cr} = \frac{\pi^2 E C_b}{(L/r_T)^2} \times \frac{1}{\pi} \times \text{調整} \approx \frac{170\,000\,C_b}{(L/r_T)^2} \text{ (ksi)}$$

ASD 彈性 LTB 無額外安全係數（已含在係數 170,000 中），等效 FS ≈ 1.67。

---

## 四、$r_T$ 的物理意義

$$r_T = \sqrt{\frac{I_{yr}}{A_r}}$$

- $I_{yr}$：受壓翼板 + 腹板受壓部分 1/3 對 y 軸的慣性矩
- $A_r$：同上截面積

物理意義：$r_T$ 是「等效側向迴轉半徑」，代表梁受壓側對側向挫屈的抵抗能力。寬翼板 → $r_T$ 大 → $L/r_T$ 小 → 較不易 LTB。

---

## 五、$C_b$ 的 ASD 定義

ASD 9th Edition 採用：

$$C_b = \frac{12.5 M_{max}}{2.5 M_{max} + 3 M_A + 4 M_B + 3 M_C}$$

（與 LRFD 相同，見 [[BENDING-MODIFICATION-FACTOR-CB]]）

- 均布荷重梁：$C_b \approx 1.14$
- 懸臂梁（自由端無束制）：$C_b = 1.0$（保守值）
- 純彎曲：$C_b = 1.0$

---

## 六、ASD 與 LRFD 對照

| 項目 | ASD（9th Ed.） | LRFD（360-10） |
|------|--------------|--------------|
| 全側撐 | $F_b = 0.66 F_y$ | $\phi_b M_n = 0.9 M_p$（Mn = Mp） |
| 分界長度 | $L_c$、$L_u$ | $L_p$、$L_r$ |
| 非彈性段 | 拋物線近似 | 線性內插（$M_p \to M_r$） |
| 彈性段 | $170000 C_b/(L/r_T)^2$ | $\phi_b C_b M_{cr}$（含 $S_{xc}$ 等效） |
| 修正係數 | $C_b$（相同公式） | $C_b$（相同） |
| 安全係數 | 隱含在係數中 | 顯式 $\phi_b = 0.90$ |

---

## 七、常見考題應用

| 題型 | 關鍵步驟 |
|------|---------|
| 計算容許彎矩 | ① 算 $L/r_T$ → ② 比較 $L_c$、$L_u$ → ③ 選公式算 $F_b$ → ④ $M_a = F_b S_x$ |
| $C_b$ 應用 | 算各段端點彎矩 M_A, M_B, M_C → 代入公式 |
| ASD vs LRFD 比較 | $F_b \approx \phi_b F_{cr} / 1.5$（近似等效） |

---

## 相關頁面

- [[asd-column]] — ASD 柱設計（與本頁構成 ASD 完整設計對）
- [[ltb-3zone]] — LRFD 三段式 LTB 計算流程
- [[LATERAL-TORSIONAL-BUCKLING]] — LTB 基礎理論
- [[BENDING-MODIFICATION-FACTOR-CB]] — Cb 因子推導
- [[lrfd-phi-values]] — LRFD/ASD 哲學比較
