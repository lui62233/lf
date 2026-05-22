#!/usr/bin/env python3
"""Generate custom SVGs for L35-L40 handouts"""
import sys
sys.path.insert(0, '.')

C={'fg':'#1A3C6D','fill':'#DBEAFE','fill2':'#DCFCE7','fill3':'#FEF3C7','water':'#BAE6FD','obj':'#93C5FD','red':'#DC2626','green':'#16A34A','gold':'#C9A84C','gray':'#6B7280','grid':'#D1D5DB','white':'#FFFFFF'}

def _sv(w,h,c): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{c}</svg>'
def _t(x,y,t,a='middle',s=13,c=None,b=True):
    cl=c or C['fg']; fw='font-weight="700"' if b else ''
    return f'<text x="{x}" y="{y}" text-anchor="{a}" font-size="{s}" fill="{cl}" {fw}>{t}</text>'
def _r(x,y,w,h,f=None,st=None,sw=3,da=None):
    fl=f or C['fill']; stl=st or C['fg']; d=f' stroke-dasharray="{da}"' if da else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fl}" stroke="{stl}" stroke-width="{sw}"{d}/>'
def _li(x1,y1,x2,y2,st=None,sw=2,da=None):
    stl=st or C['fg']; d=f' stroke-dasharray="{da}"' if da else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stl}" stroke-width="{sw}"{d}/>'

# ========== NUMBER LINE ==========
def number_line():
    w,h = 640, 120
    ox,oy = 40, 55
    step = 55
    body = ''
    body += _li(ox-10, oy, ox+step*12+10, oy, sw=2.5)
    body += f'<polygon points="{ox+step*12+10},{oy} {ox+step*12},{oy-6} {ox+step*12},{oy+6}" fill="{C["fg"]}"/>'
    labels = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for i, val in enumerate(labels):
        x = ox + (i+0)*step
        body += _li(x, oy-15, x, oy+15, sw=1.5)
        body += _t(x, oy+28, str(val), s=11 if val<0 else 12, c=C['red'] if val==0 else C['fg'])
    zero_x = ox + 5*step
    body += _li(zero_x, oy-20, zero_x, oy+20, st=C['red'], sw=3)
    body += _t(zero_x, oy-25, '0', s=14, c=C['red'])
    body += _t(ox-5, oy-22, '負數', s=11, c=C['red'], a='start')
    body += _t(ox+step*10+10, oy-22, '正數', s=11, c=C['green'], a='end')
    return _sv(w,h,body)

# ========== COORDINATE PLANE ==========
def coordinate_plane():
    w,h = 480, 480
    cx,cy = w//2, h//2
    step = 35
    body = ''
    for i in range(-6, 7):
        x = cx + i*step; y = cy + i*step
        body += _li(x, cy-6*step, x, cy+6*step, st=C['grid'], sw=0.6)
        body += _li(cx-6*step, y, cx+6*step, y, st=C['grid'], sw=0.6)
    body += _li(cx-6.5*step, cy, cx+6.5*step, cy, sw=2.5)
    body += _li(cx, cy-6.5*step+20, cx, cy+6.5*step, sw=2.5)
    body += f'<polygon points="{cx+6.5*step},{cy} {cx+6.5*step-8},{cy-5} {cx+6.5*step-8},{cy+5}" fill="{C["fg"]}"/>'
    body += f'<polygon points="{cx},{cy-6.5*step+20} {cx-5},{cy-6.5*step+28} {cx+5},{cy-6.5*step+28}" fill="{C["fg"]}"/>'
    body += _t(cx+6.5*step+12, cy+5, 'x', s=14)
    body += _t(cx+5, cy-6.5*step-12, 'y', s=14)
    for i in range(-5, 6):
        if i==0: continue
        x = cx + i*step
        body += _t(x, cy+16, str(i), s=9, c=C['gray'])
    for i in range(-5, 6):
        if i==0: continue
        y = cy - i*step
        body += _t(cx-14, y+4, str(i), s=9, c=C['gray'], a='end')
    body += _t(cx-10, cy+16, 'O', s=13, c=C['red'])
    body += _t(cx+5*step-15, cy-5*step+15, 'I', s=11, c=C['red'])
    body += _t(cx-5*step+15, cy-5*step+15, 'II', s=11, c=C['red'])
    body += _t(cx-5*step+15, cy+5*step-5, 'III', s=11, c=C['red'])
    body += _t(cx+5*step-15, cy+5*step-5, 'IV', s=11, c=C['red'])
    px, py = cx+3*step, cy-2*step
    body += f'<circle cx="{px}" cy="{py}" r="5" fill="{C["red"]}"/>'
    body += _t(px+12, py-8, '(3,2)', s=11, c=C['red'], a='start')
    body += _li(px, py, px, cy, st=C['red'], sw=1, da='3,2')
    body += _li(px, py, cx, py, st=C['red'], sw=1, da='3,2')
    return _sv(w,h,body)

