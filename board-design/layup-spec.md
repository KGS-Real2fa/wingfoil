# Step 2: materials, layup schedule and weight budget

Board: 2000 × 560 × 154 mm, 120 L, from `board_model.py`. Rider 100 kg all-up. Build: hot-wire EPS core, vacuum-bagged wet layup, no CNC.

Skin areas measured from the model: deck 0.94 m², bottom 0.99 m², chine-and-rail band 0.34 m² (geometric; the basalt band is wider because it laps onto deck and bottom). Outline perimeter 4.57 m.

## Construction concept

Full sandwich on deck and bottom, basalt band round the rails, carbon everywhere else.

- **Why a sandwich.** On a 560 mm wide flat panel, a single carbon skin straight on EPS dents under heels and cracks on touchdowns. The fix is either a denser core and two skins per side (about +2.0 kg) or a 3 mm PVC foam skin under one carbon layer (+1.0 kg). The sandwich is lighter and stiffer, and it lets the core be 20 kg/m³, which is the single biggest weight lever on the board.
- **Why basalt on the rails only.** The PVC cannot wrap the sharp aft chines or the vertical rail band, so that band gets cloth only. Basalt (E about 85 GPa, elongation 3%, density 2.7) takes rail knocks and mast-tip hits far better than carbon (elongation 1.5%), and it is where impacts actually land. Carbon stays on the panels, where stiffness per gram matters.
- **Why no stringer.** Global bending is trivial on a 154 mm thick carbon box (see checks below). All the structure goes into the panels and the track block.

## Bill of materials

The costed shopping list with links is in `bill-of-materials.xlsx`. Summary:

| Item | Spec | Quantity |
|---|---|---|
| Core | EPS 20 kg/m³ block, fused, 2050 × 580 × 170 mm | 1 |
| Deck and bottom sandwich | PVC foam 3 mm, 80 kg/m³ (Divinycell H80, Airex C70.75 or equal) | 2.1 m² (two sheets 2050 × 600, or four 1250 × 600 butt-joined) |
| Track block, top | PVC foam 130 kg/m³ (H130), 50 mm thick | 150 × 420 mm |
| Track block, lower | PVC foam 60 kg/m³ (H60), to full depth under the H130 | 150 × 420 × 97 mm (two 50 mm sheets) |
| Outer skins | Carbon 200 g/m² 2 × 2 twill, 1000 mm wide | 4.2 m |
| Stance patch | Carbon-aramid 2 × 2 twill, 200 to 215 g/m², 1000 to 1200 mm wide | 1.0 m |
| Rail band | Basalt 200 g/m² twill, 1000 mm wide | 2.0 m (cut into 150 mm strips, straight grain) |
| Inner skins | E-glass 100 g/m² plain weave, 1000 mm wide | 4.2 m |
| Resin | Low-viscosity laminating epoxy, slow hardener, 24 h pot-to-sand (Sicomin SR 8100, Resoltech 1050, West 105/206 or equal) | 3 kg kit (2.5 kg used) |
| Fairing | Epoxy + microballoons (glass bubbles) for the fill coat | 0.3 L bubbles |
| Tracks | Two 14 inch (356 mm) foil track boxes, M8, 90 mm centres | 2 |
| Fittings | Gore-Tex vent plug, leash plug, recessed deck handle | 1 each |
| Pad | 5 mm EVA, 900 × 560 mm | 1 |
| Consumables | Peel ply, perforated release film, breather, bag film, tacky tape, 150 mm vacuum gauge, regulator or bleed valve | |

## Layup schedule, outside in

Thickness used for the core insets: deck and bottom panels 3.8 mm, rail band 1.0 mm. The templates already carry these.

**Bottom**

1. Carbon 200 g twill, full bottom, wrapped 40 mm up over the chine onto the rail band. Fibres at 0/90 along the board.
2. Track patch: two layers carbon 200 g, 520 × 350 mm centred on the tracks, edges staggered 25 mm, under the full layer. The patch sits on the PVC, not in place of it.
3. PVC H80 3 mm, full bottom, stopping at the chine line (the chine corner stays a sharp foam edge; the basalt band wraps it).
4. E-glass 100 g inner skin, full bottom, bonds PVC to EPS.

