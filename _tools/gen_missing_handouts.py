#!/usr/bin/env python3
"""霖楓學苑 · LF Academy — P6下學期 6 MISSING Handouts Generator v1.0
Generates L29, L30, L37, L38, L39, L40 with embedded SVGs and formula PNGs.
"""
import sys, os, subprocess

# Add the tools directory to sys.path
TOOLS_DIR = r"G:\lam-fung-academy\_tools"
OUTPUT_DIR = r"G:\lam-fung-academy\講義\P6"
sys.path.insert(0, TOOLS_DIR)

from svg_geometry import (_sv, _t, _r, _li, _ra, C,
    square, rectangle, triangle, trapezoid, circle_shape, cuboid,
    displacement, composite_L, composite_T, composite_hole,
    grid_diagram, bar_simple, bar_composite, bar_blank, bar_composite_blank,
    line_chart, line_blank, pie_chart, data_table)

try:
    from render_math import tex2png_b64, get_template
except:
    def tex2png_b64(formula, fontsize=48, dpi=1200, bold=False, has_frac=None):
        return ""
    def get_template(name, fs=48, bold=False):
        return ""

# ── Helper: run render_math.py from CLI ──
def render_formula(formula, fs=48, bold=False, has_frac=None):
    """Generate formula as base64 PNG."""
    if has_frac is None:
        has_frac = r'\frac' in formula
    try:
        cmd = [sys.executable, os.path.join(TOOLS_DIR, 'render_math.py'), formula, str(fs)]
        if bold:
            cmd.append('true')
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout.strip()
    except:
        try:
            return tex2png_b64(formula, fontsize=fs, bold=bold, has_frac=has_frac)
        except:
            return ""

def render_template(name, fs=48, bold=False):
    """Render a known template formula."""
    try:
        cmd = [sys.executable, os.path.join(TOOLS_DIR, 'render_math.py'), '--template', name, str(fs)]
        if bold:
            cmd.append('true')
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout.strip()
    except:
        try:
            return get_template(name, fs=fs, bold=bold)
        except:
            return ""

# ── CSS Fragment ──
CSS_COMMON = '''<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;500;700;900&family=Noto+Serif+HK:wght@600;700;900&display=swap');

  :root {
    --blue:#1A3C6D; --gold:#C9A84C; --red:#DC2626; --green:#16A34A;
    --white:#FFF; --ink:#1A1A1A; --gray:#6B7280;
    --lightbg:#F9FAFB; --borderc:#D1D5DB;
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  body {
    font-family:'Noto Sans HK',sans-serif;
    background:#E5E5E5; color:var(--ink);
    font-size:13px; line-height:1.65;
    -webkit-font-smoothing:antialiased;
  }

  @media print {
    body { background:white; font-size:11px; }
    .pb { box-shadow:none; min-height:0; padding:24px 36px; }
    .pb.cover-page { page-break-after:always; }
    .page-break { page-break-before:always; }
    .no-print { display:none!important; }
    .qt .qw { background: repeating-linear-gradient(transparent,transparent 23px,#E5E7EB 23px,#E5E7EB 24px); border: 1px dashed #9CA3AF; }
    .qt td { padding:4px 6px; }
    .qt { font-size:10.5px; }
    .qt .qtxt { font-size:11.5px; }
    .h1 { font-size:14px; margin:12px 0 7px; }
    .h2 { font-size:12px; }
    .kp { padding:7px 10px; }
    .kp-rules { font-size:10.5px; }
    .ex { padding:7px 10px; }
    .ex-q { font-size:12px; }
    .warn { font-size:10.5px; padding:5px 8px; }
    .mn { font-size:12px; padding:8px 10px; }
    .sc { gap:6px; }
    .sc-i { padding:10px; }
    .sc-i .n { width:26px;height:26px;font-size:14px; }
    .sc-i .t { font-size:11px; }
    .tc { gap:8px; }
    .tc-w, .tc-r { padding:10px; }
    .et { font-size:10px; }
  }

  .container { max-width:1000px; margin:0 auto; }

  .pb {
    width:100%;
    background:var(--white);
    padding:36px 48px;
    display:flex; flex-direction:column;
  }

  /* Fractions */
  .f  { display:inline-flex; flex-direction:column; align-items:center; vertical-align:middle; margin:0 2px; font-size:inherit; }
  .f .n { font-size:inherit; line-height:1.15; }
  .f .d { font-size:inherit; line-height:1.15; }
  .f .b { width:100%; height:1.4px; background:currentColor; margin:2px 0; min-width:16px; }

  .fd { display:inline-flex; flex-direction:column; align-items:center; vertical-align:middle; margin:0 3px; }
  .fd .n { font-size:16px; font-weight:700; line-height:1.15; }
  .fd .d { font-size:16px; font-weight:700; line-height:1.15; }
  .fd .b { width:100%; height:2px; background:currentColor; min-width:22px; margin:3px 0; }

  .fi { display:inline-flex; flex-direction:column; align-items:center; vertical-align:middle; margin:0 1px; font-size:inherit; }
  .fi .n { font-size:inherit; line-height:1; }
  .fi .d { font-size:inherit; line-height:1; }
  .fi .b { width:100%; height:1px; background:currentColor; min-width:12px; }

  .fb { display:inline-flex; align-items:baseline; vertical-align:middle; margin:0 2px; }
  .fb .wh { font-size:inherit; }
  .fb .fr { display:inline-flex; flex-direction:column; align-items:center; margin:0 1px; }
  .fb .fr .n { font-size:inherit; line-height:1.15; }
  .fb .fr .d { font-size:inherit; line-height:1.15; }
  .fb .fr .b { width:100%; height:1.2px; background:currentColor; min-width:14px; }

  /* Cover */
  .cover {
    justify-content:center; align-items:center; text-align:center;
    background:var(--white);
  }
  .cv-logo { font-family:'Noto Serif HK',serif; font-size:20px; font-weight:900; color:var(--blue); letter-spacing:6px; }
  .cv-badge {
    display:inline-block; border:1.5px solid var(--gold); color:var(--gold);
    padding:5px 22px; border-radius:20px; font-size:12px; letter-spacing:3px;
    margin:16px 0;
  }
  .cv-title { font-family:'Noto Serif HK',serif; font-size:30px; font-weight:900; color:var(--blue); letter-spacing:3px; margin:12px 0 6px; }
  .cv-sub { font-size:13px; color:var(--gray); margin-bottom:24px; }
  .cv-info {
    display:inline-block; text-align:left;
    background:var(--lightbg); border:1px solid var(--borderc); border-radius:8px;
    padding:18px 24px; font-size:12px; line-height:2;
  }
  .cv-info b { color:var(--blue); }
  .cv-row { margin-top:24px; font-size:13px; display:flex; gap:28px; flex-wrap:wrap; }
  .cv-row .ln { display:inline-block; width:100px; border-bottom:1px solid var(--borderc); }

  /* Sections */
  .h1 {
    font-family:'Noto Serif HK',serif;
    font-size:17px; font-weight:900; color:var(--blue);
    padding:7px 12px; margin:18px 0 10px;
    border-left:4px solid var(--gold); background:#FFFBEB;
  }
  .h2 {
    font-family:'Noto Serif HK',serif;
    font-size:14px; font-weight:700; color:var(--blue);
    margin:14px 0 6px; padding-bottom:3px; border-bottom:1px solid var(--borderc);
  }

  /* KP */
  .kp { margin:10px 0; padding:11px 14px; background:var(--lightbg); border:1px solid var(--borderc); border-radius:5px; }
  .kp-title { font-size:14px; font-weight:900; color:var(--blue); margin-bottom:4px; }
  .kp-rules { font-size:12px; line-height:1.7; }
  .kp-rules ol,.kp-rules ul { padding-left:18px; }

  /* Example */
  .ex { border:2px solid var(--gold); border-radius:7px; padding:11px 14px; margin:8px 0; background:#FFFDF5; }
  .ex-title { font-size:13px; font-weight:900; color:#92400E; margin-bottom:5px; }
  .ex-q { font-size:14px; font-weight:700; margin:5px 0; line-height:1.7; }

  /* Warn */
  .warn { background:#FEF2F2; border-left:3px solid var(--red); padding:6px 10px; margin:7px 0; font-size:12px; font-weight:600; color:#991B1B; }

  /* Mnemonic */
  .mn { background:linear-gradient(135deg,#FFF8E7,#FFEDD5); border:2px solid var(--gold); border-radius:7px; padding:10px 14px; margin:7px 0; text-align:center; font-size:15px; font-weight:900; color:var(--blue); }

  /* Tables */
  .qt { width:100%; border-collapse:collapse; margin:6px 0; font-size:12px; }
  .qt th { background:var(--blue); color:white; padding:5px 8px; font-size:11px; font-weight:600; text-align:left; }
  .qt td { padding:6px 8px; border:1px solid var(--borderc); vertical-align:top; }
  .qt tr:nth-child(even) td { background:#FAFBFC; }
  .qt .qn { width:34px; text-align:center; font-weight:700; }
  .qt .qd { width:52px; text-align:center; font-size:10px; font-weight:700; }
  .qt .qw {
    min-height:85px;
    background: repeating-linear-gradient(transparent,transparent 22px,#E5E7EB 22px,#E5E7EB 23px);
  }
  .qt .qtxt { font-size:13px; line-height:1.7; }
  .d1 { background:#FEF3C7; color:#92400E; }
  .d2 { background:#DCFCE7; color:#166534; }
  .d3 { background:#DBEAFE; color:#1E40AF; }
  .d4 { background:#F3E8FF; color:#7C3AED; }

  .ss { display:inline-block; padding:1px 5px; border-radius:2px; font-size:8px; font-weight:700; }
  .sh { background:#FEE2E2; color:#991B1B; }
  .sm { background:#FEF3C7; color:#92400E; }

  /* Trap compare */
  .tc { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:8px 0; }
  .tc-w { background:#FEF2F2; border:2px solid #FECACA; border-radius:8px; padding:14px; text-align:center; }
  .tc-r { background:#F0FDF4; border:2px solid #BBF7D0; border-radius:8px; padding:14px; text-align:center; }
  .tc-w .lbl { font-size:14px; font-weight:900; color:var(--red); margin-bottom:5px; }
  .tc-r .lbl { font-size:14px; font-weight:900; color:var(--green); margin-bottom:5px; }
  .tc-w .eq { font-size:17px; color:var(--red); }
  .tc-r .eq { font-size:17px; color:var(--green); }
  .tc-w .why { font-size:10px; color:#991B1B; margin-top:4px; }
  .tc-r .why { font-size:10px; color:#14532D; margin-top:4px; }

  .sc { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin:8px 0; }
  .sc-i { background:var(--lightbg); border:2px solid var(--borderc); border-radius:8px; padding:12px; text-align:center; }
  .sc-i .n { width:30px;height:30px;border-radius:50%; background:var(--blue); color:white; font-weight:900; font-size:16px; display:flex; align-items:center; justify-content:center; margin:0 auto 6px; }
  .sc-i .t { font-size:13px; font-weight:900; }
  .sc-i .d { font-size:10px; color:var(--gray); line-height:1.4; margin-top:2px; }

  .et { width:100%; border-collapse:collapse; margin:6px 0; font-size:11px; }
  .et th { background:var(--red); color:white; padding:5px 8px; }
  .et td { padding:5px 8px; border:1px solid var(--borderc); }

  /* SVG Geometry */
  .geom { text-align:center; margin:8px 0; }
  .geom svg { max-width:100%; }

  .end-note { text-align:center; margin-top:20px; padding-top:14px; border-top:1px solid var(--borderc); font-size:11px; color:var(--gray); }

  /* Exam-specific */
  .exam-header { background:var(--blue); color:white; text-align:center; padding:12px; border-radius:4px; margin-bottom:14px; }
  .exam-header .e-title { font-family:'Noto Serif HK',serif; font-size:18px; font-weight:900; }
  .score-box { border:2px solid var(--blue); display:inline-block; padding:8px 20px; text-align:center; margin:8px; }
  .score-box .sc-big { font-size:22px; font-weight:900; color:var(--blue); }
  .grade-table { width:100%; border-collapse:collapse; margin:8px 0; font-size:10px; }
  .grade-table th, .grade-table td { border:1px solid var(--borderc); padding:3px 6px; text-align:center; }
  .grade-table th { background:var(--blue); color:white; }
</style>
'''

FOOTER = '''<div class="end-note">
<p>霖楓學苑 · LF Academy · 不教數學，教避開陷阱。</p>
</div>'''

# ═══════════════════════════════════════════════
# HTML PAGE STRUCTURE HELPERS
# ═══════════════════════════════════════════════

def html_head(title, lesson_code):
    return f'''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson_code} {title}</title>
{CSS_COMMON}
</head>
<body>
<div class="container">
'''

def html_tail():
    return '''</div>
</body>
</html>'''

def cover_page(lesson_code, lesson_num, title, duration, traps, sspa, prerequisites, objectives):
    return f'''
<div class="pb cover-page cover">
  <div class="cv-logo">霖楓學苑 · LF Academy</div>
  <div class="cv-badge">小六 · 第{lesson_num}堂 · 學生版講義 v6</div>
  <div class="cv-title">{title}</div>
  <div class="cv-sub">P6 下學期 · {duration} · 一對三線上課程</div>

  <div class="cv-info">
    <b>核心陷阱：</b>{traps}<br>
    <b>SSPA 關聯：</b>{sspa}<br>
    <b>前置知識：</b>{prerequisites}<br>
    <b>本堂目標：</b>{objectives}
  </div>

  <div class="cv-row">
    <span>學生姓名：<span class="ln"></span></span>
    <span>班級：<span class="ln"></span></span>
    <span>日期：<span class="ln"></span></span>
    <span>完成時長：<span class="ln"></span></span>
  </div>
</div>
'''

def q_row(num, question, diff_class, diff_label, min_h=85):
    return f'''<tr><td class="qn">{num}</td><td class="qtxt">{question}</td><td class="qd {diff_class}">{diff_label}</td><td class="qw" style="min-height:{min_h}px;"></td></tr>'''

def h1(text):
    return f'<div class="h1">{text}</div>'

def h2(text):
    return f'<div class="h2">{text}</div>'

def kp_block(title_html, rules_html):
    return f'<div class="kp"><div class="kp-title">{title_html}</div><div class="kp-rules">{rules_html}</div></div>'

def ex_block(title, question):
    return f'<div class="ex"><div class="ex-title">{title}</div><div class="ex-q">{question}</div></div>'

def warn(text):
    return f'<div class="warn">⚠️ {text}</div>'

def mn(text):
    return f'<div class="mn">🧠 {text}</div>'

def pb_open():
    return '<div class="pb">'

def pb_close():
    return '</div>'

def page_break():
    return '<div class="page-break"></div>'

def sc_cards(steps):
    """steps = [(num, title, desc), ...] up to 4"""
    html = '<div class="sc">'
    for n, t, d in steps:
        html += f'<div class="sc-i"><div class="n">{n}</div><div class="t">{t}</div><div class="d">{d}</div></div>'
    html += '</div>'
    return html

def trap_compare(red_lbl, red_eq, red_why, green_lbl, green_eq, green_why):
    return f'''<div class="tc">
  <div class="tc-w"><div class="lbl">❌ {red_lbl}</div><div class="eq">{red_eq}</div><div class="why">{red_why}</div></div>
  <div class="tc-r"><div class="lbl">✅ {green_lbl}</div><div class="eq">{green_eq}</div><div class="why">{green_why}</div></div>
</div>'''

def error_table(errors):
    """errors = [(id, trap, symptom, cause, fix, prevention, severity), ...] 7 rows"""
    html = '''<table class="et"><tr><th>#</th><th>陷阱類型</th><th>錯誤症狀</th><th>根本原因</th><th>正確解法</th><th>預防方法</th><th>嚴重度</th></tr>'''
    for e in errors:
        html += '<tr>' + ''.join(f'<td>{c}</td>' for c in e) + '</tr>'
    html += '</table>'
    return html

def geom_div(svg_string):
    return f'<div class="geom">{svg_string}</div>'

def qtable(rows, headers=True):
    """rows = list of (num, question, diff_class, diff_label, min_h)"""
    html = '<table class="qt">'
    if headers:
        html += '<tr><th class="qn">#</th><th>題目</th><th class="qd">難度</th><th>作答區（寫出完整計算過程）</th></tr>'
    for r in rows:
        html += q_row(*r)
    html += '</table>'
    return html

def magic_box(text, color='blue'):
    """A highlighted insight box"""
    colors = {'blue':'#DBEAFE', 'red':'#FEE2E2', 'green':'#DCFCE7', 'yellow':'#FEF3C7'}
    return f'<div style="background:{colors.get(color,"#F9FAFB")};border:2px solid var(--borderc);border-radius:6px;padding:10px 14px;margin:8px 0;font-size:13px;text-align:center;font-weight:700;color:var(--blue);">{text}</div>'

# ═══════════════════════════════════════════════
# GENERATE SVGs
# ═══════════════════════════════════════════════

