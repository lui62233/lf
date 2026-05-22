#!/usr/bin/env python3
"""Replace inline SVGs in P5 handouts with svg_geometry.py v2.3 output.
Handles L06, L18, L21. Imports directly to avoid subprocess encoding issues."""
import re, sys, os

TOOLS = r'G:\lam-fung-academy\_tools'
sys.path.insert(0, TOOLS)
import svg_geometry as sg

FILES = {
    'L06': r'G:\lam-fung-academy\講義\P5\LF-P5-上-L06-綜合-面積-多位數-估算-v1.html',
    'L18': r'G:\lam-fung-academy\講義\P5\LF-P5-上-L18_上學期陷阱總複習-圖形與方程.html',
    'L21': r'G:\lam-fung-academy\講義\P5\LF-P5-下-L21_圓的認識.html',
}

# Each entry: callable (function + kwargs) or None (keep original).
# The list length must = number of <svg> blocks in the file.
# None means keep the original SVG unchanged.
REPLACEMENTS = {
    'L06': [
        sg.rectangle(l=200, w=120),
    ],
    'L18': [
        None,                                                       # 0: line segment AB in Q4
        sg.triangle(b=100, h=60, tt='right'),                      # 1: triangle area trap
        sg.trapezoid(u=40, lo=80, h=50),                           # 2: trapezoid area trap
        None,                                                       # 3: balance scale (keep)
        sg.rectangle(l=120, w=90),                                  # 4: rectangle composite+eq
    ],
    'L21': [
        None,                                                       # 0: line segment AB in Q4
        sg.circle_shape(r=100),                                     # 1: circle O/r/d
        None,                                                       # 2: compass drawing (keep)
        sg.square(s=150),                                           # 3: square a^2
        sg.circle_shape(r=60),                                      # 4: circle for real-life
    ],
}

SVG_RE = re.compile(r'<svg\b.*?</svg>', re.DOTALL)

for name in ['L06', 'L18', 'L21']:
    filepath = FILES[name]
    print(f'\n{"="*60}')
    print(f'Processing {name}: {os.path.basename(filepath)}')

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    matches = list(SVG_RE.finditer(html))
    repl_list = REPLACEMENTS[name]
    print(f'  Found {len(matches)} SVGs, {len(repl_list)} entries in replacement list')

    if len(matches) != len(repl_list):
        print(f'  *** MISMATCH: SVG count != replacement count! Aborting.')
        continue

    # Build new HTML by concat: text before SVG + new SVG + ...
    parts = []
    last_end = 0
    for i, (m, repl) in enumerate(zip(matches, repl_list)):
        parts.append(html[last_end:m.start()])
        if repl is None:
            parts.append(m.group())
            kind = 'KEEP'
        else:
            parts.append(repl)
            kind = 'REPLACE'
        old_len = m.end() - m.start()
        new_len = len(parts[-1])
        print(f'  [{i}] {kind}: {old_len} -> {new_len} bytes')
        last_end = m.end()
    parts.append(html[last_end:])

    new_html = ''.join(parts)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'  Written: {len(new_html)} chars')

print('\nDone! All files updated.')
