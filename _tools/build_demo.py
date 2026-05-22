import sys, os, io, base64, subprocess
sys.path.insert(0, r'G:\lam-fung-academy\_tools')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=['Noto Sans HK','DejaVu Sans']
matplotlib.rcParams['mathtext.fontset']='dejavusans'
from svg_geometry import rectangle as svg_rect, triangle as svg_tri, trapezoid as svg_trap, grid_diagram as svg_grid, displacement as svg_disp, square as svg_sq, composite_L as svg_L, composite_T as svg_T, composite_hole as svg_hole

def tex2png(f, fs=56, dpi=1200, bold=False):
    """v1.3: 1200dpi·48px·3x超採樣·分數自適應"""
    has_frac = '\\frac' in f
    use_fs = int(fs * 1.5) if has_frac else fs
    use_h = 0.75 if has_frac else 0.55
    if bold: f = r'\mathbf{' + f + '}'
    w = max(1.8, len(f) * 0.16)
    fig, ax = plt.subplots(figsize=(w, use_h)); ax.axis('off')
    ax.text(0.5, 0.5, f'${f}$', fontsize=use_fs, ha='center', va='center', transform=ax.transAxes)
    buf = io.BytesIO(); fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.05, dpi=dpi, transparent=True); buf.seek(0); plt.close(fig)
    return f'data:image/png;base64,{base64.b64encode(buf.read()).decode()}'

F = {
    'wrong': tex2png(r'\frac{4}{2} = 2', bold=True),
    'right': tex2png(r'\frac{7}{12}', bold=True),
    'area_para': tex2png(r'A = b \times h'),
    'area_tri': tex2png(r'A = \frac{1}{2}bh'),
    'area_tri_bold': tex2png(r'A = \frac{1}{2}bh', bold=True),
    'area_trap': tex2png(r'A = \frac{(a+b)h}{2}'),
    'area_rect': tex2png(r'A = l \times w'),
    'peri_sq': tex2png(r'P = 4a'),
    'peri_rect': tex2png(r'P = 2(l+w)'),
}

S = {
    'para': svg_rect(140, 80), 'tri_r': svg_tri(110, 80, 'right'),
    'tri_o': svg_tri(110, 80, 'obtuse'), 'tri_i': svg_tri(110, 80, 'isosceles'),
    'trap': svg_trap(70, 120, 75), 'grid': svg_grid(4, 3),
    'disp': svg_disp(), 'sq': svg_sq(90),
    'Lshape': svg_L(80, 100, 90, 45), 'Tshape': svg_T(130, 35, 60, 55),
    'hole': svg_hole(150, 100, 50, 50),
}

