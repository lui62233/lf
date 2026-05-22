#!/usr/bin/env python3
"""
霖楓學苑 · LF Academy — Trap Routing Engine v1.0
The bridge from "static library" to "diagnostic engine."
Input: Student's weak trap types (T1-T10 scores)
Output: Personalized lesson sequence with specific questions to prioritize
"""
import os, glob, re, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'G:\lam-fung-academy\講義'

# T1-T10 keywords that appear in handout filenames/content
TRAP_KEYWORDS = {
    'T1': ['單位', '進位', '位值', '多位數', '長度', '重量', '容量', '測量', 'cm²', 'm²', 'km', 'm³', 'cm³', 'L', 'mL', '換算'],
    'T2': ['小數', '小數點', '近似值', '四捨五入', '十分位', '百分位', '0.1', '0.01'],
    'T3': ['運算次序', '四則', '混合', '括號', '先乘除', '運算序'],
    'T4': ['面積', '平行四邊形', '三角形面積', '梯形面積', '周界', '公式混淆', '底乘高'],
    'T5': ['幾何', '圖形', '立體', '對稱', '截面', '摺紙', '柱體', '錐體', '面棱', '頂點'],
    'T6': ['分數', '通分', '約分', '擴分', '真分數', '假分數', '帶分數', '異分母', '同分母', '分數除法', '分數乘法'],
    'T7': ['百分數', '折扣', '利潤', '虧損', '佔比', '原值', '增減', '%', '折上折'],
    'T8': ['速率', '速度', '平均速率', '多段行程', '相對速度', '相遇', '追及', 'km/h'],
    'T9': ['方程', '代數', '未知數', '等式', '不等式', 'x=', '化簡', '同類項'],
    'T10': ['統計', '圖表', '棒形', '折線', '圓形圖', '數據', '平均數', '可能性', '概率', '趨勢'],
}

# Map trap types to recommended lesson numbers per grade
# (grade, lesson_range) -> primary trap
TRAP_LESSONS = {
    ('P3', 'T1'): list(range(13, 18)) + [31],  # L13-L17 measurement + L31 capacity
    ('P3', 'T2'): [27],  # L27 小數初探
    ('P3', 'T3'): [4, 24],  # L04 加減混合, L24 四則混合
    ('P3', 'T4'): [],  # P3 has limited area content
    ('P3', 'T5'): [18, 34, 37],  # L18 立體認識, L34 立體進階, L37 對稱
    ('P3', 'T6'): [11, 12, 25, 26],  # L11-L12 分數初探, L25-L26 分數進階
    ('P3', 'T7'): [],  # P3 has no percentage
    ('P3', 'T8'): [16, 17, 32, 33],  # L16-L17 時間, L32-L33 時間進階
    ('P3', 'T9'): [],  # P3 has no equations
    ('P3', 'T10'): [28, 29, 30, 38],  # L28-L30 棒形圖, L38 可能性

    ('P4', 'T1'): [1, 13, 14, 15, 26, 27, 28, 29],  # 多位數 + 測量
    ('P4', 'T2'): [26, 27, 28, 29],  # L26-L29 小數
    ('P4', 'T3'): [4, 5, 33],  # L04-L05 四則, L33 四則進階
    ('P4', 'T4'): [11, 12, 13, 14, 35],  # L11-L14 面積周界, L35 綜合
    ('P4', 'T5'): [15, 30, 31, 36],  # L15 方向, L30-L31 對稱, L36 路線
    ('P4', 'T6'): [8, 9, 10, 21, 22, 23, 24, 25],  # L08-L10 + L21-L25 分數
    ('P4', 'T7'): [],  # P4 minimal percentage
    ('P4', 'T8'): [15, 36],  # L15 方向速率, L36 路線
    ('P4', 'T9'): [],  # P4 minimal equations
    ('P4', 'T10'): [16, 17, 34],  # L16-L17 棒形圖, L34 概率

    ('P5', 'T1'): [1, 2, 6, 25, 26, 27],  # 多位數 + 體積
    ('P5', 'T2'): [12, 13],  # 小數乘法 + 近似值
    ('P5', 'T3'): [16, 30],  # 綜合 + 混合運算
    ('P5', 'T4'): [3, 4, 5, 6, 36],  # 面積系列
    ('P5', 'T5'): [3, 4, 5, 21, 25, 26, 27, 36],  # 幾何系列
    ('P5', 'T6'): [7, 9, 10, 22, 23, 24],  # 分數系列
    ('P5', 'T7'): [],  # P5 limited percentage
    ('P5', 'T8'): [],  # P5 limited speed
    ('P5', 'T9'): [14, 15, 31, 33],  # 代數 + 方程
    ('P5', 'T10'): [32, 33],  # 統計圖表

    ('P6', 'T1'): [16, 29],  # 體積 + 排水法
    ('P6', 'T2'): [1, 2, 3],  # 小數除法 + 互換
    ('P6', 'T3'): [3, 10],  # 綜合應用
    ('P6', 'T4'): [6, 21, 22],  # 圓面積系列
    ('P6', 'T5'): [6, 21, 22, 29, 37],  # 圓 + 立體
    ('P6', 'T6'): [2, 3],  # 分數互換
    ('P6', 'T7'): [4, 5, 23],  # 百分數系列
    ('P6', 'T8'): [8, 9, 14, 28],  # 速率系列
    ('P6', 'T9'): [24, 25, 35],  # 方程系列
    ('P6', 'T10'): [15, 17, 26, 27],  # 統計圖表系列
}

