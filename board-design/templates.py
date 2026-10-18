"""Generate full-scale templates from board_model.py.

Outputs (next to this file):
  templates_A4.pdf     - cover/scale check, tiled station templates, tiled outline and rocker
  fullsize_plot.pdf    - outline + rocker on one 2100 x 750 mm sheet for a plotter / print shop
"""
import math
import os
import numpy as np
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

import board_model as bm

PAGE_W, PAGE_H = landscape(A4)            # points
MARGIN = 10 * mm
LABEL_H = 14 * mm
OVERLAP = 15.0                            # mm, tiled pages
LIGHT, MID, DARK = (0.82, 0.82, 0.82), (0.55, 0.55, 0.55), (0, 0, 0)


def polyline(c, pts, ox, oy, width=0.8, dash=None, color=DARK):
    c.setStrokeColorRGB(*color)
    c.setLineWidth(width)
    c.setDash(*(dash or ([], 0)))
    p = c.beginPath()
    p.moveTo(ox + pts[0][0] * mm, oy + pts[0][1] * mm)
    for x, y in pts[1:]:
        p.lineTo(ox + x * mm, oy + y * mm)
    c.drawPath(p, stroke=1, fill=0)
    c.setDash([], 0)


def scale_bar(c, x, y):
    c.setStrokeColorRGB(*DARK)
    c.setLineWidth(0.6)
    c.line(x, y, x + 100 * mm, y)
    for i in range(0, 101, 10):
        h = 3 * mm if i % 50 == 0 else 1.5 * mm
        c.line(x + i * mm, y, x + i * mm, y + h)
    c.setFont("Helvetica", 7)
    c.drawString(x, y - 3 * mm, "100 mm scale check: print at 100% / Actual size, no 'fit to page'")


# ------------------------------------------------------------------ geometry
XS = np.linspace(0, bm.LENGTH, 801)
HW = bm.half_width(XS)
ROCK = bm.rocker(XS)
THK = bm.thickness(XS)


def outline_lines():
    finished = np.column_stack([XS, HW])
    core = np.column_stack([XS, np.maximum(HW - bm.RAIL_SKIN_MM, 0)])
    return finished, core


def rocker_lines():
    bottom = np.column_stack([XS, ROCK])
    deck = np.column_stack([XS, ROCK + THK])
    core_bottom = np.column_stack([XS, ROCK + bm.PANEL_SKIN_MM])
    core_deck = np.column_stack([XS, ROCK + THK - bm.PANEL_SKIN_MM])
    chine = np.column_stack([XS, ROCK + bm.bevel_frac(XS) * THK])     # bottom edge of rail at the rail line
    rail_top = np.column_stack([XS, ROCK + bm.rail_frac(XS) * THK])
    return bottom, deck, core_bottom, core_deck, chine, rail_top


