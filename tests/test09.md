# Test 09 — CH-09 · Repeatability

**Scorecard: PASS** · section C. Measurement dynamics · suite v1.14 (frozen 2026-07-22)

## The question

Measure, then measure again immediately. Does the second measurement always return the first answer?

## Why it is a real test

This is the projection postulate — in textbook quantum mechanics it is an AXIOM, written in by hand. Here nothing of the sort is written anywhere. If repeatability appears, it appears as a consequence of the rewrite leaning toward what was just recorded.

## How this is set up in the toy

Same arena as test 01. 'Immediately' is exact and matters: the second measurement happens **before the substrate takes its next turn** — no ticks pass in between. What is compared is the two recorded integers. Note what is not frozen: the second measurement still draws six fresh pool numbers and writes a brand-new state. The answer repeats; the state behind it does not.

*(One-page overview of the apparatus, and what is deliberately not modelled: [`../setup.md`](../setup.md).)*

## Protocol

At each fold, immediately re-fold before the substrate takes its next turn, and compare the two recorded integers. Count matches over the whole run, in three cells spanning two substrate worlds.

## The pass bar — frozen before the run

P(repeat) >= 1 - 3J. Quantum mechanics says certainty; the bar allows slack the machine did not need.

## Controls that had to fail

An isotropic fold (one that does not lean toward the winner) drops repeat certainty to 0.336 — roughly chance for three outcomes. The lean is doing the work.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| counted certainty per cell | `W1|301 = 1; W1|303 = 1; W2|17 = 1` | Lab 156 |
| counts per cell | `W1|301 = 59000/59000; W1|303 = 59000/59000; W2|17 = 59000/59000` | Lab 156 |
| isotropic control certainty | `0.335842` | Lab 156 |
| scout run certainty (Lab 148 run 2) | `1` | Lab 148 run 2 |
| scout events per frame | `59000` | Lab 148 run 2 |
| Lab 156 row verdict | PASS | Lab 156 |

### Recomputed from raw counts

**Recomputed by summing the raw per-cell counts:**

    W1|301     59000/59000
    W1|303     59000/59000
    W2|17      59000/59000
    TOTAL      177000/177000   ratio = 1.000000

## Caveats and scope

Certainty here is exact, not approximate, and that is a structural consequence of the rewrite rather than a statistical near-miss. What is NOT frozen is the state behind the answer: it is rebuilt from six fresh pool numbers every time.

## Evidence files

- `metrics/metrics_148_run2.json` — Lab 148 run 2 (`148_measurement_persistence/metrics_148_run2.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> The machine repeated 177,000 times out of 177,000, across two different worlds. Exactly 1.0.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
