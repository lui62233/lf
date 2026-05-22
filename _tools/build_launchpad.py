#!/usr/bin/env python3
"""
Build the LF Academy Web Launchpad + Windows Batch Shortcuts
The missing UI layer — one-click access to everything.
"""
import os, glob, json

BASE = r'G:\lam-fung-academy'
OPS = os.path.join(BASE, '_operations')
TOOLS = os.path.join(BASE, '_tools')
LECTURES = os.path.join(BASE, '講義')

# ═══════════════════════════════════════════════
# 1. WEB LAUNCHPAD
# ═══════════════════════════════════════════════

# Count everything
counts = {}
for grade in ['P3','P4','P5','P6']:
    path = os.path.join(LECTURES, grade)
    htmls = len(glob.glob(os.path.join(path, '*.html')))
    pdfs = len(glob.glob(os.path.join(path, '*.pdf')))
    svgs = 0
    for f in glob.glob(os.path.join(path, '*.html')):
        with open(f, 'r', encoding='utf-8') as fh:
            svgs += fh.read().count('<svg')
    counts[grade] = {'html': htmls, 'pdf': pdfs, 'svgs': svgs}

# Build launchpad
launchpad = f'''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<title>霖楓學苑 · LF Academy — Launchpad</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;700;900&family=Noto+Serif+HK:wght@700;900&display=swap');
:root{{--blue:#1A3C6D;--gold:#C9A84C;--red:#DC2626;--green:#16A34A;--white:#FFF;--lightbg:#F9FAFB;--borderc:#D1D5DB;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Noto Sans HK',sans-serif;background:#F3F4F6;color:#1A1A1A;font-size:14px;line-height:1.6;min-height:100vh;}}
.topbar{{background:linear-gradient(135deg,#1A3C6D,#1E4D8C);color:white;padding:16px 24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}}
.topbar h1{{font-family:'Noto Serif HK',serif;font-size:22px;letter-spacing:2px;}}
.topbar .sub{{color:#C9A84C;font-size:12px;}}
.topbar .status{{display:flex;gap:12px;flex-wrap:wrap;}}
.topbar .status .dot{{display:inline-block;width:10px;height:10px;border-radius:50%;background:#16A34A;margin-right:4px;}}
.container{{max-width:1300px;margin:0 auto;padding:20px;}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;}}
.card{{background:white;border-radius:12px;padding:20px;box-shadow:0 1px 3px rgba(0,0,0,0.08);}}
.card h2{{font-size:16px;color:var(--blue);margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--gold);}}
.card h3{{font-size:13px;color:var(--blue);margin:12px 0 6px;}}
.btn{{display:block;width:100%;padding:10px 16px;margin:6px 0;border:none;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;text-align:center;text-decoration:none;transition:all 0.15s;font-family:'Noto Sans HK',sans-serif;}}
.btn:hover{{transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,0.15);}}
.btn-primary{{background:var(--blue);color:white;}}
.btn-gold{{background:var(--gold);color:white;}}
.btn-green{{background:var(--green);color:white;}}
.btn-red{{background:var(--red);color:white;}}
.btn-outline{{background:white;color:var(--blue);border:2px solid var(--blue);}}
.btn-sm{{padding:6px 12px;font-size:11px;display:inline-block;width:auto;margin:2px;}}
.stat-row{{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--borderc);font-size:13px;}}
.stat-row .val{{font-weight:900;}}
.good{{color:var(--green);}}.warn{{color:#D97706;}}
.search-box{{width:100%;padding:10px 14px;border:2px solid var(--borderc);border-radius:8px;font-size:13px;margin:8px 0;font-family:'Noto Sans HK',sans-serif;}}
.search-box:focus{{border-color:var(--blue);outline:none;}}
.result-list{{max-height:300px;overflow-y:auto;margin-top:8px;}}
.result-item{{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;border-bottom:1px solid var(--borderc);font-size:12px;}}
.result-item:hover{{background:var(--lightbg);}}
.result-item a{{color:var(--blue);text-decoration:none;font-weight:700;}}
.result-item a:hover{{text-decoration:underline;}}
.tag{{display:inline-block;padding:2px 8px;border-radius:4px;font-size:10px;font-weight:700;margin:0 2px;}}
.tag-html{{background:#DBEAFE;color:#1E40AF;}}
.tag-pdf{{background:#DCFCE7;color:#166534;}}
.tag-svg{{background:#EDE9FE;color:#7C3AED;}}
.cmd-box{{background:#1E1E1E;color:#E5E5E5;padding:12px 16px;border-radius:8px;font-family:'Consolas','Courier New',monospace;font-size:12px;margin:8px 0;overflow-x:auto;white-space:nowrap;}}
.cmd-box .prompt{{color:#C9A84C;}}
.cmd-box .cmd{{color:#93C5FD;}}
.quick-actions{{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0;}}
.footer{{text-align:center;padding:24px;color:#6B7280;font-size:11px;}}
@media print{{body{{background:white;}}.topbar{{background:var(--blue)!important;-webkit-print-color-adjust:exact;}}}}
</style>
</head>
<body>

<div class="topbar">
<div>
<h1>霖楓學苑 · LF Academy</h1>
<div class="sub">Launchpad v1.0 — 一鍵控制台 · 不教數學，教避開陷阱。</div>
</div>
<div class="status">
<span><span class="dot"></span> 系統正常</span>
<span>📚 {sum(c['html'] for c in counts.values())} 堂</span>
<span>📄 {sum(c['pdf'] for c in counts.values())} PDF</span>
<span>📐 {sum(c['svgs'] for c in counts.values())} SVG</span>
</div>
</div>

<div class="container">
<div class="grid">

<!-- CARD 1: Quick Actions -->
<div class="card">
<h2>⚡ 常用操作（點擊即開）</h2>

<div class="quick-actions">
<a href="./講義/master_index.html" class="btn btn-primary btn-sm" target="_blank">📚 講義總索引</a>
<a href="./_operations/trap_diagnostic_test.html" class="btn btn-gold btn-sm" target="_blank">🧪 陷阱診斷測驗</a>
<a href="./_operations/teacher_training_manual.html" class="btn btn-green btn-sm" target="_blank">👩‍🏫 教師培訓手冊</a>
<a href="./_operations/trap_reference_cheatsheet.html" class="btn btn-outline btn-sm" target="_blank">📋 陷阱參考海報</a>
</div>

<h3>📣 市場與溝通</h3>
<div class="quick-actions">
<a href="./_operations/parent_comm_templates.html" class="btn btn-outline btn-sm" target="_blank">💬 家長通訊模板</a>
<a href="./_operations/social_media_30day_calendar.html" class="btn btn-outline btn-sm" target="_blank">📱 社交媒體日曆</a>
<a href="./_operations/brand_positioning_v2.html" class="btn btn-outline btn-sm" target="_blank">🎯 品牌定位 v2.0</a>
</div>

<h3>📊 數據與診斷</h3>
<div class="quick-actions">
<a href="./_operations/trap_effectiveness_tracker.html" class="btn btn-outline btn-sm" target="_blank">📈 TEI 陷阱追蹤表</a>
<a href="./_operations/routing_report_P5_sample.html" class="btn btn-outline btn-sm" target="_blank">🗺️ 路由報告 (P5樣本)</a>
<a href="./_operations/answer_keys/answer_key_index.html" class="btn btn-outline btn-sm" target="_blank">✅ 答案冊索引</a>
</div>
</div>

<!-- CARD 2: System Commands -->
<div class="card">
<h2>🖥️ 系統指令（複製→貼上到終端機）</h2>

<h3>全系統健康檢查</h3>
<div class="cmd-box">
<span class="prompt">G:\\lam-fung-academy&gt;</span> <span class="cmd">python _tools\\master_control.py check</span>
</div>

<h3>重建索引+儀表板</h3>
<div class="cmd-box">
<span class="prompt">G:\\lam-fung-academy&gt;</span> <span class="cmd">python _tools\\master_control.py rebuild</span>
</div>

<h3>生成TEI追蹤表</h3>
<div class="cmd-box">
<span class="prompt">G:\\lam-fung-academy&gt;</span> <span class="cmd">python _tools\\master_control.py track</span>
</div>

<h3>生成個人化路由報告</h3>
<div class="cmd-box">
<span class="prompt">G:\\lam-fung-academy&gt;</span> <span class="cmd">python _tools\\master_control.py route --grade P5 --weak T4,T9 --strong T1,T2</span>
</div>

<h3>重建全部PDF（耗時較長）</h3>
<div class="cmd-box">
<span class="prompt">G:\\lam-fung-academy&gt;</span> <span class="cmd">python _tools\\master_control.py rebuild</span>
</div>

<p style="font-size:10px;color:#6B7280;margin-top:8px;">💡 提示：複製灰色框內的指令，在 VS Code 終端機 (Ctrl+`) 貼上執行。</p>
</div>

<!-- CARD 3: Handout Search -->
<div class="card">
<h2>🔍 快速搜尋講義</h2>
<input type="text" class="search-box" id="searchInput" placeholder="輸入關鍵詞：例如「面積」「分數」「棒形圖」「SSPA」...">
<div class="result-list" id="searchResults">
<p style="color:#6B7280;font-size:12px;">請輸入關鍵詞開始搜尋...</p>
</div>
</div>

<!-- CARD 4: System Status -->
<div class="card">
<h2>📊 系統狀態</h2>
'''
for grade in ['P3','P4','P5','P6']:
    c = counts[grade]
    grade_name = {'P3':'小三','P4':'小四','P5':'小五','P6':'小六'}[grade]
    status_class = 'good' if c['html'] == 40 else 'warn'
    launchpad += f'<div class="stat-row"><span>{grade} {grade_name}</span><span class="val {status_class}">{c["html"]}/40 堂 | {c["pdf"]} PDF | {c["svgs"]} SVG</span></div>'

