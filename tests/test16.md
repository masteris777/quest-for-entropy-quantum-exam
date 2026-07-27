# Test 16 — CH-15 · No signalling

**Scorecard: PASS** · section D. Two systems at once · suite v1.14 (frozen 2026-07-22)

## The question

Can measuring one system change what a distant system sees, before a signal travelling at the world's own light speed could have arrived?

## Why it is a real test

Any global hidden-variable construction is under immediate suspicion of allowing faster-than-light signalling. If it does, it is dead — not because of Bell, but because of relativity. This row is the survival check.

## Protocol

Intervene on the substrate at a known position and tick. Compare the far observer's record bit by bit against the unintervened run. Compute the light-cone arrival tick for each observer from its distance. Check that the far record is identical before its cone tick, and that the NEAR observer (inside the cone) does diverge — the positive control, which proves the intervention was real.

## The pass bar — frozen before the run

Remote record bit-identical until exact light-cone crossing, on every seed.

## Controls that had to fail

The near-side observer is the positive control: it must diverge, and it must respect its own cone. Both hold on every seed. Lab 138 adds the foliation-invariance gate: the same event identities hold across five different time slicings, 0 mismatches in 56,360 derived events per foliation.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| intervention tick / position | `600` | Lab 143 |
| far observer distance / cone tick | `619` | Lab 143 |
| near observer distance / cone tick | `608` | Lab 143 |
| Lab 143 verdict | GAUGE-INERT | Lab 143 |
| Lab 138 verdict | DOCTRINE-HOLDS | Lab 138 |
| Lab 138 event-identity mismatches, foliation F0 | `0` | Lab 138 |
| Lab 138 derived events checked, foliation F0 | `56360` | Lab 138 |

### Recomputed from raw counts

**Per-seed light-cone check.** Far observer's cone tick = `619`, near observer's = `608`. The far record must be bit-identical before its cone; the near one must diverge (the positive control).

| seed | far record identical pre-cone | far no-signalling | near diverges | near respects own cone | first divergence (far) |
|---|---|---|---|---|---|
| 55100 | True | True | True | True | 640 |
| 55101 | True | True | True | True | 661 |
| 55102 | True | True | True | True | 646 |
| 55103 | True | True | True | True | 694 |

## Caveats and scope

Four seeds, one intervention geometry. The general statement rests on the accompanying theorems, not on this count.

## Evidence files

- `metrics/metrics_138_fate3.json` — Lab 138 (`138_fate_3_foliation_invariance/metrics_138_fate3.json` in the research tree)
- `metrics/metrics_143_fate3.json` — Lab 143 (`143_fate_3_two_observer/metrics_143_fate3.json` in the research tree)

## What the article says

> We compared the remote record bit by bit and it stayed identical until the exact moment a signal travelling at the world's own light speed could have arrived. Four seeds out of four, plus a proof.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
