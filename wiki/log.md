# Wiki 操作紀錄

> append-only，請勿刪除已有紀錄

---

## 2026-05-27 — SS-2020-3 解析修正 + 三個知識點新增

**操作類型：** 解析勘誤（Cowork）+ code-ref 知識點新增（Cowork）

### SS-2020-3 解析修正

**勘誤原因：** 原解析誤將兩端彎矩判定為雙曲率，實際為單曲率。
**修正範圍：** `raw/solutions/SS-2020-3/SS-2020-3.md`

| 項目 | 修正前（錯） | 修正後（對） |
|------|------------|------------|
| 強軸曲率判定 | 雙曲率，$M_1/M_2 = +1$ | 單曲率，$M_1/M_2 = -1$ |
| 弱軸曲率判定 | 雙曲率，$M_1/M_2 = +0.5$ | 單曲率，$M_1/M_2 = -0.5$ |
| $B_{1x}$ | $0.32 → 取 1.0$ | $1.167$（直接採用）|
| $B_{1y}$ | $0.549 → 取 1.0$ | $1.007$（直接採用）|
| **最終答案 $M_{wy}$** | **8.0 tf·m**（偏不安全）| **7.5 tf·m** |

**verificationStatus：** verified ✅（使用者確認）  
**ingest 執行：** 2026-05-27（Cowork 執行，等效 Claude Code ingest）

### 新增 code-ref 知識點（Cowork 直接寫入，不走 ingest）

- `wiki/code-ref/b1-m1m2-sign-convention.md` — B1 公式中 M1/M2 符號規則（單曲率=負、雙曲率=正）
- `wiki/code-ref/column-buckling-lambda-boundary.md` — λ_c = 1.5 彈/非彈性挫曲分界，臨界值 0.39Fy
- `wiki/code-ref/pm-interaction-physical-meaning.md` — P-M 互制方程式物理意義（雙折線、0.2門檻、8/9係數）

---

## 2026-05-26 — 建立四個跨層知識工具

**操作：** 建立 diagnosis / failure-modes / materials / code-ref 四個知識層次

**新建頁面：**
- `wiki/failure-modes/` — index + strength / stability / serviceability / connection（共 5 頁）
- `wiki/materials/` — index + stress-strain / residual-stress / fracture-toughness / weldability（共 5 頁）
- `wiki/code-ref/` — index（規範條文對應矩陣）
- `wiki/index.md` — 新增 Part 6 跨層知識工具導航區塊

**架構說明：**
知識庫從 Philosophy → Concept → Method 三層，擴充為七層：
Philosophy / Concept / Method / Diagnosis / Failure-Modes / Materials / Code-Ref

---

## 2026-04-20 — ingest SS-2014-4

**操作：** ingest SS-2014-4
**來源：** raw/solutions/SS-2014-4/SS-2014-4.md
**verificationStatus：** verified ✅

**新增頁面：**
- wiki/problems/SS-2014-4.md

**解題摘要：**
- W14×90 梁柱桿件 LRFD 檢核（斜撐構架，ASTM A572 Gr.50）
- B2 = 1.081（P-Δ 效應，θ=0.075）；B1 = 1.0（取下限，P-δ 可忽略）
- Mux = 326.2 kN-m（頂端控制，B1×Mnt + B2×Mlt）
- φcPn = 4433 kN（強軸控制，λc=0.573，Fcr=305.0 MPa）
- φbMnx = 810.4 kN-m（L < Lp，無LTB，全塑性）
- P-M 互制比 = **0.821 ≤ 1.0** ✅

**附屬檔案：**
- SS-2014-4-pm-viz.html（P-M 互制圖）
- SS-2014-4-fig-1.jpg（題目附圖）

**更新概念頁：**
- BEAM-COLUMN-INTERACTION：⚠️ → ✅ SS-2014-4
- P-DELTA-EFFECT：⚠️ → ✅ SS-2014-4
- MOMENT-AMPLIFICATION-CM：新增 ✅ SS-2014-4（B1 中的 Cm 計算）

**更新導航：**
- wiki/index.md：1.3 梁柱桿件與 2.1 耐震設計表格改為 ✅ 連結；已驗證 3→4 題
- wiki/by-year.md：2014年第四題改為 ✅ 連結；已驗證 3→4 題

---

## 2026-04-16 — ingest SS-2014-1, SS-2014-2, SS-2014-3

**操作：** ingest（消化 2014 年三道已驗證題目）
**執行時間：** 2026-04-16
**來源：** raw/solutions/SS-2014-1/SS-2014-1.md、SS-2014-2/SS-2014-2.md、SS-2014-3/SS-2014-3.md

**新增題目頁：**
- `wiki/problems/SS-2014-1.md` — 4.1.1 壓力桿件 LRFD；λc推導、柱強度曲線兩段式、高強度鋼對細長柱效益分析；附 column-curve-viz.html + hand-1/2.png
- `wiki/problems/SS-2014-2.md` — 4.2.2 鋼結構材料特性（概念題，副分類6.3.1）；SN490B vs ASTM A572 Gr.50 材料差異與梁柱接頭耐震行為
- `wiki/problems/SS-2014-3.md` — 4.1.2 梁桿件 LRFD；W21×93 雙向彎矩梁：非彈性LTB + Cb=1.136 + 弱軸1.5FySy上限 + 雙向互制0.664；附 hand-1/2.png

**新增陷阱頁：**
- `wiki/traps/WEAK-AXIS-BENDING-LIMIT.md` — 弱軸彎曲強度上限（1.5FySy），觸發自 SS-2014-3
- `wiki/traps/HIGH-STRENGTH-STEEL-SLENDER-COLUMN.md` — 高強度鋼對細長壓力桿件無效，觸發自 SS-2014-1

**更新概念頁（⚠️ → ✅）：**
- COLUMN-STRENGTH-CURVE：SS-2014-1 ✅
- RESIDUAL-STRESS：SS-2014-1 ✅
- FLEXURAL-BUCKLING-GENERAL：SS-2014-1 ✅
- CAPACITY-DESIGN：SS-2014-2 ✅
- STRONG-COLUMN-WEAK-BEAM：SS-2014-2 ✅
- LATERAL-TORSIONAL-BUCKLING：SS-2014-3 ✅
- BENDING-MODIFICATION-FACTOR-CB：SS-2014-3 ✅
- BIAXIAL-BENDING-BEAM：SS-2014-3 ✅（補充弱軸上限說明）
- SHAPE-FACTOR：新增 SS-2014-3 條目（弱軸Zy/Sy=1.57>1.5）

**更新導航：**
- wiki/index.md：三題改為 ✅ 連結；Wiki 狀態更新為 3 頁 / 3 題已驗證
- wiki/by-year.md：2014年三題改為 ✅ 連結；頁尾更新為已驗證 3 題

---

## 2026-04-16 — compile-all

**操作：** compile-all（更新 wiki，納入 2025 年新題）
**執行時間：** 2026-04-16
**來源：** raw/json/concepts.json、raw/json/question_index.json、raw/solutions/methods/

**結果：**
- wiki/concepts/ — 無變更（30 頁，全部已存在）
- wiki/methods/ — 無變更（conjugate-beam.md 已存在）
- wiki/by-year.md — 新增 **2025 年（民國 114 年）— 4 題**（SS-2025-1 至 SS-2025-4）；總數更新為 98 題（2002–2025）
- wiki/index.md — 新增 SS-2025-1、SS-2025-2、SS-2025-3（加入對應分類表格）；新增 SS-2025-4 至 Part 5 塑性分析；總數更新為 98 題
- wiki/problems/ — 無變更（0 頁，無已驗證題目）

**新增題目（SS-2025-1 至 SS-2025-4，均為 unverified）：**
- SS-2025-1：4.1.2 梁桿件 / LRFD / 結實斷面、塑性彎矩、銲接組合斷面
- SS-2025-2：4.1.1 拉力及壓力桿件 / ASD / 剪力遲滯、U值、淨截面
- SS-2025-3：4.1.2 梁桿件 / LRFD / LTB側扭挫屈、Lp、Lr
- SS-2025-4：4.2.1 塑性分析與設計 / 概念題 / 崩塌機構、上限定理

**備註：**
- question_index.json 現有 98 題（2002–2025），全部 verificationStatus = "unverified"
- 前次 compile-all 的 by-year.md/index.md 總數標示「91 題」有誤，本次一併修正為 98 題

---

## 2026-04-15 — compile-all

**操作：** compile-all（初次建立整個 wiki）
**執行時間：** 2026-04-15
**來源：** raw/json/concepts.json、raw/json/question_index.json、raw/solutions/methods/

**結果：**
- 生成 wiki/concepts/ — 30 個概念頁（依 concepts.json 全部概念）
- 生成 wiki/methods/conjugate-beam.md — 共軛梁法方法論頁
- 生成 wiki/by-year.md — 91 道題目依年份分類（全部標記 ⚠️ unverified）
- 生成 wiki/index.md — 依知識庫架構分類的主導航
- wiki/problems/ — 0 頁（無已驗證題目可生成）

