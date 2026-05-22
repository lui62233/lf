#!/usr/bin/env python3
"""Complete SVG replacement for P5 handouts L06, L18, L21 using svg_geometry v2.3.
Handles ALL replacements in one pass. Imports directly to avoid encoding issues.
Non-geometric SVGs (line-segment, balance-scale, compass) are kept as-is."""

import re, sys, os

sys.path.insert(0, r'G:\lam-fung-academy\_tools')
import svg_geometry as sg

# ---------------------------------------------------------------------------
# Files and their replacement maps
# Format: { label: (filepath, [replacement or None, ...]) }
# None = keep original SVG. The list length must match the number of <svg>
# blocks found in the file.
# ---------------------------------------------------------------------------

FILES = {
    'L06': (
        r'G:\lam-fung-academy\講義\P5\LF-P5-上-L06-綜合-面積-多位數-估算-v1.html',
        [sg.rectangle(l=200, w=120)],
    ),
    'L18': (
        r'G:\lam-fung-academy\講義\P5\LF-P5-上-L18_上學期陷阱總複習-圖形與方程.html',
        [
            sg.triangle(b=100, h=60, tt='right'),          # 0: triangle area trap
            sg.trapezoid(u=40, lo=80, h=50),               # 1: trapezoid area trap
            None,                                          # 2: balance scale (keep)
            sg.rectangle(l=120, w=90),                     # 3: rectangle (already tool, re-assert)
        ],
    ),
    'L21': (
        r'G:\lam-fung-academy\講義\P5\LF-P5-下-L21_圓的認識.html',
        [
            None,                                          # 0: line segment AB (Q4)
            sg.circle_shape(r=100),                         # 1: circle O/r/d
            None,                                          # 2: compass drawing (keep)
            sg.square(s=150),                               # 3: square a^2
            sg.circle_shape(r=60),                          # 4: circle (real-life)
        ],
    ),
}

SVG_RE = re.compile(r'<svg\b.*?</svg>', re.DOTALL)

for name, (filepath, repl_list) in FILES.items():
    print(f'\n{"="*60}')
    print(f'Processing {name}: {os.path.basename(filepath)}')

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    matches = list(SVG_RE.finditer(html))
    print(f'  Found {len(matches)} SVGs, {len(repl_list)} replacements')

    if len(matches) != len(repl_list):
        print(f'  *** COUNT MISMATCH! SVG count={len(matches)}, replacement count={len(repl_list)}')
        # Show what we found to help debug
        for i, m in enumerate(matches):
            snippet = m.group()[:100].replace('\n',' ')[:80]
            print(f'    SVG[{i}] pos={m.start()} len={len(m.group())} start={snippet}...')
        continue

    # Build new HTML: text-before + replacement + text-after for each SVG
    parts = []
    last_end = 0
    for i, (m, repl) in enumerate(zip(matches, repl_list)):
        parts.append(html[last_end:m.start()])
        if repl is None:
            parts.append(m.group())
            action = 'KEEP'
        else:
            parts.append(repl)
            action = 'REPLACE'
        delta = len(parts[-1]) - (m.end() - m.start())
        print(f'  [{i}] {action}: {m.end()-m.start()} -> {len(parts[-1])} bytes ({delta:+d})')
        last_end = m.end()
    parts.append(html[last_end:])

    new_html = ''.join(parts)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'  Written: {len(new_html)} chars')

print('\nDone! All files updated.')
