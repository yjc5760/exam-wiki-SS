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

## 貢獻

歡迎 PR！新增 skill 請：
1. 將 `.skill` 檔放入本目錄
2. 在本 README 的「Skills 清單」補充說明
