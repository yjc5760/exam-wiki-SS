# exam-wiki-SS — Claude Code 操作指令（Runbook）

> **適用環境：** Claude Code（終端機執行 `claude`）
> **不適用：** Cowork（解題請用 CLAUDE-SOLVE.md，跨層知識維護直接在 wiki/ 操作）
> **格式與命名規範：** 見 CLAUDE-SPEC.md

---

## 指令索引

| 指令 | 觸發語句 | 用途 |
|------|---------|------|
| [INGEST](#ingest) | `ingest SS-XXXX-N` | 將一道已驗證題目寫入 wiki |
| [COMPILE-ALL](#compile-all) | `compile all` | 從零初始化整個 wiki |
| [QUERY](#query) | 直接提問 | 查詢知識庫 |
| [LINT](#lint) | `lint wiki` | 健檢 wiki 完整性 |
| [STATUS](#status) | `status` | 查看驗證進度與統計 |

---

## INGEST

**觸發語句：** `ingest SS-2015-1`

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

④ Claude Code：
   ingest SS-XXXX-N
   （重新 ingest 讓 wiki 同步更新）
```

---

## COMPILE-ALL

**觸發語句：** `compile all`

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

**觸發語句：** 直接提問

**執行步驟：**
```
1. 讀取 wiki/index.md 定位相關分類
2. 讀取相關 concepts/ methods/ traps/ 頁面
3. 合成答案，附頁面連結與出現題目
4. 【重要】有新洞察 → 存回對應 wiki 頁面（查詢也能累積知識）
```

---

## LINT

**觸發語句：** `lint wiki`

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

**觸發語句：** `status`

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