# ------------------------------------------------------------------ pages
def cover(c):
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN, PAGE_H - MARGIN - 6 * mm, "2.0 m / 120 L downwind pump board: full-scale templates")
    c.setFont("Helvetica", 9)
    lines = [
        f"Length {bm.LENGTH:.0f} mm, max width {2*HW.max():.0f} mm, max thickness {THK.max():.0f} mm, "
        f"volume {bm.volume_litres(bm.T_SCALE):.1f} L.",
        f"Bold lines = CORE cut lines: finished shape inset {bm.PANEL_SKIN_MM} mm on deck and bottom (PVC sandwich) and {bm.RAIL_SKIN_MM} mm on the rail band. Thin dashed = finished shape.",
        "Print every page at 100% (Actual size). Measure the 100 mm bar on each page before cutting anything.",
        f"Tiled pages overlap {OVERLAP:.0f} mm: trim one edge, align the 50 mm grid and x labels, tape, then glue to MDF/hardboard.",
        "Station templates are FULL sections tiled over A4 (stringer = dash-dot line). Female template: cut away the inside of the bold line.",
        "x is measured from the TAIL. Stations and tracks are marked on the outline and rocker templates.",
        "",
        f"Foil tracks: dual US-style, {bm.TRACK_SPACING:.0f} mm centres ({bm.TRACK_SPACING/2:.0f} mm each side of stringer), "
        f"{bm.TRACK_LEN:.0f} mm long,",
        f"   from x = {bm.TRACK_CENTRE_X - bm.TRACK_LEN/2:.0f} to {bm.TRACK_CENTRE_X + bm.TRACK_LEN/2:.0f} mm "
        f"(centre {bm.TRACK_CENTRE_X:.0f} mm from tail). Start with the mast plate mid-track.",
        f"Track block (long-dash line on outline): {bm.BLOCK_WIDTH:.0f} x {bm.BLOCK_LEN:.0f} mm, full depth, "
        f"x = {bm.TRACK_CENTRE_X - bm.BLOCK_LEN/2:.0f} to {bm.TRACK_CENTRE_X + bm.BLOCK_LEN/2:.0f} mm.",
        "",
        "Station   x from tail   x from nose   width   thickness   bottom rocker   chine height   rail-band top",
    ]
    for x in bm.STATIONS:
        _, b, t = bm.section(x, bm.T_SCALE)
        lines.append(f"  S{bm.STATIONS.index(x)+1}       {x:6.0f}        {bm.LENGTH-x:6.0f}     {2*b:6.0f}    {t:6.1f}"
                     f"        {float(bm.rocker(x)):5.1f}          {bm.bevel_frac(x)*t:5.1f}          {bm.rail_frac(x)*t:5.1f}")
    y = PAGE_H - MARGIN - 16 * mm
    for ln in lines:
        c.setFont("Courier" if ln.startswith("  S") or ln.startswith("Station   ") else "Helvetica", 9)
        c.drawString(MARGIN, y, ln)
        y -= 5 * mm
    scale_bar(c, MARGIN, MARGIN + 6 * mm)
    c.showPage()


def station_page(c, idx, x):
    poly, b, t = bm.section(x, bm.T_SCALE)
    core = bm.inset(poly)
    ox, oy = MARGIN + 4 * mm, MARGIN + 22 * mm
    # light 10 mm grid with 50 mm emphasis
    for gy in range(0, int(t) + 11, 10):
        polyline(c, [(0, gy), (b + 5, gy)], ox, oy, 0.25 if gy % 50 else 0.5, color=LIGHT)
    for gx in range(0, int(b) + 6, 10):
        polyline(c, [(gx, 0), (gx, t + 5)], ox, oy, 0.25 if gx % 50 else 0.5, color=LIGHT)
    polyline(c, [(0, -8), (0, t + 8)], ox, oy, 0.6, dash=([6, 2, 1, 2], 0), color=MID)   # stringer
    polyline(c, poly.tolist(), ox, oy, 0.4, dash=([3, 2], 0))
    polyline(c, core.tolist(), ox, oy, 1.4)
    c.setFont("Helvetica", 7)
    c.setFillColorRGB(*MID)
    c.drawString(ox - 2 * mm, oy - 11 * mm, "stringer")
    c.setFillColorRGB(*DARK)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(MARGIN, PAGE_H - MARGIN - 4 * mm, f"Station S{idx}: {x:.0f} mm from tail ({bm.LENGTH - x:.0f} mm from nose)")
    c.setFont("Helvetica", 8.5)
    c.drawString(MARGIN, PAGE_H - MARGIN - 9 * mm,
                 f"Half section. Full width {2*b:.0f} mm, thickness at stringer {t:.1f} mm, bottom rocker {float(bm.rocker(x)):.1f} mm. "
                 f"Bold = core (inset {bm.PANEL_SKIN_MM} mm deck/bottom, {bm.RAIL_SKIN_MM} mm rails), dashed = finished. Female template: cut away the inside of the bold line.")
    scale_bar(c, PAGE_W - MARGIN - 100 * mm, MARGIN + 4 * mm)
    c.showPage()