def gen_all_svgs():
    """Generate all SVGs needed across all 6 handouts."""
    svgs = {}

    # L29 SVGs
    svgs['displacement_1'] = displacement(150, 85, 28, 52, 42, 42)
    svgs['displacement_2'] = displacement(140, 80, 35, 60, 45, 40)
    svgs['cuboid_1'] = cuboid(130, 70, 75)
    svgs['cuboid_2'] = cuboid(100, 55, 60)
    svgs['composite_L_1'] = composite_L(60, 80, 80, 35)
    svgs['composite_T_1'] = composite_T(120, 30, 55, 55)
    svgs['composite_hole_1'] = composite_hole(130, 85, 50, 50)
    svgs['grid_diagram_1'] = grid_diagram(5, 3)

    # L30 SVGs (exam)
    svgs['circle_1'] = circle_shape(55)
    svgs['circle_2'] = circle_shape(50)
    svgs['trapezoid_1'] = trapezoid(80, 140, 75)
    svgs['rect_1'] = rectangle(140, 80)
    svgs['triangle_1'] = triangle(120, 80, 'right')
    svgs['triangle_2'] = triangle(100, 70, 'regular')
    svgs['bar_simple_1'] = bar_simple({'A':85, 'B':62, 'C':73, 'D':48, 'E':55}, title='', ylabel='分數', unit='分', ystep=20, bar_w=35, bar_gap=15, ymax=100)
    svgs['pie_1'] = pie_chart({'中文':120, '英文':100, '數學':80, '常識':60}, title='', radius=70)
    svgs['line_1'] = line_chart({'1月':30,'2月':45,'3月':55,'4月':42,'5月':68,'6月':80}, title='', ylabel='溫度', unit='°C', ystep=10, ymax=100)

    # L37 SVGs
    svgs['cuboid_3'] = cuboid(120, 60, 80)
    svgs['cuboid_4'] = cuboid(100, 50, 65)

    # L38 SVGs
    svgs['composite_L_2'] = composite_L(70, 90, 90, 40)
    svgs['pie_2'] = pie_chart({'數學':30,'英文':25,'中文':20,'其他':25}, title='', radius=65)

    # L39 SVGs
    # (no special diagrams needed beyond what's defined)

    # L40 SVGs
    # (no special diagrams needed beyond what's defined)

    # Custom SVGs for specific needs
    svgs['cross_section_demo'] = create_cross_section_svg()
    svgs['net_demo'] = create_net_svg()
    svgs['cylinder_demo'] = create_cylinder_svg()
    svgs['prism_demo'] = create_prism_svg()
    svgs['bridge_diagram'] = create_bridge_svg()
    svgs['growth_path'] = create_growth_path_svg()

    return svgs

def create_cross_section_svg():
    """Demonstrate cross-sections of a cylinder/cuboid at different angles."""
    w, h = 400, 320
    parts = []
    # Left: cuboid with vertical cut showing rectangle cross-section
    parts.append(_r(25, 60, 100, 80, f=C['fill'], st=C['fg'], sw=2))
    parts.append(_li(75, 40, 75, 160, st=C['red'], sw=2, da='6,3'))
    parts.append(_t(75, 175, '垂直切面：長方形', s=11, c=C['red']))
    # Right: cuboid with horizontal cut showing rectangle cross-section
    parts.append(_r(200, 60, 100, 80, f=C['fill2'], st=C['fg'], sw=2))
    parts.append(_li(180, 100, 320, 100, st=C['green'], sw=2, da='6,3'))
    parts.append(_t(250, 175, '水平切面：長方形', s=11, c=C['green']))
    # Labels
    parts.append(_t(75, 25, '立體截面示意圖', s=14, c=C['fg']))
    parts.append(_t(200, 210, '🪤 陷阱：切面形狀取決於切割方向！', s=12, c=C['red']))
    return _sv(w, h, ''.join(parts))

def create_net_svg():
    """Show a simple net/folding pattern example."""
    w, h = 380, 280
    parts = []
    # Draw a cross-shaped net (typical cube net)
    cell = 50
    # Bottom, front, top, back, right side
    positions = [(cell, cell*2), (cell, cell), (cell, 0), (cell, cell*3), (0, cell), (cell*2, cell)]
    colors = [C['fill'], C['fill2'], C['fill2'], C['fill'], C['fill3'], C['fill3']]
    labels = ['底', '前', '頂', '後', '左', '右']
    for i, ((x, y), col) in enumerate(zip(positions, colors)):
        parts.append(f'<rect x="{x+80}" y="{y+30}" width="{cell}" height="{cell}" fill="{col}" stroke="{C["fg"]}" stroke-width="2"/>')
        parts.append(_t(x+80+cell//2, y+30+cell//2+4, labels[i], s=11))
    parts.append(_t(190, 260, '摺紙圖樣（正方體展開圖）', s=12, c=C['fg']))
    parts.append(_t(190, 275, '🪤 陷阱：每個面都要對得上！', s=11, c=C['red']))
    return _sv(w, h, ''.join(parts))

def create_cylinder_svg():
    """Simple cylinder diagram."""
    w, h = 280, 260
    parts = []
    # Top ellipse
    parts.append(f'<ellipse cx="140" cy="60" rx="80" ry="25" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="2.5"/>')
    # Bottom ellipse (full)
    parts.append(f'<ellipse cx="140" cy="170" rx="80" ry="25" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="2.5"/>')
    # Sides
    parts.append(f'<line x1="60" y1="60" x2="60" y2="170" stroke="{C["fg"]}" stroke-width="2.5"/>')
    parts.append(f'<line x1="220" y1="60" x2="220" y2="170" stroke="{C["fg"]}" stroke-width="2.5"/>')
    # Radius label
    parts.append(_li(140, 60, 220, 60, st=C['red'], sw=2, da='4,2'))
    parts.append(_t(185, 50, 'r', s=13, c=C['red']))
    # Height
    parts.append(_li(235, 60, 235, 170, st=C['green'], sw=2, da='4,2'))
    parts.append(_t(250, 115, 'h', s=13, c=C['green']))
    # Labels
    parts.append(_t(140, 215, '圓柱體 Cylinder', s=13, c=C['fg']))
    parts.append(_t(140, 235, 'V=πr²h, 表面積=2πr²+2πrh', s=11, c=C['gray']))
    return _sv(w, h, ''.join(parts))

def create_prism_svg():
    """Triangular prism diagram."""
    w, h = 300, 260
    parts = []
    # Triangular prism - top face
    pts_top = '110,50 220,50 165,110'
    parts.append(f'<polygon points="{pts_top}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="2.5"/>')
    # Bottom face (offset)
    pts_bot = '110,140 220,140 165,200'
    parts.append(f'<polygon points="{pts_bot}" fill="#BFDBFE" stroke="{C["fg"]}" stroke-width="2.5"/>')
    # Connecting edges
    parts.append(_li(110, 50, 110, 140))
    parts.append(_li(220, 50, 220, 140))
    parts.append(_li(165, 110, 165, 200))
    # Height label
    parts.append(_li(230, 50, 230, 140, st=C['green'], sw=2, da='4,2'))
    parts.append(_t(245, 95, 'h', s=12, c=C['green']))
    # Base area
    parts.append(_t(165, 230, '三角柱 Prism — V=底面積×高', s=12, c=C['fg']))
    parts.append(_t(165, 248, '🪤 陷阱：「底」可以係任何形狀！先計底面積', s=10, c=C['red']))
    return _sv(w, h, ''.join(parts))

def create_bridge_svg():
    """Bridge diagram showing arithmetic → algebraic transition."""
    w, h = 500, 220
    parts = []
    # Left side: arithmetic
    parts.append(_r(20, 30, 180, 150, f=C['fill2'], st=C['green'], sw=2))
    parts.append(_t(110, 12, '小學算術思維', s=13, c=C['green']))
    parts.append(_t(110, 80, '搵答案 = 數字運算', s=12, c=C['fg']))
    parts.append(_t(110, 105, '一步一步計出黎', s=12, c=C['fg']))
    parts.append(_t(110, 130, '例：?+5=12 → ?=7', s=11, c=C['gray']))
    # Right side: algebraic
    parts.append(_r(290, 30, 180, 150, f=C['fill'], st=C['fg'], sw=2))
    parts.append(_t(380, 12, '中學代數思維', s=13, c=C['fg']))
    parts.append(_t(380, 80, '表達關係 = 變數等式', s=12, c=C['fg']))
    parts.append(_t(380, 105, '設未知數 → 列方程', s=12, c=C['fg']))
    parts.append(_t(380, 130, '例：x+5=12 → x=7', s=11, c=C['gray']))
    # Bridge
    parts.append(f'<polygon points="205,65 285,65 285,145 205,145" fill="{C["fill3"]}" stroke="{C["gold"]}" stroke-width="3"/>')
    parts.append(_t(245, 110, '過渡期', s=14, c=C['fg']))
    parts.append(_t(245, 160, '同一問題，兩種解法！', s=10, c=C['red']))
    return _sv(w, h, ''.join(parts))

def create_growth_path_svg():
    """Growth path / journey diagram for L40."""
    w, h = 500, 200
    parts = []
    points = [(60, 120), (180, 120), (300, 120), (420, 120)]
    labels = ['P3', 'P5', 'P6呈分', 'F1']
    colors = [C['fill3'], C['fill2'], C['fill'], '#DCFCE7']
    for i, ((x, y), lbl) in enumerate(zip(points, labels)):
        parts.append(f'<circle cx="{x}" cy="{y}" r="25" fill="{colors[i]}" stroke="{C["fg"]}" stroke-width="2.5"/>')
        parts.append(_t(x, y+5, lbl, s=11))
    # Connecting arrows
    for i in range(len(points)-1):
        parts.append(f'<line x1="{points[i][0]+25}" y1="{points[i][1]}" x2="{points[i+1][0]-25}" y2="{points[i+1][1]}" stroke="{C["gold"]}" stroke-width="3"/>')
        parts.append(f'<polygon points="{points[i+1][0]-30},{points[i+1][1]-6} {points[i+1][0]-30},{points[i+1][1]+6} {points[i+1][0]-22},{points[i+1][1]}" fill="{C["gold"]}"/>')
    parts.append(_t(250, 50, '數學成長之旅', s=16, c=C['fg']))
    parts.append(_t(250, 170, '每個階段都係新挑戰，但你都過到關！', s=11, c=C['gray']))
    return _sv(w, h, ''.join(parts))

# ═══════════════════════════════════════════════
# INDIVIDUAL HANDOUT GENERATORS
# ═══════════════════════════════════════════════

def gen_l29():
    """L29: 容量體積進階（排水法+溢出+立體截面）"""
    svgs = gen_all_svgs()
    lesson_code = "LF-P6-下-L29"
    title = "容量體積進階（排水法+溢出+立體截面）"
    lesson_num = 29
    filepath = os.path.join(OUTPUT_DIR, f"{lesson_code}_容量體積進階_排水法溢出截面.html")

    parts = [html_head(title, lesson_code)]

    # Cover
    parts.append(cover_page(lesson_code, lesson_num, title, '65 分鐘',
        '🪤 T1-T2-T4 排水法陷阱 — 60%學生直接用新水位×底面積！· 截面形狀取決於切割方向 · 摺紙圖樣每個面都要對得上',
        '<span class="ss sh">🔴 高頻</span> SSPA 呈分試必考，佔卷一約 8-12%，排水法應用題每年出現',
        '堂16（容量體積基礎）· 堂21（圓的認識）· 堂18（綜合圖表幾何測量）',
        '❶ 立體截面判斷 ❷ 摺紙圖樣辨認 ❸ 排水法進階 ❹ 溢出法多物體計算'))

    # Page 2: Warm-up
    parts.append(pb_open())
    parts.append(h1('一、熱身啟動題（共 5 題，5 分鐘）'))
    warmup_qs = [
        (1, '填滿 1 個長 20 cm、闊 15 cm、高 10 cm 的長方體容器需要多少 mL 的水？（1 cm³ = 1 mL）', 'd1', '🌱 基礎', 80),
        (2, '一個長方體魚缸長 50 cm、闊 30 cm，水位高 25 cm。魚缸內有多少 cm³ 的水？', 'd1', '🌱 基礎', 80),
        (3, '一塊不規則石頭放入盛滿水的容器中，溢出 350 mL 的水。石頭的體積是多少 cm³？', 'd2', '🌿 進階', 80),
        (4, '一個長方體容器底面積是 200 cm²，水位上升了 3 cm。放入的物體體積是多少？', 'd2', '🌿 進階', 80),
        (5, '畫出一個正方體的摺紙圖樣（展開圖），至少畫出 2 種不同的樣式。', 'd2', '🌿 進階', 100),
    ]
    parts.append(qtable(warmup_qs))

    # KP1: 立體截面
    parts.append(h1('二、核心知識精講 ＋ 例題練習'))
    parts.append(kp_block(
        '知識點一：立體截面 — 切落去係咩形狀？<span class="ss sh">🔴 SSPA 進階</span>',
        '''<ol>
<li><strong>截面定義：</strong>用一個平面去切一個立體，切面就是截面</li>
<li><strong>長方體截面：</strong>垂直切→長方形；水平切→長方形；斜切→平行四邊形或梯形</li>
<li><strong>圓柱截面：</strong>垂直切→長方形；水平切→圓形；斜切→橢圓形</li>
<li><strong>圓錐截面：</strong>水平切→圓形（大小不同）；垂直切→等腰三角形</li>
<li><strong>球體截面：</strong>任何方向切→圓形（圓的大小取決於離球心的距離）</li></ol>'''))
    parts.append(geom_div(svgs['cross_section_demo']))

    # Trap section for cross-section
    parts.append(ex_block('🪤 陷阱引爆例題：截面方向決定形狀！',
        '一個圓柱體，沿垂直方向切開，截面是什麼形狀？沿水平方向切開呢？'))
    parts.append(trap_compare(
        '常見錯誤：混淆截面',
        '圓柱垂直切→圓形（❌錯！）',
        '誤以為任意方向切圓柱都係圓形',
        '正確答案',
        '垂直切→長方形 | 水平切→圓形',
        '圓柱垂直切時切面穿過弧面，成長方形'))

    # KP2: 摺紙圖樣
    parts.append(kp_block(
        '知識點二：摺紙圖樣（展開圖/Net）<span class="ss sm">🟡 SSPA 中頻</span>',
        '''<ol>
<li><strong>正方體展開圖：</strong>共 11 種不同的展開方式（6個面，每個正方形）</li>
<li>辨認規則：摺起來後每個面都要對得上，不能重疊也不能有缺口</li>
<li><strong>長方體展開圖：</strong>3 對長方形，相對的面完全相同</li>
<li><strong>圓柱展開圖：</strong>1個長方形（側面）+ 2個圓形（上下底）</li></ol>'''))
    parts.append(geom_div(svgs['net_demo']))

    parts.append(warn('🪤 致命陷阱：摺紙圖樣必須每個面都對得上！摺起來後多一個面或少一個面都係錯。呈分試要逐一檢查每個面的相鄰關係。'))

    parts.append(mn('🧠 口訣：「截面方向決定形狀，摺紙圖樣面面俱到。切垂直睇側面，切水平睇底面。」'))

    # Cross-section practice
    parts.append(h2('知識點一＋二 同步練習'))
    cross_qs = [
        (6, '一個長方體（5cm×3cm×4cm），沿垂直於底面的方向切開，截面最大可能是什麼形狀？尺寸是多少？', 'd2', '🌿 進階', 85),
        (7, '一個圓錐體，從頂點垂直向下切到圓形底面，截面是什麼形狀？', 'd2', '🌿 進階', 80),
        (8, '以下哪一個不是正方體的展開圖？（A）十字形 6 個正方形（B）T 字形 6 個正方形（C）一字排開 7 個正方形（D）Z 字形 6 個正方形', 'd3', '🌳 挑戰', 80),
        (9, '畫出一個長方體（6cm×4cm×3cm）其中一種正確的展開圖，標明各面尺寸。', 'd3', '🌳 挑戰', 100),
    ]
    parts.append(qtable(cross_qs))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 3: KP3 - Displacement method
    parts.append(pb_open())

    parts.append(kp_block(
        '知識點三：排水法進階 — 多物體、多步驟<span class="ss sh">🔴 SSPA 必考</span>',
        '''<ol>
<li><strong>排水法原理：</strong>物體體積 = 上升水的體積 = 底面積 × 水位差</li>
<li><strong>多物體情況：</strong>逐一放入→每次水位上升的總和 = 所有物體總體積 ÷ 底面積</li>
<li><strong>不完全浸沒：</strong>如果物體沒有完全沉入水中，排水體積不等於物體體積（只計浸沒部分）</li>
<li><strong>取出物體：</strong>取出後水位下降的體積 = 被取出的物體體積</li>
<li><strong>公式：</strong>上升水位 = 物體體積 ÷ 底面積；物體體積 = 底面積 × 水位變化</li></ol>'''))
    parts.append(geom_div(svgs['displacement_1']))

    # Displacement examples
    parts.append(ex_block('例題 1（基礎排水法）',
        '一個長方體容器長 30 cm、闊 20 cm，初始水位 15 cm。放入一塊石頭後（完全浸沒），水位升至 19 cm。求石頭的體積。'))
    parts.append(ex_block('例題 2（多物體排水法）',
        '容器底面積 400 cm²，水位初始 10 cm。先後放入 A、B 兩個物體（皆完全浸沒），水位先升至 14 cm，再升至 17 cm。求 B 物體的體積。'))

    parts.append(trap_compare(
        '60% 學生犯的錯誤',
        '石頭體積 = 30×20×19 = 11400 cm³',
        '直接用新水位×底面積，忘記計算的是「整缸水」的體積！',
        '正確解法',
        '石頭體積 = 30×20×(19-15) = 2400 cm³',
        '用水位差 4 cm × 底面積！體積=底面積×水位變化'))

    parts.append(mn('🧠 口訣：「排水法求體積，唔係求總水體積！底面積乘水位差，升幾多乘幾多！」'))

    # Displacement practice
    parts.append(h2('知識點三 同步練習'))
    disp_qs = [
        (10, '長方體容器底面積 250 cm²，水位 8 cm。放入物體後水位升至 12 cm（完全浸沒）。物體體積 = ？', 'd2', '🌿 進階', 85),
        (11, '魚缸長 60 cm、闊 40 cm，水位 30 cm。放入 3 條金魚後，水位升至 30.5 cm。3 條金魚的總體積 = ？', 'd2', '🌿 進階', 85),
        (12, '容器底面積 300 cm²，初始水位 20 cm。放入 A 物後水位升到 24 cm；再放入 B 物後水位升到 27 cm。A 和 B 哪個體積大？大多少？', 'd3', '🌳 挑戰', 90),
        (13, '一個正方體容器邊長 20 cm，水位 15 cm。放入一個邊長 8 cm 的正方體鐵塊。鐵塊完全浸沒後，水位升高多少 cm？', 'd3', '🌳 挑戰', 90),
    ]
    parts.append(qtable(disp_qs))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 4: KP4 - Overflow + practice
    parts.append(pb_open())

    parts.append(kp_block(
        '知識點四：溢出法 — 當容器不夠裝的時候<span class="ss sm">🟡 SSPA 中高頻</span>',
        '''<ol>
<li><strong>溢出原理：</strong>當放入物體的體積 > 容器剩餘空間時，多出的水會溢出</li>
<li><strong>溢出體積 = </strong>物體體積 - 容器剩餘空間 = 物體體積 - 底面積×(容器高度 - 初始水位)</li>
<li><strong>多物體溢出：</strong>逐一放入，每次計算剩餘空間，若不足則溢出</li>
<li><strong>取出物體：</strong>取出物體後容器水位必然下降，不會溢出</li></ol>'''))

    parts.append(geom_div(svgs['displacement_2']))
    parts.append(geom_div(svgs['cuboid_1']))

    parts.append(ex_block('🪤 陷阱引爆例題（溢出計算）',
        '一個長方體容器長 25 cm、闊 20 cm、高 30 cm，初始水位 25 cm。放入一塊體積 3000 cm³ 的石頭（完全浸沒）。水會溢出嗎？溢出多少？'))
    parts.append(trap_compare(
        '常見錯誤：忘記計算剩餘空間',
        '直接計新水位 = 25+(3000÷500)=31cm > 30，所以溢出',
        '方向正確但漏計溢出量！',
        '正確解法',
        '剩餘空間=25×20×(30-25)=2500 cm³<br>溢出=3000-2500=500 cm³',
        '先計剩餘空間，再比較物體體積'))

    parts.append(h2('知識點四 同步練習'))
    overflow_qs = [
        (14, '容器長 40 cm、闊 30 cm、高 20 cm，水位 18 cm。放入體積 3000 cm³ 的物體後，會溢出多少 cm³ 的水？', 'd3', '🌳 挑戰', 90),
        (15, '魚缸長 50 cm、闊 30 cm、高 40 cm，水位 35 cm。先放入 A 物（體積 2000 cm³），再放入 B 物（體積 3500 cm³）。最終水位在哪裡？有沒有溢出？', 'd3', '🌳 挑戰', 100),
        (16, '容器底面積 200 cm²、高 25 cm，水位 20 cm。放入 5 個相同的球，每個體積 250 cm³。問有幾個球會導致溢出？', 'd4', '🏔️ 極限', 100),
    ]
    parts.append(qtable(overflow_qs))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 5: Tiered practice
    parts.append(pb_open())
    parts.append(h1('三、課堂分層同步練習'))
    parts.append(h2('🌱 基礎層（共 3 題，全體必做）'))
    basic_qs = [
        (17, '一個長方體容器長 20 cm、闊 15 cm，初始水位 10 cm。放入石頭（完全浸沒）後水位升到 13 cm。石頭體積 = ？', 'd1', '🌱 基礎', 85),
        (18, '一個正方體有 6 個面。它的展開圖最少由幾個正方形組成？', 'd1', '🌱 基礎', 80),
        (19, '一個圓柱體沿水平方向切開，截面是什麼形狀？', 'd1', '🌱 基礎', 80),
    ]
    parts.append(qtable(basic_qs))

    parts.append(h2('🌿 進階層（共 3 題）'))
    adv_qs = [
        (20, '容器底面積 180 cm²，初始水位 12 cm。放入物體後水位升到 16.5 cm。物體體積 = ？', 'd2', '🌿 進階', 85),
        (21, '下圖摺起來後能否成為一個正方體？為什麼？<br>（十字形 6 個正方形，上方多出 1 個正方形）', 'd2', '🌿 進階', 90),
        (22, '一個圓柱體（半徑 5 cm，高 12 cm）沿垂直方向切開。截面的長和寬各是多少？', 'd2', '🌿 進階', 85),
    ]
    parts.append(qtable(adv_qs))

    parts.append(h2('🌳 挑戰層（共 3 題）'))
    chal_qs = [
        (23, '魚缸長 80 cm、闊 50 cm、高 60 cm，裝了 <span class="f"><span class="n">3</span><span class="b"></span><span class="d">4</span></span> 的水。放入一個體積 15000 cm³ 的裝飾物。會溢出嗎？溢出多少？', 'd3', '🌳 挑戰', 100),
        (24, '容器底面積 400 cm²，高 30 cm。初始水位 25 cm。連續放入 A(2000 cm³)、B(1500 cm³)、C(800 cm³) 三個物體。每次放入後計算水位變化。最終有溢出嗎？', 'd3', '🌳 挑戰', 100),
        (25, '一個不規則容器，分為上、下兩部分（上下截面積不同）。已知截面形狀，如何計算物體體積？簡述你的方法。', 'd3', '🌳 挑戰', 100),
    ]
    parts.append(qtable(chal_qs))

    parts.append(h2('🏔️ 極限挑戰（共 2 題）'))
    ext_qs = [
        (26, '一個圓柱容器（半徑 10 cm，高 30 cm），初始水位 20 cm。放入一個半徑 4 cm 的鐵球（完全浸沒）。<br>(a) 水位升高多少 cm？（π=3.14，球體積=<span class="f"><span class="n">4</span><span class="b"></span><span class="d">3</span></span>πr³）<br>(b) 如果鐵球只浸沒了 <span class="f"><span class="n">3</span><span class="b"></span><span class="d">4</span></span>，水位變化如何？', 'd4', '🏔️ 極限', 110),
        (27, '一個容器裝滿水（長 30 cm、闊 20 cm、高 25 cm）。放入一個邊長 10 cm 的正方體鐵塊。鐵塊一半露出水面（鐵塊密度大於水，沉到底部但身高超過水位）。溢出了多少 cm³ 的水？', 'd4', '🏔️ 極限', 110),
    ]
    parts.append(qtable(ext_qs))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 6: Application problems
    parts.append(pb_open())
    parts.append(h1('四、SSPA 應用題訓練（共 5 題）'))

    app_qs = [
        (28, '【SSPA 真題改編】一個長方體水箱長 1.2 m、闊 0.8 m、高 0.6 m，裝了 <span class="f"><span class="n">2</span><span class="b"></span><span class="d">3</span></span> 的水。放入一個體積 0.15 m³ 的石像。問：<br>(a) 石像放入前水箱內有多少升水？（1 m³ = 1000 L）<br>(b) 石像放入後水位會溢出嗎？如會，溢出多少升？', 'd3', '🌳 挑戰', 110),
        (29, '【SSPA 真題】一個正方體容器邊長 30 cm，初始水位 25 cm。先放入邊長 5 cm 的正方體 A（完全浸沒），再放入邊長 4 cm 的正方體 B（完全浸沒）。求最終水位。', 'd3', '🌳 挑戰', 100),
        (30, '【SSPA 真題改編】一個圓柱形水桶（底半徑 15 cm，高 50 cm），初始水位 35 cm。放入一塊不規則石頭，水位升至 38 cm。求石頭體積。（π=3.14）', 'd3', '🌳 挑戰', 100),
        (31, '【課外延伸】一個正方體展開圖如右（十字形，上方多一個正方形，共 7 個正方形）。這個展開圖能摺成一個正方體嗎？請解釋原因。如果不能，應該如何修改？', 'd3', '🌳 挑戰', 100),
        (32, '【綜合難題】一個長方體容器長 50 cm、闊 40 cm、高 45 cm。初始水位 30 cm。操作過程：<br>① 放入石頭 A → 水位升到 33 cm<br>② 取出石頭 A → 水位回到 30 cm<br>③ 放入石頭 B → 水位升到 36 cm<br>④ 再放入石頭 A → 溢出？<br>求石頭 A 和 B 各自的體積，以及步驟④是否有溢出。', 'd4', '🏔️ 極限', 120),
    ]
    parts.append(qtable(app_qs))
    parts.append(pb_close())
    parts.append(page_break())

    # Page 7: Homework
    parts.append(pb_open())
    parts.append(h1('五、課後鞏固練習（家課）'))
    parts.append(h2('基礎鞏固（5+ 題，必做）'))
    hw_basic = [
        ('HW1', '容器底面積 150 cm²，水位 10 cm。放入石頭後水位升至 13 cm。石頭體積 = ？', 'd1', '🌱', 80),
        ('HW2', '一個正方體有 6 個正方形面，它的展開圖中正方形之間如何相連？寫出 2 種不同的展開圖排列方式。', 'd1', '🌱', 85),
        ('HW3', '容器長 30 cm、闊 20 cm，水位上升 4 cm。放入物的體積 = ？', 'd1', '🌱', 80),
        ('HW4', '圓柱沿水平方向切開，截面是什麼？沿垂直方向切開呢？', 'd1', '🌱', 80),
        ('HW5', '容器長 25 cm、闊 16 cm，初始水位 20 cm。放入物體後水位升至 24 cm。物體體積 = ？', 'd1', '🌱', 80),
    ]
    parts.append(qtable(hw_basic))

    parts.append(h2('進階挑戰（3+ 題）'))
    hw_adv = [
        ('HW6', '容器底面積 200 cm²、高 30 cm，水位 25 cm。放入體積 1500 cm³ 的物體。水會溢出嗎？溢出多少？', 'd2', '🌿', 90),
        ('HW7', '魚缸長 100 cm、闊 50 cm、高 60 cm，裝了 <span class="f"><span class="n">5</span><span class="b"></span><span class="d">6</span></span> 的水。放入體積 25000 cm³ 的假山。最終水位在哪？', 'd3', '🌳', 100),
        ('HW8', '一個不規則形狀的金屬物體放入盛滿水的容器中，溢出 480 mL 水。這個金屬物體的體積 = ？cm³', 'd2', '🌿', 85),
    ]
    parts.append(qtable(hw_adv))
    parts.append(pb_close())
    parts.append(page_break())

    # Page 8: Error table + Mnemonic + Strategy Cards + Footer
    parts.append(pb_open())
    parts.append(h1('六、常見錯誤辨析表（The Error Table）'))
    errors = [
        ('1', 'T1 — 單位混淆', 'cm³ vs mL vs L 不分', '未掌握 1cm³=1mL=0.001L', '換算後再代入公式', '做題前先統一單位', '🔴 高'),
        ('2', 'T2 — 公式代錯', '用新水位×底面積當物體體積', '混淆「整缸水體積」和「上升水體積」', '體積 = 底面積 × 水位差', '記口訣：升幾多乘幾多', '🔴 高'),
        ('3', 'T4 — 幾何混淆', '截面方向搞錯，垂直切圓柱以為是圓形', '未理解截面取決於切割角度', '垂直切圓柱→長方形，水平切→圓形', '畫圖輔助想像', '🟡 中'),
        ('4', 'T3 — 溢出計算遺漏', '忘記計算容器剩餘空間', '直接比較物體體積和容器體積', '溢出 = 物體體積 - 底面積×(高度-初始水位)', '先計剩餘空間再比較', '🔴 高'),
        ('5', 'T5 — 摺紙圖樣', '展開圖摺不起或面重疊', '未檢查各面的相鄰關係和數量', '6個正方形面每個都必須存在且不重疊', '逐一追蹤每個面摺起後的位置', '🟡 中'),
        ('6', 'T6 — 部分浸沒', '不完全浸沒時仍用物體全體積', '未注意「完全浸沒」的條件', '部分浸沒時只計算浸沒部分的排水', '讀題時圈出「完全浸沒」關鍵詞', '🔴 高'),
        ('7', 'T7 — 多物體次序', '取出後忘記水位會下降', '多步驟操作時未追蹤每次水位變化', '每次放入/取出後重新計算水位', '用表格記錄每一步後的水位', '🟡 中'),
    ]
    parts.append(error_table(errors))

    parts.append(mn('🧠 本堂核心口訣：「排水法：底面積乘水位差，升幾多乘幾多，唔係乘總水位！溢出法：先計剩餘空間，再減物體體積，唔夠裝先會漏！」'))
    parts.append(mn('🧠 截面口訣：「圓柱切垂直睇長方，切水平睇圓形。方向決定截面，想像把刀點樣切！」'))

    parts.append(h1('七、解題策略卡（4-Step Strategy Cards）'))
    parts.append(sc_cards([
        ('①', '讀題圈關鍵', '圈出容器尺寸、初始水位、物體體積、「完全浸沒」等關鍵詞'),
        ('②', '計剩餘空間', '剩餘空間 = 底面積 × (容器高度 - 當前水位)'),
        ('③', '比較判斷', '物體體積 vs 剩餘空間 → 決定溢出或不溢出'),
        ('④', '驗算單位', '檢查所有單位是否一致（cm, cm², cm³, mL, L）'),
    ]))

    parts.append(FOOTER.replace('LF-P6-下-LXX', lesson_code))
    parts.append(pb_close())

    parts.append(html_tail())

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))

    print(f"  [OK] L29 written: {filepath}")
    return filepath


