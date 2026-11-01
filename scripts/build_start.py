#!/usr/bin/env python3
"""產生 exam-wiki-SS「從這裡開始」起點頁 (start.html)。
首頁 index.html 是題庫儀表板，保持不動；起點頁另存 start.html。
所有連結集中在 UNITS / GLOBAL 資料區，改連結只改這裡，再重跑即可。"""
from html import escape
from pathlib import Path
import sys

SITE = "https://yjc5760.github.io/exam-wiki-SS/"
REPO = "https://github.com/yjc5760/exam-wiki-SS"

GLOBAL = {
    "frequency": "study/frequency-SS.html",
    "strategy_video": "https://youtu.be/nE_assOYwMc",
    "wiki": "index.html",
    "feedback": REPO + "/issues/new?template=correction.yml",
}

# 依你清單的順序排列（建議讀書順序）
UNITS = [
    {
        "id": "SS-U1-1", "name": "拉力及壓力桿件",
        "overview": "study/unit-SS-U1-1.html",
        "lecture": "study/lecture-SS-U1-1.html",
        "textbook": [("拉力桿件", "study/textbook-SS-U1-1-tension.html"),
                     ("壓力桿件", "study/textbook-SS-U1-1-compression.html")],
        "lecture_video": "https://youtu.be/HfItAmMc8fU",
        "lecture_anim": "https://youtu.be/KFU-vxOU514",
        "video_handout": "影片講義/SS-U1-1_拉力及壓力桿件.html",
        "slides_pdf": "https://share.google/lnSgqBy4KQ9SjV0OX",
        "formula_video": "https://youtu.be/Ax_AZFu6EAM",
        "notebooklm": "https://notebook.google.com/notebook/8eed97ef-2b14-42fb-bb67-c841713536f5",
        "solutions": [
            ("SS-2013-3", "兩平面有效長度", "https://youtu.be/3_ru5_vteTE"),
            ("SS-2013-2", "靠桿與萊梅厥公式", "https://youtu.be/iuuQeUykMmY"),
            ("SS-2005-1", "單角鋼拉力桿件", "https://youtu.be/ybm1gNFO_s0"),
            ("SS-2024-1", "具殘留應力之柱強度曲線", "https://youtu.be/5-ynHlywZ48"),
            ("SS-2015-3", "雙槽鋼組合柱", "https://youtu.be/0fMRMMfWGqA"),
        ],
    },
    {
        "id": "SS-U1-2", "name": "梁桿件",
        "overview": "study/unit-SS-U1-2.html",
        "lecture": "study/lecture-SS-U1-2.html",
        "textbook": [],
        "lecture_video": "https://youtu.be/ENSQq26Ni_A",
        "lecture_anim": "https://youtu.be/8fjgRfoFBzE",
        "video_handout": "影片講義/SS-U1-2_梁桿件.html",
        "slides_pdf": "https://share.google/JDyIxAVvWFxO1gC0z",
        "formula_video": "https://youtu.be/C8oEftebIVI",
        "notebooklm": "https://notebook.google.com/notebook/b6d54c39-8c67-48cc-a287-29691173b108",
        "solutions": [
            ("SS-2011-3", "端彎矩梁的側扭挫曲", "https://youtu.be/wwc0XcjxRGM"),
            ("SS-2025-1", "銲接H型鋼強軸設計彎矩", "https://youtu.be/ou0R1Uz30bQ"),
            ("SS-2014-3", "雙向彎曲梁之LTB與互制", "https://youtu.be/v7c-kBjfpZo"),
            ("SS-2023-3", "非對稱斷面之My與Mp", "https://youtu.be/a74ZRBsiCOA"),
            ("SS-2010-4", "樓版鋼梁設計：自重迭代與撓度", "https://youtu.be/d6dxV6qHPd0"),
        ],
    },
    {
        "id": "SS-U1-4", "name": "接合之分析與設計",
        "overview": "study/unit-SS-U1-4.html",
        "lecture": "study/lecture-SS-U1-4.html",
        "textbook": [],
        "lecture_video": "https://youtu.be/dixgCh7xLDk",
        "lecture_anim": "https://youtu.be/qTE5S43Ii-0",
        "video_handout": "影片講義/SS-U1-4_接合之分析與設計.html",
        "slides_pdf": "https://share.google/bTzNbrpXiyq0oelou",
        "formula_video": "https://youtu.be/_EwPT6FnUXw",
        "notebooklm": "https://notebook.google.com/notebook/53601c4c-236a-4b5c-835d-5a9a8b8f6808",
        "solutions": [
            ("SS-2015-2", "雙槽鋼拉力桿與填角銲", "https://youtu.be/HNwcaz3QKKU"),
            ("SS-2017-4", "偏心U形銲縫群", "https://youtu.be/5jZRoS3V70k"),
            ("SS-2017-2", "摩阻型螺栓接合", "https://youtu.be/gAAvoECp0fk"),
            ("SS-2020-4", "梁腹板續接", "https://youtu.be/ozO-ofntGrE"),
            ("SS-2018-3", "箱型柱-H梁接頭填角銲檢核", "https://youtu.be/H4yjoRyUW-4"),
            ("SS-2009-4", "銲接與高拉力螺栓", "https://youtu.be/kKQWCGDvgyg"),
        ],
    },
    {
        "id": "SS-U1-3", "name": "梁柱桿件",
        "overview": "study/unit-SS-U1-3.html",
        "lecture": "study/lecture-SS-U1-3.html",
        "textbook": [],
        "lecture_video": "https://youtu.be/nIcbt4y-2dY",
        "lecture_anim": "https://youtu.be/N9_AECPTywg",
        "video_handout": "影片講義/SS-U1-3_梁柱桿件.html",
        "slides_pdf": "https://share.google/3QsNmvpTMZhTlablf",
        "formula_video": "https://youtu.be/MSYwIb7odIA",
        "notebooklm": "https://notebook.google.com/notebook/df28fa46-201e-412b-9f2d-ee4aeb263199",
        "solutions": [
            ("SS-2013-4", "B1B2放大法 無側撐鋼架", "https://youtu.be/Khlkt8AIymY"),
            ("SS-2020-3", "梁柱雙軸互制", "https://youtu.be/PnpkDSeDf6s"),
            ("SS-2003-4", "雙軸梁柱ASD檢核", "https://youtu.be/2DaVn2kLJQE"),
            ("SS-2011-1", "直接分析法", "https://youtu.be/nKk8tQ8OdN4"),
            ("SS-2022-1", "箱形梁柱檢核", "https://youtu.be/fpS1AflKLXs"),
            ("SS-2009-1", "強柱弱梁與P-M互制曲線", "https://youtu.be/IPtLjbDJwX4"),
        ],
    },
    {
        "id": "SS-U2-3", "name": "設計規範對施工之要求",
        "overview": "study/unit-SS-U2-3.html",
        "lecture": "study/lecture-SS-U2-3.html",
        "textbook": [],
        "lecture_video": "https://youtu.be/qXGQkOb_b2w",
        "lecture_anim": "https://youtu.be/aNZHpnzQkHU",
        "video_handout": "影片講義/SS-U2-3_設計規範對施工之要求.html",
        "slides_pdf": "https://share.google/Ob6Whwy12p8UArlgB",
        "formula_video": "https://youtu.be/9042JfQL-PI",
        "notebooklm": "https://notebook.google.com/notebook/cff3f476-afb8-4d81-bfd0-2885c1fcb0f8",
        "solutions": [
            ("SS-2021-1", "銲道瑕疵與非破壞性檢測", "https://youtu.be/QuweTw6j8gg"),
            ("SS-2004-1", "高強度螺栓施工", "https://youtu.be/E11xVGjHYCU"),
            ("SS-2019-1", "鋼結構三種防蝕方法", "https://youtu.be/VXze1vIfKRA"),
            ("SS-2022-3", "韌性抗彎矩構架之銲接部位與NDT", "https://youtu.be/jJcr_UJeoAI"),
            ("SS-2016-2", "回銲（繞角銲）", "https://youtu.be/Mp3TA-kSXT4"),
        ],
    },
]


