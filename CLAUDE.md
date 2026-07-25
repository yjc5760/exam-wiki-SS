# 結構工程技師考試知識庫 — 鋼結構設計（SS）

> 科目代碼：SS｜資料夾：`exam-wiki-SS`｜其他科目另建獨立資料庫

## 專案說明

本資料庫專門收錄「專門職業及技術人員高等考試結構工程技師」**第四科：鋼結構設計**的考古題解析知識庫。

- **科目代碼：** SS（Steel Structure Design）
- **題目編號格式：** SS-YYYY-N（如 SS-2015-1）
- **其他科目：** 各自建立獨立資料庫（exam-wiki-RC、exam-wiki-SM 等）

**核心工作流程：**
```
在 Cowork 開啟 exam-wiki-SS/ 資料夾（Project）
    ↓
說：「解析 XXXX 年考卷」
Cowork 讀取 CLAUDE.md + 考卷 PDF + question_index.json
  → 建立所有尚無解析的題目資料夾（已有解析者跳過）
  → 提醒你將各題附圖截圖存入對應資料夾
  → 等待你通知「截圖完成，請開始解題」
    ↓
【你做】依提醒截圖存檔，完成後告知 Cowork
    ↓
【重要】Cowork 一次只解一題，解完存檔後再繼續下一題
    ↓
你加入補充截圖（chart/eqn/hand）
請 Cowork 更新 question_index.json（tags、verified）
    ↓
說：「ingest SS-XXXX-N」→ Cowork 直接執行，wiki 自動更新
```

---

## 兩個環境分工

| 環境 | 負責什麼 |
|------|---------|
| **你（使用者）** | PDF 題目附圖截圖（fig-N.png）、chart/eqn/hand 補充截圖、人工驗算後通知 Cowork 更新 verificationStatus |
| **Cowork** | 解題（SOLVE，**一次一題**）、存檔（.md + viz.html）、更新 question_index.json、**所有 wiki 操作指令**（ingest / compile-all / lint / status / reindex / add-concept / add-method / refresh-dashboard / frequency / analyze / predict / study / find / related / unverified / query，共 16 個，詳見 CLAUDE-CODE.md）、直接維護 wiki/diagnosis/ · wiki/failure-modes/ · wiki/materials/ · wiki/code-ref/ · wiki/queries/ · study/（study 指令輸出）、**修正 raw/solutions/methods/ 的公式錯誤**（須驗算＋同步 wiki＋記 log） |

---

## 單向資料流

```
raw/solutions/SS-XXXX-N/SS-XXXX-N.md  ──→  wiki/problems/      （Cowork: ingest）
raw/json/concepts.json                 ──→  wiki/concepts/      （Cowork: compile-all）
raw/solutions/methods/                 ──→  wiki/methods/       （Cowork: compile-all）
   ↑ 修正公式錯誤時改「這一端」，不要只改 wiki 副本（否則下次 compile 會被蓋回）
Cowork 查詢結果                        ──→  wiki/queries/       （Cowork 直接存入）
Cowork study 指令輸出                  ──→  study/              （Cowork 直接存入）
Cowork 跨層知識工具                    ──→  wiki/diagnosis/     （Cowork 直接存入）
                                       ──→  wiki/failure-modes/ （Cowork 直接存入）
                                       ──→  wiki/materials/     （Cowork 直接存入）
                                       ──→  wiki/code-ref/      （Cowork 直接存入）

解題內容唯一來源：raw/solutions/ 下的 .md 檔案
索引資訊唯一來源：raw/json/question_index.json
方法論唯一來源：raw/solutions/methods/（可修正，須驗算＋同步 wiki＋記 log，見規則 1）
wiki/queries/、study/（study 輸出）及四個跨層知識目錄：由 Cowork 直接寫入，不走 ingest 流程
```

---

## 資料夾結構

