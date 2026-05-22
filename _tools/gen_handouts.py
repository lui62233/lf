#!/usr/bin/env python3
"""Generate L31-L40 handouts for LF Academy P6 Semester 2 Final Sprint"""
import os

OUT = 'G:/lam-fung-academy/講義/P6'

def read_svg(name):
    with open(f'G:/lam-fung-academy/_tools/svg_{name}.svg', 'r', encoding='utf-8') as f:
        return f.read()

SVG = {}
for n in ['number_line','coordinate_plane','cylinder','prism','composite','inequality1','inequality2','bridge','growth']:
    SVG[n] = read_svg(n)

CSS = '''<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;500;700;900&family=Noto+Serif+HK:wght@600;700;900&display=swap');
  :root {
    --blue:#1A3C6D; --gold:#C9A84C; --red:#DC2626; --green:#16A34A;
    --white:#FFF; --ink:#1A1A1A; --gray:#6B7280;
    --lightbg:#F9FAFB; --borderc:#D1D5DB;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    font-family:'Noto Sans HK',sans-serif;
    background:#E5E5E5; color:var(--ink);
    font-size:13px; line-height:1.65;
    -webkit-font-smoothing:antialiased;
  }
  @media print {
    body { background:white; font-size:11px; }
    .pb { box-shadow:none; min-height:0; padding:24px 36px; }
    .pb.cover-page { page-break-after:always; }
    .page-break { page-break-before:always; }
    .no-print { display:none!important; }
    .qt .qw { background: repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px); border: 1px dashed #9CA3AF; }
    .qt td { padding:4px 6px; }
    .qt { font-size:10.5px; }
    .qt .qtxt { font-size:11.5px; }
    .h1 { font-size:14px; margin:12px 0 7px; }
    .h2 { font-size:12px; }
    .kp { padding:7px 10px; }
    .kp-rules { font-size:10.5px; }
    .ex { padding:7px 10px; }
    .ex-q { font-size:12px; }
    .warn { font-size:10.5px; padding:5px 8px; }
    .mn { font-size:12px; padding:8px 10px; }
    .sc { gap:6px; }
    .sc-i { padding:10px; }
    .sc-i .n { width:26px;height:26px;font-size:14px; }
    .sc-i .t { font-size:11px; }
    .tc { gap:8px; }
    .tc-w, .tc-r { padding:10px; }
    .et { font-size:10px; }
    .timer { font-size:10px; }
  }
  .container { max-width:1000px; margin:0 auto; }
  .pb {
    width:100%;
    background:var(--white);
    padding:36px 48px;
    display:flex; flex-direction:column;
  }
  .f  { display:inline-flex; flex-direction:column; align-items:center; vertical-align:middle; margin:0 2px; font-size:inherit; }
  .f .n { font-size:inherit; line-height:1.15; }
  .f .d { font-size:inherit; line-height:1.15; }
  .f .b { width:100%; height:1.4px; background:currentColor; margin:2px 0; min-width:16px; }
  .fd { display:inline-flex; flex-direction:column; align-items:center; vertical-align:middle; margin:0 3px; }
  .fd .n { font-size:16px; font-weight:700; line-height:1.15; }
  .fd .d { font-size:16px; font-weight:700; line-height:1.15; }
  .fd .b { width:100%; height:2px; background:currentColor; min-width:22px; margin:3px 0; }
  .fi { display:inline-flex; flex-direction:column; align-items:center; vertical-align:middle; margin:0 1px; font-size:inherit; }
  .fi .n { font-size:inherit; line-height:1; }
  .fi .d { font-size:inherit; line-height:1; }
  .fi .b { width:100%; height:1px; background:currentColor; min-width:12px; }
  .cover {
    justify-content:center; align-items:center; text-align:center;
    background:var(--white);
  }
  .cv-logo { font-family:'Noto Serif HK',serif; font-size:20px; font-weight:900; color:var(--blue); letter-spacing:6px; }
  .cv-badge {
    display:inline-block; border:1.5px solid var(--gold); color:var(--gold);
    padding:5px 22px; border-radius:20px; font-size:12px; letter-spacing:3px;
    margin:16px 0;
  }
  .cv-title { font-family:'Noto Serif HK',serif; font-size:28px; font-weight:900; color:var(--blue); letter-spacing:3px; margin:12px 0 6px; }
  .cv-sub { font-size:13px; color:var(--gray); margin-bottom:24px; }
  .cv-info {
    display:inline-block; text-align:left;
    background:var(--lightbg); border:1px solid var(--borderc); border-radius:8px;
    padding:18px 24px; font-size:12px; line-height:2;
  }
  .cv-info b { color:var(--blue); }
  .cv-row { margin-top:24px; font-size:13px; display:flex; gap:28px; flex-wrap:wrap; }
  .cv-row .ln { display:inline-block; width:100px; border-bottom:1px solid var(--borderc); }
  .h1 {
    font-family:'Noto Serif HK',serif;
    font-size:17px; font-weight:900; color:var(--blue);
    padding:7px 12px; margin:18px 0 10px;
    border-left:4px solid var(--gold); background:#FFFBEB;
  }
  .h2 {
    font-family:'Noto Serif HK',serif;
    font-size:14px; font-weight:700; color:var(--blue);
    margin:14px 0 6px; padding-bottom:3px; border-bottom:1px solid var(--borderc);
  }
  .kp { margin:10px 0; padding:11px 14px; background:var(--lightbg); border:1px solid var(--borderc); border-radius:5px; }
  .kp-title { font-size:14px; font-weight:900; color:var(--blue); margin-bottom:4px; }
  .kp-rules { font-size:12px; line-height:1.7; }
  .kp-rules ol,.kp-rules ul { padding-left:18px; }
  .ex { border:2px solid var(--gold); border-radius:7px; padding:11px 14px; margin:8px 0; background:#FFFDF5; }
  .ex-title { font-size:13px; font-weight:900; color:#92400E; margin-bottom:5px; }
  .ex-q { font-size:14px; font-weight:700; margin:5px 0; line-height:1.7; }
  .warn { background:#FEF2F2; border-left:3px solid var(--red); padding:6px 10px; margin:7px 0; font-size:12px; font-weight:600; color:#991B1B; }
  .mn { background:linear-gradient(135deg,#FFF8E7,#FFEDD5); border:2px solid var(--gold); border-radius:7px; padding:10px 14px; margin:7px 0; text-align:center; font-size:15px; font-weight:900; color:var(--blue); }
  .qt { width:100%; border-collapse:collapse; margin:6px 0; font-size:12px; }
  .qt th { background:var(--blue); color:white; padding:5px 8px; font-size:11px; font-weight:600; text-align:left; }
  .qt td { padding:6px 8px; border:1px solid var(--borderc); vertical-align:top; }
  .qt tr:nth-child(even) td { background:#FAFBFC; }
  .qt .qn { width:34px; text-align:center; font-weight:700; }
  .qt .qd { width:52px; text-align:center; font-size:10px; font-weight:700; }
  .qt .qw {
    min-height:80px;
    background: repeating-linear-gradient(transparent,transparent 22px,#E5E7EB 22px,#E5E7EB 23px);
  }
  .qt .qtxt { font-size:13px; line-height:1.7; }
  .d1 { background:#FEF3C7; color:#92400E; }
  .d2 { background:#DCFCE7; color:#166534; }
  .d3 { background:#DBEAFE; color:#1E40AF; }
  .d4 { background:#F3E8FF; color:#7C3AED; }
  .ss { display:inline-block; padding:1px 5px; border-radius:2px; font-size:8px; font-weight:700; }
  .sh { background:#FEE2E2; color:#991B1B; }
  .sm { background:#FEF3C7; color:#92400E; }
  .tc { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:8px 0; }
  .tc-w { background:#FEF2F2; border:2px solid #FECACA; border-radius:8px; padding:14px; text-align:center; }
  .tc-r { background:#F0FDF4; border:2px solid #BBF7D0; border-radius:8px; padding:14px; text-align:center; }
  .tc-w .lbl { font-size:14px; font-weight:900; color:var(--red); margin-bottom:5px; }
  .tc-r .lbl { font-size:14px; font-weight:900; color:var(--green); margin-bottom:5px; }
  .tc-w .eq { font-size:17px; color:var(--red); }
  .tc-r .eq { font-size:17px; color:var(--green); }
  .tc-w .why { font-size:10px; color:#991B1B; margin-top:4px; }
  .tc-r .why { font-size:10px; color:#14532D; margin-top:4px; }
  .sc { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin:8px 0; }
  .sc-i { background:var(--lightbg); border:2px solid var(--borderc); border-radius:8px; padding:12px; text-align:center; }
  .sc-i .n { width:30px;height:30px;border-radius:50%; background:var(--blue); color:white; font-weight:900; font-size:16px; display:flex; align-items:center; justify-content:center; margin:0 auto 6px; }
  .sc-i .t { font-size:13px; font-weight:900; }
  .sc-i .d { font-size:10px; color:var(--gray); line-height:1.4; margin-top:2px; }
  .et { width:100%; border-collapse:collapse; margin:6px 0; font-size:11px; }
  .et th { background:var(--red); color:white; padding:5px 8px; }
  .et td { padding:5px 8px; border:1px solid var(--borderc); }
  .timer-box { background:var(--lightbg); border:2px solid var(--red); border-radius:6px; padding:8px 12px; margin:4px 0; text-align:center; font-weight:700; color:var(--red); font-size:13px; }
  .end-note { text-align:center; margin-top:20px; padding-top:14px; border-top:1px solid var(--borderc); font-size:11px; color:var(--gray); }
  .exam-header {
    border:2px solid var(--blue);
    padding:14px 18px;
    margin-bottom:16px;
    text-align:center;
  }
  .exam-header .school {
    font-family:'Noto Serif HK',serif;
    font-size:18px; font-weight:900; color:var(--blue); letter-spacing:5px;
  }
  .exam-header .title {
    font-family:'Noto Serif HK',serif;
    font-size:22px; font-weight:900; color:var(--blue); letter-spacing:3px;
    margin:6px 0;
    border-top:1px solid var(--gold); border-bottom:1px solid var(--gold);
    padding:6px 0;
  }
  .exam-header .info {
    font-size:12px; color:var(--gray);
  }
  .score-box {
    display:flex; gap:8px; justify-content:center; margin:10px 0;
  }
  .score-box .sb {
    border:1.5px solid var(--borderc); border-radius:6px;
    padding:8px 14px; text-align:center; min-width:70px;
  }
  .score-box .sb .lbl { font-size:9px; color:var(--gray); }
  .score-box .sb .val { font-size:18px; font-weight:900; color:var(--blue); }
  .formula-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin:10px 0; }
  .formula-card { background:var(--lightbg); border:1px solid var(--borderc); border-radius:6px; padding:10px; text-align:center; }
  .formula-card .topic { font-size:10px; color:var(--gray); }
  .formula-card .name { font-size:12px; font-weight:900; color:var(--blue); margin:3px 0; }
  .formula-card .formula { font-size:14px; font-weight:700; color:var(--red); margin:3px 0; }
  .formula-card .note { font-size:9px; color:var(--gray); }
  .checklist { width:100%; border-collapse:collapse; margin:6px 0; font-size:12px; }
  .checklist td { padding:6px 8px; border:1px solid var(--borderc); }
  .checklist .trap-col { width:90px; font-weight:700; text-align:center; }
  .checklist .check-col { width:60px; text-align:center; }
  .goal-card { background:linear-gradient(135deg,#DBEAFE,#EFF6FF); border:2px solid var(--blue); border-radius:8px; padding:16px; margin:10px 0; text-align:center; }
  .goal-card .goal-num { font-size:36px; font-weight:900; color:var(--blue); }
  .goal-card .goal-label { font-size:13px; color:var(--blue); font-weight:700; margin-top:4px; }
  .plan-table { width:100%; border-collapse:collapse; margin:8px 0; font-size:11px; }
  .plan-table th { background:var(--green); color:white; padding:5px 8px; }
  .plan-table td { padding:6px 8px; border:1px solid var(--borderc); }
  .template-box { border:2px dashed var(--gold); border-radius:8px; padding:16px; margin:8px 0; background:#FFFDF5; }
  .template-box .tpl-title { font-size:13px; font-weight:900; color:#92400E; margin-bottom:8px; text-align:center; }
  .reflection-box { border:2px solid var(--green); border-radius:8px; padding:16px; margin:8px 0; background:#F0FDF4; }
  .reflection-box .ref-title { font-size:13px; font-weight:900; color:var(--green); margin-bottom:8px; text-align:center; }
  .bridge-card { border:2px solid var(--gold); border-radius:8px; padding:14px; margin:8px 0; background:linear-gradient(135deg,#FFFDF5,#FFF8E7); }
  .bridge-card .br-title { font-size:13px; font-weight:900; color:#92400E; margin-bottom:5px; }
  .svg-wrap { text-align:center; margin:10px 0; }
  .svg-wrap svg { max-width:100%; height:auto; }
</style>'''

