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
Cowork: ingest SS-XXXX-N → wiki 自動更新
```

---

## 兩個環境分工

| 環境 | 負責什麼 |
|------|---------|
| **你（使用者）** | PDF 題目附圖截圖（fig-N.png）、chart/eqn/hand 補充截圖、驗算後更新 verificationStatus |
| **Cowork** | 解題（SOLVE，**一次一題**）、存檔（.md + viz.html）、更新 question_index.json（hasSolution/tags/designMethod）、考題分布分析、直接維護 wiki/diagnosis/ · wiki/failure-modes/ · wiki/materials/ · wiki/code-ref/ · wiki/queries/；以及 ingest、compile-all、lint、status、add method（詳見 CLAUDE-CODE.md） |

---

## 單向資料流

```
raw/solutions/SS-XXXX-N/SS-XXXX-N.md  ──→  wiki/problems/      （Cowork: ingest）
raw/json/concepts.json                 ──→  wiki/concepts/      （Cowork: compile）
raw/solutions/methods/                 ──→  wiki/methods/       （Cowork: add method）
Cowork 查詢結果                        ──→  wiki/queries/       （Cowork 直接存入）
Cowork 跨層知識工具                    ──→  wiki/diagnosis/     （Cowork 直接存入）
                                       ──→  wiki/failure-modes/ （Cowork 直接存入）
                                       ──→  wiki/materials/     （Cowork 直接存入）
                                       ──→  wiki/code-ref/      （Cowork 直接存入）

解題內容唯一來源：raw/solutions/ 下的 .md 檔案
索引資訊唯一來源：raw/json/question_index.json
wiki/queries/ 及四個跨層知識目錄：由 Cowork 直接寫入，不走 ingest 流程
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
│
├── study/                           ← 讀書筆記與講義（非架構核心，供參考）
│
├── raw/                             ← 所有原始資料（唯讀，絕對不可修改）
│   ├── exams/                       ← 原始考卷 PDF（命名：SS-YYYY_鋼結構設計.pdf）
│   ├── json/
│   │   ├── concepts.json            ← 概念定義（供 compile-all）
│   │   └── question_index.json      ← ⭐ 題目總索引（唯一需要人工維護的 JSON）
│   └── solutions/                   ← AI 解析 + 補充截圖（每題一個資料夾）
│       ├── SS-YYYY-N/
│       │   ├── SS-YYYY-N.md
│       │   ├── SS-YYYY-N-fig-1.png
│       │   └── SS-YYYY-N-[內容碼]-viz.html
│       └── methods/                 ← 解題方法論
│
└── wiki/                            ← 知識庫輸出
    ├── index.md                     ← 主導航（七層架構）
    ├── by-year.md                   ← 依考年分類
    ├── log.md                       ← 操作紀錄（append only）
    ├── concepts/                    ← 概念頁         ← Cowork
    ├── methods/                     ← 方法論頁       ← Cowork
    ├── traps/                       ← 陷阱頁         ← Cowork
    ├── problems/                    ← 題目頁         ← Cowork
    ├── philosophy/                  ← 設計哲學頁     ← Cowork
    ├── queries/                     ← 查詢結果頁     ← Cowork
    ├── diagnosis/                   ← 題型診斷層     ← Cowork
    ├── failure-modes/               ← 失敗模式層     ← Cowork
    ├── materials/                   ← 材料行為層     ← Cowork
    └── code-ref/                    ← 規範條文對應層 ← Cowork
