---
name: unit-lecture
description: >
  為六科考試知識庫（exam-wiki-SS/RC/SA/SD/SM/MM）的某個命題大綱單元產生
  「理解導向」觀念講義，輸出 HTML + 可列印 PDF。
  當使用者說「生成 XX-Un-m 講義」、「幫我做這單元的觀念講義」、
  「我要在練這單元考題前先懂原理」、「不要死記公式的講義」、「unit-lecture」，
  或指名某科某單元要講義／教材／原理說明時，必須使用此 skill。
  內容以物理直覺與圖解為主軸，每條規範公式都追溯來源，
  並在最後精選最具代表性的 N 題供時間有限者練習。
---

# unit-lecture — 單元觀念講義產生器

為結構技師考試知識庫的**單一命題大綱單元**產生理解導向講義。

**這不是速查表。** 知識庫裡通常已有 `study/study-XX-Un-m.html` 之類的速查／複習頁；
本 skill 產出的是**練題之前**用來建立物理直覺的講義，兩者並存、不互相覆蓋。

**檔名規則：** `study/lecture-XX-Un-m.html` + `study/lecture-XX-Un-m.pdf`（不要用 `study-` 前綴）

---

## 適用科目

| 代號 | 科目 | 資料夾 |
|------|------|--------|
| SS | 鋼結構設計 | `exam-wiki-SS` |
| RC | 鋼筋混凝土設計 | `exam-wiki-RC` |
| SA | 結構分析 | `exam-wiki-SA` |
| SD | 結構動力學／耐震設計 | `exam-wiki-SD` |
| SM | 材料力學 | `exam-wiki-SM` |
| MM | 工程數學／力學 | `exam-wiki-MM` |

六科資料夾結構相同。單元代號格式 `XX-Un-m`（U＝單元號、m＝子項號），
可在該科 `CLAUDE.md` 的「命題大綱分類」表查到。

---

## Step 0：定位

1. 從工作資料夾判斷科目（資料夾名 `exam-wiki-XX`）。使用者若指定其他科目而該資料夾未掛載，直接說明並請對方開啟該資料夾。
2. 讀 `CLAUDE.md` 確認單元代號與名稱。
3. 確認 `wiki/topics/XX-Un-m.md` 存在（該單元的題目清單）。

**立刻用 TaskCreate 建立任務清單**（採集 → 撰寫 → HTML → PDF → 精選題 → 驗證）。

---

## Step 1：資料採集

把下列腳本寫到沙盒暫存區執行（`REPO` 換成該科在 bash 中的實際掛載路徑）：

```python
# gather.py — 用法: python3 gather.py <REPO> <XX-Un-m>
import json, sys, re, os
from collections import Counter
repo, topic = sys.argv[1], sys.argv[2]
qs = json.load(open(f'{repo}/raw/json/question_index.json'))['questions']
sel = [q for q in qs if q.get('primaryTopicId') == topic or topic in (q.get('secondaryTopicIds') or [])]
pri = [q for q in sel if q.get('primaryTopicId') == topic]
print(f'# {topic}｜主分類 {len(pri)} 題、副分類 {len(sel)-len(pri)} 題\n')
mass = Counter()
for q in sorted(sel, key=lambda x: x['moduleId']):
    tag = 'P' if q in pri else 'S'
    print(tag, q['moduleId'], q.get('year'), q.get('designMethod'), '|', '/'.join(q.get('tags', [])))
    mass.update(q.get('tags', []))
print('\n# 標籤頻次（決定章節配重與複習優先順序）')
print(mass.most_common(50))
print('\n# 知識庫可用素材')
for d in ['concepts', 'methods', 'code-ref', 'diagnosis', 'failure-modes', 'materials', 'traps']:
    p = f'{repo}/wiki/{d}'
    if os.path.isdir(p):
        print(f'-- {d}:', ', '.join(sorted(os.listdir(p))[:80]))
```

接著**讀取**與本單元標籤對應的 `wiki/concepts/`、`wiki/code-ref/`、`wiki/methods/`、
`wiki/diagnosis/`、`wiki/traps/` 頁面（一次用 `for f in ...; do cat $f; done` 批次讀，省來回）。
`code-ref/` 特別重要 —— 它記錄規範常數的推導來源，是「不死記公式」的主要彈藥。