**備註：**
- question_index.json 共 91 題，全部 verificationStatus = "unverified"
- 待驗證後，執行 `ingest SS-XXXX-N` 即可生成對應題目頁
- concepts.json 中有多個 related_concept_ids 指向尚未定義的概念（LINT 可偵測）

---

## 2026-05-26 — add method cb-factor

**操作：** ADD-METHOD cb-factor（Cowork 執行）

**新增：**
- `wiki/methods/cb-factor.md`（彎矩梯度修正因子 Cb 完整方法論頁）

**更新：**
- `wiki/index.md`：Part 3 方法論表格加入 Cb 因子；快速導航更新
- `wiki/log.md`：本條紀錄

**來源：** `raw/solutions/methods/cb-factor/cb-factor.md`（含互動圖 cb-factor-chart.html）

---

## 2026-05-26 — 批次 ingest 94 題

**操作：** ingest 所有未 ingest 題目（Cowork 批次執行）

**新增 wiki/problems/：** 94 個題目頁面（SS-2002 ~ SS-2013、SS-2015 ~ SS-2023、SS-2024、SS-2025 全年）

**跳過（已存在）：** SS-2014-1、SS-2014-2、SS-2014-3、SS-2014-4

**更新：**
- wiki/by-year.md：完整重建（98 題全部附連結）
- wiki/index.md：所有題目連結從 ⚠️ 更新為 ✅，統計數字更新

**總計：** wiki/problems/ 現有 98 題，全部 verified

---

## 2026-05-26 — compile-all

**操作：** compile-all（Cowork 執行）

**概念頁（wiki/concepts/）：** 30 頁均已存在，本次更新出現題目連結（⚠️→✅）：21 頁

**方法論（wiki/methods/）：** 2 頁（cb-factor, conjugate-beam）

**題目頁（wiki/problems/）：** 98 頁（全部 verified）

**wiki/queries/：** 目錄已建立

**wiki/by-year.md / wiki/index.md：** 已於前次 ingest 批次更新

**design_philosophy.json：** 不存在，跳過 wiki/philosophy/ 生成

---

## 2026-05-26 — 生成 wiki/philosophy/

**操作：** compile-all 補充（Cowork 執行）

**新增 wiki/philosophy/：** 8 頁（lrfd-beam、lrfd-column、asd-column、lrfd-tension、lrfd-connection、lrfd-beam-column-box、asd-pin-tension、probability-analysis）+ index.md

**來源：** CLAUDE-SOLVE.md「設計哲學框架」章節

---

## 2026-05-26 — lint 修復①：新建 23 個缺失概念頁

**新建：** BEARING-STIFFENER, BEARING-TYPE-CONNECTION, BOLTED-CONNECTION-DESIGN, CONCRETE-ENCASED-BEAM, CONNECTION-DESIGN, EFFECTIVE-NET-AREA, EULER-BUCKLING, HIGH-STRENGTH-BOLT-PRACTICE, MOMENT-AMPLIFICATION-B1-B2, PLASTIC-HINGE, PLASTIC-MOMENT-MP, PLASTIC-NEUTRAL-AXIS-PNA, SECOND-ORDER-ANALYSIS, SEISMIC-CONNECTION-DETAILS, SEISMIC-DESIGN-PHILOSOPHY, SHEAR-BUCKLING-WEB, SHEAR-CONNECTOR, TENSION-MEMBER-DESIGN, TORSIONAL-BUCKLING, WEB-CRIPPLING, WELDED-CONNECTION-DESIGN, WELDING-PRACTICE, YIELD-MOMENT-MY

---

## 2026-05-26 lint 修復全套（Task #7）

**操作者：** Cowork  
**操作內容：** 依序修復 lint 健檢所有 54 項問題

### ② 梁柱缺 pm-viz（10 題）
為以下 4.1.3 梁柱桿件題目生成 P-M 互制互動圖，並更新 wiki/problems 圖形區塊：
- ASD 題：SS-2003-4、SS-2004-4、SS-2007-2、SS-2008-4、SS-2019-3
- LRFD 題：SS-2012-3、SS-2020-3、SS-2022-1
- 概念型：SS-2011-1（DAM 概念圖）、SS-2013-4（B₁-B₂ 框架圖）

### ③ 標籤不足（6 題）
從各題 raw/solutions .md 擷取正確標籤，更新 question_index.json 及 wiki/problems：
SS-2016-1（8標籤）、SS-2016-2（6標籤）、SS-2016-5（8標籤）、
SS-2017-1（8標籤）、SS-2017-2（7標籤）、SS-2017-4（7標籤）

### ④ 孤立頁面
- 建立 wiki/traps/index.md，列出兩個 traps 頁面
- 建立 wiki/concepts/index.md，列出全部 53 個概念頁（依知識骨架分類）
- 建立 wiki/queries/README.md（目錄標記）並從 wiki/index.md 加入連結
- SS-2014-1.md 加入 → HIGH-STRENGTH-STEEL-SLENDER-COLUMN.md 連結
- SS-2014-3.md 加入 → WEAK-AXIS-BENDING-LIMIT.md 連結

### ⑤ 圖說缺漏
SS-2016-3 wiki/problems 頁已有 `*圖說（圖N...）：` 格式，確認為誤報，無需修改

### ⑥ 斷開連結
LATERAL-TORSIONAL-BUCKLING.md：`[[PLASTIC-MOMENT-MP]]` → `[塑性彎矩 Mp](PLASTIC-MOMENT-MP.md)`

**結果：** lint 最終驗收 0 項待處理 ✅

---

## 2026-05-26 出題頻率分析查詢

**操作者：** Cowork  
**操作內容：** 依 question_index.json 統計 98 題出題頻率，生成查詢結果頁  
**存入：** `wiki/queries/出題頻率分析-2026-05-26.md`  
**更新：** `wiki/queries/README.md`（加入查詢列表）、`wiki/index.md`（修正快速導航格式）

---

## 2026-05-31 VHA 藏寶圖儀表板建立

**操作者：** Cowork  
**操作內容：** 將 SS-2020-3 的 §3.5 VHA 轉化為互動式「藏寶圖」HTML 儀表板  
**存入：** `wiki/queries/SS-2020-3-treasure-map.html`  
**特性：** KaTeX 數學式渲染（inline embed）、L1/L2/SO/FU 顏色區分、知識線索連結、陷阱警示  
**更新：** `wiki/queries/README.md`（加入查詢列表）

## 2026-05-31 vha-treasure-map skill 建立

**操作者：** Cowork  
**操作內容：** 將 VHA→藏寶圖工作流程打包為 Cowork skill  
**存入：** `skills/vha-treasure-map.skill`  
**更新：** `skills/README.md`（新建，說明安裝方式與觸發語句）  
**清除：** `study/vha.skill`、`study/vha-updated.skill`、`study/vha-SKILL-updated.md`（草稿）

## 2026-06-11 命題大綱分類代號全面遷移（4.1.x → XX-Un-m）

**操作者：** Cowork  
**依據：** `raw/json/syllabus_taxonomy.json`（六科完整分類代號，格式 XX-Un-m）  
**對照表：** 4.1.1→SS-U1-1 · 4.1.2→SS-U1-2 · 4.1.3→SS-U1-3 · 4.1.4→SS-U1-4 · 4.2.1→SS-U2-1 · 4.2.2→SS-U2-2 · 4.2.3→SS-U2-3 · 6.3.1→SD-U3-1 · 1.1.1→MM-U1-1  
**修改範圍：**
- `raw/solutions/`：93 題解析 .md 標頭（主/副分類）＋ 2 個 viz.html subtitle ＋ methods/ 14 個 .md（適用題型）— 經使用者核准之 raw/ 一次性例外修改
- `wiki/problems/`：全部題目頁（主/副分類 [[ ]] 連結）
- `wiki/philosophy/`：11 頁（標題括號、命題大綱欄）
- `wiki/index.md`、`wiki/by-year.md`、`wiki/traps/`、`wiki/methods/`、`wiki/code-ref/`：零星舊代號
- `CLAUDE-CODE.md`：LINT 第 6 項改用新代號；新增第 17 項 topicId 驗證（須存在於 syllabus_taxonomy.json）
**保留不動：** `wiki/log.md` 歷史紀錄、`wiki/queries/` 歷史查詢頁、`study/`、`wiki/topics/` 舊代號頁（已為轉址存根，維持舊連結相容）

## 2026-06-11 建立知識庫儀表板（dashboard.html）

**操作者：** Cowork  
**操作內容：** 參考 exam-wiki-RC 儀表板改造為 SS 版，建立單頁總覽介面  
**存入：** `dashboard.html`（介面）＋ `dashboard-data.js`（98 題快照，自 question_index.json 生成）  
**功能：** 題庫瀏覽（搜尋／年份／單元／考點／設計法／練習進度篩選）、考點統計圖、七層知識架構導覽、指令速查、站內 Markdown＋KaTeX 閱讀器（File System Access API）、匯出 PDF、練習進度 localStorage 追蹤  
**更新：** `CLAUDE-CODE.md` 新增 DASHBOARD 指令（觸發語句「更新儀表板資料」）

