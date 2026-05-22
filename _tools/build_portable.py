#!/usr/bin/env python3
"""
霖楓學苑 · LF Academy — Portable Deployment Builder
Creates a self-contained portable version that works on ANY device:
- Phone (iPhone/Android): open in browser
- Tablet (iPad/Android): open in browser
- Other computers (Windows/Mac/Linux): open in browser or run Python
- USB drive: plug and play
- Cloud (Google Drive/Dropbox): share link → open in browser
"""
import os, sys, glob, json, shutil, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'G:\lam-fung-academy'
PORTABLE = os.path.join(BASE, '_portable')
os.makedirs(PORTABLE, exist_ok=True)

print('Building Portable LF Academy System...')
print('='*60)

# ═══════════════════════════════════════════════
# 1. PORTABLE WEB — Works on ANY device with a browser
# ═══════════════════════════════════════════════
WEB = os.path.join(PORTABLE, 'web')
os.makedirs(WEB, exist_ok=True)

# Copy launchpad
shutil.copy(os.path.join(BASE, 'launchpad.html'), os.path.join(WEB, 'index.html'))

# Copy all handouts (HTML + PDF) — these work standalone
imported = 0
for grade in ['P3','P4','P5','P6']:
    src_dir = os.path.join(BASE, '講義', grade)
    dst_dir = os.path.join(WEB, '講義', grade)
    os.makedirs(dst_dir, exist_ok=True)

    for f in glob.glob(os.path.join(src_dir, '*.html')):
        shutil.copy(f, os.path.join(dst_dir, os.path.basename(f)))
        imported += 1

print(f'  Handouts: {imported} HTML files copied')

# Copy operations assets
ops_dst = os.path.join(WEB, '_operations')
os.makedirs(ops_dst, exist_ok=True)
for f in glob.glob(os.path.join(BASE, '_operations', '*.html')):
    shutil.copy(f, os.path.join(ops_dst, os.path.basename(f)))
print(f'  Operations: {len(glob.glob(os.path.join(ops_dst, "*.html")))} assets')

# Copy config
config_dst = os.path.join(WEB, '_config')
os.makedirs(config_dst, exist_ok=True)
for f in glob.glob(os.path.join(BASE, '_config', '*')):
    shutil.copy(f, os.path.join(config_dst, os.path.basename(f)))