> **原則：先採集完再寫作。** 不要邊查邊寫，會寫成拼貼。

---

## Step 2：與使用者確認（AskUserQuestion）

三個問題，附推薦選項：

1. **輸出格式** — HTML + PDF 兩份（推薦）／只要 HTML／只要 PDF
2. **深度** — 觀念圖解為主（推薦）／完整數學推導／觀念＋手算範例
3. **是否附歷屆考點對應表** — 要（推薦）／只要純觀念

若使用者已在對話中講明，就不要再問。

---

## Step 3：講義骨架

**頭尾固定，中段依標籤分群動態決定。**

| 節次 | 內容 | 必要性 |
|------|------|--------|
| §0 | **全景**：用一句話說出本單元的核心對立，並畫成對照圖 | 必要 |
| §1…§k | **主題章節**：依標籤分群，每群一節；由淺入深、前後相依 | 必要 |
| §k+1 | **解題決策流程**：真正有判斷菱形的流程圖，不是條列 | 必要 |
| §k+2 | **歷屆題 × 觀念對照表**：主分類、副分類分開列 | 依 Step 2 |
| §k+3 | **陷阱總表**：15–20 條，可在考前十分鐘掃完 | 必要 |
| §k+4 | **自我檢測**：10–12 個「為什麼」，答案用 `<details>` 摺疊 | 必要 |
| §k+5 | **★ 精選 N 題**（見 Step 6） | 必要 |

**§0 那句話怎麼找**：問自己「這單元所有公式的差異，最終都源自哪一個物理對立？」
例：SS-U1-1 是「拉力是材料強度問題，壓力是幾何穩定問題」。
找不到這句話，代表你還沒讀懂這個單元 —— 回 Step 1。

**中段分群**：把標籤頻次表分成 4–8 個考點群，每群一節。
群的順序要讓後面的節能引用前面的結論（例：先講 Euler，才能講有效長度 K）。

---

## Step 4：寫作原則（品質的來源，逐條照做）

1. **每節從「這條公式在怕什麼」開始，不從公式開始。** 公式是結論，不是起點。

2. **每個規範常數都要交代出處。** 沒有「規範就是這樣規定」這種句子。
   典型：`0.6` ← von Mises 的 `1/√3`；`0.877` ← 初始彎曲 L/1000 的折減；
   `φ` 值差異 ← 破壞模式的延性與離散度。
   查不到出處就翻 `wiki/code-ref/`；還是查不到，就誠實寫「規範以試驗迴歸得到，物理意義為…」。

3. **用極限檢查取代背表。** 教讀者拿 `x→0`、`x→∞`、對稱情況去驗證公式方向。
   例：`U = 1 − x̄/L`，`x̄=0 → U=1`、`L→∞ → U→1`。忘記表格值時能自救。

4. **「兩個東西並排」是最有效的解釋裝置。** 拉 vs 壓、柱挫屈 vs 板挫屈、
   LRFD vs ASD、理論 K vs 設計 K、延性破壞 vs 脆性破壞。並排就自己解釋了自己。

5. **安全係數／折減係數一律用「破壞有沒有預警」解釋。**
   延性破壞變形大、看得見 → 係數寬鬆；脆性破壞無預警 → 係數嚴格。
   這條邏輯貫穿所有結構規範，講一次可以通吃。

6. **陷阱寫成三段式**（沿用 `wiki/traps/` 的格式）：觸發信號 → 錯誤思維 → 正確認知，
   並標註出自哪一題。

7. **每個大主題結尾要能濃縮成一條 5–7 步的箭頭因果鏈**，讓讀者用嘴巴講得出來。
   講義最後把所有因果鏈集中重列一次。

8. **圖優先於文字，文字優先於推導。** 使用者選「觀念圖解為主」時，
   數學只留關鍵幾步 + 結論，把省下的篇幅給圖與直覺。

9. **範例的答案要能自我檢查。** 例如同一題用 LRFD 與 ASD 各算一次，
   比值應落在 1.4–1.6；比值離譜代表算錯。教讀者建立這種檢查習慣。

