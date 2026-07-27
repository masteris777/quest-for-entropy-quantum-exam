# Test 05 — CH-05 · Cosine fringes with first-harmonic purity

**Scorecard: PASS** · section B. Interference · suite v1.14 (frozen 2026-07-22)

## The question

When the machine is pointed at a two-path setup and the phase is swept, do the counted events trace the quantum interference curve — and only that curve?

## Why it is a real test

Lots of mechanisms wiggle. Very few wiggle as a pure first harmonic with the right amplitude. Purity is the part that is hard to fake: overtones are the fingerprint of a construction that is imitating the shape rather than producing it.

## Protocol

Sweep the two-path phase over a 24-point grid, count outcomes at each phase, fit the first harmonic, and compare both the fitted curve and its overtone content against the analytic Born curves. Repeated across frames, two target-weight profiles, and a second world.

## The pass bar — frozen before the run

RMS <= 0.05 against the Born curves; no overtone content above the residual.

## Controls that had to fail

Generic ensembles at the same frames produce RMS 0.287 and 0.315 — an order of magnitude worse — and, tellingly, produce EXACT hard nulls where the certified ensemble does not. That control failure is the seed of CH-06.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| Lab 113 verdict | FINGERPRINT-CARRIED | Lab 113 |
| Lab 114 verdict | PARTIAL-HARDENED | Lab 114 |
| Lab 114 verdict reason | >=5/6 pass or CELL-BLOCKED, cells 1-4 pass, controls separate, tracking@91 confirmed. 1 valid engineered cell(s) failed their bars | Lab 114 |
| RMS, cell 91-asym | `0.0149914` | Lab 114 |
| RMS, cell 91-sym | `0.0155698` | Lab 114 |
| RMS, cell 93-asym | `0.0307054` | Lab 114 |
| RMS, cell 201-asym | `0.0152128` | Lab 114 |
| RMS, cell 91-P2-asym | `0.0204295` | Lab 114 |
| RMS, cell 11-asym-W2 (second world) | `0.0473347` | Lab 114 |
| generic control RMS, C1 | `0.287465` | Lab 114 |
| generic control RMS, C2 | `0.314514` | Lab 114 |

## Caveats and scope

One of six hardened cells missed its bar (the lab verdict is PARTIAL-HARDENED, not a clean sweep) and the per-cell RMS reaches 0.047 in the second world. The article's stated range is the honest full range across cells, not the best one.

## Evidence files

- `metrics/metrics_113.json` — Lab 113 (`113_engineered_ensemble_twoslit/metrics_113.json` in the research tree)
- `metrics/metrics_114.json` — Lab 114 (`114_fingerprint_hardening/metrics_114.json` in the research tree)
- `metrics/metrics_114b.json` — Lab 114b (`114_fingerprint_hardening/metrics_114b.json` in the research tree)

## What the article says

> The counts trace a cosine — the real interference curve, RMS 0.015 to 0.047 away from the quantum one.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
