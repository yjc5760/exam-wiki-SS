# 結構工程技師考試知識庫 — 鋼結構設計（SS）
# 規格與檢核清單（CLAUDE-SPEC.md）

> 本文件為知識庫的所有「資料格式、命名規則、JSON 欄位、完成標準」唯一依據。
> **Cowork 進行任何新增或修改時，必須遵守本文件的規定。**

---

## 1. 命名規則（全專案適用）

所有資料夾與檔案名稱必須**完全小寫或大寫（依規定），單字間以短橫線（`-`）連接**。

### 1.1 題庫與模組

- 領域（Domain）與學科（Subject）：固定為 `SS`（鋼結構設計）。
- 題號模組（ModuleId）：`SS-YYYY-N`
  - YYYY 為**西元年**（如 2015、2024）。
  - N 為該卷題號（如 1、2、3、4，部分有 5）。
  - 例：`SS-2015-1`

### 1.2 圖檔與補充檔案

- 題目附圖：`SS-YYYY-N-fig-n.png`（由使用者手動截圖）
- 官方設計圖表截圖：`SS-YYYY-N-chart-n.png`
- 參考公式截圖：`SS-YYYY-N-eqn-n.png`
- 手寫補充：`SS-YYYY-N-hand-n.png`
- PDF 補充筆記：`*.pdf`（由使用者放入對應題目資料夾，命名無強制規範）

> **⚠️ 禁止：** 不可使用 `SS-2015-1-fig.png`（必須有後置序號 `-1`）。

### 1.3 互動圖（HTML）

- 由 Cowork 在解析時生成，格式為 `SS-YYYY-N-[內容碼]-viz.html`
- SS 專屬內容碼（由題型決定）：
  - 梁設計/剪力力學：`sfd-bmd`
  - 梁柱桿件（軸力與雙向彎矩）：`pm`
  - 側扭挫屈判斷：`ltb`
  - 柱強度曲線：`column-curve`
  - 接合詳圖：`connection`
- 例：`SS-2018-2-pm-viz.html`

> **⚠️ 禁止：** 不可使用 `SS-2018-2-viz.html` 或 `SS-2018-2-pm.html`。必須有特定的內容碼及 `-viz` 後綴。

### 1.4 Wiki 概念與方法論（由 Cowork 建立）

- 概念頁 ID（ConceptId）：`大寫-大寫.md`
  - 例：`EFFECTIVE-LENGTH-FACTOR.md`、`LATERAL-TORSIONAL-BUCKLING.md`
- 方法論 ID（MethodId）：`小寫-小寫.md`
  - 例：`conjugate-beam.md`、`b1b2-amplification.md`

---

## 2. 原始資料層（`raw/`）規範

### 2.1 JSON 規範

**`raw/json/question_index.json`**（唯一由人工維護/授權 Cowork 更新的檔案）
> 每新增一題解析，必須確保對應條目完整填寫。

```json
{
  "moduleId": "SS-2015-1",         // YYYY 必須為西元
  "year": 2015,
  "number": 1,
  "primaryTopicId": "SS-U1-2",     // 對應 syllabus_taxonomy.json 的子項 ID
  "secondaryTopicIds": ["SS-U2-2"],// 跨考點時填寫（必為陣列）
  "designMethod": "LRFD",          // LRFD / ASD / SD（耐震）/ MM（材力）/ N/A
  "hasSolution": true,             // 只要有 .md 就是 true
  "verificationStatus": "verified",// unverified / needs-review / verified
  "hasHandwritten": false,         // 有無 -hand-*.png
  "hasViz": true,                  // 有無 *-viz.html
  "tags": [                        // 至少 3 個具體考點標籤
    "結實斷面",
    "Cb係數",
    "塑性彎矩"
  ]
}
```

> ⚠️ 注意：所有 YYYY 均為西元。

