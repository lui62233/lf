#!/usr/bin/env python3
"""
Enhance existing P6 下學期 handouts:
1. Add missing SVGs (L21 circle, L22 composite circles, L26 pie, L27 multi-chart, L28 speed)
2. Apply v7 quality (answer spaces 80px+, print grid lines)
3. Add blank chart templates to L26-L27
"""
import sys, os, glob, re, subprocess
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import (circle_shape, line_chart, line_blank, pie_chart,
                          bar_simple, bar_composite, bar_blank, bar_composite_blank,
                          cuboid, displacement, composite_L, composite_T, composite_hole,
                          rectangle, triangle, grid_diagram)

P6 = r'G:\lam-fung-academy\講義\P6'

def fig_card(title, svg, note=''):
    n = f'<div style="font-size:9px;color:var(--gray);margin-top:3px;">{note}</div>' if note else ''
    return f'<div style="text-align:center;margin:8px 0;padding:8px;background:#F0F9FF;border:1px solid var(--borderc);border-radius:5px;"><strong style="font-size:13px;color:var(--blue);">{title}</strong><br>{svg}{n}</div>'

def enhance_file(filepath, diagrams):
    """Add diagram SVGs + apply v7 fixes to a handout."""
    if not os.path.exists(filepath):
        return 0
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    added = 0
    for marker, svg_key, label in diagrams:
        if marker in html and svg_key in DIAG:
            block = fig_card(label, DIAG[svg_key])
            html = html.replace(marker, block + '\n' + marker, 1)
            added += 1
    # v7 answer spaces
    for old, new in [('36px','75px'),('40px','75px'),('45px','75px'),('48px','80px'),
                     ('50px','80px'),('52px','80px'),('55px','85px'),('58px','88px'),
                     ('60px','90px'),('62px','90px'),('65px','95px')]:
        html = re.sub(f'min-height:{old}', f'min-height:{new}', html)
    if '.qt .qw { background: none; border: 1px dashed #D1D5DB; }' in html:
        html = html.replace('.qt .qw { background: none; border: 1px dashed #D1D5DB; }',
                           '.qt .qw { background: repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px); border: 1px dashed #9CA3AF; }')
    if added > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    return added

# Generate all needed diagrams
print('Generating diagrams...')
DIAG = {
    # Circles
    'circle_r5': circle_shape(55),
    'circle_r7': circle_shape(60),
    'circle_r10': circle_shape(65),
    'circle_compass': circle_shape(70),
    # Composite circles
    'circle_annulus': circle_shape(65),
    # Charts for L26-L28
    'pie_book': pie_chart({'中文書':120,'英文書':80,'數學書':60,'科普書':40}, '圖書館藏書佔比'),
    'pie_blank1': pie_chart({'故事書':35,'漫畫':25,'科普':20,'其他':20}, '圖書種類分佈示例'),
    'bar_compare': bar_composite([
        {'name':'1月','data':{'A店':300,'B店':280}},
        {'name':'2月','data':{'A店':450,'B店':500}},
        {'name':'3月','data':{'A店':520,'B店':480}},
        {'name':'4月','data':{'A店':380,'B店':420}}
    ], '兩店銷售對比', '銷售額', '元', ystep=100),
    'line_speed': line_chart(
        {'1h':40,'2h':55,'3h':70,'4h':65,'5h':85,'6h':90},
        '六小時速率變化', '速率', 'km/h', ystep=10
    ),
    'line_blank_speed': line_blank(
        ['1h','2h','3h','4h','5h','6h'],
        '請繪製速率變化折線圖', '速率', 'km/h', ymax=100, ystep=10
    ),
    'blank_bar': bar_blank(
        ['Q1','Q2','Q3','Q4'],
        '請繪製季度銷售棒形圖', '銷售額', '萬元', ymax=200, ystep=25
    ),
    'blank_comp_bar': bar_composite_blank(
        ['Q1','Q2','Q3','Q4'],
        ['A店','B店'],
        '請繪製複合棒形圖', '銷售額', '萬元', ymax=200, ystep=25
    ),
}
print(f'  {len(DIAG)} diagrams ready')