## 2026-06-11 知識庫全面優化（10 項）

**操作者：** Cowork  
**操作內容：** 系統性補強內容缺口、修正結構性問題、完善文件

### 高優先：內容缺口補強

1. **wiki/index.md — 接合設計（SS-U1-4）題目清單補齊**
   - 補充 19 道主分類為 SS-U1-4 的題目表格（2002–2024年），與其他三個分類格式統一
   - 同步在接合設計核心概念增加 FILLET-WELD-DESIGN、ECCENTRIC-CONNECTION 連結

2. **新建概念頁：FILLET-WELD-DESIGN.md（填角銲設計）**
   - 含有效喉厚公式、LRFD/ASD 設計強度、破壞模式、常見陷阱、8 道歷年考題對照
   - 連結至 eccentric-weld.md 方法頁及 fillet-weld-0707.md 推導頁

3. **新建概念頁：ECCENTRIC-CONNECTION.md（偏心接合）**
   - 彈性向量法 vs 極限分析法比較；偏心螺栓群 Jp 計算；牛腿接合（bracket）力矩組合
   - 含 5 道歷年考題對照

4. **新建方法頁：slip-critical-lrfd.md（高拉力螺栓摩阻型 LRFD 設計）**
   - 完整 7 步驟：A325/A490 預拉力表 → φRn 計算 → 雙剪校正 → 同時受拉折減 → 承壓驗核 → 間距邊距
   - 含 φ=1.00 vs φ=0.75 常見混淆說明

5. **新建方法頁：composite-beam-pna.md（合成梁塑性中性軸計算）**
   - beff 計算 → Cs/Cc 比較 → PNA 位置判斷 → 兩種情況（版內/鋼梁內）的 Mn 計算
   - 含剪力連接器設計步驟

### 中優先：結構性問題修正

6. **wiki/index.md — 刪除底部重複「快速導航」區塊，移除靜態 Wiki 狀態數字**
   - 底部重複區塊改為「知識工具導航」（內容不重複）
   - 靜態數字（概念頁 53）改為指引用戶執行 `status` 指令

7. **CLAUDE-CODE.md — lint 第 6 項降級為 [warn]**
   - 改為：「SS-U1-3 梁柱題目且年份 ≥ 2016 但無 pm-viz → [warn]」
   - 年份 < 2016 的梁柱題不報告，避免大量偽警報

8. **CLAUDE-CODE.md — DASHBOARD 補充驗證步驟**
   - 第 6 步新增瀏覽器驗證提示：「確認題數、viz 連結可點擊、篩選統計功能正常」

### 低優先：體驗優化

9. **知識庫使用說明書.md — 更新版本 + 補充 dashboard 指令**
   - 版本更新為 2026-06-11
   - 維護指令表格新增「更新儀表板資料」
   - lint wiki 說明補充「[error] / [warn] 分級報告」

10. **skills/README.md — 補充新增 Skill 規範**
    - 新增 YAML 格式說明、加入本清單步驟、命名規則三個子節
    - 讓未來開源貢獻者有明確的規範可參考

**更新索引頁：**
- `wiki/concepts/index.md`：概念頁數從 58→60，接合設計表格補入兩個新概念
- `wiki/methods/index.md`：接合設計方法補入 slip-critical-lrfd，斷面性質補入 composite-beam-pna，頻率排名從 16→18


## 2026-06-11 �R���¥N���s��

**�ާ@�̡G** Cowork
**�ާ@���e�G** �R�� wiki/topics/ �� 9 ���¥N����}�s�ڡ]4.1.1.md�B4.1.2.md�B4.1.3.md�B4.1.4.md�B4.2.1.md�B4.2.2.md�B4.2.3.md�B6.3.1.md�B1.1.1.md�^
**��]�G** �N���E���]4.x��SS-Un-m�^������A���Ѯw�����w�L���� [[4.x]] �s���A�s�ڳॢ�γ~
**�O�d�G** SS-U1-1.md �� 9 �ӷs�N���D���]�t�U�����D�زM��^+ index.md �����v�T
- **2026-07-02**: ���� \��s�����O���\ (REFRESH-DASHBOARD) ���O�A�q \question_index.json\ �P \syllabus_taxonomy.json\ ���s�ͦ��F \dashboard-data.js\ �����O�ַӸ�ơC
- 2026-07-10｜STUDY｜產生子項深度複習頁 ×5：study/study-SS-U1-1.html（24題）、study-SS-U1-2.html（21題）、study-SS-U1-3.html（11題）、study-SS-U1-4.html（19題）、study-SS-U2-3.html（7題）。七區塊架構（命題分析/圖解/流程圖/公式速查/互動考題清單/高頻陷阱/互動計算器），KaTeX 渲染，題號連結至 index.html markdown 渲染器。
- 2026-07-19: 新增 Keynote PDF 按鈕至所有 study HTML 檔案。
- 2026-07-25｜UNIT-LECTURE｜產生 SS-U1-2 梁桿件觀念講義：`study/lecture-SS-U1-2.html` + `.pdf`（32 頁）。核心軸線「梁＝受壓翼板(壓桿)＋受拉翼板(拉桿)被腹板綁在一起」→ 推導 LTB；全單元編為「三道關卡確認有沒有資格用 Mp」。含 2 則手算範例（非對稱斷面 ENA/PNA/Zx；LTB 三區段完整流程）、12 題自我檢測、★精選 5 題（SS-2011-3 / SS-2025-1 / SS-2014-3 / SS-2023-3 / SS-2010-4）。同時渲染 25 題 `study/problems-view/*.html`（來源 raw/solutions/），並於 `study-SS-U1-2.html` 加入回連按鈕。
- 2026-07-25｜FIX｜**公式勘誤修正（6 檔）**。撰寫 SS-U1-2 講義時發現既有頁面的公式係數與單位標註錯誤，已逐項以數值自洽驗算後修正：
  1. `raw/solutions/methods/ltb-3zone/ltb-3zone.md` + `wiki/methods/ltb-3zone.md`：`Lp = 300ry/√Fy [kgf/cm²]` 代入得 6ry（正確約 50ry），改為 `1.76ry√(E/Fy) = 80ry/√Fy [tf/cm²]`；並補標 λpf/λpw 的 tf-cm² 與 ksi 雙係數、ASD 段落加單位警告。**（此為 raw/ 例外修改，經使用者同意；規則 1 的保護對象為考卷與驗證解答，方法論文件屬可維護內容）**
  2. `wiki/concepts/COMPACT-SECTION.md`：梁腹板 `λp=138、λr=322` 有誤 —— 138 實為**耐震** λpd（見 SS-2021-3），已改為 `λp=170/√Fy、λr=260/√Fy`（依 SS-2016-1 題目所附規範表），並新增柱腹板 68/√Fy、耐震 λpd 專列與單位對照表。
  3. `wiki/concepts/LATERAL-TORSIONAL-BUCKLING.md`：`Lr` 分母誤植為 `√(Fy−Fr)`，應為 `(Fy−Fr)`（量綱才是長度；誤用會使 Lr 高估 34%）。已補 X1/X2 定義與量綱自檢說明。
  4. `wiki/methods/asd-beam.md`：ASD 係數 `703,000 / 1,170,000 / 1,055,000` 彼此不相容（代入下界得 Fb=0.011 ksi，應為 0.60Fy；且與彈性式不接軌）。已改為 AISC ASD 9th Ed. 正確值 `102,000 / 510,000 / 1,530,000 / 170,000`（ksi），並附 tf/cm² 換算表與接軌驗算。Lc 兩式補上 in-ksi / cm-tf / mm-MPa 三制對照。
  5. `wiki/methods/asd-beam-column.md`：同 4 之係數，一併修正並加單位註記。
  6. `wiki/code-ref/asd-beam-fb-derivation.md`：Lc `200bf/Fy、137,900`（實為 mm-MPa 制且第一式漏了根號）改為三制對照表；`1,055,000`→`1,530,000` 並移除多餘的外層 Cb；`FS≈1.515`（由 0.66 反推，循環論證）改為 `FS=5/3`，補「0.66/0.60=形狀因子」推導；另標明 `0.79−0.002(bf/2tf)√Fy` 是**翼板局部挫屈 F1-3**，非 LTB 公式，不參與「取較大值」。
  驗算方式：所有係數以 Python 重算並檢查邊界接軌（ASD F1-6 在下界須得 0.60Fy、在分界須與 F1-7 相等），寬厚比則交叉比對 SS-2016-1、SS-2021-3 兩題驗證解答。