def gen_l30():
    """L30: SSPA模擬4（第三次呈分試終極全真·75分鐘）"""
    svgs = gen_all_svgs()
    lesson_code = "LF-P6-下-L30"
    title = "SSPA模擬4（第三次呈分試終極全真·75分鐘）"
    lesson_num = 30
    filepath = os.path.join(OUTPUT_DIR, f"{lesson_code}_SSPA模擬4_終極全真.html")

    parts = [html_head(title, lesson_code)]

    # Cover (exam format)
    parts.append(f'''
<div class="pb cover-page cover">
  <div class="cv-logo">霖楓學苑 · LF Academy</div>
  <div class="cv-badge">小六 · 第{lesson_num}堂 · 全真模擬考試</div>
  <div class="cv-title">{title}</div>
  <div class="cv-sub">P6 下學期 · 75 分鐘 · 滿分 100 分 · 第三次呈分試格式</div>

  <div class="cv-info">
    <b>考試範圍：</b>L21-L29（圓面積、百分數應用、方程、圖表、速率、排水法、立體截面）<br>
    <b>考試格式：</b>Section A MC（10題×3分）＋ Section B 計算（8題×5分）＋ Section C 應用（3題×10分）<br>
    <b>陷阱分佈：</b>🪤 T1-T10 全覆蓋，模擬真卷陷阱密度<br>
    <b>目標：</b>80+ 分 = A grade · 65-79 分 = B grade · 50-64 分 = C grade
  </div>

  <div class="cv-row">
    <span>學生姓名：<span class="ln"></span></span>
    <span>班級：<span class="ln"></span></span>
    <span>日期：<span class="ln"></span></span>
    <span>得分：<span class="ln"></span></span>
  </div>
</div>
''')

    # Exam header
    parts.append(pb_open())
    parts.append('''<div class="exam-header">
  <div class="e-title">SSPA 模擬考試（四）— 第三次呈分試終極全真</div>
  <p style="font-size:11px; margin-top:4px;">時間：75 分鐘 | 滿分：100 分 | 共三部分</p>
</div>''')

    # Section A: MC
    parts.append(h1('Section A：多項選擇題 Multiple Choice（10 題 × 3 分 = 30 分）'))
    parts.append('<p style="color:var(--gray);font-size:10px;">指示：選出正確答案，把答案字母填在右邊方格內。每題只有一個正確答案。</p>')

    mc_qs = [
        ('A1', '一個圓的半徑是 7 cm，它的面積是？（π = <span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>）<br>A. 44 cm²&nbsp;&nbsp;B. 154 cm²&nbsp;&nbsp;C. 308 cm²&nbsp;&nbsp;D. 616 cm²', 'd2', '🌿', 55),
        ('A2', '一件商品標價 $250，打八折後再減 $20，最終售價是？<br>A. $160&nbsp;&nbsp;B. $170&nbsp;&nbsp;C. $180&nbsp;&nbsp;D. $200', 'd2', '🌿', 55),
        ('A3', '解方程：3(x + 2) = 21，x = ？<br>A. 3&nbsp;&nbsp;B. 5&nbsp;&nbsp;C. 6&nbsp;&nbsp;D. 7', 'd2', '🌿', 55),
        ('A4', '以下哪一個是正方體的正確展開圖？<br>A. 7個正方形排成一字形&nbsp;&nbsp;B. 5個正方形十字形&nbsp;&nbsp;C. 6個正方形十字形（上1中4下1）&nbsp;&nbsp;D. 3個正方形三角形排列', 'd3', '🌳', 55),
        ('A5', '一個長方體容器底面積 200 cm²，水位從 15 cm 升至 21 cm。放入物體的體積是？<br>A. 1200 cm³&nbsp;&nbsp;B. 1800 cm³&nbsp;&nbsp;C. 3000 cm³&nbsp;&nbsp;D. 4200 cm³', 'd2', '🌿', 55),
        ('A6', '小明以 60 km/h 行駛 2 小時，再以 80 km/h 行駛 1.5 小時。總行程距離 = ？<br>A. 180 km&nbsp;&nbsp;B. 210 km&nbsp;&nbsp;C. 240 km&nbsp;&nbsp;D. 270 km', 'd3', '🌳', 55),
        ('A7', '一個圓柱體沿垂直方向切開，截面是？<br>A. 圓形&nbsp;&nbsp;B. 橢圓形&nbsp;&nbsp;C. 長方形&nbsp;&nbsp;D. 三角形', 'd2', '🌿', 55),
        ('A8', '半圓的半徑是 10 cm，它的周長是？（π = 3.14）<br>A. 31.4 cm&nbsp;&nbsp;B. 41.4 cm&nbsp;&nbsp;C. 51.4 cm&nbsp;&nbsp;D. 62.8 cm', 'd3', '🌳', 55),
        ('A9', '圖中複合圖形由一個長方形和一個半圓組成。長方形長 14 cm、闊 10 cm，半圓的直徑等於長方形的闊。整個圖形的面積約是？<br>A. 140 cm²&nbsp;&nbsp;B. 179 cm²&nbsp;&nbsp;C. 219 cm²&nbsp;&nbsp;D. 240 cm²', 'd4', '🏔️', 55),
        ('A10', '一個圓的圓周是 62.8 cm，它的面積是？（π = 3.14）<br>A. 125.6 cm²&nbsp;&nbsp;B. 314 cm²&nbsp;&nbsp;C. 628 cm²&nbsp;&nbsp;D. 942 cm²', 'd3', '🌳', 55),
    ]
    parts.append(qtable(mc_qs))

    # Score boxes for Section A
    parts.append('<div style="text-align:right;margin:8px 0;">Section A 得分：<span style="display:inline-block;width:60px;border-bottom:1px solid var(--borderc);"></span> / 30</div>')

    parts.append(pb_close())
    parts.append(page_break())

    # Section B: Calculation
    parts.append(pb_open())
    parts.append(h1('Section B：計算題 Calculation（8 題 × 5 分 = 40 分）'))
    parts.append('<p style="color:var(--gray);font-size:10px;">指示：寫出所有計算步驟。只寫答案不給步驟分。每題步驟 3 分，答案 2 分。</p>')

    calc_qs = [
        ('B1', '計算以下利潤問題：成本 $320，以賺 25% 的價格出售。售價是多少？如果之後打九折，最終利潤率是多少？', 'd2', '🌿', 95),
        ('B2', '解方程組：<br>2x + y = 13<br>x - y = 2<br>求 x 和 y 的值。', 'd3', '🌳', 95),
        ('B3', '一個複合圓形由一個大半圓和一個小半圓組成（如圖）。大半圓半徑 8 cm，小半圓半徑 4 cm。求整個圖形的面積和周長。（π = 3.14）', 'd3', '🌳', 100),
        ('B4', '圓形圖顯示 40 名學生的課外活動選擇：足球 35%、籃球 25%、游泳 20%、其他 20%。<br>(a) 各項活動各有多少人選擇？<br>(b) 足球比籃球多多少人？', 'd2', '🌿', 95),
        ('B5', '一個長方體容器長 40 cm、闊 25 cm、高 30 cm。初始水位 20 cm。放入一個體積 5000 cm³ 的物體（完全浸沒）。<br>(a) 有水溢出嗎？如有，溢出多少？<br>(b) 如果沒有溢出，最終水位是多少？', 'd3', '🌳', 100),
        ('B6', '甲、乙兩車同時從 A、B 兩地相向而行。甲車速率 70 km/h，乙車速率 50 km/h。兩地相距 360 km。<br>(a) 幾小時後兩車相遇？<br>(b) 相遇時甲車行了多少 km？', 'd3', '🌳', 95),
        ('B7', '一個圓的半徑是 r cm。如果半徑增加 50%，新圓的面積是原來圓面積的多少倍？', 'd3', '🌳', 90),
        ('B8', '一個正方體（邊長 10 cm）放在一個長方體容器（長50cm、闊40cm、高25cm，初始水位15cm）中完全浸沒。求水位上升的高度。', 'd2', '🌿', 90),
    ]
    parts.append(qtable(calc_qs))

    # Diagrams for B3 and B4
    parts.append(geom_div(svgs['circle_1']))
    parts.append('<p style="text-align:center;font-size:10px;color:var(--gray);">（B3 參考圖：複合半圓形）</p>')
    parts.append(geom_div(svgs['pie_1']))
    parts.append('<p style="text-align:center;font-size:10px;color:var(--gray);">（B4 參考圖：課外活動圓形圖）</p>')

    parts.append('<div style="text-align:right;margin:8px 0;">Section B 得分：<span style="display:inline-block;width:60px;border-bottom:1px solid var(--borderc);"></span> / 40</div>')

    parts.append(pb_close())
    parts.append(page_break())

    # Section C: Application
    parts.append(pb_open())
    parts.append(h1('Section C：應用題 Application（3 題 × 10 分 = 30 分）'))
    parts.append('<p style="color:var(--gray);font-size:10px;">指示：詳細寫出解題過程。步驟分：列式 3 分、計算 4 分、答案 2 分、驗算 1 分。</p>')

    app_qs_exam = [
        ('C1', '【綜合應用：百分數＋圓面積＋排水法】<br>一個圓柱形水箱（底半徑 20 cm，高 80 cm）裝了 75% 的水。放入一個半徑 8 cm 的實心鐵球（完全浸沒）。（取 π = 3.14，球體公式 V=<span class="f"><span class="n">4</span><span class="b"></span><span class="d">3</span></span>πr³）<br>(a) 水箱原有水多少 cm³？（2分）<br>(b) 鐵球體積是多少？（2分）<br>(c) 放入鐵球後水位升高多少 cm？（3分）<br>(d) 水會溢出嗎？如有，溢出多少 cm³？（3分）', 'd4', '🏔️', 150),
        ('C2', '【綜合應用：速率＋圖表＋方程】<br>下圖顯示一輛車從 A 城到 C 城的行程（經 B 城停留）。<br>A→B：120 km，速率 80 km/h<br>B 停留：30 分鐘<br>B→C：速率 60 km/h，比 A→B 多用 30 分鐘<br>(a) A→B 用了多少時間？（2分）<br>(b) B→C 的距離是多少？（3分）<br>(c) 全程平均速率是多少 km/h？（3分）<br>(d) 如果全程用 x km/h 的均速行駛，總時間不變。列出方程並求解 x。（2分）', 'd4', '🏔️', 150),
        ('C3', '【綜合應用：立體截面＋摺紙圖樣＋複合體積】<br>一個正方體紙盒（邊長 12 cm），沿對角線切開。求：<br>(a) 切開後的截面是什麼形狀？畫出並標明尺寸。（3分）<br>(b) 切開後得到的兩個立體各是什麼形狀？每個的體積是多少？（3分）<br>(c) 畫出這個正方體的一種正確展開圖（標明各邊尺寸）。（2分）<br>(d) 如果把這個切開的半個正方體（三角柱）放入一個長 20 cm、闊 15 cm、水位 10 cm 的水箱中完全浸沒，水位會升到多少？（2分）', 'd4', '🏔️', 150),
    ]
    parts.append(qtable(app_qs_exam))

    parts.append('<div style="text-align:right;margin:8px 0;">Section C 得分：<span style="display:inline-block;width:60px;border-bottom:1px solid var(--borderc);"></span> / 30</div>')

    # Total score
    parts.append('''<div style="text-align:center;margin:16px 0;padding:14px;background:var(--lightbg);border:2px solid var(--borderc);border-radius:8px;">
  <div style="font-size:16px;font-weight:900;color:var(--blue);margin-bottom:8px;">總分 Summary</div>
  <div style="display:flex;justify-content:center;gap:24px;font-size:12px;">
    <span>Section A：<span class="ln" style="width:50px;"></span>/30</span>
    <span>Section B：<span class="ln" style="width:50px;"></span>/40</span>
    <span>Section C：<span class="ln" style="width:50px;"></span>/30</span>
    <span style="font-weight:900;">總分：<span class="ln" style="width:50px;"></span>/100</span>
  </div>
</div>''')

    # Grade band table
    parts.append('''<table class="grade-table">
  <tr><th>等級 Grade</th><th>分數範圍</th><th>SSPA 對應</th><th>建議</th></tr>
  <tr><td style="background:#DCFCE7;">A（優異）</td><td>85-100</td><td>Band 1 穩入</td><td>保持水準，重點攻克極限題</td></tr>
  <tr><td style="background:#F0FDF4;">B（良好）</td><td>70-84</td><td>Band 1 邊緣</td><td>複習陷阱題，提升應用題</td></tr>
  <tr><td style="background:#FEF3C7;">C（合格）</td><td>55-69</td><td>Band 2 穩入</td><td>強化基礎計算，多做 MC</td></tr>
  <tr><td style="background:#FEF2F2;">D（待改善）</td><td>40-54</td><td>Band 2-3 之間</td><td>回歸基本概念，大量基礎練習</td></tr>
  <tr><td style="background:#FEE2E2;">E（需努力）</td><td>0-39</td><td>需要大幅改善</td><td>建議 1 對 1 補底，重溫核心 KP</td></tr>
</table>''')

    parts.append('<p style="text-align:center;font-size:16px;font-weight:900;color:var(--blue);margin:16px 0;font-family:Noto Serif HK,serif;">— 全卷完 —</p>')

    parts.append(pb_close())
    parts.append(page_break())

    # Answer page placeholder
    parts.append(pb_open())
    parts.append(h1('模擬考試 — 答案參考（課堂檢討用）'))
    parts.append('<table class="qt"><tr><th class="qn">題號</th><th>答案</th><th>分數</th><th>陷阱備註</th></tr>')
    answers = [
        ('A1', 'B (154 cm²)', '3', 'πr² 不是 2πr'),
        ('A2', 'C ($180)', '3', '八折=×0.8，不要用 1-0.8'),
        ('A3', 'B (x=5)', '3', '先展開括號'),
        ('A4', 'C (十字形6面)', '3', '7個面不可能摺成立方體'),
        ('A5', 'A (1200 cm³)', '3', '用 (21-15) 不是直接用 21'),
        ('A6', 'C (240 km)', '3', '2×60=120, 1.5×80=120'),
        ('A7', 'C (長方形)', '3', '垂直切圓柱=長方形截面'),
        ('A8', 'C (51.4 cm)', '3', 'πr+2r=31.4+20=51.4'),
        ('A9', 'B (約179 cm²)', '3', '矩形+半圓面積'),
        ('A10', 'B (314 cm²)', '3', '先由C求r, 再求A'),
    ]
    for a in answers:
        parts.append(f'<tr><td class="qn">{a[0]}</td><td>{a[1]}</td><td>{a[2]}</td><td>{a[3]}</td></tr>')
    parts.append('</table>')

    parts.append(FOOTER.replace('LF-P6-下-LXX', lesson_code))
    parts.append(pb_close())

    parts.append(html_tail())

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))

    print(f"  [OK] L30 written: {filepath}")
    return filepath