**Deck**

1. Carbon 200 g twill, full deck, wrapped 40 mm over the rail band.
2. Stance patch: one layer carbon-aramid 2 × 2 twill, 200 to 215 g, 900 × 500 mm, from 450 to 1350 mm from the tail, under the full carbon layer (see the carbon-aramid section below).
3. PVC H80 3 mm, full deck, stopping at the top of the vertical rail band.
4. E-glass 100 g inner skin.

**Rail band (chine, vertical rail, 50 mm onto deck and bottom)**

1. Basalt 200 g, 150 mm wide, two layers, laid last on each side so the basalt is outermost on the rails. Stagger the two layers 15 mm. Join strips with 30 mm overlaps, never at the tail corners.
2. At the transom corners add a third basalt patch, 150 × 150 mm, folded round the corner.

**Track block**

1. Rout a 150 × 420 mm pocket through the full core depth, centred at 760 mm from the tail (550 to 970 mm; marked on the outline template). Bond the H60 stack and the H130 top (tracks go into the H130) with thickened epoxy, under vacuum. Fair flush to the bottom core line.
2. Rout the track slots in the H130 and pot the boxes in epoxy thickened with milled fibre, with the mast plate bolted to the boxes to hold them parallel and at 90 mm centres while it cures.

## Bagging sequence (four pulls)

1. Deck inner: glass 100 g wet-out, PVC panel on top, bag at −0.35 bar max (EPS 20 crushes above about −0.5 bar). Breather only, no peel ply needed. Cure overnight.
2. Bottom inner: same, with the track block already bonded in.
3. Bottom outer: carbon full layer with the track patch, then the basalt band on this side, peel ply, perforated film, breather. Bag at −0.4 bar.
4. Deck outer: carbon with the stance patch, basalt band to meet the bottom band with a 50 mm overlap on the vertical rail, peel ply, breather. Bag at −0.4 bar.

Then: fill coat of epoxy and microballoons only where the weave needs it, sand, fit the vent, leash plug and handle in epoxy-filled recesses, clear UV topcoat (two-pack polyurethane) or leave sanded with a UV-stable epoxy. Pad last.

## Weight budget

| Item | Basis | kg |
|---|---|---|
| EPS core 20 kg/m³ | 104 L after sandwich, block and skins | 2.08 |
| PVC H80 3 mm, deck and bottom | 1.92 m² × 0.24 kg/m² | 0.46 |
| Inner glass 100 g + resin | 1.92 m² × 0.30 kg/m² (resin uptake into EPS included) | 0.58 |
| Carbon 200 g outer, deck and bottom with wraps | 2.29 m² × 0.38 kg/m² | 0.87 |
| Deck stance patch | 0.45 m² × 0.38 | 0.17 |
| Bottom track patches | 0.36 m² × 0.38 | 0.14 |
| Basalt rail band, 2 × 200 g | 0.69 m² × 0.76 kg/m² | 0.52 |
| Track block H130 + H60 | 3.15 L + 6.1 L | 0.78 |
| 14 inch track boxes and potting | | 0.55 |
| Fill coat, sanding, clear topcoat | | 0.40 |
| Vent, leash plug, handle | | 0.12 |
| Deck pad 5 mm EVA | 0.9 m² | 0.45 |
| **Total, ready to ride** | | **7.1** |

Expect 6.8 to 7.6 kg (the 14 inch tracks and longer block added 0.3 kg on 2026-10-16; a lower block in H45 instead of H60 would win back 0.1 kg). Production 120 L downwind boards run 6.5 to 8 kg, so this is a light board, not a fantasy. Levers if it comes in heavy: resin control (every 100 g/m² of excess resin over 2.3 m² is 0.23 kg; weigh the resin, aim at 1:1 with cloth weight before bagging), and the pad (a half-pad saves 0.2 kg). Going to 25 kg/m³ core costs 0.53 kg; 30 kg/m³ costs 1.06 kg.