10. **誠實標註未涵蓋範圍。** 精選題沒涵蓋到的考點群要明白列出，
    不要讓讀者誤以為練完就滿分。

11. **口吻**：對著一個有基礎、時間不夠的考生說話。不客套、不重複、不寫「總而言之」。

---

## Step 5：SVG 圖解模式庫

全部用**內嵌 SVG**（不要外部圖檔，PDF 才能一起帶走）。四種夠用：

| 模式 | 用途 | 要點 |
|------|------|------|
| **左右對照圖** | §0 的核心對立、兩種設計法、兩種破壞模式 | 中線分隔，兩側結構完全鏡像，底部各寫一行結論 |
| **狀態序列圖** | 漸進的物理過程（逐步降伏、三種平衡、載重歷程） | 3 格並排，每格下方一行說明，用顏色標示嚴重度遞增 |
| **函數曲線圖** | 規範曲線 vs 理想曲線、分段公式的交界 | 畫座標軸與刻度，理想曲線用虛線、規範曲線用粗實線，**標出交界點座標** |
| **決策流程圖** | 解題流程 | 必須有菱形判斷節點與分支箭頭；矩形內寫該步驟的關鍵公式 |

**SVG 硬規則（踩過的坑）：**

- **SVG `<text>` 裡不可以放 `\(...\)` 數學式** —— KaTeX 的 auto-render 不處理 SVG 文字節點，
  會原樣顯示反斜線。SVG 內一律用純文字（`Fy`、`λc`、`P·δ`、`KL/r`）。
- 中文字寬約等於 font-size，**估算文字寬度 = 字數 × font-size**，據此設 viewBox 寬度，
  否則文字會被切掉或壓到別的元素。
- 方框內的文字寧可分兩行，不要靠加寬方框解決。
- 每張圖下方一定要有 `<div class="cap">` 說明「這張圖在說什麼」，不是只寫圖號。

---

## Step 6：精選 N 題

**預設 5 題**；使用者說幾題就給幾題。

先跑覆蓋率計算取得候選，**再用判斷定案**（腳本只提供資訊，不做決定）：

```python
# pick.py — 用法: python3 pick.py <REPO> <XX-Un-m> <N>
import json, sys
from collections import Counter
repo, topic, N = sys.argv[1], sys.argv[2], int(sys.argv[3])
qs = json.load(open(f'{repo}/raw/json/question_index.json'))['questions']
sel = [q for q in qs if q.get('primaryTopicId') == topic or topic in (q.get('secondaryTopicIds') or [])]
mass = Counter()
for q in sel: mass.update(q['tags'])
total = sum(mass.values())
chosen, cov = [], set()
for _ in range(N):                       # 貪婪最大覆蓋
    best = max((q for q in sel if q not in chosen),
               key=lambda q: sum(mass[t] for t in set(q['tags']) - cov))
    gain = sum(mass[t] for t in set(best['tags']) - cov)
    chosen.append(best); cov |= set(best['tags'])
    print(f"{best['moduleId']} ({best['year']}) 新增權重 {gain}"
          f" 累計 {sum(mass[t] for t in cov)/total:.0%} | {'/'.join(best['tags'])}")
print('\n未涵蓋且出現 >=2 次的標籤：',
      [(k, v) for k, v in mass.most_common() if k not in cov and v >= 2])
```

**定案準則（覆蓋率只是起點）：**

- 一題能練到最多**獨立技能**者優先（例：同一題要求 LRFD 與 ASD 各算一次）。
- 彼此**重疊最少**；貪婪結果若有兩題高度重疊，換掉後者。
- **觀念鏈題**（計算量小但牽動多題的因果鏈）投報率最高，一定要留一席。
- **需要自己建立前置資料**的題型（自算斷面性質、自建模型）留一席，這是別題練不到的。
- 同分時選**近年題**。
- 標籤語彙有同義詞（如「對位圖 / nomograph」）與符號標籤（如 `λc`、`Fcr`），
  raw 覆蓋率會低估。**改以「考點群」報告涵蓋度**，並誠實列出未涵蓋的群。