def a(href, text, cls="", ext=None):
    if ext is None:
        ext = href.startswith("http")
    tgt = ' target="_blank" rel="noopener"' if ext else ""
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{escape(href)}"{c}{tgt}>{text}</a>'


def unit_block(i, u):
    tb = ""
    if u["textbook"]:
        tb = "".join(f"<li>{a(h, '教科書：' + escape(t))}</li>" for t, h in u["textbook"])
    sols = "".join(
        f'<li>{a(h, f"<span class=qid>{escape(q)}</span> {escape(t)}")}</li>'
        for q, t, h in u["solutions"])
    return f"""
<details class="unit" id="{u['id']}"{' open' if i == 0 else ''}>
  <summary>
    <span class="unum">{i+1}</span>
    <span class="utitle"><span class="uid">{u['id']}</span>{escape(u['name'])}</span>
    <span class="ucount">{len(u['solutions'])} 題解題影片</span>
  </summary>
  <div class="ubody">
    <div class="col">
      <h4><span class="dot d1"></span>先看（15 分鐘）</h4>
      <ul>
        <li>{a(u['overview'], '單元總覽：考什麼、哪些公式要背')}</li>
      </ul>
      <h4><span class="dot d2"></span>懂原理 <small>文字或影片選一種</small></h4>
      <ul>
        <li>{a(u['lecture'], '觀念講義（網頁）')}</li>
        <li>{a(u['lecture_video'], '觀念講義影片')} ・ {a(u['lecture_anim'], '動畫版')}</li>
        <li>{a(u['video_handout'], '影片講義（圖文）')}</li>
        <li>{a(u['slides_pdf'], '講義簡報 PDF')}</li>
        {tb}
      </ul>
    </div>
    <div class="col">
      <h4><span class="dot d3"></span>記公式</h4>
      <ul>
        <li>{a(u['formula_video'], '公式記憶影片')}</li>
        <li>{a(u['overview'], '單元總覽的「必須自己背」清單')}</li>
      </ul>
      <h4><span class="dot d5"></span>問到懂</h4>
      <ul>
        <li>{a(u['notebooklm'], 'NotebookLM 單元筆記本')}</li>
      </ul>
    </div>
    <div class="col wide">
      <h4><span class="dot d6"></span>試一題 → <span class="dot d4"></span>練題目 <small>讀完講義先任選一題試寫；之後每題都先自己寫，寫過才看影片</small></h4>
      <ul class="sols">{sols}</ul>
    </div>
  </div>
</details>"""


