# 結構工程技師考試知識庫 — 鋼結構設計（SS）
# 解題指令手冊（CLAUDE-SOLVE.md）

> **使用環境：Cowork**
> 在 Cowork 開啟 `exam-wiki-SS/` 資料夾後，此檔案提供解題、分析的完整規範。
> wiki 的維護（ingest/compile/lint）請使用 Claude Code，詳見 CLAUDE.md。

---

## 操作指令（Cowork 執行）

---

### 【ADD-METHOD】新增解題方法論（在 Cowork 執行）

**觸發方式：** 在 Cowork 討論某個解題方法後，說「加入知識庫」

**適用內容：**
```
解題工具型知識（跨多道題目使用）：
- 共軛梁法、虛功法、最小功法
- 彎矩分配法、傾角變位法
- 平行軸定理應用、組合斷面計算
- P-M 互制圖繪製
- 其他考試常用手算方法
```

**輸出物：**
```
1. raw/solutions/methods/[method-id]/[method-id].md
   → 完整說明文件（LaTeX 公式 + 步驟 + 邊界條件表）
2. raw/solutions/methods/[method-id]/[method-id]-chart.html
   → 圖形說明（如有）
```

**wiki/methods/[method-id].md 格式：**
```markdown
# [方法名稱]

**方法 ID：** [method-id]
**知識分類：** 解題工具
**適用題型：** [列出適用的 syllabusCode，如 `SS-U1-2`、`SS-U1-3`]

## 核心原理
## 邊界條件 / 對應關係表
## 步驟流程
## 常用型式與結果表
## 推導示範
## 圖形
## 出現題目（使用本方法的考題）
```

**你的後續動作：**
```
1. 加入手寫補充圖片（如有）
2. 在 Cowork 輸入：add method [method-id]
   → 生成 wiki/methods/[method-id].md
   → 更新 wiki/index.md（方法論區塊）
   → 在 wiki/log.md 追加紀錄
```

---

---

### 【SOLVE】解析一年考卷（在 Cowork 執行）

**觸發方式：** 在 Cowork 中開啟 `exam-wiki-SS/` 資料夾，輸入：
```
解析 [年份] 年考卷
例：解析 2014 年考卷
```

**Cowork 執行前置（自動）：**
```
自動讀取：
  - CLAUDE.md（身份層：分工、資料流、重要規則）
  - CLAUDE-SPEC.md（格式規範、命名規則、完成標準）
  - raw/exams/[對應考卷].pdf
  - raw/json/question_index.json（確認哪些題目已有解析）
不需要手動上傳任何檔案
```

**Cowork Project 設定建議：**
```
Project 名稱：exam-wiki-SS
指定資料夾：exam-wiki-SS/
指令檔：CLAUDE-SOLVE.md（設為 Project 指令）
```
設定完成後每次開啟 Project 即自動載入所有規範。

**執行規則：**
```
【階段一：建立資料夾並等待截圖（觸發語句後立即執行）】

1. 讀取 raw/exams/SS-YYYY_鋼結構設計.pdf（YYYY 為對應西元年）
2. 讀取 raw/json/question_index.json，找出尚無解析的題目
3. 為所有尚無解析的題目建立資料夾：
   → mkdir raw/solutions/SS-YYYY-N/（每題一個，已有解析者跳過）
4. 讀取考卷 PDF，瀏覽每道題目，判斷是否有附圖：
   → 有附圖的題目：列出，提醒使用者截圖並存入對應路徑：
       raw/solutions/SS-YYYY-N/SS-YYYY-N-fig-1.png
   → 無附圖的題目：標注「無需截圖」
5. 輸出截圖清單後停止，等待使用者通知「截圖完成，請開始解題」

【階段二：逐題解析（收到截圖完成通知後執行）】

6. 先讀考卷最後一頁的參考公式，確認適用公式
7. 依序解析尚無解析的題目，但每次只解一題：
   → 解完一題，存檔後停止
   → 使用者確認後說「繼續下一題」，再解下一題
   → 目的：避免單次輸出超過 32,000 token 上限
8. 每道題目輸出一份獨立的 .md 檔案：
   → 直接存入 raw/solutions/SS-XXXX-N/SS-XXXX-N.md
9. 所有數學公式使用 LaTeX 格式
10. 每份解析開頭必須包含標籤區塊
11. 判斷是否需要輸出互動圖（依「圖形觸發條件」）：
    → 直接存入 raw/solutions/SS-XXXX-N/SS-XXXX-N-[內容碼]-viz.html
```