```

---

## 知識分類骨架（七層）

Wiki 導航依七層知識架構組織（七層均由 Cowork 直接維護）：

| 層 | 目錄 | 維護者 | 內容 |
|----|------|:------:|------|
| Layer 1 | `concepts/` + `problems/` | Cowork | 核心構件設計（拉壓/梁/梁柱/接合） |
| Layer 2 | `philosophy/` | Cowork | 設計哲學與實務（耐震/材料/施工） |
| Layer 3 | `methods/` | Cowork | 解題方法論（共軛梁/虛功/P-M圖） |
| Layer 4 | `diagnosis/` | Cowork | 題型診斷決策樹 |
| Layer 5 | `failure-modes/` | Cowork | 失敗模式（強度/穩定/使用性/接合） |
| Layer 6 | `materials/` | Cowork | 材料行為（應力應變/殘留應力/斷裂韌性/銲接性） |
| Layer 7 | `code-ref/` | Cowork | 規範條文對應（AISC 360/341/AWS D1.1） |

---

## 重要規則

1. **`raw/` 目錄下所有檔案絕對不可修改**（`question_index.json` 除外）
2. **`verifiedSolution` 是最終答案，不可質疑或重新計算**
3. **`wiki/log.md` 只可 append，不可刪除已有紀錄**
4. **wiki/ 大多數目錄是 compile 輸出，不可手動修改**；例外：diagnosis/ · failure-modes/ · materials/ · code-ref/ · queries/ 由 Cowork 直接維護
5. **ingest 前必須確認 verificationStatus = "verified"**
6. 概念連結使用 `[[concept_id]]`（Obsidian 相容）
7. 每次 ingest 同時更新 index.md 和 by-year.md
8. **格式與命名規範見 CLAUDE-SPEC.md；操作指令見 CLAUDE-CODE.md**

---

## CHANGELOG

| 日期 | 變更 | 原因 |
|------|------|------|
| 2026-04-06 | 初始建立 schema v1 | 從 Karpathy LLM Wiki 概念出發 |
| 2026-04-06 | 升級 v2：加入 solutions/ 資料夾、手寫補充機制 | 整合實際解題流程 |
| 2026-04-06 | 升級 v3：question_index 獨立、by-year.md、單向資料流 | 四項架構優化 |
| 2026-04-06 | 移除 formulas.json；加入標籤分類系統；加入圖片雙重保險規範；統一圖片命名規則 | 多項規格優化 |
| 2026-04-06 | 資料夾改名為 exam-wiki-SS，確立每科獨立資料庫策略 | 六科規模差異大，獨立維護效率更高 |
| 2026-04-07 | 移除 symbols.json、base/ 目錄；整合多個 JSON 進 CLAUDE.md | 簡化結構，減少中間層 |
| 2026-04-07 | 解題環境從 Claude.ai Chat 改為 Cowork | Cowork 可直接存取資料夾 |
| 2026-04-21 | SOLVE 工作流程加入 PDF 截圖步驟；fig PNG 由使用者負責 | 統一截圖品質與流程 |
| 2026-04-22 | 七項文件優化（解析格式、多子圖命名、設計哲學框架擴充等） | 2018–2022 年解題實戰缺口修正 |
| 2026-04-28 | Cowork 每次僅解一題；fig 截圖責任移轉至使用者 | token 上限與截圖品質控制 |
| 2026-05-27 | 知識庫架構從三層升為七層（diagnosis / failure-modes / materials / code-ref） | 98 題累積後需要更豐富的橫向知識工具 |
| 2026-05-27 | Harness 四層拆分：新建 CLAUDE-CODE.md / CLAUDE-SPEC.md / README.md / GLOSSARY.md；CLAUDE.md 精簡為純身份層（~150行） | 降低每次 session 的閒置 token，固化執行路徑 |
| 2026-05-27 | 修正 CLAUDE-SOLVE.md 過時引用（格式規範指向 CLAUDE-SPEC.md）；連結 GLOSSARY.md 至 wiki/index.md 與 wiki/concepts/index.md；新建 study/ 目錄存放讀書講義 | 消除殘留的文件不一致問題 |
| 2026-05-31 | 新增 `skills/` 目錄；建立 `vha-treasure-map.skill`（VHA→藏寶圖互動儀表板，含 KaTeX 渲染） | 將 SS-2020-3 藏寶圖工作流程打包為可重用 skill，方便 GitHub 開源共享 |
| 2026-05-31 | 清除 `study/` 中的 VHA skill 草稿（vha.skill、vha-updated.skill、vha-SKILL-updated.md） | 正式 skill 已安裝，草稿無需保留 |

---

## 目前收錄狀況

> 此處不維護靜態數字（容易過時）。執行 `status` 指令可取得最新的驗證進度、解析題目數、標籤統計。
>
> 總題數：**98 題**（2002–2025 年）