def tiled(c, title, lines, xr, yr, marks):
    """lines: list of (pts, width, dash). Tiles model-space rectangle xr x yr over A4 landscape pages."""
    aw = (PAGE_W - 2 * MARGIN) / mm
    ah = (PAGE_H - 2 * MARGIN - LABEL_H) / mm
    sx, sy = aw - OVERLAP, ah - OVERLAP
    ncol = math.ceil((xr[1] - xr[0] - aw) / sx) + 1 if xr[1] - xr[0] > aw else 1
    nrow = math.ceil((yr[1] - yr[0] - ah) / sy) + 1 if yr[1] - yr[0] > ah else 1
    for r in range(nrow):
        for col in range(ncol):
            x0, y0 = xr[0] + col * sx, yr[0] + r * sy
            ox, oy = MARGIN - x0 * mm, MARGIN + LABEL_H - y0 * mm
            c.saveState()
            clip = c.beginPath()
            clip.rect(MARGIN, MARGIN + LABEL_H, aw * mm, ah * mm)
            c.clipPath(clip, stroke=0, fill=0)
            for gx in range(int(x0 // 10) * 10, int(x0 + aw) + 10, 10):
                polyline(c, [(gx, y0), (gx, y0 + ah)], ox, oy, 0.5 if gx % 50 == 0 else 0.2,
                         color=MID if gx % 100 == 0 else LIGHT)
            for gy in range(int(y0 // 10) * 10, int(y0 + ah) + 10, 10):
                polyline(c, [(x0, gy), (x0 + aw, gy)], ox, oy, 0.5 if gy % 50 == 0 else 0.2,
                         color=MID if gy % 100 == 0 else LIGHT)
            for pts, w, dash in lines:
                polyline(c, pts.tolist() if hasattr(pts, "tolist") else pts, ox, oy, w, dash)
            c.setFont("Helvetica", 7)
            for mx, label, my in marks:
                polyline(c, [(mx, yr[0]), (mx, yr[1])], ox, oy, 0.6, dash=([4, 3], 0), color=(0.2, 0.2, 0.7))
                c.setFillColorRGB(0.2, 0.2, 0.7)
                c.drawString(ox + (mx + 1.5) * mm, oy + my * mm, label)
            c.setFillColorRGB(*MID)
            for gx in range(int(x0 // 100) * 100, int(x0 + aw) + 100, 100):
                for gy in range(int(y0 // 100) * 100, int(y0 + ah) + 100, 100):
                    c.drawString(ox + (gx + 1) * mm, oy + (gy + 1) * mm, f"x{gx}/y{gy}")
            c.restoreState()
            c.setStrokeColorRGB(*MID)
            c.setLineWidth(0.3)
            c.rect(MARGIN, MARGIN + LABEL_H, aw * mm, ah * mm)
            c.setFillColorRGB(*DARK)
            c.setFont("Helvetica-Bold", 10)
            c.drawString(MARGIN, MARGIN + 8 * mm, title)
            c.setFont("Helvetica", 8)
            c.drawString(MARGIN, MARGIN + 3 * mm,
                         f"sheet row {r+1}/{nrow}, col {col+1}/{ncol}   (x {x0:.0f} to {x0+aw:.0f} mm, y {y0:.0f} to {y0+ah:.0f} mm)")
            scale_bar(c, PAGE_W - MARGIN - 100 * mm, MARGIN + 6 * mm)
            c.showPage()


def station_tiled(c, idx, x):
    """Full (both halves) section at station x, tiled over A4 sheets."""
    poly, b, t = bm.section(x, bm.T_SCALE)
    core = bm.inset(poly)
    full = lambda p: np.vstack([np.column_stack([-p[::-1, 0], p[::-1, 1]]), p])
    stringer = np.array([(0, -8), (0, t + 8)])
    tiled(c, f"STATION S{idx}: {x:.0f} mm from tail, W {2*b:.0f}, T {t:.1f}",
          [(stringer, 0.6, ([6, 2, 1, 2], 0)), (full(poly), 0.4, ([3, 2], 0)), (full(core), 1.4, None)],
          (-b - 10, b + 10), (-10, t + 10), [])


def station_marks(y_label):
    marks = [(x, f"S{i+1} x={x}", y_label) for i, x in enumerate(bm.STATIONS)]
    t0, t1 = bm.TRACK_CENTRE_X - bm.TRACK_LEN / 2, bm.TRACK_CENTRE_X + bm.TRACK_LEN / 2
    marks += [(t0, f"track rear {t0:.0f}", y_label + 12), (t1, f"track front {t1:.0f}", y_label + 12)]
    return marks


def main():
    finished, core = outline_lines()
    bottom, deck, cb, cd, chine, rail_top = rocker_lines()
    ty = bm.TRACK_SPACING / 2
    t0, t1 = bm.TRACK_CENTRE_X - bm.TRACK_LEN / 2, bm.TRACK_CENTRE_X + bm.TRACK_LEN / 2
    track_rect = np.array([(t0, ty - 12), (t1, ty - 12), (t1, ty + 12), (t0, ty + 12), (t0, ty - 12)])
    track_cl = np.array([(t0 - 20, ty), (t1 + 20, ty)])
    b0, b1, bw = bm.TRACK_CENTRE_X - bm.BLOCK_LEN / 2, bm.TRACK_CENTRE_X + bm.BLOCK_LEN / 2, bm.BLOCK_WIDTH / 2
    block_rect = np.array([(b0, 0), (b0, bw), (b1, bw), (b1, 0)])
    stringer = np.array([(-10, 0), (bm.LENGTH + 10, 0)])

    c = canvas.Canvas(os.path.join(bm.OUT, "templates_A4.pdf"), pagesize=landscape(A4))
    c.setTitle("2.0 m 120 L downwind board templates")
    cover(c)
    for i, x in enumerate(bm.STATIONS):
        station_tiled(c, i + 1, x)
    tiled(c, "OUTLINE (half, stringer at y=0)",
          [(stringer, 0.6, ([6, 2, 1, 2], 0)), (finished, 0.4, ([3, 2], 0)), (core, 1.4, None),
           (track_rect, 0.8, None), (track_cl, 0.4, ([2, 2], 0)), (block_rect, 0.6, ([5, 2], 0))],
          (-10, bm.LENGTH + 10), (-10, HW.max() + 10), station_marks(HW.max() - 30))
    tiled(c, "ROCKER / PROFILE at stringer",
          [(bottom, 0.4, ([3, 2], 0)), (deck, 0.4, ([3, 2], 0)), (cb, 1.4, None), (cd, 1.4, None),
           (chine, 0.5, ([1, 2], 0)), (rail_top, 0.5, ([1, 2], 0))],
          (-10, bm.LENGTH + 10), (-10, (ROCK + THK).max() + 10), station_marks(-6))
    c.save()

    # single sheet for a plotter
    W, H = 2100 * mm, 750 * mm
    c = canvas.Canvas(os.path.join(bm.OUT, "fullsize_plot.pdf"), pagesize=(W, H))
    ox, oy = 50 * mm, 450 * mm
    polyline(c, stringer.tolist(), ox, oy, 0.6, dash=([6, 2, 1, 2], 0))
    for sgn in (1, -1):
        polyline(c, [(x, sgn * y) for x, y in finished], ox, oy, 0.4, dash=([3, 2], 0))
        polyline(c, [(x, sgn * y) for x, y in core], ox, oy, 1.4)
        polyline(c, [(x, sgn * y) for x, y in track_rect], ox, oy, 0.8)
        polyline(c, [(x, sgn * y) for x, y in block_rect], ox, oy, 0.6, dash=([5, 2], 0))
    for x in bm.STATIONS:
        hw = float(bm.half_width(x))
        polyline(c, [(x, -hw), (x, hw)], ox, oy, 0.5, dash=([4, 3], 0), color=(0.2, 0.2, 0.7))
    oy2 = 60 * mm
    for pts, w, d in [(bottom, 0.4, ([3, 2], 0)), (deck, 0.4, ([3, 2], 0)), (cb, 1.4, None), (cd, 1.4, None),
                      (chine, 0.5, ([1, 2], 0)), (rail_top, 0.5, ([1, 2], 0))]:
        polyline(c, pts.tolist(), ox, oy2, w, d)
    for x in bm.STATIONS:
        polyline(c, [(x, -5), (x, float(bm.deck_z(x)) + 5)], ox, oy2, 0.5, dash=([4, 3], 0), color=(0.2, 0.2, 0.7))
    c.setFont("Helvetica", 30)
    c.drawString(ox, H - 40 * mm, "2.0 m / 120 L downwind pump board: outline (top) and stringer rocker (bottom), 1:1, x from tail")
    scale_bar(c, ox, 20 * mm)
    c.save()


if __name__ == "__main__":
    main()
    print("written")