---

#### 題目附圖規範（由使用者預先完成）

**責任分工：** fig PNG 截圖由**使用者**在解題前完成，存入對應資料夾後再通知 Cowork 解題。

**存檔命名規則：**（完整規格見 CLAUDE-SPEC.md §5）
```
raw/solutions/SS-YYYY-N/SS-YYYY-N-fig-1.png   ← 第一張題目附圖
raw/solutions/SS-YYYY-N/SS-YYYY-N-fig-2.png   ← 第二張（同題有多圖時）
```

**截圖品質要求（使用者截圖時確認）：**
```
✅ 圖片完整包含結構示意圖、幾何標示、載重符號
✅ 圖片不包含其他題目的文字
✅ 圖片頂部/底部有適當留白（避免截斷符號）
✅ 同題多子圖且相鄰 → 一次截成單一 fig-1.png
✅ 同題多子圖且位置分散 → 分別存為 fig-1.png、fig-2.png
```

**在 .md 中引用（雙重保險格式）：**
```markdown
![SS-YYYY-N 題目附圖：[精確描述結構型式、幾何、載重]](SS-YYYY-N-fig-1.png)

*圖說：[關鍵幾何數值、支撐條件、載重位置、斷面尺寸等完整文字說明]*
```

**無附圖題目（純文字題）的處理：**
> 若某題完全無結構示意圖、幾何圖或表格（題目僅以文字描述幾何與條件），
> **仍需建立資料夾**，但不建立 `fig-1.png`。
> .md 中不引用任何 fig PNG，直接以文字說明幾何條件。
> 常見無附圖題型：純概念說明題、已在題幹完整給出數字的計算題（如 SS-2022-1）。

---

#### 解題前置：三層掃描法（每題解題前先執行）

**核心原則：** 先見林（外在全貌）→ 再見樹（策略路徑）→ 後見土（內在意圖）

**第一層：外在掃描（2分鐘內完成）**
```
[目標] 這題最終要我交出什麼？（數字？圖表？OK/N.G.？）
[已知] 題目給了哪些數字和條件？（斷面、材料、載重、幾何、參考公式）
[待算] 從已知到目標，需要算出哪些中間參數？（Mu, Lb, Cb, U...）
```

**第二層：策略掃描**
```
[邏輯] 適用哪個設計邏輯？（見下方「設計哲學框架」）
[陷阱] 考官可能在哪裡挖了坑？（非標準型式、模糊地帶、易混淆觀念）
[捷徑] 有沒有條件可以跳過某些步驟？（結實斷面→跳過、Cw沒給→繞道）
```

**第三層：內在掃描**
```
[核心] 這題最重要的一個觀念是什麼？（強弱軸差異、剪力遲滯、殘留應力）
[線索] 特殊用字給了什麼暗示？（「無面外束制」→LTB、「忽略自重」→善意）
```

---

#### 設計哲學框架（解題邏輯對照）

**LRFD 梁桿件（SS-U1-2）**
```
核心：φbMn 取所有極限狀態中最脆弱一環
步驟：① 基準強度（全斷面塑性化 Mp）
      ② 局部挫屈檢核（結實/非結實斷面）
      ③ 側向扭轉挫屈 LTB（比較 Lb 與 Lp、Lr）
      ④ 剪力強度檢核（h/tw 三段式）
      ⑤ 使用性撓度（未因數化活載重）
```

**LRFD 壓力桿件（SS-U1-1）**
```
核心：φcPn 取所有極限狀態中最脆弱一環
步驟：① 基準強度（全斷面降伏 AgFy）
      ② 局部挫屈檢核
      ③ 整體彎曲挫屈（計算 λc → Fcr → Pn）
      關鍵：λc = (KL/rπ)√(Fy/E)
            λc ≤ 1.5 → 非彈性：Fcr = 0.658^(λc²) Fy
            λc > 1.5 → 彈性：Fcr = [0.877/λc²] Fy
```