html = '''<!DOCTYPE html><html lang="zh-HK"><head><meta charset="UTF-8">
<style>@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;500;700;900&family=Noto+Serif+HK:wght@600;700;900&display=swap');
:root{--blue:#1A3C6D;--gold:#C9A84C;--red:#DC2626;--green:#16A34A;--white:#FFF;--ink:#1A1A1A;--gray:#6B7280;--lightbg:#F9FAFB;--borderc:#D1D5DB;}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Noto Sans HK',sans-serif;background:#E5E5E5;color:var(--ink);font-size:14px;line-height:1.7;}
.container{max-width:1000px;margin:0 auto;}
.pb{width:100%;background:var(--white);padding:32px 42px;display:flex;flex-direction:column;}
@media print{body{background:white;font-size:11px;}.pb{box-shadow:none;min-height:0;padding:20px 30px;}.pb.cover-page{page-break-after:always;}.no-print{display:none!important;}}
.cover{justify-content:center;align-items:center;text-align:center;}
.cv-logo{font-family:'Noto Serif HK',serif;font-size:20px;font-weight:900;color:var(--blue);letter-spacing:6px;}
.cv-badge{display:inline-block;border:1.5px solid var(--gold);color:var(--gold);padding:5px 22px;border-radius:20px;font-size:12px;letter-spacing:3px;margin:14px 0;}
.cv-title{font-family:'Noto Serif HK',serif;font-size:30px;font-weight:900;color:var(--blue);letter-spacing:3px;margin:10px 0 5px;}
.cv-sub{font-size:13px;color:var(--gray);margin-bottom:20px;}
.h1{font-family:'Noto Serif HK',serif;font-size:16px;font-weight:900;color:var(--blue);padding:6px 10px;margin:14px 0 8px;border-left:4px solid var(--gold);background:#FFFBEB;}
.h2{font-family:'Noto Serif HK',serif;font-size:13px;font-weight:700;color:var(--blue);margin:12px 0 5px;padding-bottom:2px;border-bottom:1px solid var(--borderc);}
.kp{margin:8px 0;padding:10px 12px;background:var(--lightbg);border:1px solid var(--borderc);border-radius:5px;}
.kp-title{font-size:13px;font-weight:900;color:var(--blue);margin-bottom:3px;}
.kp-rules{font-size:12px;line-height:1.7;}
.tc{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:7px 0;}
.tc-w{background:#FEF2F2;border:2px solid #FECACA;border-radius:8px;padding:14px;text-align:center;}
.tc-r{background:#F0FDF4;border:2px solid #BBF7D0;border-radius:8px;padding:14px;text-align:center;}
.tc-w .lbl{font-size:14px;font-weight:900;color:var(--red);margin-bottom:4px;}
.tc-r .lbl{font-size:14px;font-weight:900;color:var(--green);margin-bottom:4px;}
.math-png{display:inline-block;vertical-align:middle;height:1.5em;margin:0 3px;}
.fig-row{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin:12px 0;}
.fig-card{text-align:center;padding:10px;background:var(--white);border-radius:8px;}
.fig-title{font-size:12px;font-weight:700;color:var(--blue);margin-bottom:6px;}
.warn{background:#FEF2F2;border-left:3px solid var(--red);padding:5px 8px;margin:6px 0;font-size:12px;font-weight:600;color:#991B1B;}
.mn{background:linear-gradient(135deg,#FFF8E7,#FFEDD5);border:2px solid var(--gold);border-radius:7px;padding:9px 12px;margin:6px 0;text-align:center;font-size:14px;font-weight:900;color:var(--blue);}
.fb{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 2px;}
.fb span{font-size:13px;font-weight:600;line-height:1.2;}
.fb .bar{width:100%;height:1.8px;background:var(--blue);min-width:18px;margin:1px 0;}
.good{color:#16A34A;font-weight:700;}.new{color:#7C3AED;font-weight:700;}
.qt{width:100%;border-collapse:collapse;margin:8px 0;font-size:13px;}
.qt th{background:var(--blue);color:white;padding:5px 8px;text-align:left;}
.qt td{padding:8px;border:1px solid var(--borderc);vertical-align:top;}
.qt tr:nth-child(even) td{background:#FAFBFC;}
</style></head><body><div class="container">

<div class="pb cover-page cover">
<div class="cv-logo">《霖楓學苑 · LF Academy》</div><div class="cv-badge">v1.2 最新工具鏈示範</div>
<div class="cv-title">平行四邊形與三角形面積</div>
<div class="cv-sub">CSS分數 + PNG超採樣公式 + SVG幾何圖形 · 三合一</div>
</div>

<div class="pb">
<div class="h1">一、<span class="new">PNG v1.2</span> 超採樣公式（800dpi·32px·2x超採樣）</div>

<div class="tc">
<div class="tc-w"><div class="lbl">常見錯誤</div>''' + '<img class="math-png" src="' + F['wrong'] + '"></div>'
html += '<div class="tc-r"><div class="lbl">正確解法</div>' + '<img class="math-png" src="' + F['right'] + '"></div></div>'

html += '<div class="kp" style="margin-top:12px;"><div class="kp-title">面積公式（PNG v1.2 · 800dpi超採樣）</div><div class="kp-rules">'
for name, label in [('area_para','平行四邊形'),('area_tri','三角形'),('area_trap','梯形'),('area_rect','長方形')]:
    html += f'<p>{label}：<img class="math-png" src="{F[name]}"></p>'
html += '</div></div>'

html += '<div class="kp"><div class="kp-title">周界公式對比（避免混淆！）</div><div class="kp-rules">'
html += f'<p>正方形：<img class="math-png" src="{F["peri_sq"]}"> ⚠️ 面積才是 a²</p>'
html += f'<p>長方形：<img class="math-png" src="{F["peri_rect"]}"> ⚠️ 面積才是 l×w</p>'
html += '</div></div>'
html += '<div class="warn">最常見致命錯誤：把周界公式當面積用！P=4a ≠ A=a²</div>'

