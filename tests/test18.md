# Test 18 — CH-17 · Apparatus recoil (the two-dial complementarity)

**Scorecard: PASS (with a named anomaly)** · section D. Two systems at once · suite v1.14 (frozen 2026-07-22)

## The question

When the apparatus takes a kick from the particle, does a LIGHT apparatus record which path was taken and kill the fringes, while a HEAVY one learns nothing and leaves them intact?

## Why it is a real test

Sabine Hossenfelder's framing of the double slit: the wall the slits are cut in recoils, and that recoil is where which-path information physically lives. It makes complementarity mechanical rather than mystical — and it needs TWO dials, not one.

## Protocol

Two independent dials. Coupling dial: strength of the kick (CH-14's dial — V falls as D rises). Mass dial m: apparatus mixedness, from a light pointer to a heavy one. At each m measure V from counted events and D operationally, and check the per-run exchange ledger for exact conservation.

## The pass bar — frozen before the run

Per-run ledger exact; V(m) within 5J of the coherent-overlap curve; D_op(m) monotone and consistent with zero at maximal mixedness; V^2 + D_op^2 <= 1 + 3J.

## Controls that had to fail

The exchange ledger itself: 2,600,000 runs, 0 non-zero residuals. The analytic reference curve for D_op is frozen from run 1's quadrature.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| operational D by apparatus mass | `0 = 0.69695; 0.25 = 0.6313; 0.5 = 0.44675; 0.75 = 0.22205; 1.0 = 0.0001` | Lab 149b |
| D at maximal mixedness | `0.0001` | Lab 149b |
| max deviation from the analytic reference | `0.0101568` | Lab 149b |
| 5J bar | `0.0510837` | Lab 149b |
| max V^2 + D^2 | `0.964198` | Lab 149b |
| Englert bar | `1.03065` | Lab 149b |
| monotone in m | `true` | Lab 149b |
| Lab 149b verdict reason | All three bars hold: max |D_op - D_ref| = 0.01016 <= 5J = 0.05108; max V^2+D_op^2 = 0.9642 <= 1+3J = 1.0307; D_op monotone falling (0.6969 -> 0.0001). The operational recount lands on run 1's frozen reference curve. | Lab 149b |
| fresh-cell exchange ledger | `n_runs = 2600000; n_nonzero = 0` | Lab 156 |
| fresh-cell D at maximal mixedness | `0.0047` | Lab 156 |
| the m=0 anomaly, both runs | `V_149 = 0.691707; V_ref_149 = 0.674; dev_149 = 0.0173; V_fresh = 0.690929; V_ref_fresh = 0.67417; dev_fresh = 0.0167589; sigma_Vpair = 0.01` | Lab 156 |
| Lab 156 row verdict | PASS | Lab 156 |

## Caveats and scope

THE PROTOCOL CORRECTION. The suite's original one-line bar for this row conflated the two dials — visibility and distinguishability move oppositely on the coupling dial but not on the mass dial, so one bar could not score both. It was split into two and TIGHTENED, and the correction was written down and dated BEFORE the first counting run of Lab 149. Suite v1.9 records it. Separately: at m = 0 the visibility runs about 0.017 above the reference curve. It is inside the bar, but it is systematic and it replicated on fresh seeds (0.0173 then 0.0168). It is carried as a named open anomaly, ANOM-149-m0, not rounded away. True momentum remains out of scope: this is a recoil ANALOGUE.

## Evidence files

- `metrics/metrics_149.json` — Lab 149 (`149_recoil_analogue/metrics_149.json` in the research tree)
- `metrics/metrics_149b.json` — Lab 149b (`149_recoil_analogue/metrics_149b.json` in the research tree)
- `metrics/metrics_156.json` — Lab 156 (`156_conformance_hardening/metrics_156.json` in the research tree)

## What the article says

> the exchange ledger is exact every run, and as the apparatus gets heavier the recoverable path information falls to 0.0001 while the visibility holds

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