launchpad += f'''
<div class="stat-row" style="margin-top:8px;font-weight:900;border-top:2px solid var(--blue);">
<span>📦 總計</span>
<span>{sum(c['html'] for c in counts.values())} 堂講義 | {sum(c['pdf'] for c in counts.values())} PDF | {sum(c['svgs'] for c in counts.values())} SVG</span>
</div>

<h3 style="margin-top:16px;">🛠️ 工具鏈</h3>
<div class="stat-row"><span>Python 腳本</span><span>{len(glob.glob(os.path.join(TOOLS, '*.py')))} 個</span></div>
<div class="stat-row"><span>營運資產</span><span>{len(glob.glob(os.path.join(OPS, '*')))} 個</span></div>
<div class="stat-row"><span>品牌配置</span><span>1 個</span></div>
</div>

<!-- CARD 5: Quick Grade Access -->
<div class="card">
<h2>📚 按年級瀏覽</h2>
'''
for grade in ['P3','P4','P5','P6']:
    grade_name = {'P3':'小三','P4':'小四','P5':'小五','P6':'小六'}[grade]
    launchpad += f'<a href="./講義/{grade}/" class="btn btn-outline" target="_blank">📖 {grade} {grade_name}（{counts[grade]["html"]} 堂）</a>'

launchpad += '''
</div>

<!-- CARD 6: Windows Shortcuts -->
<div class="card">
<h2>🪟 Windows 一鍵批次檔</h2>
<p style="font-size:11px;color:#6B7280;margin-bottom:8px;">以下 .bat 檔案放在 G:\\lam-fung-academy\\ 目錄，雙擊即可執行，無需打開終端機。</p>

<h3>🔍 系統檢查</h3>
<div class="cmd-box">check_system.bat</div>
<p style="font-size:10px;color:#6B7280;">雙擊 → 自動檢查 160 堂講義狀態 → 結果顯示在視窗中</p>

<h3>📊 重建全部</h3>
<div class="cmd-box">rebuild_all.bat</div>
<p style="font-size:10px;color:#6B7280;">雙擊 → 重建總索引 + 品質儀表板</p>

<h3>📄 重建所有 PDF</h3>
<div class="cmd-box">rebuild_pdfs.bat</div>
<p style="font-size:10px;color:#6B7280;">雙擊 → 重建全部 160 個 PDF（⚠️ 需時約 20-30 分鐘）</p>
</div>

</div>
</div>

<div class="footer">
霖楓學苑 · LF Academy · Launchpad v1.0<br>
開啟方式：在資料夾中雙擊 <strong>launchpad.html</strong> 即可在瀏覽器中打開此控制台<br>
所有連結均為相對路徑，無需網絡伺服器
</div>

<script>
// Search functionality
const handouts = [
'''