**`raw/json/concepts.json`**（由 Cowork 生成與維護，供 compile 使用）
```json
{
  "LATERAL-TORSIONAL-BUCKLING": {
    "topicId": "SS-U1-2",
    "name_zh": "側向扭轉挫屈",
    "name_en": "Lateral-Torsional Buckling, LTB",
    "definition": "...",
    "related_concept_ids": ["PLASTIC-MOMENT", "RESIDUAL-STRESS"]
  }
}
```

### 2.2 題目附屬檔案（由 Cowork 或使用者產生）

所有附檔存放在該題資料夾內（`raw/solutions/SS-XXXX-N/`）。

**圖形嵌入要求（在 .md 中）：**

1.  **使用者截圖的 PNG 檔 (`-fig`, `-chart`, `-eqn`, `-hand`)**：
    - 必須提供準確的 alt text 與 `*圖說：...*` 說明（讓 AI 看不到圖也能解題）。
    - 範例：
      ```markdown
      ![SS-2015-1 題目附圖：長度 6m 之簡支梁，受中心集中活載重 PL 及均佈靜載重 qD](SS-2015-1-fig-1.png)

      *圖說：6m 簡支梁，兩端鉸接，跨中受 PL=10t。上方載重為均佈靜載重 2t/m（含自重）。斷面型式為 W400x200x8x13。*
      ```

2.  **使用者補充的 PDF 檔 (`*.pdf`)**：
    - 命名無強制規範（例：`老師解答.pdf` 或 `筆記.pdf`）。
    - 放入資料夾後，不需在 .md 內引用；但需對 Cowork 說 `更新儀表板資料`，儀表板的題卡會自動產生「📎 補充筆記 PDF」按鈕。

3.  **Cowork 生成的互動 HTML 圖 (`*-viz.html`)**：
    - 在 `.md` 中以特定標記顯示連結。
    - 範例：
      ```markdown
      > 📊 互動圖：[梁柱 P-M 互制圖 (SS-2018-2-pm-viz.html)](SS-2018-2-pm-viz.html)
      ```

---

## 3. Wiki 輸出層（`wiki/`）規範

此層檔案除了 `wiki/diagnosis/`、`wiki/failure-modes/`、`wiki/materials/`、`wiki/code-ref/` 與 `wiki/queries/` 之外，其餘均由 `ingest` 或 `compile all` 指令生成。

### 3.1 題解 Markdown 模板（由 ingest 寫入）

> 從 `raw/` 讀入時，Cowork 會在文檔最開頭（H1 之後，正文之前）注入 Meta 區塊。

```markdown
# 考題編號：[SS-XXXX-N]

**主分類：** `SS-U1-2` 梁桿件
**副分類：** 無
**設計法：** LRFD
**標籤：** `LTB` `Cb係數` `非結實斷面`

---
（接續 raw/solutions/SS-XXXX-N/SS-XXXX-N.md 內容）
```

### 3.2 內部連結格式（Wiki 化）

- 概念連結：`[[LATERAL-TORSIONAL-BUCKLING]]`（不帶 .md，大寫大寫-大寫）
- 題目連結：`[[SS-2015-1]]`（大寫）
- 方法論連結：`[[b1b2-amplification]]`（小寫小寫-小寫）
- GitHub 內文跳轉錨點規則：`#小寫英數與短橫線`。
  - 例：跳轉至 `## 2. 考點分析` → `[前往考點](#2-考點分析)`

### 3.3 公式編排與 KaTeX 規範

1.  **公式顯示環境：**
    - 獨立數學式（display mode）必須使用 `$$...$$`，並前後空行。
    - 行內數學式（inline mode）必須使用 `$...$`。
    - 在 Markdown 表格中，不要使用複雜的 display mode。
2.  **上標與下標：** 多字元下標必須加大括號（如 `F_{cr}`，不是 `F_cr`）。
3.  **符號一致性：** 單位使用正體字 `\text{ kN}`，如 `$P = 100 \text{ kN}$`。

### 3.4 變數層次分析（VHA）格式模板

