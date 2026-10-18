from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment

import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bill-of-materials.xlsx")
F = "Arial"
BLUE = Font(name=F, color="0000FF")
BLACK = Font(name=F)
BOLD = Font(name=F, bold=True)
HEAD = Font(name=F, bold=True, color="FFFFFF")
HEAD_FILL = PatternFill("solid", start_color="1F3A5F")
SECTION_FILL = PatternFill("solid", start_color="DCE6F1")
YELLOW = PatternFill("solid", start_color="FFFF00")
EUR = '#,##0.00 "€";-#,##0.00 "€";"-"'
thin = Side(style="thin", color="BFBFBF")
GRID = Border(bottom=thin)

# (category, item, spec, qty_needed, buy_qty, unit, unit_price, basis, supplier, notes)
ROWS = [
    ("Core and foam", None),
    ("Core", "EPS core block", "EPS (PSE) 20 kg/m³, fused, cut to 2050 × 580 × 170 mm", "1 block", 1, "block", 40,
     "Estimate", "Local EPS/PSE manufacturer, cut to size", "Ask for one-piece 2050 mm length; a glued joint across the board is a weak point under the stance."),
    ("Sandwich", "PVC foam 3 mm, 80 kg/m³", "Divinycell H80 3 mm plain sheet, 1220 × 610 mm (item 5800301)", "2.1 m² (4 sheets)", 3.72, "m²", 42.20,
     "Quoted", "R&G, Germany: https://r-g.de/en/art/5800H80", "Box of 5 sheets = 3.72 m². Price incl. VAT, shipping extra. Two sheets butt-joined per side."),
    ("Track block", "PVC foam 50 mm, 130 kg/m³", "Divinycell H130 (or H100) 50 mm, piece ≥ 150 × 420 mm", "150 × 420 mm", 1, "piece", 25,
     "Estimate", "R&G or a DIAB distributor", "Top of the track block; the tracks are routed into this."),
    ("Track block", "PVC foam 50 mm, 60 kg/m³", "Divinycell H60 50 mm, two pieces ≥ 150 × 420 mm", "150 × 420 × 97 mm", 2, "piece", 10,
     "Estimate", "R&G or a DIAB distributor", "Stacked under the H130 to full core depth, sanded to the core line."),
    ("Reinforcements", None),
    ("Cloth", "Carbon twill 200 g/m²", "Carbon 3K 2 × 2 twill, 200 g/m², 1000 mm wide", "4.1 m", 4.2, "m", 35,
     "Estimate", "R&G, Castro Composites, Quai West Composites", "Deck and bottom full layers (2.05 m each); track patches cut from the offcut strip."),
    ("Cloth", "Carbon-aramid twill ~215 g/m²", "Carbon/aramid hybrid 2 × 2 twill, 200 to 215 g/m², ≥ 1000 mm wide", "1.0 m", 1.0, "m", 0,
     "On hand", "Quai West Composites (Bordeaux/Ciboure), 50.48 €/m if more is needed", "Karl has some. Stance patch 900 × 500 mm under the deck carbon."),
    ("Cloth", "Basalt twill 200 g/m²", "Basalt 2 × 2 twill, 200 g/m², 1000 mm wide", "1.4 m²", 2.0, "m", 22,
     "Estimate", "R&G, Castro Composites", "Rail band: 150 mm strips, two layers, plus transom corner patches."),
    ("Cloth", "E-glass 100 g/m²", "E-glass plain weave, 100 g/m², 1000 mm wide", "4.1 m", 4.2, "m", 6,
     "Estimate", "Any composites shop", "Inner skin under the PVC, deck and bottom (2.05 m each; a 560 mm panel does not nest twice in 1000 mm)."),
    ("Resin and fillers", None),
    ("Resin", "Laminating epoxy, slow", "Low-viscosity laminating epoxy with slow hardener (Sicomin, Resoltech or equal)", "2.5 kg mixed", 3.0, "kg kit", 38,
     "Estimate", "Sicomin distributor, Quai West Composites (Resoltech)", "Weigh resin to 1:1 with cloth weight; every 100 g/m² excess adds 0.23 kg."),
    ("Filler", "Glass microballoons", "Hollow glass bubbles for fairing/fill coat", "0.3 L", 1, "pack", 10,
     "Estimate", "Any composites shop", ""),
    ("Filler", "Colloidal silica", "Fumed silica thickener for bonding the track block", "50 g", 1, "pack", 8,
     "Estimate", "Any composites shop", ""),
    ("Filler", "Milled fibre / cotton flock", "For potting the track boxes", "100 g", 1, "pack", 8,
     "Estimate", "Any composites shop", ""),
    ("Hardware", None),
    ("Tracks", "Foil tracks 14 inch (356 mm)", "Pair of dual-track foil boxes, M8, 90 mm centres", "2", 2, "track", 50,
     "Estimate", "O'Karbon 14 in carbon tracks: https://www.okarbon.eu/product/foil-tracks/ ; fallback Foil-Tec 400 mm: https://foil-tec.com/en-us/collections/foil-tracks-boxes-and-inserts", "O'Karbon lists no price. Confirm the Armstrong A+ and F-One plates fit before buying. Foil-Tec 400 mm is USD 29.99 each from Australia."),
    ("Tracks", "M8 T-nuts and bolts", "4 T-nuts + 4 stainless M8 bolts", "1 set", 1, "set", 20,
     "Estimate", "Usually supplied with the mast plate", "Skip if your foil came with them."),
    ("Fittings", "Vent plug", "Gore-Tex breathable vent plug, flush", "1", 1, "each", 12, "Estimate", "Surf shop / shaping supply", ""),
    ("Fittings", "Leash plug", "Standard flush leash plug", "1", 1, "each", 6, "Estimate", "Surf shop / shaping supply", ""),
    ("Fittings", "Recessed carry handle", "Flush deck handle, epoxy-set", "1", 1, "each", 15, "Estimate", "Surf shop / shaping supply", ""),
    ("Finish", "Deck pad", "EVA 5 mm, 900 × 560 mm", "1", 1, "each", 40, "Estimate", "Surf shop / EVA sheet supplier", "Half-pad saves 0.2 kg."),
    ("Finish", "UV clear coat (optional)", "Two-pack polyurethane clear, 0.5 L", "0.5 L", 1, "tin", 25, "Estimate", "Marine paint supplier", "Optional; a sanded UV-stable epoxy finish is lighter."),
    ("Consumables", None),
    ("Bagging", "Peel ply", "Nylon peel ply, ≥ 1000 mm wide", "5 m", 5, "m", 3, "Estimate", "Any composites shop", ""),
    ("Bagging", "Perforated release film", "≥ 1000 mm wide", "5 m", 5, "m", 3, "Estimate", "Any composites shop", ""),
    ("Bagging", "Breather", "150 g/m² polyester breather, ≥ 1000 mm wide", "5 m", 5, "m", 3, "Estimate", "Any composites shop", ""),
    ("Bagging", "Vacuum bag film", "≥ 1500 mm wide; four pulls", "12 m", 12, "m", 2, "Estimate", "Any composites shop", ""),
    ("Bagging", "Sealant tape", "Tacky tape, 15 m rolls", "2 rolls", 2, "roll", 12, "Estimate", "Any composites shop", ""),
    ("Shop", "Mixing and laminating kit", "Cups, sticks, brushes, foam rollers, squeegees", "1 kit", 1, "kit", 25, "Estimate", "", ""),
    ("Shop", "Nitrile gloves", "Box of 100", "1", 1, "box", 10, "Estimate", "", ""),
    ("Shop", "Abrasives", "80 / 120 / 180 / 240 / 320 grit", "1 set", 1, "set", 25, "Estimate", "", ""),
    ("Shop", "Template board", "3 mm hardboard or MDF, 2440 × 1220 mm", "1", 1, "sheet", 15, "Estimate", "DIY store", "For the printed templates."),
    ("Shop", "Spray adhesive", "Repositionable, for gluing printouts to board", "1", 1, "can", 10, "Estimate", "DIY store", ""),
    ("Shop", "Acetone", "1 L", "1", 1, "L", 6, "Estimate", "DIY store", ""),
]

