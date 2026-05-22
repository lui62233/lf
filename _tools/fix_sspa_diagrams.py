#!/usr/bin/env python3
"""
Add missing diagrams to ALL 7 SSPA mock exams across P5 and P6.
Each exam paper should mirror real SSPA format with proper diagrams.
"""
import sys, os, re, subprocess
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import (triangle, trapezoid, circle_shape, cuboid,
                          rectangle, square, composite_hole, displacement,
                          line_chart, pie_chart, bar_simple)

def svg_wrap(svg_str, max_w='280px'):
    """Wrap SVG in a centered container for exam paper layout."""
    return f'<div style="text-align:center;margin:8px 0;"><div style="display:inline-block;max-width:{max_w};">{svg_str}</div></div>'

def diagram(title, svg_str, max_w='280px'):
    """Create a labeled diagram for exam questions."""
    return f'''<div style="text-align:center;margin:8px 0;padding:6px;background:#FAFBFC;border:1px solid var(--borderc);border-radius:4px;">
<div style="font-size:10px;color:var(--gray);margin-bottom:4px;">{title}</div>
<div style="display:inline-block;max-width:{max_w};">{svg_str}</div>
</div>'''

# ═══════════════════════════════════════════════
# Generate all diagrams needed across exams
# ═══════════════════════════════════════════════
print('Generating all SSPA exam diagrams...')

DIAG = {
    # Triangles
    'tri_12x8': triangle(110, 80, 'right'),
    'tri_16x9': triangle(120, 85, 'right'),
    'tri_12x9': triangle(110, 80, 'right'),
    'tri_iso': triangle(110, 80, 'isosceles'),
    # Trapezoids
    'trap_5_9_4': trapezoid(60, 110, 60),
    'trap_8_12_6': trapezoid(60, 120, 70),
    'trap_7_13_6': trapezoid(55, 120, 70),
    'trap_6_14_8': trapezoid(50, 120, 75),
    # Circles
    'circle_r5': circle_shape(55),
    'circle_r7': circle_shape(60),
    'circle_r9': circle_shape(65),
    'circle_r14': circle_shape(70),
    'circle_d10': circle_shape(55),
    'circle_d16': circle_shape(65),
    'circle_d28': circle_shape(70),
    # Cuboids
    'cuboid_8x5x4': cuboid(120, 55, 65),
    'cuboid_generic': cuboid(130, 60, 70),
    # Rectangle
    'rect_8x5': rectangle(120, 65),
    'rect_12x5': rectangle(140, 60),
    'rect_18x12': rectangle(150, 80),
    # Composite
    'hole_8x5_3x3': composite_hole(120, 75, 36, 36),
    # Displacement
    'disp_basic': displacement(150, 85, 28, 52, 40, 40),
    'disp_overflow': displacement(150, 85, 40, 62, 40, 40),
    # Charts
    'line_rainfall': line_chart(
        {'一月':45,'二月':60,'三月':85,'四月':70,'五月':95,'六月':110},
        title='六個月降雨量', ylabel='降雨量', unit='mm', ystep=20
    ),
    'pie_90deg': pie_chart({'A':1,'B':1,'C':1,'D':1}, title='圓形圖示例：90°=1/4', radius=60),
}

print(f'  Generated {len(DIAG)} diagrams')

# ═══════════════════════════════════════════════
# Fix functions for each exam paper
# ═══════════════════════════════════════════════

def fix_exam(filepath, exam_name, diagrams_to_add):
    """Add diagrams to an exam paper at specified insertion points."""
    if not os.path.exists(filepath):
        print(f'  SKIP {exam_name}: file not found')
        return 0

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    added = 0
    for marker, svg_key, label in diagrams_to_add:
        if marker in html and svg_key in DIAG:
            svg_block = diagram(label, DIAG[svg_key])
            # Insert diagram BEFORE the question that references it
            html = html.replace(marker, svg_block + '\n' + marker, 1)
            added += 1

    # Also fix answer space min-heights for exam format
    for old, new in [('min-height:32px','min-height:48px'),('min-height:36px','min-height:52px'),
                     ('min-height:40px','min-height:55px'),('min-height:45px','min-height:60px')]:
        if old in html:
            html = html.replace(old, new)

    if added > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    print(f'  {exam_name}: +{added} diagrams, total {html.count(chr(60)+"svg")} SVGs')
    return added


