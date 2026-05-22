#!/usr/bin/env python3
"""Extend L32 with chart SVGs — bar, line, pie, blank templates"""
import sys, re
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
from svg_geometry import bar_simple, bar_composite, bar_blank, bar_composite_blank, line_chart, line_blank, pie_chart

# Generate all chart SVGs
charts = {}

# Simple bar chart for example
charts['bar_scores'] = bar_simple(
    {'紅隊':18,'藍隊':24,'綠隊':14,'黃隊':20},
    title='比賽得分', ylabel='得分', unit='分', ystep=4, bar_w=44
)

# Books bar chart
charts['bar_books'] = bar_simple(
    {'一月':120,'二月':95,'三月':150,'四月':135},
    title='四個月借書數量', ylabel='借書量', unit='本', ystep=25
)

# Composite bar — class activities
charts['bar_activities'] = bar_composite([
    {'name':'5A班','data':{'足球':12,'籃球':8,'游泳':15,'跑步':10}},
    {'name':'5B班','data':{'足球':10,'籃球':14,'游泳':9,'跑步':11}}
], title='兩班課外活動人數', ylabel='人數', unit='人', ystep=5)

# Blank bar chart for student drawing
charts['bar_blank_draw'] = bar_blank(
    ['一月','二月','三月','四月'],
    title='請根據數據繪製棒形圖', ylabel='銷售量', unit='件', ymax=200, ystep=25
)

# Blank composite bar for student drawing
charts['blank_comp'] = bar_composite_blank(
    ['足球','籃球','游泳','跑步'],
    ['5A班','5B班'],
    title='請根據數據表繪製複合棒形圖', ylabel='人數', unit='人', ymax=20, ystep=5
)

# Line chart
charts['line_sales'] = line_chart(
    {'一月':100,'二月':120,'三月':150,'四月':130},
    title='A店筆記本銷量走勢', ylabel='銷量', unit='件', ystep=25
)

# Blank line chart
charts['line_blank_draw'] = line_blank(
    ['一月','二月','三月','四月'],
    title='請根據數據繪製折線圖', ylabel='銷量', unit='件', ymax=200, ystep=25
)

# Pie chart
charts['pie_stationery'] = pie_chart(
    {'筆記本':450,'文件夾':380,'鉛筆':220,'橡皮':150},
    title='文具銷售佔比'
)

# Blank bar chart simple
charts['bar_blank_simple'] = bar_blank(
    ['可樂','橙汁','檸檬茶'],
    title='請繪製飲品銷量棒形圖', ylabel='銷量', unit='箱', ymax=300, ystep=50
)

# Composite sales chart
charts['bar_sales2'] = bar_composite([
    {'name':'A店','data':{'一月':300,'二月':450,'三月':520,'四月':380}},
    {'name':'B店','data':{'一月':280,'二月':500,'三月':480,'四月':420}}
], title='兩店四個月銷售總額', ylabel='銷售額', unit='元', ystep=100)

# Blank bar for Q34
charts['bar_blank_34'] = bar_composite_blank(
    ['故事書','科普書','漫畫'],
    ['5A班','5B班'],
    title='請根據Q34數據繪製複合棒形圖', ylabel='圖書數量', unit='本', ymax=60, ystep=10
)

# Museum composite for 🌳 level
charts['bar_museum_blank'] = bar_composite_blank(
    ['一月','二月','三月','四月'],
    ['成人','學生','長者'],
    title='請根據🌳1數據繪製博物館入場複合棒形圖', ylabel='入場人數', unit='人', ymax=500, ystep=100
)

# Line chart for Q35
charts['line_blank_35'] = line_blank(
    ['一月','二月','三月','四月'],
    title='請根據Q35數據繪製集團總銷量折線圖', ylabel='銷量', unit='件', ymax=600, ystep=100
)

# Pie chart for Q36
charts['pie_blank_36'] = pie_chart(
    {'筆記本':500,'文件夾':390},
    title='A店商品銷量佔比（參考）'
)

# Read original L32
orig_path = r'G:\lam-fung-academy\講義\P5\LF-P5-下-L32_複合棒形圖+數據分析.html'
with open(orig_path, 'r', encoding='utf-8') as f:
    html = f.read()

def chart_section(title_text, svg_key, note=''):
    """Wrap a chart SVG in a nice HTML section."""
    note_html = f'<div style="font-size:10px; color:var(--gray); margin-top:4px;">▲ {note}</div>' if note else ''
    return f'''<div style="text-align:center; margin:12px 0; padding:10px; background:#FFFBEB; border:1px solid var(--borderc); border-radius:5px;">
<strong style="font-size:14px; color:var(--blue);">{title_text}</strong>
{charts[svg_key]}
{note_html}
</div>'''

# ═══════════ INSERTION 1: After the composite bar chart (after the closing </div> of the chart container)
# Add a simple bar chart example + line chart comparison
insert1 = f'''
{chart_section('📊 簡單棒形圖示例：比賽得分', 'bar_scores', '每格代表2分。紅隊18分=9格，藍隊24分=12格。注意：軸標籤要清楚、刻度要均勻。')}

<div class="ex">
<div class="ex-title">💡 棒形圖 vs 折線圖 — 何時用哪種？</div>
<div class="ex-q">棒形圖用來比較不同類別的數量；折線圖用來顯示同一數據隨時間的變化趨勢。以下同一組數據的兩種表示：</div>
<div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin:10px 0;">
<div style="flex:1; min-width:280px;">{charts['bar_books']}</div>
<div style="flex:1; min-width:280px;">{charts['line_sales']}</div>
</div>
<div style="font-size:10px; color:var(--gray); margin-top:4px;">▲ 左：棒形圖（強調各月數值比較）| 右：折線圖（強調上升/下降趨勢）— 注意兩者使用場景不同！</div>
</div>
'''