TOOLS = [
    ("Hot-wire cutter with 2.1 m bow or table", "Have"),
    ("Vacuum pump", "Have"),
    ("Vacuum gauge and bleed valve or regulator", "Check: the inner skins need −0.35 bar max so the EPS 20 does not crush"),
    ("Router with 8 to 12 mm straight bit", "Check: for the track block pocket and track slots"),
    ("Scales, 1 g resolution", "Check: for weighing resin to 1:1"),
    ("Carbon / aramid shears", "Check: aramid blunts ordinary scissors"),
    ("Sanding blocks, longboard", "Check"),
]

WEIGHT = [
    ("EPS core 20 kg/m³", "104 L after sandwich, block and skins", 2.08),
    ("PVC H80 3 mm, deck and bottom", "1.92 m² × 0.24 kg/m²", 0.46),
    ("Inner glass 100 g + resin", "1.92 m² × 0.30 kg/m²", 0.58),
    ("Carbon 200 g outer with wraps", "2.29 m² × 0.38 kg/m²", 0.87),
    ("Carbon-aramid stance patch", "0.45 m² × 0.38 kg/m²", 0.17),
    ("Bottom track patches, 2 × carbon", "2 × 520 × 350 mm × 0.38 kg/m²", 0.14),
    ("Basalt rail band, 2 × 200 g", "0.69 m² × 0.76 kg/m²", 0.52),
    ("Track block H130 + H60", "3.15 L × 130 + 6.1 L × 60 g/L", 0.78),
    ("14 inch track boxes and potting", "estimate", 0.55),
    ("Fill coat, sanding, clear coat", "estimate", 0.40),
    ("Vent, leash plug, handle", "estimate", 0.12),
    ("Deck pad 5 mm EVA", "0.9 m²", 0.45),
]

