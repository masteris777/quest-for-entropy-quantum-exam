# Test 15 — CH-14 · The visibility-distinguishability trade-off

**Scorecard: PASS** · section C. Measurement dynamics · suite v1.14 (frozen 2026-07-22)

## The question

Can path knowledge and fringe visibility both be high? Quantum mechanics says no: squared and added they must not exceed 1.

## Why it is a real test

Englert's relation is a bound, not a fit — and the interesting thing is not obeying it but SATURATING it. A sloppy construction sits safely underneath; quantum mechanics rides the edge. This row is also where this campaign came closest to publishing something false.

## Protocol

Sweep the marker coupling g from 0 to pi/2. At each g measure fringe visibility V from counted events, and measure D as Englert's OPERATIONAL distinguishability: the difference in flip probability between single-branch calibration ensembles pushed through the identical coupling and marker fold. Compute V^2 + D^2 at each g.

## The pass bar — frozen before the run

Counted V^2 + D^2 <= 1 + O(J), traced monotonically in g.

## Controls that had to fail

Calibration arm A must never flip (measured: 0.0 at every g) and arm B must flip with certainty at full coupling (measured: 1.0). A matched Born-coin replay reproduces the same D curve, confirming the estimator now computes the quantity the physics defines.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| V^2 + D^2 by coupling | `0 = 0.909087; pi/8 = 0.725593; pi/4 = 0.575797; 3pi/8 = 0.811542; pi/2 = 1` | Lab 155 |
| max V^2 + D^2 | `1` | Lab 155 |
| kill bar | `1.03065` | Lab 155 |
| operational D by coupling | `0 = 0; pi/8 = 0.15315; pi/4 = 0.50025; 3pi/8 = 0.8471; pi/2 = 1` | Lab 155 |
| analytic D reference | `0 = 0; pi/8 = 0.146447; pi/4 = 0.5; 3pi/8 = 0.853553; pi/2 = 1` | Lab 155 |
| calibration arm A flip probability | `0 = 0; pi/8 = 0; pi/4 = 0; 3pi/8 = 0; pi/2 = 0` | Lab 155 |
| calibration arm B flip at full coupling | `1` | Lab 155 |
| fresh-cell max V^2 + D^2 (Lab 156) | `1` | Lab 156 |
| matched Born-coin replay D (Lab 156) | `0 = 0; pi/8 = 0.1473; pi/4 = 0.49925; 3pi/8 = 0.8552; pi/2 = 1` | Lab 156 |
| ledger #36 identity, declared | D_op = |P(flip|B)-P(flip|A)| on single-branch ensembles = Englert's operational D (bar-estimator identity, stated) | Lab 156 |
| Lab 155 verdict | PASS | Lab 155 |

## Caveats and scope

THE NEAR-MISS. The first version of this row came back at 1.015 — over the bound, which would have been a genuine departure from quantum mechanics and the biggest result of the campaign. Before claiming it, a matched quantum-mechanical replay was pushed through the identical scoring code: it scored the same excess (1.0457). The estimator, not the machine, was wrong — post-collapse truth labels do not instantiate Englert's operational quantity. Ledger #36 turned this into a standing rule: a bound is only meaningful if the reference physics scores correctly on the same instrument.

## Evidence files

- `metrics/metrics_155.json` — Lab 155 (`155_englert_operational_d/metrics_155.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> The machine's counted values reach 1.000004 and no further, and it saturates the bound at full coupling.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
