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

1. **`raw/` 目錄下所有檔案一律不可修改**，僅以下三處例外：
   - `raw/json/question_index.json`（索引唯一人工維護處）
   - `raw/solutions/methods/`（方法論文件，可修正公式錯誤與單位標註）
   - `raw/solutions/SS-YYYY-N/SS-YYYY-N.md`（**個別題目解析，僅限「解析勘誤」**，見下方條件）

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
   > **為什麼「解析勘誤」是例外**：本規則要保護的是**可追溯性**，不是保護錯誤。
   > `raw/solutions/SS-YYYY-N/SS-YYYY-N.md` 是解題內容的**唯一正本**，
   > `wiki/problems/` 與 `study/problems-view/` 都由它生成 —— 只改下游副本，
   > 下次 `ingest` 會被蓋回錯誤版本，等於錯誤永久留存。
   >
   > ⚠️ **教訓（2026-07-30）**：該次 VERIFY 已查出 `SS-2013-2.md` 的 π²EIc 量級筆誤，
   > 卻因本規則舊條文「不在例外內」而**不敢修，只在 log 記一筆**。
   > 該檔後續（2026-08-22）被查出更嚴重的觀念錯誤（把考卷原文「柱 CD 為**靠桿**」讀成「鉸接」，
   > 挫屈載重高估約 3 倍）。**規則不該讓已知錯誤留在正本裡。**
   >
   > **修改 `SS-YYYY-N.md` 的四個條件（缺一不可）**：
   > ① **回考卷原文**：以 `raw/exams/` 的 PDF 為準重新判讀題意與圖說。
   >    ⚠️ 本科考卷為 Adobe-CNS1 CID 字型，`pdftotext` **抽不到中文**，且支承符號、鉸接圓圈、
   >    尺寸線只能目視 —— 必須轉圖（300–450 dpi）**逐頁目視判讀**，不可只靠文字抽取；
   > ② **數值獨立重算**：每個數字以程式重算，並做量綱檢查與雙路徑交叉驗算，不可憑印象改；
   > ③ **同步全部下游**：`wiki/problems/`、`study/problems-view/`、該題 `*-viz.html`、
   >    `raw/json/question_index.json`（tags）、必要時 `dashboard-data.js` 與 `study/study-*.html`；
   > ④ 在 `wiki/log.md` 記錄**改了什麼、為什麼錯、怎麼驗證的**，並在 .md 頁尾加「修正日期」。
   >
   > **不在例外內（仍完整受保護）**：`raw/exams/`（考卷原件）、同資料夾的
   > `-fig-*.png`／`-chart-*.png`／`-eqn-*.png`／`-hand-*.png`（使用者截圖證據）、
   > 使用者放入的補充筆記 `*.pdf`。勘誤只准動 `.md` 正本與 Cowork 自己生成的 `*-viz.html`。
   >
   > **驗證狀態連動**：解析一經勘誤，該題 `verificationStatus` 必須退回 `unverified`，
   > 由使用者人工複核後才可改回 `verified`（規則 5）。

