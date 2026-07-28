# Test 17 — CH-16 · CHSH from an embedded pair

**Scorecard: PARTIAL — unfinished, obstruction measured** · section D. Two systems at once · suite v1.14 (frozen 2026-07-22)

## The question

Can a pair of observers living inside the machine produce correlations that beat the classical bound S = 2?

## Why it is a real test

This is Bell's test run from the inside. Quantum mechanics reaches 2.83. A global hidden-variable world is ALLOWED to do this — Bell only forbids the local kind — so the row is a genuine open question about whether the construction can reach it.

## How this is set up in the toy

Back to Model Two. The pair is prepared from a substrate channel the fold does not use: one channel value fixes a shared orientation `lam`, wing A gets a share at angle `lam` and wing B at `lam + pi/2` — a singlet analogue — and this happens **before any setting is chosen**. Each wing has two settings and folds under its own setting only. Four arms are run: the shared-substrate pair, a severed pair (wing B rebuilt from a disjoint pool), and both again with the settings swapped as an intervention check. 200,000 rounds per arm. Two supporting experiments ship with this deep dive: one measuring what local pseudorandomness can do (nothing), and one measuring what a shared global node can do (everything, on one bit).

*(One-page overview of the apparatus, and what is deliberately not modelled: [`../setup.md`](../setup.md).)*

## Protocol

Prepare a shared pair from a fold-unused substrate channel BEFORE any setting is chosen. Give each wing two settings. Fold each wing under its own setting only. Count the four correlators E(a,b) and combine into S. Run four arms: the substrate pair, a severed pair (independent pools), and both with the settings swapped.

## The pass bar — frozen before the run

Counted S > 2.5 with settings independence audited.

## Controls that had to fail

Severed pair drops to S = 0.002. Swap-intervention total variations all clean against their bars. Sixteen no-signalling checks across the arms, largest 0.006 against a bar of 0.019. A leakage audit records that settings were not derived from world state and no cross-wing setting channel existed.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| S, substrate pair | `2.00052` | Lab 150 |
| sigma_S | `0.00774528` | Lab 150 |
| S, severed control | `0.0019644` | Lab 150 |
| S, settings swapped | `1.9872` | Lab 150 |
| correlator E(0,0) | `-0.50103` | Lab 150 |
| correlator E(0,1) | `0.50086` | Lab 150 |
| correlator E(1,0) | `-0.50208` | Lab 150 |
| correlator E(1,1) | `-0.496549` | Lab 150 |
| rounds per arm | `200000` | Lab 150 |
| quantum reference (labelled only) | `2.82843` | Lab 150 |
| classical reference (labelled only) | `2` | Lab 150 |
| settings derived from world state | `false` | Lab 150 |
| cross-wing setting channel | `false` | Lab 150 |
| verdict | UNBUILT-AT-BUDGET | Lab 150 |
| verdict reason | S_substrate = 2.0005 +/- 0.0077 does not exceed 2 + 3*sigma_S = 2.0232: the preparation cannot produce cross-wing correlation sufficient for S > 2 under the frozen guardrails. Obstruction diagnosis in lab-report-150.md (declared analytic expectation D11: guardrails 2+7 + deterministic fold => LHV model => E[S] <= 2 by CHSH/Bell; the counted value sits at the sawtooth LHV boundary reference 2). | Lab 150 |
| -- calibration: a deterministic local strategy reaches | `2` | Lab 77 |
| -- calibration: quantum singlet reaches | `2.82942` | Lab 77 |
| -- calibration: a no-signalling 'PR box' would reach | `4` | Lab 77 |
| -- best S per local pseudorandom family (Lab 77) | `lcg = 2.00332; logistic_chaos = 2.00302; crypto_hash = 2.00262; os_crypto = 2.00233; shared_lambda_response = 2.00076` | Lab 77 |
| -- spread across all five families | `0.00099` | Lab 77 |
| -- a shared global node reaches (Lab 78) | `2.82768` | Lab 78 |
| -- ... on this many substrate bits per trial | `1` | Lab 78 |
| -- ... with signalling leakage per side | `alice = 0.000464; bob = 0.000545` | Lab 78 |

### Recomputed from raw counts

**Recomputed from the four raw correlators, not read from a summary field:**

    S = |E00 - E01 + E10 + E11| = 2.0005184586
    stored value                = 2.0005184586
    difference                  = 0.00e+00

## Caveats and scope

The row reads PARTIAL, not FAIL, and the distinction is a theorem rather than a preference. Under the guardrails imposed by adversarial review — own-setting-only fold contexts, world-state-independent settings — the certified pair is Bell-factorized, and for factorized models S <= 2 is PROVED. The run therefore measured a ceiling that had already been derived. That it saturates the ceiling exactly is the informative part. The completion path (joint-setting-dependent substrate dynamics with counted marginal invariance) is designed but NOT built, and it is gated behind user and critique review because it touches the model's foundations. It may not work.

**The two supporting experiments in the table are worth reading together.** Lab 77 measured what LOCAL randomness can do: five families from a linear congruential generator up to SHA-256, a million trials each, all pinned at S = 2.003 with a spread of 0.001. Complexity buys nothing — a cryptographic hash is exactly as unable to violate Bell as a toy generator. Lab 78 measured what a SHARED GLOBAL node can do: the full quantum value, on exactly one shared bit per trial, with signalling leakage down at 0.0005. So the resource that would close CH-16 is known, cheap, and already measured in isolation. What has not been done is making the fold itself supply it inside Model Two. That is the gap, stated as precisely as we can state it.

## Evidence files

- `metrics/metrics_150.json` — Lab 150 (`150_embedded_chsh/metrics_150.json` in the research tree)
- `metrics/metrics_77.json` — Lab 77 (`77_local_prng_bell_ceiling/metrics_77.json` in the research tree)
- `metrics/metrics_78.json` — Lab 78 (`78_two_layer_shared_node_bell/metrics_78.json` in the research tree)

## What the article says

> We got S = 2.0005, plus or minus 0.0077. ... It is not a failure to correlate — it is the classical ceiling, hit exactly.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