**ASD 壓力桿件（SS-U1-1）**
```
核心：fa ≤ Fa（工作載重應力不超過容許應力）
步驟：① 計算需求應力 fa = P/A
      ② 計算 Cc = √(2π²E/Fy)，判斷挫屈類型
      ③ KL/r ≤ Cc → 非彈性：Fa = [1-(KL/r)²/2Cc²]Fy / FS
         KL/r > Cc → 彈性：Fa = 12π²E / 23(KL/r)²
      ④ 檢核 fa ≤ Fa
```

**LRFD 拉力桿件（SS-U1-1）**
```
核心：φtPn 取三種極限狀態最小值
步驟：① GSY 全斷面降伏：φt=0.9，Pn=FyAg
      ② NSF 淨斷面斷裂：φt=0.75，Pn=FuAe，Ae=UAn
         U值：查表（0.9/0.85/0.75）或 U=1-x̄/L
      ③ BSR 塊狀剪力：φ=0.75
         當 FuAnt ≥ 0.6FuAnv：Rn=0.6FyAgv+FuAnt
         當 0.6FuAnv ≥ FuAnt：Rn=0.6FuAnv+FyAgt
         上限：φ[0.6FuAnv+FuAnt]
```

**LRFD 接合設計（SS-U1-4）**
```
填角銲：φRn = (0.75)(0.6FEXX)(t)(L)
        t = 有效喉厚 = 0.707w
高拉力螺栓：依承壓型/摩阻型分別計算
```

**LRFD 梁柱桿件（箱形 BOX 斷面，SS-U1-3）**
```
斷面性質（BOX b_o × b_o × t，正方形）：
  A = b_o² - b_i²，b_i = b_o - 2t
  I = (b_o⁴ - b_i⁴)/12
  S = I/(b_o/2)
  Z = (b_o³ - b_i³)/4
  r = √(I/A)

局部挫屈：b/t = b_i/t ≤ 50/√Fy（題目提供公式，Fy 單位 tf/cm²）

P-M 互制：
  Pu/(φcPn) ≥ 0.2 → H1-1a：Pu/(φcPn) + (8/9)[Muy/φbMny + Muz/φbMnz] ≤ 1.0
  Pu/(φcPn) < 0.2 → H1-1b：Pu/(2φcPn) + [Muy/φbMny + Muz/φbMnz] ≤ 1.0

剪力面積（受 V 方向）：Aw = 2 × h × t（兩片平行腹板）
  h = b_i（清淨高）；h/tw ≤ 50√(kv/Fy) → Vn = 0.6FyAw

充分側向支撐 → 無 LTB → φbMn = φbMp = 0.9FyZ（兩軸對稱）
```

**ASD 插銷鉸接拉力構件（SS-U1-1）**
```
設計服務載重：P = PD + PL（不因數化）
四種破壞模式（Ω 值）：
  ① 全斷面降伏：Pn = FyAg，Ω = 1.67
  ② 有效淨面積斷裂：Pn = Fu(2t × be)，be = min(2t+16, 實際)，Ω = 2.00
  ③ 剪力斷裂（剪出）：Pn = 0.6Fu × Asf，Asf = 2t(a + d/2)，Ω = 2.00
  ④ 承壓：Pn = 1.8Fy × Apb，Apb = td，Ω = 2.00
取最小 Pa = Pn/Ω，確認 Pa ≥ P
```

**機率分析題（SD-U3-1 強柱弱梁）**
```
核心：建立不等式條件 → 對聯合機率密度作二重積分
步驟：
  ① 建立「失敗條件」不等式（例：Fy_beam > 1.25Fy_col）
  ② 確認各隨機變數的分布（均勻/常態）及範圍
  ③ 繪製積分區域草圖（確認上下限）
  ④ 計算 P = ∫∫ f_X(x)f_Y(y) dy dx（雙重積分）
  ⑤ 比較不同材料等級的機率，說明範圍縮小的效益
均勻分布：f(x) = 1/(上限-下限)；P = f_X × f_Y × 有效面積
```

---

#### 解析輸出格式（每份 SS-XXXX-N.md 的結構）