## Engineering checks

- **Global bending.** Touchdown at 2.5 g, 2450 N through the feet 300 mm either side of the mast: 735 N·m. Section at the stance: 560 wide, 150 mm between skin centroids, 0.2 mm carbon skins. Skin stress 735 / (0.56 × 0.0002 × 0.15) = 44 MPa against 600 MPa plus for twill carbon. Safety factor above 10; the sandwich and the panel loads govern, not the beam.
- **Track block crushing.** Foil lift 1000 N on a 0.85 m mast with the rider off-centre gives up to 900 N·m at the plate. Over a 165 mm plate that is a 5.5 kN couple on half the plate area (0.0074 m²): 0.74 MPa. H130 compressive strength is 3.0 MPa (safety 4). The same block in H80 gives 1.9 and in bare EPS 20 it fails, which is why the block exists.
- **Box pull-out.** Each box has about 0.03 m² of bonded side area; at 1.1 MPa shear for H130 that is 33 kN against bolt loads under 4 kN.
- **Panel denting.** 3 mm H80 under 200 g carbon gives a heel-load panel that matches production sandwich boards; the stance patch doubles the skin where the heels land.

## What this changes in the templates

Core lines are now inset 3.8 mm on the deck and bottom panels and 1.0 mm on the rail band, blended over a few millimetres at the chine. `templates_A4.pdf` and `fullsize_plot.pdf` have been regenerated with these insets. The EPS blank needed is 2050 × 580 × 170 mm.

## Sourcing: 3 mm 80 kg/m³ PVC foam, France and EU (checked 2026-10-15)

No French web shop found that stocks plain 3 mm H80 or Airex C70.75 off the shelf for individuals. The French routes are trade channels; the hobby-size stock sits in Germany, Czechia and Spain, all of which ship to France.

