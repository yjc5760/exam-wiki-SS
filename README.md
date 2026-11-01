# exam-wiki-SS — 鋼結構設計考古題知識庫

**科目：** 專門職業及技術人員高等考試結構工程技師 — 第四科：鋼結構設計
**收錄範圍：** 2002–2025 年（民國 91–114 年），共 98 題
**題目編號：** SS-YYYY-N（如 SS-2015-1 = 2015年第1題）

---

## 這個資料庫是什麼

每道考古題都有一份 **深度解析**（LaTeX 公式、逐步計算、陷阱說明），解析由 AI 完成，經盲解比對與人工驗算確認。讀書以 `study/`（題目瀏覽頁、觀念講義、單元總覽、教科書）為準。

> 2026-11-01 起 **wiki/ 只保留 `wiki/queries/`**（稽核報告、盲解紀錄、變更紀錄 log.md）；舊 wiki 各層已封存於 `archive/wiki/`，不再維護、內容未經全面核對。

**兩個工作角色：**

| 你要做什麼 | 怎麼做 |
|-----------|--------|
| 解一道新題 | 對 **Cowork** 說「解析 XXXX 年考卷」 |
| 解析勘誤後同步 | 依 CLAUDE.md 規則 1（重生 `study/problems-view/`、更新索引與教材、記 `wiki/queries/log.md`）；ingest 已停用 |
| 查詢知識 / 跨題分析 | 對 **Cowork** 直接提問 |

> 所有操作都在 Cowork 對話中完成，無需終端機或其他工具。完整指令清單見 **CLAUDE-CODE.md**。

---

## 快速導航

| 我想找... | 去哪找 |
|----------|-------|
| **視覺化瀏覽整個知識庫** | **雙擊 `index.html`**（題庫搜尋篩選、考點統計、進度追蹤、指令速查） |
| 特定題目的解析 | `raw/solutions/SS-YYYY-N/SS-YYYY-N.md` |
| 子項單元總覽（考什麼＋公式給／背＋逐題公式表） | `study/unit-SS-UN-n.html`（由 `study/data/unit-SS-UN-n.json` 經 `python scripts/build_unit_page.py SS-UN-n` 產生；舊 `study-`／`formula-given-` 為轉址頁） |
| **單元觀念講義（練題前建立原理直覺）** | `study/lecture-SS-UN-n.html` + `.pdf`（說「生成 SS-UN-n 講義」生成） |
| 題目渲染頁（公式／附圖可讀） | `study/problems-view/SS-YYYY-N.html` |
| 稽核、盲解比對報告 | `wiki/queries/`（總帳 `audit-ledger-SS.json`） |
| 操作紀錄 | `wiki/queries/log.md` |
| 舊 wiki 各層（概念、方法、陷阱、規範對應…） | `archive/wiki/`（封存，僅供參考） |

---

## 檔案地圖

```
exam-wiki-SS/
├── README.md          ← 你在這裡（冷啟動導覽）
├── CLAUDE.md          ← 身份層：分工、資料流、重要規則
├── CLAUDE-SOLVE.md    ← Cowork 解題 Skill（流程層）
├── CLAUDE-CODE.md     ← 所有 Cowork 指令 Runbook（16個指令）
├── CLAUDE-SPEC.md     ← 所有格式/命名規範（規格層）
├── index.html         ← 離線儀表板（題庫篩選/統計/進度追蹤/指令速查）
├── dashboard-data.js  ← 儀表板快照（更新儀表板資料 指令重新生成）
│
├── skills/            ← 配套 Cowork Skills（.skill 打包檔 + 原始碼，見 skills/README.md）
│
├── study/             ← 讀書講義
│   ├── study-*.html   ← 速查／複習頁（study 指令輸出）
│   ├── lecture-*.html ← 單元觀念講義 + 同名 .pdf（unit-lecture skill 輸出）
│   └── assets/katex/  ← 本機 KaTeX，供 lecture-*.html 離線渲染數學式（勿刪）
│
├── raw/               ← 原始資料（預設唯讀；例外見 CLAUDE.md 規則 1）
│   ├── exams/         ← 考卷 PDF（SS-YYYY_鋼結構設計.pdf）
│   ├── json/          ← question_index.json ✏️可改、concepts.json
│   └── solutions/     ← 每題一個資料夾，含 .md + 截圖
│       ├── SS-YYYY-N/ ← 🔒 證據，不可修改
│       └── methods/   ← ✏️ 方法論，可修正公式（須驗算＋記 log）
│
├── wiki/
│   └── queries/       ← 稽核／盲解報告、audit-ledger、log.md
│
└── archive/wiki/      ← 🗄️ 2026-11-01 封存的舊 wiki 各層（唯讀參考）
```

---

## 如何開始解一道新題

```
1. 在 Cowork 開啟此資料夾（Project）
2. 說：「解析 2025 年考卷」
3. 依提醒截圖題目附圖，存入對應資料夾
4. 告知 Cowork「截圖完成，請開始解題」
5. Cowork 輸出 SS-2025-1.md（一次一題）
6. 人工驗算無誤後，說：「將 SS-2025-1 的 verificationStatus 改為 verified」
7. 執行 `python scripts/render_problem_view.py SS-2025-1` 產生題目瀏覽頁（ingest 已停用）
```

---

## 關鍵規則（避免常見錯誤）

- 年份用**西元**（SS-2015-1，不是 SS-104-1）
- PNG 截圖必須加序號（`fig-1.png`，不可寫 `fig.png`）
- 不產生互動圖 `*-viz.html`（2026-11-01 廢止）；圖解一律用 `figs/*.svg` 向量圖
- 公式必須用 LaTeX（`$F_y$`，不可寫純文字）
- ingest 前確認 `verificationStatus = "verified"`

> 完整規則見 **CLAUDE-SPEC.md**