def generate_route(grade, weak_traps, strong_traps):
    """Generate personalized lesson sequence for a student."""
    routes = []
    priority_lessons = set()

    # Weak traps get priority
    for trap in weak_traps:
        lessons = TRAP_LESSONS.get((grade, trap), [])
        for l in lessons:
            priority_lessons.add((l, '🔴', trap))

    # Strong traps get maintenance
    for trap in strong_traps:
        lessons = TRAP_LESSONS.get((grade, trap), [])
        for l in lessons[:2]:  # Only 2 maintenance lessons per strong trap
            if (l, '🔴', trap) not in priority_lessons:
                priority_lessons.add((l, '🟢', trap))

    # Sort by lesson number
    sorted_lessons = sorted(priority_lessons, key=lambda x: x[0])

    # Generate 4-week plan
    weeks = {1: [], 2: [], 3: [], 4: []}
    for i, (lesson, priority, trap) in enumerate(sorted_lessons):
        week = (i % 4) + 1
        weeks[week].append((lesson, priority, trap))

    return weeks

# ═══════════════════════════════════════════════
# Build routing engine HTML report
# ═══════════════════════════════════════════════

def build_routing_report(grade, weak_traps, strong_traps):
    weeks = generate_route(grade, weak_traps, strong_traps)

    grade_name = {'P3':'小三','P4':'小四','P5':'小五','P6':'小六'}.get(grade, grade)

    html = f'''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<title>LF Academy · Trap Routing Report — {grade} {grade_name}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;700;900&display=swap');
body{{font-family:'Noto Sans HK',sans-serif;max-width:900px;margin:0 auto;padding:20px;color:#1A1A1A;font-size:13px;line-height:1.7;}}
.header{{background:linear-gradient(135deg,#1A3C6D,#1E4D8C);color:white;padding:24px 32px;border-radius:12px;margin-bottom:20px;}}
.header h1{{font-size:22px;margin:0;}}.header .sub{{color:#C9A84C;font-size:13px;margin-top:6px;}}
.diagnosis{{display:flex;gap:16px;margin:16px 0;flex-wrap:wrap;}}
.trap-card{{flex:1;min-width:140px;padding:14px;border-radius:8px;text-align:center;}}
.trap-weak{{background:#FEF2F2;border:2px solid #FECACA;}}
.trap-strong{{background:#F0FDF4;border:2px solid #BBF7D0;}}
.trap-card .code{{font-size:20px;font-weight:900;}}
.trap-card .name{{font-size:11px;color:#6B7280;margin-top:4px;}}
.week{{margin:20px 0;padding:16px;border-radius:8px;border:1px solid #D1D5DB;}}
.week h2{{color:#1A3C6D;margin:0 0 12px;font-size:16px;border-bottom:2px solid #C9A84C;padding-bottom:6px;}}
.lesson{{display:flex;align-items:center;gap:10px;padding:8px 12px;margin:4px 0;border-radius:6px;background:#FAFBFC;}}
.lesson .num{{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:12px;flex-shrink:0;}}
.priority-high{{background:#DC2626;color:white;}}
.priority-maint{{background:#16A34A;color:white;}}
.lesson .info{{flex:1;}}.lesson .trap-tag{{font-size:10px;padding:2px 6px;border-radius:3px;font-weight:700;}}
.tag-weak{{background:#FEE2E2;color:#991B1B;}}.tag-strong{{background:#DCFCE7;color:#166534;}}
.footer{{margin-top:30px;padding-top:14px;border-top:1px solid #D1D5DB;text-align:center;font-size:10px;color:#6B7280;}}
@media print{{body{{font-size:10px;}}}}
</style>
</head>
<body>
<div class="header">
<h1>霖楓學苑 · LF Academy</h1>
<div class="sub">Trap Routing Engine v1.0 — 個人化學習路徑 · {grade} {grade_name}</div>
</div>

<h2>陷阱敏感度診斷</h2>
<div class="diagnosis">
'''
    for trap in ['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10']:
        if trap in weak_traps:
            html += f'<div class="trap-card trap-weak"><div class="code">🔴 {trap}</div><div class="name">弱項·優先補底</div></div>'
        elif trap in strong_traps:
            html += f'<div class="trap-card trap-strong"><div class="code">🟢 {trap}</div><div class="name">強項·保持練習</div></div>'

    html += '</div>\n'

    for week_num in [1, 2, 3, 4]:
        lessons = weeks[week_num]
        if not lessons:
            continue
        html += f'<div class="week"><h2>第 {week_num} 週 — {"🔴 重點補底" if week_num <= 2 else "🟡 鞏固擴展"}</h2>'
        for lesson, priority, trap in lessons:
            pri_class = 'priority-high' if priority == '🔴' else 'priority-maint'
            tag_class = 'tag-weak' if priority == '🔴' else 'tag-strong'
            html += f'''<div class="lesson">
<div class="num {pri_class}">{lesson}</div>
<div class="info">LF-{grade} 第 {lesson} 堂 <span class="trap-tag {tag_class}">{trap}</span></div>
<div style="font-size:10px;color:#6B7280;">{"🎯 重點練習" if priority == "🔴" else "📝 保持練習"}</div>
</div>'''
        html += '</div>\n'

    html += f'''
<div class="footer">
霖楓學苑 · LF Academy · Trap Routing Engine v1.0<br>
基於 {grade} {grade_name} T1-T10 陷阱診斷結果自動生成<br>
建議每週 3-5 堂 · 每堂專注 1 個陷阱類型 · 4 週後重新診斷
</div>
</body>
</html>'''
    return html