- 2026-07-25｜HARNESS｜**規則 1 例外擴充**：`raw/` 唯讀的例外由「`question_index.json`」擴充為「`question_index.json` + `raw/solutions/methods/`」，並明訂修改 methods 的三個必要條件（① 數值驗算 ② 同步覆蓋 wiki/methods/ ③ 記 log）。理由：`methods/` 是 `wiki/methods/` 的 compile 來源，公式勘誤若只改 wiki 副本會被 `compile-all` 蓋回，無法根治；而方法論屬「可維護的知識整理」，與需要保護可追溯性的「證據」（考卷、題目解析、驗證答案）性質不同。`raw/solutions/SS-YYYY-N/` 明確排除在例外之外，仍受規則 1、2 完整保護。同步更新四處：`CLAUDE.md`（規則 1 全文、資料夾結構圖加 🔒/✏️ 標記、單向資料流、兩個環境分工、CHANGELOG）、`README.md`（結構圖）、`CLAUDE-CODE.md`（ADD-METHOD 節新增 FIX-METHOD 五步流程與單位標註要求）。
- 2026-07-25｜UNIT-LECTURE｜產生 SS-U1-4 接合之分析與設計觀念講義：`study/lecture-SS-U1-4.html` + `.pdf`（33 頁）。核心軸線「構材設計求一個強度；接合設計求一串強度取最小值」→ 由「力量換手」推出極限狀態清單；全單元收斂為「兩把尺」（剪→×0.6、降伏配 FyAg／斷裂配 FuAn）。含 6 則手算範例（角鋼三破壞模式比較／摩阻型 vs 承壓型強度對照／銲腳 LRFD-ASD 雙算互驗／L 形偏心銲道並證明最遠點非臨界點／腹板銲道彎剪組合應力／斷續銲間距由構造規定控制）、11 張內嵌 SVG、18 條陷阱總表、12 題自我檢測、★精選 6 題（SS-2015-2 / SS-2017-4 / SS-2017-2 / SS-2020-4 / SS-2018-3 / SS-2009-4）。規範常數全部追溯來源：0.6 ← von Mises 1/√3；0.707 ← 45° 喉部幾何；2.4Fudt ← 1.2FuLct 在 Lc=2d 的封頂；Fnv(X)/Fnv(N) ≈ 1.25 ← 螺紋處有效面積 0.8Ab；Du=1.13 ← 實際預拉力統計高於規範最小值 13%。
- 2026-07-25｜UNIT-LECTURE｜同步作業：重新渲染 `study/problems-view/` 之 SS-U1-4 全 26 題（主 19、副 7），講義題號一律連向渲染頁（無 .md 連結殘留、無 @@MATH 殘留、圖片路徑逐一驗證）；`study/study-SS-U1-4.html` §1 按鈕列擴為三顆（觀念講義／PDF／Keynote）並加註使用順序。考點群題數以 `question_index.json` 重新統計後修正講義內數字（填角銲 10、拉力接合端 10、高強度螺栓 10、梁柱接頭 6、偏心向量法 5、施工/NDT 5、剪力流 1、ASD 6、概念題 7）；精選 6 題覆蓋度誠實揭露（考點群 7/8 = 88%，標籤權重 47%），未涵蓋項目於 §14 逐條列出並給候補題。
- 2026-07-25｜UNIT-LECTURE｜產生 SS-U1-3 梁柱桿件觀念講義：`study/lecture-SS-U1-3.html` + `.pdf`（30 頁）。核心軸線「柱與梁的內力算一次就定了；梁柱的內力會自己長大 —— 因為只有它同時有 P 與側向變形，而 P×δ 又是彎矩」；全單元編為「兩條腿走路」（需求側 B1/B2 或 Cm/F'e ＋ 強度側 φcPn/φbMn，在 P-M 互制式會合）。含 5 則手算範例（B1 單曲率 vs 雙曲率同柱同軸力對照／B2 靠桿漏算使 B2 少一半並觸發 0.6 上限／LRFD 完整 P-M 兩腿流程／ASD 完整互制並以 LRFD 利用率比 1.03 互驗／強柱弱梁兩個修正各自足以翻盤）、10 張內嵌 SVG、16 條陷阱總表、12 題自我檢測、★精選 6 題（SS-2013-4 / SS-2020-3 / SS-2003-4 / SS-2011-1 / SS-2022-1 / SS-2009-1）。規範常數全部追溯來源：1/(1−P/Pcr) ← 微分方程多出 Py 項後的剩餘勁度（Pcr−P），勁度歸零即挫屈；8/9 與 0.9 ← 為使 H1-1a/H1-1b 在 Pu/φcPn=0.2 處連續；F'e 的 12/23 ← Euler 應力 ÷ FS(23/12)；Cc = √(2π²E/Fy) ← Euler 應力＝Fy 再乘 √2（殘留應力）；ASD 的 FS 由 5/3 連續變化到 23/12 並與彈性段銜接；DAM 的 1.6 ← (1.2D+1.6L)/(D+L) 在 L≫D 的上限；1.5FySy ← 矩形翼板的形狀因數。
- 2026-07-25｜UNIT-LECTURE｜同步作業：新增渲染 `study/problems-view/` 之 SS-2003-4、SS-2004-4、SS-2007-2、SS-2008-4、SS-2009-1、SS-2011-1、SS-2013-4、SS-2014-4、SS-2020-3、SS-2022-1（共 10 題，另 SS-2012-3、SS-2019-3、SS-2014-3 已存在）；`study/study-SS-U1-3.html` §1 按鈕列擴為三顆（觀念講義／PDF／Keynote）並加註使用順序；§9 與 §14 對 RBS 的引用改為指向 `lecture-SS-U1-4.html#s7` 的明確跨講義連結。精選 6 題覆蓋度誠實揭露（考點群 7/8 = 88%，標籤權重 75%），唯一完全落空的群為「LTB 併入梁柱（Fbx 的 L/rT 分段、Cb）」，已於 §14 列為第一候補（SS-2007-2）。
- 2026-07-25｜NOTE｜`raw/solutions/SS-2014-4/` 內有 `SS-2014-4-fig-1.jpg`，但 `SS-2014-4.md` 未以 markdown 語法引用該圖，故渲染頁 `study/problems-view/SS-2014-4.html` 無附圖（渲染器忠實反映來源，未自行插圖）。因 `raw/solutions/SS-YYYY-N/` 受規則 1、2 保護，未修改；若需顯示該圖，須由使用者決定是否在來源 .md 補上圖片連結。
- 2026-07-30｜VHA-LECTURE｜產生「VHA 七題觀念講義」：`study/lecture-VHA-7題觀念講義.html` + `.pdf`（51 頁）。來源為 SS-2005-1、SS-2013-2、SS-2013-3、SS-2015-3、SS-2018-2、SS-2024-1、SS-2025-2 之 §3.5 變數層次分析（主要公式／L2 推導／L3 深層知識），七題全屬 `SS-U1-1`。章節依主題邏輯排序（拉力三道防線 → 剪力遲滯最佳化 → 組合柱斷面 → 分段有效長度 → 箱型柱完整檢核 → 殘留應力與柱曲線來源 → 框架層間穩定），每章結構為「主要公式追來源 → L2 逐步推導 → L3 深層知識逐條講透 → 完整手算範例 → 易錯點與 30 秒自我檢核」。含 7 則手算範例、24 條 L3 深層知識展開、9 張內嵌 SVG、七章 L3 卡關清單（33 項可勾選）。公式來源全部追溯：0.6 ← von Mises 1/√3；BSR 上限式 ← 長剪切面先整段剪力降伏（判準 Anv/Agv > Fy/Fu）；U=1−x̄/L ← 力繞過角部需傳力距離；L_opt = L_weld（通則，此時 U=0.5）；Cc = √(2π²E/Fy) ← Fe = Fy/2 ＝殘留應力使降伏啟始；ASD 的 FS 由 5/3 連續變化至 23/12；λc² = Fy/Fe（可推導）；0.877 ← 初始彎曲缺陷折減；0.658^λ² ← 隱含拋物線殘留應力分布故平滑（對照本題塊狀分布產生 B/B′ 跳躍）；G = 柱／梁勁度比 ← 「梁夾得住柱嗎」；LeMessurier ΣP ≤ ΣPe ← 側移挫屈為整層模態故柱間可互相支援。
- 2026-07-30｜VERIFY｜上述講義之 87 項數值主張以 Python 獨立重算逐項交叉比對，全部通過（tolerance 0.5～2%）。同時發現並修正來源解析之單位量級筆誤一處：`SS-2013-2.md` 將 π²EIc 寫為「605,946 tf·cm²」，正確值為 6.059×10⁸ tf·cm²（後續 Pe 數值本身正確，僅該中間式量級掉 10³）。講義內採正確寫法並於附錄註明；因 `raw/solutions/SS-2013-2/` 受規則 1、2 保護，未修改來源檔。
- 2026-08-08｜STUDY-REFACTOR｜重構 `study/study-SS-U1-1.html`，由「七區段深度複習頁」改為單一主題的**命題情報頁（只留 ① 命題分析）**。動機：同子項三份教材內容大量重疊 —— ② 截面圖解 ≈ `lecture-SS-U1-1.html` §1.1／§4.2／§8.1、③ 解題流程圖 ≈ lecture §9、④ 核心公式速查 ≈ `formula-given-SS-U1-1.html` §二（且後者多了 24 年考卷「給／背」證據，屬上位版）、⑥ 高頻陷阱 Top 8 ≈ lecture §11。三檔重新分工為：lecture＝為什麼（原理）、formula-given＝要不要背（記憶決策）、study＝考什麼（可由 `question_index.json` 重生的命題事實）。刪除區段 ②③④⑥⑦（⑦ LRFD 柱強度計算器經確認直接刪除），保留並擴充 ① 為六個區塊：1.1 出題概況（KPI＋年度堆疊圖＋題型圓餅）、1.2 考點結構（四類可篩選卡片）、1.3 考點漂移（2002–2013 vs 2014–2025 對切）、1.4 ASD／LRFD 走向、1.5 考題清單（主 24 ＋副 7 ＝ 31 題）、1.6 命題風險排序。頁面標題由「深度複習」改為「命題分析」；檔名不變（`lecture-SS-U1-1.html`、`formula-given-SS-U1-1.html` 均有連回本檔）。
- 2026-08-08｜DATA-FIX｜上述重構過程中，以 `raw/json/question_index.json` 重新統計並修正原頁三處錯誤／缺漏：① KPI「近 6 年出題 6/6」有誤 —— U1-1 主考點在 2019、2020、2021 連續三年空白，2020–2025 六個考年中僅 4 年出題（共 7 題），已改為「4/6」；② 考題清單原僅列 24 題主考點，遺漏 7 題副考點（SS-2002-1、SS-2003-3、SS-2004-2、SS-2007-1、SS-2009-3、SS-2012-3、SS-2019-3），現併入清單並以虛線灰底與「副・所屬子項」標籤區分，篩選鈕新增「僅主考點／僅副考點」；③ 題號連結仍指向舊式 `../index.html#md=raw/solutions/...`（瀏覽器顯示未渲染純文字），已全數改指 `problems-view/SS-YYYY-N.html`，31 個連結逐一確認檔案存在。另新增每題 designMethod 色籤（LRFD／ASD／混合／概念題）。
- 2026-08-08｜ANALYSIS｜本輪由統計得出、原頁未呈現的三項命題觀察（均可由 `question_index.json` 複算）：① **考點漂移**：把 24 題對切為前後各 12 題，有效長度 K 值由 6 題降至 1 題（且該題 SS-2023-1 為概念題，最後一題計算型停在 SS-2013-2，空窗 12 年），柱挫屈強度由 2 題升至 6 題，拉力桿件由 1 題升至 4 題 —— 依「歷史總題數」分配複習時間會高估 K 值、低估柱強度曲線推導；② **ASD 未退場**：ASD 於前 12 年僅 1 題，後 12 年 5 題，近 4 年（2022–2025）更佔 3/6，`Cc`／變動 `FS`／`Fa` 兩段式不可當舊制跳過；③ **風險排序**：柱強度曲線推導＋殘留應力（近 12 年 3 次、題型幾乎重複）與剪力遲滯 U 值（連兩年、每次換載體）列為高風險，對位圖計算題（歷史第二高頻但空窗 12 年）與組合柱平行軸定理（空窗 10 年）列為中高風險，SRC 複合柱（空窗 22 年）列為低風險。
- 2026-08-08｜BUGFIX｜`study/problems-view/` 全 88 個渲染頁的「← 返回講義」按鈕按了沒反應。原因：按鈕寫的是 `href="javascript:history.back()"`，而 `study-*.html` / `lecture-*.html` 的題號連結一律帶 `target="_blank"`，新分頁沒有上一頁歷史，`history.back()` 因此無效（不是連結壞掉，是分頁沒有回頭路）。修正為三段 fallback：優先 `document.referrer`（新分頁仍會帶入來源頁，可正確回到講義或命題分析頁）→ 其次 `history.back()`（同分頁開啟的情況）→ 最後退回根目錄 `../../index.html` 儀表板（直接開檔、無 referrer 時）。88 檔全數套用，兩種既有寫法（`←` 與 `&#8592;`）皆已統一。
- 2026-08-08｜UX｜`study/problems-view/` 全 88 頁的返回列改為兩顆按鈕，解決「返回講義」名實不符的問題。原本單一按鈕寫「返回講義」但實際行為是 `history.back()`（回上一頁），且該題的講義未必等於來源頁 —— 例如 SS-2002-1 主分類為 SS-U1-2 梁桿件、SS-U1-1 只是副分類，卻可從 `study-SS-U1-1.html` 點進來。現拆為：①「← 上一頁」沿用 referrer → history → 根儀表板三段 fallback，回到實際點進來的那一頁；②「📘 Un-m 單元名 講義」為每檔靜態產生的固定連結，指向該題**主分類單元**的 `lecture-SS-Un-m.html`。主分類無講義的 6 題（SS-2005-4、SS-2009-1、SS-2009-2、SS-2012-2、SS-2020-1、SS-2020-2）改指第一個有講義的副分類單元並於按鈕標註「（副分類）」。分布：U1-1 24、U1-2 23、U1-3 12、U1-4 21、U2-3 8，合計 88，五個目標講義檔均已確認存在。單元代碼與名稱依 `question_index.json` 的 primaryTopicId 產生，非人工填寫。
- 2026-08-08｜UX｜`study/problems-view/` 全 88 頁的「← 上一頁」改為「🔍 Un-m 速查頁」，靜態指向該題主分類單元的 `study-SS-Un-m.html`（命題分析頁）。原本的 referrer／history fallback 屬「回上一頁」語意，按鈕文字看不出會去哪；改為與旁邊的「📘 講義」按鈕採同一套單元推導，兩顆按鈕永遠指向同一單元的兩份教材，行為可預測。分布：U1-1 24、U1-2 23、U1-3 12、U1-4 21、U2-3 8，合計 88；已程式驗證 88 檔的 study-／lecture- 連結單元完全一致，且五個目標速查頁檔案均存在。註：因採主分類推導，跨單元的題目兩顆按鈕會指向主分類單元而非來源頁 —— 例如 SS-2003-3（主分類 U1-4、副分類 U1-1）即使從 `study-SS-U1-1.html` 點入，兩顆按鈕仍指向 U1-4。
- 2026-08-08｜UX｜`study/problems-view/` 全 88 頁改為「跟隨來源單元」：頁尾注入一段小腳本，讀取 `document.referrer`，若來源是 `study-`／`lecture-`／`formula-given-SS-Un-m.html`，就把「🔍 速查頁」與「📘 講義」兩顆按鈕同時改指向**來源那個單元**並改寫按鈕文字；來源不明（直接開檔、從儀表板進入）時維持 HTML 內靜態的主分類單元連結。因此 SS-2003-3（主分類 U1-4、副分類 U1-1）從 `study-SS-U1-1.html` 點入時，兩顆按鈕會顯示並指向 U1-1；從別處進入則回到 U1-4。設計取捨：靜態 href 保證無 JS／無 referrer 時仍可用，JS 只做覆寫，不是唯一路徑。
- 2026-08-08｜INCIDENT｜作業過程中 `study/problems-view/SS-2002-2.html` 曾被清為 0 位元組。原因：批次腳本寫成 `open(f,'w').write(re.sub(...))`，Python 先開檔（'w' 立即截斷內容）才計算取代結果，而該次 `re.sub` 的 replacement 字串含 `\d` 觸發 `re.error: bad escape`，例外中斷時檔案已被清空，且該檔為排序後第一個處理對象。已由 `git show HEAD:study/problems-view/SS-2002-2.html` 取回原始版本，重新套用三項變更（兩顆按鈕、CSS、跟隨腳本）後寫回，並驗證 17,428 bytes、按鈕指向 SS-U1-2 梁桿件（與 `question_index.json` 的 primaryTopicId 一致）。後續批次改用 `lambda _: SCRIPT` 作為 replacement 避免跳脫字元被解讀，並在寫檔前先完成字串運算。最終全 88 檔通過檢查：各含 1 組 quick／lect 按鈕與 1 份跟隨腳本、結尾標籤完整、無 `javascript:history.back` 殘留、study- 與 lecture- 連結單元 100% 一致。
- 2026-08-08｜SKILL｜新增 `skills/unit-exam-intel/`（SKILL.md 17.8 KB）與打包檔 `skills/unit-exam-intel.skill`，把本輪 `study-SS-U1-1.html` 的重構做法固化為六科（SS/RC/SA/SD/SM/MM）通用流程。輸出 `study/study-XX-Un-m.html`（單一自包含 HTML，不產 PDF —— 本頁價值在可篩選清單、可點題號與 Canvas 圖表，列印會損失一半功能，且資料隨新考卷改變，紙本易過期）。六個區塊：出題概況／考點結構／考點漂移／設計法（或題型）走向／考題清單（主＋副）／命題風險排序。三份 study 教材的分工在 SKILL.md 開頭明訂：lecture＝為什麼、formula-given＝要不要背、unit-exam-intel＝考什麼（唯一純資料驅動、可自動重生者）。
- 2026-08-08｜SKILL｜`unit-exam-intel` 的核心設計原則是「**頁面上每個數字都必須由程式算出，不可手打**」，並以兩支純標準函式庫腳本落實：`scripts/stats.py` 從 `question_index.json` 算出 KPI、全科排名與前三名、考年總數與命中年數、連續空窗年段、前後對切、各期設計法分布、標籤頻率、含主副旗標的完整題目清單；`scripts/verify.py` 反向對帳成品頁的 `Q[]` 題號集合、逐題主副旗標與 designMethod、篩選鈕括號數字（含「僅主／僅副」）、四個 KPI、題號連結是否都存在對應 `problems-view/*.html`、以及三種禁用寫法（`../index.html#md=`、`javascript:history.back()`、區塊編號 `1.1`），任一不過即以離開碼 1 逐條列出。已用「故意改壞」測試確認 verify.py 抓得到篩選鈕數字與 KPI 的不一致。
- 2026-08-08｜DATA-FIX｜撰寫 skill 時以 `stats.py` 回頭核對 `study/study-SS-U1-1.html`，又抓到一處本輪自己寫錯的數字：KPI 副標與註腳寫「2020–25 共 7 題」，實際為 **6 題**（SS-2022-2、2023-1、2023-2、2024-1、2024-2、2025-2）。兩處已更正。這正是把統計寫成腳本的理由 —— 同一份資料手數兩次，兩次都可能錯。
- 2026-08-08｜SKILL｜六科差異已在 SKILL.md 內處理：① `designMethod` 欄位並非各科都有，`stats.py` 以 `method.available` 標記，缺欄位時（SA、MM 等）改用題型／解法／主題年代分布等其他軸線，不得硬掰；② 主考點 < 8 題時跳過「考點漂移」區塊（對切無統計意義）；③ `study/problems-view/` 為選用，缺席時題號退化為純文字並於頁尾註明；④ 各科分群軸線建議已列表（SS/RC 依構件或極限狀態、SA 依解法、SD 依自由度與規範、SM 依土壤主題、MM 依力學主題）。另附 `reference/template.html`（23.3 KB，含全部 CSS、篩選邏輯與兩張 Canvas 圖），以 `{{UNIT}}` 等 8 個佔位符參數化。
- 2026-08-08｜STUDY-REFACTOR｜以 `unit-exam-intel` skill 重構 `study/study-SS-U1-4.html`，由七區段「深度複習頁」改為只回答「這個單元考什麼」的**命題情報頁**。重疊盤點結果：② 接合圖解 ≈ `lecture-SS-U1-4.html` §1–§7、③ 解題流程圖（偏心接合彈性向量法）≈ lecture §6／§10、④ 核心公式速查 ≈ `formula-given-SS-U1-4.html` §二（後者多了 37 條公式 × 24 年考卷「給／背」證據，屬上位版）、⑥ 高頻陷阱 Top 8 ≈ lecture §12，四段全部刪除並改為連結；⑦ 互動計算器（填角銲設計強度）為唯一不重複內容，經與使用者確認後直接刪除。保留並擴充 ① 命題分析為六個無編號區塊：出題概況（四張 KPI＋年度堆疊圖＋題型圓餅）／考點結構（五群可篩選卡片）／考點漂移（2002–2009 前 9 題 vs 2012–2024 後 10 題）／設計法走向／考題清單（主 19 ＋副 7 ＝ 26 題）／命題風險排序。考點分群依「解題套路」而非標籤字面，每題只歸一群：🔩 螺栓與接合端極限狀態 10、🌀 偏心接合（彈性向量法）5、🔥 銲接強度與剪力流 2、🏗️ 梁柱接頭與耐震細部 4、📘 機制／破壞模式／施工概念 5。檔名不變（`lecture-SS-U1-4.html` 與 `formula-given-SS-U1-4.html` 均已有連回本檔的按鈕，無須新增）。全頁數字由 `scripts/stats.py` 產出，`scripts/verify.py` 七項對帳全數通過。
- 2026-08-08｜DATA-FIX｜`scripts/verify.py` 對帳時揪出 `raw/json/question_index.json` 的 designMethod 錯誤：**SS-2006-2 與 SS-2006-5 標為 `LRFD`，但兩題的解析 .md（受規則 1、2 保護的證據）皆明載「設計法：概念題」，且兩題確實全為說明繪圖題**（2006-2 問預拉力意義／塊狀剪力／FCAW 全名／工地銲接濕度風速限制；2006-5 要求繪梁柱接頭細部並說明連續板功能）。以程式比對全庫 98 題後發現 **2006 年四題（SS-2006-1、-2、-4、-5）全被填為 `LRFD`**，研判為整年預設值未逐題修正。經使用者確認後將此四題的 `designMethod` 一律改為 `概念題`（索引為規則 1 的兩處例外之一，可人工維護；本次僅改該欄位，`git diff --numstat` 確認全檔僅 5 行變動，未重排格式）。連帶影響：SS-U1-4 設計法分布由「ASD 5／LRFD 10／概念題 4」更正為「**ASD 5／LRFD 8／概念題 6**」，前段（2002–2009）由「LRFD 5／ASD 3／概念題 1」更正為「**LRFD 3／ASD 3／概念題 3**」；`study-SS-U1-1.html`（SS-2006-1）與 `study-SS-U1-2.html`（SS-2006-4）的設計法走向表亦受影響，尚未重跑，下次觸碰該兩頁時應以 `stats.py` 重新產出。另註：同一次掃描發現 16 筆 .md 與索引的措辭差異（如「概念題（含計算）」vs「概念題」、「混合（ASD + LRFD）」vs「混合」），屬同義不同寫法，未動。
- 2026-08-08｜ANALYSIS｜SS-U1-4 由統計得出的三項命題觀察（全部可由 `stats.py` 複算）：① **考點漂移** —— 主考點 19 題對切後，偏心接合（彈性向量法）由前段 4 題（SS-2002-4、2004-3、2005-3、2007-1）降至後段 1 題（SS-2017-4），**已空窗 8 年**；銲接強度與剪力流由 0 升至 2（SS-2018-3、2019-4 連兩年，前段從未單獨出過非偏心的銲道強度計算）；梁柱接頭主考點僅 SS-2006-5 與 SS-2024-4（相隔 18 年），但同期以副考點形式掛在 SD-U3-1 出現兩次（SS-2012-2、2020-1）——「這個考點沒有消失，只是換了門牌」。重心由「把偏心接合算出來」漂向「把接合為什麼會壞說清楚」。② **題型走向** —— 概念題占比由前段 3/9 升至近 6 考年（2020–2025）**3/5**；同期計算題僅存 SS-2020-4（ASD）與 SS-2021-2（LRFD）各一，ASD 未退場且兩題 ASD（2018-3 銲道容許應力、2020-4 A490 `F_va`=2.8 tf/cm²）都是完整容許應力檢核。③ **風險排序** —— 偏心接合彈性向量法（歷史 5 題、空窗 8 年、題型固定且四次考試全零公式）與銲接破壞形式／HAZ（SS-2023-4、2024-4 連兩年）列高風險；梁柱接頭細部（主考點空窗 18 年）與塊狀剪力多路徑（跨 6 題、一半為副考點）列中高風險；斷續銲剪力流（24 年僅 SS-2019-4 一次、且與 U1-2 重疊）列低風險。另註出題密度：24 個考年中 15 年出現，空窗集中於 2010–2011 與 2013–2016 兩段；近 6 考年僅 4 年出題共 5 題，為本單元二十四年來最低密度。
- 2026-08-08｜STUDY-REFACTOR｜以 `unit-exam-intel` skill 重構 `study/study-SS-U1-2.html`，由七區段「深度複習頁」改為命題情報頁。重疊盤點：② Mn–Lb 設計曲線與斷面分類圖解 ≈ `lecture-SS-U1-2.html` §1–§3、③ 解題流程圖 ≈ lecture §10、④ 核心公式速查（八個子節）≈ `formula-given-SS-U1-2.html` §二（後者多了 33 條公式 × 24 年考卷「給／背」證據）、⑥ 高頻陷阱 Top 8 ≈ lecture §12，四段刪除改為連結；⑦ 互動計算器（LTB 公稱彎矩）為唯一不重複內容，經使用者確認後刪除（與 U1-4 的填角銲計算器同一處置）。擴充為六個無編號區塊。考點分五群、每題只歸一群：🌀 LTB 側扭挫屈三區段 11、📏 斷面分類與塑性彎矩 6、📐 斷面選擇與使用性檢核 2、🧱 合成梁與 SRC 2、✂️ 腹板剪力與剪力流 4，清單主 21 ＋副 4 ＝ 25 題。互連按鈕四顆（lecture／formula-given 之 HTML＋PDF 均存在），`lecture-SS-U1-2.html` 與 `formula-given-SS-U1-2.html` 原本就有連回本檔的按鈕，未新增。`verify.py` 七項對帳全過。
- 2026-08-08｜DATA-FIX｜本頁的設計法分布已反映同日 U1-4 那輪對 `question_index.json` 的修正：**SS-2006-4（板梁剪力挫屈與張力場，純概念繪圖題）原被誤填為 `LRFD`，已改為 `概念題`**（該筆屬 2006 年整年四題誤填的一部分，另三題為 SS-2006-1／-2／-5）。連帶更正：U1-2 設計法全期由「LRFD 16／ASD 3／概念題 2」變為「**LRFD 15／ASD 3／概念題 3**」，前段（2002–2011）由「LRFD 7／ASD 2／概念題 1」變為「**LRFD 6／ASD 2／概念題 2**」。舊頁的區段標題另有一處分群數字與本輪不同（舊頁寫「LTB 12 題」），差異來源為分群準則改變而非資料錯誤——舊頁把 SS-2015-1（三分點集中力梁的 LTB＋剪力＋撓度全檢核）計入 LTB 群，本輪依「每題只歸最主要的解題套路」原則改列入「斷面選擇與使用性檢核」群，與 SS-2010-4 同群。
- 2026-08-08｜ANALYSIS｜SS-U1-2 由統計得出的三項命題觀察（全部可由 `stats.py` 複算）：① **出現率全科最高** —— 24 個考年中 17 年出現（U1-1 為 18/24 但總題數較高、U1-4 僅 15/24），空窗只有 2003–2004 與 2017–2018 兩段各兩年，且兩次都在隔年立刻回歸（2005、2019）。② **考點漂移** —— 主考點 21 題對切後，LTB 側扭挫屈維持 5→6（二十四年沒有中斷超過三年，近年 2021-3／2024-3／2025-3 三度出現，變的只是包裝：求 φbMn → 反求載重 → 強弱軸對照 → 概念說明）；斷面分類與塑性彎矩由 1 升至 3（2016-1、2023-3、2025-1，**2023 起連三年**），是升溫最快的一群；腹板剪力與剪力流由 2 降至 0，主考點**空窗 19 年**（最後為 2006-4），僅以副考點形式延續於 2019-4、2020-4；整梁設計題（選斷面＋剪力＋撓度）**空窗 10 年**（最後為 2015-1）。重心由「把一根梁完整設計出來」收斂到「把斷面的本錢算清楚」。③ **設計法** —— ASD 自 2016-1 之後**連續 6 個考年零出現**，近 6 考年 5 題中 4 題為 LRFD 計算題、1 題概念題；本單元是六個子項中最能安心把重心放在 LRFD 的一個，與 U1-3（ASD 梁柱互制式幾乎必給必考）恰成對比。④ **風險排序** —— LTB 三區段（11 題、佔本單元 52%、空窗 0 年）與斷面分類／Mp（6 題含 U2-1 兩題副考點、空窗 0 年）列高風險；合成梁／SRC（2 題、空窗 6 年、兩題套路完全相同）與整梁設計（2 題、空窗 10 年、唯一同時考三條檢核線的題型）列中高風險；板梁張力場（1 題、空窗 19 年）列低風險。
- 2026-08-08｜STUDY-REFACTOR｜以 `unit-exam-intel` skill 重構 `study/study-SS-U2-3.html`，由七區段「深度複習頁」改為命題情報頁。重疊盤點：② 主題地圖（施工要求四大領域）≈ `lecture-SS-U2-3.html` §0–§6、③ 概念題答題架構 SOP ≈ lecture §7、④ 知識卡速查（八張卡）≈ `formula-given-SS-U2-3.html` §二（後者多了 38 條規定 × 24 年考卷「給／背」證據）、⑥ 高頻陷阱 Top 8 ≈ lecture §9，四段刪除改為連結；⑦ 快問快答翻卡為唯一不重複內容，經使用者確認後刪除（功能與 lecture §10「自我檢測 12 個為什麼」相近；與 U1-4 填角銲計算器、U1-2 LTB 計算器同一處置）。考點分五群、每題只歸一群：🛡️ 防蝕與塗裝 3、🔥 銲接施工細節與瑕疵 3、🏗️ 耐震構架的加嚴要求 3、🔍 非破壞檢測 NDT 2、🔩 高強度螺栓施工 2，清單主 7 ＋副 6 ＝ 13 題。`verify.py` 七項對帳全過。
- 2026-08-08｜STRUCTURE｜本頁與前三個單元有兩處結構差異，均為 skill 明訂的例外處理：① **跳過「考點漂移」區塊** —— 主考點僅 7 題，低於做前後對切的門檻（8 題），`stats.py` 的對切結果為前段 3 題／後段 4 題，樣本太小，硬做會給出不穩且誤導的結論；趨勢改以出題概況的一行註腳描述（主考點 2016–2022 密集 5 題後 2023 起連三年掛零，同期改以副考點形式在 U1-4 出現三次）。② **「設計法走向」改軸線** —— 本單元 13 題 `designMethod` 全部是「概念題」，做 ASD／LRFD 表毫無資訊量，改用「現身形式」軸線：期間 × 主考點／副考點掛 U1-4／副考點掛其他，三列分別為 2002–2013（2／1／2＝5）、2014–2025（5／3／0＝8）、近 6 考年 2020–2025（2／3／0＝5）。此表回答了一個舊頁完全沒呈現的事實：**近 6 考年副考點（3）多過主考點（2）**。
- 2026-08-08｜ANALYSIS｜SS-U2-3 由統計得出的三項命題觀察（全部可由 `stats.py` 複算）：① **主考點 7 題但實際要準備 13 題** —— 6 題副考點裡 **4 題掛在 SS-U1-4 接合**（2009-4、2021-4、2023-4、2024-4），另兩題掛 U1-2（2002-1 銲條乾燥）與 SD-U3-1（2009-2 節點域）；2014 年之後副考點**全部集中到 U1-4**，不再散落其他單元，故最有效率的準備方式是把本單元與 U1-4 綁在一起讀。② **出現節奏是「一陣一陣」** —— 24 個考年只有 7 年出現主考點，空窗四段（2002–2003、2005–2009、2011–2015、2023–2025），但 2016–2022 七年內密集出了 5 題（2016-2、2018-4、2019-1、2021-1、2022-3）。③ **風險排序** —— 防蝕與塗裝（7 題主考點中佔 3 題、歷史最高頻、空窗 6 年、答案結構固定）與 NDT（跨主副共 4 題、近 4 個考年出現 3 次、每次換問法）列高風險；耐震加嚴細部（3 題、關鍵數字 `tz≥(dz+wz)/90` 與板厚 `≥40 mm` 用 SN-C 皆 24 年零次印出）與高強度螺栓施工（主考點空窗 21 年、但 2021-4 以副考點回歸）列中高風險；銲接細節規定（回銲 end return、銲條乾燥，主題極窄各只考過一次）列中低風險。另註：本單元 13 題全為概念說明題，零計算，得分關鍵在答題骨架而非算式。
- 2026-08-08｜STUDY-REFACTOR｜以 `unit-exam-intel` skill 重構 `study/study-SS-U1-3.html`，由七區段「深度複習頁」改為命題情報頁。重疊盤點：② P–M 互制曲線與二階效應圖解 ≈ `lecture-SS-U1-3.html` §1／§2／§6、③ 解題流程圖（LRFD B1/B2 標準流程）≈ lecture §10、④ 核心公式速查（六個子節）≈ `formula-given-SS-U1-3.html` §二（後者多了 40 條公式 × 24 年考卷「給／背」證據）、⑥ 高頻陷阱 Top 8 ≈ lecture §12，四段刪除改為連結；⑦ 互動計算器（LRFD H1 互制檢核）為唯一不重複內容，經使用者確認後刪除（與 U1-4 填角銲、U1-2 LTB、U2-3 快問快答同一處置，四個單元一致）。考點分四群、每題只歸一群：🅰️ ASD 互制三式 5、🅱️ LRFD H1 互制檢核 3、🔺 二階效應放大（B1／B2、Mnt／Mlt）2、📘 規範層次的延伸（直接分析法／強柱弱梁）2，清單主 11 ＋副 1 ＝ 12 題。`verify.py` 七項對帳全過。至此 SS 六個子項中的五個（U1-1、U1-2、U1-3、U1-4、U2-3）皆已改為命題情報頁。
- 2026-08-08｜NOTE｜本輪未發現 `question_index.json` 的資料錯誤（U1-3 的 12 題 designMethod 與各題 .md 標示一致，前三輪的 2006 年整年誤填未波及本單元）。舊頁的分群與本輪相同軸線但一群僅 1 題（「直接分析法（1題）」違反 skill 的「每群至少 2 題」），本輪將 2011-1 與副考點 2009-1（強柱弱梁，主考點掛 SD-U3-1）合併為「規範層次的延伸」群——兩題的共同性質是 designMethod 皆為概念題、且都在問「規範為什麼這樣要求」而非代數字。另舊頁未列副考點（僅 11 題），本輪補入 SS-2009-1 成為 12 題。
- 2026-08-08｜ANALYSIS｜SS-U1-3 由統計得出的四項命題觀察（全部可由 `stats.py` 複算）：① **一題吃三個單元** —— 本單元只負責需求側（把內力放大），強度側的 `φcPn` 來自 U1-1、`φbMn` 來自 U1-2，故 11 題主考點實際檢驗三個單元的內容。② **考點漂移** —— 對切後 ASD 互制由 4 降至 1（2008 年後只回來過 2019-3 一次），LRFD H1 由 0 升至 3（2012-3、2020-3、2022-1，題型高度一致），B1／B2 二階放大由 0 升至 2（2013-4、2014-4 連兩年後**空窗 11 年**，是本單元空窗最久的計算題型），直接分析法由 1 降至 0（2011-1 唯一一次，空窗 14 年）。重心由「ASD 三式代數字」漂向「LRFD 的需求端怎麼被二階效應放大」。③ **設計法分界全科最乾淨** —— 前段（2003–2011）LRFD 掛零、ASD 4 題；後段（2012–2022）LRFD 5 題、ASD 僅 2019-3 一題（但配分 30 分）；近 6 考年 2 題全為 LRFD。④ **風險排序** —— LRFD H1 雙軸彎矩互制（3 題、空窗 3 年、唯一在近 6 考年出現的題型）與 B1／B2 放大（2 題、空窗 11 年、且 `Mu=B1·Mnt+B2·Mlt` 二十四年零次印出）列高風險；ASD 互制三式（5 題、歷史最高頻、但公式幾乎必給故準備成本低）與 K 值／對位圖併入梁柱（2013-4 唯一一次、與 U1-1 同步空窗 12 年）列中高風險；強柱弱梁 P-M 曲線（空窗 16 年、多半以耐震題回歸）與直接分析法（空窗 14 年、屬規範改版當年的「新聞題」）列中／低風險。另註：本單元 11 題主考點**全數附 P–M 互動圖**，是全科互動圖覆蓋率最高的單元。
- 2026-08-08｜UX｜全站把「速查頁」正名為「命題分析」，並移除 Keynote 按鈕。動機：`study-SS-Un-m.html` 五個單元已全部重構為命題情報頁（只回答「這個單元考什麼」），「速查頁」這個舊名稱描述的是重構前的七區段深度複習頁，名實不符；且 Keynote 按鈕指向的課堂投影片 PDF 與三份教材（lecture／formula-given／study）的分工重疊，使用者已明確要求移除。改動範圍：① **五份觀念講義** `lecture-SS-U1-1/-2/-3/-4/-U2-3.html` 的 header 按鈕列——「📊 速查頁」改為「📊 命題分析」（title 同步改為「命題分析：出題頻率、考點結構、考題清單、命題風險」，底色由灰 `#eceff1` 改為藍 `#e3f2fd`／`#1565c0` 以與講義本身的灰階按鈕區隔）、刪除「📄 Keynote」按鈕；② **U1-1、U1-3、U2-3 三份講義補上「🎯 給／背分界」按鈕**（U1-2、U1-4 原本就有），五份講義現在的按鈕列一致為「命題分析／給／背分界／本頁 PDF」三顆；③ `lecture-SS-U1-2.html` 內文的「使用順序建議：本講義（練題前）→ Keynote（課堂）→ 速查頁（考前）」改為「本講義（練題前）→ 給／背分界（決定背誦優先序）→ 命題分析（考前排練題順序）」，與三份教材的分工一致。
- 2026-08-08｜BUGFIX｜上述作業中發現 `lecture-SS-U1-3.html` 與 `lecture-SS-U2-3.html` 的 `<nav>` 尾端各有**兩顆未套樣式的殘留連結**：`<a href="formula-given-SS-U1-3.html">▶ U1-3 給／背分界</a>` 與 `<a href="formula-given-SS-U2-3.html">▶ U2-3 給／背分界</a>`，兩檔都同時含這兩顆——亦即 U1-3 的講義掛著指向 U2-3 的按鈕、U2-3 的講義掛著指向 U1-3 的按鈕，是先前批次插入時未依單元區分所致。兩檔的四顆殘留連結已全數移除，改為各自單元一顆、與 U1-2／U1-4 相同樣式（`#ffebee`／`#c62828`）的正式按鈕。
- 2026-08-08｜UX｜`study/problems-view/` 全 88 個題目渲染頁同步正名：header 的「🔍 Un-m 速查頁」按鈕文字與 `title` 屬性改為「🔍 Un-m 命題分析」，並同步改寫頁尾「跟隨來源單元」腳本內用來覆寫按鈕的兩個字串（`q.title` 與 `q.innerHTML`），確保由 `study-`／`lecture-`／`formula-given-SS-Un-m.html` 點入時動態改寫的文字也是新名稱。分兩批處理：82 檔為標準寫法，另 6 檔（SS-2005-4、SS-2009-1、SS-2009-2、SS-2012-2、SS-2020-1、SS-2020-2）因主分類單元無教材而採「（副分類）」變體寫法，第一批的樣式比對不到、被驗證擋下後單獨修正——這正是「先算完字串、驗證通過才寫檔」的作法擋下誤改的一次實例（對照 2026-08-08 的 SS-2002-2 清空事故）。88 檔全數通過結構檢查：各含 1 組 quick／lect 按鈕、結尾標籤完整、全站已無「速查頁」字樣殘留。
- 2026-08-08｜DOCS｜「速查頁 → 命題分析」正名的第二輪：把用語修正推到**所有設定檔與 skill 原始碼**，避免下次產頁時又照舊規格做出 Keynote 按鈕。逐檔改動：① `skills/unit-lecture/SKILL.md` —— 開頭「這不是速查表」段改為指出同子項另有 `study-`（命題分析：考什麼）與 `formula-given-`（給／背分界：要不要背）兩份教材、三者並存；「與同子項既有教材互連」整節重寫（教材表由四列縮為三列並加上「回答什麼／產出者」欄、刪除「使用者自備課堂 Keynote／投影片」那一列、nav 範例由「速查頁／Keynote／本頁 PDF」改為「命題分析／給／背分界／本頁 PDF」三顆並附 title 與新配色、加入兩則 ⚠️ 明文禁令：`study-` 的正式名稱是「命題分析」不是「速查頁」、不要放 Keynote 或課堂投影片按鈕）；Step 8 驗證清單第 5 項加上「nav 內沒有 Keynote 按鈕、全檔沒有『速查頁』字樣」。② `CLAUDE-CODE.md` 的 STUDY 節加註「子項層級已改由 `unit-exam-intel` 負責，下方七區塊為 2026-08 以前的舊規格，不要照舊產頁」，並把 `unit-lecture` 二欄分工表擴為 `lecture-`／`formula-given-`／`study-` 三欄。③ `CLAUDE-SPEC.md` 的檔名前綴表補上 `formula-given-` 一列，`study-` 的定位由「速查／複習頁」改為「命題分析」並註明子項層級由 `unit-exam-intel` 產出；1.2 節的禁令改為「不可命名為 `study-SS-UN-n.html`（會覆蓋該子項的命題分析頁）」。④ `skills/README.md` 的兩張分工表、`skills/unit-formula-map/SKILL.md` 與 `skills/unit-exam-intel/SKILL.md` 的相關描述、`知識庫使用說明書.md` 的指令表與目錄樹、`檔案架構索引表.md` 的 `study/` 與 `skills/` 兩列，全部同步為三份教材的新分工。
- 2026-08-08｜BUGFIX｜上述盤點另外抓到 `CLAUDE-CODE.md` STUDY 節殘留一條**與現行規則相牴觸的指示**：「【重要】點擊題號或標題時，必須以 `<a href="../index.html#md=raw/solutions/SS-XXXX-N/SS-XXXX-N.md&t=SS-XXXX-N">` 格式連結至 markdown 渲染器」。這正是 `unit-exam-intel` 的 `verify.py` 第 6 項明文禁止、且 2026-08-08 稍早才從 `study-SS-U1-1.html` 全數清掉的舊式連結（把 .md 丟給瀏覽器，公式與附圖不會渲染）。已改為「一律連 `problems-view/SS-XXXX-N.html`，禁止使用 `../index.html#md=`」，並說明 `study/problems-view/` 是全部題目的 HTML 渲染層。若未修，下次執行單元層級 `study` 指令會再度產出未渲染的連結。
- 2026-08-08｜PACKAGE｜重新打包 `skills/` 下三個 `.skill` 檔，使其與專案版原始碼一致：`unit-lecture.skill`（1 檔，15,706 → 16,221 bytes）、`unit-exam-intel.skill`（5 檔，26,470 → 25,674 bytes，排除 `__pycache__`）、`unit-formula-map.skill`（6 檔，19,560 → 19,578 bytes）。另記錄一項既存落差供日後處理：**已安裝版的 `unit-formula-map` 缺少整個 `scripts/` 目錄**（專案版有 `prerender.py`、`build_pdf.py`、`tex2svg.js`、`verify.py` 四支），且其 SKILL.md 少了「配套腳本」那段說明——即已安裝版比專案版舊。本輪依使用者選擇，改由使用者自行安裝重新打包後的 `.skill`，未以 `save_skill` 寫回帳號；在完成安裝前，實際觸發的仍是舊版 skill。