```
exam-wiki-SS/
├── README.md                        ← 冷啟動快速導覽
├── CLAUDE.md                        ← 本檔（身份層：分工、資料流、重要規則）
├── CLAUDE-SOLVE.md                  ← Cowork 解題 Skill
├── CLAUDE-CODE.md                   ← Cowork 操作指令（Runbook）
├── CLAUDE-SPEC.md                   ← 規格驗證層（格式、命名、完成標準）
├── index.html                       ← 離線儀表板（題庫篩選/統計/進度追蹤/指令速查）
├── dashboard-data.js                ← 儀表板快照（更新儀表板資料 指令重新生成）
│
├── study/                           ← 讀書筆記、講義、study 指令 HTML 輸出
│
├── raw/                             ← 所有原始資料（預設唯讀，僅 ✏️ 兩處可改）
│   ├── exams/                       ← 原始考卷 PDF（命名：SS-YYYY_鋼結構設計.pdf）
│   ├── json/
│   │   ├── concepts.json            ← 概念定義（供 compile-all）
│   │   └── question_index.json      ← ⭐✏️ 題目總索引（唯一需要人工維護的 JSON）
│   └── solutions/                   ← AI 解析 + 補充截圖（每題一個資料夾）
│       ├── SS-YYYY-N/               ← 🔒 證據，不可修改（規則 1、2）
│       │   ├── SS-YYYY-N.md
│       │   ├── SS-YYYY-N-fig-1.png
│       │   ├── SS-YYYY-N-[內容碼]-viz.html
│       │   └── *.pdf                ← 補充筆記（選用，命名無限制）
│       └── methods/                 ← ✏️ 解題方法論（可修正公式／單位，見規則 1）
│
└── wiki/                            ← 知識庫輸出
    ├── index.md                     ← 主導航（七層架構）
    ├── by-year.md                   ← 依考年分類
    ├── log.md                       ← 操作紀錄（append only）
    ├── concepts/                    ← 概念頁         ← Cowork (compile-all)
    ├── methods/                     ← 方法論頁       ← Cowork (compile-all)
    ├── traps/                       ← 陷阱頁         ← Cowork (compile-all)
    ├── problems/                    ← 題目頁         ← Cowork (ingest)
    ├── philosophy/                  ← 設計哲學頁     ← Cowork (compile-all)
    ├── queries/                     ← 查詢結果頁     ← Cowork (直接存入)
    ├── diagnosis/                   ← 題型診斷層     ← Cowork (直接存入)
    ├── failure-modes/               ← 失敗模式層     ← Cowork (直接存入)
    ├── materials/                   ← 材料行為層     ← Cowork (直接存入)
    └── code-ref/                    ← 規範條文對應層 ← Cowork (直接存入)
```

---

## 知識分類骨架（七層）

Wiki 導航依七層知識架構組織（前三層由 Cowork 透過 compile-all/ingest 生成，後四層由 Cowork 直接維護）：

| 層 | 目錄 | 維護者 | 內容 |
|----|------|:------:|------|
| Layer 1 | `concepts/` + `problems/` | Cowork (ingest/compile) | 核心構件設計（拉壓/梁/梁柱/接合） |
| Layer 2 | `philosophy/` | Cowork (compile-all) | 設計哲學與實務（耐震/材料/施工） |
| Layer 3 | `methods/` | Cowork (compile-all) | 解題方法論（共軛梁/虛功/P-M圖） |
| Layer 4 | `diagnosis/` | Cowork (直接存入) | 題型診斷決策樹 |
| Layer 5 | `failure-modes/` | Cowork (直接存入) | 失敗模式（強度/穩定/使用性/接合） |
| Layer 6 | `materials/` | Cowork (直接存入) | 材料行為（應力應變/殘留應力/斷裂韌性/銲接性） |
| Layer 7 | `code-ref/` | Cowork (直接存入) | 規範條文對應（AISC 360/341/AWS D1.1） |

---

## 命題大綱分類（依官方命題大綱）

> topicId 格式：`SS-UN-n` 等，U = 單元號，n = 子項號。
> `primaryTopicId` 填最主要考點；跨子項時用 `secondaryTopicIds` 列出。

### SS 單元：鋼結構設計

| topicId | 命題大綱子項 |
|---------|------------|
| SS-U1-1 | 拉力及壓力桿件 |
| SS-U1-2 | 梁桿件 |
| SS-U1-3 | 梁柱桿件 |
| SS-U1-4 | 接合之分析與設計 |
| SS-U2-1 | 塑性分析與設計 |
| SS-U2-2 | 鋼結構材料特性 |
| SS-U2-3 | 設計規範對施工之要求 |

### 其他相關單元

| topicId | 命題大綱子項 |
|---------|------------|
| MM-U1-1 | 斷面性質計算（材力） |
| SD-U3-1 | 結構耐震設計 |

---

## 重要規則

1. **`raw/` 目錄下所有檔案一律不可修改**，僅以下兩處例外：
   - `raw/json/question_index.json`（索引唯一人工維護處）
   - `raw/solutions/methods/`（方法論文件，可修正公式錯誤與單位標註）

   > **為什麼 methods/ 是例外**：本規則要保護的是**證據**（考卷、AI 解析、驗證過的答案），
   > 這些一旦被改就失去可追溯性。但 `raw/solutions/methods/` 存的是**可維護的知識整理**，
   > 且它是 `wiki/methods/` 的 compile 來源 —— 只改 wiki 副本的話，下次 `compile-all` 會被蓋回舊版。
   > 發現公式或係數錯誤時，必須改 raw 來源才算根治。
   >
   > **修改 methods/ 的三個條件（缺一不可）**：
   > ① 修正前先做**數值驗算**（邊界代入、量綱檢查、與驗證解答交叉比對），不可憑印象改；
   > ② 改完**同步覆蓋** `wiki/methods/` 對應檔；
   > ③ 在 `wiki/log.md` 記錄**改了什麼、為什麼、怎麼驗證的**。
   >
   > ⚠️ `raw/solutions/SS-YYYY-N/`（個別題目解析）**不在例外內**，仍受規則 1 與規則 2 保護。

