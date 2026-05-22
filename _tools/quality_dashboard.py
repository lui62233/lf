#!/usr/bin/env python3
"""
霖楓學苑 · LF Academy — System Quality Dashboard
Scans all handouts across all grades and reports:
- Handout counts (HTML + PDF)
- SVG counts per handout
- Answer space health
- Page counts (from PDFs)
- Missing PDFs
- Zero-SVG handouts (potential quality issues)
"""
import os, glob, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pymupdf

BASE = r'G:\lam-fung-academy\講義'

def scan_grade(grade_path, grade_name):
    """Scan one grade directory and return stats."""
    html_files = sorted(glob.glob(os.path.join(grade_path, '*.html')))
    results = []
    for f in html_files:
        name = os.path.basename(f)
        pdf = f.replace('.html', '.pdf')
        has_pdf = os.path.exists(pdf)

        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()

        svgs = content.count('<svg')
        has_grid = 'repeating-linear-gradient' in content
        has_cover = 'cover-page' in content or 'cv-logo' in content
        has_trap = 'tc-w' in content and 'tc-r' in content
        has_error_table = 'class="et"' in content
        has_mnemonic = 'class="mn"' in content
        has_footer = '不教數學' in content

        pages = 0
        if has_pdf:
            try:
                doc = pymupdf.open(pdf)
                pages = len(doc)
                doc.close()
            except:
                pages = -1

        results.append({
            'name': name,
            'svgs': svgs,
            'pages': pages,
            'has_pdf': has_pdf,
            'has_grid': has_grid,
            'has_cover': has_cover,
            'has_trap': has_trap,
            'has_error_table': has_error_table,
            'has_mnemonic': has_mnemonic,
            'has_footer': has_footer,
            'size_kb': len(content) // 1024,
            'quality_score': sum([has_grid, has_cover, has_trap, has_error_table, has_mnemonic, has_footer])
        })

    return results

print('=' * 70)
print('霖楓學苑 · LF Academy — System Quality Dashboard')
print('=' * 70)

all_results = {}
total_html = 0
total_pdf = 0
total_svgs = 0
zero_svg_handouts = []
low_quality = []

for grade, path in [('P3', os.path.join(BASE, 'P3')),
                     ('P4', os.path.join(BASE, 'P4')),
                     ('P5', os.path.join(BASE, 'P5')),
                     ('P6', os.path.join(BASE, 'P6'))]:
    if not os.path.exists(path):
        print(f'\n{grade}: Directory not found')
        continue

    results = scan_grade(path, grade)
    all_results[grade] = results

    html_count = len(results)
    pdf_count = sum(1 for r in results if r['has_pdf'])
    svg_count = sum(r['svgs'] for r in results)
    avg_pages = sum(r['pages'] for r in results if r['pages'] > 0) / max(1, sum(1 for r in results if r['pages'] > 0))
    avg_svgs = svg_count / max(1, html_count)
    avg_quality = sum(r['quality_score'] for r in results) / max(1, html_count)

    total_html += html_count
    total_pdf += pdf_count
    total_svgs += svg_count

    print(f'\n{"─"*70}')
    print(f'{grade} | {html_count} HTML | {pdf_count} PDF | {svg_count} total SVGs | {avg_svgs:.1f} SVGs/堂 | {avg_pages:.0f}pp avg | Quality {avg_quality:.1f}/6')

    # Flag issues
    for r in results:
        if r['svgs'] == 0:
            # Check if it's a computation-focused topic (acceptable) or geometry (problem)
            name_lower = r['name'].lower()
            geom_keywords = ['面積', '體積', '圖形', '立體', '圓', '圖表', '棒形', '折線', '排水', '形狀', '周界']
            chart_keywords = ['統計', '數據', '圓形圖', '棒形圖', '折線圖']
            if any(k in name_lower for k in geom_keywords + chart_keywords):
                zero_svg_handouts.append(f'{grade}: {r["name"][:60]} ({r["pages"]}pp, GEOM/CHART topic!)')
        if r['quality_score'] < 4:
            low_quality.append(f'{grade}: {r["name"][:60]} (score {r["quality_score"]}/6)')

print(f'\n{"="*70}')
print(f'TOTALS: {total_html} HTML | {total_pdf} PDF | {total_svgs} SVGs across all grades')
print(f'{"="*70}')

print(f'\n{"="*70}')
print('Dashboard complete.')
