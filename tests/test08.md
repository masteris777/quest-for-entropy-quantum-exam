# Test 08 — CH-08 · The which-path sum rule

**Scorecard: PASS** · section B. Interference · suite v1.14 (frozen 2026-07-22)

## The question

If the path is marked, does interference vanish completely — leaving the plain sum of the two paths with no cross term?

## Why it is a real test

This is the observer effect in its most testable form, and it is the row the browser demo shows live. Partial marking must partially kill the fringes; full marking must kill them entirely.

## How this is set up in the toy

Same two-path setup as test 05, plus a detector. **The 'which-path detector' is a two-level marker system** carried alongside the state. Marking is a controlled rotation R(g) applied to the marker, conditioned on the path component of the state — g is the coupling dial, and g = pi/2 is total marking. The marker is then measured by its own certified two-outcome fold (the same fold machinery, built and certified for dimension 2 in its own lab, because the three-outcome one does not apply). Visibility V is fitted from the counted fringes; distinguishability D is how well the marker's record identifies the path.

*(One-page overview of the apparatus, and what is deliberately not modelled: [`../setup.md`](../setup.md).)*

## Protocol

Couple a marker to the path degree of freedom with strength g, run the interference sweep, and measure both the fringe visibility V and the path distinguishability D at each g. At g = pi/2 the marking is total.

## The pass bar — frozen before the run

Fringe visibility at the residual floor when the path is fully marked.

## Controls that had to fail

The uncertified 'bare argmax' marker from the first attempt is re-run as a control and reproduces the exact broken corner that voided the earlier run — a control that certifies the instrument, not just the result.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| V at zero marking (Lab 147) | `0.955196` | Lab 147 |
| V at full marking (Lab 147) | `0.00197695` | Lab 147 |
| D at full marking (Lab 147) | `1` | Lab 147 |
| V at full marking, fresh cells (Lab 156) | `0.00127103` | Lab 156 |
| D at full marking, fresh cells (Lab 156) | `1` | Lab 156 |
| uncertified-marker control reproduces the broken corner | `true` | Lab 156 |
| Lab 156 row verdict | PASS | Lab 156 |

## Caveats and scope

The measured V at full marking is not zero but at the residual floor, which is the same ~1% that limits every other row.

## Evidence files

- `metrics/metrics_147.json` — Lab 147 (`147_whichpath_marker_eraser/metrics_147.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> With full marking the machine's fringe visibility falls to 0.0020 while the path information reads 1.0000.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
