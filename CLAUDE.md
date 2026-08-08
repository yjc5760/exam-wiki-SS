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
| 2026-08-07 | 修正 `skills/unit-lecture/SKILL.md` 適用科目表：SM 由「材料力學」改為「土壤力學與基礎設計」、MM 由「工程數學／力學」改為「材料力學」、RC/SA/SD 補為命題大綱全名；並同步專案版與已安裝版（專案版原本落後，缺 `problems-view` 渲染整節） | SM 與 MM 的科目名互換會導向錯誤的資料夾；六科名稱應以 `raw/json/syllabus_taxonomy.json` 為唯一依據 |
| 2026-07-25 | **規則 1 例外擴充**：`raw/` 唯讀的例外從「`question_index.json`」擴充為「`question_index.json` + `raw/solutions/methods/`」，並訂出三項修改條件（驗算／同步 wiki／記 log） | `methods/` 是 `wiki/methods/` 的 compile 來源，只改 wiki 副本會被 `compile-all` 蓋回；公式勘誤需能根治。個別題目解析 `raw/solutions/SS-YYYY-N/` 仍受完整保護 |

---

## 目前收錄狀況

> 此處不維護靜態數字（容易過時）。執行 `status` 指令可取得最新的驗證進度、解析題目數、標籤統計。
>
> 總題數：**98 題**（2002–2025 年）
