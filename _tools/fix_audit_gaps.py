#!/usr/bin/env python3
"""
Fix all critical P5 gaps found in system audit:
1. Deploy L08 from template to P5 directory (missing handout!)
2. Clean L32 duplicate
3. Add chart SVGs to L33 (data+equations integration)
4. Apply answer space fixes to L08 and L33
5. Rebuild all missing PDFs
"""
import sys, os, shutil, glob, re, subprocess
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import bar_simple, bar_composite, line_chart, pie_chart, data_table

P5 = r'G:\lam-fung-academy\講義\P5'
TEMPLATES = r'G:\lam-fung-academy\_templates'

# ═══════════ 1. Deploy L08 from template ═══════════
print('1. Deploying P5 L08 (異分母分數加法) from template...')

src = os.path.join(TEMPLATES, '學生版講義範例_L08_v6.html')
dst = os.path.join(P5, 'LF-P5-上-L08_異分母分數加法.html')

with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

# Apply v7 quality upgrades
# Fix answer spaces
for old, new in [('min-height:36px','min-height:75px'),('min-height:40px','min-height:75px'),
                 ('min-height:45px','min-height:75px'),('min-height:48px','min-height:80px'),
                 ('min-height:50px','min-height:80px'),('min-height:52px','min-height:80px'),
                 ('min-height:55px','min-height:85px'),('min-height:58px','min-height:88px'),
                 ('min-height:60px','min-height:90px')]:
    if old in html:
        html = html.replace(old, new)

# Fix print CSS
if '.qt .qw { background: none; border: 1px dashed #D1D5DB; }' in html:
    html = html.replace('.qt .qw { background: none; border: 1px dashed #D1D5DB; }',
                       '.qt .qw { background: repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px); border: 1px dashed #9CA3AF; }')

# Update naming to LF Academy
html = html.replace('學生版講義範例', '霖楓學苑 · LF Academy · P5-上-L08')
html = html.replace('範例_L08', 'LF-P5-上-L08')

with open(dst, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'  L08 deployed: {len(html)} chars, {html.count(chr(60)+"svg")} SVGs')

# ═══════════ 2. Clean L32 duplicate ═══════════
print('\n2. Cleaning L32 duplicate...')
v2_path = os.path.join(P5, 'LF-P5-下-L32_複合棒形圖+數據分析_v2.html')
orig_path = os.path.join(P5, 'LF-P5-下-L32_複合棒形圖+數據分析.html')

# The v2 has more content (from our extension script). Keep v2 as main, clean up.
if os.path.exists(v2_path):
    # v2 has more SVGs and content — promote it to the main file
    shutil.copy(v2_path, orig_path)
    os.remove(v2_path)
    print(f'  Promoted v2 -> main, removed duplicate')
else:
    print(f'  v2 not found, nothing to clean')

