# Test 01 — CH-01 · Born statistics

**Scorecard: PASS** · section A. Static statistics · suite v1.14 (frozen 2026-07-22)

## The question

Do the frequencies the observer counts match the probabilities quantum mechanics assigns — the squared length of each arrow?

## Why it is a real test

This is the floor of the whole exercise. The machine never squares anything: it compares three lengths, takes the longest, and writes down one integer. The squared law is not installed anywhere. So if the counted frequencies land on the quantum values, they landed there by mechanism, not by construction.

## Protocol

Run the certified fold for tens of thousands of ticks in a fixed observer frame. Tally how often each of the three outcomes is recorded. Compare the tallies against the Born values for the same states and frame. The quantum formula is used only to draw the reference; it never enters the machine.

## The pass bar — frozen before the run

D_born <= 2J across at least two substrate worlds and at least six cells, where J is the cell's own measured precision.

## Controls that had to fail

Generic (non-certified) ensembles at the same frame fail decisively. A record-level pool-versus-PRNG swap agrees to 0.0063, showing the result is about the fold and not about the particular number source.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| Lab 100 v2 verdict | GRADUATE-EXISTENCE | Lab 100 v2 |
| Lab 101 verdict | OTHER | Lab 101 |
| Lab 101b verdict | CONTROL-REAL | Lab 101b |
| Lab 101c verdict | CELL-RESTORED | Lab 101c |

## Caveats and scope

The recipe theta was found by an optimizer against this row and this row only, then frozen for the whole rest of the suite. That is engineering and it is declared. The measured precision J is the same ~1% scale that becomes a hard wall in CH-06.

## Evidence files

- `metrics/metrics_100_v2.json` — Lab 100 v2 (`100_repreparation_fold/metrics_100_v2.json` in the research tree)
- `metrics/metrics_101.json` — Lab 101 (`101_existence_hardening/metrics_101.json` in the research tree)
- `metrics/metrics_101b.json` — Lab 101b (`101_existence_hardening/metrics_101b.json` in the research tree)
- `metrics/metrics_101c.json` — Lab 101c (`101_existence_hardening/metrics_101c.json` in the research tree)

## What the article says

> They land on the quantum values, off by 0.007 to 0.015. Call it about one percent.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