# ═══════════════════════════════════════════════
# Generate sample routing reports for all grades
# ═══════════════════════════════════════════════
OUTPUT = r'G:\lam-fung-academy\_operations'

# Sample student profiles (weak traps, strong traps)
samples = {
    'P3': (['T1','T3','T6'], ['T5','T10']),
    'P4': (['T4','T6','T7'], ['T1','T2','T3']),
    'P5': (['T4','T5','T9'], ['T1','T2','T6']),
    'P6': (['T7','T8','T10'], ['T1','T3','T6']),
}

for grade, (weak, strong) in samples.items():
    html = build_routing_report(grade, weak, strong)
    path = os.path.join(OUTPUT, f'routing_report_{grade}_sample.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{grade}: routing report -> {path}')

# Also build a master routing engine Python module
engine_path = os.path.join(OUTPUT, 'trap_routing_engine.py')
with open(engine_path, 'w', encoding='utf-8') as f:
    f.write(open(__file__, encoding='utf-8').read())

print(f'\nRouting Engine:')
print(f'  4 sample reports generated')
print(f'  Engine module: trap_routing_engine.py')
print(f'  TRAP_LESSONS dictionary: {sum(len(v) for v in TRAP_LESSONS.values())} lesson mappings across 4 grades × 10 traps')
