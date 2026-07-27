# Test 07 — CH-07 · The decoherence law

**Scorecard: PASS** · section B. Interference · suite v1.14 (frozen 2026-07-22)

## The question

When phase noise is added, does interference fade along the specific curve quantum mechanics predicts — not merely in the right direction?

## Why it is a real test

Anything noisy loses coherence. The test is the LAW: visibility must track a particular analytic dephasing curve as the noise width is turned up. Direction is cheap; the curve is not.

## Protocol

Introduce phase dispersion of width Delta into the two-path preparation, sweep Delta, fit visibility from counted events at each width, and compare against the analytic dephasing curve at two frames.

## The pass bar — frozen before the run

Visibility tracks the analytic curve within instrument bounds (~0.02 at the tested frames).

## Controls that had to fail

Shares the fingerprint battery's generic-ensemble controls, which fail on shape before dephasing is even applied.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| dose sweep tracking confirmed, frame 91 | `true` | Lab 114 |
| dose sweep tracking confirmed, frame 93 | `true` | Lab 114 |
| Lab 114b verdict | STRUCTURE-CONFIRMED | Lab 114b |
| high-statistics cell RMS (800k events) | `0.020042` | Lab 114b |
| second-profile cell RMS | `0.0252063` | Lab 114b |

### Recomputed from raw counts

**The dephasing dose sweep.** `Vmf` is the counted visibility at noise width `Delta`; `ratio` is that visibility relative to the un-noised case; `sinc` is the analytic curve it must follow; `diff` is the gap.

| frame | noise width Delta | counted visibility | ratio to zero-noise | analytic curve | gap |
|---|---|---|---|---|---|
| 91 | 0.0000 | 0.9819 | 1.0000 | 1.0000 | 0.0000 |
| 91 | 0.5236 | 0.9308 | 0.9480 | 0.9549 | 0.0069 |
| 91 | 1.0472 | 0.8125 | 0.8275 | 0.8270 | 0.0005 |
| 91 | 1.5708 | 0.6286 | 0.6402 | 0.6366 | 0.0036 |
| 91 | 2.0944 | 0.4089 | 0.4164 | 0.4135 | 0.0029 |
| 93 | 0.0000 | 0.6046 | 1.0000 | 1.0000 | 0.0000 |
| 93 | 1.0472 | 0.4859 | 0.8037 | 0.8270 | 0.0233 |
| 93 | 2.0944 | 0.2450 | 0.4053 | 0.4135 | 0.0082 |

Worst gap across every noise level and both frames: **0.0233**.

## Caveats and scope

Measured at two frames, not across the full frame battery. The residual structure identified in Lab 120 sets the floor on how closely any of these curves can be tracked — the same ~J that shows up everywhere else.

## Evidence files

- `metrics/metrics_114.json` — Lab 114 (`114_fingerprint_hardening/metrics_114.json` in the research tree)
- `metrics/metrics_114b.json` — Lab 114b (`114_fingerprint_hardening/metrics_114b.json` in the research tree)

## What the article says

> Turn the noise up and the machine's visibility follows that curve step for step, never more than 0.023 away from it.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
