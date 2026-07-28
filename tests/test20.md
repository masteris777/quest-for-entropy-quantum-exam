# Test 20 — CH-19 · Passive observation cannot fake collapse

**Scorecard: PASS (theorem, machine-checked)** · section E. Structural theorems · suite v1.14 (frozen 2026-07-22)

## The question

Can ANY deterministic world, watched passively through a fixed set of questions, reproduce collapse statistics?

## Why it is a real test

This is the wall that killed the programme's earlier direction and the reason the fold exists at all. If passive watching could do it, no back-action would be needed and the whole machine would be over-engineered. It cannot, and that is proved, not measured.

## How this is set up in the toy

Not an experiment — a proof. The object is any deterministic flow observed through a fixed finite partition, with nothing written back. The Leggett-Garg quantity K3 is built from three-time correlations. The classical bound is established by exhaustive pointwise enumeration over the eight sign patterns plus a symbolic linearity identity; the quantum value is derived symbolically. The corroborating measurement (a passively watched world scoring just under the bound) came from a separate, earlier experiment in Model Two's lineage.

*(One-page overview of the apparatus, and what is deliberately not modelled: [`../setup.md`](../setup.md).)*

## Protocol

Not an experiment. T1: any deterministic flow observed passively through a fixed finite partition admits a joint distribution over all finite outcome histories, hence satisfies every Leggett-Garg bound (K3 <= 1) — checked by pointwise 8-case enumeration plus a symbolic linearity identity. T2: quantum collapse violates it exactly, K3 = 3/2 at theta = pi/3, symbolic. T3: therefore no passive observation of any deterministic world reproduces collapse statistics; the missing ingredient is necessarily non-passive.

## The pass bar — frozen before the run

All lemmas verified exactly, rational or symbolic, no floats. No untagged step.

## Controls that had to fail

Stage C is the empirical corroboration that came FIRST historically: a passively watched world was measured at K3 = 0.99963 — riding the classical ceiling, never crossing it. The theorem later explained why it never could.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| classical bound, symbolic | sum(p_i)=1 (probability) and each (1-value_i)>=0 (L2) => K3 = 1 - sum(p_i*(1-value_i)) <= 1. | Lab 119 |
| quantum value, symbolic | 2*cos(theta) - cos(2*theta) | Lab 119 |
| measured K3, passively watched world | `0.999634` | Lab 119 |
| does it exceed the classical bound? | `false` | Lab 119 |
| verdict | PASS | Lab 119 |
| verdict reason | All five lemmas verified exactly (rational/symbolic, no floats); the write-up has no untagged step; Stage C's stored-number comparison is consistent (delta gives K3=0.9996, and the classical/Born gaps were measured up to 0.529 in prior labs). | Lab 119 |

## Caveats and scope

The theorem constrains PASSIVE observation through a FIXED finite partition. It says nothing about what an active, state-rewriting observer can do — which is precisely the loophole the fold walks through, deliberately.

## Evidence files

- `metrics/metrics_119.json` — Lab 119 (`119_macrorealism_close/metrics_119.json` in the research tree)

## What the article says

> Passive observation of a deterministic world cannot fake collapse. Ever. It is a theorem.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