FOOTER = '<div class="end-note">霖楓學苑 · LF Academy · 不教數學，教避開陷阱。</div>'

def page_break():
    return '</div>\n\n<div class="pb">'

def wrap_html(title, body, file_id, pages, questions):
    return f'''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{CSS}
</head>
<body>

<div class="container">

{body}

</div>

<div class="no-print" style="position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--blue);color:white;padding:10px 24px;border-radius:30px;font-size:13px;letter-spacing:1px;box-shadow:0 4px 16px rgba(0,0,0,.25);z-index:100;">
  Ctrl+P PDF | {pages}頁 · {questions}題 | {file_id} v6
</div>

</body>
</html>'''

def cover(code, num, title, sub, info_rows, extra_row=None):
    r = f'''<!-- PAGE 1: COVER -->
<div class="pb cover-page cover">
  <div class="cv-logo">霖楓學苑 · LF Academy</div>
  <div class="cv-badge">小六 · 第{num}堂 · 學生版講義</div>
  <div class="cv-title">{title}</div>
  <div class="cv-sub">{sub}</div>

  <div class="cv-info">
'''
    for b_text, rest in info_rows:
        r += f'    <b>{b_text}</b>{rest}<br>\n'
    r += '''  </div>

  <div class="cv-row">
    <span>學生姓名：<span class="ln"></span></span>
    <span>班級：<span class="ln"></span></span>
    <span>日期：<span class="ln"></span></span>
    <span>完成時長：<span class="ln"></span></span>
  </div>
</div>
'''
    return r