> 在解析檔案的 `## 3.5 變數層次分析 (Variable Hierarchy Analysis)` 必須嚴格遵照以下 Markdown 格式輸出。

```markdown
## 3.5 變數層次分析 (Variable Hierarchy Analysis)
> 複習提示：第一次解題後，在每個卡住的知識點旁標記 `⚠`；第二次複習時只看有 `⚠` 的項目。

### 最終目標
計算梁柱桿件承受雙向彎矩下的 P-M 互制比，判斷是否 ≤ 1.0。

### 本題關鍵公式（依計算順序）
- 1. $A_g = b_f t_f \times 2 + (d - 2t_f)t_w$  (求全斷面積)
- 2. $\lambda_c = \frac{KL}{r\pi}\sqrt{\frac{F_y}{E}}$ (求柱細長比)
- 3. $F_{cr} = 0.658^{\lambda_c^2} F_y$ (求柱壓應力，含 $\boxed{\lambda_c}$)
- 4. $P_n = \boxed{A_g} \times \boxed{F_{cr}}$ (求標稱軸力)

### L1：題目直接給定
_看到題目就能讀出的數字，不需要任何公式。_

| 符號 | 數值 | 說明 |
|:---:|:---|:---|
| $K$ | 1.0 | 兩端鉸接柱有效長度係數 |
| $L$ | 600 cm | 桿件總長 |
| $F_y$ | 2.5 tf/cm² | A36 鋼降伏應力 |
| $E$ | 2040 tf/cm² | 鋼材彈性模數 |

### L2：需知識點推導
_需要知道公式名稱與適用條件，套入 L1 即可算出。_

**第一階段：斷面幾何性質**
| 符號 | 公式／來源 | 卡關? |
|:---:|:---|:---|
| $A_g$ | $b_f t_f \times 2 + (d - 2t_f)t_w$ | |
| $r_y$ | $\sqrt{I_y/A_g}$ | |

**第二階段：柱軸力設計 (LRFD)**
| 符號 | 公式／來源 | 卡關? |
|:---:|:---|:---|
| $\lambda_c$ | $\frac{KL}{r\pi}\sqrt{\frac{F_y}{E}}$ | |
| $F_{cr}$ | 非彈性區挫屈：$0.658^{\lambda_c^2} F_y$ | |

### L3：深層知識（不懂就卡住）

| 知識點 | 說明 | 卡關? |
|:---|:---|:---|
| LTB 判斷條件 | 未知 $L_b$ 時須先檢核 $L_b$ 與 $L_p, L_r$ 關係決定強度 | |
| 強弱軸挫屈控制 | $P_n$ 須取 $x$ 軸與 $y$ 軸挫屈強度的較小值 | |
```

---

## 4. 完成標準清單

### 4.1 Cowork 解完一題後（SOLVE）
- [ ] 存檔為 `raw/solutions/SS-XXXX-N/SS-XXXX-N.md`
- [ ] 標題使用 `H1` 且包含題號 `SS-YYYY-N`
- [ ] 第 3.5 節的 VHA 卡關欄位 `| |` 均留空（供考生自填）
- [ ] VHA 的關鍵公式區段正確使用 `\boxed{}` 標記中繼變數
- [ ] 數學式無純文字的 `Mu`、`Fcr`（皆替換為 `$M_u$`、`$F_{cr}$` 等 LaTeX）
- [ ] （如有）生互動圖 `-viz.html` 且附上正確對應檔名之 Markdown 連結
- [ ] 自動更新 `question_index.json`：hasSolution=true，且填入 3 個以上的標籤
- [ ] 自動填寫 designMethod 與 secondaryTopicIds

### 4.2 ingest 到 Wiki
- [ ] 前置檢查：`verificationStatus === "verified"`
- [ ] `wiki/problems/[id].md` 被建立
- [ ] 對應的 `concepts.json` 條目的相關題目表格已更新
- [ ] `wiki/index.md` 與 `wiki/by-year.md` 已追加此題連結
- [ ] 在 `wiki/log.md` 紀錄此操作
