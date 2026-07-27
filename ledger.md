# The honesty ledger — the conformance campaign

Five times during this exam the machine looked wrong and **we** were wrong. This file is the
record. Four of the five are numbered entries in the programme's running honesty ledger — the
numbering starts at 33 because earlier entries belong to earlier campaigns. The fifth is not a
ledger entry at all but a dated, versioned change to the exam itself, and it is here because it
is the same kind of admission.

The rule these come from: when a result is caught before it is published, the catch goes on the
record with the same weight the result would have had. A scorecard without this file is
advertising.

---

## #33 — We tested the wrong thing (CH-10, Lab 148 run 1)

**What happened.** The first run of the post-measurement blurring test returned a FAIL.

**What was actually wrong.** The run compared the counted decay against a mis-referenced
protocol — the wrong analytic curve for what the script was actually doing. The FAIL was
therefore about our comparison, not about the machine.

**Disposition.** The run was declared **VOID as a CH-10 test**, not "failed and retried". A
corrected protocol was written into `feedback-2.md` and re-run as Lab 148 run 2, which passed:
counted certainty exactly 1.0, RMS 0.0103 against the corrected reference. No bar was weakened
in the process.

**Bonus.** Re-reading the protocol surfaced a stronger test nobody had asked for — the one-step
counted collapse chain — which became **CH-09b** and is now one of the strongest rows on the
paper. Evidence: `metrics/metrics_148_run2.json`, deep dives `tests/test11.md`, `tests/test10.md`.

---

## #34 / #35 — Our instrument was broken, not the machine (CH-13 and CH-14, Labs 147 and 152)

**What happened.** The quantum eraser and the visibility-distinguishability trade-off both
failed hard.

**What was actually wrong.** Both failures traced to the *marker* being measured with: an
uncertified "bare argmax" fold that had never been put through the certification the main fold
had. Entry #35 sharpened it: the v1 marker had a pure-state infidelity of 0.0245 — a coverage
gap, not a physics result.

**Disposition.** The failures were attributed to the instrument and the rows were re-gated
rather than recorded. This exposed a real, previously unnamed structural gap: **the family had
no certified measurement instrument for two-outcome subsystems at all.** One was built (Lab
151), certified on its own terms (J2 = 0.0031, exact ties 50/50 within 3e-4), hardened into a
v2 (Lab 153), and only then were CH-13 and CH-14 re-run.

**The check that makes this honest rather than convenient:** the uncertified v1 marker was kept
as a permanent control. In the fresh-cell hardening it reproduces the exact broken corner it
produced originally (`v1_control_reproduces_corner: true` in `metrics/metrics_156.json`). The
instrument story is falsifiable, not asserted.

Evidence: `metrics/metrics_147.json`, `metrics/metrics_156.json`, deep dives `tests/test14.md`,
`tests/test15.md`.

---

## #36 — We ran quantum mechanics through our own marking scheme, and it failed too (CH-14, Lab 154)

**What happened.** With the certified marker in place, the trade-off row came back at
**V² + D² = 1.0456** at coupling 3π/8 — over the bound of 1 + 3J = 1.0307. Taken at face value
that is a measured departure from quantum mechanics, and it would have been the biggest result
of the campaign.

**What was actually wrong.** Before claiming it, a matched quantum-mechanical replay — real
Born statistics, same coupling sweep — was pushed through the identical scoring code. **It
scored the same excess, 1.0457.** The estimator was the problem: post-collapse truth labels do
not instantiate Englert's *operational* distinguishability. The quantity being computed was not
the quantity the physics defines.

**Disposition.** Lab 155 recounted with the operational definition (single-branch calibration
ensembles through the identical coupling and marker fold). Result: max V² + D² = **1.000004**,
inside the bound and saturating at full coupling. The bar itself never moved.

**The standing rule this created:** *a bar is only meaningful if the reference physics scores
correctly on the same instrument.* It is now applied to every conformance row that reports a
bound. Evidence: `metrics/metrics_154.json` (whose overall verdict still reads PARTIAL because
of this kill), `metrics/metrics_155.json`, deep dive `tests/test15.md`.

---

## #37 — We carried a setting where we should have re-fitted one (CH-12, Lab 156)

**What happened.** The interaction-free collapse row passed on its home cells and **missed on
fresh frames**: profile deviations 0.048 and 0.028 against a bar of 0.027. Lab 156 recorded row
R6 as **FAIL**, and that FAIL is still in `metrics/metrics_156.json` — it was not overwritten.

**What was actually wrong.** The fresh frames were run with the recipe **transferred** from the
original frames rather than re-fitted for them. And the size of the miss matched, closely, a
transfer penalty that had been measured independently elsewhere in the same battery.

**Disposition.** Lab 156b re-fitted the recipe natively for the new frames — the ordinary,
declared, CH-01-only tuning step — and re-ran. Profile deviations dropped to 0.0058 and 0.0154,
inside the bar. The attribution was confirmed *by repair*, which is the only way an attribution
like this is worth anything.

**The rule this created:** bar-instrument calibration — a pass bar assumes the instrument was
calibrated for the cell it is applied to. Evidence: `metrics/metrics_156.json` (row R6),
`metrics/metrics_156b.json`, deep dive `tests/test13.md`.

---

## Suite v1.9 — We wrote a bar that measured two things at once (CH-17)

*Not a numbered ledger entry: this one is a change to the exam, recorded in the suite's own
changelog as version 1.9 rather than in the ledger. It belongs here anyway.*

**What happened.** The apparatus-recoil row's original pass mark was a single line, and it
conflated two physically different dials: **coupling strength** (where visibility falls as
distinguishability rises) and **apparatus mixedness** (where distinguishability falls toward
zero while visibility holds at the kick's coherent overlap). One bar cannot score both, because
the two quantities move in opposite directions on one dial and the same direction on the other.

**Disposition.** The bar was split into two and **tightened**, and — the part that matters — the
correction was written down, versioned as suite v1.9, and dated **before Lab 149's first
counting run**. It is a theory-driven protocol correction, not a post-result bar change, and the
timestamps are the evidence for that distinction.

**Carried forward openly:** at zero apparatus mass the counted visibility runs about 0.017 above
the analytic reference. It is inside the bar, but it is systematic and it replicated on fresh
seeds — 0.0173 in the first run, 0.0168 on hardening. It is named **ANOM-149-m0** and carried as
an open anomaly rather than rounded away. Evidence: `metrics/metrics_149b.json`,
`metrics/metrics_156.json` (row R9), deep dive `tests/test18.md`.

---

## The pattern

Three of these (#33, #34/#35, #36) are the same lesson in different disguises: **a test is only
as good as the instrument that produced it.** The other two are about bars rather than
instruments: a bar assumes a calibration (#37), and a bar must measure one thing (v1.9).

Zero of them are the machine being wrong in a way that survived checking. That is not a boast —
it is a warning about what this file can and cannot tell you. It records the errors we caught.
It cannot record the ones we did not.
