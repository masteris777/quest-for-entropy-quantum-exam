# Test 13 — CH-12 · Interaction-free (null-result) collapse

**Scorecard: PASS** · section C. Measurement dynamics · suite v1.14 (frozen 2026-07-22)

## The question

If a detector is present on one path but never fires, do the fringes still die?

## Why it is a real test

Elitzur and Vaidman's bomb tester. This is the strangest row on the paper: information gained by NOT seeing something still costs the interference. A construction where 'nothing happened' means 'nothing changed' fails here immediately.

## Protocol

Place the which-path fold on one arm. Keep only the runs in which it did not register. Sweep the interference phase on that null-conditioned subensemble and fit visibility. Also compare the null-conditioned screen profile against the single-path profile it should now match.

## The pass bar — frozen before the run

Null-conditioned screen counts fringe-free at the floor; profile consistent with the single-path shape.

## Controls that had to fail

Stage D probes the reservoir directly for any leakage signal: delta/noise 0.30, i.e. quiet.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| null-conditioned visibility (Lab 146) | `0.00580056` | Lab 146 |
| RMS vs single-path profile (Lab 146) | `0.0080369` | Lab 146 |
| kill triggered (Lab 146) | `false` | Lab 146 |
| reservoir probe delta/noise (Lab 146 stage D) | `0.299704` | Lab 146 |
| transferred-recipe V_null (Lab 156, R6) | `301 = 0.0064554; 303 = 0.00726224` | Lab 156 |
| transferred-recipe profile deviation (Lab 156, R6) | `301 = 0.0480244; 303 = 0.0284165` | Lab 156 |
| Lab 156 row verdict (transferred recipe) | FAIL | Lab 156 |
| Lab 156b verdict (native recipe) | PASS | Lab 156b |
| Lab 156b verdict reason | B holds both frames (J_native 301=0.00247, 303=0.01368 <= 0.03; iso control 225x worse) AND C holds both frames (V_null 0.01968/0.00870 vs bars 0.02695/0.02672; profile max_dev 0.00583/0.01542 vs bars 0.02695/0.02672). | Lab 156b |

## Caveats and scope

This row is the one that exposed ledger #37. On fresh frames with the recipe TRANSFERRED rather than re-fitted, the profile half MISSED (max deviation 0.048 and 0.028 against a bar of 0.027) and Lab 156 recorded R6 as FAIL. Re-fitting the recipe natively for the new frames (Lab 156b) repaired it to 0.0058 and 0.0154. Both the failure and the repair are below. The size of the miss matched a transfer penalty measured independently in the same battery.

## Evidence files

- `metrics/metrics_146.json` — Lab 146 (`146_delayed_choice_fold_timing/metrics_146.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)
- `metrics/metrics_156b.json` — Lab 156b (`156_conformance_hardening/metrics_156b.json` in the research tree)

## What the article says

> The machine does this: fringe visibility on the non-firing runs sits at 0.0058, flat at the floor.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
