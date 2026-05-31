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