def schedule_rows(weeks):
    # 每單元：1 週原理＋抓重點，1 週練題（12 週版再多 1 週）；最後留總複習
    rows = []
    w = 1
    rows.append((f"第 {w} 週", "定方向", "看出題頻率熱圖與讀書策略影片，排定自己的單元順序；開始 " + UNITS[0]['id']))
    w += 1
    per = 1 if weeks == 8 else 2
    for u in UNITS:
        end = w + per - 1 if weeks == 12 else w
        label = f"第 {w} 週" if end == w else f"第 {w}–{end} 週"
        if weeks == 8:
            what = "單元總覽 → 觀念講義 → 試寫一題 → 公式影片 → 練 3 題以上"
        else:
            what = "第一週：單元總覽、觀念講義、試寫一題、背公式；第二週：清單上的考古題全部自己寫一遍"
        rows.append((label, f"{u['id']} {u['name']}", what))
        w = end + 1
    last = f"第 {w} 週" if w == weeks else f"第 {w}–{weeks} 週"
    rows.append((last, "總複習", "重看各單元總覽的「必背公式」，限時重寫錯過的題目，用 AI 追問仍不懂的地方"))
    return "".join(f"<tr><td>{escape(a_)}</td><td>{escape(b)}</td><td>{escape(c)}</td></tr>" for a_, b, c in rows)