**每題要寫出：** 題號（連到 `../wiki/problems/`）、考年、**為什麼選它**、讀本講義哪幾節、
**做完要能回答的問題**。最後附「練這幾題的正確方法」與 1–2 題候補。

---

## Step 7：產出 HTML

存到 `<REPO>/study/lecture-XX-Un-m.html`。

### 數學式離線化（必做）

沙盒無法連 CDN，且使用者可能離線閱讀。把 KaTeX 放進該科 repo：

```bash
mkdir -p /tmp/v && cd /tmp/v && npm install katex --no-audit --no-fund
D=<REPO>/study/assets/katex && mkdir -p $D/fonts
cp /tmp/v/node_modules/katex/dist/katex.min.css /tmp/v/node_modules/katex/dist/katex.min.js $D/
cp /tmp/v/node_modules/katex/dist/contrib/auto-render.min.js $D/
cp /tmp/v/node_modules/katex/dist/fonts/*.woff2 $D/fonts/     # 只複製 woff2，約 600KB
```

`<head>` 用相對路徑引用（同一個 `assets/` 可被該科所有講義共用）：

```html
<link rel="stylesheet" href="assets/katex/katex.min.css">
<script defer src="assets/katex/katex.min.js"></script>
<script defer src="assets/katex/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});"></script>
```

行內數學一律用 `\( ... \)`，展示式用 `$$ ... $$`（**不要**用單 `$`，會誤判貨幣符號）。

### 版面 CSS（house style，沿用以維持六科一致）

```css
:root{--ac:#1565c0;--ac2:#e3f2fd;--tension:#2e7d32;--tension2:#e8f5e9;
--comp:#c62828;--comp2:#ffebee;--warn:#ef6c00;--warn2:#fff3e0;
--key:#6a1b9a;--key2:#f3e5f5;--bg:#f7f9fb;--card:#fff;--ink:#263238;--mut:#607d8b;--bd:#dfe6ea}
*{box-sizing:border-box}
body{margin:0;font-family:"Microsoft JhengHei","Noto Sans TC",-apple-system,sans-serif;
background:var(--bg);color:var(--ink);line-height:1.75;font-size:15.5px}
header{background:linear-gradient(135deg,#0d47a1,#1976d2 60%,#42a5f5);color:#fff;padding:34px 26px}
header h1{margin:0 0 8px;font-size:1.6em}header .sub{opacity:.9;font-size:.93em;margin:0}
header .meta{margin-top:12px;font-size:.82em;opacity:.8}
nav{position:sticky;top:0;z-index:20;background:#fff;border-bottom:2px solid var(--bd);
padding:9px 14px;display:flex;flex-wrap:wrap;gap:6px;box-shadow:0 2px 6px rgba(0,0,0,.05)}
nav a{text-decoration:none;color:var(--ac);font-size:.85em;padding:4px 11px;border-radius:14px;background:var(--ac2)}
nav a:hover{background:var(--ac);color:#fff}
main{max-width:980px;margin:0 auto;padding:24px 18px 80px}
section{margin-bottom:46px}
h2{font-size:1.32em;border-left:6px solid var(--ac);padding-left:12px;margin:44px 0 18px;line-height:1.4}
h3{font-size:1.08em;margin:30px 0 10px;color:#0d47a1}
h4{font-size:.99em;margin:20px 0 8px;color:#37474f}
.lead{font-size:1.03em;background:#fff;border:1px solid var(--bd);border-left:5px solid var(--ac);
border-radius:0 10px 10px 0;padding:14px 18px;margin:16px 0}
.box{background:var(--card);border:1px solid var(--bd);border-radius:11px;padding:16px 18px;margin:16px 0}
.why{background:var(--key2);border:1px solid #ce93d8;border-left:5px solid var(--key);
border-radius:0 10px 10px 0;padding:13px 17px;margin:16px 0}
.why b:first-child{color:var(--key)}
.trap{background:var(--warn2);border:1px solid #ffcc80;border-left:5px solid var(--warn);
border-radius:0 10px 10px 0;padding:13px 17px;margin:16px 0}
.trap b:first-child{color:#e65100}
.tens{background:var(--tension2);border:1px solid #a5d6a7;border-left:5px solid var(--tension);
border-radius:0 10px 10px 0;padding:13px 17px;margin:16px 0}
.comp{background:var(--comp2);border:1px solid #ef9a9a;border-left:5px solid var(--comp);
border-radius:0 10px 10px 0;padding:13px 17px;margin:16px 0}
.fig{background:#fff;border:1px solid var(--bd);border-radius:11px;padding:16px 14px 10px;margin:20px 0;overflow-x:auto}
.fig svg{display:block;margin:0 auto;max-width:100%;height:auto}
.fig .cap{font-size:.85em;color:var(--mut);text-align:center;margin-top:10px;line-height:1.6}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:.9em;background:#fff}
th,td{border:1px solid var(--bd);padding:8px 10px;text-align:left;vertical-align:top}
th{background:#eceff1;font-weight:600}
tbody tr:nth-child(even){background:#fafcfd}
ul,ol{margin:10px 0 10px 4px;padding-left:22px}li{margin:5px 0}
.pill{display:inline-block;font-size:.76em;padding:2px 8px;border-radius:10px;margin-right:4px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:760px){.grid2{grid-template-columns:1fr}}
details{background:#fff;border:1px solid var(--bd);border-radius:9px;padding:10px 14px;margin:12px 0}
summary{cursor:pointer;font-weight:600;color:var(--ac)}
details p{border-left:3px solid #e0e0e0;padding-left:12px;margin:8px 0;color:#37474f}
.qlink{color:#1565c0;text-decoration:none;border-bottom:1px dotted #90caf9;font-weight:600}
.katex-display{margin:14px 0!important;overflow-x:auto;overflow-y:hidden}
footer{text-align:center;color:var(--mut);font-size:.83em;padding:26px;border-top:1px solid var(--bd)}
```

