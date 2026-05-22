#!/usr/bin/env python3
"""
霖楓學苑 · LF Academy — Master Handout Index Generator
Builds a navigable HTML index of ALL handouts across P3-P6.
"""
import os, glob, json
from datetime import datetime

BASE = r'G:\lam-fung-academy\講義'
OUTPUT = r'G:\lam-fung-academy\講義\master_index.html'

grades_data = {}
total = 0
for grade in ['P3', 'P4', 'P5', 'P6']:
    path = os.path.join(BASE, grade)
    if not os.path.exists(path):
        grades_data[grade] = []
        continue
    files = sorted(glob.glob(os.path.join(path, '*.html')))
    handouts = []
    for f in files:
        name = os.path.basename(f)
        pdf = f.replace('.html', '.pdf')
        has_pdf = os.path.exists(pdf)
        # Parse topic from filename
        topic = name.replace('.html', '').replace('LF-'+grade+'-', '')
        # Count SVGs
        with open(f, 'r', encoding='utf-8') as fh:
            svgs = fh.read().count('<svg')
        handouts.append({
            'filename': name,
            'topic': topic,
            'svgs': svgs,
            'has_pdf': has_pdf,
            'path': f'./{grade}/{name}',
            'pdf_path': f'./{grade}/{name.replace(".html", ".pdf")}'
        })
    grades_data[grade] = handouts
    total += len(handouts)

html = f'''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<title>霖楓學苑 · LF Academy — 講義總索引</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;700;900&family=Noto+Serif+HK:wght@700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Noto Sans HK',sans-serif;background:#F3F4F6;color:#1A1A1A;font-size:14px;line-height:1.6;}}
.header{{background:linear-gradient(135deg,#1A3C6D,#1E4D8C);color:white;padding:32px;text-align:center;}}
.header h1{{font-family:'Noto Serif HK',serif;font-size:28px;letter-spacing:4px;}}
.header .sub{{color:#C9A84C;font-size:14px;margin-top:6px;letter-spacing:2px;}}
.stats{{display:flex;justify-content:center;gap:24px;margin:16px 0;flex-wrap:wrap;}}
.stat{{background:rgba(255,255,255,0.15);padding:10px 20px;border-radius:20px;font-size:13px;}}
.container{{max-width:1200px;margin:0 auto;padding:20px;}}
.grade-section{{margin:20px 0;}}
.grade-title{{font-family:'Noto Serif HK',serif;font-size:22px;font-weight:900;color:#1A3C6D;padding:10px 16px;border-left:5px solid #C9A84C;background:#FFFBEB;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center;}}
.grade-title .count{{font-size:14px;color:#6B7280;font-weight:400;}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:8px;}}
.card{{background:white;border-radius:8px;padding:10px 14px;border:1px solid #D1D5DB;display:flex;align-items:center;gap:10px;transition:box-shadow 0.15s;text-decoration:none;color:inherit;}}
.card:hover{{box-shadow:0 4px 12px rgba(0,0,0,0.12);}}
.card .num{{width:36px;height:36px;border-radius:50%;background:#1A3C6D;color:white;font-weight:900;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.card .info{{flex:1;min-width:0;}}
.card .info .topic{{font-size:13px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
.card .info .meta{{font-size:10px;color:#6B7280;margin-top:2px;}}
.card .badge{{font-size:9px;padding:2px 6px;border-radius:3px;font-weight:700;flex-shrink:0;}}
.badge-svg{{background:#DBEAFE;color:#1E40AF;}}
.badge-pdf{{background:#DCFCE7;color:#166534;}}
.badge-nopdf{{background:#FEE2E2;color:#991B1B;}}
.footer{{text-align:center;padding:32px;color:#6B7280;font-size:12px;}}
.summary-bar{{background:white;border-radius:12px;padding:16px 24px;margin:20px 0;display:flex;gap:24px;justify-content:center;flex-wrap:wrap;box-shadow:0 1px 3px rgba(0,0,0,0.08);}}
.summary-item{{text-align:center;}}
.summary-item .val{{font-size:28px;font-weight:900;color:#1A3C6D;}}
.summary-item .lbl{{font-size:11px;color:#6B7280;}}
</style>
</head>
<body>
<div class="header">
<h1>霖楓學苑 · LF Academy</h1>
<div class="sub">不教數學，教避開陷阱。 — 全級講義總索引</div>
<div class="stats">
<div class="stat">📅 更新：{datetime.now().strftime('%Y-%m-%d %H:%M')}</div>
<div class="stat">📚 {total} 堂講義</div>
<div class="stat">📐 SVG 幾何圖形庫 v2.4</div>
<div class="stat">🧮 render_math v1.3</div>
</div>
</div>

<div class="container">
<div class="summary-bar">
'''

# Summary stats
for grade in ['P3','P4','P5','P6']:
    h = grades_data[grade]
    pdfs = sum(1 for x in h if x['has_pdf'])
    svgs = sum(x['svgs'] for x in h)
    html += f'<div class="summary-item"><div class="val">{len(h)}</div><div class="lbl">{grade} 講義</div></div>\n'
    html += f'<div class="summary-item"><div class="val">{pdfs}</div><div class="lbl">{grade} PDF</div></div>\n'
    html += f'<div class="summary-item"><div class="val">{svgs}</div><div class="lbl">{grade} SVGs</div></div>\n'

html += '</div>\n'

for grade in ['P5','P6','P4','P3']:
    handouts = grades_data[grade]
    if not handouts:
        continue
    pdf_count = sum(1 for h in handouts if h['has_pdf'])
    svg_total = sum(h['svgs'] for h in handouts)
    html += f'''
<div class="grade-section">
<div class="grade-title">{grade} · 小{["三","四","五","六"][["P3","P4","P5","P6"].index(grade)]} <span class="count">{len(handouts)} 堂 · {pdf_count} PDF · {svg_total} SVGs</span></div>
<div class="grid">
'''
    for i, h in enumerate(handouts):
        svg_badge = f'<span class="badge badge-svg">{h["svgs"]} SVG</span>' if h['svgs'] > 0 else ''
        pdf_badge = '<span class="badge badge-pdf">PDF</span>' if h['has_pdf'] else '<span class="badge badge-nopdf">NO PDF</span>'
        html += f'''  <a href="{h['path']}" class="card">
    <div class="num">{i+1}</div>
    <div class="info">
      <div class="topic">{h['topic'][:60]}</div>
      <div class="meta">LF-{grade}</div>
    </div>
    {svg_badge}
    {pdf_badge}
  </a>
'''
    html += '</div></div>\n'

html += f'''
<div class="footer">
霖楓學苑 · LF Academy · 不教數學，教避開陷阱。<br>
全級 P3-P6 共 {total} 堂講義 · 版本 v7 · 生成於 {datetime.now().strftime('%Y-%m-%d %H:%M')}
</div>
</div>
</body>
</html>'''

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Master index: {len(html)} chars, {total} handouts indexed')
print(f'Saved to: {OUTPUT}')
