# Test 12 — CH-11 · Delayed choice

**Scorecard: PASS** · section C. Measurement dynamics · suite v1.14 (frozen 2026-07-22)

## The question

Does the fate of the interference pattern depend on WHETHER a which-path fold happens, and never on WHEN it happens?

## Why it is a real test

Wheeler's question. If the fringes depended on the timing of the choice, something in the construction would be reaching backwards along the trajectory — and a deterministic machine that needs retrocausality to imitate quantum mechanics has not explained anything.

## How this is set up in the toy

The two-path setup of test 05 plus the marker of test 08, with a flight time. The state is given a flight of 64 ticks between preparation and readout, and the which-path fold is inserted at t_d = 0, 16, 32, 48 or 63 ticks into that flight — from before it begins to the last tick before it ends. Everything else is held identical. The only thing that varies is WHEN the marking happens.

*(One-page overview of the apparatus, and what is deliberately not modelled: [`../setup.md`](../setup.md).)*

## Protocol

Fix a flight time of 64 ticks. Insert the which-path fold at t_d = 0, 16, 32, 48 and 63 — from before the flight begins to the last tick before it ends. Sweep the interference phase at each insertion time and fit visibility.

## The pass bar — frozen before the run

V(t_d) independent of insertion time to within 3x counting noise. Kill the row if the spread exceeds that.

## Controls that had to fail

The unmarked arm gives V0 = 0.989: the fringes are fully there when nothing folds. The kill bars sit near 0.35 — two orders above the measured values.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| unmarked visibility V0 (Lab 146) | `0.98911` | Lab 146 |
| V by insertion time, frame 91 | `0 = 0.00459918; 16 = 0.00383392; 32 = 0.00464518; 48 = 0.00333888; 63 = 0.00506784` | Lab 146 |
| V by insertion time, frame 93 | `0 = 0.00234056; 16 = 0.00340397; 32 = 0.004347; 48 = 0.0020479; 63 = 0.00176522` | Lab 146 |
| kill 1 triggered | `false` | Lab 146 |
| kill 2 triggered | `false` | Lab 146 |
| fresh-cell V by t_d (Lab 156) | `301 = {'0': 0.005215630481931601, '16': 0.006045057527922897, '32': 0.0056147514407875665, '48': 0.00225177700704711, '63': 0.007567110276397726}; 303 = {'0': 0.0019124857397742805, '16': 0.002262528348741209, '32': 0.002523764507417231, '48': 0.0028643005535179135, '63': 0.0021575281531388915}` | Lab 156 |
| fresh-cell spread | `301 = 0.00531533; 303 = 0.000951815` | Lab 156 |
| fresh-cell kills | `301 = [False, False]; 303 = [False, False]` | Lab 156 |
| Lab 156 row verdict | PASS | Lab 156 |

## Caveats and scope

Tested over one flight window with five insertion points, not a continuum. 'Independent of when' is measured, not proved.

## Evidence files

- `metrics/metrics_146.json` — Lab 146 (`146_delayed_choice_fold_timing/metrics_146.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> Every marked run gave visibility 0.0076 or below, against a kill bar of 0.35 — flat, no dependence on timing at all.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