wb = Workbook()
ws = wb.active
ws.title = "BOM"
ws["A1"] = "2.0 m / 120 L downwind pump board: bill of materials"
ws["A1"].font = Font(name=F, bold=True, size=14)
ws["A2"] = ("Blue = editable input (quantities and prices). Black = formula. Price basis: Quoted = checked on the supplier page 2026-10-15/16; "
            "Estimate = typical EU retail, check before ordering; On hand = already owned.")
ws["A2"].font = Font(name=F, italic=True, size=9)
ws.merge_cells("A2:L2")
ws["A2"].alignment = Alignment(wrap_text=True)
ws.row_dimensions[2].height = 28

headers = ["#", "Category", "Item", "Specification", "Needed", "Buy qty", "Unit", "Unit price (€)", "Line cost (€)",
           "Price basis", "Supplier / link", "Notes"]
HR = 4
for c, h in enumerate(headers, 1):
    cell = ws.cell(row=HR, column=c, value=h)
    cell.font, cell.fill = HEAD, HEAD_FILL
    cell.alignment = Alignment(vertical="center", wrap_text=True)

r = HR + 1
n = 0
first = r
for row in ROWS:
    if row[1] is None:
        ws.cell(row=r, column=1, value=row[0]).font = BOLD
        for c in range(1, 13):
            ws.cell(row=r, column=c).fill = SECTION_FILL
        r += 1
        continue
    n += 1
    cat, item, spec, need, buy, unit, price, basis, sup, notes = row
    vals = [n, cat, item, spec, need, buy, unit, price, f"=F{r}*H{r}", basis, sup, notes]
    for c, v in enumerate(vals, 1):
        cell = ws.cell(row=r, column=c, value=v)
        cell.font = BLUE if c in (6, 8) else BLACK
        cell.border = GRID
        cell.alignment = Alignment(vertical="top", wrap_text=c in (4, 11, 12))
    ws.cell(row=r, column=8).number_format = EUR
    ws.cell(row=r, column=9).number_format = EUR
    if basis == "On hand":
        ws.cell(row=r, column=10).fill = YELLOW
    r += 1
last = r - 1

r += 1
for label, formula in [
    ("Total materials", f"=SUM(I{first}:I{last})"),
    ("of which quoted", f'=SUMIF(J{first}:J{last},"Quoted",I{first}:I{last})'),
    ("of which estimated", f'=SUMIF(J{first}:J{last},"Estimate",I{first}:I{last})'),
    ("Shipping allowance (edit)", 60),
    ("Total with shipping", f"=I{r}+I{r+3}"),
]:
    ws.cell(row=r, column=8, value=label).font = BOLD
    cell = ws.cell(row=r, column=9, value=formula)
    cell.number_format = EUR
    cell.font = BLUE if isinstance(formula, (int, float)) else BOLD
    r += 1
ws.cell(row=r - 2, column=10, value="Three to four parcels from DE, CZ/ES and FR; adjust to your quotes.").font = Font(name=F, size=9, italic=True)

widths = [4, 15, 28, 44, 16, 9, 8, 13, 13, 11, 44, 52]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[chr(64 + i)].width = w
ws.freeze_panes = ws.cell(row=HR + 1, column=4)

# Tools sheet
wt = wb.create_sheet("Tools check")
wt["A1"], wt["B1"] = "Tool", "Status"
for c in ("A1", "B1"):
    wt[c].font, wt[c].fill = HEAD, HEAD_FILL
for i, (tool, st) in enumerate(TOOLS, 2):
    wt.cell(row=i, column=1, value=tool).font = BLACK
    wt.cell(row=i, column=2, value=st).font = BLACK
wt.column_dimensions["A"].width = 42
wt.column_dimensions["B"].width = 80

# Weight sheet
ww = wb.create_sheet("Weight budget")
for c, h in enumerate(["Item", "Basis", "kg"], 1):
    cell = ww.cell(row=1, column=c, value=h)
    cell.font, cell.fill = HEAD, HEAD_FILL
for i, (item, basis, kg) in enumerate(WEIGHT, 2):
    ww.cell(row=i, column=1, value=item).font = BLACK
    ww.cell(row=i, column=2, value=basis).font = BLACK
    k = ww.cell(row=i, column=3, value=kg)
    k.font, k.number_format = BLUE, "0.00"
tr = len(WEIGHT) + 2
ww.cell(row=tr, column=1, value="Total, ready to ride").font = BOLD
t = ww.cell(row=tr, column=3, value=f"=SUM(C2:C{tr-1})")
t.font, t.number_format = BOLD, "0.00"
ww.cell(row=tr + 1, column=1, value="Without pad").font = BLACK
t2 = ww.cell(row=tr + 1, column=3, value=f"=C{tr}-C{tr-1}")
t2.number_format = "0.00"
ww.cell(row=tr + 3, column=1, value="Source: layup-spec.md weight budget, updated 2026-10-16 for 14 inch tracks (+0.3 kg over the 10 inch version).").font = Font(name=F, italic=True, size=9)
ww.column_dimensions["A"].width = 36
ww.column_dimensions["B"].width = 40
ww.column_dimensions["C"].width = 8

wb.save(OUT)
print("saved", OUT, "rows", first, last)
