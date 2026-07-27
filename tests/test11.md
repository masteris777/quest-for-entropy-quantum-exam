# Test 11 — CH-10 · Post-measurement blurring

**Scorecard: PASS** · section C. Measurement dynamics · suite v1.14 (frozen 2026-07-22)

## The question

After a measurement the answer is sharp. If the observer waits without measuring, does the sharpness decay along the curve the evolved state predicts — dip and partial revival included?

## Why it is a real test

A construction can freeze a value and look repeatable. The test that separates freezing from evolving is what happens when you WAIT. The revival is the part that cannot be faked by damping: the certainty comes partly back.

## Protocol

Fold, then evolve the state under the substrate turn alone for Delta ticks without folding, then fold again and record whether the outcome matches. Sweep Delta. Compare against r_free(Delta), the analytic curve for the freely evolved state. Re-run under two coprime schedule offsets (7 and 11) to rule out sampling artifacts.

## The pass bar — frozen before the run

P(same outcome vs Delta) tracks r_free(Delta) within 5J.

## Controls that had to fail

The composition control — repeated measurement instead of free evolution, the Zeno chain — separates from the data by up to 0.348. That is the control that says the machine is evolving, not freezing.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| RMS vs r_free, per cell and offset | `W1|301|off7 = 0.015089; W1|301|off11 = 0.0141492; W1|303|off7 = 0.0179157; W1|303|off11 = 0.0179146; W2|17|off7 = 0.0146313; W2|17|off11 = 0.0145982` | Lab 156 |
| bar (5J) per cell | `W1|301|off7 = 0.0510837; W1|301|off11 = 0.0510837; W1|303|off7 = 0.0642959; W1|303|off11 = 0.0642959; W2|17|off7 = 0.0342495; W2|17|off11 = 0.0342495` | Lab 156 |
| RMS vs the Zeno composition control | `W1|301|off7 = 0.182004; W1|301|off11 = 0.189271; W1|303|off7 = 0.117112; W1|303|off11 = 0.120079; W2|17|off7 = 0.148026; W2|17|off11 = 0.147041` | Lab 156 |
| max separation between the two references | `0.347792` | Lab 156 |
| schedule offsets used (coprime) | `7, 11` | Lab 156 |
| scout RMS vs analytic (Lab 148 run 2) | `0.0103472` | Lab 148 run 2 |
| scout RMS vs composition control | `0.174573` | Lab 148 run 2 |
| Lab 156 row verdict | PASS | Lab 156 |

## Caveats and scope

Run 1 of this lab was VOIDED, not failed: it compared against the wrong reference curve. See ledger #33 and `ledger.md`. The numbers here are from the corrected run and its fresh-cell hardening.

## Evidence files

- `metrics/metrics_148_run2.json` — Lab 148 run 2 (`148_measurement_persistence/metrics_148_run2.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> The machine follows that curve, revival included. The control that fakes it by measuring repeatedly instead separates by up to 0.28.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
