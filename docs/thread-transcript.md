# Design thread transcript

The design conversation between Karl and Claude, 15 to 18 October 2026, as posted in the Claude project thread. Progress checklists and system notices are left out; messages are verbatim. Links to the shared project folder have been rewritten to point at the files in this repository. Some messages describe earlier versions of the design that were later changed; the files in `board-design/` are the current state.

---

**Karl** · 2026-10-15 10:42
Started this thread from a suggestion ("Help me work out a plan for a project").

**Claude** · 10:43
To shape this I need a few facts from you. Short answers are fine.

1. Your weight, and what front wing and mast you'll ride (brand/area, mast length, box type: Tuttle or dual track)?
2. Which tools do you have: hot-wire cutter, CNC, vacuum bagging pump, or just hand tools?
3. Is there a target finished weight in mind, or just "as light as practical while still strong enough"?

Here's my draft plan, before I start:

1. **Design spec.** Settle the outline, rocker, rails, deck and bottom shape, and where the foil box goes for 2.0 m and 120 L. I'd start around 2000 × 50 cm and ~11 cm thick, with a narrow nose and a flat, slightly concave standing area so it pumps up easily.
2. **Materials and layup schedule.** Choose the EPS/XPS core density and basalt cloth weights per zone (deck, bottom, rails, foil box), plus PVC or wood reinforcement and the epoxy system. This step also includes a weight budget. Basalt is about 45% denser than carbon and less stiff, so where it adds weight it needs a sandwich layer rather than just more plies.
3. **Templates and cut files.** Full-scale printable outline, rocker and cross-section templates, plus hot-wire or CNC files if you have those tools.
4. **Build guide.** A step-by-step for shaping, laminating (vacuum bag or wet layup), installing the foil box, adding the leash and pad points, and finishing.

Edit, add or cut steps as you like, and I'll start on step 1 once you answer.

**Karl** · 10:46
95kg plus wet  suit and wing  foil is either a 2450 armstrong or a 1950 Fone   I do not have CND, I do have vaccum bagging  I do have hot wire  ,  I will need at least 5 station templates and track locations.  that are full printable on A4 sheets .   change my idea of using bassalt cloth and use carbon.  use bassalt cloth only on the rails/edges because of durability.

**Claude** · 10:47
Got it: carbon with basalt rails, hot-wire plus vacuum bag, and A4 station templates. I'm starting on the design spec and templates now.

**Claude** · 10:52
The design spec and full-scale templates are done. Next I need your OK on the shape below, or any changes, before I start step 2 (the carbon layup with basalt rails, plus a weight budget).

- **Size:** 2000 × 540 mm, 159 mm thick, which comes out at exactly 120 L. At this length, 120 L forces that thickness. Going to 560 mm wide would bring it down to about 150 mm, but then the station templates would no longer fit on one A4 sheet.
- **Shape for pumping:** the bottom is flat from 300 to 1000 mm from the tail, then rises to 112 mm of nose rocker. It has a chined bottom, boxy rails and a square tail with a sharp release edge.
- **Tracks:** two US-style tracks at 90 mm centres, running 635 to 885 mm from the tail. Start with the mast plate in the middle of the track for both foils. That starting point is my estimate, not a measured figure, so check that your Armstrong and F-One plates fit 90 mm M8 tracks.
- **Templates:** [templates_A4.pdf](../board-design/templates_A4.pdf) has 7 half-section station templates, one per A4 sheet. It also has tiled outline and rocker templates with the tracks and stations marked, and every sheet has a grid and a 100 mm scale bar. [fullsize_plot.pdf](../board-design/fullsize_plot.pdf) is a single sheet for a print shop.
- **Core lines:** the bold lines are the core cut lines, inset 1.5 mm for the laminate. If step 2 adds a PVC deck sandwich, I'll regenerate them.

Details and the hot-wire cutting order are in [design-spec.md](../board-design/design-spec.md). Everything comes from [board_model.py](../board-design/board_model.py), so any change is a single rerun.

**Karl** · 10:53
you misunderstood.  the A4 limit is that the templates need to be mulitple A4 sheets taped together to form the template.  there is no requirement that the whole design fit on an a4

**Claude** · 10:53
Understood, templates can span taped sheets. I'm widening the board to 560 mm and making the station templates tiled full sections.

**Claude** · 10:54
The templates are fixed. Since sheet size no longer constrains anything, I widened the board to 560 mm, which drops the thickness from 159 to 154 mm at the same 120 L. A thinner board keeps the deck closer to the foil, which helps pumping.

