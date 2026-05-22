#!/usr/bin/env python3
"""Write SVGs to files with proper UTF-8 encoding"""
import sys
sys.path.insert(0, '.')
from gen_svgs import number_line, coordinate_plane, cylinder_3d, prism_triangular, cuboid_cylinder_composite, inequality_line, inequality_line2, bridge_diagram, growth_path

svgs = {
    'number_line': number_line,
    'coordinate_plane': coordinate_plane,
    'cylinder': cylinder_3d,
    'prism': prism_triangular,
    'composite': cuboid_cylinder_composite,
    'inequality1': inequality_line,
    'inequality2': inequality_line2,
    'bridge': bridge_diagram,
    'growth': growth_path,
}

for name, fn in svgs.items():
    try:
        svg = fn()
        with open(f'G:/lam-fung-academy/_tools/svg_{name}.svg', 'w', encoding='utf-8') as f:
            f.write(svg)
        print(f'OK: {name} ({len(svg)} chars)')
    except Exception as e:
        print(f'FAIL: {name}: {e}')

print('Done writing all SVGs')