html += '<div class="h1" style="margin-top:20px;">二、<span class="new">SVG</span> 幾何圖形（svg_geometry.py 自動生成）</div>'

shapes = [
    [('平行四邊形','para'),('正方形','sq')],
    [('直角三角形','tri_r'),('鈍角三角形（高在外面）','tri_o'),('等腰三角形','tri_i')],
    [('梯形','trap'),('排水法示意','disp')],
    [('格點圖（面積=鋪滿格數）','grid')],
]
for row in shapes:
    html += '<div class="fig-row">'
    for label, key in row:
        html += f'<div class="fig-card"><div class="fig-title">{label}</div>{S[key]}</div>'
    html += '</div>'

html += '<div class="mn">口訣：「底乘高係平行四邊，底乘高除二係三角。高一定係垂直線，鈍角三角拉出嚟睇。」</div>'

html += '''<div class="h1" style="margin-top:20px;">三、<span class="good">CSS 分數</span> 練習題（向量·無限清晰·完美字體匹配）</div>
<table class="qt">
<tr><th>#</th><th>題目</th><th>作答區</th></tr>
<tr><td style="text-align:center;">1</td><td>平行四邊形底 8cm，高 5cm。面積 = ？</td><td style="min-height:40px;border:1px dashed #D1D5DB;"></td></tr>
<tr><td style="text-align:center;">2</td><td>三角形底 10cm，高 6cm。面積 = ？</td><td style="min-height:40px;border:1px dashed #D1D5DB;"></td></tr>
<tr><td style="text-align:center;">3</td><td>計算：<span class="fb"><span>5</span><span class="bar"></span><span>6</span></span> + <span class="fb"><span>1</span><span class="bar"></span><span>4</span></span> = ？</td><td style="min-height:40px;border:1px dashed #D1D5DB;"></td></tr>
<tr><td style="text-align:center;">4</td><td>計算：<span class="fb"><span>2</span><span class="bar"></span><span>3</span></span> × <span class="fb"><span>3</span><span class="bar"></span><span>5</span></span> = ？</td><td style="min-height:40px;border:1px dashed #D1D5DB;"></td></tr>
</table>

<div style="text-align:center;margin-top:24px;padding:16px;background:var(--lightbg);border-radius:8px;">
<h3 style="color:var(--blue);">三種技術對比總結</h3>
<table style="margin:12px auto;border-collapse:collapse;font-size:13px;">
<tr style="background:var(--blue);color:white;"><th style="padding:8px 14px;">技術</th><th style="padding:8px 14px;">適用場景</th><th style="padding:8px 14px;">優勢</th></tr>
<tr><td style="padding:8px 14px;"><span class="good">CSS 分數</span></td><td style="padding:8px 14px;">練習題中的分數</td><td style="padding:8px 14px;">向量·零體積·完美字體匹配</td></tr>
<tr><td style="padding:8px 14px;"><span class="new">PNG v1.2</span></td><td style="padding:8px 14px;">公式展示·封面·重點</td><td style="padding:8px 14px;">超採樣800dpi·專業LaTeX排版</td></tr>
<tr><td style="padding:8px 14px;"><span class="new">SVG</span></td><td style="padding:8px 14px;">幾何圖形</td><td style="padding:8px 14px;">向量·可縮放·自動標註</td></tr>
</table>
</div>
</div></div></body></html>'''

path = r'G:\lam-fung-academy\_templates\demo_v2.html'
with open(path, 'w', encoding='utf-8') as f: f.write(html)
print(f'HTML: {len(html)} chars, {len(F)} PNGs, {len(S)} SVGs')

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
pdf = r'G:\lam-fung-academy\_templates\demo_v2.pdf'
subprocess.run([edge, '--headless', '--disable-gpu', f'--print-to-pdf={pdf}', f'file:///{path}'], capture_output=True, timeout=60)

import pymupdf
doc = pymupdf.open(pdf)
total_imgs = sum(len(p.get_images()) for p in doc)
print(f'PDF: {len(doc)}p, {total_imgs} embedded PNGs, {os.path.getsize(pdf)} bytes')
for i, page in enumerate(doc):
    imgs = page.get_images()
    if imgs: print(f'  P{i+1}: {len(imgs)} images, sample: {imgs[0][2]}x{imgs[0][3]}px')