def gen_l37():
    """L37: 中一預習：面積體積公式擴展（棱柱+圓柱）"""
    svgs = gen_all_svgs()
    lesson_code = "LF-P6-下-L37"
    title = "中一預習：面積體積公式擴展（棱柱+圓柱）"
    lesson_num = 37
    filepath = os.path.join(OUTPUT_DIR, f"{lesson_code}_中一預習面積體積公式擴展.html")

    parts = [html_head(title, lesson_code)]

    parts.append(cover_page(lesson_code, lesson_num, title, '65 分鐘',
        '🪤 T2 圓柱表面積忘加兩個圓面！· T4 棱柱「底」可以是任何形狀 · T1 單位換算陷阱 cm³↔m³↔L↔mL',
        '<span class="ss sh">🔴 中一必備</span> 中一上學期首兩個月核心內容，預習後輕鬆銜接',
        '堂16（容量體積基礎）· 堂21-22（圓周圓面積）· 堂29（排水法進階）',
        '❶ 棱柱體積=底面積×高 ❷ 圓柱體積=πr²h ❸ 圓柱表面積 ❹ 單位進階換算'))

    # Page 2: Warm-up
    parts.append(pb_open())
    parts.append(h1('一、熱身啟動題（共 5 題，5 分鐘）'))
    warmup = [
        (1, '長方體體積公式是？底面積和高的關係是什麼？', 'd1', '🌱 基礎', 80),
        (2, '計算圓面積：半徑 = 5 cm，面積 = ？（π = 3.14）', 'd1', '🌱 基礎', 80),
        (3, '1 m³ = 多少 cm³？（請寫出換算過程）', 'd1', '🌱 基礎', 80),
        (4, '一個長方體的長=8 cm、闊=5 cm、高=10 cm。它的體積=？表面積=？', 'd2', '🌿 進階', 85),
        (5, '一個圓的直徑=14 cm，圓周=？圓面積=？（π = <span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>）', 'd2', '🌿 進階', 85),
    ]
    parts.append(qtable(warmup))

    # KP1: Prism
    parts.append(h1('二、核心知識精講 ＋ 例題練習'))

    parts.append(kp_block(
        '知識點一：棱柱（角柱）— 體積 = 底面積 × 高 <span class="ss sh">🔴 中一核心</span>',
        '''<ol>
<li><strong>棱柱定義：</strong>兩個底面全等且平行，側面為長方形的立體</li>
<li><strong>體積公式：V = 底面積 × 高</strong>（無論底是什麼形狀！）</li>
<li>三角柱：底面積 = <span class="f"><span class="n">1</span><span class="b"></span><span class="d">2</span></span> × b × h<sub>三角</sub>，V = 底面積 × 柱高</li>
<li>梯形柱：底面積 = <span class="f"><span class="n">(a+b)×h<sub>梯形</sub></span><span class="b"></span><span class="d">2</span></span>，V = 底面積 × 柱高</li>
<li><strong>關鍵：</strong>先找出或計算底面面積，再乘以柱體高度</li></ol>'''))
    parts.append(geom_div(svgs['prism_demo']))

    parts.append(ex_block('例題 1（三角柱體積）',
        '一個三角柱的底面是直角三角形（兩條直角邊分別為 6 cm 和 8 cm），柱體高度為 15 cm。求該三角柱的體積。'))
    parts.append(ex_block('例題 2（梯形柱體積）',
        '一個梯形柱的底面是梯形（上底 4 cm、下底 10 cm、梯形高 5 cm），柱體高度為 12 cm。求體積。'))

    parts.append(trap_compare(
        '常見錯誤：混淆「底面高」和「柱體高」',
        'V = <span class="f"><span class="n">1</span><span class="b"></span><span class="d">2</span></span>×(6+8)×15 = 105 cm³',
        '直接用兩邊長度當成底和高，忘記這不是三角形面積',
        '正確：V=底面積×柱高',
        'V = <span class="f"><span class="n">1</span><span class="b"></span><span class="d">2</span></span>×6×8×15 = 360 cm³',
        '底面積 = 三角形面積 = 1/2 × b × h，再 × 柱高'))

    # KP2: Cylinder
    parts.append(kp_block(
        '知識點二：圓柱體 — 體積與表面積 <span class="ss sh">🔴 中一必考</span>',
        '''<ol>
<li><strong>體積公式：</strong>V = π × r² × h（底面積 πr² 乘以高）</li>
<li><strong>表面積公式：</strong>總表面積 = 2πr²（兩個圓面）＋ 2πrh（側面展開為長方形）</li>
<li><strong>側面積：</strong>側面展開 = 圓周 × 高 = 2πr × h</li>
<li><strong>🪤 最大陷阱：</strong>表面積 = <strong>兩個圓面 + 側面</strong>，不是一個圓面！許多學生忘記加頂部圓面。</li></ol>'''))
    parts.append(geom_div(svgs['cylinder_demo']))

    parts.append(ex_block('例題 3（圓柱體積）',
        '一個圓柱體的底半徑為 7 cm，高為 20 cm。求它的體積。（π = <span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>）'))
    parts.append(ex_block('例題 4（圓柱表面積 — 陷阱題）',
        '一個圓柱的底半徑為 5 cm，高為 12 cm。求它的總表面積。（π = 3.14）'))

    parts.append(trap_compare(
        '最高頻錯誤：忘加頂部圓面！',
        '表面積 = πr² + 2πrh = 78.5 + 376.8 = 455.3 cm²',
        '只計了一個底面 + 側面，忘記圓柱有頂和底兩個圓面',
        '正確：圓柱總表面積',
        '表面積 = 2πr² + 2πrh = 157 + 376.8 = 533.8 cm²',
        '2πr² = 兩個圓面（頂+底），不是一個！'))

    parts.append(mn('🧠 「圓柱表面積，上下兩個圓，加埋側面長方形。2πr² 加 2πrh，唔好漏咗個頂！」'))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 3: Practice + KP3
    parts.append(pb_open())

    parts.append(h2('知識點一＋二 同步練習'))
    kp_prac = [
        (6, '三角柱：底面三角形 b=10 cm, h=6 cm，柱高=8 cm。體積 = ？', 'd2', '🌿 進階', 85),
        (7, '梯形柱：底面梯形 a=5 cm, b=11 cm, 梯形h=4 cm，柱高=10 cm。體積 = ？', 'd2', '🌿 進階', 85),
        (8, '圓柱：r=7 cm, h=15 cm。體積 = ？（π=<span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>）', 'd2', '🌿 進階', 85),
        (9, '圓柱：r=6 cm, h=10 cm。總表面積 = ？（π=3.14）', 'd3', '🌳 挑戰', 90),
    ]
    parts.append(qtable(kp_prac))

    # KP3: Composite 3D
    parts.append(kp_block(
        '知識點三：複合立體體積 — 拆解 + 組合 <span class="ss sm">🟡 中一進階</span>',
        '''<ol>
<li>複合立體的體積 = 各部分體積之和（或差）</li>
<li>拆解策略：將複合體拆成 2-3 個基本立體（棱柱、圓柱、長方體等）</li>
<li>常見複合：圓柱＋長方體、三角柱＋長方體、兩個不同棱柱的組合</li>
<li><strong>中空物體：</strong>總體積 = 外部體積 - 中空部分體積</li></ol>'''))

    parts.append(geom_div(svgs['composite_L_1']))

    parts.append(ex_block('例題 5（複合體積）',
        '一個複合立體由一個長方體（長15cm、闊10cm、高8cm）和一個放在上面的三角柱（底為直角三角形，兩邊6cm和8cm，柱長10cm）組成。求總體積。'))
    parts.append(ex_block('例題 6（中空圓柱）',
        '一個圓柱形管道的內半徑為 4 cm，外半徑為 5 cm，長度為 30 cm。求管道的材料體積。（π=3.14）'))

    parts.append(h2('知識點三 同步練習'))
    comp_qs = [
        (10, '一個複合體由邊長 10 cm 的正方體和放在上面的半徑 5 cm、高 8 cm 的圓柱組成。求總體積。（π=3.14）', 'd3', '🌳 挑戰', 95),
        (11, '一個中空長方體外尺寸 20×15×10 cm，內中空部分 14×9×8 cm。求材料體積。', 'd3', '🌳 挑戰', 90),
        (12, '一個 L 形棱柱的底面為 L 形（參考上圖），柱高為 10 cm。求體積。', 'd3', '🌳 挑戰', 90),
        (13, '一個複合體由三角柱（底三角形面積 24 cm²，柱高 6 cm）放在長方體（8×5×3 cm）上。總體積 = ？', 'd2', '🌿 進階', 85),
    ]
    parts.append(qtable(comp_qs))

    # KP4: Unit conversion
    parts.append(kp_block(
        '知識點四：單位換算進階 — 同單位才能乘！<span class="ss sm">🟡 SSPA 中頻</span>',
        '''<ol>
<li><strong>長度：</strong>1 m = 100 cm，1 cm = 10 mm</li>
<li><strong>面積：</strong>1 m² = 10000 cm²（100 × 100）</li>
<li><strong>體積：</strong>1 m³ = 1,000,000 cm³（100 × 100 × 100）</li>
<li><strong>容量：</strong>1 L = 1000 mL = 1000 cm³，1 m³ = 1000 L</li>
<li><strong>🪤 終極陷阱：</strong>所有維度必須用同一單位才能相乘！例如長用 m、闊用 cm → 先統一為 cm 或 m。</li></ol>'''))

    parts.append(warn('🪤 致命陷阱：體積換算時 m³ 轉 cm³ 是 ×1,000,000（一百萬），不是 ×100！因為 1 m³ = 100 cm × 100 cm × 100 cm。'))

    parts.append(mn('🧠 「單位換算三分類：長度百倍、面積萬倍、體積百萬倍！m轉cm乘100，m²轉cm²乘10000，m³轉cm³乘1000000！」'))

    parts.append(h2('知識點四 同步練習'))
    unit_qs = [
        (14, '換算：3.5 m³ = ？cm³', 'd2', '🌿 進階', 80),
        (15, '換算：4500000 cm³ = ？m³', 'd2', '🌿 進階', 80),
        (16, '一個長方體 2 m × 1.5 m × 0.8 m，體積 = ？L（1 m³ = 1000 L）', 'd2', '🌿 進階', 80),
        (17, '一個長方體長 1.2 m、闊 80 cm、高 0.5 m。體積 = ？cm³', 'd3', '🌳 挑戰', 85),
    ]
    parts.append(qtable(unit_qs))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 4: Tiered practice
    parts.append(pb_open())
    parts.append(h1('三、課堂分層同步練習'))
    parts.append(h2('🌱 基礎層（共 3 題）'))
    basic = [
        (18, '三角柱：底三角形面積 30 cm²，柱高 12 cm。V = ？', 'd1', '🌱 基礎', 80),
        (19, '圓柱：r=3 cm, h=10 cm。V = ？（π=3.14）', 'd1', '🌱 基礎', 80),
        (20, '2.5 L = ？cm³', 'd1', '🌱 基礎', 80),
    ]
    parts.append(qtable(basic))

    parts.append(h2('🌿 進階層（共 3 題）'))
    adv = [
        (21, '六角柱：底面正六邊形面積 64 cm²，柱高 15 cm。V = ？', 'd2', '🌿 進階', 85),
        (22, '圓柱 r=5 cm, h=8 cm。求側面積和總表面積。（π=3.14）', 'd2', '🌿 進階', 90),
        (23, '一個容器由半徑 10 cm 的圓柱（高 20 cm）和圓柱上方的半個球體組成。假設球體積不用計算，只求圓柱部分體積。（π=3.14）', 'd2', '🌿 進階', 90),
    ]
    parts.append(qtable(adv))

    parts.append(h2('🌳 挑戰層（共 3 題）'))
    chal = [
        (24, '一個中空圓柱（內 r=3 cm, 外 R=5 cm, 高 12 cm）。求材料體積。（π=3.14）', 'd3', '🌳 挑戰', 95),
        (25, '一個複合體由底層長方體（20×12×5 cm）和上層三角柱（底三角形=右三角形 8-6-10，柱長=12 cm）組成。總體積 = ？', 'd3', '🌳 挑戰', 100),
        (26, '圓柱 A（r=4 cm, h=10 cm）vs 圓柱 B（r=8 cm, h=2.5 cm）。哪個體積較大？大多少 %？（π=3.14）', 'd3', '🌳 挑戰', 100),
    ]
    parts.append(qtable(chal))

    parts.append(h2('🏔️ 極限挑戰（共 2 題）'))
    ext = [
        (27, '一個複合體由底層圓柱（r=10 cm, h=5 cm）、中層正方體（邊長 14 cm）、頂層三角柱（底為等邊三角形面積 43.3 cm²，柱高 14 cm）組成。總體積 = ？（π=3.14）', 'd4', '🏔️ 極限', 110),
        (28, '一個圓柱形水箱（r=20 cm, h=50 cm）裝了 80% 的水。放入一個實心圓柱（r=8 cm, h=15 cm）完全浸沒。水位上升多少 cm？（π=3.14）', 'd4', '🏔️ 極限', 110),
    ]
    parts.append(qtable(ext))
    parts.append(pb_close())
    parts.append(page_break())

    # Page 5: Application + Homework
    parts.append(pb_open())
    parts.append(h1('四、SSPA + 中一銜接應用題（共 5 題）'))
    app = [
        (29, '【中一真題型】一個三角柱容器（底為直角三角形：兩直角邊 15 cm 和 20 cm，柱高 30 cm）。問：<br>(a) 底面面積是多少？<br>(b) 容器能裝多少 mL 的水？<br>(c) 如果倒入 3000 mL 水，水位會有多高？', 'd3', '🌳 挑戰', 110),
        (30, '【中一真題型】一個圓柱形水桶（r=14 cm, h=40 cm），裝了 <span class="f"><span class="n">3</span><span class="b"></span><span class="d">4</span></span> 的水。（π=<span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>）<br>(a) 水桶內有多少 L 水？（1 L = 1000 cm³）<br>(b) 如果把水全部倒入一個正方體容器（邊長 25 cm），正方體容器能裝得下嗎？如果不能，會溢出多少 L？', 'd4', '🏔️ 極限', 120),
        (31, '【中一真題型】一個複合立體由圓柱（r=5 cm, h=10 cm）和放在上面的圓錐（相同半徑 r=5 cm, h=6 cm）組成。（圓錐體公式 V=<span class="f"><span class="n">1</span><span class="b"></span><span class="d">3</span></span>πr²h）求總體積。（π=3.14）', 'd4', '🏔️ 極限', 110),
        (32, '【單位換算挑戰】一個游泳池長 25 m、闊 10 m、平均水深 1.5 m。如果用一個容量 500 L 的水桶加水，最少需要多少桶才能裝滿游泳池？', 'd3', '🌳 挑戰', 100),
        (33, '【設計題】你需要設計一個容量為 1000 cm³ 的圓柱形容器。如果半徑選為 5 cm，高度應該是多少？（π=3.14，答案取至整數 cm）', 'd3', '🌳 挑戰', 100),
    ]
    parts.append(qtable(app))

    parts.append(h1('五、課後鞏固練習（家課）'))
    parts.append(h2('基礎鞏固（5+ 題）'))
    hwb = [
        ('HW1', '三角柱：b=12 cm, h=5 cm（三角形高），柱高=8 cm。體積 = ？', 'd1', '🌱', 80),
        ('HW2', '圓柱：r=7 cm, h=20 cm。體積 = ？（π=<span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>）', 'd1', '🌱', 80),
        ('HW3', '圓柱：r=4 cm, h=15 cm。側面積 = ？總表面積 = ？（π=3.14）', 'd1', '🌱', 85),
        ('HW4', '換算：5000000 cm³ = ？m³ = ？L', 'd1', '🌱', 80),
        ('HW5', '長方體 80cm × 50cm × 40cm。體積 = ？cm³ = ？L', 'd1', '🌱', 80),
    ]
    parts.append(qtable(hwb))

    parts.append(h2('進階挑戰（3+ 題）'))
    hwa = [
        ('HW6', '中空圓柱外 R=6 cm, 內 r=4 cm, h=20 cm。材料體積 = ？（π=3.14）', 'd2', '🌿', 90),
        ('HW7', '複合體：長方體（30×20×10 cm）+ 三角柱（底面積 60 cm², 柱高 20 cm）。總體積 = ？', 'd2', '🌿', 90),
        ('HW8', '一個圓柱形罐頭（r=4 cm, h=10 cm）的標籤紙完全包裹側面。標籤紙的面積是？', 'd2', '🌿', 85),
    ]
    parts.append(qtable(hwa))
    parts.append(pb_close())
    parts.append(page_break())

    # Page 6: Error table + Mnemonic + Strategy Cards
    parts.append(pb_open())
    parts.append(h1('六、常見錯誤辨析表（The Error Table）'))
    errors = [
        ('1', 'T1 — 單位混淆', '用 m 和 cm 混合相乘，結果完全錯', '忘記統一單位就相乘', '先將所有尺寸轉為同一單位', '做題前先檢查單位是否一致', '🔴 高'),
        ('2', 'T2 — 公式混淆', 'V = πr²×h 寫成 V = 2πr×h', '混淆圓周公式和圓面積公式', 'V 用 πr²（面積），不是 2πr（周長）', 'V公式中有 r²，周長公式沒有', '🔴 高'),
        ('3', 'T4 — 忘加頂面', '表面積只計一個圓面 + 側面', '以為圓柱只有一個底面（像杯子）', '總表面積 = 2πr²（兩個圓面）+ 2πrh', '畫圖標出兩個圓面', '🔴 高'),
        ('4', 'T3 — 混淆高度', '用三角形的高當作柱體的高', '不清楚「底面高」和「柱體高」的區別', '底面積中用的高是底面圖形的高，再×柱高', '先計底面積，再乘以柱體高度', '🟡 中'),
        ('5', 'T6 — 換算數量級', '1 m³ = 100 cm³（❌）', '忘記體積是三維換算', '1 m³ = 100×100×100 = 1,000,000 cm³', 'm³→cm³ 乘一百萬', '🔴 高'),
        ('6', 'T5 — 中空計算', '忘記減去中空部分或減錯', '未畫圖標註內外尺寸', '材料體積 = 外部體積 - 內部空間', '畫截面圖輔助理解', '🟡 中'),
        ('7', 'T7 — 複合拆解', '複合體拆錯或漏計某一部', '複合體結構分析不清楚', '逐一標號拆解，分別計體積再相加', '用不同顏色標出各部分', '🟡 中'),
    ]
    parts.append(error_table(errors))

    parts.append(mn('🧠 「棱柱底面積乘高，圓柱πr²乘高。表面積要計兩個圓，唔好漏咗個頂！單位統一先好乘，m³轉cm³乘一百萬！」'))

    parts.append(h1('七、解題策略卡（4-Step Strategy Cards）'))
    parts.append(sc_cards([
        ('①', '統一單位', '檢查所有尺寸的單位，轉換為同一單位（建議全部轉 cm）'),
        ('②', '識別底形', '看清底面是什麼形狀（三角形/梯形/圓形），計算底面積'),
        ('③', '套入公式', '體積=底面積×高。圓柱特別注意：V=πr²h，表面積=2πr²+2πrh'),
        ('④', '驗算單位', '答案的單位是 cm³（體積）或 cm²（表面積），不要混淆'),
    ]))

    parts.append(FOOTER.replace('LF-P6-下-LXX', lesson_code))
    parts.append(pb_close())

    parts.append(html_tail())

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))

    print(f"  [OK] L37 written: {filepath}")
    return filepath


