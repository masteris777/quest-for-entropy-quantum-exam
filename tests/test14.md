# Test 14 — CH-13 · The quantum eraser

**Scorecard: PASS** · section C. Measurement dynamics · suite v1.14 (frozen 2026-07-22)

## The question

Mark the path so the fringes die, then erase the marker and sort the records by what the erased marker said. Do the fringes come back in each pile, out of step with each other, cancelling when pooled?

## Why it is a real test

The eraser is the experiment people reach for when they want to claim retrocausality. It is nothing of the sort, and a mechanism that reproduces it makes that visible: nothing is un-measured, the records are just reorganised.

## How this is set up in the toy

The setup of test 08, plus erasure. After the marker has been coupled at full strength, an erasing rotation is applied and the marker is folded **in the conjugate basis** — which destroys the which-path information and produces a fresh binary label that is correlated with the phase rather than the path. Runs are then sorted into two piles by that label and the fringes are fitted in each pile separately, and in the two pooled together.

*(One-page overview of the apparatus, and what is deliberately not modelled: [`../setup.md`](../setup.md).)*

## Protocol

Couple the marker at full strength, then apply the erasing rotation and fold the marker in the conjugate basis. Split the runs by erased-marker outcome. Sweep the interference phase and fit visibility separately in each subensemble, then in the pooled data.

## The pass bar — frozen before the run

Subensemble V >= 0.5 * V_0, the two at opposite phases; pooled V at the floor.

## Controls that had to fail

The pooled data is its own control: if the fringes were real rather than subselected, pooling would not cancel them. It cancels to 0.0002.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| subensemble V, plus branch (Lab 154 shown in figure) | `0.9528` | Lab 156 |
| subensemble V, minus branch | `0.955255` | Lab 156 |
| recovery bar | `0.476739` | Lab 156 |
| phase gap between the branches | `3.13888` | Lab 156 |
| pooled visibility | `0.00101765` | Lab 156 |
| pooled bar | `0.0212132` | Lab 156 |
| subensemble split | `0.499975` | Lab 156 |
| Lab 154 verdict | PARTIAL | Lab 154 |
| Lab 156 row verdict | PASS | Lab 156 |

## Caveats and scope

The article quotes Lab 154's numbers because that is the run plotted in the figure. The fresh-seed hardening (Lab 156) gives slightly different values — split 0.49998, phase gap pi - 0.0027, pooled 0.0010 — and both are below. Earlier attempts at this row (Labs 147, 152) FAILED on an uncertified marker instrument; see ledger #34/#35. One more thing that looks odd until you know why: Lab 154's own overall verdict field reads PARTIAL. That is not about the eraser. The same lab also carried the CH-14 measurement, which tripped its kill bar at 1.0456 — the estimator error of ledger #36, adjudicated in test15. The eraser half of Lab 154 passed cleanly.

## Evidence files

- `metrics/metrics_154.json` — Lab 154 (`154_eraser_retest_v2/metrics_154.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> The machine splits the records 49.97 to 50.03, brings both piles back at visibility 0.955 and 0.952, and puts them a phase gap of 3.1399 apart.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