# ═══════════ INSERTION 2: After KP3 (knowledge point 3 about making charts)
# Add blank chart templates for student practice
insert2 = f'''
<div class="h1" style="margin-top:12px;">📐 繪圖實戰區 — 從數據到圖表</div>

{chart_section('🖊️ 練習一：根據下表繪製簡單棒形圖', 'bar_blank_draw', '數據：一月100件、二月120件、三月150件、四月130件。每格代表25件，請在虛線框內畫出棒形。')}

{chart_section('🖊️ 練習二：根據下表繪製複合棒形圖', 'blank_comp', '數據請參考上方「兩班課外活動人數」複合棒形圖。注意：先畫5A班（藍色），再畫5B班（橙色），每組兩條棒並排。')}
'''

# ═══════════ INSERTION 3: Before the 終極挑戰 section, add a comprehensive drawing practice zone
insert3 = f'''
<div class="h1">📐 綜合繪圖練習 — 三種圖表全覆蓋</div>
<div class="kp"><div class="kp-title">呈分試必備：能讀圖，更要能畫圖！</div><div class="kp-rules">
SSPA 卷一常見題型：給你一個數據表，要求你 (a) 繪製棒形圖 (b) 繪製折線圖 (c) 回答數據問題。<br>
以下三題提供了空白圖表模板，請根據題目數據完成繪製。
</div></div>

<table class="qt">
<tr><th class="qn">繪1</th><th>題目</th><th class="qd">圖表</th></tr>
<tr><td class="qn">📊</td><td class="qtxt">超級市場統計了三種飲品的月銷量（箱）：可樂 240 箱、橙汁 180 箱、檸檬茶 210 箱。請在下方空白棒形圖中畫出棒形。</td><td class="qd">{charts['bar_blank_simple']}</td></tr>
<tr><td class="qn">📊</td><td class="qtxt">下表是兩班捐贈圖書數量，請在下方空白複合棒形圖中畫出。<br><table class="dt"><tr><th></th><th>故事書</th><th>科普書</th><th>漫畫</th></tr><tr><td>5A(本)</td><td>40</td><td>30</td><td>50</td></tr><tr><td>5B(本)</td><td>35</td><td>45</td><td>25</td></tr></table></td><td class="qd">{charts['bar_blank_34']}</td></tr>
<tr><td class="qn">📈</td><td class="qtxt">根據複合棒形圖數據，計算 A店+B店 合併後一至四月的每月集團總銷量，然後在下方折線圖中標出數據點並連線。</td><td class="qd">{charts['line_blank_35']}</td></tr>
</table>

<div style="text-align:center; margin:12px 0;">
<strong style="font-size:14px; color:var(--blue);">📊 圓形圖（餅圖）示例 — 文具銷售佔比</strong>
{charts['pie_stationery']}
<div style="font-size:10px; color:var(--gray); margin-top:4px;">▲ 圓形圖用來表示「部分佔整體的幾分之幾」。扇形愈大 = 佔比愈高。</div>
</div>

{chart_section('🏔️ 博物館入場複合棒形圖（🌳1 配套模板）', 'bar_museum_blank', '三種花紋（成人/學生/長者）× 四個月。先用鉛筆畫草稿，確認高度正確後再上色。')}
'''

# Now insert them at the right places
# Insert 1: After the main composite bar chart (after "本堂主要參考圖表" note div close)
marker1 = '本堂主要參考圖表，大部分例題和練習題均以此圖數據為基礎</div>\n  </div>'
html = html.replace(marker1, marker1 + '\n' + insert1)

# Insert 2: After KP3 同步練習 table close (Q18), before the closing </div> of page 3
marker2 = '<td class="qn">18</td><td class="qtxt">根據複合棒形圖中的數據，自行繪製一個簡單的數據表'
# Find the closing of Q18's table row and insert after the table
# Insert after Q18 row (last row in KP3 practice)
marker2b = '</table>\n</div>\n\n<!-- ═══════════════ PAGE 4: KP4 + TIERED PRACTICE ═══════════════ -->'
html = html.replace(marker2b, '</table>\n' + insert2 + '\n</div>\n\n<!-- ═══════════════ PAGE 4: KP4 + TIERED PRACTICE ═══════════════ -->')

# Insert 3: Before the 終極挑戰 section
marker3 = '<!-- ═══════════════ PAGE 6: ERROR SUMMARY ═══════════════ -->'
html = html.replace(marker3, insert3 + '\n' + marker3)

# Write the extended version
out_path = r'G:\lam-fung-academy\講義\P5\LF-P5-下-L32_複合棒形圖+數據分析_v2.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Also overwrite original
with open(orig_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Extended L32: {len(html)} chars (was {len(html) - sum(len(v) for v in charts.values())} before charts)')
print(f'Added {len(charts)} chart SVGs')
# Count total SVGs
svg_count = html.count('<svg')
print(f'Total SVGs in file: {svg_count}')