# ═══════════════════════════════════════════════
# P5 SSPA Exams
# ═══════════════════════════════════════════════

P5 = r'G:\lam-fung-academy\講義\P5'
P6 = r'G:\lam-fung-academy\講義\P6'

total = 0

# P5 L11 — SSPA模擬1
total += fix_exam(
    os.path.join(P5, 'LF-P5-上-L11-SSPA模擬1.html'),
    'P5-L11 SSPA1',
    [
        ('三角形底長 12 cm，高 8 cm。面積', 'tri_12x8', '▲ 三角形：底12cm·高8cm'),
        ('梯形：上底 5 cm，下底 9 cm，斜邊 7 cm，高 4 cm', 'trap_5_9_4', '▲ 梯形：注意高≠斜邊！'),
        ('平行四邊形底長 2 m，高 50 cm', 'tri_iso', '▲ 平行四邊形：底2m·高50cm（注意單位！）'),
        ('中間挖走一個邊長 3 cm 的正方形', 'hole_8x5_3x3', '▲ 長方形8×5cm·挖走3×3cm正方形'),
    ]
)

# P5 L19 — SSPA模擬2
total += fix_exam(
    os.path.join(P5, 'LF-P5-上-L19-SSPA模擬2.html'),
    'P5-L19 SSPA2',
    [
        ('梯形：上底 8 cm，下底 12 cm，斜邊 10 cm，高 6 cm', 'trap_8_12_6', '▲ 梯形：斜邊10cm（求面積不需要！）'),
        ('下圖由一個長方形（長 12 cm，闊 5 cm）和一個三角形', 'rect_12x5', '▲ 長方形12×5cm + 三角形（底12cm·高4cm）'),
        ('長方形面積 = 6 m²。以 cm² 表示', 'rect_8x5', '▲ 長方形（面積單位換算參考）'),
    ]
)

# P5 L29 — SSPA模擬3
total += fix_exam(
    os.path.join(P5, 'LF-P5-下-L29_SSPA模擬3.html'),
    'P5-L29 SSPA3',
    [
        ('一個圓的半徑是 9 cm。直徑是多少？', 'circle_r9', '▲ 圓：半徑9cm'),
        ('長方體長 8 cm、闊 5 cm、高 4 cm。體積', 'cuboid_8x5x4', '▲ 長方體：8×5×4cm'),
    ]
)

# P5 L37 — SSPA模擬4
total += fix_exam(
    os.path.join(P5, 'LF-P5-T2-L37-SSPA模擬4.html'),
    'P5-L37 SSPA4',
    [
        ('三角形底長 16 cm，高 9 cm。面積', 'tri_16x9', '▲ 三角形：底16cm·高9cm'),
        ('梯形：上底 7 cm，下底 13 cm，斜邊 11 cm，高 6 cm', 'trap_7_13_6', '▲ 梯形：斜邊11cm（陷阱！求面積不需要斜邊）'),
        ('平行四邊形底長 2 m，高 80 cm。面積', 'tri_iso', '▲ 平行四邊形：底2m·高80cm（陷阱！單位不一致）'),
        ('一個圓形花圃，半徑 = 7 m。圓周大約是多少？', 'circle_r7', '▲ 圓形花圃：半徑7m'),
    ]
)

# ═══════════════════════════════════════════════
# P6 SSPA Exams
# ═══════════════════════════════════════════════

# P6 L07 — SSPA模擬1
total += fix_exam(
    os.path.join(P6, '學生版講義_P6_上_L07_SSPA模擬1_v6.html'),
    'P6-L07 SSPA1',
    [
        ('一個圓的半徑是 5 cm，圓周是多少？', 'circle_r5', '▲ 圓：半徑5cm（C=2πr）'),
        ('一個圓的直徑是 10 cm，圓面積是多少？', 'circle_d10', '▲ 圓：直徑10cm（r=5·A=πr²）'),
        ('一個半圓，半徑 = 6 cm。半圓周長', 'circle_r5', '▲ 半圓：r=6cm（周界=πr+2r！）'),
        ('圓扇形，r = 4 cm。扇形周長', 'circle_r5', '▲ 1/4圓扇形：r=4cm'),
        ('一個圓的半徑 = 7 cm。求 (a) 圓周 (b) 圓面積', 'circle_r7', '▲ 圓：半徑7cm（π=22/7）'),
        ('一個半圓的直徑是 20 cm。求它的周長', 'circle_d10', '▲ 半圓：直徑20cm·r=10cm'),
        ('一個圓形噴水池的直徑是 14 m', 'circle_r14', '▲ 圓形噴水池：直徑14m + 環形小徑闊1m'),
    ]
)

