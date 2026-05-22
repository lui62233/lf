#!/usr/bin/env python3
"""
P3/P4 Handout Quality Audit Script
Checks 17 structural/semantic elements across all 80 files
"""
import os, re, json, csv
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict

P3_DIR = r"G:\lam-fung-academy\講義\P3"
P4_DIR = r"G:\lam-fung-academy\講義\P4"
OUTPUT_CSV = r"G:\lam-fung-academy\_operations\p3_p4_audit_raw.csv"
OUTPUT_JSON = r"G:\lam-fung-academy\_operations\p3_p4_audit_raw.json"

RESULTS = []

def audit_file(filepath):
    level = "P3" if "P3" in filepath else "P4"
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    issues = []
    score = 6  # start at 6, subtract for issues

    # ─── 1. COVER PAGE ───
    has_logo = bool(soup.select_one('.cv-logo'))
    has_badge = bool(soup.select_one('.cv-badge'))
    has_title = bool(soup.select_one('.cv-title'))
    has_sub = bool(soup.select_one('.cv-sub'))
    has_info = bool(soup.select_one('.cv-info'))
    has_row = bool(soup.select_one('.cv-row'))

    if not has_logo: issues.append("MISSING: cover logo (.cv-logo)")
    if not has_badge: issues.append("MISSING: cover badge (.cv-badge)")
    if not has_title: issues.append("MISSING: cover title (.cv-title)")
    if not has_sub: issues.append("MISSING: cover subtitle (.cv-sub)")
    if not has_info: issues.append("MISSING: cover info box (.cv-info)")
    if not has_row: issues.append("MISSING: cover name/class row (.cv-row)")

    # Check cover info fields
    if has_info:
        info_text = soup.select_one('.cv-info').get_text()
        info_checks = {
            "對應教材": "對應教材" in info_text,
            "核心陷阱": "核心陷阱" in info_text or "陷阱" in info_text,
            "SSPA 關聯": "SSPA" in info_text,
            "前置知識": "前置知識" in info_text,
            "本堂目標": "本堂目標" in info_text
        }
        for k, v in info_checks.items():
            if not v:
                issues.append(f"COVER INFO missing: {k}")

    # ─── 2. ERROR TABLE (.et) ───
    et = soup.select_one('.et')
    if et:
        et_rows = et.select('tr')
        et_data_rows = et.select('tbody tr') if et.select('tbody') else et.select('tr')[1:]  # skip header
        if len(et_data_rows) < 6:
            issues.append(f"Error table has only {len(et_data_rows)} rows (need >=6)")
    else:
        issues.append("MISSING: error table (.et)")

    # ─── 3. FOOTER ───
    end_notes = soup.select('.end-note')
    has_footer = False
    for en in end_notes:
        if "不教數學" in en.get_text() or "避開陷阱" in en.get_text():
            has_footer = True
            break
    if not has_footer:
        issues.append("MISSING: footer with '不教數學，教避開陷阱'")

    # ─── 4. ANSWER GRID LINES ───
    style_text = html
    has_grid = 'repeating-linear-gradient' in style_text
    if not has_grid:
        issues.append("MISSING: repeating-linear-gradient for answer grid lines")

    # ─── 5. PRINT CSS ───
    has_print = '@media print' in style_text
    if not has_print:
        issues.append("MISSING: @media print CSS")

    # ─── 6. TRAP COMPARISON (.tc) ───
    has_tc = bool(soup.select_one('.tc'))
    tc_w = bool(soup.select_one('.tc-w'))
    tc_r = bool(soup.select_one('.tc-r'))
    if not has_tc:
        issues.append("MISSING: trap comparison (.tc) - core pedagogy element")
    elif not tc_w:
        issues.append("MISSING: ❌ wrong answer panel (.tc-w)")
    elif not tc_r:
        issues.append("MISSING: ✅ correct answer panel (.tc-r)")

    # ─── 7. MNEMONIC (.mn) ───
    mn = soup.select('.mn')
    if not mn:
        issues.append("MISSING: mnemonic 口訣 (.mn)")
    else:
        for m in mn:
            mtext = m.get_text().strip()
            if len(mtext) < 8:
                issues.append(f"Mnemonic too short: '{mtext[:40]}'")

    # ─── 8. WARM-UP ───
    has_warmup = '熱身' in html or 'warm' in html.lower()
    if not has_warmup:
        issues.append("MISSING: warm-up section")

    # ─── 9. WARNINGS (.warn) ───
    warns = soup.select('.warn')
    if len(warns) < 1:
        issues.append("MISSING: warning alerts (.warn)")

    # ─── 10. STEP CARDS (.sc) ───
    sc = soup.select('.sc')
    if not sc:
        # Not strictly required for all lessons, note but don't subtract score
        issues.append("NOTE: no step cards (.sc) — may be OK for some lesson types")

    # ─── 11. FONT SIZE (P3/P4 should be slightly larger) ───
    body_font = ''
    font_match = re.search(r'body\s*\{[^}]*font-size:\s*(\d+)px', style_text, re.DOTALL)
    if font_match:
        body_font = int(font_match.group(1))
        if body_font < 12:
            issues.append(f"Body font size is {body_font}px — too small for {level}")

    # ─── 12. CONTENT SECTION CHECK ───
    sections = soup.select('.h1')
    if len(sections) < 3:
        issues.append(f"Only {len(sections)} section headers (.h1) — seems thin")

    # ─── 13. QUESTION TABLE (.qt) ───
    qt = soup.select('.qt')
    if not qt:
        issues.append("MISSING: question tables (.qt)")

    # ─── 14. KP SECTION (.kp) ───
    kps = soup.select('.kp')
    if len(kps) < 1:
        issues.append("MISSING: knowledge point sections (.kp)")

    # ─── 15. SSPA MARKERS ───
    has_sspa = 'SSPA' in html or '呈分試' in html
    if not has_sspa:
        issues.append("MISSING: SSPA/呈分試 references")

    # ─── 16. MATH CONTENT ───
    has_math = bool(soup.select('.f, .fd, .fi')) or '\\frac' in html or 'LCM' in html
    if not has_math:
        # Some lessons may legitimately have no fractions (e.g., direction)
        pass

    # ─── 17. FIGURE ELEMENTS (for geometry lessons) ───
    has_svg = bool(soup.select('svg'))
    fig_labels = soup.select('.fig-label, .fig-title, .fig-card')

    # Calculate scores
    critical_issues = [i for i in issues if i.startswith("MISSING:") and "NOTE:" not in i]
    minor_issues = [i for i in issues if i.startswith("NOTE:")]
    error_table_issue = [i for i in issues if "Error table" in i]

    # Score calculation
    score = 6
    if len(critical_issues) >= 5: score = 1
    elif len(critical_issues) >= 4: score = 2
    elif len(critical_issues) >= 3: score = 3
    elif len(critical_issues) >= 2: score = 4
    elif len(critical_issues) >= 1: score = 5

    result = {
        "file": filename,
        "level": level,
        "path": filepath,
        "score": score,
        "critical_count": len(critical_issues),
        "minor_count": len(minor_issues),
        "total_issues": len(issues),
        "issues": issues,
        "has_cover": all([has_logo, has_badge, has_title, has_sub, has_info, has_row]),
        "has_et": bool(et),
        "has_footer": has_footer,
        "has_grid": has_grid,
        "has_print": has_print,
        "has_trap_compare": has_tc,
        "has_mnemonic": bool(mn),
        "mnemonic_count": len(mn),
        "warn_count": len(warns),
        "section_count": len(sections),
        "kp_count": len(kps),
        "qt_count": len(qt),
        "has_svg": has_svg,
        "has_sspa": has_sspa,
        "body_font": body_font
    }

    return result

