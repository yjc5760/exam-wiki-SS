# exam-wiki-SS — 鋼結構設計考古題知識庫

**科目：** 專門職業及技術人員高等考試結構工程技師 — 第四科：鋼結構設計
**收錄範圍：** 98 題（2002–2025 年，民國 91–114 年）
**題目編號：** SS-YYYY-N（如 SS-2015-1 = 2015年第1題）

---

## 這個資料庫是什麼

每道考古題都有一份 **深度解析**（LaTeX 公式、逐步計算、陷阱說明）和一份 **wiki 題目頁**（標籤、考點、互動圖）。所有解析由 AI 完成，人工驗算確認後才進 wiki。

**工作環境：**

| 你要做什麼 | 用哪個環境 |
|-----------|-----------|
| 解一道新題 | **Cowork**（說「解析 XXXX 年考卷」） |
| 把解析寫進 wiki | **Cowork**（輸入 `ingest SS-XXXX-N`） |
| 查詢知識 / 跨題分析 | **Cowork**（直接提問） |
| 維護四層橫向知識工具 | **Cowork**（diagnosis / failure-modes / materials / code-ref） |

---

## 快速導航

| 我想找... | 去哪找 |
|----------|-------|
| 特定題目的解析 | `raw/solutions/SS-YYYY-N/SS-YYYY-N.md` |
| wiki 題目頁（含標籤/圖形） | `wiki/problems/SS-YYYY-N.md` |
| 依年份瀏覽所有題目 | `wiki/by-year.md` |
| 概念說明（LTB、柱強度等） | `wiki/concepts/CONCEPT-ID.md` |
| 術語快速查詢 | `wiki/concepts/GLOSSARY.md` |
| 解題策略（拿到考題怎麼判斷） | `wiki/diagnosis/` |
| 設計法/規範 | `wiki/code-ref/index.md` |
| 操作紀錄 | `wiki/log.md` |

---

## 檔案地圖

```
exam-wiki-SS/
├── README.md          ← 你在這裡（冷啟動導覽）
├── CLAUDE.md          ← 身份層：分工、資料流、重要規則
├── CLAUDE-SOLVE.md    ← Cowork 解題 Skill（流程層）
├── CLAUDE-CODE.md     ← Cowork 操作指令 Runbook（流程層）
├── CLAUDE-SPEC.md     ← 所有格式/命名規範（規格層）
├── skills/            ← Cowork Skills（.skill 檔，可安裝）
│
├── raw/               ← 原始資料（唯讀）
│   ├── exams/         ← 考卷 PDF（SS-YYYY_鋼結構設計.pdf）
│   ├── json/          ← question_index.json、concepts.json
│   └── solutions/     ← 每題一個資料夾，含 .md + 截圖 + viz.html
│
└── wiki/              ← 知識庫（七層架構）
    ├── problems/      ← 所有題目頁
    ├── concepts/      ← 概念頁（含 GLOSSARY.md）
    ├── methods/       ← 解題方法論
    ├── diagnosis/     ← 題型診斷決策樹
    ├── failure-modes/ ← 失敗模式分類
    ├── materials/     ← 材料行為
    └── code-ref/      ← 規範條文對應
```

---

## 如何開始解一道新題

```
1. 在 Cowork 開啟此資料夾（Project）
2. 說：「解析 2025 年考卷」
3. 依提醒截圖題目附圖，存入對應資料夾
4. 告知 Cowork「截圖完成，請解 SS-2025-1」
5. Cowork 輸出 SS-2025-1.md（+ viz.html 如有）
6. 人工驗算無誤後，通知 Cowork 更新 verificationStatus = verified
7. 在 Cowork 輸入：ingest SS-2025-1
```

---

## 關鍵規則（避免常見錯誤）

- 年份用**西元**（SS-2015-1，不是 SS-104-1）
- PNG 截圖必須加序號（`fig-1.png`，不可寫 `fig.png`）
- 互動圖後綴必須是 `-viz.html`（`pm-viz.html`，不是 `pm.html`）
- 公式必須用 LaTeX（`$F_y$`，不可寫純文字）
- ingest 前確認 `verificationStatus = "verified"`

> 完整規則見 **CLAUDE-SPEC.md**
