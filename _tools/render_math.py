#!/usr/bin/env python3
"""霖楓學苑 · LF Academy 數學公式渲染器 v1.3 — 1200dpi·48px·分數自適應放大"""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; import io, base64, sys
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=['Noto Sans HK','DejaVu Sans']
matplotlib.rcParams['mathtext.fontset']='dejavusans'
matplotlib.rcParams['axes.unicode_minus']=False

def tex2png_b64(formula:str, fontsize:int=48, dpi:int=1200, bold:bool=False,
                has_frac:bool=None)->str:
    """v1.3: 1200dpi·48px·3x超採樣·分數自適應放大
       含分數的公式自動增加字型(×1.5)和高度，防止分子分母被壓縮變細
       用法: <img style="height:1.5em;vertical-align:middle;" src="...">"""
    if has_frac is None: has_frac = '\\frac' in formula
    fs = int(fontsize * 1.5) if has_frac else fontsize
    h = 0.75 if has_frac else 0.55  # taller figure for fractions
    if bold: formula = r'\mathbf{' + formula + '}'
    w = max(1.8, len(formula) * 0.16)
    fig, ax = plt.subplots(figsize=(w, h)); ax.axis('off')
    ax.text(0.5, 0.5, f'${formula}$', fontsize=fs, ha='center', va='center',
            transform=ax.transAxes)
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.05,
                dpi=dpi, transparent=True)
    buf.seek(0); plt.close(fig)
    return f'data:image/png;base64,{base64.b64encode(buf.read()).decode()}'

T={
'frac_add':r'\frac{2}{3}+\frac{3}{5}','frac_sub':r'\frac{5}{6}-\frac{1}{4}',
'frac_mul':r'\frac{2}{3}\times\frac{3}{5}=\frac{2}{5}','frac_div':r'\frac{2}{3}\div\frac{4}{5}=\frac{5}{6}',
'frac_mixed':r'1\frac{1}{2}+2\frac{2}{3}','frac_three':r'\frac{1}{2}+\frac{1}{3}+\frac{1}{4}',
'area_square':r'A=a^2','area_rect':r'A=l\times w','area_triangle':r'A=\frac{1}{2}bh',
'area_para':r'A=b\times h','area_trap':r'A=\frac{(a+b)h}{2}',
'vol_cube':r'V=a^3','vol_cuboid':r'V=l\times w\times h',
'circle_c':r'C=2\pi r=\pi d','circle_a':r'A=\pi r^2',
'speed':r'S=\frac{D}{T}','average':r'Avg=\frac{Sum}{Count}',
'pct':r'\%=\frac{part}{whole}\times100\%','discount':r'Discount=Original\times(1-r)',
'eq1':r'x+5=12\rightarrow x=7','eq2':r'2x+3=11\rightarrow x=4',
'unit_area':r'1m^2=10{,}000cm^2','unit_vol':r'1m^3=1{,}000{,}000cm^3',
}

def get_template(name:str,fs:int=48,bold:bool=False)->str:
    if name not in T: raise ValueError(f"Unknown: {name}")
    return tex2png_b64(T[name],fontsize=fs,bold=bold)

if __name__=='__main__':
    if len(sys.argv)<2: print("Usage: render_math.py <formula|--template name|--list>"); sys.exit(0)
    if sys.argv[1]=='--list':
        for n,f in T.items(): print(f"  {n}: {f}")
    elif sys.argv[1]=='--template': print(get_template(sys.argv[2],int(sys.argv[3])if len(sys.argv)>3 else 48,bool(sys.argv[4])if len(sys.argv)>4 else False))
    else: print(tex2png_b64(sys.argv[1],int(sys.argv[2])if len(sys.argv)>2 else 48))
