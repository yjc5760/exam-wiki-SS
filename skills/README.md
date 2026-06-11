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

