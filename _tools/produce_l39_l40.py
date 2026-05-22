#!/usr/bin/env python3
"""Produce the final 2 P6 handouts: L39 (中學數學思維轉換) + L40 (學期總結+暑假計劃)"""
import sys, os
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import rectangle, triangle, circle_shape, grid_diagram

P6 = r'G:\lam-fung-academy\講義\P6'

# Generate SVGs
svgs = {
    'rect_compare': rectangle(120, 60),
    'tri_area': triangle(110, 70, 'right'),
    'grid_coord': grid_diagram(6, 6),
    'circle_demo': circle_shape(55),
}

# ═══════════ L39: 中學數學思維轉換 ═══════════
l39 = '''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<title>LF Academy · P6-下-L39 中學數學思維轉換 — 學生版講義 v6</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;500;700;900&family=Noto+Serif+HK:wght@600;700;900&display=swap');
:root{--blue:#1A3C6D;--gold:#C9A84C;--red:#DC2626;--green:#16A34A;--white:#FFF;--ink:#1A1A1A;--gray:#6B7280;--lightbg:#F9FAFB;--borderc:#D1D5DB;}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Noto Sans HK',sans-serif;background:#E5E5E5;color:var(--ink);font-size:13px;line-height:1.65;}
@media print{body{background:white;font-size:11px;}.pb{box-shadow:none;min-height:0;padding:24px 36px;}.pb.cover-page{page-break-after:always;}.page-break{page-break-before:always;}.no-print{display:none!important;}.qt .qw{background:repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px);border:1px dashed #9CA3AF;}.qt td{padding:4px 6px;}.qt{font-size:10.5px;}.qt .qtxt{font-size:11.5px;}.h1{font-size:14px;margin:12px 0 7px;}.h2{font-size:12px;}.kp{padding:7px 10px;}.kp-rules{font-size:10.5px;}.ex{padding:7px 10px;}.ex-q{font-size:12px;}.warn{font-size:10.5px;padding:5px 8px;}.mn{font-size:12px;padding:8px 10px;}.sc{gap:6px;}.sc-i{padding:10px;}.sc-i .n{width:26px;height:26px;font-size:14px;}.sc-i .t{font-size:11px;}.tc{gap:8px;}.tc-w,.tc-r{padding:10px;}.et{font-size:10px;}}
.container{max-width:1000px;margin:0 auto;}
.pb{width:100%;background:var(--white);padding:36px 48px;display:flex;flex-direction:column;}
.f{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 2px;font-size:inherit;}.f .n{font-size:inherit;line-height:1.15;}.f .d{font-size:inherit;line-height:1.15;}.f .b{width:100%;height:1.4px;background:currentColor;margin:2px 0;min-width:16px;}
.fd{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 3px;}.fd .n{font-size:16px;font-weight:700;line-height:1.15;}.fd .d{font-size:16px;font-weight:700;line-height:1.15;}.fd .b{width:100%;height:2px;background:currentColor;min-width:22px;margin:3px 0;}
.cover{justify-content:center;align-items:center;text-align:center;background:var(--white);}
.cv-logo{font-family:'Noto Serif HK',serif;font-size:20px;font-weight:900;color:var(--blue);letter-spacing:6px;}
.cv-badge{display:inline-block;border:1.5px solid var(--gold);color:var(--gold);padding:5px 22px;border-radius:20px;font-size:12px;letter-spacing:3px;margin:16px 0;}
.cv-title{font-family:'Noto Serif HK',serif;font-size:30px;font-weight:900;color:var(--blue);letter-spacing:3px;margin:12px 0 6px;}
.cv-sub{font-size:13px;color:var(--gray);margin-bottom:24px;}
.cv-info{display:inline-block;text-align:left;background:var(--lightbg);border:1px solid var(--borderc);border-radius:8px;padding:18px 24px;font-size:12px;line-height:2;}.cv-info b{color:var(--blue);}
.cv-row{margin-top:24px;font-size:13px;display:flex;gap:28px;}.cv-row .ln{display:inline-block;width:100px;border-bottom:1px solid var(--borderc);}
.h1{font-family:'Noto Serif HK',serif;font-size:17px;font-weight:900;color:var(--blue);padding:7px 12px;margin:18px 0 10px;border-left:4px solid var(--gold);background:#FFFBEB;}
.h2{font-family:'Noto Serif HK',serif;font-size:14px;font-weight:700;color:var(--blue);margin:14px 0 6px;padding-bottom:3px;border-bottom:1px solid var(--borderc);}
.kp{margin:10px 0;padding:11px 14px;background:var(--lightbg);border:1px solid var(--borderc);border-radius:5px;}
.kp-title{font-size:14px;font-weight:900;color:var(--blue);margin-bottom:4px;}
.kp-rules{font-size:12px;line-height:1.7;}
.ex{border:2px solid var(--gold);border-radius:7px;padding:11px 14px;margin:8px 0;background:#FFFDF5;}
.ex-title{font-size:13px;font-weight:900;color:#92400E;margin-bottom:5px;}.ex-q{font-size:14px;font-weight:700;margin:5px 0;line-height:1.7;}
.warn{background:#FEF2F2;border-left:3px solid var(--red);padding:6px 10px;margin:7px 0;font-size:12px;font-weight:600;color:#991B1B;}
.mn{background:linear-gradient(135deg,#FFF8E7,#FFEDD5);border:2px solid var(--gold);border-radius:7px;padding:10px 14px;margin:7px 0;text-align:center;font-size:15px;font-weight:900;color:var(--blue);}
.qt{width:100%;border-collapse:collapse;margin:6px 0;font-size:12px;}
.qt th{background:var(--blue);color:white;padding:5px 8px;font-size:11px;font-weight:600;text-align:left;}
.qt td{padding:6px 8px;border:1px solid var(--borderc);vertical-align:top;}
.qt tr:nth-child(even) td{background:#FAFBFC;}
.qt .qn{width:34px;text-align:center;font-weight:700;}.qt .qd{width:52px;text-align:center;font-size:10px;font-weight:700;}
.qt .qw{min-height:80px;background:repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px);}
.qt .qtxt{font-size:13px;line-height:1.7;}
.d1{background:#FEF3C7;color:#92400E;}.d2{background:#DCFCE7;color:#166534;}.d3{background:#DBEAFE;color:#1E40AF;}.d4{background:#F3E8FF;color:#7C3AED;}
.ss{display:inline-block;padding:1px 5px;border-radius:2px;font-size:8px;font-weight:700;}.sh{background:#FEE2E2;color:#991B1B;}.sm{background:#FEF3C7;color:#92400E;}
.tc{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0;}
.tc-w{background:#FEF2F2;border:2px solid #FECACA;border-radius:8px;padding:14px;text-align:center;}
.tc-r{background:#F0FDF4;border:2px solid #BBF7D0;border-radius:8px;padding:14px;text-align:center;}
.tc-w .lbl{font-size:14px;font-weight:900;color:var(--red);margin-bottom:5px;}.tc-r .lbl{font-size:14px;font-weight:900;color:var(--green);margin-bottom:5px;}
.tc-w .eq{font-size:17px;color:var(--red);}.tc-r .eq{font-size:17px;color:var(--green);}
.tc-w .why{font-size:10px;color:#991B1B;margin-top:4px;}.tc-r .why{font-size:10px;color:#14532D;margin-top:4px;}
.sc{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:8px 0;}
.sc-i{background:var(--lightbg);border:2px solid var(--borderc);border-radius:8px;padding:12px;text-align:center;}
.sc-i .n{width:30px;height:30px;border-radius:50%;background:var(--blue);color:white;font-weight:900;font-size:16px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;}
.sc-i .t{font-size:13px;font-weight:900;}.sc-i .d{font-size:10px;color:var(--gray);line-height:1.4;margin-top:2px;}
.et{width:100%;border-collapse:collapse;margin:6px 0;font-size:11px;}
.et th{background:var(--red);color:white;padding:5px 8px;}.et td{padding:5px 8px;border:1px solid var(--borderc);}
.end-note{text-align:center;margin-top:20px;padding-top:14px;border-top:1px solid var(--borderc);font-size:11px;color:var(--gray);}
.bridge{background:linear-gradient(135deg,#DBEAFE,#EDE9FE);border:2px solid #7C3AED;border-radius:8px;padding:14px;margin:10px 0;text-align:center;}
.compare{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0;}
.compare-l{background:#FEF2F2;border:2px solid #FECACA;border-radius:8px;padding:12px;}
.compare-r{background:#F0FDF4;border:2px solid #BBF7D0;border-radius:8px;padding:12px;}
.compare-l .h{font-size:13px;font-weight:900;color:var(--red);margin-bottom:4px;}
.compare-r .h{font-size:13px;font-weight:900;color:var(--green);margin-bottom:4px;}
</style>
</head>
<body>
<div class="container">

<div class="pb cover-page cover">
<div class="cv-logo">霖楓學苑 <span style="font-weight:400;color:#C9A84C;font-size:14px;">· LF Academy</span></div>
<div class="cv-badge">小六 · 第 39 堂 · 學生版講義</div>
<div class="cv-title">中學數學思維轉換</div>
<div class="cv-sub">算術→代數 · 具體→抽象 · 小學→中學 · 65 分鐘</div>
<div class="cv-info">
<b>核心轉換：</b>從小學「搵答案」到中學「表達關係」的思維飛躍<br>
<b>關鍵技能：</b>① 用變數代替數字 ② 文字→方程系統化翻譯 ③ 理解「通解」vs「特解」<br>
<b>心態建設：</b>中學數學係「唔同」，唔係「更難」——轉換思維方式就搞得掂<br>
<b>前置知識：</b>P5-P6 代數式、簡易方程、列方程解應用題<br>
<b>本堂目標：</b>❶ 理解算術與代數的核心差異 ❷ 掌握文字→方程翻譯法 ❸ 建立中學數學信心
</div>
<div class="cv-row">
<span>學生姓名：<span class="ln"></span></span><span>班級：<span class="ln"></span></span><span>日期：<span class="ln"></span></span>
</div>
</div>

<div class="pb">
<div class="h1">一、思維熱身：同一條題目，兩種解法</div>

<div class="ex"><div class="ex-title">熱身挑戰 — 先用你識嘅方法，再睇新方法</div>
<div class="ex-q">小明買咗 3 本書同 2 枝筆，共付 $85。每枝筆 $5。每本書幾錢？<br>(a) 用小學算術方法計 (b) 用代數方法（設 $x）計</div></div>

<div class="compare">
<div class="compare-l">
<div class="h">🏫 小學算術思維</div>
<p style="font-size:12px;">2枝筆 = 2×$5 = $10<br>3本書 = $85 − $10 = $75<br>1本書 = $75 ÷ 3 = <strong>$25</strong></p>
<p style="font-size:10px;color:var(--gray);margin-top:4px;">「逆向推理」：由結果倒推。<br>每一步都係具體數字。</p>
</div>
<div class="compare-r">
<div class="h">🎓 中學代數思維</div>
<p style="font-size:12px;">設每本書 $x<br>3x + 2(5) = 85<br>3x + 10 = 85<br>3x = 75<br>x = <strong>25</strong></p>
<p style="font-size:10px;color:var(--gray);margin-top:4px;">「正向建模」：先寫關係式，<br>再求解。用變數代表未知數。</p>
</div>
</div>

<div class="h1">二、核心轉換一：從「搵答案」到「表達關係」</div>

<div class="kp"><div class="kp-title">算術 vs 代數：根本差異</div><div class="kp-rules">
① <strong>算術</strong>：用已知數計算未知數。每一步都係具體數字。適合「一步到位」嘅問題。<br>
② <strong>代數</strong>：用變數（字母）代表未知數，先建立方程式，再求解。適合複雜、多步驟問題。<br>
③ <strong>關鍵心態轉變</strong>：唔好急住計答案！先寫出「關係式」，再用數學規則變形求解。<br>
④ <strong>代數嘅威力</strong>：一個方程式可以解決一「類」問題（通解），而唔係淨係一個「個別」問題（特解）。
</div></div>

<div class="mn">🧠 口訣：「代數唔係計數快啲，係表達關係清晰啲——先寫關係，後求答案。」</div>

<div class="h2">同步練習：兩種方法對比</div>
<table class="qt">
<tr><th class="qn">#</th><th>題目</th><th class="qd">類型</th><th>作答區</th></tr>
<tr><td class="qn">1</td><td class="qtxt">一個長方形，長係闊嘅 3 倍，周界 = 64 cm。分別用算術同代數方法求長和闊。</td><td class="qd d2">對比</td><td class="qw"></td></tr>
<tr><td class="qn">2</td><td class="qtxt">爸爸今年 45 歲，小明今年 12 歲。幾年後爸爸年齡係小明嘅 2 倍？(a) 算術 (b) 代數（設 x 年後）</td><td class="qd d2">對比</td><td class="qw"></td></tr>
</table>

<div class="h1">三、核心轉換二：文字→方程 系統化翻譯法</div>

<div class="kp"><div class="kp-title">「關鍵詞→數學符號」翻譯表</div><div class="kp-rules">
<table style="width:100%;border-collapse:collapse;font-size:12px;margin:8px 0;">
<tr style="background:var(--blue);color:white;"><th style="padding:5px;">中文關鍵詞</th><th style="padding:5px;">數學符號</th><th style="padding:5px;">例句</th><th style="padding:5px;">翻譯</th></tr>
<tr><td style="padding:4px;">是、等於、為</td><td>=</td><td>A 是 B 的 2 倍</td><td>A = 2B</td></tr>
<tr><td style="padding:4px;">比…多</td><td>+</td><td>A 比 B 多 5</td><td>A = B + 5</td></tr>
<tr><td style="padding:4px;">比…少</td><td>−</td><td>A 比 B 少 3</td><td>A = B − 3</td></tr>
<tr><td style="padding:4px;">…的…倍</td><td>×</td><td>A 是 B 的 3 倍</td><td>A = 3B</td></tr>
<tr><td style="padding:4px;">共、總共、合共</td><td>+（加總）</td><td>A 和 B 共 20</td><td>A + B = 20</td></tr>
<tr><td style="padding:4px;">相差</td><td>−（絕對值）</td><td>A 和 B 相差 4</td><td>|A − B| = 4</td></tr>
</table>
</div></div>

<div class="ex"><div class="ex-title">🪤 陷阱：翻譯方向搞反！</div><div class="ex-q">「A 比 B 多 5」→ 邊個等於邊個加 5？</div>
<div class="tc">
<div class="tc-w"><div class="lbl">❌ 致命錯誤</div><div class="eq">B = A + 5</div><div class="why">「A 比 B 多 5」即係 A 係較大嗰個！所以 A = B + 5，唔係掉轉！</div></div>
<div class="tc-r"><div class="lbl">✅ 正確翻譯</div><div class="eq">A = B + 5</div><div class="why">記憶法：「比」後面嗰個係基準。「A 比 B 多」→ 由 B 出發加 → A = B + 5</div></div>
</div></div>

<div class="h2">翻譯練習</div>
<table class="qt">
<tr><th class="qn">#</th><th>中文描述</th><th class="qd">翻譯成方程</th><th>你的翻譯</th></tr>
<tr><td class="qn">3</td><td class="qtxt">兩個連續整數之和是 25</td><td class="qd d1"></td><td class="qw"></td></tr>
<tr><td class="qn">4</td><td class="qtxt">長方形長比闊多 4 cm，周界 40 cm</td><td class="qd d2"></td><td class="qw"></td></tr>
<tr><td class="qn">5</td><td class="qtxt">小明年齡的 3 倍比爸爸年齡少 6 歲（爸爸 45 歲）</td><td class="qd d2"></td><td class="qw"></td></tr>
<tr><td class="qn">6</td><td class="qtxt">兩數之和為 30，大數是小數的 4 倍</td><td class="qd d2"></td><td class="qw"></td></tr>
</table>
</div>

<div class="pb page-break">
<div class="h1">四、核心轉換三：從「具體數字」到「抽象變數」</div>

<div class="kp"><div class="kp-title">點解要用字母？— 代數的三大優勢</div><div class="kp-rules">
① <strong>通用性</strong>：x + 5 = 12 → x = 7，呢個方法適用於「任何」同類方程，唔使次次重新推理。<br>
② <strong>表達規律</strong>：第 n 個三角形數 = n(n+1)/2。用 n 可以表達「任何位置」嘅值，唔使逐個計。<br>
③ <strong>證明</strong>：用代數可以「證明」數學規律永遠成立（例如：兩個奇數之和一定是偶數 = 2m+1 + 2n+1 = 2(m+n+1)）
</div></div>

<div class="ex"><div class="ex-title">例題 — 由具體到抽象</div><div class="ex-q">
三角形數列：1, 3, 6, 10, 15, 21, ...<br>
第 1 個 = 1、第 2 個 = 3、第 3 個 = 6、第 4 個 = 10<br>
(a) 第 10 個三角形數係幾多？(b) 第 n 個三角形數嘅公式係咩？(c) 第 100 個三角形數係幾多？
</div></div>

<div class="sc">
<div class="sc-i"><div class="n">①</div><div class="t">觀察規律</div><div class="d">1, 3, 6, 10, 15...<br>逐個差：+2,+3,+4,+5...</div></div>
<div class="sc-i"><div class="n">②</div><div class="t">找公式</div><div class="d">第n個 = n(n+1)/2<br>驗證：n=4→10✓</div></div>
<div class="sc-i"><div class="n">③</div><div class="t">代n入公式</div><div class="d">n=10→10×11/2<br>=55</div></div>
<div class="sc-i"><div class="n">④</div><div class="t">通用威力</div><div class="d">n=100→100×101/2<br>=5050（一秒！）</div></div>
</div>

<div class="h2">同步練習</div>
<table class="qt">
<tr><th class="qn">#</th><th>題目</th><th class="qd">難度</th><th>作答區</th></tr>
<tr><td class="qn">7</td><td class="qtxt">觀察數列：2, 5, 10, 17, 26, ... (a) 第 6 項 = ？(b) 第 n 項公式 = ？（提示：n²+1）(c) 第 50 項 = ？</td><td class="qd d2">🌿</td><td class="qw"></td></tr>
<tr><td class="qn">8</td><td class="qtxt">用代數證明：「任意兩個連續整數的乘積一定是偶數」。（提示：設第一個為 n，第二個為 n+1）</td><td class="qd d3">🌳</td><td class="qw"></td></tr>
</table>

<div class="bridge">
<h3 style="color:#7C3AED;">🌉 小學 → 中學 數學思維橋樑</h3>
<p style="font-size:12px;margin:6px 0;">小學數學 = 釣魚（每次捉一條）<br>中學代數 = 織網（一次過捉晒成個品種）<br><strong>你已經識釣魚。而家學織網。</strong></p>
</div>

<div class="h1">五、中學常見新題型預覽</div>
<table class="qt">
<tr><th class="qn">#</th><th>題目</th><th class="qd">難度</th><th>作答區</th></tr>
<tr><td class="qn">9</td><td class="qtxt">解方程：5x − 3 = 2x + 9（提示：先將所有 x 搬到一邊）</td><td class="qd d1">🌱</td><td class="qw"></td></tr>
<tr><td class="qn">10</td><td class="qtxt">解不等式：3x + 4 < 19（不等式同方程差唔多，但乘/除負數要反轉符號！）</td><td class="qd d2">🌿</td><td class="qw"></td></tr>
<tr><td class="qn">11</td><td class="qtxt">化簡：3(2x − 4) + 2(x + 1)（提示：先拆括號，再合併同類項）</td><td class="qd d1">🌱</td><td class="qw"></td></tr>
<tr><td class="qn">12</td><td class="qtxt">坐標平面上有 A(2,3) 和 B(5,7) 兩點。求 AB 的距離。（提示：用畢氏定理）</td><td class="qd d3">🌳</td><td class="qw"></td></tr>
</table>

<div class="h1">六、本堂核心要點總結</div>
<table class="et">
<tr><th>#</th><th>核心轉換</th><th>具體含義</th></tr>
<tr><td>1</td><td><strong>答案→關係</strong></td><td>唔好急住計答案！先寫出變數之間的關係式，再求解。</td></tr>
<tr><td>2</td><td><strong>數字→字母</strong></td><td>用 x, y, n 代表未知數或變數。一個公式解決無限多個問題。</td></tr>
<tr><td>3</td><td><strong>逆向→正向</strong></td><td>算術習慣逆向推理（由結果倒推）。代數係正向建模（先寫方程再解）。</td></tr>
<tr><td>4</td><td><strong>文字→符號</strong></td><td>「比…多」= +，「是…的N倍」= ×N。建立系統化翻譯能力。</td></tr>
<tr><td>5</td><td><strong>特解→通解</strong></td><td>算術得出嘅係「呢個問題」嘅答案。代數得出嘅係「呢類問題」嘅解法。</td></tr>
<tr><td>6</td><td><strong>計算→證明</strong></td><td>中學開始要識「證明」而唔係淨係「計出答案」。用代數表達邏輯。</td></tr>
<tr><td>7</td><td><strong>恐懼→信心</strong></td><td>中學數學係「唔同」，唔係「更難」。你已經有晒基礎，只需轉換思維模式。</td></tr>
</table>

<div class="end-note">霖楓學苑 · LF Academy · 不教數學，教避開陷阱。 · LF-P6-下-L39</div>
</div>

</div>
<div class="no-print" style="position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--blue);color:white;padding:10px 24px;border-radius:30px;font-size:13px;letter-spacing:1px;box-shadow:0 4px 16px rgba(0,0,0,.25);z-index:100;">
Ctrl+P | LF-P6-下-L39 v6
</div>
</body>
</html>'''