```
# 考題編號：[SS-XXXX-N]

**主分類：** `4.X.X` 分類名稱
**副分類：** `4.X.X` 分類名稱（無則省略）
**設計法：** LRFD / ASD / 概念題
**標籤：** `標籤1` `標籤2` `標籤3` ...

---

## 1. 原始題目重述 (Problem Restatement)
   - 清晰重述題幹與子問題
   - 用文字描述所有附圖的關鍵資訊
   - 圖片引用（依命名規則，含 alt text 和圖說）
   - 參考公式截圖（eqn-1.png，圖說含完整 LaTeX 文字化）

## 2. 考題核心精神與出題者意圖 (Core Concepts & Examiner's Intent)
   - 分析題目「靈魂」：核心觀念是什麼
   - 推測出題者測驗的能力、想避開的陷阱

## 3. 解題戰略地圖與陷阱分析 (Strategic Roadmap & Trap Analysis)
   - 步驟化作戰計畫（先算什麼、後算什麼）
   - 明確列出 3-4 個關鍵陷阱及應對策略

## 3.5 變數層次分析 (Variable Hierarchy Analysis)  ← 必須輸出，格式見 CLAUDE-SPEC.md §4.4
   - L1 表格：題目直接給定的所有數字（含斷面表、設計圖、參考公式中的係數）
   - L2 表格：需套公式推導的中間變數（按計算步驟分組）
   - L3 表格：深層知識點（從陷阱分析 §3 提取，考生若不懂就會用錯 L2）
   - 卡關欄位（⚠ 欄）全部留空，由考生複習時自填

## 4. 步驟化詳細計算過程 (Step-by-Step Detailed Calculation)
   > 📊 互動圖（如有）：`SS-XXXX-N-sfd-bmd-viz.html`
   - 完整計算過程，含公式、單位、中間結果
   - 關鍵步驟加「策略註解」說明為何這樣做
   - 最終答案用 \boxed{} 標示
   - 手寫補充圖片（依命名規則，含精確圖說）

## 5. 關鍵爭議點與進階探討 (Critical Issues & Advanced Discussion)
   - 題目中可能存在爭議或多種解讀的地方
   - 考場上最安全、最推薦的應對方法
   - 相關實務應用或進階觀念（如適用）
```

---

**命名規則：**（完整對照見 CLAUDE-SPEC.md §1）
```
SS-YYYY-N.md
YYYY = 西元年（2015、2024...）
N    = 題號（1、2、3、4，部分年份有 5）
```

**Cowork 完成後，你的後續動作：**
```
（Cowork 已自動完成：.md 解析存檔、question_index.json 更新
  → hasSolution=true、tags、designMethod、secondaryTopicIds 均已寫入）

1. 確認 fig PNG（你預先截圖者）品質正確（圖片完整、無截到其他題目）
2. 加入補充截圖（依命名規則拍照或截圖命名後存入）：
   - SS-XXXX-N-chart-1.png  ← 設計圖表（如有，例如φbMn vs Lb 曲線）
   - SS-XXXX-N-eqn-1.png    ← 參考公式截圖（如有，從考卷截圖）
3. 加入手寫補充（如有）：
   - SS-XXXX-N-hand-1.png
4. 人工驗算解析內容正確後，更新 verificationStatus（此欄位需人工確認）：
   告訴 Cowork：「將 SS-XXXX-N 的 verificationStatus 改為 verified」
   → Cowork 修改 question_index.json 中對應題目的 verificationStatus 欄位
5. 在 Cowork 輸入：`ingest SS-XXXX-N`
6. 說「繼續下一題」→ Cowork 解析下一道尚未有解析的題目
```

**question_index.json 欄位更新分工：**

| 欄位 | 由誰更新 | 時機 |
|------|---------|------|
| `hasSolution` | Cowork 自動 | SOLVE 結束時 |
| `tags` | Cowork 自動 | SOLVE 結束時 |
| `designMethod` | Cowork 自動 | SOLVE 結束時 |
| `secondaryTopicIds` | Cowork 自動 | SOLVE 結束時 |
| `verificationStatus` | **人工確認後告知 Cowork** | 驗算正確後 |
| `hasHandwritten` | 人工（加入 hand PNG 後） | 手寫補充存入後 |

---


---

### 【ANALYZE】考題分布分析（在 Cowork 執行）

**觸發語句：** `考題分布`

**執行：** 讀取 `raw/json/question_index.json`，輸出兩段式報告：