| Source | What | Notes |
|---|---|---|
| [R&G, Germany: Divinycell H80 1220 × 610 mm](https://r-g.de/en/art/5800H80) | 1, 1.5, 2, 3, 5, 10 mm plain sheets | 3 mm: 42.20 €/m² incl. VAT in a box of 5 (3.7 m², enough for the board with the deck and bottom each in two butt-joined sheets). Ships to France. |
| [Havel Composites, Czechia: Airex C70.75 3 mm, 2180 × 1020 mm](https://www.havel-composites.com/en/products/airex-c-70-75-th-3-mm-2180-x-1020-mm) | One sheet covers one whole side with no joint | Page would not load from here; confirm price and stock. Two sheets needed. |
| [Lindinger, Austria: R&G Airex C70.75 2000 × 500 × 3 mm](https://www.lindinger.at/fr/Accessoires-de-construction/Materieux/Barres-tubes-plaques/R-G-AIREX-plaque-C70.75-vert-2000-x-500-x-3-mm-Paquet-20-Pieces/9780234) | Pack of 20 | 500 mm is narrower than the 560 mm board; would need a centre joint. Not the first choice. |
| [Castro Composites, Spain (FR site): Divinycell H80 3 mm](https://www.castrocompositesshop.com/en/sandwich-cores/1379-divinycell-h80-gsc10-contour-scrim-pvc-foam-3-mm-8431252522187.html) | 1220 × 813 mm, 41.60 € excl. tax | Contour-cut on a scrim (GSC10): it prints a grid through thin skins and holds resin. Avoid for this build; their [PVC foam category](https://www.castrocompositesshop.com/en/89-pvc-foams) shows no plain 3 mm. |
| [Sicomin, Châteauneuf-les-Martigues: Airex core materials](https://sicomin.com/en/epoxy-products/core-materials/airex) | French manufacturer and distributor | Trade sales by quote via their contact form; worth a call since they are in France and also supply the epoxy. |
| Gazechim Composites (France) | DIAB and Airex trade distributor | Pro accounts; ask a local shaper or boatyard to add two sheets to an order. |

Equivalents: Divinycell H80, Airex C70.75, Gurit PVC 80 are interchangeable at 3 mm for this job; Airex C70.75 is the surf-industry standard.

## Carbon-aramid twill under foot (2026-10-15)

Karl asked about a carbon-Kevlar twill under the feet in place of pure carbon. Verdict: yes for the **stance patch**, laid **under** the full carbon layer; no for the full deck layer.

- **What it buys.** Aramid stops cracks and holds a punctured skin together. A heel strike after a fall, or a mast-tip hit from the foil, cracks a pure carbon skin into a sharp-edged hole that lets water in; the same hit on a hybrid leaves a dent with the skin intact. For a board that gets knee-paddled and climbed onto in chop, that is the realistic failure mode, so the toughness is worth having where the heels land.
- **What it costs.** A 50/50 hybrid has half the carbon tows, so that layer is about 30% less stiff in-plane (aramid E 70 to 80 GPa against carbon 230). On the stance zone the deck has two layers plus the 3 mm PVC, and the PVC does most of the dent resistance, so the stiffness loss is not noticeable. Weight: 215 g against 200 g, plus 0.01 kg. Cost about 50 € per metre against 35 to 40 € for carbon.
- **Why under, not over.** Aramid fuzzes when sanded and wicks water where fibres are exposed; it also yellows in UV. With the hybrid as the inner stance layer and carbon on top, the outer skin is sandable, the fuzz never appears, and the aramid sits where crack arrest matters.
- **Why not the whole deck.** Aramid is weak in compression (about a fifth of its tensile strength). The deck is the compression face in global bending, and although the stresses are tiny (44 MPa), a full hybrid deck would also be a nightmare to fair at the rail laps and around the handle recess.

Change to the schedule: deck layer 2 becomes **carbon-aramid 2 × 2 twill, about 200 to 215 g/m², 900 × 500 mm from 450 to 1350 mm from the tail**, under the full 200 g carbon layer. Sources: [Quai West Composites (Bordeaux and Ciboure): sergé carbone-aramide 215 g, 1200 mm wide, 50.48 € per metre](https://boutique.quai-west-composites.fr/tissus/305-serge-carbone-aramide-200gr.html), or [R&G CAT-200100: carbon-aramid twill 205 g, 100 cm wide](https://www.r-g.de/en/art/CAT-200100). One metre is enough.

## Can the carbon-aramid replace the PVC? (2026-10-15)

No. They do different jobs. The PVC is a spacer and a load spreader: it moves the skin away from the EPS and turns the skin into a tiny sandwich that spreads a heel over enough area for 20 kg/m³ foam to carry it. A cloth layer, carbon or aramid, has no thickness and spreads nothing.

Numbers, per metre of panel width:
- Local bending stiffness of two cloth layers straight on EPS (0.5 mm, E about 60 GPa): E t³/12 = 0.6 N·m.
- The same outer layer over 3 mm PVC with the inner glass: E t d²/2 = about 60 N·m. A hundred times stiffer for 0.54 kg/m² instead of 0.38.
- A heel is 100 kg on about 30 cm²: 0.33 MPa. EPS 20 yields at about 0.09 MPa, so the skin must spread the load over four times the heel area or the core crushes under the skin and the dent stays. The sandwich does that; cloth on foam does not, which is why boards without a sandwich use 30 kg/m³ or denser cores and still dent.
- To get the same spreading from cloth alone you would need roughly 1 mm of laminate (five layers of 200 g): 1.9 kg/m², three and a half times the weight of the sandwich, and the aramid's lower modulus makes it worse at this than carbon.

Where the aramid helps is after the dent: it keeps the skin in one piece. That is why it goes in the stance patch on top of the PVC, not in place of it.

The only real substitute for the PVC skin is another thin stiff sheet: 1.5 to 2 mm paulownia or balsa veneer ("compsand" construction), which is cheaper and easy to find in France but heavier (about 0.5 kg/m² for paulownia at 2 mm) and needs to be wetted and bagged in two stages to take the deck crown. If PVC proves hard to buy, that is the fallback.