2. **`verifiedSolution` 是最終答案，不可質疑或重新計算**
3. **`wiki/log.md` 只可 append，不可刪除已有紀錄**
4. **wiki/ 大多數目錄是 compile 輸出，不可手動修改**；例外：diagnosis/ · failure-modes/ · materials/ · code-ref/ · queries/ 由 Cowork 直接維護
5. **ingest 前必須確認 verificationStatus = "verified"**
6. 概念連結使用 `[[concept_id]]`（Obsidian 相容）
7. 每次 ingest 同時更新 index.md 和 by-year.md
8. **格式與命名規範見 CLAUDE-SPEC.md；操作指令（ingest/compile/lint/status 等 16 項）見 CLAUDE-CODE.md，全部由 Cowork 執行**

---

## CHANGELOG

| 日期 | 變更 | 原因 |
|------|------|------|
| 2026-04-06 | 升級 v3：question_index 獨立、by-year.md、單向資料流 | 四項架構優化 |
| 2026-05-27 | 知識庫架構從三層升為七層（diagnosis / failure-modes / materials / code-ref） | 98 題累積後需要更豐富的橫向知識工具 |
| 2026-05-27 | Harness 四層拆分：新建 CLAUDE-CODE.md / CLAUDE-SPEC.md / README.md / GLOSSARY.md | 降低每次 session 的閒置 token，固化執行路徑 |
| 2026-06-11 | 分類代號全面遷移至 `syllabus_taxonomy.json` 的 XX-Un-m 格式；新增 `dashboard.html` | 六科統一分類代號；單頁總覽 98 題全貌 |
| 2026-06-12 | GitHub Pages 部署：新增 `index.html`（導向儀表板）與 `.nojekyll` | 知識庫以靜態網站佈署至 GitHub Pages |
| 2026-07-02 | 參考 RC 知識庫進行全文件升級，導入 16 項指令工作流、儀表板 `index.html` 整合、補充筆記 PDF 支援、以及 `study` 複習講義功能 | 統一 SS 與 RC 的文件架構，提升使用體驗與分析能力 |
| 2026-07-25 | 新增 `skills/unit-lecture.skill`（單元觀念講義產生器，六科通用）；新增 `study/lecture-SS-U1-1.html` / `.pdf` 與共用的 `study/assets/katex/` | 建立「練題前先建立物理直覺」的教材類型，與既有 `study-*.html` 速查頁分工 |
| 2026-07-25 | 新增 `study/lecture-SS-U1-2.html` / `.pdf`；新增 `study/problems-view/`（raw/solutions 的 HTML 渲染層，題號連結改指此處） | 題號原本連到 `.md`，瀏覽器只顯示未渲染純文字；渲染層讓公式／表格／附圖可讀 |
| 2026-07-25 | 新增 `study/lecture-SS-U1-3.html` / `.pdf`（梁柱桿件，30 頁）；`study/problems-view/` 補齊 SS-U1-3 全 12 題渲染頁；`study-SS-U1-3.html` 加入三顆教材互連按鈕 | 六子項中最後一個缺講義、且與 U1-1／U1-2 相依最深的單元 |
| 2026-07-25 | 新增 `study/lecture-SS-U1-4.html` / `.pdf`（接合之分析與設計，33 頁）；`study/problems-view/` 補齊 SS-U1-4 全 26 題渲染頁；`study-SS-U1-4.html` 加入三顆教材互連按鈕 | SS 最大單元（26 題）補上「練題前建立物理直覺」的教材 |
| 2026-07-25 | **規則 1 例外擴充**：`raw/` 唯讀的例外從「`question_index.json`」擴充為「`question_index.json` + `raw/solutions/methods/`」，並訂出三項修改條件（驗算／同步 wiki／記 log） | `methods/` 是 `wiki/methods/` 的 compile 來源，只改 wiki 副本會被 `compile-all` 蓋回；公式勘誤需能根治。個別題目解析 `raw/solutions/SS-YYYY-N/` 仍受完整保護 |

---

## 目前收錄狀況

> 此處不維護靜態數字（容易過時）。執行 `status` 指令可取得最新的驗證進度、解析題目數、標籤統計。
>
> 總題數：**98 題**（2002–2025 年）
