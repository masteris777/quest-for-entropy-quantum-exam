# Test 06 — CH-06 · Arbitrarily deep interference nulls

**Scorecard: FAIL — the confessed discriminator** · section B. Interference · suite v1.14 (frozen 2026-07-22)

## The question

Can the dark bands of the interference pattern be made arbitrarily dark, the way quantum mechanics allows?

## Why it is a real test

This is the one place the family is forbidden something quantum mechanics permits. Quantum interference can cancel exactly: push the setup toward a perfect null and the counted darkness goes to zero, with no floor. If a construction has a floor, it is distinguishable from quantum mechanics by measurement, not by argument.

## Protocol

Build a ladder of ever-deeper target nulls (eps^2 from 0.1 down to 1e-4), count events landing in the dark channel at each rung with N up to 500,000, and compare the counted dark fraction against the Born prediction (which is eps^2 itself). Run the ladder for two different fold architectures: the certified richness fold (the incumbent) and a certified hierarchical / dominance fold.

## The pass bar — frozen before the run

Counted contrast must keep falling with the target depth; a ratio of counted to Born within [0.5, 2.0] at every rung, log-log slope within 0.1 of 1.

## Controls that had to fail

Three independent escape routes were tested and all closed. (1) Reservoir: change the pool, floor unchanged. (2) Gauge: average over a 24-element Clifford design with exact diagonal-coset structure — the first-harmonic residual returns at 0.919 of baseline, classified INVARIANT, so the floor is not a coordinate artifact. (3) Architecture: the hierarchical fold fails from the other side.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| Lab 157 verdict (gauge route) | INVARIANT | Lab 157 |
| baseline first-harmonic residual h1 | `0.01981` | Lab 157 |
| twirled h1 (24-element Clifford design) | `0.0182145` | Lab 157 |
| ratio twirled/baseline | `0.91946` | Lab 157 |
| classification | INVARIANT | Lab 157 |
| design is a group of 24 | `true` | Lab 157 |
| Lab 158b verdict (architecture route) | PARTIAL | Lab 158b |
| Lab 158b verdict reason | Stage A holds (max RMS 0.00500 vs bar 0.06); B1 fails (ratio bar False, slopes 224: 1.4701, 226: 1.7801, control floors True); B2 holds (5 applicable cells, max applicable ratio 1.029 vs bar 3.0). Failing: ['B1']. | Lab 158b |

### Recomputed from raw counts

**The near-null ladder, recomputed from raw event counts.** `p_dark` is counted-dark / N; Born predicts `p_dark = eps^2`, so `ratio` is how many times too much light is left in the dark band.

| frame | target eps^2 | N | hierarchical dark | hier p_dark | incumbent dark | incumbent p_dark | incumbent ratio vs Born |
|---|---|---|---|---|---|---|---|
| 224 | 0.1 | 50,000 | 5,177 | 0.10354 | 6,159 | 0.12318 | 1.232x |
| 224 | 0.03 | 50,000 | 1,214 | 0.02428 | 2,593 | 0.05186 | 1.729x |
| 224 | 0.01 | 50,000 | 313 | 0.00626 | 1,249 | 0.02498 | 2.498x |
| 224 | 0.003 | 50,000 | 57 | 0.00114 | 826 | 0.01652 | 5.507x |
| 224 | 0.001 | 50,000 | 5 | 0.0001 | 661 | 0.01322 | 13.22x |
| 224 | 0.0003 | 500,000 | 0 | 0 | 6,132 | 0.012264 | 40.88x |
| 224 | 0.0001 | 500,000 | 0 | 0 | 6,048 | 0.012096 | 121x |
| 226 | 0.1 | 50,000 | 5,169 | 0.10338 | 6,121 | 0.12242 | 1.224x |
| 226 | 0.03 | 50,000 | 1,250 | 0.025 | 2,648 | 0.05296 | 1.765x |
| 226 | 0.01 | 50,000 | 331 | 0.00662 | 1,293 | 0.02586 | 2.586x |
| 226 | 0.003 | 50,000 | 61 | 0.00122 | 780 | 0.0156 | 5.2x |
| 226 | 0.001 | 50,000 | 6 | 0.00012 | 680 | 0.0136 | 13.6x |
| 226 | 0.0003 | 500,000 | 1 | 2e-06 | 6,268 | 0.012536 | 41.79x |
| 226 | 0.0001 | 500,000 | 0 | 0 | 6,176 | 0.012352 | 123.5x |

At the deepest rung (frame 224, eps^2 = 1e-4, N = 500,000): Born expects about **50** dark events. The hierarchical fold produced **0**. The incumbent produced **6,048** — a floor of 0.0121, 121 times too bright.
At the deepest rung (frame 226, eps^2 = 1e-4, N = 500,000): Born expects about **50** dark events. The hierarchical fold produced **0**. The incumbent produced **6,176** — a floor of 0.01235, 124 times too bright.

## Caveats and scope

The CLIFF-OR-FLOOR DICHOTOMY is a named conjecture, measured on both sides and proved on neither. It is not established over every possible deterministic measurement architecture — only over the two certified ones tested here plus three invariance classes. Closing it (or breaking it) is the open problem.

## Evidence files

- `metrics/metrics_157.json` — Lab 157 (`157_gauge_twirl_scout/metrics_157.json` in the research tree)
- `metrics/metrics_158b.json` — Lab 158b (`158_hierarchical_fold/metrics_158b.json` in the research tree)

## What the article says

> Push toward a perfect null and the contrast stops falling. It flattens out at about 1.2 percent and stays there.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
