"""Parametric model of a 2.0 m / 120 L downwind pump wingfoil board.

Coordinates (mm): x = distance from tail (0) to nose (LENGTH), y = across from
stringer (0) to rail, z = up from the lowest point of the bottom rocker.

Run:  python3 board_model.py   -> writes spec + A4 template PDFs next to this file.
"""
import math
import os
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- parameters
LENGTH = 2000.0
TARGET_LITRES = 120.0
PANEL_SKIN_MM = 3.8        # deck/bottom: 100 g glass + 3 mm PVC + 200 g carbon + fill; core inset by this
RAIL_SKIN_MM = 1.0         # chine/rail band: 200 g carbon wrap + 2 x 200 g basalt + fill
SKIN_MM = RAIL_SKIN_MM     # kept for older callers
STATIONS = [150, 450, 750, 1050, 1350, 1650, 1850]   # from tail

# Plan-shape half widths (x, half-width). Max width 560 mm.
OUTLINE = [(0, 171), (40, 207), (150, 243), (300, 264), (500, 277), (750, 280),
           (950, 280), (1150, 276), (1350, 263), (1550, 238), (1720, 203),
           (1850, 156), (1950, 95), (1985, 54), (2000, 0)]

# Bottom rocker at stringer (x, z). Dead straight run from the transom to 1000 mm
# (skiff-style: flow leaves the transom tangent to the run, no tail kick).
ROCKER = [(0, 0), (300, 0), (1000, 0), (1200, 3), (1400, 12),
          (1600, 30), (1750, 50), (1880, 76), (1960, 98), (2000, 112)]

# Thickness shape at stringer, normalised; scaled to hit TARGET_LITRES.
THICK_SHAPE = [(0, 0.58), (150, 0.70), (400, 0.88), (650, 1.0), (1050, 1.0),
               (1300, 0.94), (1550, 0.80), (1750, 0.62), (1900, 0.42),
               (1970, 0.27), (2000, 0.16)]

# Section shape along the board (x, value)
FLAT_FRAC = [(0, 0.82), (600, 0.72), (1200, 0.62), (1700, 0.48), (2000, 0.40)]  # flat bottom / half-width
BEVEL_FRAC = [(0, 0.10), (500, 0.20), (1100, 0.26), (1700, 0.32), (2000, 0.34)]  # chine height / thickness
RAIL_FRAC = [(0, 0.40), (1000, 0.46), (2000, 0.50)]   # top of vertical rail band / thickness
EDGE_R = [(0, 0.0), (500, 0.0), (900, 4.0), (1400, 10.0), (2000, 14.0)]  # chine fillet radius, mm (sharp aft)
DEADRISE = [(0, 0.0), (1300, 0.0), (1600, 3.0), (1850, 7.0), (2000, 9.0)]  # soft-V nose, degrees
DECK_N = 5.0                                          # deck super-ellipse exponent (higher = flatter, boxier)

# Foil tracks (US-box style dual tracks, 90 mm centres)
TRACK_CENTRE_X = 760.0
TRACK_LEN = 356.0          # 14 inch tracks (changed from 10 inch on 2026-10-16)
TRACK_SPACING = 90.0
BLOCK_LEN = 420.0          # high-density track block, full core depth
BLOCK_WIDTH = 150.0


# ---------------------------------------------------------------- helpers
def pchip(points):
    """Monotone cubic (Fritsch-Carlson) interpolator from (x, y) pairs."""
    xs = np.array([p[0] for p in points], float)
    ys = np.array([p[1] for p in points], float)
    h = np.diff(xs)
    d = np.diff(ys) / h
    m = np.zeros_like(ys)
    m[0], m[-1] = d[0], d[-1]
    for k in range(1, len(xs) - 1):
        if d[k - 1] * d[k] > 0:
            w1, w2 = 2 * h[k] + h[k - 1], h[k] + 2 * h[k - 1]
            m[k] = (w1 + w2) / (w1 / d[k - 1] + w2 / d[k])

    def f(x):
        x = np.asarray(x, float)
        k = np.clip(np.searchsorted(xs, x) - 1, 0, len(xs) - 2)
        t = (x - xs[k]) / h[k]
        h00 = (1 + 2 * t) * (1 - t) ** 2
        h10 = t * (1 - t) ** 2
        h01 = t * t * (3 - 2 * t)
        h11 = t * t * (t - 1)
        return h00 * ys[k] + h10 * h[k] * m[k] + h01 * ys[k + 1] + h11 * h[k] * m[k + 1]
    return f


half_width = pchip(OUTLINE)
rocker = pchip(ROCKER)
thick_shape = pchip(THICK_SHAPE)
flat_frac = pchip(FLAT_FRAC)
bevel_frac = pchip(BEVEL_FRAC)
rail_frac = pchip(RAIL_FRAC)
edge_r = pchip(EDGE_R)
deadrise = pchip(DEADRISE)


def chaikin(poly, iters=3):
    for _ in range(iters):
        p = poly
        q = 0.75 * p[:-1] + 0.25 * p[1:]
        r = 0.25 * p[:-1] + 0.75 * p[1:]
        new = np.empty((2 * len(q), 2))
        new[0::2], new[1::2] = q, r
        poly = np.vstack([p[:1], new, p[-1:]])   # keep end points (stringer)
    return poly


def resample(poly, step=2.0):
    seg = np.hypot(*np.diff(poly, axis=0).T)
    s = np.concatenate([[0], np.cumsum(seg)])
    n = max(int(s[-1] / step), 2)
    si = np.linspace(0, s[-1], n)
    return np.column_stack([np.interp(si, s, poly[:, 0]), np.interp(si, s, poly[:, 1])])


