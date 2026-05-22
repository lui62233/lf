#!/usr/bin/env python3
"""霖楓學苑 · LF Academy SVG 幾何圖形庫 v2.3 — 精簡·無公式卡·適合A4列印"""
import sys
C={'fg':'#1A3C6D','fill':'#DBEAFE','fill2':'#DCFCE7','fill3':'#FEF3C7','water':'#BAE6FD','obj':'#93C5FD','red':'#DC2626','green':'#16A34A','gold':'#C9A84C','gray':'#6B7280','grid':'#D1D5DB','white':'#FFFFFF'}
def _sv(w,h,c): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{c}</svg>'
def _t(x,y,t,a='middle',s=13,c=None,b=True):
    cl=c or C['fg']; fw='font-weight="700"' if b else ''
    return f'<text x="{x}" y="{y}" text-anchor="{a}" font-size="{s}" fill="{cl}" {fw}>{t}</text>'
def _r(x,y,w,h,f=None,st=None,sw=3,da=None):
    fl=f or C['fill']; stl=st or C['fg']; d=f' stroke-dasharray="{da}"' if da else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fl}" stroke="{stl}" stroke-width="{sw}"{d}/>'
def _li(x1,y1,x2,y2,st=None,sw=3,da=None):
    stl=st or C['fg']; d=f' stroke-dasharray="{da}"' if da else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stl}" stroke-width="{sw}"{d}/>'
def _ra(x,y,s=10):
    return f'<polyline points="{x+s},{y} {x+s},{y+s} {x},{y+s}" fill="none" stroke="{C["fg"]}" stroke-width="2"/>'