def build():
    units_html = "".join(unit_block(i, u) for i, u in enumerate(UNITS))
    n_sol = sum(len(u["solutions"]) for u in UNITS)
    html = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>鋼結構設計 從這裡開始</title>
<meta name="description" content="結構技師「鋼結構設計」考古題知識庫的學習路徑：出題頻率、觀念講義、公式記憶、解題影片與 AI 問答，一頁看懂怎麼讀。">
<meta property="og:title" content="鋼結構設計（SS）從這裡開始">
<meta property="og:description" content="把歷屆考古題變成知識庫：六步學習路徑＋8／12 週進度表，免費使用。">
<meta property="og:url" content="{SITE}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Noto+Serif+TC:wght@700;900&display=swap" rel="stylesheet">
<style>
:root {{
  --bg:#f6f4ef; --paper:#fffdf8; --ink:#1d2328; --muted:#5d666e; --line:#dcd6ca;
  --steel:#2f4a5e; --accent:#c4561d; --accent-soft:#f6e3d6;
  --d1:#2f4a5e; --d2:#3f7d6b; --d3:#b8862b; --d4:#c4561d; --d5:#6a5aa0; --d6:#1f8a9a;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#14181b; --paper:#1b2024; --ink:#e7e4dd; --muted:#a0a8ae; --line:#2f363c;
  --steel:#8fb2cc; --accent:#ec8a55; --accent-soft:#3a2a20;
  --d1:#8fb2cc; --d2:#6cc0a6; --d3:#e0b45a; --d4:#ec8a55; --d5:#a898dc; --d6:#5cc4d2;
}} }}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Noto Sans TC",system-ui,sans-serif;line-height:1.7;font-size:16px}}
a{{color:var(--steel);text-decoration-thickness:1px;text-underline-offset:3px}}
a:hover{{color:var(--accent)}}
.wrap{{max-width:980px;margin:0 auto;padding:0 16px}}
header.top{{border-bottom:1px solid var(--line);background:var(--paper)}}
header.top .wrap{{display:flex;justify-content:space-between;align-items:center;gap:12px;padding-top:10px;padding-bottom:10px;font-size:14px}}
header.top b{{letter-spacing:.04em}}
header.top nav a{{margin-left:14px;text-decoration:none}}
.hero{{padding:56px 0 36px}}
.kicker{{font-size:13px;letter-spacing:.18em;color:var(--accent);font-weight:700}}
h1{{font-family:"Noto Serif TC",serif;font-size:clamp(30px,6vw,48px);line-height:1.25;margin:10px 0 16px;font-weight:900}}
.lead{{font-size:18px;color:var(--muted);max-width:640px;margin:0}}
.cta{{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}}
.btn{{display:inline-block;padding:10px 18px;border-radius:6px;text-decoration:none;font-weight:700;font-size:15px;border:1.5px solid var(--steel)}}
.btn.primary{{background:var(--steel);color:var(--paper)}}
.btn.primary:hover{{background:var(--accent);border-color:var(--accent);color:#fff}}
.btn.ghost{{color:var(--steel)}}
.stats{{display:flex;flex-wrap:wrap;gap:28px;margin-top:30px;font-size:14px;color:var(--muted)}}
.stats b{{display:block;font-size:26px;color:var(--ink);font-family:"Noto Serif TC",serif}}
section{{padding:34px 0}}
h2{{font-family:"Noto Serif TC",serif;font-size:26px;margin:0 0 6px}}
.sub{{color:var(--muted);margin:0 0 22px}}
/* path */
.path{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(6,1fr);gap:0;counter-reset:s}}
.path li{{position:relative;padding:18px 14px 16px;background:var(--paper);border:1px solid var(--line);border-left:none}}
.path li:first-child{{border-left:1px solid var(--line);border-radius:8px 0 0 8px}}
.path li:last-child{{border-radius:0 8px 8px 0}}
.path li::before{{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:var(--c)}}
.path .n{{font-size:12px;font-weight:700;color:var(--c);letter-spacing:.1em}}
.path h3{{margin:2px 0 6px;font-size:19px}}
.path p{{margin:0;font-size:14px;color:var(--muted);line-height:1.6}}
.path .t{{display:inline-block;margin-top:8px;font-size:12px;padding:1px 8px;border-radius:20px;background:var(--bg);color:var(--muted)}}
@media (max-width:900px) and (min-width:761px){{
  .path{{grid-template-columns:repeat(3,1fr);row-gap:10px}}
  .path li{{border-left:1px solid var(--line);border-radius:8px}}
}}
@media (max-width:760px){{
  .path{{grid-template-columns:1fr}}
  .path li,.path li:first-child,.path li:last-child{{border:1px solid var(--line);border-top:none;border-radius:0}}
  .path li:first-child{{border-top:1px solid var(--line);border-radius:8px 8px 0 0}}
  .path li:last-child{{border-radius:0 0 8px 8px}}
  .path li::before{{top:0;bottom:0;right:auto;width:4px;height:auto}}
  .path li{{padding-left:20px}}
}}
.rules{{margin:6px 0 0;padding-left:20px}}.rules li{{margin:4px 0}}
.tip{{margin-top:16px;padding:12px 16px;border-radius:8px;background:var(--accent-soft);font-size:15px}}
/* units */
.unit{{background:var(--paper);border:1px solid var(--line);border-radius:8px;margin-bottom:10px;overflow:hidden}}
.unit summary{{list-style:none;cursor:pointer;display:flex;align-items:center;gap:14px;padding:14px 16px}}
.unit summary::-webkit-details-marker{{display:none}}
.unit summary::after{{content:"＋";margin-left:auto;color:var(--muted);font-weight:700}}
.unit[open] summary::after{{content:"－"}}
.unum{{flex:none;width:32px;height:32px;border-radius:50%;display:grid;place-items:center;background:var(--steel);color:var(--paper);font-weight:700}}
.utitle{{font-weight:700;font-size:17px}}
.uid{{display:block;font-size:12px;font-weight:500;color:var(--muted);letter-spacing:.06em}}
.ucount{{font-size:13px;color:var(--muted);white-space:nowrap}}
.ubody{{display:grid;grid-template-columns:1fr 1fr;gap:4px 28px;padding:4px 20px 18px;border-top:1px solid var(--line)}}
.ubody .wide{{grid-column:1/-1}}
.ubody h4{{margin:14px 0 4px;font-size:14px;display:flex;align-items:center;gap:8px}}
.ubody h4 small{{font-weight:400;color:var(--muted)}}
.ubody ul{{margin:0;padding-left:20px;font-size:15px}}
.ubody li{{margin:3px 0}}
.sols{{columns:2;column-gap:28px}}
.sols li{{break-inside:avoid}}
.qid{{font-variant-numeric:tabular-nums;font-size:13px;color:var(--muted);margin-right:4px}}
.dot{{width:10px;height:10px;border-radius:50%;display:inline-block}}
.d1{{background:var(--d1)}}.d2{{background:var(--d2)}}.d3{{background:var(--d3)}}.d4{{background:var(--d4)}}.d5{{background:var(--d5)}}.d6{{background:var(--d6)}}
@media (max-width:640px){{ .ubody{{grid-template-columns:1fr}} .sols{{columns:1}} .ucount{{display:none}} }}
/* schedule */
.tabs{{display:flex;gap:6px;margin-bottom:12px}}
.tabs button{{font:inherit;font-size:14px;padding:6px 14px;border-radius:20px;border:1px solid var(--line);background:var(--paper);color:var(--ink);cursor:pointer}}
.tabs button[aria-selected="true"]{{background:var(--steel);color:var(--paper);border-color:var(--steel)}}
.tablewrap{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;background:var(--paper);border:1px solid var(--line);border-radius:8px;font-size:15px}}
th,td{{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{font-size:13px;color:var(--muted);font-weight:500}}
td:first-child{{white-space:nowrap;font-variant-numeric:tabular-nums;color:var(--muted)}}
td:nth-child(2){{font-weight:700;white-space:nowrap}}
tr:last-child td{{border-bottom:none}}
@media (max-width:640px){{
  thead{{display:none}}
  table,tbody,tr,td{{display:block;width:100%}}
  tr{{padding:10px 14px;border-bottom:1px solid var(--line)}}
  tr:last-child{{border-bottom:none}}
  td{{border:none;padding:0}}
  td:nth-child(2){{white-space:normal;margin:2px 0}}
}}
/* ai */
.prompts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}
.prompt{{background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:14px 16px;font-size:15px}}
.prompt b{{display:block;font-size:13px;color:var(--accent);margin-bottom:4px}}
.prompt code{{font-family:inherit;display:block;background:var(--bg);padding:8px 10px;border-radius:6px;margin-top:6px;font-size:14px}}
footer{{border-top:1px solid var(--line);padding:28px 0 48px;font-size:14px;color:var(--muted)}}
footer p{{margin:6px 0}}
</style>
</head>
<body>
<header class="top"><div class="wrap">
  <b>exam-wiki-SS</b>
  <nav>{a('#path','路徑',ext=False)}{a('#units','單元',ext=False)}{a('#plan','進度表',ext=False)}{a(GLOBAL['wiki'],'題庫儀表板',ext=False)}</nav>