def fillet(p0, p1, p2, r, n=8):
    """Replace corner p1 (between p0 and p2) with a circular arc of radius r."""
    p0, p1, p2 = map(np.asarray, (p0, p1, p2))
    u, v = p0 - p1, p2 - p1
    lu, lv = np.linalg.norm(u), np.linalg.norm(v)
    u, v = u / lu, v / lv
    theta = math.acos(np.clip(np.dot(u, v), -1, 1))
    if r <= 0.05 or theta > math.pi - 1e-3:
        return [tuple(p1)]
    t = min(r / math.tan(theta / 2), 0.45 * lu, 0.45 * lv)
    r = t * math.tan(theta / 2)
    a, bpt = p1 + u * t, p1 + v * t
    bis = (u + v) / np.linalg.norm(u + v)
    centre = p1 + bis * (r / math.sin(theta / 2))
    a0, a1 = math.atan2(*(a - centre)[::-1]), math.atan2(*(bpt - centre)[::-1])
    if a1 - a0 > math.pi:
        a1 -= 2 * math.pi
    if a0 - a1 > math.pi:
        a1 += 2 * math.pi
    return [tuple(centre + r * np.array([math.cos(ang), math.sin(ang)])) for ang in np.linspace(a0, a1, n)]


def section(x, t_scale):
    """Half-section polyline from bottom stringer (0,0) round the rail to deck stringer (0,t)."""
    b = float(half_width(x))
    t = float(thick_shape(x)) * t_scale
    if b < 1 or t < 1:
        return np.array([[0, 0], [0, max(t, 0)]]), b, t
    a = flat_frac(x) * b
    c = bevel_frac(x) * t
    d = rail_frac(x) * t
    r = float(edge_r(x))
    v = a * math.tan(math.radians(float(deadrise(x))))      # chine rise from the soft-V nose
    pts = [(0, 0)]
    for s in np.linspace(0, 1, 12)[1:]:                       # parabolic soft V (flat when v == 0)
        pts.append((a * s, v * s * s))
    pts = pts[:-1] + fillet(pts[-2], (a, v), (b, c), r) + fillet((a, v), (b, c), (b, d), r) + [(b, d)]
    for s in np.linspace(0, 1, 60)[1:]:
        y = b * (1 - s)
        z = d + (t - d) * (1 - (y / b) ** DECK_N) ** (1 / DECK_N)
        pts.append((y, z))
    poly = resample(np.array(pts), 1.5)
    return poly, b, t


def half_area(poly):
    """Area between polyline and the stringer (y=0) axis, mm^2."""
    y, z = poly[:, 0], poly[:, 1]
    closed_y = np.concatenate([y, [0]])
    closed_z = np.concatenate([z, [0]])
    return 0.5 * abs(np.dot(closed_y[:-1], closed_z[1:]) - np.dot(closed_y[1:], closed_z[:-1]))


def volume_litres(t_scale, n=401):
    xs = np.linspace(0, LENGTH, n)
    areas = [2 * half_area(section(x, t_scale)[0]) for x in xs]
    return np.trapezoid(areas, xs) / 1e6


def inset(poly, d=None):
    """Offset an open convex half-section inward. d=None uses PANEL_SKIN_MM where the surface
    faces up/down (deck and bottom sandwich panels) and RAIL_SKIN_MM on the chine/rail band,
    blended over a few mm so the core has no step."""
    p = poly
    tang = np.gradient(p, axis=0)
    tang /= np.linalg.norm(tang, axis=1)[:, None] + 1e-12
    normal = np.column_stack([-tang[:, 1], tang[:, 0]])   # left of travel = inside for CCW traverse
    if d is None:
        panel = np.abs(normal[:, 1]) > math.cos(math.radians(35))
        d = np.where(panel, PANEL_SKIN_MM, RAIL_SKIN_MM).astype(float)
        k = np.ones(9) / 9
        d = np.convolve(np.pad(d, 4, mode="edge"), k, mode="valid")
        d = d[:, None]
    q = p + d * normal
    q[0, 0] = 0.0
    q[-1, 0] = 0.0
    return q


def solve_scale():
    lo, hi = 50.0, 300.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if volume_litres(mid) < TARGET_LITRES:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


T_SCALE = solve_scale()


def thickness(x):
    return thick_shape(x) * T_SCALE


def deck_z(x):
    return rocker(x) + thickness(x)


def volume_below(z_wl, t_scale=None, n=401):
    """Litres of hull below a horizontal waterline z_wl (board level, trim 0)."""
    t_scale = T_SCALE if t_scale is None else t_scale
    xs = np.linspace(0, LENGTH, n)
    areas = []
    for x in xs:
        poly, _, _ = section(x, t_scale)
        z = poly[:, 1] + float(rocker(x))
        under = np.minimum(z, z_wl) - float(rocker(x))
        under = np.maximum(under, 0)
        areas.append(2 * half_area(np.column_stack([poly[:, 0], under])))
    return np.trapezoid(areas, xs) / 1e6


def static_waterline(mass_kg):
    lo, hi = 0.0, 400.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if volume_below(mid) < mass_kg / 1.025:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    print(f"max thickness {T_SCALE:.1f} mm, volume {volume_litres(T_SCALE):.2f} L")
    for x in STATIONS:
        _, b, t = section(x, T_SCALE)
        print(f"x={x:5.0f}  width={2*b:6.1f}  thick={t:6.1f}  rocker={float(rocker(x)):5.1f}")
    for m in (7, 107):
        wl = static_waterline(m)
        print(f"{m} kg afloat: waterline {wl:.0f} mm above keel, transom immersed {wl - float(rocker(0)):.0f} mm, "
              f"freeboard at max thickness {deck_z(850) - wl:.0f} mm")
