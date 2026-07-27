# Test 04 — CH-04 · Mixture affinity and the superposition gap

**Scorecard: PASS** · section A. Static statistics · suite v1.14 (frozen 2026-07-22)

## The question

Does a coin-flip mixture of two setups give the plain average of their statistics — and does a coherent combination instead give the average plus a specific extra term?

## Why it is a real test

This is the difference between 'don't know which' and 'both at once'. A classical machine can fake the first easily. Getting the second one right, at the size the theory pins down, is the harder half.

## Protocol

Prepare two component ensembles A and B. Stage B2: blend them with probability p using an independent selector channel, count, and compare against p*F_A + (1-p)*F_B. Stage B3: prepare the coherent combination instead and measure the departure from the mixture prediction.

## The pass bar — frozen before the run

Affine on mixtures at O(J^2); coherent gap equal to the analytic cross-term at O(J).

## Controls that had to fail

A generic ensemble at the same frame gives RMS 0.222 against the certified 0.017.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| verdict (lab) | OTHER | Lab 118 |
| verdict reason | No ladder rule matched exactly: B1=False, B2=True, B3=True, control_fails=True. | Lab 118 |
| B2 max residual, p=0.25 | `0.00084` | Lab 118 |
| B2 max residual, p=0.50 | `0.002075` | Lab 118 |
| B2 max residual, p=0.75 | `0.00130625` | Lab 118 |
| B2 bar | `0.04` | Lab 118 |
| B1 max residual, p=0.25 (tighter bar) | `0.00283125` | Lab 118 |
| B1 bar (counting-noise scaled) | `0.00228` | Lab 118 |
| B1 pass | `false` | Lab 118 |
| B3 coherent-gap RMS, frame 91 | `0.0172621` | Lab 118 |
| B3 coherent-gap RMS, frame 93 | `0.0268801` | Lab 118 |
| B3 generic control RMS | `0.222223` | Lab 118 |

## Caveats and scope

Honest detail the article does not have room for: the lab ran the affinity check at TWO tightnesses. At the pre-declared bar (stage B2, bar 0.04) it passes with room to spare. At a second, much tighter bar scaled to raw counting noise (stage B1, bar 0.00228) the largest residual is 0.00283 — a marginal miss at the counting floor. The lab's own verdict field is therefore 'OTHER' rather than 'PASS', and the suite grades the row on the pre-declared bar. Both numbers are below, decide for yourself.

## Evidence files

- `metrics/metrics_118.json` — Lab 118 (`118_mixture_affinity/metrics_118.json` in the research tree)

## What the article says

> flat on the coin flip to 0.002, and the extra term shows up at the predicted size

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