# Index all handouts for search
for grade in ['P3','P4','P5','P6']:
    path = os.path.join(LECTURES, grade)
    for f in sorted(glob.glob(os.path.join(path, '*.html'))):
        name = os.path.basename(f)
        topic = name.replace('.html','').replace(f'LF-{grade}-','')
        launchpad += f'  {{"grade":"{grade}","name":"{name}","topic":"{topic}","path":"./講義/{grade}/{name}"}},\n'

launchpad += '''];
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

searchInput.addEventListener('input', function() {
  const query = this.value.toLowerCase();
  if (query.length < 1) {
    searchResults.innerHTML = '<p style="color:#6B7280;font-size:12px;">請輸入關鍵詞開始搜尋...</p>';
    return;
  }
  const filtered = handouts.filter(h => h.topic.toLowerCase().includes(query) || h.grade.includes(query));
  if (filtered.length === 0) {
    searchResults.innerHTML = '<p style="color:#DC2626;font-size:12px;">沒有找到匹配的講義。試試其他關鍵詞。</p>';
    return;
  }
  searchResults.innerHTML = filtered.slice(0, 20).map(h =>
    `<div class="result-item">
      <span><span class="tag tag-html">${h.grade}</span> ${h.topic.substring(0,60)}</span>
      <span><a href="${h.path}" target="_blank">📖 開啟</a></span>
    </div>`
  ).join('');
  if (filtered.length > 20) {
    searchResults.innerHTML += `<p style="color:#6B7280;font-size:10px;text-align:center;margin-top:4px;">顯示前 20 筆，共 ${filtered.length} 筆結果。請輸入更具體的關鍵詞。</p>`;
  }
});
</script>
</body>
</html>'''