用途約定：`.why` 紫＝為什麼／物理直覺；`.trap` 橘＝陷阱；`.lead` 藍＝該節主張；
`.box` 白＝手算範例；`.tens`/`.comp` 綠/紅＝成對概念的兩側。

### 分段寫檔

講義通常 1000+ 行。先 Write 出骨架（head + nav + `<!--APPEND-->` 佔位 + footer），
再用 Edit 反覆把 `<!--APPEND-->` 換成「新內容 + `<!--APPEND-->`」逐節長出來。
一次寫完容易中斷且難修。

### 題號連結

寫完後把表格裡的題號轉成連結：

```python
import re
s = open(path, encoding='utf-8').read()
s, n = re.subn(r'<td>(XX-\d{4}-\d)</td>',
    lambda m: f'<td><a class="qlink" href="../wiki/problems/{m.group(1)}.md">{m.group(1)}</a></td>', s)
open(path, 'w', encoding='utf-8').write(s)
```

---

## Step 8：產出 PDF

**沙盒沒有 Chromium，playwright 的瀏覽器也下載不到。**
可行路徑只有一條：**MathJax 把 TeX 轉成內嵌 SVG → WeasyPrint 排版**。

### 8.1 環境（分開執行，單次 bash 上限 45 秒）

```bash
# 一定要裝在 /tmp，不要裝在掛載資料夾 —— 掛載點會漏檔（version.js、*.d.ts 掉失）
mkdir -p /tmp/v && cd /tmp/v && npm install mathjax-full@3.2.2 --no-audit --no-fund
```
```bash
pip install weasyprint --break-system-packages -q     # 約 40 秒
```

### 8.2 `tex2svg.js`

```javascript
const fs = require('fs');
const P = '/tmp/v/node_modules/';
const {mathjax} = require(P + 'mathjax-full/js/mathjax.js');
const {TeX} = require(P + 'mathjax-full/js/input/tex.js');
const {SVG} = require(P + 'mathjax-full/js/output/svg.js');
const {liteAdaptor} = require(P + 'mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require(P + 'mathjax-full/js/handlers/html.js');
const {AllPackages} = require(P + 'mathjax-full/js/input/tex/AllPackages.js');
const adaptor = liteAdaptor(); RegisterHTMLHandler(adaptor);
const doc = mathjax.document('', {InputJax: new TeX({packages: AllPackages}),
                                  OutputJax: new SVG({fontCache: 'local'})});
const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = items.map(it => adaptor.outerHTML(
  doc.convert(it.tex, {display: it.display, em: 16, ex: 8, containerWidth: 800})));
fs.writeFileSync(process.argv[3], JSON.stringify(out), 'utf8');
console.log('converted ' + out.length);
```

