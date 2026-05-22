#!/usr/bin/env python3
"""Add circle/geometry SVGs to P5 L21 and L36"""
import sys, re
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import circle_shape, square, rectangle, triangle, trapezoid

def fig_card(title, svg, note=''):
    note_html = f'<div style="font-size:9px; color:var(--gray); margin-top:3px;">{note}</div>' if note else ''
    return f'''<div style="text-align:center; margin:8px 0; padding:8px; background:#F0F9FF; border:1px solid var(--borderc); border-radius:5px;">
<strong style="font-size:13px; color:var(--blue);">{title}</strong><br>
{svg}
{note_html}
</div>'''

# ═══════════ L21: Circle basics ═══════════
path21 = r'G:\lam-fung-academy\講義\P5\LF-P5-下-L21_圓的認識.html'
with open(path21, 'r', encoding='utf-8') as f:
    html = f.read()

svgs_l21 = {
    'circle_basic': circle_shape(70),
    'circle_small': circle_shape(55),
}

insert_l21 = f'''
{fig_card('⭕ 圓的結構 — 圓心(O)、半徑(r)、直徑(d)', svgs_l21['circle_basic'], '圓心O是圓的中心點。半徑r是圓心到圓周的距離。直徑d=2r，穿過圓心連接圓周兩端。紅色虛線=直徑。')}

<div class="kp" style="margin-top:10px;">
<div class="kp-title">圓的關鍵關係</div>
<div class="kp-rules">
① <strong>直徑 = 2 × 半徑</strong>（d = 2r）<br>
② <strong>半徑 = 直徑 ÷ 2</strong>（r = d ÷ 2）<br>
③ <strong>圓周 = π × 直徑 = 2πr</strong>（C = πd = 2πr）<br>
④ <strong>圓面積 = π × 半徑²</strong>（A = πr²）
</div>
</div>
'''

# Insert after KP1 (圓的認識)
m1 = '知識點一：' if '知識點一' in html else '<div class="kp-title">'
# Find the first KP title about circles
if '圓的結構' in html or '圓心' in html or '半徑' in html:
    # Insert before the first KP section
    m = '<div class="kp">'
    idx = html.find(m)
    if idx > 0:
        html = html[:idx] + insert_l21 + '\n' + html[idx:]
        print('  L21: Inserted circle diagrams before first KP')

with open(path21, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'  L21: {html.count(chr(60)+"svg")} SVGs total')

# ═══════════ L36: SSPA Geometry review ═══════════
path36 = r'G:\lam-fung-academy\講義\P5\LF-P5-上-L36_SSPA幾何題滿分衝刺.html'
with open(path36, 'r', encoding='utf-8') as f:
    html = f.read()

svgs_l36 = {
    'square_s': square(80),
    'rect_r': rectangle(120, 70),
    'tri_r': triangle(110, 75, 'right'),
    'tri_i': triangle(110, 75, 'isosceles'),
    'trap_t': trapezoid(70, 120, 70),
    'circle_c': circle_shape(60),
}

insert_l36 = f'''
<div class="h1">📐 幾何圖形快速參考（本堂所有題目共用）</div>
<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:10px 0;">
<div style="flex:1; min-width:140px;">{fig_card('正方形 A=a²', svgs_l36['square_s'], 'P=4a')}</div>
<div style="flex:1; min-width:160px;">{fig_card('長方形 A=l×w', svgs_l36['rect_r'], 'P=2(l+w)')}</div>
<div style="flex:1; min-width:150px;">{fig_card('三角形 A=½bh', svgs_l36['tri_r'], '高⊥底邊')}</div>
</div>
<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:10px 0;">
<div style="flex:1; min-width:150px;">{fig_card('等腰三角形', svgs_l36['tri_i'], '兩腰相等·高在內部')}</div>
<div style="flex:1; min-width:160px;">{fig_card('梯形 A=½(a+b)h', svgs_l36['trap_t'], 'b₁=上底·b₂=下底')}</div>
<div style="flex:1; min-width:140px;">{fig_card('圓 A=πr²·C=2πr', svgs_l36['circle_c'], 'π≈3.14 或 22/7')}</div>
</div>
<div class="warn">⚠️ SSPA 幾何題最常見錯誤：① 混淆面積公式和周界公式 ② 忘記÷2（三角形/梯形）③ 高必須是垂直距離 ④ 單位寫錯（cm² vs cm）</div>
'''

m2 = '<div class="h1">'
# Find second h1 (after cover page)
matches = list(re.finditer(r'<div class="h1">', html))
if len(matches) >= 2:
    pos = matches[1].start()
    html = html[:pos] + insert_l36 + '\n' + html[pos:]
    print('  L36: Inserted geometry reference diagrams')

with open(path36, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'  L36: {html.count(chr(60)+"svg")} SVGs total')