def main():
    all_files = []
    for d in [P3_DIR, P4_DIR]:
        if os.path.exists(d):
            for f in sorted(os.listdir(d)):
                if f.endswith('.html'):
                    all_files.append(os.path.join(d, f))

    print(f"Found {len(all_files)} HTML files to audit")

    for fp in all_files:
        print(f"  Auditing: {os.path.basename(fp)}...")
        try:
            r = audit_file(fp)
            RESULTS.append(r)
        except Exception as e:
            print(f"  ERROR in {fp}: {e}")
            RESULTS.append({
                "file": os.path.basename(fp),
                "level": "P3" if "P3" in fp else "P4",
                "path": fp,
                "score": 0,
                "critical_count": 999,
                "minor_count": 0,
                "total_issues": 1,
                "issues": [f"PARSE ERROR: {str(e)}"],
                "error": str(e)
            })

    # Statistics
    p3 = [r for r in RESULTS if r['level'] == 'P3']
    p4 = [r for r in RESULTS if r['level'] == 'P4']

    print(f"\n{'='*60}")
    print(f"AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"Total files: {len(RESULTS)} (P3: {len(p3)}, P4: {len(p4)})")

    # Score distribution
    score_dist = defaultdict(int)
    for r in RESULTS:
        score_dist[r['score']] += 1
    for s in range(7):
        print(f"  Score {s}/6: {score_dist.get(s, 0)} files")

    # Common issues
    issue_counts = defaultdict(int)
    for r in RESULTS:
        for issue in r['issues']:
            # Normalize issue text
            key = issue.split(':')[0] if ':' in issue else issue
            issue_counts[key] += 1

    print(f"\nTop 10 issues:")
    for k, v in sorted(issue_counts.items(), key=lambda x: -x[1])[:10]:
        print(f"  [{v:3d}] {k}")

    # Template completeness rates
    print(f"\nTemplate element coverage:")
    for field in ['has_cover', 'has_et', 'has_footer', 'has_grid', 'has_print', 'has_trap_compare', 'has_mnemonic']:
        count = sum(1 for r in RESULTS if r[field])
        print(f"  {field}: {count}/{len(RESULTS)} ({100*count/len(RESULTS):.0f}%)")

    # Save raw data
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(RESULTS, f, ensure_ascii=False, indent=2)

    # Save CSV
    csv_fields = ['file', 'level', 'score', 'critical_count', 'has_cover', 'has_et', 'has_footer',
                  'has_grid', 'has_print', 'has_trap_compare', 'has_mnemonic', 'mnemonic_count',
                  'warn_count', 'section_count', 'kp_count', 'qt_count', 'has_svg', 'issues']
    with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
        writer.writeheader()
        for r in RESULTS:
            r_copy = {k: r.get(k, '') for k in csv_fields}
            r_copy['issues'] = ' | '.join(r['issues'])
            writer.writerow(r_copy)

    print(f"\nRaw data saved to: {OUTPUT_JSON}")
    print(f"CSV saved to: {OUTPUT_CSV}")

    # Also output files needing most attention
    print(f"\n{'='*60}")
    print(f"FILES NEEDING IMMEDIATE ATTENTION (score <= 3):")
    print(f"{'='*60}")
    for r in sorted(RESULTS, key=lambda x: x['score']):
        if r['score'] <= 3:
            print(f"\n  [{r['score']}/6] {r['level']} — {r['file']}")
            for issue in r['issues']:
                if not issue.startswith("NOTE:"):
                    print(f"    - {issue}")

if __name__ == '__main__':
    main()
