#!/usr/bin/env python3
"""Add circle SVGs to P6 L06"""
import sys
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import circle_shape

def fig_card(title, svg, note=''):
    note_html = f'<div style="font-size:9px; color:var(--gray); margin-top:3px;">{note}</div>' if note else ''
    return f'''<div style="text-align:center; margin:8px 0; padding:8px; background:#F0F9FF; border:1px solid var(--borderc); border-radius:5px;">
<strong style="font-size:13px; color:var(--blue);">{title}</strong><br>
{svg}
{note_html}
</div>'''

path = r'G:\lam-fung-academy\講義\P6\學生版講義_P6_上_L06_圓周與圓面積_v6.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

svgs = {
    'circle1': circle_shape(75),
    'circle2': circle_shape(55),
}

insert = f'''
{fig_card('Circle Structure: centre(O), radius(r), diameter(d=2r)', svgs['circle1'], 'Red dashed = diameter. C=2(pi)r=(pi)d. A=(pi)r^2. (pi) ~ 3.14 or 22/7.')}

<div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin:10px 0;">
<div style="flex:1; min-width:200px;">{fig_card('Half Circle: Perimeter = r + half-arc = r + (pi)r', svgs['circle2'], 'Half circle area = (pi)r^2 / 2. Perimeter INCLUDES the diameter -- DO NOT forget +2r!')}</div>
<div style="flex:1; min-width:200px;">
<div style="background:#FEF2F2; border:2px solid #FECACA; border-radius:6px; padding:10px; text-align:center;">
<strong style="color:#DC2626;">⚠️ Most Common Trap</strong>
<p style="font-size:12px; margin:4px 0;">Half-circle perimeter = <strong>(pi)r + 2r</strong> (NOT just (pi)r!)<br>Forgetting the diameter = -2 marks</p>
</div>
</div>
</div>
'''

# Find first KP section
first_kp = html.find('<div class="kp">')
if first_kp > 0:
    html = html[:first_kp] + insert + '\n' + html[first_kp:]
    print('Inserted circle diagrams before first KP')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

svg_count = html.count('<svg')
print(f'P6 L06: {svg_count} SVGs total (was 2)')