def square(s=100):
    m=15;w,h=s+m*2+40,s+m*2+10;ox,oy=m+20,m
    body=_r(ox,oy,s,s)+_ra(ox,oy,10)
    body+=_t(ox+s//2,oy+s+18,'a',s=14)
    return _sv(w,h,body)

def rectangle(l=150,w=90):
    m=15;w2,h2=l+m*2+40,w+m*2+10;ox,oy=m+20,m
    body=_r(ox,oy,l,w)+_ra(ox,oy,10)
    body+=_t(ox+l//2,oy+w+18,'l',s=13)
    body+=_t(ox-14,oy+w//2,'w',a='end',s=13)
    return _sv(w2,h2,body)

def triangle(b=120,h=80,tt='right'):
    m=20;tw,th=b+m*2+30,h+m*2+30;ox,oy=m+15,h+m
    if tt=='right':
        pts=f'{ox},{oy} {ox+b},{oy} {ox},{oy-h}'
        body=f'<polygon points="{pts}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="3"/>'+_ra(ox,oy-h-10,8)
        body+=_li(ox,oy-h,ox,oy,st=C['red'],sw=2,da='6,3')+_t(ox-14,oy-h//2,'h',s=12,c=C['red'])
    elif tt=='obtuse':
        # 鈍角在頂點：底120·高55 (b>2h確保頂角>90°)·高在三角形內
        oh=55;pts=f'{ox},{oy} {ox+b},{oy} {ox+b//2},{oy-oh}'
        body=f'<polygon points="{pts}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="3"/>'
        body+=_li(ox+b//2,oy-oh,ox+b//2,oy,st=C['red'],sw=2,da='6,3')+_t(ox+b//2+12,oy-oh//2,'h',s=12,c=C['red'])
    else:
        pts=f'{ox},{oy} {ox+b},{oy} {ox+b//2},{oy-h}'
        body=f'<polygon points="{pts}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="3"/>'
        body+=_li(ox+b//2,oy-h,ox+b//2,oy,st=C['red'],sw=2,da='6,3')+_t(ox+b//2+12,oy-h//2,'h',s=12,c=C['red'])
    body+=_t(ox+b//2,oy+22,'b',s=14)
    return _sv(tw,th,body)

def trapezoid(u=80,lo=140,h=75):
    m=20;tw,th=lo+m*2+30,h+m*2+20;ox,oy=m+15,h+m;dx=(lo-u)//2
    pts=f'{ox},{oy} {ox+lo},{oy} {ox+lo-dx},{oy-h} {ox+dx},{oy-h}'
    body=f'<polygon points="{pts}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="3"/>'
    body+=_li(ox+dx,oy-h,ox+dx,oy,st=C['red'],sw=2,da='6,3')+_t(ox+dx+12,oy-h//2,'h',s=12,c=C['red'])
    body+=_t(ox+lo//2,oy+22,f'b₂',s=13)
    body+=_t(ox+dx+u//2,oy-h-8,f'b₁',s=12)
    return _sv(tw,th,body)

def circle_shape(r=60):
    m=10;tw,th=r*2+m*2+40,r*2+m*2+20;cx,cy=r+m+20,r+m
    body=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="3"/>'
    body+=f'<circle cx="{cx}" cy="{cy}" r="3" fill="{C["fg"]}"/>'+_t(cx,cy-7,'O',s=11)
    body+=_li(cx,cy,cx+r,cy,sw=2)+_t(cx+r//2,cy-7,'r',s=12)
    body+=_li(cx-r,cy+8,cx+r,cy+8,st=C['red'],sw=2,da='5,2')+_t(cx,cy+22,'d=2r',s=11,c=C['red'])
    return _sv(tw,th,body)

def cuboid(l=120,w=60,h=70):
    m=15;tw,th=l+w+m*2+20,h+w+m*2+10;ox,oy=m+10,m;d=w//3
    front=_r(ox,oy+d,l,h)
    top=f'<polygon points="{ox},{oy+d} {ox+d},{oy} {ox+l+d},{oy} {ox+l},{oy+d}" fill="{C["fill"]}" stroke="{C["fg"]}" stroke-width="3"/>'
    side=f'<polygon points="{ox+l},{oy+d} {ox+l+d},{oy} {ox+l+d},{oy+h} {ox+l},{oy+d+h}" fill="#BFDBFE" stroke="{C["fg"]}" stroke-width="3"/>'
    body=front+top+side+_t(ox+l//2,oy+d+h+16,'l',s=13)
    return _sv(tw,th,body)

def displacement(cw=150,ch=85,wb=28,wa=52,ow=42,oh=42):
    tw,th=cw*2+70,ch+100;ox1,ox2=15,cw+55;oy=15
    def _draw(x,wh,obj=False,label=''):
        c=_r(x,oy,cw,ch,f=C['white'],st=C['fg'],sw=3)
        wy=oy+ch-wh
        c+=_r(x,wy,cw,wh,f=C['water'],st='#7DD3FC',sw=1.5)
        c+=_li(x-8,wy,x+cw+8,wy,st=C['red'],sw=1.5,da='4,2')+_t(x+cw+14,wy+4,f'{wh}cm',a='start',s=11,c=C['red'])
        if obj:
            oxo=x+(cw-ow)//2;oyo=oy+ch-oh
            c+=_r(oxo,oyo,ow,oh,f=C['obj'],st=C['fg'],sw=2.5)
            c+=_t(oxo+ow//2,oyo+oh//2,'石頭',s=12,c=C['red'])
        c+=_t(x+cw//2,oy+ch+20,label,s=13,c=C['fg'])
        return c
    body=_draw(ox1,wb,label='投入前')
    body+=_draw(ox2,wa,True,label='投入後（完全浸沒）')
    ay1=oy+ch-wb;ay2=oy+ch-wa
    body+=_li(ox1+cw+12,ay1,ox1+cw+12,ay2,st=C['red'],sw=2.5)
    body+=f'<polygon points="{ox1+cw+8},{ay2+4} {ox1+cw+16},{ay2+4} {ox1+cw+12},{ay2-2}" fill="{C["red"]}"/>'
    body+=_t(ox1+cw+26,(ay1+ay2)//2,f'+{wa-wb}cm',s=13,c=C['red'],a='start')
    body+=_t(tw//2,oy+ch+52,'水面上升 = 物體體積 ÷ 底面積',s=14,c=C['green'])
    return _sv(tw,th,body)

def composite_L(w1=60,h1=80,w2=80,h2=35):
    m=15;tw,th=w1+w2+m*2+30,max(h1,h2)+m*2+10;ox,oy=m+15,m
    body=_r(ox,oy,w1,h1)+_t(ox+w1//2,oy+h1+16,f'{w1}',s=11)
    body+=_r(ox+w1,oy+h1-h2,w2,h2,f=C['fill2'])+_t(ox+w1+w2//2,oy+h1+16,f'{w2}',s=11)
    body+=_li(ox+w1,oy,ox+w1,oy+h1,st=C['gray'],sw=1,da='5,2')
    return _sv(tw,th,body)

def composite_T(w_top=120,h_top=30,w_bot=55,h_bot=55):
    m=15;tw,th=w_top+m*2+30,h_top+h_bot+m*2+10;ox,oy=m+15,m;dx=(w_top-w_bot)//2
    body=_r(ox,oy,w_top,h_top)+_t(ox+w_top//2,oy+h_top+14,f'{w_top}',s=11)
    body+=_r(ox+dx,oy+h_top,w_bot,h_bot,f=C['fill2'])+_t(ox+dx+w_bot//2,oy+h_top+h_bot+14,f'{w_bot}',s=11)
    body+=_li(ox+dx,oy+h_top,ox+dx+w_bot,oy+h_top,st=C['gray'],sw=1,da='4,2')
    return _sv(tw,th,body)

def composite_hole(outer_w=130,outer_h=85,inner_w=50,inner_h=50):
    m=15;tw,th=outer_w+m*2+30,outer_h+m*2+10;ox,oy=m+15,m
    ix=(outer_w-inner_w)//2;iy=(outer_h-inner_h)//2
    body=_r(ox,oy,outer_w,outer_h,f=C['fill'],st=C['fg'],sw=3)
    body+=_r(ox+ix,oy+iy,inner_w,inner_h,f=C['white'],st=C['red'],sw=2.5,da='6,3')
    body+=_t(ox+ix+inner_w//2,oy+iy+inner_h//2,'挖去',s=11,c=C['red'])
    return _sv(tw,th,body)

def grid_diagram(cols=5,rows=3,fc=None,fr=None):
    cell=35;m=15;tw,th=cols*cell+m*2+40,rows*cell+m*2+20;ox,oy=m+20,m
    fcol=fc or cols;frow=fr or rows
    body=_r(ox,oy,fcol*cell,frow*cell,f=C['fill'],st='none',sw=0)
    for i in range(cols+1): body+=_li(ox+i*cell,oy,ox+i*cell,oy+rows*cell,st=C['grid'],sw=0.8)
    for j in range(rows+1): body+=_li(ox,oy+j*cell,ox+cols*cell,oy+j*cell,st=C['grid'],sw=0.8)
    body+=_r(ox,oy,cols*cell,rows*cell,f='none',sw=3)
    body+=_t(ox+cols*cell//2,oy+rows*cell+18,f'{cols} 格',s=12)
    return _sv(tw,th,body)

# ═══════════════════════════════════════════════
# v2.4 統計圖表模組 — bar charts, line graphs, pie charts
# ═══════════════════════════════════════════════

CHART_C = {
    'bar1':'#3B82F6','bar2':'#F97316','bar3':'#10B981','bar4':'#8B5CF6',
    'bar1l':'#DBEAFE','bar2l':'#FFEDD5','bar3l':'#D1FAE5','bar4l':'#EDE9FE',
    'line1':'#DC2626','line2':'#2563EB','line3':'#059669',
    'pie':['#3B82F6','#F97316','#10B981','#EF4444','#8B5CF6','#F59E0B','#EC4899','#06B6D4'],
    'grid':'#E5E7EB','axis':'#374151'
}

def _ax(x,y,w,h,ylabel='',xlabels=None,ymax=100,ystep=25,unit=''):
    """Draw axes + grid + labels. Returns (body, chart_left, chart_top, chart_w, chart_h)."""
    cl,ct,cw,ch=85,35,w-105,h-65
    body=f'<line x1="{cl}" y1="{ct}" x2="{cl}" y2="{ct+ch}" stroke="{CHART_C["axis"]}" stroke-width="2"/>'
    body+=f'<line x1="{cl}" y1="{ct+ch}" x2="{cl+cw}" y2="{ct+ch}" stroke="{CHART_C["axis"]}" stroke-width="2"/>'
    # Y-axis labels + gridlines
    steps=int(ymax/ystep)
    for i in range(steps+1):
        val=i*ystep;yy=ct+ch-i*(ch/steps)
        body+=f'<line x1="{cl}" y1="{yy}" x2="{cl+cw}" y2="{yy}" stroke="{CHART_C["grid"]}" stroke-width="0.5"/>'
        body+=_t(cl-8,yy+4,str(val),a='end',s=10,c=C['gray'])
    if unit:
        body+=_t(cl-8,ct+4,f'({unit})',a='end',s=9,c=C['gray'])
    if ylabel:
        body+=f'<text x="14" y="{ct+ch//2}" text-anchor="middle" font-size="11" fill="{C["fg"]}" transform="rotate(-90,14,{ct+ch//2})">{ylabel}</text>'
    # X-axis labels
    if xlabels:
        n=len(xlabels);bar_w=cw/n
        for i,lab in enumerate(xlabels):
            body+=_t(cl+bar_w*i+bar_w/2,ct+ch+18,lab,s=11)
    return body,cl,ct,cw,ch

def bar_simple(data:dict,title:str='',ylabel:str='',unit:str='',ystep:int=0,bar_w:int=40,bar_gap:int=18,ymax:int=0):
    """Simple bar chart. data={category:value, ...}. Returns complete SVG."""
    cats=list(data.keys());vals=list(data.values())
    max_v=max(vals) if vals else 10
    if ymax<=0: ymax=((max_v//ystep)+1)*ystep if ystep else max_v+max_v//5
    if ystep<=0: ystep=max(1,ymax//6)
    n=len(cats);bar_total=n*bar_w+(n-1)*bar_gap
    w=bar_total+130;h=320
    body,cl,ct,cw,ch=_ax(0,0,w,h,ylabel=ylabel,xlabels=cats,ymax=ymax,ystep=ystep,unit=unit)
    # Title
    if title: body+=_t(w//2,ct-10,title,s=14,c=C['fg'])
    # Bars
    for i,(cat,val) in enumerate(zip(cats,vals)):
        x=cl+bar_gap//2+i*(bar_w+bar_gap)
        bh=val/ymax*ch;y=ct+ch-bh
        body+=_r(x,y,bar_w,bh,f=CHART_C['bar1'],st='#1D4ED8',sw=1)
        body+=_t(x+bar_w//2,y-10,str(val),s=10,c=C['fg'])
    return _sv(w,h,body)

def bar_composite(groups:list,title:str='',ylabel:str='',unit:str='',ystep:int=0,bar_w:int=24,ymax:int=0):
    """Composite/grouped bar chart.
    groups=[{name:'A店',data:{'一月':100,'二月':120,...}}, {name:'B店',data:{...}}]
    Returns complete SVG."""
    n_groups=len(groups)
    if n_groups==0: return ''
    cats=list(groups[0]['data'].keys());n_cats=len(cats)
    all_vals=[v for g in groups for v in g['data'].values()]
    max_v=max(all_vals) if all_vals else 10
    if ymax<=0: ymax=((max_v//ystep)+1)*ystep if ystep else max_v+max_v//5
    if ystep<=0: ystep=max(1,ymax//6)
    colors=[CHART_C['bar1'],CHART_C['bar2'],CHART_C['bar3'],CHART_C['bar4']]
    group_w=bar_w*n_groups+6*(n_groups-1);gap=20
    total_w=n_cats*group_w+(n_cats-1)*gap+130;h=380
    body,cl,ct,cw,ch=_ax(0,0,total_w,h,ylabel=ylabel,xlabels=cats,ymax=ymax,ystep=ystep,unit=unit)
    if title: body+=_t(total_w//2,ct-10,title,s=14,c=C['fg'])
    for ci,cat in enumerate(cats):
        gx=cl+gap//2+ci*(group_w+gap)
        for gi,g in enumerate(groups):
            val=g['data'][cat];bh=val/ymax*ch;bx=gx+gi*(bar_w+6);by=ct+ch-bh
            body+=_r(bx,by,bar_w,bh,f=colors[gi],st='#1D4ED8' if gi==0 else '#C2410C' if gi==1 else '#047857',sw=0.8)
            if n_groups<=3: body+=_t(bx+bar_w//2,by-10,str(val),s=8,c=C['fg'])
    # Legend
    lx=total_w//2-(n_groups*70)//2;ly=ct+ch+28
    for gi,g in enumerate(groups):
        body+=_r(lx+gi*70,ly,12,10,f=colors[gi],st='none',sw=0)
        body+=_t(lx+gi*70+16,ly+9,g['name'],s=10,c=C['fg'],a='start')
    return _sv(total_w,h,body)

def bar_blank(categories:list,title:str='',ylabel:str='',unit:str='',ystep:int=0,bar_w:int=40,bar_gap:int=18,ymax:int=100):
    """Empty bar chart template — axes + grid but NO bars. For student drawing practice."""
    n=len(categories);bar_total=n*bar_w+(n-1)*bar_gap
    w=bar_total+130;h=320
    if ystep<=0: ystep=max(1,ymax//6)
    body,cl,ct,cw,ch=_ax(0,0,w,h,ylabel=ylabel,xlabels=categories,ymax=ymax,ystep=ystep,unit=unit)
    if title: body+=_t(w//2,ct-10,title,s=13,c=C['fg'])
    # Faint bar outlines to guide drawing
    for i in range(n):
        x=cl+bar_gap//2+i*(bar_w+bar_gap)
        body+=f'<rect x="{x}" y="{ct}" width="{bar_w}" height="{ch}" fill="none" stroke="{CHART_C["grid"]}" stroke-width="1" stroke-dasharray="4,3"/>'
    # Note
    body+=_t(w//2,ct+ch+32,'（請在虛線框內畫出棒形）',s=10,c=C['gray'])
    return _sv(w,h,body)

def bar_composite_blank(categories:list,group_names:list,title:str='',ylabel:str='',unit:str='',ystep:int=0,bar_w:int=24,ymax:int=100):
    """Empty composite bar chart template — axes + grid + guide boxes. For student practice."""
    n_groups=len(group_names);n_cats=len(categories)
    if n_groups==0: return ''
    colors=[CHART_C['bar1'],CHART_C['bar2'],CHART_C['bar3'],CHART_C['bar4']]
    group_w=bar_w*n_groups+6*(n_groups-1);gap=20
    total_w=n_cats*group_w+(n_cats-1)*gap+130;h=380
    if ystep<=0: ystep=max(1,ymax//6)
    body,cl,ct,cw,ch=_ax(0,0,total_w,h,ylabel=ylabel,xlabels=categories,ymax=ymax,ystep=ystep,unit=unit)
    if title: body+=_t(total_w//2,ct-10,title,s=13,c=C['fg'])
    for ci in range(n_cats):
        gx=cl+gap//2+ci*(group_w+gap)
        for gi in range(n_groups):
            bx=gx+gi*(bar_w+6)
            body+=f'<rect x="{bx}" y="{ct}" width="{bar_w}" height="{ch}" fill="none" stroke="{colors[gi]}" stroke-width="1" stroke-dasharray="4,3"/>'
    # Legend
    lx=total_w//2-(n_groups*70)//2;ly=ct+ch+28
    for gi,gn in enumerate(group_names):
        body+=_r(lx+gi*70,ly,12,10,f=colors[gi],st='none',sw=0)
        body+=_t(lx+gi*70+16,ly+9,gn,s=10,c=C['fg'],a='start')
    body+=_t(total_w//2,ly+24,'（請在虛線框內按數據畫出棒形）',s=10,c=C['gray'])
    return _sv(total_w,h,body)

def line_chart(data:dict,title:str='',ylabel:str='',unit:str='',ystep:int=0,ymax:int=0,dot_r:int=4):
    """Line chart. data={x_label:y_value, ...}"""
    pts=list(data.items());xs=list(data.keys());ys=[v for _,v in pts]
    max_v=max(ys) if ys else 10
    if ymax<=0: ymax=((max_v//ystep)+1)*ystep if ystep else max_v+max_v//5
    if ystep<=0: ystep=max(1,ymax//6)
    n=len(pts);gap=60
    w=n*gap+130;h=320
    body,cl,ct,cw,ch=_ax(0,0,w,h,ylabel=ylabel,xlabels=xs,ymax=ymax,ystep=ystep,unit=unit)
    if title: body+=_t(w//2,ct-10,title,s=14,c=C['fg'])
    # Points + lines
    pts_xy=[]
    for i,(_,val) in enumerate(pts):
        x=cl+gap//2+i*gap;y=ct+ch-val/ymax*ch
        pts_xy.append((x,y))
        body+=f'<circle cx="{x}" cy="{y}" r="{dot_r}" fill="{CHART_C["line1"]}" stroke="white" stroke-width="1.5"/>'
        body+=_t(x,y-12,str(val),s=10,c=C['fg'])
    # Connect lines
    if len(pts_xy)>1:
        pline=' '.join(f'{x},{y}' for x,y in pts_xy)
        body+=f'<polyline points="{pline}" fill="none" stroke="{CHART_C["line1"]}" stroke-width="2.5" stroke-linejoin="round"/>'
    return _sv(w,h,body)

def line_blank(x_labels:list,title:str='',ylabel:str='',unit:str='',ystep:int=0,ymax:int=100):
    """Empty line chart template — axes + grid + faint guide dots. For student practice."""
    n=len(x_labels);gap=60
    w=n*gap+130;h=320
    if ystep<=0: ystep=max(1,ymax//6)
    body,cl,ct,cw,ch=_ax(0,0,w,h,ylabel=ylabel,xlabels=x_labels,ymax=ymax,ystep=ystep,unit=unit)
    if title: body+=_t(w//2,ct-10,title,s=13,c=C['fg'])
    # Faint guide dots
    for i in range(n):
        x=cl+gap//2+i*gap
        body+=f'<circle cx="{x}" cy="{ct+ch//2}" r="2" fill="{CHART_C["grid"]}" stroke="none"/>'
    body+=_t(w//2,ct+ch+32,'（請按數據標出點並連線）',s=10,c=C['gray'])
    return _sv(w,h,body)

def pie_chart(data:dict,title:str='',radius:int=80):
    """Pie chart. data={category:value, ...}. Returns complete SVG."""
    total=sum(data.values());r=radius;cx,cy=r+60,r+55
    tw,th=r*2+220,r*2+150;legend_x=cx+r+30
    colors=CHART_C['pie']
    body=''
    if title: body+=_t(tw//2,22,title,s=14,c=C['fg'])
    # Pie chart — donut style with labels
    items=list(data.items())
    # Calculate percentages and build slices
    import math
    start_angle=-90  # start from top
    for i,(cat,val) in enumerate(items):
        pct=val/total*100;angle=val/total*360
        end_angle=start_angle+angle
        # Arc path
        sr,er=math.radians(start_angle),math.radians(end_angle)
        x1=cx+r*math.cos(sr);y1=cy+r*math.sin(sr)
        x2=cx+r*math.cos(er);y2=cy+r*math.sin(er)
        large=1 if angle>180 else 0
        d=f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large},1 {x2},{y2} Z'
        body+=f'<path d="{d}" fill="{colors[i%len(colors)]}" stroke="white" stroke-width="2"/>'
        # Label on slice (mid-angle)
        mid=math.radians(start_angle+angle/2);lx=cx+(r*0.65)*math.cos(mid);ly=cy+(r*0.65)*math.sin(mid)
        if pct>=8: body+=_t(lx,ly+4,f'{pct:.0f}%',s=9,c='white')
        # Legend entry
        ly2=legend_x;ly=cy-30+i*22
        body+=_r(legend_x,ly,12,10,f=colors[i%len(colors)],st='none',sw=0)
        body+=_t(legend_x+18,ly+9,f'{cat} ({val})',s=10,c=C['fg'],a='start')
        start_angle=end_angle
    return _sv(tw,th,body)

def data_table(headers:list,rows:list,title:str=''):
    """Render a data table as SVG for printing. headers=['col1','col2',...], rows=[[v1,v2,...],...]"""
    ncols=len(headers);col_w=100;row_h=30
    tw=ncols*col_w+60;th=(len(rows)+1)*row_h+80
    ox,oy=30,40
    body=''
    if title: body+=_t(tw//2,oy-12,title,s=13,c=C['fg'])
    # Header
    for ci,h in enumerate(headers):
        body+=_r(ox+ci*col_w,oy,col_w,row_h,f=C['blue'] if 'fg' not in C else '#1A3C6D',st='none',sw=0)
        body+=_t(ox+ci*col_w+col_w//2,oy+row_h//2+4,h,s=11,c='white')
    # Rows
    for ri,row in enumerate(rows):
        ry=oy+(ri+1)*row_h
        bg=C['fill'] if ri%2==0 else C['white']
        for ci,val in enumerate(row):
            body+=_r(ox+ci*col_w,ry,col_w,row_h,f=bg,st=C['grid'],sw=0.5)
            body+=_t(ox+ci*col_w+col_w//2,ry+row_h//2+4,str(val),s=10,c=C['fg'])
    # Border
    body+=_r(ox,oy,ncols*col_w,(len(rows)+1)*row_h,f='none',sw=2)
    return _sv(tw,th,body)

if __name__=='__main__':
    if len(sys.argv)<2:print("v2.3 shapes: square rectangle triangle trapezoid circle cuboid displacement composite_L composite_T composite_hole grid_diagram");sys.exit(0)
    s=sys.argv[1]
    try:
        if s=='square':print(square(int(sys.argv[2])if len(sys.argv)>2 else 100))
        elif s=='rectangle':print(rectangle(int(sys.argv[2])if len(sys.argv)>2 else 150,int(sys.argv[3])if len(sys.argv)>3 else 90))
        elif s=='triangle':print(triangle(int(sys.argv[2])if len(sys.argv)>2 else 120,int(sys.argv[3])if len(sys.argv)>3 else 80,sys.argv[4]if len(sys.argv)>4 else'right'))
        elif s=='trapezoid':print(trapezoid(int(sys.argv[2])if len(sys.argv)>2 else 80,int(sys.argv[3])if len(sys.argv)>3 else 140,int(sys.argv[4])if len(sys.argv)>4 else 75))
        elif s=='circle':print(circle_shape(int(sys.argv[2])if len(sys.argv)>2 else 60))
        elif s=='cuboid':print(cuboid(int(sys.argv[2])if len(sys.argv)>2 else 120,int(sys.argv[3])if len(sys.argv)>3 else 60,int(sys.argv[4])if len(sys.argv)>4 else 70))
        elif s=='displacement':print(displacement())
        elif s=='composite_L':print(composite_L())
        elif s=='composite_T':print(composite_T())
        elif s=='composite_hole':print(composite_hole())
        elif s=='grid_diagram':print(grid_diagram(int(sys.argv[2])if len(sys.argv)>2 else 5,int(sys.argv[3])if len(sys.argv)>3 else 3))
        else:print(f"Unknown: {s}")
    except Exception as e:print(f"Error: {e}",file=sys.stderr);sys.exit(1)
