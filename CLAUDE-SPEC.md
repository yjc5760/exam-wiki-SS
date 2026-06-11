# exam-wiki-SS — 規格與驗證層（Spec）

> **用途：** 所有格式規範、命名規則、完成標準的唯一依據。
> **適用對象：** Cowork（解題與操作指令時參照）、使用者（補圖截圖時參照）
> **本檔取代：** `命名規則參考表.md`（保留供快速瀏覽，以本檔為準）

---

## 目錄

1. [題目編號（moduleId）](#1-moduleid)
2. [考卷 PDF 命名](#2-pdf)
3. [解析資料夾](#3-solution-folder)
4. [解析 .md 主檔格式](#4-solution-md)
   - 4.1 開頭標籤區塊
   - 4.2 數學公式（強制 LaTeX）
   - 4.3 圖片引用規範（雙重保險）
   - 4.4 [變數層次分析（Variable Hierarchy Analysis）](#4-4-vha)
5. [PNG 靜態截圖規範](#5-png)
6. [viz HTML 互動圖規範](#6-viz-html)
7. [Wiki 頁面格式模板](#7-wiki-templates)
8. [標籤分類系統](#8-tags)
9. [question_index.json 欄位規範](#9-json)
10. [完成標準（Definition of Done）](#10-dod)
11. [常見錯誤對照表](#11-errors)

---

<a id="1-moduleid"></a>
## 1　題目編號（moduleId）

```
SS-YYYY-N
```

| 欄位 | 說明 | 規則 |
|------|------|------|
| `SS` | 科目代碼（Steel Structure） | 固定，大寫 |
| `YYYY` | 西元年 | 4 位數，如 `2015` |
| `N` | 該年第幾題 | 阿拉伯數字，無前導零，如 `1`、`2`、`3`、`4`、`5` |

**範例：**

| moduleId | 說明 |
|----------|------|
| `SS-2015-1` | 2015 年第 1 題 |
| `SS-2006-5` | 2006 年第 5 題 |
| `SS-2025-4` | 2025 年第 4 題 |

> 年份用西元（不用民國）。題號從 `1` 起算，無前導零（不可寫成 `SS-2015-01`）。

---

<a id="2-pdf"></a>
## 2　考卷 PDF 命名（`raw/exams/`）

```
SS-YYYY_鋼結構設計.pdf
```

| 欄位 | 說明 |
|------|------|
| `SS-YYYY` | 科目代碼 + 西元年，底線 `_` 隔開後半 |
| `鋼結構設計` | 固定字串，科目全名 |
| `.pdf` | 副檔名，小寫 |

**範例：**
```
SS-2015_鋼結構設計.pdf
SS-2024_鋼結構設計.pdf
命題大綱.pdf              ← 命題大綱（不含年份）
```

> 檔名開頭必須是 `SS-YYYY`，Cowork 的 SOLVE 指令依此定位考卷。

---

<a id="3-solution-folder"></a>
## 3　解析資料夾（`raw/solutions/`）

```
raw/solutions/SS-YYYY-N/
```

每道題目一個資料夾，名稱即 moduleId。方法論另建：

```
raw/solutions/methods/[method-id]/
```

---

<a id="4-solution-md"></a>
## 4　解析 .md 主檔格式

### 4.1 開頭標籤區塊（每份解析必須包含）

```markdown
### 考題編號：SS-YYYY-N

**主分類：** `SS-U1-2` 分類名稱
**副分類：** `SS-U1-4` 分類名稱（無副分類則省略）
**設計法：** LRFD / ASD / 概念題 / 塑性分析 / 混合
**標籤：** `標籤1` `標籤2` `標籤3` ...
```

### 4.2 數學公式（強制 LaTeX）

- 行內：`` $F_y = 2.52 \text{ tf/cm}^2$ ``
- 獨立：`$$P_u = 1.2P_D + 1.6P_L$$`
- **禁止純文字公式**（不可寫 Fy=2520 kgf/cm²）

### 4.3 圖片引用規範（雙重保險原則）

每張圖片在 .md 中必須包含 **alt text + 圖說** 兩部分：

```markdown
![精確描述圖片工程內容的 alt text](SS-YYYY-N-fig-1.png)

*圖說：關鍵數值、條件、結論的完整文字化說明。*
```

**為什麼需要雙重保險：** Cowork 在做 ingest 時以文字為主，若圖片只有空白 alt text，AI 看不到圖片內容，圖片資訊等於消失。必須用文字把關鍵資訊同步記錄下來。

| 圖片類型 | Alt Text 要求 | 圖說要求 |
|---------|-------------|---------|
| `fig`（題目附圖） | 結構型式、跨距、載重位置、支撐條件 | 關鍵幾何數值、側撐點位置、控制參數 |
| `chart`（設計圖表） | 圖表類型、座標軸範圍、圖中曲線條數 | 所有斷面名稱與重量、設計點座標、控制斷面結論 |
| `eqn`（參考公式） | 公式類型與數量 | **所有公式完整以 LaTeX 文字化**（最重要） |
| `hand`（手寫補充） | 方法名稱與推導目標 | 步驟摘要、關鍵中間結果、最終公式 |
| `section`（斷面圖） | 斷面型式、主要尺寸 | 關鍵幾何數值、對稱軸位置 |

**eqn 圖說範例（最重要）：**

```markdown
![SS-XXXX-N參考公式：剪力強度三段式及撓度公式](SS-XXXX-N-eqn-1.png)

*圖說：題目提供的參考公式：*
*【剪力強度 - 三段判斷】*
- *當 $h/t_w \leq 50\sqrt{k_v/F_{yw}}$ 時：$V_n = 0.6 F_{yw} A_w$*
- *當 $50\sqrt{k_v/F_{yw}} < h/t_w \leq 62\sqrt{k_v/F_{yw}}$ 時：$V_n = 0.6 F_{yw} A_w \cdot \frac{50\sqrt{k_v/F_{yw}}}{h/t_w}$*
- *當 $h/t_w > 62\sqrt{k_v/F_{yw}}$ 時：$V_n = \frac{1860 k_v}{(h/t_w)^2} A_w$*
```

<a id="4-4-vha"></a>
### 4.4 變數層次分析（Variable Hierarchy Analysis）

> **目的：** 幫助考生在複習時精確定位「卡在哪裡」，做到針對性補強而非重新看整題。

每道題的解析 .md 中，在 `## 3. 解題戰略地圖` 之後、`## 4. 步驟化詳細計算` 之前，**必須加入一個 `## 3.5 變數層次分析` 區塊**（置於第 3、4 節之間）。

> 編號用 `3.5` 因為 VHA 位於 §3（戰略地圖）之後、§4（詳細計算）之前。

#### 格式模板

```markdown
## 3.5 變數層次分析（Variable Hierarchy Analysis）

> 複習提示：第一次解題後，在每個卡住的知識點旁標記 `⚠`；第二次複習時只看有 `⚠` 的項目。

### 最終目標
`[最終求解目標，如：選最輕合格斷面 → 驗剪力 → 驗撓度]`

### L1：題目直接給定
_看到題目就能讀出的數字，不需要任何公式。_

| 符號 | 數值 | 說明 |
|------|------|------|
| $L$ | 8.4 m | 跨距 |
| $P_D$ | 22 tf | 靜載重 |
| ... | ... | ... |

### L2：需知識點推導
_需要知道公式名稱與適用條件，套入 L1 即可算出。_

**Step 1：[步驟名稱]**

| 符號 | 公式/來源 | 卡關? |
|------|----------|:-----:|
| $P_u$ | $1.2P_D + 1.6P_L$（LRFD 組合） | |
| $M_u$ | $P_u \times L/3$（三分點彎矩） | |

**Step 2：[步驟名稱]**

| 符號 | 公式/來源 | 卡關? |
|------|----------|:-----:|
| $Z_x$ | $b_f t_f(H-t_f) + t_w h_w^2/4$ | |

### L3：深層知識（不懂就卡住）
_L2 中某些公式本身需要背景概念才能正確應用的知識點。_

| 知識點 | 說明 | 卡關? |
|--------|------|:-----:|
| LRFD 載重組合邏輯 | 為何用 1.2D + 1.6L？ | |
| LTB 三段式判斷 | $L_b$ 與 $L_p$、$L_r$ 的比較邏輯 | |
```

#### 層次定義

| 層次 | 定義 | 判斷標準 |
|------|------|---------|
| **L1** | 題目直接給的數字 | 不看任何公式就能讀出 |
| **L2** | 需要套公式推導 | 知道公式名稱 + 套 L1 即可算 |
| **L3** | 深層概念（控制 L2 的應用） | 不懂這個概念就會用錯 L2 公式 |

#### 卡關標記規則

- 解題後，考生對每個 L2/L3 項目自評：能立刻算出 → 空白；需要查表才想起 → `⚠`；完全不知道 → `⚠⚠`
- 複習策略：優先補強 `⚠⚠`，再看 `⚠`，空白項目跳過

#### SOLVE 輸出要求

Cowork 在 SOLVE 時，`## 3.5 變數層次分析` 區塊須包含：
1. 最終目標（一句話）
2. L1 表格（題目所有給定數值，含斷面表、設計圖）
3. L2 表格（按計算步驟分組，每個中間變數一列）
4. L3 表格（從陷阱分析 §3 提取的深層知識點）
5. **卡關欄位留空**（由考生複習時自行填 ⚠）

---

<a id="5-png"></a>
## 5　PNG 靜態截圖規範

### 格式

```
SS-YYYY-N-[類型碼]-[序號].png
```

### 類型碼對照表

| 類型碼 | 內容 | 誰負責 | 範例 |
|--------|------|:------:|------|
| `fig` | 題目附圖（結構示意、幾何圖、接合詳圖） | 使用者 | `SS-2015-1-fig-1.png` |
| `chart` | 設計圖表（φbMn vs Lb、P-M 互制圖靜態截圖） | 使用者 | `SS-2015-1-chart-1.png` |
| `eqn` | 題目提供的參考公式截圖 | 使用者 | `SS-2015-1-eqn-1.png` |
| `hand` | 手寫補充推導 | 使用者 | `SS-2015-1-hand-1.png` |
| `section` | 斷面示意圖（組合斷面幾何） | 使用者 | `SS-2015-1-section-1.png` |

### 命名規則

| 規則 | 說明 |
|------|------|
| 序號從 `1` 起 | 單張也要寫 `-1`，不可省略 |
| 序號代表同類型第幾張 | 與文件出現順序無關 |
| 全部小寫 | 類型碼和副檔名均小寫 |
| 連字號 `-` 分隔 | 不用底線 `_` |

### Glob 查詢模式（供 LINT 使用）

```bash
*-fig-*.png       # 所有題目附圖
*-chart-*.png     # 所有設計圖表截圖
*-eqn-*.png       # 所有公式截圖（LINT 檢查圖說是否文字化）
*-hand-*.png      # 所有手寫補充
```

---

<a id="6-viz-html"></a>
## 6　viz HTML 互動圖規範

### 格式

```
SS-YYYY-N-[內容碼]-viz.html
```

後綴 `-viz` 標示「視覺化互動檔案」，與 PNG 靜態截圖明確區隔。

### 內容碼對照表

| 內容碼 | 說明 | 觸發條件 | 範例 |
|--------|------|---------|------|
| `sfd-bmd` | 剪力圖 + 彎矩圖 | 題目要求「繪製剪力圖/彎矩圖」 | `SS-2015-1-sfd-bmd-viz.html` |
| `pm` | P-M 互制圖 | 梁柱桿件題目（SS-U1-3） | `SS-2022-1-pm-viz.html` |
| `column-curve` | 柱強度曲線（Fcr/Fy vs λc） | 柱強度曲線相關題目 | `SS-2024-1-column-curve-viz.html` |
| `section` | 斷面幾何示意（互動版） | 組合斷面幾何計算題目 | `SS-2015-3-section-viz.html` |
| `connection` | 接合詳圖（互動版） | 接合詳圖說明題目 | `SS-2015-2-connection-viz.html` |
| `ltb` | LTB 側扭挫屈設計曲線 | 梁 LTB 三區段設計題目 | `SS-2025-3-ltb-viz.html` |

### 方法論 HTML（例外命名）

方法論資料夾的 HTML 不加 `-viz`，沿用資料夾名稱：

```
raw/solutions/methods/cb-factor/cb-factor-chart.html
raw/solutions/methods/conjugate-beam/conjugate-beam-chart.html
```

### HTML 規格要求

| 項目 | 規格 |
|------|------|
| 寬度 | 580px |
| 繪圖技術 | Canvas 或 SVG，不依賴外部函式庫 |
| 必須標注 | 關鍵數值、座標軸單位、控制點名稱 |
| 色彩慣例 | SFD 藍色系、BMD 紅色系、控制點綠色 |
| 執行方式 | 直接瀏覽器開啟，無需伺服器 |

### 在解析 .md 中引用互動圖

```markdown
> 📊 **剪力圖與彎矩圖請參閱：** `SS-2015-1-sfd-bmd-viz.html`
```

---

<a id="7-wiki-templates"></a>
## 7　Wiki 頁面格式模板

### 7.1 題目頁：`wiki/problems/SS-YYYY-N.md`

```markdown
# SS-YYYY-N — [一行核心摘要]

**來源：** [examName] · [subject] · [questionNumber]
**考年：** [year]（民國[year-1911]年）
**主分類：** [[SS-U1-2]] [topicName]
**副分類：** [[SS-U1-4]]（無則省略）
**設計法：** LRFD / ASD / 概念題
**標籤：** `標籤1` `標籤2` `標籤3`
**驗證狀態：** ✅ verified

---

## 題幹摘要
## 核心考點
## 解題關鍵步驟
## 用到的公式
## 涉及陷阱

## 圖形（如有）

| 檔案 | 類型 | 內容 |
|------|------|------|
| [SS-XXXX-N-sfd-bmd-viz.html](../../raw/solutions/SS-XXXX-N/SS-XXXX-N-sfd-bmd-viz.html) | HTML 互動 | 剪力圖 + 彎矩圖 |
| [SS-XXXX-N-chart-1.png](../../raw/solutions/SS-XXXX-N/SS-XXXX-N-chart-1.png) | PNG 截圖 | 設計圖表 |

## 手寫補充（如有）
## 相關題目
```

### 7.2 概念頁：`wiki/concepts/[CONCEPT-ID].md`

概念 ID 規則：全大寫英文 + 連字號分隔（如 `LATERAL-TORSIONAL-BUCKLING`）

```markdown
# [概念名稱]

**概念 ID：** [id]
**知識分類：** [Part 1.X]
**規範來源：** [document chapter]

## 定義
## 前置概念
## 相關概念

## 關鍵公式

$$[公式]$$

適用條件：[說明]

## 常見陷阱
## 出現題目（表格）
```

### 7.3 Wiki 各目錄命名規則

| 目錄 | 命名格式 | 範例 |
|------|---------|------|
| `wiki/problems/` | `SS-YYYY-N.md`（= moduleId） | `SS-2015-1.md` |
| `wiki/concepts/` | `全大寫-連字號.md` | `LATERAL-TORSIONAL-BUCKLING.md` |
| `wiki/traps/` | `全大寫-連字號.md` | `HIGH-STRENGTH-STEEL-SLENDER-COLUMN.md` |
| `wiki/methods/` | `全小寫-連字號.md` | `cb-factor.md` |
| `wiki/queries/` | `主題-YYYY-MM-DD.md` | `出題頻率分析-2026-05-26.md` |
| `wiki/philosophy/` | `全小寫-連字號.md` | `lrfd-column.md` |

---

<a id="8-tags"></a>
## 8　標籤分類系統

每道題目有四個分類維度，全部記錄在 `raw/json/question_index.json`：

| 欄位 | 說明 | 範例 |
|------|------|------|
| `primaryTopicId` | 命題大綱主分類（唯一） | `"SS-U1-2"` |
| `primaryTopicName` | 主分類名稱 | `"梁桿件"` |
| `secondaryTopicIds` | 命題大綱副分類（跨主題時用） | `["SS-U1-4"]` |
| `designMethod` | 設計法 | `"LRFD"` / `"ASD"` / `"概念題"` / `"混合"` |
| `tags` | 自由標籤（核心考點，3–8 個） | `["LTB側扭挫屈","剪力強度","使用性撓度"]` |

### 命題大綱分類對照

> 完整六科分類見 `raw/json/syllabus_taxonomy.json`

| topicId   | 分類名稱                  |
|-----------|--------------------------|
| SS-U1-1   | 拉力及壓力桿件             |
| SS-U1-2   | 梁桿件                    |
| SS-U1-3   | 梁柱桿件                  |
| SS-U1-4   | 接合之分析與設計            |
| SS-U2-1   | 塑性分析與設計              |
| SS-U2-2   | 鋼結構材料特性              |
| SS-U2-3   | 設計規範對施工之要求         |
| MM-U1-1   | 斷面性質計算（材力）         |
| SD-U3-1   | 結構耐震設計               |

### 標準標籤詞彙

| 類別 | 標準標籤 |
|------|---------|
| **主題類型** | 壓力桿件、拉力桿件、梁桿件、梁柱桿件、接合設計 |
| **挫屈類型** | LTB側扭挫屈、整體挫屈、局部挫屈、彈性挫屈、非彈性挫屈 |
| **壓力桿件** | 有效長度、K值、殘留應力、切線模數、柱強度曲線、Fcr-λc、λc（無因次細長比） |
| **拉力桿件** | 剪力遲滯、U值、塊狀剪力、有效淨面積、淨截面斷裂 |
| **梁桿件** | 側扭挫屈、Cb係數、結實斷面、塑性彎矩、使用性撓度 |
| **梁柱桿件** | P-M互制公式、B1-B2放大法、二階效應、雙軸彎矩、側移構架 |
| **接合** | 填角銲、高拉力螺栓、E70XX銲條、偏心接合 |
| **設計法** | ASD容許應力設計法、LRFD設計法、塑性分析 |
| **材料** | SN耐震鋼材、降伏比、衝擊韌性、殘留應力 |
| **耐震** | 強柱弱梁、節點域、RBS犬骨接頭、梁柱接頭（耐震） |
| **施工** | 施工規範、焊接細節、NDT、防蝕 |

---

<a id="9-json"></a>
## 9　`question_index.json` 欄位規範

### 各欄位允許值

| 欄位 | 允許值 | 說明 |
|------|--------|------|
| `moduleId` | `SS-YYYY-N` | 題目唯一識別碼 |
| `year` | 整數（如 `114`） | 民國年 |
| `primaryTopicId` | 見第 8 節對照表，格式 `XX-Un-m`（如 `SS-U1-2`） | 命題大綱主分類，唯一 |
| `primaryTopicName` | 見第 8 節對照表 | 主分類名稱 |
| `secondaryTopicIds` | `[]` 或 `["SS-U1-4"]` | 跨主題時填入，可多個 |
| `designMethod` | `LRFD` / `ASD` / `概念題` / `塑性分析` / `混合` | 設計方法 |
| `verificationStatus` | `verified` / `unverified` / `needs-review` | 驗證狀態 |
| `hasSolution` | `true` / `false` | 是否已有解析 `.md` |
| `hasViz` | `true` / `false` | 是否有互動圖 |
| `tags` | 字串陣列（中文，3–8 個） | 核心考點標籤 |

### `verificationStatus` 說明

| 狀態 | 說明 | ingest 是否允許 |
|------|------|:--------------:|
| `verified` | 人工驗算確認正確 | ✅ |
| `unverified` | 尚未驗算 | ❌ |
| `needs-review` | 發現錯誤，待修正 | ❌ |

---

<a id="10-dod"></a>
## 10　完成標準（Definition of Done）

### 一道題「解題完成」的標準

| 項目 | 檢查方式 |
|------|---------|
| `raw/solutions/SS-YYYY-N/SS-YYYY-N.md` 存在 | 檔案系統確認 |
| 開頭標籤區塊完整（編號、主分類、設計法、標籤） | 讀取 .md 前 20 行 |
| 所有獨立公式使用 LaTeX `$$...$$` | grep `\$\$` |
| 每張 PNG 圖片有對應 `*圖說：*` | grep `圖說：` |
| `eqn` 類型圖片的圖說含 LaTeX 公式 | grep `\$` in 圖說區塊 |
| `question_index.json` 中 `hasSolution: true` | JSON 確認 |
| `tags` ≥ 3 個 | JSON 確認 |

### 一道題「ingest 完成」的標準（在 verified 之後）

| 項目 | 檢查方式 |
|------|---------|
| `wiki/problems/SS-YYYY-N.md` 存在且有完整標籤 | 檔案系統確認 |
| `wiki/index.md` 在對應分類下有此題連結 | grep moduleId |
| `wiki/by-year.md` 在對應年份有此題 | grep moduleId |
| 有互動圖時，wiki/problems 頁面有「圖形」區塊 | grep `## 圖形` |
| `wiki/log.md` 有 ingest 紀錄 | grep moduleId |

---

<a id="11-errors"></a>
## 11　常見錯誤對照表

| 類別 | ❌ 錯誤 | ✅ 正確 | 原因 |
|------|--------|--------|------|
| moduleId | `SS-104-1` | `SS-2015-1` | 年份用民國而非西元 |
| moduleId | `SS-2015-01` | `SS-2015-1` | 題號有前導零 |
| moduleId | `ss-2015-1` | `SS-2015-1` | 科目代碼小寫 |
| 考卷 PDF | `SS-2015鋼結構設計.pdf` | `SS-2015_鋼結構設計.pdf` | 年份後缺底線 `_` |
| PNG | `SS-2015-1-fig1.png` | `SS-2015-1-fig-1.png` | 類型碼與序號間缺連字號 |
| PNG | `SS-2015-1-eqn.png` | `SS-2015-1-eqn-1.png` | 缺序號（單張也要寫 `-1`） |
| PNG | `SS-2015-1-hand_1.png` | `SS-2015-1-hand-1.png` | 用底線而非連字號 |
| PNG | `SS-2015-1-FIG-1.png` | `SS-2015-1-fig-1.png` | 類型碼大寫 |
| viz HTML | `SS-2015-1-pm.html` | `SS-2015-1-pm-viz.html` | 缺 `-viz` 後綴 |
| viz HTML | `SS-2015-1-viz-pm.html` | `SS-2015-1-pm-viz.html` | 內容碼與 `-viz` 順序錯誤 |
| concepts | `lateral-torsional-buckling.md` | `LATERAL-TORSIONAL-BUCKLING.md` | 概念頁應全大寫 |
| concepts | `LATERAL_TORSIONAL_BUCKLING.md` | `LATERAL-TORSIONAL-BUCKLING.md` | 用底線而非連字號 |
| methods | `CB-Factor.md` | `cb-factor.md` | 方法論頁應全小寫 |
| designMethod | `lrfd` | `LRFD` | 設計法值大寫 |
| tags | `LTB` | `LTB側扭挫屈` | 標籤應含中文說明 |
| verificationStatus | `Verified` | `verified` | 狀態值全小寫 |
| 公式 | `Fy=2520 kgf/cm²` | `$F_y = 2520 \text{ kgf/cm}^2$` | 禁止純文字公式 |

---

*本規格文件由 CLAUDE.md + 命名規則參考表.md 整合而來。若規則有異動，以本檔為準，並同步更新 CHANGELOG。*