`fontCache:'local'` 讓每個 SVG 自帶字形定義 —— WeasyPrint 不支援跨元素的全域字形快取。

### 8.3 `build_pdf.py`

```python
#!/usr/bin/env python3
# 用法: python3 build_pdf.py <src.html> <out.pdf> <work_dir> "<頁尾文字>"
import re, json, subprocess, sys, html as htmllib

SRC, PDF, WORK = sys.argv[1], sys.argv[2], sys.argv[3]
FOOT = sys.argv[4] if len(sys.argv) > 4 else ''
src = open(SRC, encoding='utf-8').read()

# 1. 保護不可處理區塊（svg / style / script），只在一般 HTML 抽數學式
PROTECT = re.compile(r'(<svg\b.*?</svg>|<style\b.*?</style>|<script\b.*?</script>)', re.S | re.I)
parts = PROTECT.split(src)
items = []
def stash(tex, display):
    # 關鍵：TeX 內的 < > & 在 HTML 原始碼中被跳脫過，不還原會被 MathJax 當成
    # 對齊字元而產生 merror，PDF 上顯示為一整塊黑方框
    items.append({'tex': htmllib.unescape(tex.strip()), 'display': display})
    return '\x00MJ%d\x00' % (len(items) - 1)
for i in range(0, len(parts), 2):
    parts[i] = re.sub(r'\$\$(.+?)\$\$', lambda m: stash(m.group(1), True), parts[i], flags=re.S)
    parts[i] = re.sub(r'\\\((.+?)\\\)', lambda m: stash(m.group(1), False), parts[i], flags=re.S)

json.dump(items, open(WORK + '/math_in.json', 'w'), ensure_ascii=False)
subprocess.run(['node', WORK + '/tex2svg.js', WORK + '/math_in.json', WORK + '/math_out.json'], check=True)
rendered = json.load(open(WORK + '/math_out.json'))

doc = ''.join(parts)
doc = re.sub(r'\x00MJ(\d+)\x00',
             lambda m: ('<div class="mjd">%s</div>' if items[int(m.group(1))]['display']
                        else '<span class="mji">%s</span>') % rendered[int(m.group(1))], doc)

# 2. 移除 CDN／導覽列，<details> 攤平（列印沒有互動）
doc = re.sub(r'<link[^>]*cdn\.jsdelivr[^>]*>', '', doc)
doc = re.sub(r'<script\b[^>]*cdn\.jsdelivr.*?</script>', '', doc, flags=re.S)
doc = re.sub(r'<link[^>]*katex\.min\.css[^>]*>', '', doc)
doc = re.sub(r'<script\b[^>]*(katex|auto-render)\.min\.js.*?</script>', '', doc, flags=re.S)
doc = re.sub(r'<nav>.*?</nav>', '', doc, flags=re.S)
doc = (doc.replace('<details>', '<div class="det">').replace('</details>', '</div>')
          .replace('<summary>', '<p class="sum">').replace('</summary>', '</p>'))

doc = doc.replace('</head>', '''<style>
@page{size:A4;margin:15mm 14mm 16mm 14mm;
 @bottom-center{content:"''' + FOOT + '''  " counter(page) " / " counter(pages);
 font-family:"Noto Sans CJK TC";font-size:8.5pt;color:#78909c}}
html,body{background:#fff!important;font-family:"Noto Sans CJK TC",sans-serif;font-size:10.2pt;line-height:1.62}
main{max-width:none;padding:0}
header{padding:20px 22px;border-radius:0}
header h1{font-size:19pt}header .sub{font-size:10pt}header .meta{font-size:8.5pt}
section{margin-bottom:20px}
h2{font-size:14pt;margin:20px 0 10px;break-after:avoid}
h3{font-size:11.6pt;margin:15px 0 6px;break-after:avoid}
h4{font-size:10.6pt;break-after:avoid}
p{margin:7px 0}
table{font-size:8.9pt}th,td{padding:4px 6px}
thead{display:table-header-group}tr{break-inside:avoid}
.fig,.why,.trap,.tens,.comp,.box,.lead{break-inside:avoid}
.fig{padding:10px 8px 6px;margin:12px 0}.fig .cap{font-size:8.6pt}
.why,.trap,.tens,.comp,.lead{padding:9px 13px;margin:11px 0;font-size:9.8pt}
ul,ol{margin:6px 0 6px 2px}li{margin:3px 0}
.mjd{text-align:center;margin:11px 0;break-inside:avoid}.mjd svg{max-width:100%}
.mji svg{vertical-align:-0.22em}
mjx-container{display:inline-block}
.det{background:#fff;border:1px solid #dfe6ea;border-radius:8px;padding:8px 12px}
.sum{font-weight:600;color:#1565c0;margin:0 0 4px;border-left:none!important;padding-left:0!important}
.det p{border-left:3px solid #e0e0e0;padding-left:10px;color:#455a64;font-size:9.6pt}
a.qlink{color:#1565c0;text-decoration:none;font-weight:600}
footer{font-size:8.5pt;padding:14px}
</style></head>''')

open(WORK + '/print.html', 'w', encoding='utf-8').write(doc)
from weasyprint import HTML
HTML(filename=WORK + '/print.html', base_url=WORK).write_pdf(PDF)
print('PDF ->', PDF)
```