total = 0

# L21: Circle + compass + sector
total += enhance_file(os.path.join(P6, 'LF-P6-下-L21_圓的認識進階_圓規作圖扇形.html'), [
    ('圓規作圖', 'circle_compass', '圓規作圖：固定圓心·展開至半徑長度·旋轉畫圓'),
    ('扇形', 'circle_r5', '扇形=兩條半徑+一段弧。圓心角θ°的扇形面積=(θ/360)×πr²'),
])

# L22: Composite circles
total += enhance_file(os.path.join(P6, 'LF-P6-下-L22_圓面積進階應用_環形複合圓形.html'), [
    ('環形', 'circle_annulus', '環形(Annulus)=大圓−小圓。Area=πR²−πr²。R=外圓半徑·r=內圓半徑'),
    ('操場形狀', 'circle_r10', '操場=長方形+兩個半圓。周界=2×長+圓周。面積=長方形+圓形'),
])

# L26: Pie charts — CRITICAL: needs more pie SVGs + blank templates
total += enhance_file(os.path.join(P6, 'LF-P6-下-L26_圓形圖閱讀製作.html'), [
    ('圓形圖示例', 'pie_book', '每個扇形角度=該類別百分比×3.6°。全部扇形加起來=360°=100%。'),
    ('繪圖參考', 'pie_blank1', '繪製步驟：①計算每類百分比 ②%×3.6°=扇形角度 ③用量角器依次畫出 ④標註類別+%'),
])

# L27: Multi-chart — needs bar + line + pie variety
total += enhance_file(os.path.join(P6, 'LF-P6-下-L27_綜合統計圖表_棒形折線圓形.html'), [
    ('複合棒形圖', 'bar_compare', '棒形圖：比較不同類別數值。適合展示各月各店銷售對比。'),
    ('折線圖', 'line_speed', '折線圖：展示數據隨時間變化趨勢。適合展示速率/溫度/股價變化。'),
])

# L28: Speed — needs line charts
total += enhance_file(os.path.join(P6, 'LF-P6-下-L28_速率應用進階_多段行程相對速度.html'), [
    ('速率變化折線圖', 'line_speed', '多段行程：總距離÷總時間=平均速率（不是速率平均！）'),
    ('繪圖練習', 'line_blank_speed', '請根據題目數據在空白折線圖上標點並連線。'),
])

# Apply v7 to ALL P6 下 files
print(f'\nTotal SVG enhancements: {total}')
print('\nApplying v7 quality to all P6 下 files...')
all_p6x = glob.glob(os.path.join(P6, 'LF-P6-下-*.html'))
fixed = 0
for f in all_p6x:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    changed = False
    for old, new in [('36px','75px'),('40px','75px'),('45px','75px'),('48px','80px'),
                     ('50px','80px'),('52px','80px'),('55px','85px'),('58px','88px'),
                     ('60px','90px'),('62px','90px'),('65px','95px')]:
        if f'min-height:{old}' in html:
            html = html.replace(f'min-height:{old}', f'min-height:{new}')
            changed = True
    if '.qt .qw { background: none; border: 1px dashed #D1D5DB; }' in html:
        html = html.replace('.qt .qw { background: none; border: 1px dashed #D1D5DB; }',
                           '.qt .qw { background: repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px); border: 1px dashed #9CA3AF; }')
        changed = True
    if changed:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        fixed += 1

print(f'  {fixed}/{len(all_p6x)} files v7-upgraded')

# Print final SVG counts
print('\nFinal SVG counts:')
for f in sorted(all_p6x):
    s = open(f, encoding='utf-8').read().count('<svg')
    n = os.path.basename(f)[:50]
    print(f'  {n}: {s} SVGs')
