# Test 03 — CH-03 · Non-contextuality at the Gleason hinge

**Scorecard: PASS** · section A. Static statistics · suite v1.14 (frozen 2026-07-22)

## The question

Does the answer to one question stay the same when it is asked alongside different companion questions?

## Why it is a real test

This is the hinge Gleason's theorem turns on. If a direction's probability is allowed to depend on which complete set it is measured in, the theorem has nothing to bite on and the squared law is not forced. Non-contextuality is what makes the geometry rigid.

## Protocol

Fix a direction. Embed it in many different complete measurement contexts (rotations of the complementary pair). Count the frequency of that direction in each context. Report SPREAD = the range of counted values across contexts, per direction.

## The pass bar — frozen before the run

epsilon_nc = O(J) on a predeclared context grid; a generic control at least 5x worse.

## Controls that had to fail

Generic (non-certified) ensembles on the identical context grid.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| verdict | HINGE-HOLDS | Lab 115 |
| verdict reason | certified median SPREAD=0.0156<=0.05, max=0.0195<=0.08, generic median=0.1656>=3.0x certified median. | Lab 115 |
| certified SPREAD, direction d1 | `0.016555` | Lab 115 |
| certified SPREAD, direction d2 | `0.010355` | Lab 115 |
| certified SPREAD, direction d3 | `0.019485` | Lab 115 |
| certified SPREAD, direction d4 | `0.01455` | Lab 115 |
| context-free check, max diff (d1) | `0` | Lab 115 |

## Caveats and scope

The spread is at the scale of J, not zero. Non-contextuality here is approximate at the machine's own precision, which is exactly what 'O(J)' means and exactly why the residual matters elsewhere.

## Evidence files

- `metrics/metrics_115.json` — Lab 115 (`115_contextuality_meter/metrics_115.json` in the research tree)

## What the article says

> We asked the same question inside many different groupings and measured the drift: 0.0156, at the machine's own one percent. The scrambled control drifted 10.6 times worse.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
