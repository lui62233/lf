#!/usr/bin/env python3
"""Extend L26 with cuboid/cube/volume SVGs"""
import sys
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import cuboid, square, rectangle

# Generate SVGs
svgs = {
    'cuboid_8x5x3': cuboid(120, 50, 80),   # Long cuboid (L=8 ratio)
    'cuboid_10x6x4': cuboid(140, 60, 80),  # Medium cuboid
    'cube_5cm': cuboid(80, 80, 80),        # Cube (all sides equal)
    'cube_4cm': cuboid(70, 70, 70),        # Smaller cube
    'unit_cube': cuboid(50, 50, 50),       # 1cm³ unit cube
    'rect_area': rectangle(120, 60),        # 2D area comparison
}

def fig_card(title, svg, note=''):
    note_html = f'<div style="font-size:9px; color:var(--gray); margin-top:3px;">{note}</div>' if note else ''
    return f'''<div style="text-align:center; margin:8px 0; padding:8px; background:#F0F9FF; border:1px solid var(--borderc); border-radius:5px;">
<strong style="font-size:13px; color:var(--blue);">{title}</strong><br>
{svg}
{note_html}
</div>'''

# Read original
path = r'G:\lam-fung-academy\講義\P5\LF-P5-下-L26-體積概念+長方體正方體體積+表面面積.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# INSERT 1: After KP1 (體積概念), before 知識點二 — add cuboid & unit cube diagrams
insert1 = f'''
{fig_card('📦 長方體體積示意：長×闊×高（三維空間）', svgs['cuboid_8x5x3'], '長=8單位、闊=5單位、高=3單位。體積=8×5×3=120立方單位。注意體積是「三維」概念（cm³），不是面積（cm²）！')}

<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:8px 0;">
<div style="flex:1; min-width:200px;">{fig_card('🟦 正方體（特殊長方體）', svgs['cube_5cm'], '長=闊=高=5cm。V=a³=5³=125 cm³。正方體是長方體的特例。')}</div>
<div style="flex:1; min-width:200px;">{fig_card('📏 對比：面積（二維·cm²）', svgs['rect_area'], '長方形面積=l×w（二維）。千萬不要混淆：面積單位是cm²，體積單位是cm³！')}</div>
</div>
'''

# INSERT 2: After KP2 (長方體體積公式), add cuboid with dimensions
insert2 = f'''
{fig_card('📐 長方體體積 V = 長 × 闊 × 高 — 三維可視化', svgs['cuboid_10x6x4'], '標註：長(l)=10cm、闊(w)=6cm、高(h)=4cm。體積=10×6×4=240 cm³。每個邊的單位必須一致！')}
'''

# INSERT 3: After KP3 (正方體體積), before KP4
insert3 = f'''
<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:8px 0;">
<div style="flex:1; min-width:180px;">{fig_card('正方體 4cm', svgs['cube_4cm'], 'V=4³=64 cm³。注意：4³ ≠ 4×3！')}</div>
<div style="flex:1; min-width:180px;">{fig_card('正方體 5cm', svgs['cube_5cm'], 'V=5³=125 cm³。SA=6×5²=150 cm²。')}</div>
</div>
<div class="warn">⚠️ 注意：5³ = 5×5×5 = 125（不是 5×3=15）。a³ 是 a 自乘三次，不是 a 乘以 3！</div>
'''

# INSERT 4: After KP4 (表面面積 vs 體積) — surface area concept
insert4 = f'''
{fig_card('🔍 體積 vs 表面面積 — 同一個長方體的兩種計法', svgs['cuboid_10x6x4'], '體積(V)=內部空間=10×6×4=240 cm³（三維·立方）。表面面積(SA)=外包裝紙=2(10×6+10×4+6×4)=2(60+40+24)=248 cm²（二維·平方）。')}
'''

# Apply inserts
# Insert 1: After KP1 sync practice table, before KP2
m1 = '<!-- ═══════════════ PAGE 2: KP2'
# Find the actual marker
m1 = '<div class="kp-title">知識點二：長方體體積'
html = html.replace(m1, insert1 + '\n<div class="kp-title">知識點二：長方體體積', 1)

# Insert 2: After KP2 同步練習 table, before KP3
m2 = '<div class="kp-title">知識點三：正方體體積'
html = html.replace(m2, insert2 + '\n<div class="kp-title">知識點三：正方體體積', 1)

# Insert 3: After KP3 sync practice, before KP4
m3 = '<div class="kp-title">知識點四：表面面積（SA）VS 體積（V）'
html = html.replace(m3, insert3 + '\n<div class="kp-title">知識點四：表面面積（SA）VS 體積（V）', 1)

# Insert 4: After KP4 sync practice table, before the tiered practice section
m4 = '<div class="h1">三、課堂分層同步練習</div>'
html = html.replace(m4, insert4 + '\n' + m4, 1)

# Write
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

svg_count = html.count('<svg')
print(f'L26 extended: {len(html)} chars, {svg_count} SVGs added')