沙盒已內建 Noto Sans/Serif CJK，中文可正常輸出。

---

## Step 9：驗證（不可略過）

1. **抽頁目視檢查**：`pdftoppm -png -r 68 -f <n> -l <n> out.pdf chk/p`，
   然後用 Read 工具看圖。**至少檢查：首頁、每張 SVG 所在頁、流程圖頁、最後一頁。**
   要看的是：SVG 文字有沒有溢出方框、數學式有沒有變成黑方框、表格有沒有被切爛。
2. **題號核對**：用腳本比對講義中出現的題號與 `question_index.json` 的該單元清單，
   確認無缺漏、無誤植、考年正確。
3. **數值核對**：把講義裡所有算出來的數字（範例、常數、交界點）用 python 重算一次。
4. **交叉引用**：檢查文中「見 §x.y」的節號在改版後仍然存在。
5. 用 `mcp__cowork__present_files` 交付 HTML 與 PDF。

---

## 已知地雷（都踩過，別再踩）

| # | 症狀 | 原因與解法 |
|---|------|-----------|
| 1 | PDF 上數學式變成整塊黑方框 | HTML 實體 `&lt;` `&gt;` 沒還原就餵給 MathJax，`&` 被當對齊字元 → `merror`。用 `html.unescape()` |
| 2 | SVG 裡出現字面的 `\(F_y\)` | KaTeX auto-render 不處理 SVG 文字節點。SVG 內改用純文字 |
| 3 | `npm install` 後 `MODULE_NOT_FOUND` | 裝在掛載資料夾會漏檔。改裝到 `/tmp` |
| 4 | CDN 抓不到（403 blocked-by-allowlist） | 沙盒只放行 npm／pypi。KaTeX 走 npm 取得後複製到 repo |
| 5 | bash 逾時 | 單次上限 45 秒。npm 與 pip 分開執行，不要串在一起 |
| 6 | 流程圖文字跑出方框 | 中文字寬≈font-size，先估寬再設 viewBox；文字寧可分行 |
| 7 | 掛載資料夾內 `rm` 失敗（Operation not permitted） | 別在掛載點做 npm 的清除；暫存一律用 `/tmp` |

---

## 產出後

1. 一句話交代成果與檔案位置，**不要複述講義內容**。
2. 主動指出這份講義**沒涵蓋**什麼、以及你認為還可以再加強的地方 —— 誠實的自我批評比推銷有價值。
3. 詢問是否要對同科其他單元或其他科目比照辦理。
