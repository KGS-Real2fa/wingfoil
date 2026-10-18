# DIY 2.0 m / 120 L downwind pump wingfoil board

A home-built downwind board for a 95 kg rider (100 kg all-up) on an Armstrong HA 2450 or F-One 1950 foil. Hot-wire cut EPS core, vacuum-bagged carbon and PVC sandwich, basalt cloth on the rails.

| | |
|---|---|
| Size | 2000 × 560 × 154 mm, 120 L |
| Shape | Straight run from transom to 1000 mm, skiff-style hard aft chines, soft-V nose, boxy rails |
| Tracks | Dual 14 inch, 90 mm centres, 582 to 938 mm from the tail |
| Construction | EPS 20 kg/m³, 3 mm H80 PVC deck and bottom, 200 g carbon twill, carbon-aramid stance patch, 2 × 200 g basalt rail band |
| Weight budget | 7.1 kg ready to ride (6.7 kg without pad) |
| Materials | About 1000 € including consumables |

## Files

| File | What it is |
|---|---|
| [board-design/design-spec.md](board-design/design-spec.md) | Shape, hydrodynamic reasoning, tracks, hot-wire sequence, wing sizing, KT Drifter comparison |
| [board-design/layup-spec.md](board-design/layup-spec.md) | Layup schedule, bagging sequence, weight budget, engineering checks, sourcing |
| [board-design/bill-of-materials.xlsx](board-design/bill-of-materials.xlsx) | Costed shopping list, tools check, weight budget |
| [board-design/templates_A4.pdf](board-design/templates_A4.pdf) | 43 pages of full-scale templates, tiled on A4: 7 station sections, outline, rocker |
| [board-design/fullsize_plot.pdf](board-design/fullsize_plot.pdf) | Outline and rocker on one 2100 × 750 mm sheet for a plotter |
| [board-design/board_model.py](board-design/board_model.py) | Parametric model: every dimension comes from here |
| [board-design/templates.py](board-design/templates.py) | Generates both PDFs from the model |
| [board-design/make_bom.py](board-design/make_bom.py) | Generates the BOM spreadsheet |
| [docs/thread-transcript.md](docs/thread-transcript.md) | The design conversation that produced all of this |

## Regenerating

Needs Python 3 with `numpy`, `reportlab` and `openpyxl`.

```
cd board-design
python3 board_model.py   # prints volume, station dimensions, float check
python3 templates.py     # rewrites templates_A4.pdf and fullsize_plot.pdf
python3 make_bom.py      # rewrites bill-of-materials.xlsx (formulas are computed when opened)
```

Print the templates at 100% / actual size and check the 100 mm scale bar on each sheet before cutting.

## Status

Steps 1 (design and templates) and 2 (layup and weight budget) are done. Step 3, the build guide, is next. Open question: how much carbon-aramid is on hand, which decides whether it also replaces the deck inner glass.
