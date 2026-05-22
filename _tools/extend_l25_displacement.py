#!/usr/bin/env python3
"""Extend L25 with displacement + cuboid SVGs"""
import sys
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import displacement, cuboid

svgs = {
    'disp_main': displacement(160, 90, 28, 52, 42, 42),
    'disp_overflow': displacement(160, 90, 40, 62, 42, 42),
    'cuboid_tank': cuboid(130, 60, 70),
}

def fig_card(title, svg, note=''):
    note_html = f'<div style="font-size:9px; color:var(--gray); margin-top:3px;">{note}</div>' if note else ''
    return f'''<div style="text-align:center; margin:8px 0; padding:8px; background:#F0F9FF; border:1px solid var(--borderc); border-radius:5px;">
<strong style="font-size:13px; color:var(--blue);">{title}</strong><br>
{svg}
{note_html}
</div>'''

path = r'G:\lam-fung-academy\講義\P5\LF-P5-下-L25_體積應用題專項.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Insert 1: After KP1 intro (排水法基礎), before KP1 陷阱例題
insert1 = f'''
{fig_card('💧 排水法原理示意圖 — 阿基米德原理', svgs['disp_main'], '🔴重點：左=投入前（水位wb cm），右=投入後（水位wa cm）。體積=底面積×(wa−wb)。不是底面積×新水位！石頭必須完全浸沒。')}
'''

# Insert 2: After KP2 (溢出問題)
insert2 = f'''
{fig_card('📦 標準長方體容器參考圖', svgs['cuboid_tank'], '長(l)×闊(w)×高(h)。底面積=l×w。容量=l×w×h。剩餘空間=容量−原有水體積。溢出=投入體積−剩餘空間。')}
'''

# Insert 3: Before 分層練習
insert3 = f'''
{fig_card('💧 排水法進階：多物體與取出', svgs['disp_main'], '複習：①物體體積=底面積×水位差 ②新水位=原水位+體積÷底面積 ③取出物體→水位下降（下降=體積÷底面積）④多物體→總體積加總後計算')}
'''

# Apply
m1 = '<div class="ex"><div class="ex-title">🪤 陷阱引爆例題 — 體積 vs 水位高度</div>'
html = html.replace(m1, insert1 + '\n' + m1, 1)

m2 = '<div class="kp-title">知識點三：不規則物體體積'
html = html.replace(m2, insert2 + '\n<div class="kp-title">知識點三：不規則物體體積', 1)

m3 = '<div class="h1">三、課堂分層同步練習</div>'
html = html.replace(m3, insert3 + '\n' + m3, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'L25 extended: {len(html)} chars, {html.count(chr(60)+"svg")} SVGs')