# P6 L13 — SSPA模擬2
total += fix_exam(
    os.path.join(P6, 'LF-P6-上-L13_SSPA模擬2.html'),
    'P6-L13 SSPA2',
    [
        ('圓形半徑 5 cm，面積', 'circle_r5', '▲ 圓：半徑5cm'),
        ('三角形底 12 cm，高 9 cm。面積', 'tri_12x9', '▲ 三角形：底12cm·高9cm'),
        ('梯形上底 8 cm，下底 14 cm，面積 88 cm²。高是多少？', 'trap_8_12_6', '▲ 梯形：上底8·下底14·面積88（逆向求高）'),
        ('圓形直徑 16 cm。（a）求周界。（b）求面積', 'circle_d16', '▲ 圓：直徑16cm·r=8cm'),
        ('梯形上底 6 cm，下底 14 cm，高 8 cm。求面積', 'trap_6_14_8', '▲ 梯形：上底6·下底14·高8'),
        ('一個圓形操場，直徑 28 m', 'circle_d28', '▲ 圓形操場：直徑28m（π=22/7）'),
    ]
)

# P6 L19 — SSPA模擬3 (most complex — has charts + geometry + displacement)
total += fix_exam(
    os.path.join(P6, 'LF-P6-上-L19_SSPA模擬3.html'),
    'P6-L19 SSPA3',
    [
        ('圓的半徑是 7 cm。面積是多少？', 'circle_r7', '▲ 圓：半徑7cm（π≈22/7）'),
        ('長方體水箱底面積 400 cm²，放入石頭後水面由 15 cm 升至 18 cm', 'disp_basic', '▲ 排水法：水位15→18cm·底面積400cm²'),
        ('圓形圖中一個扇形為 90°，佔全體的？', 'pie_90deg', '▲ 圓形圖：90°扇形=1/4圓'),
        ('圓的半徑是 14 cm。求 (a) 圓周長 (b) 圓面積', 'circle_r14', '▲ 圓：半徑14cm（π≈22/7）'),
        ('水箱底面積 500 cm²，原有水深 12 cm。放入一塊 3000 cm³ 的石頭', 'disp_overflow', '▲ 排水法+溢出：水箱高25cm·原水深12cm'),
        ('以下折線圖顯示某城市 6 個月的降雨量', 'line_rainfall', '▲ 六個月降雨量折線圖：45,60,85,70,95,110mm'),
        ('一個長方形，長增加 20%，闊減少 20%', 'rect_18x12', '▲ 長方形：原面積 vs 變化後面積'),
    ]
)

print(f'\n=== TOTAL: {total} diagrams added across 7 SSPA exams ===')

# ═══════════════════════════════════════════════
# Rebuild all 7 PDFs
# ═══════════════════════════════════════════════
print('\nRebuilding all SSPA PDFs...')
import pymupdf

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
exams = [
    os.path.join(P5, 'LF-P5-上-L11-SSPA模擬1.html'),
    os.path.join(P5, 'LF-P5-上-L19-SSPA模擬2.html'),
    os.path.join(P5, 'LF-P5-下-L29_SSPA模擬3.html'),
    os.path.join(P5, 'LF-P5-T2-L37-SSPA模擬4.html'),
    os.path.join(P6, '學生版講義_P6_上_L07_SSPA模擬1_v6.html'),
    os.path.join(P6, 'LF-P6-上-L13_SSPA模擬2.html'),
    os.path.join(P6, 'LF-P6-上-L19_SSPA模擬3.html'),
]

for f in exams:
    if os.path.exists(f):
        pdf = f.replace('.html', '.pdf')
        r = subprocess.run([edge, '--headless', '--disable-gpu', f'--print-to-pdf={pdf}', f'file:///{f}'],
                          capture_output=True, timeout=90)
        doc = pymupdf.open(pdf)
        svgs = open(f, encoding='utf-8').read().count('<svg')
        name = os.path.basename(f)[:45]
        print(f'  {name}: {len(doc)}p, {svgs} SVGs, {os.path.getsize(pdf)}b')
        doc.close()

print('\n=== ALL SSPA EXAMS UPDATED ===')