# Update launchpad paths to be relative for web
launchpad_path = os.path.join(WEB, 'index.html')
with open(launchpad_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix paths for portable web version (remove ./ prefix assumptions)
html = html.replace('./講義/', '講義/')
html = html.replace('./_operations/', '_operations/')

with open(launchpad_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Create mobile-friendly index
mobile_html = '''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>霖楓學苑 · LF Academy</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;700;900&family=Noto+Serif+HK:wght@700;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Noto Sans HK',sans-serif;background:#F3F4F6;color:#1A1A1A;font-size:15px;line-height:1.6;min-height:100vh;}
.header{background:linear-gradient(135deg,#1A3C6D,#1E4D8C);color:white;padding:20px 16px;text-align:center;}
.header h1{font-family:'Noto Serif HK',serif;font-size:20px;letter-spacing:2px;}
.header p{color:#C9A84C;font-size:13px;margin-top:4px;}
.container{padding:16px;max-width:600px;margin:0 auto;}
.card{background:white;border-radius:12px;padding:16px;margin:12px 0;box-shadow:0 1px 3px rgba(0,0,0,0.08);}
.card h2{font-size:16px;color:#1A3C6D;margin-bottom:10px;}
.btn{display:block;width:100%;padding:14px 16px;margin:8px 0;border:none;border-radius:10px;font-size:15px;font-weight:700;text-align:center;text-decoration:none;font-family:'Noto Sans HK',sans-serif;}
.btn-blue{background:#1A3C6D;color:white;}
.btn-gold{background:#C9A84C;color:white;}
.btn-green{background:#16A34A;color:white;}
.btn-outline{background:white;color:#1A3C6D;border:2px solid #1A3C6D;}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.footer{text-align:center;padding:20px;font-size:11px;color:#6B7280;}
.grade-links{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.grade-link{background:white;border:2px solid #D1D5DB;border-radius:10px;padding:14px;text-align:center;text-decoration:none;color:#1A3C6D;font-weight:700;font-size:14px;}
.grade-link:hover{border-color:#C9A84C;}
</style>
</head>
<body>
<div class="header">
<h1>霖楓學苑 · LF Academy</h1>
<p>不教數學，教避開陷阱。</p>
</div>
<div class="container">
<div class="card">
<h2>📚 按年級瀏覽講義</h2>
<div class="grade-links">
<a href="講義/P3/" class="grade-link">P3 小三<br><small>40 堂</small></a>
<a href="講義/P4/" class="grade-link">P4 小四<br><small>40 堂</small></a>
<a href="講義/P5/" class="grade-link">P5 小五<br><small>40 堂</small></a>
<a href="講義/P6/" class="grade-link">P6 小六<br><small>40 堂</small></a>
</div>
</div>
<div class="card">
<h2>🧪 診斷與教學工具</h2>
<a href="_operations/trap_diagnostic_test.html" class="btn btn-gold">陷阱診斷測驗</a>
<a href="_operations/teacher_training_manual.html" class="btn btn-outline">教師培訓手冊</a>
<a href="_operations/trap_reference_cheatsheet.html" class="btn btn-outline">陷阱參考海報</a>
</div>
<div class="card">
<h2>📣 營運工具</h2>
<a href="_operations/parent_comm_templates.html" class="btn btn-outline">家長通訊模板</a>
<a href="_operations/social_media_30day_calendar.html" class="btn btn-outline">社交媒體日曆</a>
<a href="_operations/brand_positioning_v2.html" class="btn btn-outline">品牌定位 v2.0</a>
</div>
<div style="text-align:center;margin:16px 0;">
<a href="index.html" class="btn btn-blue">🖥️ 完整桌面版控制台</a>
</div>
</div>
<div class="footer">霖楓學苑 · LF Academy · 便攜版</div>
</body>
</html>'''

with open(os.path.join(WEB, 'mobile.html'), 'w', encoding='utf-8') as f:
    f.write(mobile_html)

# Create directory index files for each grade (so browsing works on web server)
for grade in ['P3','P4','P5','P6']:
    grade_dir = os.path.join(WEB, '講義', grade)
    grade_name = {'P3':'小三','P4':'小四','P5':'小五','P6':'小六'}[grade]
    files = sorted(glob.glob(os.path.join(grade_dir, '*.html')))

    index_html = f'''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>LF Academy · {grade} {grade_name} 講義</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;700;900&display=swap');
body{{font-family:'Noto Sans HK',sans-serif;max-width:800px;margin:0 auto;padding:16px;font-size:14px;background:#F3F4F6;}}
h1{{color:#1A3C6D;border-left:4px solid #C9A84C;padding-left:12px;}}
a{{display:block;padding:12px 16px;margin:6px 0;background:white;border-radius:8px;text-decoration:none;color:#1A3C6D;font-weight:700;border:1px solid #D1D5DB;}}
a:hover{{border-color:#C9A84C;background:#FFFBEB;}}
small{{color:#6B7280;font-weight:400;}}
</style></head><body>
<h1>{grade} {grade_name} · 講義目錄<br><small>{len(files)} 堂</small></h1>
'''
    for f in files:
        name = os.path.basename(f).replace('.html','')
        topic = name.replace(f'LF-{grade}-','').replace(f'LF-{grade}-','')
        index_html += f'<a href="{os.path.basename(f)}">{topic[:80]}</a>\n'

    index_html += '<p style="text-align:center;margin-top:20px;"><a href="../../mobile.html" style="display:inline;padding:8px 16px;background:#1A3C6D;color:white;border-radius:20px;">← 返回主頁</a></p></body></html>'

    with open(os.path.join(grade_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)

print(f'\n  Portable Web: {WEB}')
print(f'  Size: {sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, fn in os.walk(WEB) for f in fn) // (1024*1024)} MB')

# ═══════════════════════════════════════════════
# 2. ONE-CLICK SETUP SCRIPT (for other Windows computers)
# ═══════════════════════════════════════════════
setup_bat = '''@echo off
echo =============================================
echo 霖楓學苑 LF Academy - 一鍵環境安裝
echo =============================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Installing...
    echo Please download Python from https://python.org
    echo Make sure to check "Add Python to PATH"
    pause
    exit /b 1
)
echo [OK] Python found

:: Install requirements
echo Installing required packages...
pip install pymupdf matplotlib -q
echo [OK] Packages installed

:: Check Edge (for PDF generation)
where msedge >nul 2>&1
if errorlevel 1 (
    echo [WARN] Microsoft Edge not found in PATH
    echo PDF generation may not work
    echo Install Edge: https://microsoft.com/edge
) else (
    echo [OK] Microsoft Edge found
)

:: Check fonts
echo.
echo [INFO] For best results, install Noto Sans HK font:
echo https://fonts.google.com/noto/specimen/Noto+Sans+HK

echo.
echo =============================================
echo Setup complete!
echo.
echo Quick start:
echo   1. Double-click launchpad.html for web control panel
echo   2. Or run: python _tools\\master_control.py check
echo =============================================
pause
'''

with open(os.path.join(PORTABLE, 'setup_windows.bat'), 'w', encoding='utf-8') as f:
    f.write(setup_bat)

# ═══════════════════════════════════════════════
# 3. DEPLOYMENT GUIDE
# ═══════════════════════════════════════════════
guide = '''# 霖楓學苑 · LF Academy — 跨裝置部署指南

## 方式一：手機/平板（最簡單）
1. 將 `_portable/web/` 文件夾上傳到以下任一平台：
   - **Google Drive**：上傳文件夾 → 右鍵「共用」→ 「任何知道連結的人都可以檢視」
   - **Dropbox**：上傳文件夾 → 複製連結
   - **GitHub Pages**（免費）：推送 `_portable/web/` 到 GitHub → Settings → Pages → 部署
2. 在手機瀏覽器中打開連結
3. 建議先打開 `mobile.html`（手機友善版），或 `index.html`（完整控制台）
4. 所有講義 HTML 都可以直接在瀏覽器中查看，無需任何 App

## 方式二：其他 Windows 電腦（完整功能）
1. 複製整個 `G:\\lam-fung-academy\\` 文件夾到新電腦
   - USB 手指
   - 外置硬碟
   - 雲端同步（Google Drive / Dropbox / OneDrive）
2. 雙擊 `setup_windows.bat` 自動安裝所需環境
3. 雙擊 `launchpad.html` 或 `open_launchpad.bat`

## 方式三：GitHub（最專業）
```bash
# 在新電腦上
git clone <你的GitHub倉庫URL> lam-fung-academy
cd lam-fung-academy
setup_windows.bat
```

## 方式四：iPhone/iPad 特定
- 使用「檔案」App 打開 Google Drive 中的 HTML 檔案
- 或使用 Safari 打開 GitHub Pages 連結
- 講義可在瀏覽器中直接查看和打印（AirPrint）

## 方式五：Android 特定
- 使用 Chrome 打開雲端連結
- 可下載講義 HTML 到手機離線查看
- 支援 Chrome 的「添加到主畫面」功能

## 檔案說明
- `launchpad.html` — 桌面版控制台（電腦用）
- `mobile.html` — 手機版首頁（手機/平板用）
- `講義/P3-P6/` — 全部 160 堂講義（HTML + PDF）
- `_operations/` — 營運資產（診斷測驗、教師手冊等）
- `_tools/` — Python 工具（僅限電腦使用）
'''

with open(os.path.join(PORTABLE, 'DEPLOYMENT_GUIDE.md'), 'w', encoding='utf-8') as f:
    f.write(guide)

# ═══════════════════════════════════════════════
# 4. GITIGNORE (for GitHub)
# ═══════════════════════════════════════════════
gitignore = '''# PDFs are large — optional to commit
講義/*/LF-*.pdf

# Python cache
__pycache__/
*.pyc

# Node modules (OCR tools)
node_modules/

# OCR data (large)
_ocr_pages/
_ocr_text/

# Portable build (generated)
_portable/

# VS Code
.vscode/
'''
with open(os.path.join(BASE, '.gitignore'), 'w', encoding='utf-8') as f:
    f.write(gitignore)

# ═══════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════
web_size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, fn in os.walk(WEB) for f in fn) // (1024*1024)
total_files = sum(1 for _, _, fn in os.walk(WEB) for _ in fn)

print(f'\n{"="*60}')
print(f'PORTABLE DEPLOYMENT READY')
print(f'{"="*60}')
print(f'Location: {PORTABLE}')
print(f'Web version: {total_files} files, {web_size} MB')
print(f'')
print(f'To use on phone/tablet:')
print(f'  1. Upload {WEB} to Google Drive / Dropbox / GitHub Pages')
print(f'  2. Open mobile.html in browser')
print(f'')
print(f'To use on another computer:')
print(f'  1. Copy entire G:\\lam-fung-academy\\ to new computer')
print(f'  2. Run setup_windows.bat')
print(f'  3. Open launchpad.html')
print(f'')
print(f'Setup guide: {os.path.join(PORTABLE, "DEPLOYMENT_GUIDE.md")}')