# ═══════════ 3. Add chart SVGs to L33 ═══════════
print('\n3. Adding chart SVGs to L33 (綜合方程數據應用)...')
l33_path = os.path.join(P5, 'LF-P5-下-L33_綜合-方程-數據-應用題.html')
if os.path.exists(l33_path):
    with open(l33_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Generate charts for data analysis section
    bar_data = bar_simple(
        {'A店':250,'B店':340,'C店':190,'D店':280},
        title='四店季度銷售額', ylabel='銷售額', unit='萬元', ystep=50
    )
    line_data = line_chart(
        {'第1次':72,'第2次':78,'第3次':85,'第4次':82,'第5次':90},
        title='SSPA模擬成績走勢', ylabel='分數', unit='分', ystep=10
    )

    insert = f'''
<div style="text-align:center; margin:10px 0; padding:8px; background:#F0F9FF; border:1px solid var(--borderc); border-radius:5px;">
<strong style="font-size:14px; color:var(--blue);">📊 數據分析參考圖表 — 方程應用</strong>
<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:8px 0;">
<div style="flex:1; min-width:240px;"><strong style="font-size:12px;">棒形圖：比較不同類別</strong><br>{bar_data}</div>
<div style="flex:1; min-width:240px;"><strong style="font-size:12px;">折線圖：追蹤變化趨勢</strong><br>{line_data}</div>
</div>
<div style="font-size:10px; color:var(--gray); margin-top:4px;">▲ 本堂練習：用方程解決數據分析問題。例如：「A店比B店多賣多少？」→ 設未知數→列方程→解題。</div>
</div>
'''

    # Insert before first KP or before tiered practice
    first_h1 = html.find('<div class="h1">')
    if first_h1 > 0:
        # Find second h1 (after cover page h1)
        second_h1 = html.find('<div class="h1">', first_h1 + 1)
        if second_h1 > 0:
            html = html[:second_h1] + insert + '\n' + html[second_h1:]
            print(f'  Inserted chart reference before first content section')

    # Fix answer spaces
    for old, new in [('min-height:48px','min-height:80px'),('min-height:50px','min-height:80px'),
                     ('min-height:52px','min-height:80px'),('min-height:55px','min-height:85px')]:
        if old in html:
            html = html.replace(old, new)

    if '.qt .qw { background: none; border: 1px dashed #D1D5DB; }' in html:
        html = html.replace('.qt .qw { background: none; border: 1px dashed #D1D5DB; }',
                           '.qt .qw { background: repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px); border: 1px dashed #9CA3AF; }')

    with open(l33_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  L33: {html.count(chr(60)+"svg")} SVGs total')
else:
    print(f'  L33 not found!')

# ═══════════ 4. Apply v7 fixes to any remaining P5 files ═══════════
print('\n4. Final sweep — applying v7 to any missed P5 files...')
all_p5 = glob.glob(os.path.join(P5, 'LF-P5-*.html'))
fixed = 0
for f in all_p5:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    changed = False
    for old, new in [('min-height:36px','min-height:75px'),('min-height:40px','min-height:75px'),
                     ('min-height:45px','min-height:75px'),('min-height:48px','min-height:80px'),
                     ('min-height:50px','min-height:80px')]:
        if old in html:
            html = html.replace(old, new)
            changed = True
    if '.qt .qw { background: none; border: 1px dashed #D1D5DB; }' in html:
        html = html.replace('.qt .qw { background: none; border: 1px dashed #D1D5DB; }',
                           '.qt .qw { background: repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px); border: 1px dashed #9CA3AF; }')
        changed = True
    if changed:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        fixed += 1
print(f'  {fixed} additional files fixed')

# ═══════════ 5. Build all missing PDFs ═══════════
print('\n5. Building missing PDFs...')
import pymupdf
edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

all_html = glob.glob(os.path.join(P5, 'LF-P5-*.html'))
built = 0
for f in all_html:
    pdf = f.replace('.html', '.pdf')
    if not os.path.exists(pdf):
        r = subprocess.run([edge, '--headless', '--disable-gpu', f'--print-to-pdf={pdf}', f'file:///{f}'],
                          capture_output=True, timeout=90)
        if r.returncode == 0:
            doc = pymupdf.open(pdf)
            name = os.path.basename(f)[:40]
            svgs = open(f, encoding='utf-8').read().count('<svg')
            print(f'  {name}: {len(doc)}p, {svgs} SVGs')
            doc.close()
            built += 1

print(f'  {built} PDFs built')

# Final counts
p5_html = len(glob.glob(os.path.join(P5, 'LF-P5-*.html')))
p5_pdf = len(glob.glob(os.path.join(P5, 'LF-P5-*.pdf')))
print(f'\n=== FINAL STATE ===')
print(f'P5 HTML: {p5_html}, P5 PDF: {p5_pdf}')
print(f'Match: {"OK" if p5_html == p5_pdf else "MISMATCH - " + str(p5_html - p5_pdf) + " PDFs missing"}')