- **Stations:** all 7 stations are now full-width sections, 2 to 3 A4 sheets each. The outline takes 16 sheets and the rocker 8, for 43 pages in total. Every sheet has a 15 mm overlap, a grid with coordinates and a 100 mm scale bar.
- **Tracks:** the track positions are unchanged, 635 to 885 mm from the tail at 90 mm centres.
- **Files:** I updated [templates_A4.pdf](../board-design/templates_A4.pdf), [fullsize_plot.pdf](../board-design/fullsize_plot.pdf) and [design-spec.md](../board-design/design-spec.md).

Once you're happy with the shape, I'll start step 2: the carbon layup with basalt rails and a weight budget.

**Karl** · 10:58
consider the hydrodynamics of adding a double tunnel shape to the bottom along the lines of what the Americas Cup hulls look like

**Claude** · 10:59
Looking at how an AC75 bottom works and whether it transfers to a 2 m board that pumps up at about 6 knots. Analysis coming.

**Claude** · 11:00
Short answer: I'd leave the tunnels off. The AC75 bottom solves problems this board doesn't have.

- **Speed regime.** With your weight on the foil, take-off is roughly 6 to 7 kt on the 2450 and 7 to 8 kt on the 1950 (Froude 0.7 to 0.9 on a 2 m hull, whose hull speed is 3.4 kt). The whole pump-up happens in the semi-displacement hump, where wave drag from the volume distribution dominates. Tunnels only pay off once air can get into them, at planing speeds this board never reaches with its bottom wet.
- **What the AC75 shape actually does.** The central bustle seals the gap under the mainsail (aero end-plating) and gives a narrow wetted strip on touchdowns. The hollows either side are in the air when foiling. A wing board gets no end-plate benefit, and the touchdown benefit comes from the narrow spine, not the tunnels.
- **Friction isn't the issue.** Shallow tunnels add about 1 mm to a 560 mm wetted perimeter; even 25 mm deep ones add 3%.
- **What tunnels cost you.** Tunnels running out through the tail hold water at the moment the board breaks free, which is the moment that matters for pumping. A flat plate gives the most dynamic lift per wetted area in the hump. Two ridges resist banking into turns. The track boxes need a flat 120 mm plate zone, so tunnels would have to start 70 mm out from the stringer. And a hot wire can't cut longitudinal concaves, so they're hand shaped, and bagged carbon bridges the ridges.
- **What does transfer:** a soft rounded V in the nose section forward of 1400 mm for AC75-style quiet touchdowns. I'll add that to the model.