def qt_row(n, qtext, diff_class, diff_label, min_h=80):
    return f'    <tr><td class="qn">{n}</td><td class="qtxt">{qtext}</td><td class="qd {diff_class}">{diff_label}</td><td class="qw" style="min-height:{min_h}px;"></td></tr>\n'

def qt_row_score(n, qtext, score, min_h=60):
    return f'    <tr><td class="qn">{n}</td><td class="qtxt">{qtext}</td><td class="qd">/ {score}</td><td class="qw" style="min-height:{min_h}px;"></td></tr>\n'

def qt_table(header, rows_html):
    return f'  <table class="qt">\n    {header}\n{rows_html}  </table>\n'

def h1(text): return f'  <div class="h1">{text}</div>\n'
def h2(text): return f'  <div class="h2">{text}</div>\n'

def kp(title, rules_html, extra=''):
    ss = ''
    if 'SSPA' in title or '必考' in title or '高頻' in title:
        ss = ' <span class="ss sh">SSPA 必考</span>'
    return f'''  <div class="kp">
    <div class="kp-title">{title}{ss}</div>
    <div class="kp-rules">
      {rules_html}
    </div>
    {extra}
  </div>
'''

def example(title, q, wrong_eq, wrong_why, right_eq, right_why):
    return f'''  <div class="ex">
    <div class="ex-title">{title}</div>
    <div class="ex-q">{q}</div>
    <div class="tc">
      <div class="tc-w"><div class="lbl">❌ 常見錯誤</div><div class="eq">{wrong_eq}</div><div class="why">{wrong_why}</div></div>
      <div class="tc-r"><div class="lbl">✅ 正確解法</div><div class="eq">{right_eq}</div><div class="why">{right_why}</div></div>
    </div>
  </div>
'''

