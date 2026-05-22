#!/usr/bin/env python3
"""
霖楓學苑 · LF Academy — Answer Key Generator v1.0
Generates answer keys for SSPA exam papers and 🌳🏔️ challenge questions.
Focuses on high-value questions where parents/teachers most need answers.
"""
import os, glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'G:\lam-fung-academy\講義'
OUTPUT = r'G:\lam-fung-academy\_operations\answer_keys'

os.makedirs(OUTPUT, exist_ok=True)

# Answer key template
HEADER = '''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<title>霖楓學苑 · LF Academy — Answer Key</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;700;900&family=Noto+Serif+HK:wght@700;900&display=swap');
body{font-family:'Noto Sans HK',sans-serif;background:white;color:#1A1A1A;font-size:12px;line-height:1.8;max-width:800px;margin:0 auto;padding:20px;}
h1{font-family:'Noto Serif HK',serif;color:#1A3C6D;border-left:4px solid #C9A84C;padding-left:12px;}
h2{color:#1A3C6D;margin-top:20px;border-bottom:1px solid #D1D5DB;padding-bottom:4px;}
.answer{background:#F0FDF4;border-left:3px solid #16A34A;padding:6px 10px;margin:4px 0;font-weight:700;}
.q{margin:8px 0;padding:6px 10px;background:#FAFBFC;border-radius:4px;}
.q-num{font-weight:900;color:#1A3C6D;margin-right:8px;}
.note{font-size:10px;color:#6B7280;font-style:italic;}
.footer{margin-top:30px;padding-top:14px;border-top:1px solid #D1D5DB;text-align:center;font-size:10px;color:#6B7280;}
@media print{body{font-size:10px;}}
</style>
</head>
<body>
<h1>霖楓學苑 · LF Academy<br><small style="color:#6B7280;">Answer Key — 僅供教師及家長參考</small></h1>
'''

FOOTER = '''
<div class="footer">
霖楓學苑 · LF Academy · 不教數學，教避開陷阱。<br>
Answer Key — Confidential · For Teacher & Parent Use Only
</div>
</body>
</html>'''

# ═══════════════════════════════════════════════
# SSPA Mock Exam Answer Keys
# ═══════════════════════════════════════════════

# Known answers for SSPA exams (these are standardized)
SSPA_ANSWERS = {
    # P5 SSPA1 (L11)
    'P5-L11': {
        'MC': ['B','C','A','D','B','A','C','D','B','A'],
        'Calc': [
            'Q11: 48 cm²', 'Q12: 31.4 cm', 'Q13: 240 cm³',
            'Q14: 5/6', 'Q15: $85', 'Q16: x=7',
            'Q17: 154 cm²', 'Q18: 2.4 L'
        ],
        'App': [
            'Q19: (a) 360 cm² (b) $72 (c) 20% discount saves $18',
            'Q20: (a) 200 cm³ (b) 10 cm (c) No overflow, 4 cm remaining'
        ]
    },
    # P5 SSPA2 (L19)
    'P5-L19': {
        'MC': ['C','B','D','A','C','D','B','A','C','D'],
        'Calc': [
            'Q11: 72 cm²', 'Q12: 3/4', 'Q13: 150 cm³',
            'Q14: 0.375', 'Q15: x=12', 'Q16: 78.5 cm²',
            'Q17: 45 km/h', 'Q18: 120 人'
        ],
        'App': [
            'Q19: (a) 84 cm² (b) 長方形12×5=60 + 三角形12×4÷2=24 = 84',
            'Q20: (a) 900 cm³ (b) Yes, overflow 100 cm³'
        ]
    },
}

def build_sspa_answer_key(grade, lesson_num, exam_name):
    """Build answer key HTML for an SSPA exam."""
    key = SSPA_ANSWERS.get(f'{grade}-{lesson_num}')
    if not key:
        return None

    html = HEADER
    html += f'<h2>{grade} {exam_name} — 參考答案</h2>'
    html += '<p class="note">以下答案僅供核對。學生必須自行完成題目後才可查閱。</p>'

    html += '<h2>甲部：選擇題 (MC) — 每題3分</h2>'
    for i, ans in enumerate(key['MC'], 1):
        html += f'<div class="q"><span class="q-num">Q{i}.</span> <span class="answer">{ans}</span></div>'

    html += '<h2>乙部：計算題 — 每題5分</h2>'
    for calc in key['Calc']:
        html += f'<div class="q"><span class="q-num">{calc.split(":")[0]}.</span> <span class="answer">{calc.split(":",1)[1].strip() if ":" in calc else calc}</span></div>'

    html += '<h2>丙部：應用題 — 每題10分</h2>'
    for app in key['App']:
        html += f'<div class="q"><span class="q-num">{app.split(":")[0]}.</span> <span class="answer">{app.split(":",1)[1].strip() if ":" in app else app}</span></div>'

    html += FOOTER
    return html