2. **`verifiedSolution` 是最終答案，不可質疑或重新計算**
   > 界線：本條保護的是**已人工驗算確認**（`verificationStatus = "verified"`）的答案。
   > 當使用者明示要求勘誤、或該題已退回 `unverified` 時，本條不阻止重新計算。
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
| 2026-07-26 | 新增 `study/lecture-SS-U2-3.html` / `.pdf`（設計規範對施工之要求，26 頁）；`study/problems-view/` 補齊該單元全 13 題（主 7 + 副 6）渲染頁；`study-SS-U2-3.html` 加入三顆教材互連按鈕 | 第二單元首份講義；本單元全為說明題，需要「三道防線（事前／事中／事後）」的答題骨架與機制解釋，而非條文背誦 |
| 2026-07-30 | 新增 `study/lecture-VHA-7題觀念講義.html` / `.pdf`（51 頁，7 章）：由 7 題的 §3.5 VHA（主要公式／L2／L3）重組為理解導向觀念講義，含 7 則完整手算範例與七章 L3 卡關清單 | VHA 原本是「解題後定位卡關點」的診斷工具，缺少「把卡關點一次補起來」的教材；本檔把跨題的 L3 深層知識串成一條可理解的觀念鏈 |
| 2026-08-07 | 新增 `study/formula-given-SS-U1-1.html` / `.pdf`（U1-1 主要公式「考卷會給 vs. 必須自己背」逐條分界，30 條公式 × 24 年考卷證據）；新增 `skills/unit-formula-map/`（六科通用）與 `skills/unit-formula-map.skill`，附 `scripts/` 四支 PDF 產線腳本 | `study-*`（速查）與 `lecture-*`（觀念）都沒回答「這條公式要不要花時間背」；此判斷需以考卷原文為證據，且掃描影像頁必須目視判讀（SS 有 102、105、112、113 四年公式全為影像），不宜每次重推流程 |
| 2026-08-07 | 新增 `study/formula-given-SS-U1-2.html` / `.pdf`（U1-2 梁桿件，33 條公式 × 25 題 × 24 年考卷證據，12 頁）；`study-SS-U1-2.html`、`lecture-SS-U1-2.html` 加入互連按鈕，`formula-given-SS-U1-1/-4.html` 補上互連 | U1-2 是題數最多（25 題）的單元，判定結論與 U1-1／U1-4 相反：LTB 的長式子幾乎必給（`Lp`/`Lr` 十一年、`Cb` 十年、`Mn`/`Mcr` 七年），但 `Mp = FyZx`／`My = FySx` 24 年一次都沒印過、`φb = 0.9` 只印過兩次。另發現 113 年第三題的整組 LTB 公式（`Lp`、`Lr`、`X1`、`X2`、`J`、`FL`、`Mr`、`Mn`、`Mcr`）以圖片嵌入，`pdftotext` 只抽到「參考公式：」四字，不目視會把該年誤判成零公式年 |
| 2026-08-07 | 新增 `study/formula-given-SS-U1-4.html` / `.pdf`（U1-4 接合之分析與設計，37 條公式 × 26 題 × 24 年考卷證據，12 頁）；`study-SS-U1-4.html`、`lecture-SS-U1-4.html`、`formula-given-SS-U1-1.html` 三處加入互連按鈕 | U1-4 是 26 題的最大單元，且是六個子項裡「公式最不給」的一個：偏心接合考過 4 次（91/93/94/106）四次全零公式、95 與 98 年整張零公式而兩年都有 U1-4 題。判定過程中另發現 113 年的「最小銲腳尺寸表」以圖片嵌入，`pdftotext` 完全抽不到，必須轉圖目視 |
| 2026-08-08 | 新增 `study/formula-given-SS-U1-3.html` / `.pdf`（U1-3 梁柱桿件，40 條公式 × 12 題 × 24 年考卷證據，16 頁）；`study-SS-U1-3.html`、`lecture-SS-U1-3.html` 及 `formula-given-SS-U1-1/-2/-4.html` 加入互連按鈕 | U1-3 的判定結論是「ASD 幾乎必給、LRFD 必漏一半」：六個 ASD 梁柱年（92/93/96/97/100/108）互制三式全給，但 111 年整題雙軸彎矩梁柱卻零 P-M 互制式、98 年要畫 P-M 曲線也零公式。最關鍵的發現是 **`Mu = B1·Mnt + B2·Mlt` 24 年零次印出**，而 102 年題目字面就在要 `Mu`、`B1`、`B2`、`Mnt`、`Mlt`（四個零件全給、唯獨不給組合式）。另修正流程風險：109 年第 3 頁參考資料**整區為影像**，`pdftotext` 只抽到「= ，= exp−0.419∙」，不目視會把 LRFD 給得最完整的一年誤判成零公式年 |
| 2026-08-08 | 新增 `study/formula-given-SS-U2-3.html` / `.pdf`（U2-3 設計規範對施工之要求，38 條規定 × 13 題 × 24 年考卷證據，15 頁）；`study-SS-U2-3.html`、`lecture-SS-U2-3.html` 加入互連按鈕 | U2-3 是六個子項裡唯一「**通常會給」為零條**的單元：38 條規定中 34 條 24 年零次印出，僅有的 4 條例外（`s≥3d`、`Le≥1.5d`、孔徑 `db+3` mm、最小銲腳尺寸表）全是別題順帶印出、本單元用不到。因 13 題全為說明題，本頁改以「規定＝數字＋判定規則＋答題骨架」四類盤點（含 `tz≥(dz+wz)/90`、`T0=0.70FuAb`、鍍層 `≥85 μm`、板厚 `≥40 mm` 用 SN-C 等 15 個關鍵數字）。另修正 U1-4 那輪對 113 年「最小銲腳尺寸表」的記錄：本輪轉圖目視確認實際級距為 `t≤6→3`／`6<t≤12→5`／`12<t≤19→6`／`19<t≤38→8` mm |
| 2026-08-08 | 新增 `skills/unit-exam-intel/`（六科通用「單元命題情報頁」產生器）與 `skills/unit-exam-intel.skill`，附 `scripts/stats.py`（統計）、`scripts/verify.py`（對帳）、`reference/template.html`（頁面骨架）；`skills/README.md` 補上說明 | 將 `study-SS-U1-1.html` 的重構做法固化為可重複流程。核心設計是「頁面上每個數字都必須由程式算出」——`stats.py` 從 `question_index.json` 算 KPI／排名／空窗年段／前後對切／設計法分布，`verify.py` 反向對帳 `Q[]` 題號集合、主副旗標、篩選鈕數字、KPI、題號連結與禁用寫法。此規則來自實際教訓：舊頁「近 6 年 6/6」實為 4/6、「共 7 題」實為 6 題（本輪由 `stats.py` 揪出並更正）。已考慮六科差異：無 `designMethod` 欄位的科目（SA、MM 等）改用其他軸線，主考點 < 8 題時跳過漂移分析 |
| 2026-08-08 | 重構 `study/study-SS-U1-1.html`：由七區段「深度複習頁」改為只留 ① 命題分析的**命題情報頁**（刪除截面圖解／解題流程圖／公式速查／高頻陷阱／柱強度計算器，因分別與 `lecture-SS-U1-1.html` §1.1·§4.2·§8.1·§9·§11 及 `formula-given-SS-U1-1.html` §二重複）；① 擴充為 1.1 出題概況／1.2 考點結構／1.3 考點漂移／1.4 ASD·LRFD 走向／1.5 考題清單（主 24＋副 7＝31 題）／1.6 命題風險排序 | 三份教材重疊嚴重，重新分工為 lecture＝為什麼、formula-given＝要不要背、study＝考什麼（可由 `question_index.json` 重生的命題事實）。同輪修正三處資料錯誤：KPI「近 6 年 6/6」實為 4/6（2019–2021 三年空白）、清單漏列 7 題副考點、題號仍連舊式 `../index.html#md=` 未渲染路徑（改指 `problems-view/`） |
| 2026-08-08 | 正名第三輪：五份 `formula-given-SS-*.html` 的 `<nav>` 整段重建——「▶ Un-m 深度複習」改為「▶ Un-m 命題分析」、指向其他單元的按鈕由只寫代號（「▶ U1-1」）統一為「▶ Un-m 給／背分界」、按鈕順序固定為「頁內錨點 → 同單元講義 → 同單元命題分析 → 其他四單元給／背分界 → 本頁 PDF」共 11 顆；規格回寫 `skills/unit-formula-map/SKILL.md`「導覽列」節（附完整範例與三條硬規則） | 五檔原本有三種不同寫法，且 U1-1／U1-2／U1-4 的「本頁 PDF」卡在中間、後面又接兩顆同類按鈕——成因是過去分批追加時直接 append 到 `</nav>` 前。SKILL.md 原本只有一句「放 lecture、study 的互連按鈕」，規格過鬆才會長出三種寫法 |
| 2026-08-08 | 正名第二輪：把用語修正推到所有設定檔與 skill 原始碼——`skills/unit-lecture/SKILL.md`「教材互連」整節重寫（三顆按鈕、刪 Keynote、加兩則明文禁令）、`CLAUDE-CODE.md` STUDY 節加註「子項層級已改由 `unit-exam-intel` 負責」並修掉舊式 `../index.html#md=` 連結指示、`CLAUDE-SPEC.md` 檔名前綴表補 `formula-given-`、`skills/README.md`／`知識庫使用說明書.md`／`檔案架構索引表.md` 分工敘述同步；三個 `.skill` 重新打包 | 只改 HTML 不改 skill 的話，下次產講義又會照舊規格放 Keynote 按鈕。同輪抓到 `CLAUDE-CODE.md` 殘留一條與 `verify.py` 第 6 項牴觸的指示（要求題號連 `../index.html#md=`），若未修，單元層級 `study` 指令會再度產出未渲染的連結。⚠️ 已安裝版 skill 需由使用者自行安裝重新打包的 `.skill` 才會生效 |
| 2026-08-08 | 全站正名：「速查頁」→「命題分析」，並移除 Keynote 按鈕。五份 `lecture-SS-*.html` 按鈕列統一為「命題分析／給／背分界／本頁 PDF」三顆（U1-1、U1-3、U2-3 補上給／背分界）；`study/problems-view/` 全 88 頁的按鈕文字、title 與「跟隨來源單元」腳本內字串同步更新 | `study-SS-*.html` 五個單元已全部重構為命題情報頁，「速查頁」是重構前七區段深度複習頁的舊名，名實不符；Keynote 指向的課堂投影片與三份教材分工重疊。同輪修掉 `lecture-SS-U1-3.html` 與 `lecture-SS-U2-3.html` 各有兩顆未套樣式且互相指錯單元的殘留 `▶ 給／背分界` 連結 |
| 2026-08-08 | 重構 `study/study-SS-U1-3.html`：以 `unit-exam-intel` 改為命題情報頁（刪除 P–M 圖解／解題流程圖／公式速查／高頻陷阱／H1 互制計算器）；考點分四群（ASD 互制三式 5、LRFD H1 互制 3、二階效應放大 2、規範層次延伸 2），清單主 11 ＋副 1 ＝ 12 題。**SS 六子項已有五個改為命題情報頁** | U1-3 是全科 ASD／LRFD 分界最乾淨的單元：前段（2003–2011）LRFD 掛零、ASD 4 題，後段（2012–2022）LRFD 5 題、ASD 僅 2019-3 一題。本輪由 `stats.py` 得出的關鍵事實是 **B1／B2 二階放大已空窗 11 年**（2013-4、2014-4 連兩年後再無），而該環節的 `Mu=B1·Mnt+B2·Mlt` 24 年零次印出，屬「空窗最久＋最不給公式」的雙重風險。分群亦修正舊頁的「直接分析法（1題）」違反每群至少 2 題，改與副考點 SS-2009-1 合併為「規範層次的延伸」；舊頁未列副考點（僅 11 題），本輪補為 12 題 |
| 2026-08-08 | 重構 `study/study-SS-U2-3.html`：以 `unit-exam-intel` 改為命題情報頁（刪除主題地圖／答題 SOP／知識卡速查／高頻陷阱／快問快答翻卡）；考點分五群（防蝕塗裝 3、銲接施工與瑕疵 3、耐震加嚴 3、NDT 2、螺栓施工 2），清單主 7 ＋副 6 ＝ 13 題 | U2-3 觸發 skill 的兩處例外處理：主考點僅 7 題（< 8）故**跳過考點漂移區塊**，趨勢改以一行註腳描述；13 題 designMethod 全為「概念題」故**設計法表改軸線**為「現身形式」（主考點／副考點掛 U1-4／副考點掛其他），由此揭出舊頁未呈現的事實——近 6 考年副考點 3 題多過主考點 2 題，且 2014 年後副考點全部集中掛在 U1-4 接合 |
| 2026-08-08 | 重構 `study/study-SS-U1-2.html`：以 `unit-exam-intel` 改為命題情報頁（刪除 Mn–Lb 圖解／解題流程圖／公式速查／高頻陷阱／LTB 計算器）；考點分五群（LTB 三區段 11、斷面分類／Mp 6、斷面選擇／撓度 2、合成梁／SRC 2、腹板剪力／剪力流 4），清單主 21 ＋副 4 ＝ 25 題 | U1-2 是全科出現率最高的單元（17/24 考年），但 21 題主考點裡 11 題是 LTB（52%），集中度全科第一。本輪由 `stats.py` 得出三項舊頁未呈現的事實：斷面分類／Mp 自 2023 起連三年出現（升溫最快）、腹板剪力主考點空窗 19 年、ASD 自 2016-1 後連續 6 個考年零出現。分群準則亦調整——SS-2015-1 由 LTB 群改列「斷面選擇與使用性檢核」群（每題只歸最主要解題套路），故 LTB 由舊頁的 12 題變為 11 題 |
| 2026-08-08 | 重構 `study/study-SS-U1-4.html`：以 `unit-exam-intel` 由七區段深度複習頁改為命題情報頁（刪除接合圖解／解題流程圖／公式速查／高頻陷阱／填角銲計算器，分別與 `lecture-SS-U1-4.html` §1–§7·§10·§12 及 `formula-given-SS-U1-4.html` §二重複）；擴充為六區塊，考點分五群（螺栓／接合端 10、偏心接合 5、銲接強度 2、梁柱接頭 4、機制概念 5），清單主 19 ＋副 7 ＝ 26 題 | U1-4 是最大單元卻與另兩份教材大量重疊；重構同時由 `verify.py` 揪出 `question_index.json` 中 2006 年四題（SS-2006-1/-2/-4/-5）designMethod 全被誤填為 LRFD，實為概念題，已修正（連帶 U1-4 設計法分布由 ASD5／LRFD10／概念4 更正為 ASD5／LRFD8／概念6） |
| 2026-08-09 | 新增 `study/` 四支公式記憶片（各 pptx + pdf + `旁白稿_SS-*.md`）：`SS-U1-2_梁桿件`（35 頁）、`SS-U1-3_梁柱桿件`（37 頁）、`SS-U1-4_接合之分析與設計`（40 頁）、`SS-U2-3_設計規範對施工之要求`（37 頁），每支回想卡 10 組＋觀念圖 5 張，旁白合計 19,091 字（配音後約 70 分鐘） | 五份 `formula-given-*` 只回答「要不要背」，沒有把「該背的那幾條真的記進去」的載體。記憶片改為主動回想結構（深色提問頁只出題、下一頁才給 LaTeX 解答＋記憶鉤），提問頁即影片的自然暫停點。四支輸入一律取自對應 `formula-given-SS-*.html` 內嵌的 `const F=[]`／`const MX=[]` 原始資料，無任何重建成分 |
| 2026-08-09 | 修正 `study/formula-given-SS-U1-3.html`「P-M 互制圖的三個折點座標」的 `eq`：`(1/9, 0.2)` → **`(0.9, 0.2)`**（`.pdf` 尚未重新產生，仍含舊值） | 該條目自身的 `meta` 推導本來就是對的（`Pu/φcPn=0.2` 代入 H1-1a 得 `x=9/8×0.8=0.9`、代入 H1-1b 得 `x=1−0.1=0.9`），`1/9` 顯係誤把 H1-1a 的係數 `8/9` 寫成折點座標。由建置 U1-3 記憶片時交叉驗算發現 |
| 2026-08-07 | 修正 `skills/unit-lecture/SKILL.md` 適用科目表：SM 由「材料力學」改為「土壤力學與基礎設計」、MM 由「工程數學／力學」改為「材料力學」、RC/SA/SD 補為命題大綱全名；並同步專案版與已安裝版（專案版原本落後，缺 `problems-view` 渲染整節） | SM 與 MM 的科目名互換會導向錯誤的資料夾；六科名稱應以 `raw/json/syllabus_taxonomy.json` 為唯一依據 |
| 2026-07-25 | **規則 1 例外擴充**：`raw/` 唯讀的例外從「`question_index.json`」擴充為「`question_index.json` + `raw/solutions/methods/`」，並訂出三項修改條件（驗算／同步 wiki／記 log） | `methods/` 是 `wiki/methods/` 的 compile 來源，只改 wiki 副本會被 `compile-all` 蓋回；公式勘誤需能根治。個別題目解析 `raw/solutions/SS-YYYY-N/` 仍受完整保護 |
| 2026-08-20 | 新增 `skills/subject-frequency-map.skill`（六科通用「全科出題頻率熱圖」產生器，附 `scripts/build_frequency.py`）；產生 `study/frequency-SS.html` | `unit-exam-intel` 一次只看一個子項，看不到整科全貌，無法回答「整科該從哪裡開始讀」。本頁把 98 題攤在 7 子項 × 24 考年的格子上，只談頻率與時間分配（押題仍看各子項命題分析頁的「命題風險排序」）。全流程無人工判斷步驟，題庫更新後可無腦重跑。同輪由對帳揪出 8 題 `primaryTopicId` 指向他科 taxonomy（`SD-U3-1` × 5、`MM-U1-1` × 3），未畫進熱圖，待修 |
| 2026-08-22 | **七題解析勘誤**（SS-2005-1／SS-2013-2／SS-2013-3／SS-2015-3／SS-2018-2／SS-2024-1／SS-2025-2）並依現行規範重新驗算；同步 `-column-curve-viz.html`、`wiki/problems/`、`study/problems-view/`、`question_index.json` tags、`study/study-SS-U1-1.html`、`dashboard-data.js` | 三題觀念錯誤改變答案：SS-2013-2 把考卷原文「柱 CD 為**靠桿**」讀成「鉸接」且未用考卷給的萊梅厥公式（w 由 287 更正為 **96.0 tf/m**、d 由 1.20 更正為 **0.40 m**）；SS-2024-1 把塊狀殘餘應力的「**強度平台段**」誤畫成「λ=√2 處不連續跳躍」，違反柱強度曲線隨 λ 單調不遞增（補 λ₂=0.985 轉折點，改為四段連續）；SS-2025-2 對板類三面圍焊誤用 `U=1−x̄/l` 並取 x̄=L/2，應依規範 §4.3 板類縱向銲之 `l/w` 階梯值且 `l ≥ w`（**L_max=3 cm、P_max 由 6.15 更正為 9.00 tf**）。另四題為判讀／漏檢核：SS-2013-3 圖 3 兩平面邊界相反（強軸 A 鉸-C 固接可滑動、弱軸 A 固接）；SS-2005-1 漏算螺栓剪力 71.8 tf（與控制值僅差 4.8%）；SS-2018-2 漏做局部挫屈 b/t 且把 φc=0.90 標為「誤」；SS-2015-3 把「固接\*-鉸接」誤述為懸臂柱。規範層面：台灣現行仍為 99 年版（φc=0.85），各題已增列 AISC 360-16／-22 對照 |
| 2026-08-22 | **全庫 98 題 `verificationStatus` 重置為 `unverified`**；同步 `wiki/problems/`（98 檔）、`wiki/index.md`（77 列＋計數）、`wiki/by-year.md`（98 列）、`index.html` 儀表板標題、`study/study-SS-U1-1〜U2-3.html`（5 檔徽章與圖例） | 同日七題勘誤中抽查 7 題即有 3 題存在改變答案的觀念錯誤（43%），`verified` 標記已失去可信度，由使用者決定全庫重置、逐題重新驗算。⚠️ 連帶效果：規則 5 使 `ingest` 目前對所有題目皆被擋下（`wiki/problems/` 98 頁仍保留），重驗通過後改回 `verified` 即恢復 |
| 2026-08-22 | **規則 1 增訂第三項例外：`raw/solutions/SS-YYYY-N/SS-YYYY-N.md` 允許「解析勘誤」**（附四項條件：回考卷原文逐頁目視判讀／數值獨立重算／同步全部下游／記 log；並明定 `raw/exams/`、使用者截圖與補充 PDF 仍完整受保護，勘誤後須退回 `unverified`）；規則 2 補上與新例外的界線。另**修復 `wiki/log.md` 的 Big5 編碼殘留**（byte 16728–17259，嚴格 Big5 解碼零損失轉 UTF-8，還原 8 處誤寫的反引號，原始位元組存於 `wiki/log.md.big5.bak`） | 舊條文「個別題目解析不在例外內」曾使 2026-07-30 的 VERIFY 查出 `SS-2013-2.md` 量級筆誤卻不敢修，該檔後續又被查出高估 3 倍的觀念錯誤——規則不該讓已知錯誤留在正本裡。改為「可勘誤但條件嚴格」，把保護對象從「檔案」精確化為「可追溯性與證據」 |
| 2026-08-22 | 第二批七題解析勘誤（`SS-U1-2` 梁桿件：SS-2008-1／2010-4／2011-3／2014-3／2015-1／2023-3／2025-1），每題新增 `## 6. 依最新規範（AISC 360-16／-22）對照`；下游同步 `wiki/problems/` ×7、`study/problems-view/` ×7、`SS-2015-1-sfd-bmd-viz.html`、`question_index.json`／`dashboard-data.js` tags（append-only）、`study/study-SS-U1-2.html` | 兩處答案變更：**SS-2015-1** 最佳斷面漏掉更輕且合格的 BH 920×300×19×25（247 kg/m，$\phi_bM_p = 233.78 \geq 230.72$），原答 251 kg/m——成因是圖 1(b) 中該曲線平台與 BH 500×500 幾乎重疊、標籤又以引線指向 $L_p = 3.02$ m 的陡降段；**SS-2014-3** 主答 $C_b$ 由 1.136 改為 **1.0**（原卷「均佈**的**雙向彎矩」中心語為彎矩，且前版「簡支梁不可能有常數彎矩」之論證有誤）。另修三處與考卷公式表牴觸／自相矛盾者：SS-2015-1 的 $A_w$ 定義（100 年考卷明列 $(d-2t_f)t_w$）、SS-2011-3 的 $C_W$（同卷明列 $I_fh^2/2$，原用近似式高估 0.37%）、SS-2008-1 的 $L_d/A_f$ 推導方向顛倒（誤歸因於壓力翼板柱效應＝翹曲機制）；SS-2023-3 修 §3.5 與 §4 的內部矛盾（$I_x$ 748,580→1,224,062）。7 題約 150 個數值以程式重算，MISMATCHES: 0；考卷 10 頁轉圖目視判讀 |
| 2026-08-22 | 第三批六題解析勘誤（`SS-U1-3` 梁柱／二階分析：SS-2003-4／2009-1／2011-1／2013-4／2020-3／2022-1），每題新增 `## 6. 依最新規範對照`；下游同步 5 份 `*-pm-viz.html`、`wiki/problems/` ×6、`study/problems-view/` ×6、`question_index.json`／`dashboard-data.js` tags、`study/study-SS-U1-3.html` | 本輪首度**回查台灣規範官方 PDF 原文**（rootlaw／行政院公報 99.09.16 版），釐清四項長期被誤用的條文：① ASD (8.2-5) 之 $C_m$ **無 $\geq 0.4$ 下限**（解說明言 1986 年起廢止，故 100 年考卷公式表所印之「(≥0.4)」有誤）；② LRFD (8.2-3) 之 $B_1$ 是台灣**自訂**的 0.64／0.32 式，**不等於** AISC 的 $C_m/(1-P_u/P_{e1})$；③ $P_{e1}$ 之 $K \leq 1.0$、$P_{e2}$ 之 $K \geq 1.0$；④ 耐震 (13.6-3) 強柱弱梁**梁側乘單一定值 1.25**，不含 $R_y$ 與 $M_v$。三題答案／控制式變更：**SS-2013-4** 圖 4 幾何判讀完全錯誤（三根柱→**單柱**、A/D 是梁端**滾支承**、$P$ 在柱頂 B），$M_{lt}$ 由 $HL/3$ 改為 **$HL$**、$\sum P_{eK}$ 由 $7.72$ 改為 **$2.88EI/L^2$**；**SS-2003-4** 由「側移構架 $C_m=0.85$」改為「有側撐＋雙曲率 $C_m=\mathbf{0.2}$」，穩定式 1.127 N.G. → **0.595 OK**（控制式改為強度式 1.140）；**SS-2020-3** 補 $1.5F_yS_y$ 上限＋$P_{e1}$ 改用 $K=1.0$，$M_{wy}$ 7.48 → **7.91** tf·m。另 **SS-2009-1** 子題(一) 原答 AISC 341 而題目明寫「我國規範」，已改為 (13.6-3)，並更正 P-M 折線兩段斜率顛倒（AB 為 $-8/9$ 較平、BC 為 $-2$ 較陡）。6 題約 180 個數值程式重算 MISMATCHES: 0；考卷 10 頁轉圖目視，其中三處需 450–500 dpi 才判得出支承符號與力偶轉向 |
| 2026-08-22 | 第四批六題解析勘誤（`SS-U1-4` 接合之分析與設計：SS-2009-4／2015-2／2017-2／2017-4／2018-3／2020-4），每題新增 `## 6. 依最新規範（AISC 360-16／-22）對照`；下游同步 `wiki/problems/` ×6（6 個 H1 全部改寫）、`study/problems-view/` ×6、`question_index.json`／`dashboard-data.js` tags（append-only）、`study/study-SS-U1-4.html`、`study/study-SS-U1-1.html`、`study/lecture-SS-U1-4.html` §7.1 補警語 | 本輪回查台灣規範**容許應力設計法第十章「接合設計」**原文，釐清五項條文：① 螺栓中心距 §10.3.9 之一般強制下限是 **8/3 d**，`3d` 僅在「沿力方向且 $F_p$ 依式(10.3-1a)/(10.3-1b) 取用」時強制（AISC 360-16 §J3.3 列為 preferred）；② 預拉力「等於最小抗拉強度之 **0.7 倍**」且應乘**螺紋處有效抗拉面積 $A_t$**（誤用 $A_b$ 高估 33%，已以 AISC 表 J3.1 之 3/4 in A325 = 28 kips 驗核）；③ 摩阻型接合台灣 ASD **以表列容許剪應力處理**（A325 標準孔 1.19、A490 標準孔 1.47 tf/cm²），並要求滑動係數 ≥ 0.33；④ 填角銲容許剪應力表 10.2-5 為 **0.3F_EXX = 144.8 N/mm²**（＝ AISC 360-16 ASD 之 $0.6F_{EXX}/2.00$，恆等）；⑤ 最小銲腳表 10.2-4 之 `12<t≤19 mm → 6 mm`（非 8 mm）。三題答案變更：**SS-2020-4** 舊解漏掉螺栓列偏心 $V\!\cdot\!e$ = 350 與腹板依剛度分擔之彎矩 $M_w I_w/I_x$ = 947 tf·cm（後者為前者 2.7 倍），最不利螺栓合力 11.67 → **25.93 tf**，螺栓 M20 → **D25**、鈑厚 8 → **12 mm**；**SS-2018-3** 圖面三處銲接符號**全為 6 mm 填角銲**（舊解誤判梁翼為 CJP 並以母材 $0.6F_y$ 驗而判 OK），翼板改以喉面積得 **151.6 N/mm² > 90.5 ⇒ NG，需 10 mm**，另更正 SN400B 之 $F_y$ 245 → **235** 並查出 $f_a = 90.5 = F/(1.5\sqrt3)$ 係**日本 AIJ 長期許容剪應力**（台灣同條件為 144.8，故 6 mm 腹板銲依台灣規範反而 OK）；**SS-2015-2** 圖 2「7 cm」量至**連接板邊緣虛線**而非槽鋼端緣、且橫向 gauge 10 cm 使橫斷面切 **2 孔**（舊解扣 1 孔），NSF 146.2 → **137.3 tf**、BSR 82.7 → **83.5 tf**（且發現**由上限式控制**）。**SS-2009-4** 更正中心距的規範層次顛倒；**SS-2017-2** 釐清 $\phi = 1.0/0.85$ 係 AISC **360-05** 之規定（360-10 起改依孔型 1.00/0.85/0.70、$h_{sc} \to h_f$）且 A 類 $\mu$ 為 0.30 非 0.33。**SS-2017-4** 數值全對（$P_u$ = 90.3 tf），以線理想化／有限寬度／坊間詳解三方交叉驗核（90.27／90.49／90.9 tf）。額外重大收穫：**109 年試卷第 3-3 頁印出台灣規範 (8.2-3) 之 $B_1$ 公式原文**，證實第三批「因 PDF 文字層破損而以物理一致性反推」的形式完全正確。6 題約 180 個數值程式重算 MISMATCHES: 0；考卷 8 頁轉圖目視，三處需 300–500 dpi 才判得出銲接符號、尺寸線圓點與隱藏線位置 |
| 2026-08-29 | 第三批六題向量圖解補繪（`SS-U1-3` 梁柱／二階分析：SS-2013-4／2020-3／2003-4／2011-1／2022-1／2009-1，共 20 張 SVG ＋ 2× PNG，腳本 `gen_SS-*.py` 隨解析版控）；下游同步 `wiki/problems/` ×6（內文 6 張＋圖形表 20 列）、`study/problems-view/` ×6（20 張） | 本組正是 2026-08-22 第三批勘誤的同一批題，每張圖都對準那輪查出的錯誤：SS-2013-4 的「三根柱」誤讀與 $M_{lt}=HL/3$、SS-2003-4 的 $C_m$ 符號、SS-2009-1 的 P-M 兩段斜率顛倒。本輪並揪出 struct-diagram 的三個排版陷阱：**中文寫進 `math_px()` 會被數學字型整段吃掉**（`render.py` 的溢出檢查抓不到，檔案仍合法）、`math_px()` 內的裸 `<` 會產生非法 XML、`est_width()` 低估含 `√` 的字串寬度而讓靠右標籤壓到長條 |
| 2026-08-29 | 第四批六題向量圖解補繪（`SS-U1-4` 接合之分析與設計：SS-2015-2／2017-4／2017-2／2020-4／2018-3／2009-4，共 20 張 SVG ＋ 2× PNG）；下游同步 `wiki/problems/` ×6（內文 8 張＋圖形表 20 列，**SS-2017-2 原無圖故新建「圖形」節**）、`study/problems-view/` ×6（20 張） | 本組正是 2026-08-22 第四批勘誤的同一批題，每張圖對準那輪查出的錯誤：SS-2020-4 漏掉的 $V\!\cdot\!e$ 與 $M I_w/I_x$（合力 11.67 → 25.93 tf）、SS-2018-3 把梁翼誤判為 CJP、SS-2009-4 中心距 $\frac{8}{3}d$ 與 $3d$ 的層次顛倒。本輪新增三項排版教訓：**`⅔` 等分數字元在襯線與中文字型皆缺字**、`cv.dim()` 的 label 走 `math_px` 故同受限制、以及 `problems-view` 的粗體錨點渲染為 `<strong>…</strong><br />` 而非 `</p>`，比對錯會把圖插到錯誤章節 |

---

## 目前收錄狀況

> 此處不維護靜態數字（容易過時）。執行 `status` 指令可取得最新的驗證進度、解析題目數、標籤統計。
>
> 總題數：**98 題**（2002–2025 年）
