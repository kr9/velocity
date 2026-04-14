#!/usr/bin/env python3
"""
Convert kiconv4.png to 4 SVG logo files.

Traces the 3 shapes from the PNG, normalises to Velocity canvas sizes,
and applies Catmull-Rom → cubic-Bezier smoothing so caps are clean curves.

Output (overwrites existing Velocity placeholders):
  src/assets/branding/logomark.svg
  src/assets/branding/logomark-dark.svg
  src/assets/branding/logo-full.svg
  src/assets/branding/logo-full-dark.svg
"""

from PIL import Image
import numpy as np
import math, os

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT  = os.path.join(BASE, 'src/assets/branding/kiconv4.png')
OUTDIR = os.path.join(BASE, 'src/assets/branding')

# ── Brand colours ─────────────────────────────────────────────────────────────
ICON_COLOR  = '#965496'   # accent (light bg)
ICON_COLOR_DARK = '#B87AB8'  # accent (dark bg)
TEXT_DARK   = '#1C1C1E'   # foreground on light background
TEXT_LIGHT  = '#F2F2F2'   # foreground on dark background

# ── Target canvas sizes (matching Velocity convention) ────────────────────────
MARK_W, MARK_H = 90, 101
FULL_W, FULL_H = 370, 101

# ── Load & build mask ─────────────────────────────────────────────────────────
img  = Image.open(INPUT).convert('RGBA')
arr  = np.array(img)

# Filled = non-transparent AND not near-white
mask = (arr[:,:,3] > 128) & ~((arr[:,:,0] > 200) & (arr[:,:,1] > 200) & (arr[:,:,2] > 200))

# ── Per-row edge scan ─────────────────────────────────────────────────────────
def scan(y_range, x_min=0, x_max=999):
    """Return left-edge and right-edge lists as (y, x) tuples."""
    L, R = [], []
    for y in y_range:
        xs = np.where(mask[y, x_min:x_max+1])[0] + x_min
        if len(xs):
            L.append((y, int(xs[0])))
            R.append((y, int(xs[-1])))
    return L, R

# Three shapes (determined from pixel analysis):
#   A – small top-left piece  (y 55-278, left of gap at x≈450)
#   B – long upper-right band (y 55-278 right half, then y 278-415 full)
#   C – long lower band       (y 585-935)
la, ra = scan(range(55, 279),  x_max=450)
lb1, rb1 = scan(range(55, 279), x_min=451)
lb2, rb2 = scan(range(279, 416))
lb, rb = lb1 + lb2, rb1 + rb2
lc, rc = scan(range(585, 936))

# ── Coordinate transform: source → target canvas ──────────────────────────────
all_pts = la + ra + lb + rb + lc + rc
sx0 = min(p[1] for p in la + lb + lc)
sx1 = max(p[1] for p in ra + rb + rc)
sy0 = min(p[0] for p in all_pts)
sy1 = max(p[0] for p in all_pts)

scale = min((MARK_W - 2) / (sx1 - sx0),
            (MARK_H - 2) / (sy1 - sy0))
ox = (MARK_W - (sx1 - sx0) * scale) / 2
oy = (MARK_H - (sy1 - sy0) * scale) / 2

def T(x, y):
    return ox + (x - sx0) * scale, oy + (y - sy0) * scale

# ── Catmull-Rom → cubic Bezier smoothing ──────────────────────────────────────
def catmull_to_cubic(p0, p1, p2, p3, alpha=0.5):
    """Return cubic bezier control points cp1 and cp2 for segment p1→p2."""
    def dist(a, b): return math.hypot(b[0]-a[0], b[1]-a[1]) ** alpha
    d1 = dist(p0, p1) or 1e-4
    d2 = dist(p1, p2) or 1e-4
    d3 = dist(p2, p3) or 1e-4
    cp1 = (p1[0] + (p2[0]-p0[0]) * d2 / (6*d1 + 6*d2),
           p1[1] + (p2[1]-p0[1]) * d2 / (6*d1 + 6*d2))
    cp2 = (p2[0] - (p3[0]-p1[0]) * d2 / (6*d2 + 6*d3),
           p2[1] - (p3[1]-p1[1]) * d2 / (6*d2 + 6*d3))
    return cp1, cp2

