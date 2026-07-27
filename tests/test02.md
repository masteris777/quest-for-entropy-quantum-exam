# Test 02 — CH-02 · Frame robustness

**Scorecard: PASS** · section A. Static statistics · suite v1.14 (frozen 2026-07-22)

## The question

Does it still work if the observer asks its questions in a different direction — and if the world underneath is a different world?

## Why it is a real test

A single lucky frame would be worthless. Quantum statistics hold in every basis; a construction that only works in one is a coincidence with good marketing.

## Protocol

Repeat CH-01 with freshly drawn observer frames, then repeat again on a second, independently built substrate world (W2) with its own turn operator and its own initial state. Bars copied over unchanged.

## The pass bar — frozen before the run

Same bar as CH-01, on fresh frames and fresh substrate.

## Controls that had to fail

Ridge tests at chance everywhere; round-trip invertibility of the substrate at 1e-15; a low-tail frame that failed pre-declared screening was excluded on the record and replaced, rather than quietly dropped.

## What was measured

Every value below is read live out of the frozen metrics files in `metrics/` by
`extract_the-quantum-exam.py`. None of it is typed by hand.

| quantity | value | source |
|---|---|---|
| Lab 101 verdict | OTHER | Lab 101 |
| Lab 101b verdict | CONTROL-REAL | Lab 101b |
| Lab 101c verdict | CELL-RESTORED | Lab 101c |

## Caveats and scope

W2 turned out to be variationally *easier* than W1 — its floors are lower. That is reported as-is; it means the first world was not a favourable pick.

## Evidence files

- `metrics/metrics_101.json` — Lab 101 (`101_existence_hardening/metrics_101.json` in the research tree)
- `metrics/metrics_101b.json` — Lab 101b (`101_existence_hardening/metrics_101b.json` in the research tree)
- `metrics/metrics_101c.json` — Lab 101c (`101_existence_hardening/metrics_101c.json` in the research tree)

## What the article says

> Fresh directions, and then a fresh substrate world underneath. Same result.

---

*Part of the companion pack for [Quest for Entropy #3 — The Machine Takes a Quantum Exam](../article.md).
The scorecard summary is in [`../scorecard.md`](../scorecard.md); run `python verify_scorecard.py`
to re-check every number the article quotes.*