def gen_l38():
    """L38: SSPA終極跨課題殺手題（混合3+陷阱·全真模擬）"""
    svgs = gen_all_svgs()
    lesson_code = "LF-P6-下-L38"
    title = "SSPA終極跨課題殺手題（混合3+陷阱·全真模擬）"
    lesson_num = 38
    filepath = os.path.join(OUTPUT_DIR, f"{lesson_code}_SSPA跨課題殺手題混合陷阱.html")

    parts = [html_head(title, lesson_code)]

    parts.append(cover_page(lesson_code, lesson_num, title, '65 分鐘',
        '🪤 每題混合 3+ 陷阱類型（T1-T10）· 無分類·全混合 · 模擬真卷壓軸題',
        '<span class="ss sh">🔴 終極</span> SSPA 真卷最後 3-5 題為跨課題綜合題，佔約 15-20%',
        'L21-L37 全部內容（圓面積、百分數、方程、圖表、速率、排水法、棱柱、圓柱）',
        '❶ 辨識混合陷阱 ❷ 跨課題綜合解題 ❸ 真卷壓軸題實戰 ❹ 時間管理策略'))

    # Page 2: Direct into intensive problems
    parts.append(pb_open())
    parts.append(h1('一、終極混合陷阱題集（40+ 題，模擬真卷壓軸題格式）'))
    parts.append('<div class="warn">⚠️ 以下每題最少混合 3 種陷阱類型（T1-T10）。題目不分章節，全部隨機混合，模仿 SSPA 真卷最後 3-5 題的「跨課題殺手題」格式。</div>')

    parts.append(h2('第 1 組：圓形 + 百分數 + 單位混合陷阱'))
    g1 = [
        (1, '一個圓形花圃的半徑是 7 m。花圃面積的 40% 種了玫瑰，其餘種了菊花。問：<br>(a) 花圃總面積？(π=<span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>)<br>(b) 玫瑰佔地多少 m²？<br>(c) 菊花面積 = ？cm²？', 'd3', '🌳', 110),
        (2, '一間圓形餐廳（r=10 m）的地面 60% 鋪木地板，剩下的鋪地磚。木地板每 m² 售 $250，地磚每 m² $180。總成本 = ？（π=3.14）', 'd4', '🏔️', 110),
        (3, '一個半圓形廣告牌（r=8 m）的表面積需要塗漆。漆油每罐覆蓋 15 m²，售價 $120。廣告牌預算 $1000 夠不夠？（π=3.14）', 'd3', '🌳', 100),
        (4, '一個圓形和一個正方形面積相同。圓的 r=10 cm，正方形的邊長是多少？（π=3.14）', 'd3', '🌳', 95),
    ]
    parts.append(qtable(g1))

    parts.append(h2('第 2 組：速率 + 方程 + 圖表混合陷阱'))
    g2 = [
        (5, '甲從 A 地出發往 B 地，速率 x km/h。2 小時後乙從 B 地出發往 A 地，速率比甲慢 15 km/h。又過 3 小時後兩人相遇。AB 相距 300 km。求 x。（列方程求解）', 'd4', '🏔️', 120),
        (6, '一輛車以 80 km/h 行駛了一段路，再以 60 km/h 行駛剩餘路程。總距離 200 km，總時間 3 小時。求兩段路的距離各是多少？（用方程）', 'd4', '🏔️', 120),
        (7, '下圖為一輛巴士的行車紀錄（折線圖省略，描述數據）：<br>0-1h: 60km/h, 1-2h: 停車, 2h-3.5h: 80km/h<br>(a) 求總距離。<br>(b) 求全程平均速率。<br>(c) 如果全程用均速 70 km/h，能省多少時間？', 'd3', '🌳', 110),
    ]
    parts.append(qtable(g2))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 3: More killer problems
    parts.append(pb_open())
    parts.append(h2('第 3 組：體積 + 排水法 + 百分數混合陷阱'))
    g3 = [
        (8, '一個長方體水箱（80×50×60 cm）裝了 75% 的水。放入一個邊長 20 cm 的正方體鐵塊（完全浸沒）。<br>(a) 原有水體積 = ？<br>(b) 鐵塊體積 = ？<br>(c) 最終水位 = ？<br>(d) 有沒有溢出？如有，溢出多少？', 'd3', '🌳', 120),
        (9, '一個圓柱水箱（r=15 cm, h=50 cm）裝了 80% 的水。放入一個半徑 6 cm 的實心鐵球（完全浸沒）。（π=3.14，球 V=<span class="f"><span class="n">4</span><span class="b"></span><span class="d">3</span></span>πr³）<br>(a) 原有水體積？<br>(b) 水位升高多少？<br>(c) 溢出？', 'd4', '🏔️', 120),
        (10, '一個容器由下層長方體（30×20×15 cm）和上層圓柱（r=10 cm, h=10 cm）垂直疊加組成（內部連通）。初始水位在長方體頂部（15 cm 高處）。放入一個體積 2000 cm³ 的物體（完全浸沒）。最終水位在哪個部分？水位升高多少？', 'd4', '🏔️', 130),
    ]
    parts.append(qtable(g3))

    parts.append(h2('第 4 組：百分數利潤 + 方程 + 圖表混合陷阱'))
    g4 = [
        (11, '一個商人以成本價 $500 購入一批貨。他先以賺 30% 的價格賣出 60%，再以八折清貨賣出剩下的。問總利潤率和總利潤金額。（百分數答案取至整數）', 'd3', '🌳', 120),
        (12, '一件貨物成本 $C。如果標價是成本的 150%，再打九折出售後仍賺 $40。<br>(a) 列出方程。<br>(b) 求成本 C。', 'd3', '🌳', 110),
        (13, '某商店三種貨品的銷售額由圓形圖表示（見圖）。貨品 A 佔 35%，貨品 B 佔 45%，貨品 C 佔 20%。總銷售額 $80,000。<br>(a) 各貨品銷售額 = ？<br>(b) 如果貨品 B 的利潤率是 25%，它的成本 = ？<br>(c) 如果貨品 C 虧損 10%，虧損了多少？', 'd3', '🌳', 120),
    ]
    parts.append(qtable(g4))

    parts.append(geom_div(svgs['pie_2']))

    parts.append(h2('第 5 組：圓面積/周長 + 複合圖形 + 單位混合陷阱'))
    g5 = [
        (14, '一個運動場由一個長方形（100m×60m）和兩端的兩個半圓（r=30m）組成。求：<br>(a) 運動場的總面積（m²）？<br>(b) 跑道總長度（周界）？<br>(c) 轉換為 cm² 和 km。（π=3.14）', 'd3', '🌳', 120),
        (15, '一個環形（同心圓）的外圓 r=14 m，內圓 r=8 m。求：<br>(a) 環形面積（π=<span class="f"><span class="n">22</span><span class="b"></span><span class="d">7</span></span>）<br>(b) 環形佔外圓面積的百分之幾？<br>(c) 如果環形是草地，每 m² 草地成本 $35，總成本 = ？', 'd3', '🌳', 110),
        (16, '一個扇形（<span class="f"><span class="n">1</span><span class="b"></span><span class="d">4</span></span>圓）的半徑是 r=12 cm。求：<br>(a) 扇形面積<br>(b) 扇形周長<br>(c) 如果將扇形捲成一個圓錐的側面，圓錐的底面半徑 = ？（π=3.14）', 'd4', '🏔️', 120),
    ]
    parts.append(qtable(g5))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 4: More
    parts.append(pb_open())
    parts.append(h2('第 6 組：方程 + 速率 + 幾何混合陷阱'))
    g6 = [
        (17, '一個長方形的長是闊的 3 倍。如果長減少 5 cm、闊增加 2 cm，新長方形的周界是 50 cm。求原長方形的面積。（列方程求解）', 'd3', '🌳', 110),
        (18, '一個三角形的三邊長度比例為 3:4:5，周界為 72 cm。求：<br>(a) 三邊各長多少？<br>(b) 三角形的面積是多少？（提示：3-4-5 為直角三角形）<br>(c) 如果每 cm² 重 2.5 g，三角形重多少 kg？', 'd3', '🌳', 110),
        (19, '一輛車的油箱是長方體形狀（60×40×30 cm），裝了 60% 的汽油。汽車每行駛 100 km 耗油 8 L。現在從 A 城出發，目的地距離 450 km。<br>(a) 油箱現有多少 L 汽油？<br>(b) 夠不夠到達目的地？<br>(c) 如果不夠，還需要多少 L？', 'd4', '🏔️', 130),
    ]
    parts.append(qtable(g6))

    parts.append(h2('第 7 組：棱柱圓柱 + 排水法 + 百分數混合陷阱'))
    g7 = [
        (20, '一個三角柱容器（底為直角三角形：15cm、20cm、25cm，柱高 40cm）裝了 70% 的水。求：<br>(a) 底面三角形的面積？<br>(b) 容器內有多少 L 水？<br>(c) 放入一個邊長 10 cm 的正方體，水位升高多少？', 'd3', '🌳', 120),
        (21, '一個圓柱容器 (r=12 cm, h=40 cm) 和一個正方體容器（邊長 20 cm）連通（底部有管道）。圓柱初始裝滿水，正方體是空的。打開連通管後，兩個容器的水位最後一樣高。求最終水位高度。', 'd4', '🏔️', 130),
        (22, '一個複合體由圓柱（r=8 cm, h=15 cm）放在長方體（20×16×10 cm）上面。整個複合體浸入一個裝了 60% 水的容器（底面積 1000 cm²，高 50 cm，初始水位 35 cm）。問水會溢出嗎？', 'd4', '🏔️', 130),
    ]
    parts.append(qtable(g7))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 5: Even more killer problems
    parts.append(pb_open())
    parts.append(h2('第 8 組：圖表閱讀 + 百分數 + 平均數混合陷阱'))
    g8 = [
        (23, '以下為某班 40 名學生的數學測驗分數分佈：<br>90-100分：8人，80-89分：12人，70-79分：10人，60-69分：6人，<60分：4人<br>(a) 全班的平均分約是多少？（用組中點計算）<br>(b) 80 分或以上的學生佔全班百分之幾？<br>(c) 如果合格線是 60 分，合格率 = ？<br>(d) 如果每位不合格的學生多做 5 題練習，每人平均提升 8 分，新合格率 = ？', 'd3', '🌳', 120),
        (24, '棒形圖顯示 A、B、C、D 四間公司的銷售額（見圖）：A:$120K, B:$85K, C:$150K, D:$95K<br>(a) 總銷售額 = ？<br>(b) C 公司比 B 公司多百分之幾？<br>(c) D 公司佔總銷售額的百分之幾？（答案取至 1 位小數）<br>(d) 如果 A 公司下年銷售額增加 25%，新的 A 銷售額 = ？', 'd3', '🌳', 110),
        (25, '一個圓形圖顯示小明每月的支出分配：住屋 40%、飲食 25%、交通 15%、娛樂 10%、儲蓄 10%。如果小明月入 $25000：<br>(a) 每月儲蓄 = ？<br>(b) 飲食和交通合共佔支出的百分之幾？<br>(c) 如果他想在 6 個月內儲到 $30000，每月必須多儲多少？（多儲的金額從娛樂扣減）', 'd3', '🌳', 110),
    ]
    parts.append(qtable(g8))

    parts.append(geom_div(svgs['bar_simple_1']))
    parts.append('<p style="text-align:center;font-size:10px;color:var(--gray);">（第 8 組參考圖）</p>')

    parts.append(h2('第 9 組：終極壓軸殺手題（混合 5+ 陷阱）'))
    g9 = [
        (26, '【終極壓軸】一個複合立體由以下部分組成：底層為長方體（長 L cm、闊 W cm、高 10 cm），中層為三角柱（底為直角三角形，直角邊為 W cm 和 8 cm，柱長 = L cm），頂層為半個圓柱（r=<span class="f"><span class="n">W</span><span class="b"></span><span class="d">2</span></span> cm, h=L cm）。已知 L=30, W=20。<br>(a) 底層體積 = ？（2分）<br>(b) 中層（三角柱）體積 = ？（3分）<br>(c) 頂層（半圓柱）體積 = ？（4分）<br>(d) 總體積 = ？cm³ = ？m³？（4分）<br>(e) 整個複合體的表面積約為？（不計底部貼合面）（7分）<br>（π=3.14）', 'd4', '🏔️', 160),
        (27, '【終極壓軸】一輛車從 A 城出發到 D 城，途經 B 城和 C 城。數據如下：<br>A→B：距離 = (2x+30) km，速率 80 km/h<br>B 停留 45 分鐘<br>B→C：距離 = (3x-10) km，速率 60 km/h<br>C 停留 30 分鐘<br>C→D：距離 = (x+50) km，速率 100 km/h<br>全程總距離 = 400 km。<br>(a) 求 x。（列方程）（3分）<br>(b) 求 A→B、B→C、C→D 各段距離。（3分）<br>(c) 求各段行車時間。（3分）<br>(d) 求全程平均速率。（3分）<br>(e) 如果全程以均速行駛（不計停留），總行車時間相同，車速 = ？（3分）<br>(f) 如果 C→D 段因塞車速率降至 60 km/h，求新的全程平均速率。（5分）', 'd4', '🏔️', 180),
    ]
    parts.append(qtable(g9))
    parts.append(pb_close())
    parts.append(page_break())

    # Page 6: More killer + Error table
    parts.append(pb_open())
    parts.append(h2('第 10 組：混合應用衝刺（額外 10 題快速練習）'))
    g10 = [
        (28, '半圓 r=10cm，求面積和周長。如果將半圓旋轉 180° 形成一個完整立體的底面，立體高 15cm，體積 = ？（π=3.14）', 'd3', '🌳', 100),
        (29, '一件貨品成本 $800，標價賺 40%，再打八五折。最終利潤 = ？利潤率 = ？', 'd3', '🌳', 100),
        (30, '解方程：<span class="f"><span class="n">2x-1</span><span class="b"></span><span class="d">3</span></span> + <span class="f"><span class="n">x+4</span><span class="b"></span><span class="d">2</span></span> = 8', 'd3', '🌳', 90),
        (31, '甲 3 小時完成一件工作，乙 5 小時完成同一工作。兩人合作需要多少小時？', 'd3', '🌳', 95),
        (32, '一個長方體容器（50×30×40cm）的水位 30cm。放入一個不規則石頭後水位升到 33cm。石頭體積 = ？如果石頭改放入一個圓柱容器（r=10cm, 水位 25cm），水位升到？', 'd3', '🌳', 110),
        (33, '一個正方體邊長 8cm，表面積 = ？體積 = ？如果每個面都塗上漆，漆的面積 = ？cm² = ？m²', 'd2', '🌿', 100),
        (34, '小明和小華共儲蓄 $840。小明的儲蓄是小華的 <span class="f"><span class="n">3</span><span class="b"></span><span class="d">4</span></span>。各儲蓄多少？', 'd2', '🌿', 90),
        (35, '一個複合圖形：長方形 12cm×8cm + 上面一個半圓（直徑=8cm）。總面積 = ？周界 = ？', 'd3', '🌳', 110),
        (36, '速率 = 距離 ÷ 時間。如果距離增加 20%，時間減少 10%，新速率 = 原速率的多少 %？', 'd4', '🏔️', 100),
        (37, '一個容器的水每分鐘漏 2.5% 的水。初始有 40 L，30 分鐘後剩多少？（用複合計算）', 'd4', '🏔️', 100),
    ]
    parts.append(qtable(g10))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 7: Error table + Mnemonic + Strategy
    parts.append(pb_open())
    parts.append(h1('二、T1-T10 陷阱引爆總表'))
    parts.append('''<table class="et">
<tr><th>陷阱碼</th><th>陷阱名稱</th><th>典型症狀</th><th>觸發條件</th><th>防禦策略</th></tr>
<tr><td>T1</td><td>單位混用</td><td>m 和 cm 相乘未換算</td><td>題目出現 2+ 不同單位</td><td>先統一為最小單位</td></tr>
<tr><td>T2</td><td>公式混淆</td><td>用錯公式（圓周/圓面積）</td><td>多個公式相似的題目</td><td>用單位區分：cm=周界，cm²=面積</td></tr>
<tr><td>T3</td><td>條件遺漏</td><td>忘了「完全浸沒」、「停留時間」</td><td>題目有隱含條件</td><td>圈出每個關鍵條件</td></tr>
<tr><td>T4</td><td>幾何誤判</td><td>半圓周長忘加直徑</td><td>半圓/扇形周長題</td><td>畫圖標出所有邊長</td></tr>
<tr><td>T5</td><td>計算失誤</td><td>π 取錯值、乘法錯</td><td>多步驟計算</td><td>分工步驟，逐步驗算</td></tr>
<tr><td>T6</td><td>概念混淆</td><td>排水法：用新水位×底面積</td><td>水位變化題</td><td>體積 = 底面積 × 水位差</td></tr>
<tr><td>T7</td><td>圖表誤讀</td><td>誤讀棒形圖/圓形圖數據</td><td>綜合圖表題</td><td>先讀圖例，再對數據</td></tr>
<tr><td>T8</td><td>方程設錯</td><td>未知數設錯位置或關係</td><td>列方程應用題</td><td>用文字定義每個變數</td></tr>
<tr><td>T9</td><td>換算數量級</td><td>m³→cm³ 乘 100 而非 1,000,000</td><td>體積單位轉換</td><td>m³→cm³ = ×1,000,000</td></tr>
<tr><td>T10</td><td>跨課題混亂</td><td>無法判斷用哪個知識點</td><td>混合多課題的綜合題</td><td>拆解題目，分段處理</td></tr>
</table>''')

    parts.append(mn('🧠 「綜合殺手題，拆解係關鍵！逐個知識點分開計，唔好一次過食晒。先睇清楚題目要乜，再揀公式，最後驗算！」'))
    parts.append(mn('🧠 「單位要統一，公式要分明。半圓記住加直徑，排水係用水位差！圖表先睇例，方程要寫清。m³轉cm³乘一百萬！」'))

    parts.append(h1('三、終極解題策略卡'))
    parts.append(sc_cards([
        ('①', '拆解題目', '將綜合題拆成 2-4 個獨立小問題，逐個擊破。每個小問題對應一個知識點。'),
        ('②', '標註陷阱', '每識別出一個陷阱類型（T1-T10），就在題旁標註。做到「預知陷阱」。'),
        ('③', '分段計算', '每一步只做一個計算，寫清楚中間結果。不要跳步。'),
        ('④', '交叉驗算', '用不同方法驗算：逆向計算、估算、單位檢查。'),
    ]))

    parts.append(FOOTER.replace('LF-P6-下-LXX', lesson_code))
    parts.append(pb_close())

    parts.append(html_tail())

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))

    print(f"  [OK] L38 written: {filepath}")
    return filepath