```
第一部分：總體趨勢分析報告
  一、總體分布概況
  二、各主題題數分布（表格）
  三、各單元主題細部分布
  四、趨勢與結論分析

第二部分：依主題條列式考題列表
  #### 主題名稱（Topic ID: 4.X.X）
  * [考題編號]: [核心精神摘要]
```

---

### 【QUERY】查詢知識庫並存回（在 Cowork 執行）

**觸發方式：** 直接向 Cowork 提問，問完後說「把這個答案存進知識庫」

**適用情境：**
```
跨題目分析：「LTB 在歷年考題中怎麼演變？」
弱點整理：「塊狀剪力破壞有哪些常見陷阱？」
比較分析：「LRFD 和 ASD 柱設計的核心差異是什麼？」
趨勢判斷：「接合設計最近三年考什麼？今年可能考什麼？」
考前衝刺：「哪些三星陷阱出現頻率最高？」
```

**執行流程：**
```
1. Cowork 讀取 wiki/index.md 定位相關分類
2. Cowork 讀取相關 concepts/、problems/、traps/、methods/ 頁面
3. Cowork 合成跨頁面的分析答案
4. 你說「把這個答案存進知識庫」
5. Cowork 存成 wiki/queries/[主題]-[日期].md
```

**wiki/queries/[id].md 格式：**
```markdown
# [查詢主題]

**查詢日期：** YYYY-MM-DD
**關鍵字：** `標籤1` `標籤2`
**參考來源：** [[概念頁]] · [[題目頁]]

## 問題
[你當時問的問題]

## 分析結果
[Cowork 合成的答案]

## 關鍵結論
[2-3 條最重要的洞察]
```

**命名規則：**
```
wiki/queries/ltb-historical-trend-20260407.md
wiki/queries/bsr-common-traps-20260407.md
wiki/queries/asd-vs-lrfd-column-20260407.md
```

**注意：**
- `wiki/queries/` 的內容**不走 ingest 流程**，由 Cowork 直接存入
- `wiki/queries/` 由 Cowork 直接寫入，不走 ingest 流程
- `lint wiki` 會檢查 queries/ 的連結是否有效

---

### 【REVIEW】複習題組（在 Cowork 執行）

**觸發語句：** `review [標籤或主題]`
例：`review LTB側扭挫屈` / `review SS-U1-2` / `review 接合設計`

**執行：**
```
1. 讀取 wiki/index.md 與 question_index.json
2. 找出所有符合標籤/主題的 verified 題目
3. 輸出複習題組：
   一、考點摘要（核心公式、常見陷阱、設計法）
   二、題目列表（依難度排序）
      | 題號 | 年份 | 設計法 | 核心考點 | 難度 |
   三、建議複習順序與重點提示
```

---

### 【PREDICT】出題預測（在 Cowork 執行）

**觸發語句：** `predict`

**執行：**
```
1. 讀取 question_index.json（所有 98 題歷年分布）
2. 分析：近 5 年（2021–2025）各主題出現頻率、輪替規律
3. 輸出預測報告：
   一、今年（2026）最可能出現的 3 個主題（含信心程度）
   二、各主題近 5 年出題熱力表
   三、歷年從未考或近年未考的冷門題型（潛在黑馬）
   四、備考建議：各主題推薦複習優先順序
```

---

### 【EXAM-SIM】模擬考試（在 Cowork 執行）

**觸發語句：** `exam-sim YYYY`
例：`exam-sim 2023`

**執行：**
```
1. 讀取 raw/exams/SS-YYYY_鋼結構設計.pdf
2. 輸出四道題目的題幹（不含解答）
3. 等待使用者作答（可說「給提示」或「解答」）
   → 「給提示」→ 輸出三層掃描法的外在掃描結果（不透露計算）
   → 「解答」→ 讀取對應 raw/solutions/ 輸出完整解析
4. 作答完成後輸出對比分析：考生解法 vs 標準解法的差異
```

---

### 【COMPARE】比較兩題（在 Cowork 執行）

**觸發語句：** `compare SS-XXXX-N SS-YYYY-M`
例：`compare SS-2018-2 SS-2022-3`

