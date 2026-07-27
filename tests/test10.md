# Test 10 — CH-09b · The one-step collapse chain

**Scorecard: PASS** · section C. Measurement dynamics · suite v1.14 (frozen 2026-07-22)

## The question

Between two consecutive measurements, does the full table of transition frequencies — every entry, off-diagonals included — match the quantum chain?

## Why it is a real test

Repeatability is a single number and a lucky construction could hit it. The transition table is nine numbers at once, and it is what the collapse postulate plus unitary evolution actually predicts. This is the strongest measurement-dynamics row on the paper.

## Protocol

Fold, let the substrate take one turn, fold again. Count M(k|j), the frequency of recording k given that j was recorded one step earlier, for all nine (j,k) pairs. Compare entry by entry against the quantum chain. Repeat at lag 3 and lag 10 to check that the chain composes.

## The pass bar — frozen before the run

Max entry difference of order J, encoded before the run as 5J per cell (the encoding is declared in the script header, not chosen afterwards).

## Controls that had to fail

An isotropic control reaches max entry difference 0.555 — two orders worse. A matched quantum-mechanical reference run through the identical counting pipeline scores 0.003-0.004, which sets the honest noise floor for this instrument.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| max entry difference per cell | `W1|301 = 0.0412685; W1|303 = 0.0577557; W2|17 = 0.00595709` | Lab 156 |
| bar (5J) per cell | `W1|301 = 0.0510837; W1|303 = 0.0642959; W2|17 = 0.0342495` | Lab 156 |
| matched-QM reference on the same instrument | `W1|301 = 0.00323981; W1|303 = 0.00437716; W2|17 = 0.0044495` | Lab 156 |
| isotropic control max difference | `0.554539` | Lab 156 |
| bar encoding, declared | suite 'O(J)' encoded as 5J (declared, header) | Lab 156 |
| Lab 156 row verdict | PASS | Lab 156 |

## Caveats and scope

The worst entry is NOT 0.0060 everywhere: that is the second world's figure. In the first world the toughest cell reaches 0.0578 against its own 5J bar of 0.0643. Every cell is inside its bar; no cell is at the quantum reference's own noise level. Both numbers are in the table below.

## Evidence files

- `metrics/metrics_148_run2.json` — Lab 148 run 2 (`148_measurement_persistence/metrics_148_run2.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> in every cell the worst entry stayed inside the bar we had set beforehand, and in the fresh second world the worst entry was off by 0.0060

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