# ========== CYLINDER 3D ==========
def cylinder_3d(r=50, h2=90):
    m=15; tw,th = r*2+m*2+160, h2+r+m*2+40
    cx,cy = r+m+50, r+m+10
    body = f'<ellipse cx="{cx}" cy="{cy+h2}" rx="{r}" ry="{r//3}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="2.5"/>'
    body += f'<line x1="{cx-r}" y1="{cy}" x2="{cx-r}" y2="{cy+h2}" stroke="{C["fg"]}" stroke-width="2.5"/>'
    body += f'<line x1="{cx+r}" y1="{cy}" x2="{cx+r}" y2="{cy+h2}" stroke="{C["fg"]}" stroke-width="2.5"/>'
    body += f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r//3}" fill="{C["fill2"]}" stroke="{C["fg"]}" stroke-width="2.5"/>'
    body += _t(cx+r+28, cy+h2//2+4, f'h={h2}', s=12, c=C['red'], a='start')
    body += _li(cx+r+14, cy+r//3, cx+r+14, cy+h2-r//3, st=C['red'], sw=1.5, da='4,2')
    body += _t(cx-4, cy-r//3-16, f'r={r}', s=12, c=C['red'])
    body += _t(cx, cy+h2+r//3+20, '圓柱體', s=13)
    body += _t(tw-20, cy+15, 'V = πr²h', s=12, c=C['green'], a='end')
    body += _t(tw-20, cy+38, 'SA = 2πr² + 2πrh', s=11, c=C['green'], a='end')
    body += _t(tw-20, cy+56, '(兩個圓面+側面)', s=10, c=C['gray'], a='end')
    return _sv(tw,th,body)

# ========== PRISM ==========
def prism_triangular():
    w,h = 420, 280
    m=20
    tx,ty = 80, 50
    tb = 150; th_t = 70
    pts_front = f'{tx},{ty+th_t} {tx+tb},{ty+th_t} {tx+tb//2},{ty}'
    body = f'<polygon points="{pts_front}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="2.5"/>'
    dx,dy = 45, -28
    pts_back = f'{tx+dx},{ty+dy+th_t} {tx+tb+dx},{ty+dy+th_t} {tx+tb//2+dx},{ty+dy}'
    body += f'<polygon points="{pts_back}" fill="{C["fill2"]}" stroke="{C["fg"]}" stroke-width="2"/>'
    body += _li(tx,ty+th_t, tx+dx,ty+dy+th_t, sw=2)
    body += _li(tx+tb, ty+th_t, tx+tb+dx, ty+dy+th_t, sw=2)
    body += _li(tx+tb//2, ty, tx+tb//2+dx, ty+dy, sw=2)
    body += _t(tx+tb//2, ty+th_t+20, '底面∥', s=12, c=C['red'])
    body += _t(tx+tb//2+dx+4, ty+dy-12, '底面∥', s=12, c=C['red'])
    body += _t(tx+tb+dx+35, (ty+dy+th_t+ty+th_t)//2, 'h', s=12, c=C['red'])
    body += _li(tx+tb+10, ty+th_t-5, tx+tb+dx+10, ty+dy+th_t+5, st=C['red'], sw=1.5, da='4,2')
    body += _t(w//2, ty+th_t+55, 'V = 底面積 × 高', s=14, c=C['green'])
    body += _t(w//2, ty+th_t+78, '(任何角柱都係呢個公式)', s=11, c=C['gray'])
    return _sv(w,h,body)

# ========== CUBOID + CYLINDER COMPOSITE ==========
def cuboid_cylinder_composite():
    w,h = 520, 300
    ox,oy = 60, 180
    cl, cw, ch = 140, 90, 70
    body = _r(ox, oy, cl, cw, f=C['fill'])
    body += _t(ox+cl//2, oy+cw+22, f'{cl}x{cw}', s=11)
    body += _t(ox-22, oy+cw//2+4, f'{ch}', s=12, c=C['red'], a='end')
    cx = ox + cl//2
    cy = oy - 35
    r = 30
    body += f'<ellipse cx="{cx}" cy="{cy+ch}" rx="{r}" ry="{r//3}" fill="none" stroke="{C["fg"]}" stroke-width="2"/>'
    body += _li(cx-r+2, cy, cx-r+2, cy+ch, sw=2)
    body += _li(cx+r-2, cy, cx+r-2, cy+ch, sw=2)
    body += f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r//3}" fill="{C["fill3"]}" stroke="{C["fg"]}" stroke-width="2.5"/>'
    body += _t(cx+r+20, cy+ch//2, 'h2', s=11, c=C['red'], a='start')
    body += _t(cx, cy-20, 'r='+str(r), s=11, c=C['red'])
    body += _t(cx, oy+cw+48, 'V = V1(長方體) + V2(圓柱)', s=12, c=C['green'])
    body += _t(cx, oy+cw+70, '  = lwh + πr²h2', s=12, c=C['green'])
    return _sv(w,h,body)

# ========== INEQUALITY LINE ==========
def inequality_line():
    w,h = 580, 110
    ox,oy = 40, 55
    step = 50
    body = _li(ox-10, oy, ox+step*10+10, oy, sw=2.5)
    body += f'<polygon points="{ox+step*10+10},{oy} {ox+step*10},{oy-6} {ox+step*10},{oy+6}" fill="{C["fg"]}"/>'
    for i in range(0, 11):
        x = ox + i*step
        body += _li(x, oy-12, x, oy+12, sw=1.2)
        body += _t(x, oy+26, str(i), s=10)
    hx = ox + 4*step
    body += _li(hx, oy, ox+10*step+10, oy, st=C['red'], sw=4)
    body += f'<circle cx="{hx}" cy="{oy}" r="5" fill="white" stroke="{C["red"]}" stroke-width="2.5"/>'
    body += _t(hx, oy-20, 'x > 4', s=13, c=C['red'])
    body += _t(hx, oy+38, '○=開放(不含)', s=9, c=C['red'])
    return _sv(w,h,body)

# ========== INEQUALITY LINE 2 (x <= 3 with filled circle) ==========
def inequality_line2():
    w,h = 580, 110
    ox,oy = 40, 55
    step = 50
    body = _li(ox-10, oy, ox+step*10+10, oy, sw=2.5)
    body += f'<polygon points="{ox+step*10+10},{oy} {ox+step*10},{oy-6} {ox+step*10},{oy+6}" fill="{C["fg"]}"/>'
    for i in range(0, 11):
        x = ox + i*step
        body += _li(x, oy-12, x, oy+12, sw=1.2)
        body += _t(x, oy+26, str(i), s=10)
    hx = ox + 3*step
    body += _li(ox-10, oy, hx, oy, st=C['green'], sw=4)
    body += f'<circle cx="{hx}" cy="{oy}" r="5" fill="{C["green"]}" stroke="{C["green"]}" stroke-width="2"/>'
    body += _t(hx, oy-20, 'x ≤ 3', s=13, c=C['green'])
    body += _t(hx, oy+38, '●=封閉(含)', s=9, c=C['green'])
    return _sv(w,h,body)

# ========== BRIDGE DIAGRAM ==========
def bridge_diagram():
    w,h = 600, 240
    body = _r(30, 50, 170, 110, f=C['fill'], st=C['fg'], sw=2.5)
    body += _t(115, 90, '小學思維', s=14)
    body += _t(115, 115, '「找出答案」', s=12)
    body += _t(115, 138, '數字→答案', s=11, c=C['gray'])
    body += _r(400, 50, 170, 110, f=C['fill2'], st=C['fg'], sw=2.5)
    body += _t(485, 90, '中學思維', s=14)
    body += _t(485, 115, '「表達關係」', s=12)
    body += _t(485, 138, '變數→關係', s=11, c=C['gray'])
    body += _r(200, 75, 200, 60, f=C['fill3'], st=C['gold'], sw=2.5, da='6,3')
    body += _t(300, 100, '數學思維轉換', s=14, c=C['gold'])
    body += _t(300, 115, '算術 → 代數', s=11, c=C['fg'])
    body += _li(200, 105, 400, 105, st=C['gold'], sw=2.5)
    body += f'<polygon points="400,105 390,97 390,113" fill="{C["gold"]}"/>'
    body += _t(300, 200, '「不教數學，教避開陷阱。」', s=13, c=C['fg'])
    return _sv(w,h,body)

# ========== GROWTH PATH (for L39) ==========
def growth_path():
    w,h = 600, 180
    body = _t(w//2, 30, '小學數學 → 中學數學：不是更難，是不同', s=14, c=C['fg'], b=True)
    # Steps
    steps = [
        ('P1-P3', '基礎運算', 40, C['fill']),
        ('P4-P6', '應用解難', 180, C['fill2']),
        ('F1-F2', '代數入門', 320, C['fill3']),
        ('F3', '抽象思維', 460, C['fill']),
    ]
    for i, (title, desc, x, clr) in enumerate(steps):
        body += _r(x-40, 65, 80, 40, f=clr, st=C['fg'], sw=2)
        body += _t(x, 82, title, s=11)
        body += _t(x, 98, desc, s=9, c=C['gray'])
        if i < len(steps)-1:
            body += _li(x+40, 85, steps[i+1][2]-40, 85, st=C['gold'], sw=2)
            body += f'<polygon points="{steps[i+1][2]-40},85 {steps[i+1][2]-50},78 {steps[i+1][2]-50},92" fill="{C["gold"]}"/>'
    body += _t(w//2, 145, '你現在在這裡！', s=13, c=C['red'])
    body += f'<circle cx="220" cy="135" r="4" fill="{C["red"]}"/>'
    return _sv(w,h,body)

# Output all SVGs
if __name__=='__main__':
    import sys
    if len(sys.argv)<2:
        print("Usage: gen_svgs.py <name>")
        print("Names: number_line coordinate_plane cylinder prism composite inequality1 inequality2 bridge growth")
        sys.exit(0)
    name = sys.argv[1]
    if name == 'number_line': print(number_line())
    elif name == 'coordinate_plane': print(coordinate_plane())
    elif name == 'cylinder': print(cylinder_3d())
    elif name == 'prism': print(prism_triangular())
    elif name == 'composite': print(cuboid_cylinder_composite())
    elif name == 'inequality1': print(inequality_line())
    elif name == 'inequality2': print(inequality_line2())
    elif name == 'bridge': print(bridge_diagram())
    elif name == 'growth': print(growth_path())
    elif name == 'all':
        for n in ['number_line','coordinate_plane','cylinder','prism','composite','inequality1','inequality2','bridge','growth']:
            print(f'=== {n} ===')
            exec(f'print({n}())' if n != 'inequality1' and n != 'inequality2' else f'print({n.replace("1","_line").replace("2","_line2")}())')
    else: print(f"Unknown: {name}")