</div></header>

<main class="wrap">
<div class="hero">
  <div class="kicker">結構技師 ・ 鋼結構設計（SS）</div>
  <h1>從這裡開始</h1>
  <p class="lead">這裡把歷屆考古題整理成知識庫：先知道考什麼，再讀懂原理、記住公式、練真題，卡住就問 AI。照著下面六步走就好，不用一次把所有連結點完。</p>
  <div class="cta">
    {a(GLOBAL['frequency'],'第一步：看出題頻率熱圖','btn primary')}
    {a(GLOBAL['strategy_video'],'▶ 全科讀書策略影片','btn ghost')}
  </div>
  <div class="stats">
    <div><b>{len(UNITS)}</b>個重點單元</div>
    <div><b>{n_sol}</b>支解題影片</div>
    <div><b>{len(UNITS)}</b>本 NotebookLM 筆記本</div>
  </div>
</div>

<section id="path">
  <h2>六步學習路徑</h2>
  <p class="sub">每個單元都照這個順序走一遍。</p>
  <ol class="path">
    <li style="--c:var(--d1)"><div class="n">STEP 1</div><h3>定方向</h3><p>全科先看出題頻率熱圖和讀書策略影片；每個單元開始前，先花 15 分鐘看單元總覽，知道這單元考什麼。</p><span class="t">全科 30 分鐘＋每單元 15 分鐘</span></li>
    <li style="--c:var(--d2)"><div class="n">STEP 2</div><h3>懂原理</h3><p>讀觀念講義，或看講義影片，選一種就好。第一次接觸、覺得抽象，先看動畫版。</p><span class="t">每單元 2–3 小時</span></li>
    <li style="--c:var(--d6)"><div class="n">STEP 3</div><h3>試一題</h3><p>還沒準備好也先寫一題。寫不出來沒關係，卡過一次，後面看講義和解答時才知道自己在找什麼。</p><span class="t">30 分鐘</span></li>
    <li style="--c:var(--d3)"><div class="n">STEP 4</div><h3>記公式</h3><p>懂了原理再背。用公式記憶影片，配合單元總覽的「必須自己背」清單。</p><span class="t">每單元約 1 小時</span></li>
    <li style="--c:var(--d4)"><div class="n">STEP 5</div><h3>練題目</h3><p>限時自己寫，只看考卷會給的公式。寫完或卡住 5 分鐘以上，才看解題影片。</p><span class="t">每題 30–40 分鐘</span></li>
    <li style="--c:var(--d5)"><div class="n">STEP 6</div><h3>問到懂</h3><p>還是不懂，就丟進 NotebookLM 或任何 AI 追問，直到能自己講給別人聽。</p><span class="t">隨時</span></li>
  </ol>
  <div class="tip">
    <b>三個原則</b>
    <ul class="rules">
      <li><b>解題影片一定在自己寫過之後才看。</b>先看再寫會產生「我懂了」的錯覺，到考場還是寫不出來。</li>
      <li><b>讀資料不超過總時間的三分之一</b>，其餘時間都拿來練題。已有基礎的人，看完單元總覽就可以直接試寫，寫不出來再回講義查。</li>
      <li><b>答案和題解對不上，不一定是你錯。</b>部分題解仍在校對中，歡迎{a(GLOBAL['feedback'],'回報')}，你的回報會讓題解更正確。</li>
    </ul>
  </div>