If you still want to try it, the workable version is a shallow double concave, 4 to 5 mm deep, from 400 to 1200 mm, fading out 200 mm before the tail, with a flat 140 mm spine under the tracks. Full notes are in [design-spec.md](../board-design/design-spec.md#bottom-shape-double-tunnels-considered-2026-10-15).

One word back, please:
- **Flat** (recommended): keep the chined flat bottom, add the soft-V nose.
- **Concave**: I'll model the shallow double concave and regenerate the templates.

**Karl** · 12:11
no on the double concave.  what about a sharper stern separation.  the 49er  and I14 skiffs all use very sharp aft sections to improve flow separation in the stern, particularly in the 7-10knot hull speed

**Claude** · 12:12
Agreed on the skiff stern. I'm putting a straight run, hard aft edges and a dry-transom check into the model now.

**Claude** · 12:14
Yes, the skiff stern transfers directly, and it's now in the model and the regenerated templates. It is the right idea for exactly the reason you give: at Froude 0.5 and above the transom runs dry, and a hard edge lets the flow leave tangent instead of wrapping round a radius and sucking the tail down. Our 6 to 8 kt take-off band sits squarely in that regime.

What changed:
- **Zero tail kick.** The bottom is now dead straight from the transom to 1000 mm. The 5 mm kick I had is a surfboard turning feature and was only drag here.
- **Hard aft chines.** Both bottom-edge corners have zero radius from the transom to 500 mm, then soften to 4 mm at 900 and 14 mm at the nose. The first station template now shows sharp corners; the nose stations are rounded.
- **Square transom** with a sharp edge all round.
- **Flat aft, not V.** I went 49er rather than I14: a flat run gives the most lift per wetted area in the hump and the cleanest release. V aft would cost both.
- **Soft-V nose** forward of 1300 mm, as promised earlier, for quiet touchdowns.

One honest caveat: at rest with you standing on it, the transom is 127 mm under and the tail deck is awash. That is simply 120 L under 107 kg and it only matters below about 4 kt; the wing pulls you through that in seconds.

Updated files: [templates_A4.pdf](../board-design/templates_A4.pdf), [design-spec.md](../board-design/design-spec.md#stern-skiff-style-separation-2026-10-15). Unless you want more shape changes, I'll start step 2, the carbon layup with basalt rails and the weight budget.

**Karl** · 12:21
under 4 knots is acceptable.   what sized wing would be estimated needed to fly in 14 knots of breeze at my weight in this configuration

**Claude** · 12:22
About **6 m²** with the HA 2450 in 14 kt at your weight; take a 7 m² if you pair it with the 1950 or want easy take-offs in the lulls. This is an estimate, not a measurement.

How I got there:
- **Drag at take-off** comes to about 190 N on the 2450 and 200 N on the 1950: half your weight still on the hull in the hump (R/Δ about 0.16), half on the foil at L/D 10, plus mast and fuselage drag.
- **A quasi-static balance** (beam reach, no pumping, no gust, 15 kt apparent, CL 0.9, 55% of the aero force as drive) would ask for 10 m². Nobody takes off like that.
- **A real take-off** (bear off in a 16 kt gust, sheet hard, pump the foil for an extra 50 N) brings the same balance down to about 4 m². That is the floor, not the plan.
- Field practice for 95 to 100 kg riders on 2000 to 2500 cm² high-aspect foils sits between those: 6 m² is the normal 14 kt wing, 7 m² the comfortable one, 5 m² for a strong pumper in gusty 14 plus.

For downwinding the smallest wing that gets you up wins, since it's flagged for the rest of the run, which points at the 6 m² with the 2450. The board's low take-off speed and clean release are exactly what let a 100 kg rider get away with 6 m² instead of 7.

The working is in [design-spec.md](../board-design/design-spec.md#wing-size-for-14-kt-at-100-kg-2026-10-15). Ready to start step 2 when you say so.

**Karl** · 12:28
start step 2

**Claude** · 12:30
Starting step 2: measuring skin areas from the model, then the carbon and basalt layup with a weight budget.

**Claude** · 12:33
Step 2 is done: [layup-spec.md](../board-design/layup-spec.md). Budget comes to **6.8 kg ready to ride** (expect 6.5 to 7.3). Please check the construction choices below, then I'll write the step 3 build guide.

- **Construction:** 20 kg/m³ EPS core, 3 mm H80 PVC sandwich on deck and bottom under one layer of 200 g carbon twill, 100 g glass inner skin. The sandwich is what lets the core be 20 kg/m³ (the biggest weight lever) without heel dents or touchdown cracks; the alternative of a denser core and two skins per side costs about 1 kg more.
- **Basalt:** two layers of 200 g, 150 mm wide, wrapping the chines and the vertical rail band and lapping 50 mm onto deck and bottom, laid outermost. The PVC can't wrap the sharp aft chines anyway, so that band is exactly where the tougher cloth earns its place.
- **Track block:** 150 × 350 mm, full depth, H130 top 50 mm for the boxes over H60 below. The check that justifies it: up to 900 N·m at the mast plate gives 0.74 MPa under the plate, which H130 takes with a safety factor of 4 and bare EPS does not take at all.
- **Patches:** two extra carbon layers over the tracks, one over the stance. No stringer; the 154 mm box has a bending safety factor above 10.
- **Bagging:** four pulls, −0.35 bar for the inner skins so the EPS doesn't crush, −0.4 for the outers. Full sequence, BOM and metre counts are in the file.
- **Templates regenerated:** core lines are now inset 3.8 mm on the panels and 1.0 mm on the rails. Blank needed is 2050 × 580 × 170 mm.

Two things you may want to change: the full-length 5 mm pad is 0.45 kg of the total, and the 2.5 kg epoxy kit assumes you weigh resin to 1:1 with cloth, since every 100 g/m² of excess resin adds 0.23 kg.

**Karl** · 13:16
provide links to sources for H80 pvc in france.  and consider the effects of using Carbon Kevlar twill under foot in place of pure carbon

**Claude** · 13:16
Searching French suppliers for 3 mm H80 PVC foam now, then the carbon-Kevlar under-foot analysis.

**Claude** · 13:19
**PVC foam:** I found no French web shop stocking plain 3 mm 80 kg/m³ sheet for individuals; the French channels are trade (Sicomin by quote, Gazechim via a pro account). The practical routes all ship to France:
- [R&G, Germany: Divinycell H80 3 mm, 1220 × 610 mm](https://r-g.de/en/art/5800H80), 42.20 €/m² in a box of 5. That box (3.7 m²) covers the board with deck and bottom each in two butt-joined sheets. My recommendation.
- [Havel Composites, Czechia: Airex C70.75 3 mm, 2180 × 1020 mm](https://www.havel-composites.com/en/products/airex-c-70-75-th-3-mm-2180-x-1020-mm). One sheet per side, no joint. The page wouldn't load for me, so confirm price and stock.
- [Castro Composites, Spain, French-language site: H80 3 mm](https://www.castrocompositesshop.com/en/sandwich-cores/1379-divinycell-h80-gsc10-contour-scrim-pvc-foam-3-mm-8431252522187.html) is contour-cut on a scrim, which prints a grid through a thin skin and drinks resin. Avoid.
- [Sicomin, Châteauneuf-les-Martigues](https://sicomin.com/en/epoxy-products/core-materials/airex) lists Airex cores but sells by quote; worth a call since they also do the epoxy.

**Carbon-aramid under foot:** yes, but as the stance patch under the full carbon layer, not as the outer skin. Aramid arrests cracks, so a heel strike or a mast-tip hit leaves a dent instead of a sharp hole that lets water in. The costs are small here: that layer is about 30% less stiff, but the PVC does the dent resistance and the stance has two layers anyway; weight is +0.01 kg. Keeping it under the carbon avoids the two real problems, which are fuzz when sanded and wicking at exposed fibres, plus UV yellowing. I would not use it for the whole deck: aramid is weak in compression and miserable to fair at the rail laps. Source: [Quai West Composites, Bordeaux and Ciboure: sergé carbone-aramide 215 g, 1200 mm wide, 50.48 €/m](https://boutique.quai-west-composites.fr/tissus/305-serge-carbone-aramide-200gr.html). One metre does it.

Both are written into [layup-spec.md](../board-design/layup-spec.md#sourcing-3-mm-80-kgm-pvc-foam-france-and-eu-checked-2026-10-15), and the schedule and BOM now carry the hybrid patch.

**Karl** · 13:48
can the carbon/aramid twill replace the PVC layer

**Karl** · 13:48
I have some already

**Claude** · 13:49
No. The PVC isn't there for strength, it's there for thickness. It turns the skin into a small sandwich that spreads your heel over enough area for 20 kg/m³ foam to carry it. A cloth layer, carbon or aramid, is 0.25 mm thick and spreads nothing.

The numbers, per metre of panel width:
- Two cloth layers straight on EPS: local stiffness about 0.6 N·m. One carbon layer over 3 mm PVC with the inner glass: about 60 N·m. A hundred times stiffer for 0.54 kg/m² instead of 0.38.
- A heel is 100 kg on roughly 30 cm², which is 0.33 MPa. EPS 20 yields at about 0.09 MPa, so the skin has to spread the load over four times the heel area or the core crushes and the dent is permanent. That is why boards without a sandwich use 30 kg/m³ cores and still dent.
- Matching the sandwich with cloth alone takes about five layers of 200 g: 1.9 kg/m², three and a half times the weight, and aramid's lower modulus makes it worse at this than carbon.

The aramid earns its place after the dent, by keeping the skin in one piece, so it belongs on top of the PVC, not instead of it.

If PVC turns out hard to buy, the real substitute is 1.5 to 2 mm paulownia veneer (compsand construction): easy to find in France, about twice the weight of the PVC, and bagged in two stages to take the deck crown. Noted in [layup-spec.md](../board-design/layup-spec.md#can-the-carbon-aramid-replace-the-pvc-2026-10-15).

**Claude** · 13:49
Good, then use it where it does a job rather than where the PVC does one. Three places it can go, in order of value:
1. The stance patch, 900 × 500 mm, as already specified.
2. The two bottom track patches, 450 × 350 mm each. Hybrid works there; the box block carries the load and the patch just ties it into the skin.
3. The inner skin under the deck PVC in place of the 100 g glass, if you have enough. That costs about 0.1 kg over glass but means one less thing to buy.

How much do you have, width and length? That decides whether 3 is on, and I'll fix the BOM to match.

**Karl** · 15:34
compare our design to that of the KT Drifter 5 Carbon Pro

**Claude** · 15:34
Looking up the KT Drifter 5 Carbon Pro specs now, then comparing them against our design.

**Claude** · 15:36
Headline: the Drifter 5 is KT's all-round wing freeride board (width and stability underfoot), not their downwind board (that is the Ginxu). Against the nearest size, the 115 L, ours is a different trade:

- **Shape.** 200 × 56 cm against 190.5 × 70.5 cm. Ours is 20% narrower with a length-to-width of 3.6 against 2.7, so less wetted width and lower wave drag through the 6 to 8 kt take-off band. KT buys stability at rest and foil control with width instead; their own chart puts 100 kg at the top of the 115 L range, and the [surf-magazin test](https://www.surf-magazin.de/en/wingsurfing/wing-boards/wingboards-2026-easy-freerider-the-kt-drifter-5-carbon-put-to-the-test/) found take-off slightly behind a slimmer mid-length and stability ahead.
- **Bottom.** Their tri-plane chines and "defined tail chines" are the same idea as our bevel chines and hard aft edges. They add a subtle double concave for soft touchdowns; we got that from the soft-V nose and kept the pump zone flat.
- **Weight.** Listed 6.6 kg, but the 100 L Carbon listed at 6.2 kg weighed 7.0 kg on test, so a real Pro 115 is likely 6.7 to 6.9. Our 6.8 kg budget with pad is parity per litre.
- **Construction.** Both sandwich-type: their fused high-density shell against our PVC; biaxial carbon and UD patches against twill and aramid. Our rails are tougher, their deck lighter.
- **Price.** [2060 to 2230 €](https://hoenalu.com/en/product/kt/drifter-5-pro-carbon) against roughly 750 € in materials.
- **Worth copying:** their 14 inch tracks. With two foils of different area our 10 inch track leaves little trim range. Going to 14 inch means a 420 mm block and tracks from 580 to 940 mm, about 0.1 kg.

Full table in [design-spec.md](../board-design/design-spec.md#comparison-with-the-kt-drifter-5-pro-carbon-2026-10-15). One word: **14** (recommended) to switch the tracks, or **10** to keep them.

**Karl** · 2026-10-16 13:47
switch the tracks and create a Bill of Materials needed

**Karl** · 13:50
continue

**Claude** · 13:50
Switching to 14 inch tracks in the model and templates now, then building the full bill of materials as a spreadsheet.

**Claude** · 13:55
Both are done. The bill of materials is in [bill-of-materials.xlsx](../board-design/bill-of-materials.xlsx) and comes to **about 1000 €** including consumables, plus a shipping allowance you can edit.

**Tracks**
- The tracks are now 14 inch (356 mm), running from 582 to 938 mm from the tail on the same 760 mm centre.
- The high-density block is 150 × 420 mm, from 550 to 970 mm. Its outline is drawn on the [templates](../board-design/templates_A4.pdf).
- I need to correct myself: the switch costs **0.3 kg**, not 0.1. The longer block and heavier boxes bring the budget to **7.1 kg** ready to ride, or 6.7 without the pad.

**Buying the tracks**
- 14 inch boxes are hard to find for DIY.
- My first pick is [O'Karbon's 14 inch carbon tracks](https://www.okarbon.eu/product/foil-tracks/). They list no price, so ask for a quote.
- The fallback is [Foil-Tec's 400 mm tracks](https://foil-tec.com/en-us/collections/foil-tracks-boxes-and-inserts) at USD 29.99 each, shipped from Australia.
- Either way, check that your Armstrong and F-One plates fit before ordering.

**About the spreadsheet**
- Only the PVC price is checked on a live supplier page, at 157 € for an R&G box of 5. All the other prices are typical EU retail estimates, and each line says which kind it is. Quantities and prices are editable and the totals update.
- The carbon-aramid is listed as on hand at no cost.
- Separate tabs cover a tools check and the weight budget. The tools check flags the vacuum regulator, the router and 1 g scales.
- While building it I found two quantity errors in the step 2 list. A 560 mm panel can't be cut twice from 1000 mm cloth, so the glass goes from 2.5 m to 4.2 m and the carbon from 4.0 m to 4.2 m. [layup-spec.md](../board-design/layup-spec.md) is corrected.

Still open from yesterday: how much carbon-aramid do you have (width × length)? If it's at least 1 × 2.5 m, it can also replace the deck inner glass.

**Karl** · 2026-10-18 11:28
please commit this thread and all of the documents to the repository https://github.com/KGS-Real2fa/wingfoil
