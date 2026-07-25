# exam-wiki-SS Skills

本目錄收錄與**鋼結構設計（SS）考題知識庫**配套的 Cowork Skills。
安裝後可在 Claude Cowork 中直接呼叫，無需重複貼上指令。

---

## 安裝方式

1. 在 Claude Cowork 中開啟本資料夾（`exam-wiki-SS/`）作為工作資料夾
2. 點擊下方對應的 `.skill` 檔案
3. 點「**Save skill**」即完成安裝
4. 安裝後直接對 Claude 說觸發語句即可使用

---

## Skills 清單

### `vha-treasure-map.skill`

**功能：** 將考題 VHA（變數層次分析）轉化為互動式「藏寶圖」HTML 儀表板

**觸發語句：**
- 「幫 SS-2020-3 做藏寶圖儀表板」
- 「VHA 轉化為儀表板」
- 「VHA dashboard」
- 「把 SS-XXXX-N 的 VHA 做成互動頁面」

**輸出：** `wiki/queries/SS-YYYY-N-treasure-map.html`（自包含 HTML，可直接開啟）

**儀表板功能：**
- KaTeX 數學式渲染（公式不顯示 raw LaTeX）
- 變數以顏色區分：L1 給定（綠）、L2 推導（藍）、本步求解（琥珀框）、最終未知（紅框）
- 知識線索卡片可相互連結，標示陷阱難關
- 自評進度追蹤（掌握 / 卡關 / 待複習）

**前置條件：** 目標題目需有完整的 `raw/solutions/SS-YYYY-N/SS-YYYY-N.md`，且包含 §3.5 VHA 區塊

---

### `unit-lecture.skill`

**功能：** 為某個命題大綱單元產生「理解導向」觀念講義（HTML + 可列印 PDF）

**觸發語句：**
- 「生成 SS-U1-2 講義」
- 「幫我做這單元的觀念講義」
- 「我要在練這單元考題前先懂原理」
- 「不要死記公式的講義」

**輸出：** `study/lecture-XX-Un-m.html` ＋ `study/lecture-XX-Un-m.pdf`

**與既有 `study-XX-Un-m.html` 的分工：**

| | `study-*.html`（既有） | `lecture-*.html`（本 skill） |
|---|---|---|
| 定位 | 速查／複習頁 | 練題**之前**的觀念建立 |
| 內容 | 公式速查、考題清單、統計 | 物理直覺、原理圖解、公式來源 |
| 時機 | 考前總複習 | 第一次接觸該單元 |

兩者並存，互不覆蓋。

**講義結構：** §0 全景對照 → 依標籤分群的主題章節 → 解題決策流程圖 →
歷屆題×觀念對照表 → 陷阱總表 → 自我檢測（摺疊答案）→ ★ 精選 N 題（預設 5 題）

**特色：**
- 每個規範常數都追溯來源（如 `0.6` ← von Mises 的 `1/√3`）
- 以「破壞有沒有預警」統一解釋所有 φ 值與安全係數的差異
- 全內嵌 SVG 圖解 + 本機 KaTeX（`study/assets/katex/`，離線可讀）
- 精選題附覆蓋率分析，並**誠實列出未涵蓋的考點群**
- PDF 走 MathJax→SVG + WeasyPrint（沙盒無 Chromium，此為唯一可行路徑）

**跨科目：** 六科（SS/RC/SA/SD/SM/MM）結構相同，同一份 skill 通用。
使用前請先在 Cowork 開啟目標科目的資料夾。

**前置條件：** 該科需有 `raw/json/question_index.json` 與 `wiki/topics/XX-Un-m.md`

---

## 相關 Skills（已內建於 Cowork，無需另外安裝）

| Skill | 功能 | 觸發語句 |
|-------|------|---------| 
| `vha` | 為解析 .md 加入 §3.5 VHA 區塊 | 「幫 SS-XXXX-N 做 VHA」 |
| `add-to-wiki` | 將知識點新增至六層知識庫 | 「把這個知識點加入知識庫」 |

---

## 新增 Skill 規範

如需新增 skill，請遵守以下格式規範：

### Skill 檔案格式（`.skill` 檔）

```yaml
name: "skill-name"
description: "一句話說明這個 skill 做什麼"
triggers:
  - "觸發語句 1"
  - "觸發語句 2"
instructions: |
  # Skill 指令說明
  
  ## 前置條件
  [列出執行前需滿足的條件]
  
  ## 執行步驟
  [步驟化說明]
  
  ## 輸出
  [說明產生哪些檔案、存放位置]
  
  ## 注意事項
  [邊界條件、常見錯誤]
```

### 加入本清單的步驟

1. 將 `.skill` 檔放入本目錄（`skills/`）
2. 在本 README 的「Skills 清單」補充說明（格式參考 `vha-treasure-map.skill` 的說明方式）
3. 在 `CLAUDE.md` 的 CHANGELOG 追加一行說明此次新增

### 命名規則

| 規則 | 說明 |
|------|------|
| 全小寫連字號 | `vha-treasure-map.skill`，不用底線或大寫 |
| 動詞開頭或名詞主題開頭 | 清楚表達功能，如 `generate-xxx`、`analyze-xxx` |
| 副檔名固定 `.skill` | 不可用 `.md`、`.txt` |

---

## 貢獻

歡迎 PR！新增 skill 請按照上方「新增 Skill 規範」格式操作。