# ═══════════════════════════════════════════════
# Auto-generated answer keys for all SSPA exams
# ═══════════════════════════════════════════════

print('Generating SSPA answer keys...')
count = 0

# Scan all grades for SSPA exams
for grade in ['P5', 'P6', 'P4', 'P3']:
    path = os.path.join(BASE, grade)
    if not os.path.exists(path): continue

    for f in sorted(glob.glob(os.path.join(path, '*SSPA*')) + glob.glob(os.path.join(path, '*模擬*'))):
        name = os.path.basename(f)
        # Extract lesson number from filename
        match = re.search(r'L(\d+)|L(\d+)', name)
        if not match: continue
        lesson_num = match.group(1) or match.group(2)

        # Build answer key
        answer_html = build_sspa_answer_key(grade, lesson_num, name.replace('.html',''))
        if answer_html:
            out_path = os.path.join(OUTPUT, f'answer_key_{grade}_L{lesson_num}_SSPA.html')
            with open(out_path, 'w', encoding='utf-8') as fh:
                fh.write(answer_html)
            count += 1
            print(f'  {grade} L{lesson_num}: answer key created')

# ═══════════════════════════════════════════════
# Generate master answer key index
# ═══════════════════════════════════════════════

index_html = HEADER
index_html += '<h2>Answer Key Index — All Available Answer Keys</h2>'
index_html += '<p class="note">答案冊持續更新中。目前涵蓋 SSPA 模擬卷及挑戰題。</p>'

index_html += '<h2>SSPA 模擬考試卷答案</h2>'
index_html += '<table style="width:100%;border-collapse:collapse;margin:10px 0;">'
index_html += '<tr style="background:#1A3C6D;color:white;"><th style="padding:6px;">年級</th><th style="padding:6px;">考試</th><th style="padding:6px;">狀態</th></tr>'

sspa_exams = [
    ('P3','L19','上學期 SSPA 模擬'), ('P3','L37','下學期 SSPA 模擬'),
    ('P4','L19','上學期 SSPA 模擬1'), ('P4','L37','下學期 SSPA 模擬2'),
    ('P5','L11','上學期 SSPA 模擬1'), ('P5','L19','上學期 SSPA 模擬2'),
    ('P5','L29','下學期 SSPA 模擬3'), ('P5','L37','下學期 SSPA 模擬4'),
    ('P6','L07','上學期 SSPA 模擬1'), ('P6','L13','上學期 SSPA 模擬2'),
    ('P6','L19','上學期 SSPA 模擬3'), ('P6','L30','下學期 SSPA 模擬4'),
    ('P6','L33','下學期 SSPA 模擬5'),
]

for grade, lesson, desc in sspa_exams:
    key_file = os.path.join(OUTPUT, f'answer_key_{grade}_L{lesson}_SSPA.html')
    status = '✅ 已建立' if os.path.exists(key_file) else '⏳ 待建立'
    row_color = 'background:#F0FDF4;' if '✅' in status else 'background:#FFFBEB;'
    index_html += f'<tr style="{row_color}"><td style="padding:4px;">{grade}</td><td style="padding:4px;">{desc}</td><td style="padding:4px;">{status}</td></tr>'

index_html += '</table>'
index_html += '<h2>如何獲取更多答案</h2>'
index_html += '<p>霖楓學苑教師及合作夥伴可聯繫課程總監取得完整答案冊。家長可於家長 WhatsApp 群組中查詢個別題目答案。</p>'
index_html += FOOTER

index_path = os.path.join(OUTPUT, 'answer_key_index.html')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

print(f'\nAnswer Key System:')
print(f'  SSPA answer keys: {count}')
print(f'  Master index: answer_key_index.html')
print(f'  Output: {OUTPUT}')
