# exam-wiki-SS — 操作指令（Runbook）

> **適用環境：** Cowork（在資料夾 Project 中直接輸入觸發語句）
> **解題流程：** 見 CLAUDE-SOLVE.md
> **格式與命名規範：** 見 CLAUDE-SPEC.md

---

## 指令索引

### 維護類
| 指令 | 觸發語句 | 用途 |
|------|---------|------|
| [INGEST](#ingest) | `ingest SS-XXXX-N` | 將一道已驗證題目寫入 wiki |
| [INGEST-ALL](#ingest-all) | `ingest all` | 批次 ingest 所有 verified 但尚未進 wiki 的題目 |
| [COMPILE-ALL](#compile-all) | `compile all` | 從零初始化整個 wiki |
| [REBUILD](#rebuild) | `rebuild [目錄]` | 重建特定 wiki 目錄（不需跑完整 compile all） |
| [REINDEX](#reindex) | `reindex` | 掃描 raw/solutions/ 修正 question_index.json 不一致 |
| [ADD-CONCEPT](#add-concept) | `add concept [概念名]` | 新增概念到 concepts.json 並建立 wiki 頁面 |
| [LINT](#lint) | `lint wiki` | 健檢 wiki 完整性 |

### 查詢類
| 指令 | 觸發語句 | 用途 |
|------|---------|------|
| [QUERY](#query) | 直接提問 | 查詢知識庫 |
| [STATUS](#status) | `status` | 查看驗證進度與統計 |
| [UNVERIFIED](#unverified) | `unverified` | 列出有解析但尚未 verified 的題目 |
| [CROSS-REF](#cross-ref) | `cross-ref [concept-id]` | 列出所有涉及某概念的題目 |
| [FREQUENCY](#frequency) | `frequency` | 統計各考點歷年出現次數，找出高頻考點 |

---

## INGEST

**觸發語句（在 Cowork 輸入）：** `ingest SS-2015-1`

**前置檢查（強制）：**
```
1. 讀取 raw/json/question_index.json
2. 找到 moduleId = "SS-2015-1" 的條目
3. 檢查 verificationStatus：
   - "verified"     → 繼續執行
   - "unverified"   → 停止，提示：「請人工驗證後將狀態改為 verified」
   - "needs-review" → 停止，提示：「此題標記為需複查，請確認後再 ingest」
```

**執行步驟：**
```
1. 讀取 raw/solutions/SS-XXXX-N/SS-XXXX-N.md
   → 這是解題內容的唯一來源（含題幹、計算、陷阱、進階探討）

2. 讀取 raw/json/question_index.json 中該題的完整條目
   → 取得 primaryTopicId、secondaryTopicIds、designMethod、tags、hasViz

3. 掃描 raw/solutions/SS-XXXX-N/ 下的所有附屬檔案：
   → *-fig-*.png、*-chart-*.png、*-eqn-*.png（靜態截圖）
   → *-hand-*.png（手寫補充）
   → *-sfd-bmd-viz.html、*-pm-viz.html 等（互動圖）

4. 建立或更新 wiki/problems/SS-XXXX-N.md
   → 填入完整標籤資訊（主分類、副分類、設計法、tags）
   → 若有互動圖，加入「圖形」區塊（含相對路徑連結）
   → wiki/problems 頁面格式見 CLAUDE-SPEC.md

5. 從 .md 萃取涉及的概念 → 更新 wiki/concepts/ 相關頁面的「出現題目」表格

6. 從 .md 萃取涉及的陷阱 → 更新 wiki/traps/ 相關頁面的「出現題目」表格

7. 更新 wiki/index.md（主分類和副分類下都加入此題連結）

8. 更新 wiki/by-year.md（對應年份加入此題）

9. 在 wiki/log.md 追加紀錄
```

**錯誤更正流程（已 verified 題目發現錯誤時）：**
```
① Cowork：
   「將 SS-XXXX-N 的 verificationStatus 改為 needs-review」

② Cowork：
   在 raw/solutions/SS-XXXX-N/SS-XXXX-N.md 末尾補充：
   ### 更正說明（YYYY-MM-DD）
   [說明哪裡錯了、正確答案是什麼]

③ 人工重新驗算確認正確後，Cowork：
   「將 SS-XXXX-N 的 verificationStatus 改回 verified」

④ 在 Cowork 輸入：
   ingest SS-XXXX-N
   （重新 ingest 讓 wiki 同步更新）
```

---

## COMPILE-ALL

**觸發語句（在 Cowork 輸入）：** `compile all`

**執行步驟：**
```
1. 讀取 raw/json/concepts.json
   → 為每個 concept_id 生成 wiki/concepts/[id].md
   → 概念頁格式見 CLAUDE-SPEC.md

2. 讀取 raw/json/design_philosophy.json（如存在）
   → 為每個 philosophyId 生成 wiki/philosophy/[id].md

3. 讀取 raw/solutions/methods/ 下所有子目錄
   → 為每個方法論生成 wiki/methods/[method-id].md

4. 讀取 raw/json/question_index.json
   → 只處理 verificationStatus = "verified" 的題目
   → 生成 wiki/problems/[moduleId].md

5. 生成 wiki/index.md（依七層知識架構分類）

6. 生成 wiki/by-year.md（依考年分類，所有題目都列入，
   未驗證的題目加上 ⚠️ 標記）

7. 建立 wiki/queries/（若不存在）
   → 此目錄由 Cowork 直接寫入，compile-all 只負責建立空目錄

8. 【注意】以下五個目錄不由 compile-all 生成，由 Cowork 直接維護，勿覆蓋：
   wiki/diagnosis/ · wiki/failure-modes/ · wiki/materials/ · wiki/code-ref/ · wiki/queries/

9. 在 wiki/log.md 追加 compile-all 紀錄
```

---

## QUERY

**觸發語句（在 Cowork 輸入）：** 直接提問

**執行步驟：**
```
1. 讀取 wiki/index.md 定位相關分類
2. 讀取相關 concepts/ methods/ traps/ 頁面
3. 合成答案，附頁面連結與出現題目
4. 【重要】有新洞察 → 存回對應 wiki 頁面（查詢也能累積知識）
```

---

## LINT

**觸發語句（在 Cowork 輸入）：** `lint wiki`

**檢查項目：**
```
1.  孤立頁面（無任何其他頁面連結）
2.  斷開連結（[[id]] 但對應頁面不存在）
3.  概念缺口（concepts.json 有 related_concept_ids 但頁面未建立）
4.  手寫補充未登錄（raw/solutions/ 有 hand-*.png 但 problems/ 頁面未標注）
5.  圖形未登錄（raw/solutions/ 有 *-viz.html 但 problems/ 頁面無圖形區塊）
6.  圖形遺漏（4.1.3 梁柱桿件題目但無 pm-viz.html）
7.  方法論缺口（raw/solutions/methods/ 有資料夾但 wiki/methods/ 無對應頁面）
8.  圖片圖說缺漏（.md 中有 ![...](*.png) 但下方無 *圖說：* 的題目）
9.  eqn.png 圖說未文字化（有 *-eqn.png 但圖說未包含公式 LaTeX）
10. by-year.md 與 question_index.json 的題目數是否一致
11. 標籤缺口：hasSolution=true 但 tags 少於 3 個的題目
12. queries/ 頁面中的斷開連結（[[id]] 但對應頁面不存在）
13. diagnosis/ 缺口（wiki/index.md 列出的題型但 diagnosis/ 無對應頁面）
14. failure-modes/ 缺口（四大類別頁面是否齊全）
15. materials/ 缺口（四大主題頁面是否齊全）
16. code-ref/ 孤立（index.md 存在但 wiki/index.md 未連結）
17. 輸出待補清單，依優先順序排列
```

---

## STATUS

**觸發語句（在 Cowork 輸入）：** `status`

**輸出格式：**
```
讀取 raw/json/question_index.json，輸出：

驗證進度：X / 98 題
✅ verified (X題)：[列出題號]
⚠️ needs-review (X題)：[列出題號]
❌ unverified (X題)：[依年份分組列出]

solutions/ 已有解析：[列出有資料夾的題目]
尚無解析可 ingest：[verified 但 solutions/ 下無資料夾]

標籤統計（前10常見標籤）：
[標籤] : X 題
```

---

## INGEST-ALL

**觸發語句（在 Cowork 輸入）：** `ingest all`

**執行步驟：**
```
1. 讀取 raw/json/question_index.json
2. 找出所有符合條件的題目：
   verificationStatus = "verified" 且 wiki/problems/[moduleId].md 不存在（或比 .md 舊）
3. 依年份順序逐一執行 INGEST 流程
4. 輸出執行摘要：成功 X 題、跳過 X 題（已存在）、失敗 X 題
5. 在 wiki/log.md 追加 ingest-all 紀錄
```

---

## REBUILD

**觸發語句（在 Cowork 輸入）：** `rebuild concepts` / `rebuild methods` / `rebuild problems` / `rebuild index`

**執行步驟：**
```
依傳入目錄名稱，只重建該目錄：
  rebuild concepts  → 重讀 raw/json/concepts.json，重新生成 wiki/concepts/
  rebuild methods   → 重讀 raw/solutions/methods/，重新生成 wiki/methods/
  rebuild problems  → 重新 ingest 所有 verified 題目（等同 ingest all 但強制覆蓋）
  rebuild index     → 重新生成 wiki/index.md 與 wiki/by-year.md
【注意】diagnosis/ · failure-modes/ · materials/ · code-ref/ · queries/ 不在 rebuild 範圍內
```

---

## REINDEX

**觸發語句（在 Cowork 輸入）：** `reindex`

**執行步驟：**
```
1. 掃描 raw/solutions/ 下所有子資料夾（排除 methods/）
2. 對每個資料夾（如 SS-2015-1/）：
   → 確認 question_index.json 中對應條目的 hasSolution 欄位
   → 若資料夾存在且含 .md 檔案 → hasSolution 應為 true
   → 若資料夾不存在或無 .md → hasSolution 應為 false
   → 發現不一致時修正 question_index.json
3. 輸出修正清單（修正了哪幾題的 hasSolution）
4. 【注意】reindex 只修正 hasSolution，不修改 verificationStatus
```

---

## ADD-CONCEPT

**觸發語句（在 Cowork 輸入）：** `add concept [概念名稱]`
例：`add concept 有效長度係數`

**執行步驟：**
```
1. 確認概念名稱，引導輸入必要欄位：
   → concept_id（全大寫-連字號，如 EFFECTIVE-LENGTH-FACTOR）
   → 知識分類（Part 1.X）
   → 規範來源（如 AISC 360 Chapter E）
   → 定義摘要（1–2 句）
   → 相關概念 ID（related_concept_ids）
2. 將新概念寫入 raw/json/concepts.json
3. 建立 wiki/concepts/[id].md（依 CLAUDE-SPEC.md §7.2 格式）
4. 更新 wiki/concepts/index.md（若存在）
5. 在 wiki/log.md 追加紀錄
```

---

## UNVERIFIED

**觸發語句（在 Cowork 輸入）：** `unverified`

**執行步驟：**
```
讀取 raw/json/question_index.json，輸出：

有解析但尚未 verified 的題目（hasSolution=true 且 verificationStatus≠"verified"）：
  ⚠️ needs-review：[列出題號]
  ❌ unverified：[列出題號，依年份排序]

提示：驗算完成後輸入「將 SS-XXXX-N 的 verificationStatus 改為 verified」
```

---

## CROSS-REF

**觸發語句（在 Cowork 輸入）：** `cross-ref [concept-id]`
例：`cross-ref LATERAL-TORSIONAL-BUCKLING`

**執行步驟：**
```
1. 讀取 wiki/concepts/[id].md 取得概念定義
2. 掃描所有 raw/solutions/SS-XXXX-N/SS-XXXX-N.md，找出提及此概念的題目
3. 同時讀取 question_index.json，交叉比對 tags 欄位
4. 輸出：
   概念：[概念名稱]
   出現題目（X 題）：
   | 題號 | 年份 | 主分類 | 設計法 | 相關程度 |
   |------|------|--------|--------|---------|
   [依相關程度排序]
5. 有新洞察可說「存進知識庫」→ 存為 wiki/queries/cross-ref-[id]-[日期].md
```

---

## FREQUENCY

**觸發語句（在 Cowork 輸入）：** `frequency`

**執行步驟：**
```
讀取 raw/json/question_index.json（所有 98 題），輸出：

一、各主分類出題頻率（topicId）
| 分類 | 名稱 | 題數 | 佔比 | 近5年題數 |
|------|------|------|------|---------|

二、設計法分布
| 設計法 | 題數 | 佔比 |

三、高頻標籤 Top 15
| 標籤 | 出現次數 | 代表題目 |

四、近年趨勢（2020–2025）
[逐年各主分類出題數熱力圖（文字版）]
```