def mnemonic(text):
    return f'  <div class="mn">🧠 口訣：{text}</div>\n'

def warn(text):
    return f'  <div class="warn">⚠️ {text}</div>\n'

def error_table(errors):
    """errors = [(desc, fix), ...]"""
    r = '  <table class="et">\n    <tr><th>#</th><th>易錯點</th><th>正確做法</th></tr>\n'
    for i, (e, f) in enumerate(errors, 1):
        r += f'    <tr><td>{i}</td><td><strong>{e}</strong></td><td>{f}</td></tr>\n'
    r += '  </table>\n'
    return r

def strategy_cards(cards):
    """cards = [(num, title, desc), ...]"""
    r = '  <div class="sc">\n'
    for n, t, d in cards:
        r += f'    <div class="sc-i"><div class="n">{n}</div><div class="t">{t}</div><div class="d">{d}</div></div>\n'
    r += '  </div>\n'
    return r

def svg_block(svg_content):
    return f'  <div class="svg-wrap">{svg_content}</div>\n'

def section_table(title, rows):
    return f'  <div class="h2">{title}</div>\n  <table class="qt">\n    <tr><th class="qn">#</th><th>題目</th><th class="qd">難度</th><th>作答區</th></tr>\n{rows}  </table>\n'

print("Functions loaded. Will now generate files...")
print(f"Output dir: {OUT}")
print(f"SVGs loaded: {list(SVG.keys())}")
print("Ready.")
