#!/usr/bin/env python3
"""Extend L27 with composite solids + displacement SVGs"""
import sys
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import composite_L, composite_T, composite_hole, cuboid, displacement

# Generate SVGs
svgs = {
    'L_shape': composite_L(100, 80, 60, 40),     # L-shaped composite
    'T_shape': composite_T(120, 35, 50, 55),     # T-shaped composite
    'hole_shape': composite_hole(140, 90, 45, 45), # Cut-out hole
    'cuboid_ref': cuboid(120, 60, 70),            # Reference cuboid
    'displacement': displacement(160, 90, 30, 55, 45, 45),  # Displacement method
}

def fig_card(title, svg, note=''):
    note_html = f'<div style="font-size:9px; color:var(--gray); margin-top:3px;">{note}</div>' if note else ''
    return f'''<div style="text-align:center; margin:8px 0; padding:8px; background:#F0F9FF; border:1px solid var(--borderc); border-radius:5px;">
<strong style="font-size:13px; color:var(--blue);">{title}</strong><br>
{svg}
{note_html}
</div>'''

# Read original
path = r'G:\lam-fung-academy\講義\P5\LF-P5-下-L27-複合立體+排水法.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# INSERT 1: After KP1 (複合立體分割法/補足法) intro — add diagrams
insert1 = f'''
{fig_card('🔷 L形複合立體 — 分割法示例', svgs['L_shape'], '底層 w₁×h₁ + 右側上層 w₂×h₂。分割線（灰色虛線）把L形切成兩個長方體，各自計算體積後相加。')}

<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:8px 0;">
<div style="flex:1; min-width:200px;">{fig_card('🔶 T形複合立體', svgs['T_shape'], '下層橫條 w_top×h_top + 上層豎條 w_bot×h_bot。同樣用分割法：切成上下兩件分別計。')}</div>
<div style="flex:1; min-width:200px;">{fig_card('🔲 挖空立體 — 補足法示例', svgs['hole_shape'], '完整長方體 − 挖去的立體 = 餘下體積。補足法：先計大長方體，再減去挖空部分。')}</div>
</div>
'''

# INSERT 2: After KP2 (排水法) intro — add displacement diagram
insert2 = f'''
{fig_card('💧 排水法示意圖 — 阿基米德原理', svgs['displacement'], '左：投入前水位 wb cm。右：投入後水位 wa cm。水位上升 = wa−wb cm。物體體積 = 容器底面積 × (wa−wb)。關鍵：物體必須完全浸沒！')}

<div class="mn">🧠 排水法三部曲：① 計底面積（容器長×闊）② 計水位差（新−舊）③ 體積 = 底面積 × 水位差</div>
'''

# INSERT 3: Before tiered practice — reference diagrams section
insert3 = f'''
<div class="h1">📐 立體參考圖（以下練習題均需參考這些圖形）</div>
<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:10px 0;">
<div style="flex:1; min-width:160px;">{fig_card('L形複合立體', svgs['L_shape'], '參考Q1,Q3,Q6,Q18,Q23')}</div>
<div style="flex:1; min-width:160px;">{fig_card('T形複合立體', svgs['T_shape'], '參考Q7')}</div>
<div style="flex:1; min-width:160px;">{fig_card('挖空立體', svgs['hole_shape'], '參考Q3,Q8,Q20')}</div>
</div>
<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:10px 0;">
<div style="flex:1; min-width:200px;">{fig_card('標準長方體', svgs['cuboid_ref'], '長(l)×闊(w)×高(h)。V=l×w×h。SA=2(lw+lh+wh)。')}</div>
<div style="flex:1; min-width:280px;">{fig_card('排水法標準示意（完全浸沒·水位上升）', svgs['displacement'], '🔴紅字標註水位變化。底面積×水位差=物體體積（不是底面積×新水位！）')}</div>
</div>
'''

# Apply inserts
# Insert 1: After KP1 口訣, before 知識點一 例題練習
m1 = '<div class="h2">知識點一 例題練習</div>'
html = html.replace(m1, insert1 + '\n' + m1, 1)

# Insert 2: After KP2 口訣, before 知識點二 例題練習
m2 = '<div class="h2">知識點二 例題練習</div>'
html = html.replace(m2, insert2 + '\n' + m2, 1)

# Insert 3: Before the tiered practice section
m3 = '<div class="h1">三、課堂分層同步練習</div>'
html = html.replace(m3, insert3 + '\n' + m3, 1)

# Write
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

svg_count = html.count('<svg')
print(f'L27 extended: {len(html)} chars, {svg_count} SVGs added')