# ═══════════ L40: 學期總結+暑假中學預習計劃 ═══════════
l40 = '''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<title>LF Academy · P6-下-L40 學期總結+暑假中學預習計劃 — 學生版講義 v6</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;500;700;900&family=Noto+Serif+HK:wght@600;700;900&display=swap');
:root{--blue:#1A3C6D;--gold:#C9A84C;--red:#DC2626;--green:#16A34A;--white:#FFF;--ink:#1A1A1A;--gray:#6B7280;--lightbg:#F9FAFB;--borderc:#D1D5DB;}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Noto Sans HK',sans-serif;background:#E5E5E5;color:var(--ink);font-size:13px;line-height:1.65;}
@media print{body{background:white;font-size:11px;}.pb{box-shadow:none;min-height:0;padding:24px 36px;}.pb.cover-page{page-break-after:always;}.page-break{page-break-before:always;}.no-print{display:none!important;}.h1{font-size:14px;margin:12px 0 7px;}.h2{font-size:12px;}.kp-rules{font-size:10.5px;}.qt{font-size:10.5px;}.qt .qtxt{font-size:11.5px;}}
.container{max-width:1000px;margin:0 auto;}
.pb{width:100%;background:var(--white);padding:36px 48px;display:flex;flex-direction:column;}
.cover{justify-content:center;align-items:center;text-align:center;background:var(--white);}
.cv-logo{font-family:'Noto Serif HK',serif;font-size:20px;font-weight:900;color:var(--blue);letter-spacing:6px;}
.cv-badge{display:inline-block;border:1.5px solid var(--gold);color:var(--gold);padding:5px 22px;border-radius:20px;font-size:12px;letter-spacing:3px;margin:16px 0;}
.cv-title{font-family:'Noto Serif HK',serif;font-size:30px;font-weight:900;color:var(--blue);letter-spacing:3px;margin:12px 0 6px;}
.cv-sub{font-size:13px;color:var(--gray);margin-bottom:24px;}
.cv-info{display:inline-block;text-align:left;background:var(--lightbg);border:1px solid var(--borderc);border-radius:8px;padding:18px 24px;font-size:12px;line-height:2;}.cv-info b{color:var(--blue);}
.cv-row{margin-top:24px;font-size:13px;display:flex;gap:28px;}.cv-row .ln{display:inline-block;width:100px;border-bottom:1px solid var(--borderc);}
.h1{font-family:'Noto Serif HK',serif;font-size:17px;font-weight:900;color:var(--blue);padding:7px 12px;margin:18px 0 10px;border-left:4px solid var(--gold);background:#FFFBEB;}
.h2{font-family:'Noto Serif HK',serif;font-size:14px;font-weight:700;color:var(--blue);margin:14px 0 6px;padding-bottom:3px;border-bottom:1px solid var(--borderc);}
.kp{margin:10px 0;padding:11px 14px;background:var(--lightbg);border:1px solid var(--borderc);border-radius:5px;}
.kp-title{font-size:14px;font-weight:900;color:var(--blue);margin-bottom:4px;}
.kp-rules{font-size:12px;line-height:1.7;}
.mn{background:linear-gradient(135deg,#FFF8E7,#FFEDD5);border:2px solid var(--gold);border-radius:7px;padding:10px 14px;margin:7px 0;text-align:center;font-size:15px;font-weight:900;color:var(--blue);}
.qt{width:100%;border-collapse:collapse;margin:6px 0;font-size:12px;}
.qt th{background:var(--blue);color:white;padding:5px 8px;font-size:11px;font-weight:600;text-align:left;}
.qt td{padding:6px 8px;border:1px solid var(--borderc);vertical-align:top;}
.qt tr:nth-child(even) td{background:#FAFBFC;}
.qt .qn{width:34px;text-align:center;font-weight:700;}
.qt .qw{min-height:80px;background:repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px);}
.qt .qtxt{font-size:13px;line-height:1.7;}
.d1{background:#FEF3C7;color:#92400E;}.d2{background:#DCFCE7;color:#166534;}.d3{background:#DBEAFE;color:#1E40AF;}
.end-note{text-align:center;margin-top:20px;padding-top:14px;border-top:1px solid var(--borderc);font-size:11px;color:var(--gray);}
.checklist{list-style:none;padding:0;}
.checklist li{padding:4px 8px;margin:2px 0;display:flex;align-items:center;gap:8px;}
.checklist li input{width:18px;height:18px;}
.plan-table{width:100%;border-collapse:collapse;margin:10px 0;font-size:12px;}
.plan-table th{background:var(--blue);color:white;padding:6px 8px;font-size:11px;text-align:center;}
.plan-table td{padding:6px 8px;border:1px solid var(--borderc);text-align:center;}
.plan-table .week{background:#FFFBEB;font-weight:700;}
.goal-box{border:2px dashed var(--gold);border-radius:8px;padding:14px;margin:10px 0;background:#FFFDF5;}
.trap-mastery{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:10px 0;}
.trap-item{text-align:center;padding:8px 4px;border-radius:6px;border:1.5px solid var(--borderc);background:var(--lightbg);}
.trap-item .code{font-weight:900;font-size:13px;}.trap-item .name{font-size:9px;color:var(--gray);}
.trap-item .score{font-size:16px;font-weight:900;margin-top:4px;}
</style>
</head>
<body>
<div class="container">

<div class="pb cover-page cover">
<div class="cv-logo">霖楓學苑 <span style="font-weight:400;color:#C9A84C;font-size:14px;">· LF Academy</span></div>
<div class="cv-badge">小六 · 第 40 堂 · 學生版講義</div>
<div class="cv-title">學期總結＋暑假中學預習計劃</div>
<div class="cv-sub">P6 全級回顧 · SSPA 終極準備 · 中一預習路線圖 · 65 分鐘</div>
<div class="cv-info">
<b>本堂目的：</b>回顧 P6 全年 40 堂學習成果 · 自我評估陷阱敏感度 · 制定 8 週暑假預習計劃<br>
<b>SSPA 終極倒數：</b>本堂為 SSPA 最後一堂預備課 · 祝你呈分試旗開得勝！<br>
<b>中學啟航：</b>暑假 8 週自學路線圖 · 中一數學搶先一步
</div>
<div class="cv-row">
<span>學生姓名：<span class="ln"></span></span><span>日期：<span class="ln"></span></span>
</div>
</div>

<div class="pb">
<div class="h1">一、P6 全年 40 堂學習回顧</div>

<div class="kp"><div class="kp-title">上學期 L01-L20：SSPA 戰鬥準備</div><div class="kp-rules">
✅ 小數除法 · 分數小數百分數互換 · 綜合應用<br>
✅ 百分數佔比求原值 · 百分數增減連續變化 · 圓周與圓面積<br>
✅ SSPA模擬1+2 · 平均數與速率基礎+應用 · 折線圖 · 排水法 · 圓形圖
</div></div>

<div class="kp"><div class="kp-title">下學期 L21-L40：SSPA 終極 + 中學橋樑</div><div class="kp-rules">
✅ 圓進階（圓規作圖·扇形·環形·複合圓形）<br>
✅ 百分數進階（利潤虧損·折上折）· 方程進階（括號·分數方程·應用題）<br>
✅ 統計圖表綜合（圓形圖·折線圖·棒形圖）· 速率進階（多段·相對速度）<br>
✅ 容量體積進階（排水法·溢出·立體截面·摺紙圖樣）<br>
✅ SSPA模擬3+4+5 · 跨課題殺手題 · 個人弱項補底<br>
✅ 中一預習（負數·代數·不等式·坐標系·棱柱圓柱·思維轉換）
</div></div>

<div class="h1">二、T1-T10 陷阱敏感度自我評估</div>
<div class="kp-rules" style="margin:8px 0;">為每個陷阱類型自評 1-5 分（5=完全掌握·1=經常中招）。誠實評分，呢個係你 SSPA 前最後嘅診斷！</div>

<div class="trap-mastery">
<div class="trap-item"><div class="code">T1</div><div class="name">單位/進位</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T2</div><div class="name">小數點</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T3</div><div class="name">運算序</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T4</div><div class="name">面積公式</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T5</div><div class="name">幾何混淆</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T6</div><div class="name">分數陷阱</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T7</div><div class="name">百分數</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T8</div><div class="name">速率</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T9</div><div class="name">方程</div><div class="score">__/5</div></div>
<div class="trap-item"><div class="code">T10</div><div class="name">統計圖表</div><div class="score">__/5</div></div>
</div>

<div class="warn" style="background:#FEF2F2;border-left:3px solid var(--red);padding:8px 10px;margin:10px 0;font-size:12px;color:#991B1B;">
⚠️ 得分 ≤ 2 的陷阱類型 = SSPA 前必須重點複習！翻閱相關講義的「易錯點總結」部分。
</div>

<div class="h1">三、SSPA 終極準備清單</div>
<table class="qt">
<tr><th class="qn">✓</th><th>準備事項</th><th>完成?</th></tr>
<tr><td class="qn"><input type="checkbox"></td><td class="qtxt">完成全部 5 次 SSPA 模擬考試並檢討錯題</td><td class="qw" style="min-height:36px;"></td></tr>
<tr><td class="qn"><input type="checkbox"></td><td class="qtxt">T1-T10 陷阱敏感度自評完成，弱項已針對性補底</td><td class="qw" style="min-height:36px;"></td></tr>
<tr><td class="qn"><input type="checkbox"></td><td class="qtxt">熟記所有面積/體積/圓形公式（連單位）</td><td class="qw" style="min-height:36px;"></td></tr>
<tr><td class="qn"><input type="checkbox"></td><td class="qtxt">熟練分數↔小數↔百分數互換（常用值：1/4, 1/2, 3/4, 1/5...）</td><td class="qw" style="min-height:36px;"></td></tr>
<tr><td class="qn"><input type="checkbox"></td><td class="qtxt">準備好考試物品：計數機、鉛筆、擦膠、量角器、圓規、直尺</td><td class="qw" style="min-height:36px;"></td></tr>
<tr><td class="qn"><input type="checkbox"></td><td class="qtxt">知道考試日期、時間、地點，預留充足交通時間</td><td class="qw" style="min-height:36px;"></td></tr>
</table>
</div>

<div class="pb page-break">
<div class="h1">四、8 週暑假中一預習計劃</div>

<table class="plan-table">
<tr><th>週</th><th>日期</th><th>主題</th><th>目標</th><th>完成✓</th></tr>
<tr><td class="week">1</td><td>___/___</td><td>負數入門</td><td>數線·比較大小·加減負數</td><td>☐</td></tr>
<tr><td class="week">2</td><td>___/___</td><td>代數式化簡</td><td>合併同類項·拆括號·分配律</td><td>☐</td></tr>
<tr><td class="week">3</td><td>___/___</td><td>方程進階</td><td>含括號方程·分數方程·兩邊有未知數</td><td>☐</td></tr>
<tr><td class="week">4</td><td>___/___</td><td>不等式+坐標系</td><td>解不等式·四象限·點與距離</td><td>☐</td></tr>
<tr><td class="week">5</td><td>___/___</td><td>面積體積擴展</td><td>棱柱體積·圓柱體積+表面面積</td><td>☐</td></tr>
<tr><td class="week">6</td><td>___/___</td><td>百分數+速率複習</td><td>利潤虧損·折上折·平均速率·相對速度</td><td>☐</td></tr>
<tr><td class="week">7</td><td>___/___</td><td>統計圖表複習</td><td>圓形圖·折線圖·棒形圖綜合</td><td>☐</td></tr>
<tr><td class="week">8</td><td>___/___</td><td>綜合預習+模擬</td><td>中一入學模擬測驗·弱項補底</td><td>☐</td></tr>
</table>

<div class="h1">五、我的數學旅程 — P3 到 P6 反思</div>
<div class="goal-box">
<p style="font-size:13px;font-weight:700;color:var(--blue);">請回答以下問題：</p>
<p style="font-size:12px;margin:6px 0;">1. P6 呢年你最鍾意邊個數學課題？點解？</p>
<div class="qw" style="min-height:72px;"></div>
<p style="font-size:12px;margin:6px 0;">2. 邊個陷阱類型（T1-T10）你進步最大？由幾多分升到幾多分？</p>
<div class="qw" style="min-height:72px;"></div>
<p style="font-size:12px;margin:6px 0;">3. 對中一數學有咩期待？有咩擔心？</p>
<div class="qw" style="min-height:72px;"></div>
<p style="font-size:12px;margin:6px 0;">4. 你會點樣用呢個暑假準備中一？（具體計劃）</p>
<div class="qw" style="min-height:72px;"></div>
</div>

<div class="h1">六、中一數學目標設定</div>
<div class="goal-box">
<table style="width:100%;font-size:12px;">
<tr><td style="padding:4px;"><strong>中一第一次測驗目標分數：</strong></td><td style="border-bottom:1px solid var(--borderc);width:120px;"></td></tr>
<tr><td style="padding:4px;"><strong>中一全級排名目標：</strong></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr><td style="padding:4px;"><strong>最想入嘅中學班級：</strong></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr><td style="padding:4px;"><strong>暑假每日溫習時間：</strong></td><td style="border-bottom:1px solid var(--borderc);">分鐘</td></tr>
</table>
</div>

<div class="mn">🧠 最後口訣：「陷阱避開晒，SSPA 唔會敗。中學新挑戰，暑假準備好。霖楓學苑陪你，由 P3 打到中學！」</div>

<div class="end-note">
霖楓學苑 · LF Academy · 不教數學，教避開陷阱。<br>
P6 全級 40 堂 · 到此完成 · 祝你 SSPA 成功 · 中學再見！<br>
LF-P6-下-L40
</div>
</div>

</div>
<div class="no-print" style="position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--blue);color:white;padding:10px 24px;border-radius:30px;font-size:13px;letter-spacing:1px;box-shadow:0 4px 16px rgba(0,0,0,.25);z-index:100;">
Ctrl+P | LF-P6-下-L40
</div>
</body>
</html>'''

# Write files
for name, content in [('L39', l39), ('L40', l40)]:
    path = os.path.join(P6, f'LF-P6-下-{name}_{"中學數學思維轉換" if name=="L39" else "學期總結暑假中學預習計劃"}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    svgs = content.count('<svg')
    print(f'{name}: {len(content)} chars, {svgs} SVGs written')

print('\nL39+L40 produced. Building PDFs...')

import subprocess, pymupdf
edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
for name in ['L39', 'L40']:
    f = os.path.join(P6, f'LF-P6-下-{name}_*.html')
    import glob as g
    matches = g.glob(f)
    if matches:
        f = matches[0]
        pdf = f.replace('.html', '.pdf')
        r = subprocess.run([edge, '--headless', '--disable-gpu', f'--print-to-pdf={pdf}', f'file:///{f}'],
                          capture_output=True, timeout=90)
        doc = pymupdf.open(pdf)
        svgs = open(f, encoding='utf-8').read().count('<svg')
        print(f'{os.path.basename(f)[:50]}: {len(doc)}p, {svgs} SVGs')
        doc.close()