# Write launchpad
launchpad_path = os.path.join(BASE, 'launchpad.html')
with open(launchpad_path, 'w', encoding='utf-8') as f:
    f.write(launchpad)
print(f'Launchpad: {launchpad_path} ({len(launchpad)} chars)')

# ═══════════════════════════════════════════════
# 2. WINDOWS BATCH FILES
# ═══════════════════════════════════════════════

bat_files = {
    'check_system.bat': '''@echo off
cd /d G:\\lam-fung-academy
echo ========================================
echo 霖楓學苑 LF Academy - 系統健康檢查
echo ========================================
python _tools\\master_control.py check
echo.
echo 檢查完成。按任意鍵關閉...
pause >nul
''',
    'rebuild_all.bat': '''@echo off
cd /d G:\\lam-fung-academy
echo ========================================
echo 霖楓學苑 LF Academy - 重建系統資產
echo ========================================
python _tools\\master_control.py rebuild
echo.
echo 重建完成。按任意鍵關閉...
pause >nul
''',
    'open_launchpad.bat': '''@echo off
start "" "G:\\lam-fung-academy\\launchpad.html"
''',
    'build_all_pdfs.bat': '''@echo off
cd /d G:\\lam-fung-academy
echo ========================================
echo 霖楓學苑 LF Academy - 批次建立 PDF
echo 警告：此操作需時 20-30 分鐘
echo ========================================
python _tools\\master_control.py rebuild
echo.
echo PDF 建立完成。按任意鍵關閉...
pause >nul
''',
}

for name, content in bat_files.items():
    path = os.path.join(BASE, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Batch file: {path}')

# ═══════════════════════════════════════════════
# 3. VS CODE TASKS
# ═══════════════════════════════════════════════
vscode_dir = os.path.join(BASE, '.vscode')
os.makedirs(vscode_dir, exist_ok=True)

tasks = {
    "version": "2.0.0",
    "tasks": [
        {
            "label": "LF Academy: System Check",
            "type": "shell",
            "command": "python",
            "args": ["_tools/master_control.py", "check"],
            "options": {"cwd": BASE},
            "group": "build",
            "presentation": {"reveal": "always", "panel": "dedicated"}
        },
        {
            "label": "LF Academy: Rebuild All",
            "type": "shell",
            "command": "python",
            "args": ["_tools/master_control.py", "rebuild"],
            "options": {"cwd": BASE},
            "group": "build",
            "presentation": {"reveal": "always", "panel": "dedicated"}
        },
        {
            "label": "LF Academy: Open Launchpad",
            "type": "shell",
            "command": "start launchpad.html",
            "options": {"cwd": BASE},
            "presentation": {"reveal": "silent"}
        },
        {
            "label": "LF Academy: Generate TEI Tracker",
            "type": "shell",
            "command": "python",
            "args": ["_tools/master_control.py", "track"],
            "options": {"cwd": BASE},
            "presentation": {"reveal": "always"}
        }
    ]
}

tasks_path = os.path.join(vscode_dir, 'tasks.json')
with open(tasks_path, 'w', encoding='utf-8') as f:
    json.dump(tasks, f, indent=2, ensure_ascii=False)
print(f'VS Code tasks: {tasks_path}')

print(f'\n=== LAUNCHPAD COMPLETE ===')
print(f'Open: {launchpad_path}')
print(f'Or double-click: {os.path.join(BASE, "open_launchpad.bat")}')
print(f'Or in VS Code: Ctrl+Shift+P → "Tasks: Run Task" → "LF Academy: Open Launchpad"')