def gen_l39():
    """L39: 中學數學思維轉換（算術→代數·具體→抽象）"""
    svgs = gen_all_svgs()
    lesson_code = "LF-P6-下-L39"
    title = "中學數學思維轉換（算術→代數·具體→抽象）"
    lesson_num = 39
    filepath = os.path.join(OUTPUT_DIR, f"{lesson_code}_中學數學思維轉換.html")

    parts = [html_head(title, lesson_code)]

    parts.append(cover_page(lesson_code, lesson_num, title, '65 分鐘',
        '🪤 T8 試圖用算術方法解所有代數問題 · T2 變數表達關係混淆 · T10 跨思維模式混亂',
        '<span class="ss sh">🔴 關鍵銜接</span> 中一數學首月核心——從「搵答案」到「表達關係」的思維轉換',
        '堂24-25（方程入門與進階）· 堂35-37（中一預習系列）',
        '❶ 算術 vs 代數思維差異 ❷ 文字題→方程系統化翻譯 ❸ 用變數概括規律 ❹ 同一問題兩種解法對比'))

    # Page 2: Warm-up + KP1
    parts.append(pb_open())
    parts.append(h1('一、熱身啟動題（共 5 題，5 分鐘）'))
    warmup = [
        (1, '小明有 $20，買了一支筆後剩下 $8。這支筆多少錢？（用算術方法）', 'd1', '🌱 基礎', 80),
        (2, '同上題：如果筆的價格是 $x，請用方程表示並求解。（用代數方法）', 'd1', '🌱 基礎', 80),
        (3, '一個數的 3 倍加 5 等於 20。這個數是多少？（分別用算術和代數兩種方法）', 'd2', '🌿 進階', 90),
        (4, '一個長方形的周界是 28 cm，長是闊的 3 倍。長和闊各是多少？（先用算術試試看）', 'd2', '🌿 進階', 90),
        (5, '你認為「方程」是工具還是障礙？寫出你對方程的真實感受。（2-3 句）', 'd1', '🌱 基礎', 85),
    ]
    parts.append(qtable(warmup))

    # KP1: Arithmetic vs Algebraic
    parts.append(h1('二、核心知識精講 ＋ 思維對比'))

    parts.append(kp_block(
        '知識點一：算術思維 vs 代數思維 — 不是更難，是不同！<span class="ss sh">🔴 核心轉換</span>',
        '''<table style="width:100%;border-collapse:collapse;margin:6px 0;font-size:11px;">
<tr style="background:#FEF3C7;"><td style="padding:6px;border:1px solid #D1D5DB;width:50%;"><b>小學算術思維（Arithmetic）</b></td><td style="padding:6px;border:1px solid #D1D5DB;width:50%;"><b>中學代數思維（Algebraic）</b></td></tr>
<tr><td style="padding:6px;border:1px solid #D1D5DB;">從已知數出發，一步一步計算</td><td style="padding:6px;border:1px solid #D1D5DB;">用變數（x, y）代表未知數</td></tr>
<tr><td style="padding:6px;border:1px solid #D1D5DB;">目標：搵出「答案」= 一個數字</td><td style="padding:6px;border:1px solid #D1D5DB;">目標：建立「關係」= 一條等式</td></tr>
<tr><td style="padding:6px;border:1px solid #D1D5DB;">逆向運算：由結果倒推</td><td style="padding:6px;border:1px solid #D1D5DB;">正向建模：設未知數→列方程→解方程</td></tr>
<tr><td style="padding:6px;border:1px solid #D1D5DB;">適合簡單、單步驟問題</td><td style="padding:6px;border:1px solid #D1D5DB;">適合複雜、多未知數、抽象問題</td></tr>
<tr><td style="padding:6px;border:1px solid #D1D5DB;">例：? + 5 = 12，所以 ? = 7</td><td style="padding:6px;border:1px solid #D1D5DB;">例：x + 5 = 12，所以 x = 7</td></tr>
</table>'''))

    parts.append(geom_div(svgs['bridge_diagram']))

    parts.append(magic_box('中學數學 = 同一樣嘢，用更 powerful 嘅工具去做。唔係難咗，係多咗一個工具箱！', 'green'))

    parts.append(ex_block('例題 1：同一問題，兩種解法（基礎對比）',
        '「小明比小華大 3 歲，兩人年齡之和是 25 歲。小明多少歲？」'))
    parts.append('''<div style="display:flex;gap:10px;margin:8px 0;">
<div style="flex:1;background:#DCFCE7;border:2px solid #BBF7D0;border-radius:8px;padding:14px;">
<div style="font-size:13px;font-weight:900;color:#166534;">小學算術解法（逆向）</div>
<div style="font-size:12px;line-height:1.7;">
兩人加埋 = 25<br>
小明 = 小華 + 3<br>
所以：小華 + (小華+3) = 25<br>
即 2×小華 = 22<br>
小華 = 11，小明 = 14
</div></div>
<div style="flex:1;background:#DBEAFE;border:2px solid #93C5FD;border-radius:8px;padding:14px;">
<div style="font-size:13px;font-weight:900;color:#1E40AF;">中學代數解法（正向）</div>
<div style="font-size:12px;line-height:1.7;">
設小華 = x 歲<br>
則小明 = x + 3 歲<br>
方程：x + (x+3) = 25<br>
2x + 3 = 25<br>
2x = 22<br>
x = 11，小明 = 14
</div></div></div>''')

    parts.append(warn('🪤 關鍵陷阱：不要試圖用算術方法解決所有問題！中學題目更複雜，算術方法會令你迷失方向。學識「let x = ...」係你嘅新超能力！'))

    parts.append(mn('🧠 「算術係倒推，代數係建模。唔好死守算術，學識用變數，複雜問題即刻變簡單！」'))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 3: KP2 + KP3
    parts.append(pb_open())

    parts.append(kp_block(
        '知識點二：文字題 → 方程 — 系統化翻譯 5 步法 <span class="ss sh">🔴 中一核心技能</span>',
        '''<ol>
<li><strong>Step 1：讀題，找出未知數</strong> — 題目問什麼，就設什麼為變數</li>
<li><strong>Step 2：設變數（let x = ...）</strong> — 用字母代表未知量，寫清楚單位</li>
<li><strong>Step 3：翻譯關係</strong> — 將中文關鍵詞轉為數學符號：<br>
&nbsp;&nbsp;「比...多」→ + | 「比...少」→ - | 「是...的 n 倍」→ × n | 「共」→ = | 「相差」→ 大減小</li>
<li><strong>Step 4：列方程</strong> — 將所有關係整合為一條等式</li>
<li><strong>Step 5：解方程 + 驗算</strong> — 解出變數後代入原題驗證</li></ol>'''))

    parts.append(ex_block('例題 2（翻譯示範）',
        '「一個數的 5 倍比它的 3 倍多 14。求這個數。」<br><br>翻譯過程：<br>設這個數 = x<br>「5倍」→ 5x<br>「比...多14」→ 5x - 3x = 14<br>方程：5x - 3x = 14 → 2x = 14 → x = 7'))
    parts.append(ex_block('例題 3（兩未知數）',
        '「甲、乙兩數之和為 48，甲是乙的 3 倍。求兩數。」<br><br>翻譯過程：<br>設乙 = x，則甲 = 3x<br>方程：3x + x = 48 → 4x = 48 → x = 12<br>所以乙 = 12，甲 = 36'))

    parts.append(h2('知識點二 同步練習'))
    trans_qs = [
        (6, '將以下文字翻譯為方程（不用解）：「一個數減去 8 後，再乘以 3，結果是 21」', 'd2', '🌿 進階', 80),
        (7, '將以下文字翻譯為方程並求解：「小明儲蓄的 2 倍比小華儲蓄的 3 倍少 $50。小明儲蓄 $100，求小華的儲蓄。」', 'd3', '🌳 挑戰', 95),
        (8, '「一個長方形的長比闊多 5 cm，周界是 38 cm。求長和闊。」— 設變數、列方程、求解。', 'd3', '🌳 挑戰', 100),
        (9, '「兩數之和為 72，較大的數是較小的數的 5 倍。求兩數。」', 'd2', '🌿 進階', 85),
    ]
    parts.append(qtable(trans_qs))

    # KP3: Generalizing patterns
    parts.append(kp_block(
        '知識點三：用變數概括規律 — 從「計出結果」到「寫出公式」<span class="ss sm">🟡 中一進階</span>',
        '''<ol>
<li><strong>數字規律：</strong>第 n 項 = 用 n 表達的公式（例如：2, 5, 8, 11... → 第 n 項 = 3n - 1）</li>
<li><strong>圖形規律：</strong>第 n 個圖形的火柴數 / 方格數 → 用 n 表示</li>
<li><strong>函數概念：</strong>y = f(x)，輸入 x 就得到對應的 y</li>
<li><strong>應用：</strong>計算任意項而無需逐個列出（例如直接計第 100 項）</li></ol>'''))

    parts.append(ex_block('例題 4（數字規律）',
        '數列：4, 7, 10, 13, 16, ...<br>(a) 寫出第 n 項的公式。<br>(b) 求第 50 項的值。<br><br>解：公差 = 3 → 第 n 項 = 3n + 1<br>第 50 項 = 3×50 + 1 = 151'))

    parts.append(ex_block('例題 5（圖形規律）',
        '第 1 個圖案用 4 支火柴，第 2 個用 7 支，第 3 個用 10 支...<br>(a) 第 n 個圖案用多少支火柴？<br>(b) 第 20 個圖案用多少支？<br><br>解：火柴數 = 3n + 1（因為每次加 3 支）<br>第 20 個 = 3×20 + 1 = 61 支'))

    parts.append(h2('知識點三 同步練習'))
    pattern_qs = [
        (10, '數列：3, 8, 13, 18, 23, ... 寫出第 n 項公式及第 30 項的值。', 'd2', '🌿 進階', 85),
        (11, '第 1 個正方形用 4 支火柴，之後每加一個正方形加 3 支火柴（相連排列）。n 個正方形用多少支火柴？', 'd3', '🌳 挑戰', 90),
        (12, '一個數列的規律是：第 n 項 = n² + 2。求第 1 至第 5 項，並計算第 10 項。', 'd3', '🌳 挑戰', 90),
    ]
    parts.append(qtable(pattern_qs))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 4: KP4 + Tiered practice
    parts.append(pb_open())

    parts.append(kp_block(
        '知識點四：算術 vs 代數 — 什麼時候該用哪個？<span class="ss sm">🟡 策略選擇</span>',
        '''<table style="width:100%;border-collapse:collapse;margin:6px 0;font-size:11px;">
<tr style="background:var(--blue);color:white;"><td style="padding:5px 8px;">情況</td><td style="padding:5px 8px;">推薦方法</td><td style="padding:5px 8px;">原因</td></tr>
<tr><td style="padding:5px 8px;border:1px solid #D1D5DB;">一步計算（例如：50 的 30% = ?）</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">算術 ✔</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">直接、快速</td></tr>
<tr><td style="padding:5px 8px;border:1px solid #D1D5DB;">兩個未知數有關聯</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">代數 ✔</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">一個變數可表達另一個</td></tr>
<tr><td style="padding:5px 8px;border:1px solid #D1D5DB;">逆向運算（知道結果找原因）</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">代數 ✔</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">方程直接建模更清晰</td></tr>
<tr><td style="padding:5px 8px;border:1px solid #D1D5DB;">規律概括 / 求第 n 項</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">代數 ✔</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">變數才能表達任意項</td></tr>
<tr><td style="padding:5px 8px;border:1px solid #D1D5DB;">幾何面積 / 體積</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">兩者皆可</td><td style="padding:5px 8px;border:1px solid #D1D5DB;">視乎複雜程度</td></tr>
</table>'''))

    parts.append(magic_box('關鍵轉念：中學數學不是「變難」，而是問題變得更多元化。你需要的是一個更大的工具箱，而不是丟棄舊的工具！', 'yellow'))

    parts.append(mn('🧠 「簡單心算夠用，複雜方程幫手。兩個方法都識，考試無有怕！」'))

    # Tiered practice
    parts.append(h1('三、課堂分層同步練習'))
    parts.append(h2('🌱 基礎層（共 3 題，全體必做）'))
    basic = [
        (13, '設 x 代表一個數。寫出以下關係的代數式：(a) 這個數加 7 (b) 這個數的 3 倍減 4 (c) 這個數的一半加 2', 'd1', '🌱 基礎', 85),
        (14, '解方程：4x - 7 = 21', 'd1', '🌱 基礎', 80),
        (15, '「一個數的 2 倍加 5 等於 19。」分別用算術和代數方法求解。', 'd1', '🌱 基礎', 90),
    ]
    parts.append(qtable(basic))

    parts.append(h2('🌿 進階層（共 3 題）'))
    adv = [
        (16, '一個長方形的長是闊的 2 倍少 1 cm，周界是 28 cm。求長和闊。（必須用代數方法）', 'd2', '🌿 進階', 95),
        (17, '「甲、乙、丙三人共有 $560。甲是乙的 2 倍，丙比乙多 $80。三人各有多少？」設變數，列方程，求解。', 'd2', '🌿 進階', 100),
        (18, '數列：5, 9, 13, 17, 21, ... 求 (a) 第 n 項公式 (b) 第 100 項的值。', 'd2', '🌿 進階', 90),
    ]
    parts.append(qtable(adv))

    parts.append(h2('🌳 挑戰層（共 3 題）'))
    chal = [
        (19, '一個兩位數的十位數字是個位數字的 2 倍。如果將兩個數字對調，新數比原數小 27。求原數。（提示：設個位 = x，十位 = 2x，原數 = 10(2x) + x = 21x）', 'd3', '🌳 挑戰', 110),
        (20, '小明今年 x 歲，爸爸今年 (x+28) 歲。5 年後，爸爸的年齡是小明的 3 倍。求 x 和小明現在的年齡。', 'd3', '🌳 挑戰', 100),
        (21, '一個分數的分子比分母小 5。如果分子加 3、分母加 1，分數的值變為 <span class="f"><span class="n">1</span><span class="b"></span><span class="d">2</span></span>。求原分數。', 'd3', '🌳 挑戰', 105),
    ]
    parts.append(qtable(chal))

    parts.append(h2('🏔️ 極限挑戰（共 1 題）'))
    ext = [
        (22, '三個人 A、B、C 的年齡滿足以下條件：<br>· A 比 B 大 5 歲<br>· C 的年齡是 B 的 2 倍少 3 歲<br>· 8 年後，三人的年齡總和是 100 歲<br>求現在三人的年齡。（設 B 的年齡 = x，依次表達 A 和 C，再建方程）', 'd4', '🏔️ 極限', 120),
    ]
    parts.append(qtable(ext))
    parts.append(pb_close())
    parts.append(page_break())

    # Page 5: Application + Homework
    parts.append(pb_open())
    parts.append(h1('四、應用題：算術 vs 代數對比實戰（共 5 題）'))
    app = [
        (23, '【對比練習 1】一個數的 4 倍減去 6 等於 26。求這個數。<br>(a) 先用算術方法（逆向運算）<br>(b) 再用代數方法（設 x，列方程）<br>你覺得哪個方法比較清楚？為什麼？', 'd2', '🌿 進階', 110),
        (24, '【對比練習 2】一個長方形的周界是 64 cm，長比闊多 8 cm。求長和闊。<br>(a) 先用算術方法（嘗試直接用數字推理）<br>(b) 再用代數方法（設闊 = x）<br>比較哪個方法更適合這個問題。', 'd3', '🌳 挑戰', 120),
        (25, '【對比練習 3】一件貨品以成本的 120% 出售，賺了 $50。求成本。<br>(a) 算術方法：$50 ÷ 20% = $250<br>(b) 代數方法：設成本 = C，1.2C - C = 50 → 0.2C = 50 → C = 250<br>這個問題用哪個方法都很快。但如果是「一件貨品以成本打八折後仍賺 15%，求成本」，哪個方法更容易？', 'd3', '🌳 挑戰', 110),
        (26, '【中一真題型】一個圓柱的體積是 628 cm³，高是 10 cm。求底半徑。（π = 3.14）<br>必須用代數方法：設 r = x，建立方程求解。', 'd3', '🌳 挑戰', 100),
        (27, '【思維轉換題】用一句話說明「算術」和「代數」的最大分別。再用一個具體例子說明為什麼中學需要代數。（寫在作答區）', 'd2', '🌿 進階', 100),
    ]
    parts.append(qtable(app))

    parts.append(h1('五、課後鞏固練習（家課）'))
    parts.append(h2('基礎鞏固（5+ 題）'))
    hwb = [
        ('HW1', '解方程：3x + 7 = 28', 'd1', '🌱', 80),
        ('HW2', '解方程：5(x - 2) = 35', 'd1', '🌱', 80),
        ('HW3', '「一個數加 12 後除以 3 等於 8。」設變數並列出方程。', 'd1', '🌱', 80),
        ('HW4', '數列：2, 6, 10, 14, 18, ... 第 n 項 = ？第 25 項 = ？', 'd1', '🌱', 80),
        ('HW5', '「兩數之和為 60，大數是小數的 4 倍。」設變數、列方程、求解。', 'd1', '🌱', 85),
    ]
    parts.append(qtable(hwb))

    parts.append(h2('進階挑戰（3+ 題）'))
    hwa = [
        ('HW6', '「一個長方形的長是闊的 3 倍，面積是 108 cm²。求長和闊。」必須用代數方法。', 'd2', '🌿', 95),
        ('HW7', '「小明比小華大 4 歲。6 年後，兩人的年齡和是 40 歲。求現在各自的年齡。」設變數、列方程、求解。', 'd2', '🌿', 100),
        ('HW8', '一個兩位數，十位數字是個位數字的 3 倍。對調數字後，新數比原數少 54。求原數。', 'd3', '🌳', 110),
    ]
    parts.append(qtable(hwa))
    parts.append(pb_close())
    parts.append(page_break())

    # Page 6: Error table + Mnemonic + Strategy
    parts.append(pb_open())
    parts.append(h1('六、常見錯誤辨析表（The Error Table）'))
    errors = [
        ('1', 'T8 — 死守算術', '每次解題都用逆向運算不肯用方程', '對代數方法缺乏信心', '從簡單題開始練習用方程，循序漸進', '同一題兩種方法都做，比較效率', '🔴 高'),
        ('2', 'T2 — 設錯變數', '設的變數不是題目問的量', '未細心讀題就設 x', '設的變數 = 題目要求的未知數', '讀題時圈出「求什麼」', '🔴 高'),
        ('3', 'T3 — 翻譯錯誤', '「比...少」寫成 ＋ 號', '中文關鍵詞的數學對應不熟', '建立中→數關鍵詞對照表', '每次做題前默念對照表', '🟡 中'),
        ('4', 'T5 — 代數運算錯', '移項時符號出錯', '移項規則未熟練', '移項 → 變號：+變-、-變+', '檢查：左邊移去右邊→變號', '🔴 高'),
        ('5', 'T6 — 不懂概括', '無法從數字規律寫出第 n 項', '未建立公差與 n 的關係概念', '第 n 項 = 公差 × n + 初項調整值', '先寫出前 3 項驗證公式', '🟡 中'),
        ('6', 'T10 — 混合方法混亂', '同一題中混用算術和代數導致錯誤', '未先決定用哪種方法', '決定一種方法 → 堅持到最後', '在題目旁標註「用代數」或「用算術」', '🟡 中'),
        ('7', 'T1 — 忘記單位', '方程解出的數沒有標單位', '注意力集中在代數運算', '答案必須帶單位（除非是純數字題）', '最後一步檢查單位', '🟡 中'),
    ]
    parts.append(error_table(errors))

    parts.append(mn('🧠 「算術倒推、代數建模。死守算術唔抵爭，學識 let x 就係贏。關鍵詞翻譯要準，移項記得要變號！」'))
    parts.append(mn('🧠 「第 n 項 = 公差 × n + 初項差。先搵公差再調整，用 n=1 驗證公式啱唔啱！」'))

    parts.append(h1('七、解題策略卡（4-Step Strategy Cards）'))
    parts.append(sc_cards([
        ('①', '讀題設變數', '圈出題目要求的量 → 設為 x（或其他字母）→ 寫清楚單位'),
        ('②', '翻譯建方程', '用關鍵詞對照表將中文轉為數學符號 → 寫出等式'),
        ('③', '解方程驗算', '移項變號 → 合併同類項 → 解出 x → 代入原題驗證'),
        ('④', '寫答案連單位', '答案 = 數值 + 單位 → 檢查是否合理 → 寫總結句'),
    ]))

    parts.append(FOOTER.replace('LF-P6-下-LXX', lesson_code))
    parts.append(pb_close())

    parts.append(html_tail())

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))

    print(f"  [OK] L39 written: {filepath}")
    return filepath