def smooth_path(pts):
    """
    Build a closed SVG path through pts using Catmull-Rom spline.
    pts: list of (x, y) in target coords.
    """
    n = len(pts)
    if n < 3:
        coords = ' '.join(f'{p[0]:.2f},{p[1]:.2f}' for p in pts)
        return f'M {coords} Z'

    d = [f'M {pts[0][0]:.2f},{pts[0][1]:.2f}']
    for i in range(n):
        p0 = pts[(i - 1) % n]
        p1 = pts[i]
        p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n]
        cp1, cp2 = catmull_to_cubic(p0, p1, p2, p3)
        d.append(f'C {cp1[0]:.2f},{cp1[1]:.2f} {cp2[0]:.2f},{cp2[1]:.2f} {p2[0]:.2f},{p2[1]:.2f}')
    d.append('Z')
    return ' '.join(d)

# ── Build polygon from left/right edge scans ──────────────────────────────────
def shape_path(left_yx, right_yx, step=8):
    """
    Subsample edge points, transform to target coords, smooth with C-R spline.
    Polygon: down the right edge, up the left edge.
    """
    def subsample(pts):
        sampled = pts[::step]
        if pts[-1] != sampled[-1]:
            sampled = sampled + [pts[-1]]
        return sampled

    right_pts = [T(x, y) for y, x in subsample(right_yx)]
    left_pts  = [T(x, y) for y, x in subsample(left_yx)]
    left_pts.reverse()
    poly = right_pts + left_pts
    return smooth_path(poly)

path_a = shape_path(la, ra, step=6)
path_b = shape_path(lb, rb, step=8)
path_c = shape_path(lc, rc, step=8)

print(f'Scale: {scale:.4f}')
print(f'Canvas offset: ({ox:.2f}, {oy:.2f})')
print(f'Shape A points: {len(la)} rows')
print(f'Shape B points: {len(lb)} rows')
print(f'Shape C points: {len(lc)} rows')

# ── SVG builders ──────────────────────────────────────────────────────────────
def mark_svg(fill):
    return (f'<svg width="{MARK_W}" height="{MARK_H}" '
            f'viewBox="0 0 {MARK_W} {MARK_H}" fill="none" '
            f'xmlns="http://www.w3.org/2000/svg">\n'
            f'<path d="{path_a}" fill="{fill}"/>\n'
            f'<path d="{path_b}" fill="{fill}"/>\n'
            f'<path d="{path_c}" fill="{fill}"/>\n'
            f'</svg>\n')

def full_svg(icon_fill, text_fill):
    tx = MARK_W + 10
    ty = round(MARK_H / 2 + 8, 1)
    return (f'<svg width="{FULL_W}" height="{FULL_H}" '
            f'viewBox="0 0 {FULL_W} {FULL_H}" fill="none" '
            f'xmlns="http://www.w3.org/2000/svg">\n'
            f'<path d="{path_a}" fill="{icon_fill}"/>\n'
            f'<path d="{path_b}" fill="{icon_fill}"/>\n'
            f'<path d="{path_c}" fill="{icon_fill}"/>\n'
            f'<text x="{tx}" y="{ty}" '
            f'font-family="Manrope, sans-serif" font-weight="700" '
            f'font-size="22" letter-spacing="-0.3" '
            f'fill="{text_fill}">Kamal Rupareliya</text>\n'
            f'</svg>\n')

# ── Write files ───────────────────────────────────────────────────────────────
outputs = {
    'logomark.svg':       mark_svg(ICON_COLOR),
    'logomark-dark.svg':  mark_svg(ICON_COLOR_DARK),
    'logo-full.svg':      full_svg(ICON_COLOR, TEXT_DARK),
    'logo-full-dark.svg': full_svg(ICON_COLOR_DARK, TEXT_LIGHT),
}

for name, content in outputs.items():
    path = os.path.join(OUTDIR, name)
    with open(path, 'w') as f:
        f.write(content)
    print(f'✓ {path}')
