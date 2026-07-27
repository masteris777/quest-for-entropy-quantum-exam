# Test 19 — CH-18 · The observer's view is forced to be complex-unitary

**Scorecard: PASS (theorem, machine-checked)** · section E. Structural theorems · suite v1.14 (frozen 2026-07-22)

## The question

Given a real, information-preserving view of a steadily turning world with no standing still, is a complex-unitary description forced — or merely convenient?

## Why it is a real test

Every physics student asks why quantum mechanics needs imaginary numbers. This is a partial answer for this class of observer: it is not a modelling choice.

## Protocol

Not an experiment. Six exact symbolic lemmas, machine-checked, no floating point in the proof stage: a real orthogonal operator on R^(2n) with no real eigenvalues decomposes into n mutually orthogonal invariant rotation planes; the blockwise quarter-turn J satisfies J^2 = -I and commutes with the operator; an odd-dimensional real eigenspace obstructs any such J by determinant parity.

## The pass bar — frozen before the run

Every proof step machine-checked or a named standard argument. No untagged steps.

## Controls that had to fail

Stage C re-runs the earlier empirical lab that motivated the theorem and confirms the theorem's predictions on it.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| lemma L1 checked | `true` | Lab 116 |
| lemma L2 checked | `true` | Lab 116 |
| lemma L3 checked | `true` | Lab 116 |
| lemma L4 checked | `true` | Lab 116 |
| lemma L5 checked | `true` | Lab 116 |
| lemma L6 checked | `true` | Lab 116 |
| no numeric pass used in the proof stage | `false` | Lab 116 |
| verdict | PASS | Lab 116 |
| verdict reason | All six lemmas machine-checked exactly (symbolic/exact, no floats); the write-up has no untagged step; Stage C regressions against Lab 88's stored checks agree. | Lab 116 |

## Caveats and scope

Scope note recorded at review: for pairwise-DISTINCT rotation angles J is unique up to per-plane orientation, but REPEATED angles admit plane-mixing complex structures. An exact counterexample is on record. Also — and this matters — this theorem is about a real, information-preserving dashboard of a turning world. It is a DIFFERENT OBJECT from the machine's three-number state, which is written complex by hand in the source. The theorem is not applied to the machine and the article does not lean on it.

## Evidence files

- `metrics/metrics_116.json` — Lab 116 (`116_schur_close/metrics_116.json` in the research tree)

## What the article says

> the structure of that view *forces* a complex-unitary description. Not chosen for convenience. Forced by the geometry.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