</section>

<section id="units">
  <h2>各單元教材</h2>
  <p class="sub">依建議讀書順序排列，點開即可看到該單元全部教材。</p>
  {units_html}
</section>

<section id="plan">
  <h2>進度表範例</h2>
  <p class="sub">依你距離考試的時間選一個，照自己的步調調整。</p>
  <div class="tabs" role="tablist">
    <button role="tab" aria-selected="true" data-t="w8">8 週衝刺</button>
    <button role="tab" aria-selected="false" data-t="w12">12 週穩讀</button>
  </div>
  <div class="tablewrap" id="w8"><table><thead><tr><th>時間</th><th>單元</th><th>要做的事</th></tr></thead><tbody>{schedule_rows(8)}</tbody></table></div>
  <div class="tablewrap" id="w12" hidden><table><thead><tr><th>時間</th><th>單元</th><th>要做的事</th></tr></thead><tbody>{schedule_rows(12)}</tbody></table></div>
</section>

<section id="ai">
  <h2>怎麼問 AI 才有用</h2>
  <p class="sub">把 AI 當成隨時可以問的家教。下面幾種問法可以直接複製使用。</p>
  <div class="prompts">
    <div class="prompt"><b>卡在某一步</b>貼上題目和你算到的地方，問：<code>我算到這裡就卡住了，下一步為什麼要這樣做？先不要給我答案，給我提示。</code></div>
    <div class="prompt"><b>答案對不上</b>貼上你的算式，問：<code>我的答案和解答不一樣，請幫我找出是哪一步錯了，並說明錯的原因。</code></div>
    <div class="prompt"><b>確認真的懂了</b>讀完一個觀念後，問：<code>請出 3 題考這個觀念的小題，等我回答後再告訴我對不對。</code></div>
    <div class="prompt"><b>公式從哪來</b>對一條公式問：<code>這條公式的物理意義是什麼？每個變數變大時結果會怎麼變？</code></div>
  </div>
</section>
</main>

<footer><div class="wrap">
  <p><b>使用須知：</b>本站內容由作者整理並借助 AI 產生，已盡力校對，但仍可能有錯誤；請以現行規範與正式教材為準。</p>
  <p><b>發現錯誤或有建議？</b>{a(GLOBAL['feedback'],'填寫勘誤回報')}（需 GitHub 帳號，免費註冊），每一則回報都會讓這份教材更好。</p>
  <p>考古題來源：考選部公開試題。 ・ {a(GLOBAL['wiki'],'題庫儀表板（全部 98 題）',ext=False)}</p>
</div></footer>

<script>
document.querySelectorAll('.tabs button').forEach(b => b.addEventListener('click', () => {{
  document.querySelectorAll('.tabs button').forEach(x => x.setAttribute('aria-selected', x === b));
  ['w8','w12'].forEach(id => document.getElementById(id).hidden = id !== b.dataset.t);
}}));
</script>
<!-- 流量統計：註冊 GoatCounter 後，把 YOURCODE 換成你的代碼並取消註解
<script data-goatcounter="https://YOURCODE.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
-->
</body>
</html>
"""
    return html


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "start.html")
    out.write_text(build(), encoding="utf-8")
    print("wrote", out)