def gen_l40():
    """L40: 學期總結+暑假中學預習計劃"""
    svgs = gen_all_svgs()
    lesson_code = "LF-P6-下-L40"
    title = "學期總結+暑假中學預習計劃"
    lesson_num = 40
    filepath = os.path.join(OUTPUT_DIR, f"{lesson_code}_學期總結暑假中學預習計劃.html")

    parts = [html_head(title, lesson_code)]

    parts.append(cover_page(lesson_code, lesson_num, title, '65 分鐘',
        '🪤 T1-T10 全覆蓋回顧 · 自我診斷 · 中一銜接規劃',
        '<span class="ss sh">🔴 總結</span> P6 全年 40 堂總結 + SSPA 考後中一準備',
        'P6 上下學期全部 40 堂內容',
        '❶ 全年知識點總檢查 ❷ T1-T10 陷阱掌握度自評 ❸ SSPA 分數預測 ❹ 8 週暑假預習計劃'))

    # Page 2: Topic checklist + Growth path
    parts.append(pb_open())
    parts.append(h1('一、P6 全年 40 堂知識點總檢查'))
    parts.append('<p style="font-size:11px;color:var(--gray);">✓ = 完全掌握 | △ = 部分掌握 | ✗ = 需要重溫</p>')

    parts.append(geom_div(svgs['growth_path']))

    # Topic checklist
    topics = [
        ('上學期 L1-L10', [
            ('L1', '小數除法', 'T5'),
            ('L2', '分數小數百分數互換', 'T1'),
            ('L3', '綜合應用', 'T10'),
            ('L4', '百分數佔比求原值', 'T2'),
            ('L5', '百分數增減連續變化', 'T2'),
            ('L6', '圓周與圓面積', 'T4'),
            ('L7', 'SSPA 模擬 1', 'ALL'),
            ('L8', '平均數與速率基礎', 'T3'),
            ('L9', '速率應用', 'T3'),
            ('L10', '綜合百分數平均數速率', 'T10'),
        ]),
        ('上學期 L11-L20', [
            ('L11', 'SSPA 計算題滿分', 'ALL'),
            ('L12', 'SSPA 應用題幾何題滿分', 'ALL'),
            ('L13', 'SSPA 模擬 2', 'ALL'),
            ('L14', '速率應用題進階', 'T3'),
            ('L15', '折線圖閱讀製作', 'T7'),
            ('L16', '容量與體積進階', 'T6'),
            ('L17', '圓形圖閱讀製作', 'T7'),
            ('L18', '綜合圖表幾何測量', 'T7,T10'),
            ('L19', 'SSPA 模擬 3', 'ALL'),
            ('L20', '學期總結寒假 SSPA 計劃', 'ALL'),
        ]),
        ('下學期 L21-L30', [
            ('L21', '圓的認識進階', 'T4'),
            ('L22', '圓面積進階應用', 'T2,T4'),
            ('L23', '百分數應用進階', 'T2'),
            ('L24', '方程進階', 'T8'),
            ('L25', '列方程解應用題進階', 'T8'),
            ('L26', '圓形圖閱讀製作', 'T7'),
            ('L27', '綜合統計圖表', 'T7,T10'),
            ('L28', '速率應用進階', 'T3'),
            ('L29', '容量體積進階（排水法）', 'T6'),
            ('L30', 'SSPA 模擬 4', 'ALL'),
        ]),
        ('下學期 L31-L40', [
            ('L31', 'SSPA 跨課題殺手題：計算篇', 'T10'),
            ('L32', 'SSPA 跨課題殺手題：應用幾何篇', 'T10'),
            ('L33', 'SSPA 模擬 5：終極考前最後一戰', 'ALL'),
            ('L34', '個人弱項終極補底', 'ALL'),
            ('L35', '中一預習：負數代數式', 'T8'),
            ('L36', '中一預習：不等式坐標系', 'T8'),
            ('L37', '中一預習：面積體積公式擴展', 'T2,T4'),
            ('L38', 'SSPA 終極殺手題：混合 3+ 陷阱', 'T10'),
            ('L39', '中學數學思維轉換', 'T8'),
            ('L40', '學期總結 + 暑假預習計劃', 'ALL'),
        ]),
    ]

    for section_title, rows in topics:
        parts.append(f'<h2>{section_title}</h2>')
        parts.append('<table class="qt"><tr><th class="qn">堂次</th><th>主題</th><th>主要陷阱</th><th style="width:50px;">✓△✗</th><th>備註</th></tr>')
        for lid, tname, traps in rows:
            parts.append(f'<tr><td class="qn">{lid}</td><td class="qtxt" style="font-size:11px;">{tname}</td><td style="font-size:10px;">{traps}</td><td class="qw" style="min-height:28px;"></td><td class="qw" style="min-height:28px;"></td></tr>')
        parts.append('</table>')

    parts.append(pb_close())
    parts.append(page_break())

    # Page 3: T1-T10 Self-assessment + SSPA Projection
    parts.append(pb_open())
    parts.append(h1('二、T1-T10 陷阱掌握度自我評估'))

    parts.append('''<table class="et">
<tr><th>Trap</th><th>陷阱名稱</th><th>自我評分 (1-5)</th><th>備註/例子</th></tr>
<tr><td>T1</td><td>單位混用 — m/cm、cm³/mL 不換算</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T2</td><td>公式混淆 — 圓周 vs 圓面積、利潤率 vs 折扣率</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T3</td><td>條件遺漏 — 停車時間、半圓忘加直徑</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T4</td><td>幾何誤判 — 周長/面積混淆、截面方向</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T5</td><td>計算失誤 — π 取錯值、進位錯誤</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T6</td><td>概念混淆 — 排水法用總水位×底面積</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T7</td><td>圖表誤讀 — 誤讀棒形圖/圓形圖刻度/圖例</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T8</td><td>方程設錯 — 變數設錯、移項未變號</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T9</td><td>換算數量級 — m³→cm³ 乘 100 而非 1,000,000</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td>T10</td><td>跨課題混亂 — 無法判斷用哪個知識點</td><td class="qw" style="min-height:30px;"></td><td class="qw" style="min-height:30px;"></td></tr>
</table>''')

    parts.append(h1('三、SSPA 最終分數預測模板'))
    parts.append('''<div style="background:var(--lightbg);border:2px solid var(--borderc);border-radius:8px;padding:16px;margin:8px 0;">
<table style="width:100%;font-size:12px;line-height:2;">
<tr><td><b>模擬 1 分數：</b></td><td style="border-bottom:1px solid var(--borderc);width:120px;"></td><td>/100</td><td><b>日期：</b></td><td style="border-bottom:1px solid var(--borderc);width:100px;"></td></tr>
<tr><td><b>模擬 2 分數：</b></td><td style="border-bottom:1px solid var(--borderc);"></td><td>/100</td><td><b>日期：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr><td><b>模擬 3 分數：</b></td><td style="border-bottom:1px solid var(--borderc);"></td><td>/100</td><td><b>日期：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr><td><b>模擬 4 分數：</b></td><td style="border-bottom:1px solid var(--borderc);"></td><td>/100</td><td><b>日期：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr><td><b>模擬 5 分數：</b></td><td style="border-bottom:1px solid var(--borderc);"></td><td>/100</td><td><b>日期：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr style="background:#FEF3C7;"><td><b>預測 SSPA 分數：</b></td><td style="border-bottom:1px solid var(--borderc);"></td><td>/100</td><td><b>目標 Band：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
</table>
</div>''')

    parts.append(h1('四、中學數學準備度自我評估'))
    parts.append('''<table class="qt">
<tr><th class="qn">#</th><th>能力指標</th><th style="width:180px;">自我評分 (1=唔識, 5=好熟)</th></tr>
<tr><td class="qn">1</td><td class="qtxt">我能熟練使用方程（let x=...）解決應用題</td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td class="qn">2</td><td class="qtxt">我能計算棱柱和圓柱的體積與表面積</td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td class="qn">3</td><td class="qtxt">我能處理負數的四則運算</td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td class="qn">4</td><td class="qtxt">我能化簡代數式（合併同類項）</td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td class="qn">5</td><td class="qtxt">我理解坐標系的基本概念</td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td class="qn">6</td><td class="qtxt">我能從文字題翻譯出方程</td><td class="qw" style="min-height:30px;"></td></tr>
<tr><td class="qn">7</td><td class="qtxt">我理解不等式的意義（>, <, ≥, ≤）</td><td class="qw" style="min-height:30px;"></td></tr>
</table>''')

    parts.append(pb_close())
    parts.append(page_break())

    # Page 4: 8-week summer plan
    parts.append(pb_open())
    parts.append(h1('五、8 週暑假中學預習計劃模板'))

    plan = [
        ('第 1 週<br>（7月中）', '負數四則運算', '正負數加減乘除、絕對值', 'L35 內容 + 課本第一章', '每日 30 分鐘', 60),
        ('第 2 週<br>（7月尾）', '代數式化簡', '合併同類項、展開括號、代入求值', 'L35 內容 + 練習題', '每日 30 分鐘', 60),
        ('第 3 週<br>（8月初）', '一元一次方程', '移項、解方程、文字題列方程', 'L24-25 + L39', '每日 30 分鐘', 60),
        ('第 4 週<br>（8月中）', '面積體積公式', '棱柱體積、圓柱體積表面積', 'L37 內容 + 課本', '每日 30 分鐘', 60),
        ('第 5 週<br>（8月尾）', '坐標系入門', '直角坐標、點的坐標、距離', 'L36 內容 + 練習', '每日 30 分鐘', 60),
        ('第 6 週<br>（8月尾）', '不等式基礎', '不等式符號、解不等式、數線', 'L36 內容 + 課本', '每日 30 分鐘', 60),
        ('第 7 週<br>（8月尾）', '綜合複習 1', '複習第 1-3 週內容 + 測驗', '自製測驗卷', '每日 45 分鐘', 60),
        ('第 8 週<br>（開學前）', '綜合複習 2', '複習第 4-6 週內容 + 模擬', '中一上學期預習卷', '每日 45 分鐘', 60),
    ]

    for week, topic, content, resources, time, min_h in plan:
        parts.append(f'''<div style="background:var(--lightbg);border:1px solid var(--borderc);border-radius:6px;padding:10px 14px;margin:6px 0;">
<div style="font-size:14px;font-weight:900;color:var(--blue);">{week}: {topic}</div>
<div style="font-size:11px;color:var(--gray);margin:3px 0;">內容：{content}</div>
<div style="display:flex;gap:16px;font-size:10px;color:var(--gray);">
<span>資源：{resources}</span><span>時間：{time}</span>
</div>
<div style="margin-top:4px;font-size:10px;">完成記錄：<span style="display:inline-block;width:80px;border-bottom:1px solid var(--borderc);"></span> 進度：___ / 7 日</div>
</div>''')

    parts.append(h1('六、推薦學習資源'))
    parts.append('''<table class="qt">
<tr><th>資源類型</th><th>名稱</th><th>用途</th></tr>
<tr><td>教科書</td><td>《數學新思維（第二版）》1A 冊</td><td>中一上學期正規教材</td></tr>
<tr><td>練習</td><td>《課室初中數學練習》1A</td><td>額外練習題</td></tr>
<tr><td>網站</td><td>教育局 EDB 數學教育組</td><td>教學資源和範例</td></tr>
<tr><td>網站</td><td>Khan Academy (中英版)</td><td>免費影片教學 + 練習</td></tr>
<tr><td>App</td><td>GeoGebra (免費)</td><td>互動幾何繪圖和探索</td></tr>
<tr><td>App</td><td>Desmos 科學計算機</td><td>免費圖形計算機</td></tr>
<tr><td>書籍</td><td>《數學大觀念》（The Math Book）</td><td>培養數學興趣和思維</td></tr>
</table>''')

    parts.append(pb_close())
    parts.append(page_break())

    # Page 5: Reflection + Goal Setting
    parts.append(pb_open())
    parts.append(h1('七、個人反思：我的數學旅程 P3 → P6'))
    parts.append('''<div style="background:var(--lightbg);border:2px solid var(--borderc);border-radius:8px;padding:16px;margin:8px 0;">
<p style="font-weight:700;color:var(--blue);margin-bottom:8px;">請根據以下提示寫出你的數學學習旅程反思：</p>
<ol style="font-size:11px;line-height:2.2;padding-left:20px;">
<li><b>P3 的時候，你覺得數學最難的是什麼？現在回頭看，那時的問題還難嗎？</b></li>
<li style="min-height:45px;border-bottom:1px dashed #D1D5DB;margin-bottom:8px;"></li>
<li><b>P5-P6 這兩年，你覺得自己進步最多的是哪個範疇？（計算/應用題/幾何/圖表/方程）</b></li>
<li style="min-height:45px;border-bottom:1px dashed #D1D5DB;margin-bottom:8px;"></li>
<li><b>在 SSPA 呈分試中，哪一種陷阱（T1-T10）你覺得自己最容易中招？你打算怎樣改善？</b></li>
<li style="min-height:45px;border-bottom:1px dashed #D1D5DB;margin-bottom:8px;"></li>
<li><b>用一個詞語形容你對中學數學的感覺：興奮 / 緊張 / 期待 / 害怕 / 其他：______</b></li>
<li style="min-height:30px;border-bottom:1px dashed #D1D5DB;margin-bottom:8px;"></li>
<li><b>為什麼？寫 2-3 句話解釋。</b></li>
<li style="min-height:45px;border-bottom:1px dashed #D1D5DB;margin-bottom:8px;"></li>
</ol>
</div>''')

    parts.append(h1('八、中一目標設定'))
    parts.append('''<div style="background:#FFFBEB;border:2px solid var(--gold);border-radius:8px;padding:16px;margin:8px 0;">
<p style="font-weight:900;color:var(--blue);margin-bottom:12px;font-family:Noto Serif HK,serif;font-size:15px;">中一數學目標宣言</p>
<table style="width:100%;font-size:11px;line-height:2.5;">
<tr><td style="width:120px;"><b>我的目標分數：</b></td><td style="border-bottom:1px solid var(--borderc);">______ / 100</td></tr>
<tr><td><b>我想進步的範疇：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr><td><b>我每週會用多少時間溫數學：</b></td><td style="border-bottom:1px solid var(--borderc);">______ 小時</td></tr>
<tr><td><b>我的數學偶像/榜樣：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
<tr><td><b>如果遇到困難，我會：</b></td><td style="border-bottom:1px solid var(--borderc);"></td></tr>
</table>
</div>''')

    parts.append(magic_box('記住：數學唔係睇你有幾聰明，係睇你有幾堅持。每次跌倒，都係離成功更近一步。中學數學係新賽道，你已經準備好！', 'green'))

    parts.append(geom_div(svgs['growth_path']))

    parts.append(mn('🧠 「P3 到 P6 你已經過咗咁多關，中學只係下一個挑戰。記住：唔係你唔夠聰明，係你未搵到啱嘅方法。霖楓學苑教你嘅唔係數學，係點樣避開陷阱。呢個能力，會跟足你一世。」'))

    parts.append(pb_close())
    parts.append(page_break())

    # Page 6: Final reflection + strategy + footer
    parts.append(pb_open())
    parts.append(h1('九、老師/家長留言區'))
    parts.append('<div style="min-height:150px;border:2px dashed var(--borderc);border-radius:8px;padding:14px;margin:8px 0;"></div>')

    parts.append(h1('十、我的 SSPA 必勝宣言'))
    parts.append('''<div style="background:#F0FDF4;border:2px solid #BBF7D0;border-radius:12px;padding:20px;text-align:center;margin:12px 0;">
<div style="font-family:Noto Serif HK,serif;font-size:18px;font-weight:900;color:var(--green);margin-bottom:12px;">我承諾：</div>
<ol style="text-align:left;font-size:12px;line-height:2.2;padding-left:24px;max-width:400px;margin:0 auto;">
<li>每次做題前，先圈出關鍵詞和陷阱提示</li>
<li>計算後檢查單位是否正確</li>
<li>遇到綜合題，先拆解再逐步解決</li>
<li>不確定的時候，用第二種方法驗算</li>
<li>相信自己：我有能力避開所有陷阱！</li>
</ol>
<p style="margin-top:16px;font-size:14px;font-weight:700;color:var(--blue);">簽名：___________________ &nbsp;&nbsp; 日期：___________________</p>
</div>''')

    parts.append(h1('十一、解題策略終極卡（適合所有題型）'))
    parts.append(sc_cards([
        ('①', '讀題圈關鍵', '圈出：單位、陷阱詞（「完全浸沒」、「停留」）、問題要求'),
        ('②', '拆解分步', '綜合題 = 幾個小題的組合。逐一標號，逐步解決。'),
        ('③', '選公式代數', '選定方法（算術/代數）→ 套公式 → 小心計算'),
        ('④', '驗算防陷阱', '用逆向/估算/單位檢查 → 答案合理嗎？→ 寫答案+單位'),
    ]))

    parts.append(FOOTER.replace('LF-P6-下-LXX', lesson_code))
    parts.append(pb_close())

    parts.append(html_tail())

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))

    print(f"  [OK] L40 written: {filepath}")
    return filepath


# ═══════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════

if __name__ == '__main__':
    print("=" * 60)
    print("霖楓學苑 · LF Academy — P6 下學期 6 MISSING Handouts")
    print("=" * 60)
    print()

    files = []
    files.append(gen_l29())
    files.append(gen_l30())
    files.append(gen_l37())
    files.append(gen_l38())
    files.append(gen_l39())
    files.append(gen_l40())

    print()
    print("=" * 60)
    print(f"ALL DONE. {len(files)} files created:")
    for f in files:
        print(f"  {f}")
    print("=" * 60)