**執行：**
```
1. 讀取兩題的 raw/solutions/[id]/[id].md
2. 並排輸出對比表：
   | 項目 | SS-XXXX-N | SS-YYYY-M |
   |------|-----------|-----------|
   | 主題 | | |
   | 設計法 | | |
   | 核心考點 | | |
   | 關鍵公式 | | |
   | 主要陷阱 | | |
   | 難度差異 | | |
3. 輸出：兩題的共同考點、差異所在、備考建議
```

---

### 【ANALYZE-YEAR】單年考卷分析（在 Cowork 執行）

**觸發語句：** `analyze YYYY`
例：`analyze 2024`

**執行：**
```
1. 讀取 raw/exams/SS-YYYY_鋼結構設計.pdf 與 question_index.json 中該年四題
2. 輸出單年分析報告：
   一、四題考點分布（topicId、designMethod）
   二、難度評估（各題）
   三、該年命題特色與趨勢觀察
   四、與前後年相比的異同
```

---

### 【STUDY】單元專題複習（在 Cowork 執行）

**觸發語句：** `study [主題/topicId]`
例：`study SS-U1-1` / `study 壓力桿件` / `study LTB`

**執行：**
```
1. 讀取 wiki/concepts/ 與 wiki/methods/ 中相關頁面
2. 讀取該主題所有 verified 題目的解析
3. 輸出系統性專題整理：
   一、核心概念地圖（觀念架構）
   二、關鍵公式整理（含適用條件）
   三、歷年題目列表與各題核心考點
   四、高頻陷阱清單（三星 ⭐⭐⭐ 優先）
   五、建議解題流程（決策樹）
```

---

### 【FIND】關鍵字搜尋（在 Cowork 執行）

**觸發語句：** `find [關鍵字]`
例：`find 接頭剪力` / `find Cb係數` / `find 塊狀剪力`

**執行：**
```
1. 掃描所有 raw/solutions/SS-XXXX-N/SS-XXXX-N.md，搜尋包含關鍵字的題目
2. 同時搜尋 question_index.json 的 tags 欄位
3. 輸出搜尋結果：
   找到 X 題：
   | 題號 | 年份 | 關鍵字出現位置（題幹/計算/陷阱） | 相關摘要 |
```

---

### 【RELATED】相似題查詢（在 Cowork 執行）

**觸發語句：** `related SS-XXXX-N`
例：`related SS-2020-2`

**執行：**
```
1. 讀取指定題目的 primaryTopicId、tags、designMethod
2. 從 question_index.json 找出：
   → 同主分類的所有題目
   → tags 有 2 個以上重疊的題目
3. 輸出相似題列表：
   | 題號 | 年份 | 共同考點 | 差異 | 推薦複習順序 |
4. 輸出：這組題目的命題模式分析
```

---

### 【UPDATE-DIAGNOSIS】更新診斷層（在 Cowork 執行）

**觸發語句：** `update diagnosis`

**執行：**
```
1. 讀取所有 verified 題目的解析與 question_index.json
2. 依題型（topicId）更新 wiki/diagnosis/ 下對應頁面：
   → 決策樹：拿到題目如何快速判斷解題路徑
   → 更新各節點的代表題目與陷阱
3. 如 diagnosis/ 缺少某 topicId 的頁面 → 新建
4. 在 wiki/log.md 追加紀錄
```

---

### 【UPDATE-FAILURE-MODES】更新失敗模式層（在 Cowork 執行）

**觸發語句：** `update failure-modes`

**執行：**
```
1. 讀取所有 verified 題目解析中「陷阱分析」區塊
2. 歸類並更新 wiki/failure-modes/ 四大類頁面：
   → 強度失敗（降伏/斷裂）
   → 穩定失敗（挫屈/LTB）
   → 使用性失敗（撓度/振動）
   → 接合失敗（銲接/螺栓）
3. 在 wiki/log.md 追加紀錄
```

---

### 【UPDATE-MATERIALS】更新材料層（在 Cowork 執行）

**觸發語句：** `update materials`

**執行：**
```
1. 讀取所有涉及材料特性的題目解析（primaryTopicId = SS-U2-2 或 tags 含材料關鍵字）
2. 更新 wiki/materials/ 四大主題頁面：
   → 應力應變行為
   → 殘留應力
   → 斷裂韌性
   → 銲接性
3. 在 wiki/log.md 追加紀錄
```
