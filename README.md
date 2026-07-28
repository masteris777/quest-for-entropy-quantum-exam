# The Quantum Exam — companion repository

Evidence repo for **Quest for Entropy #3: [“The Machine Takes a Quantum Exam”](article.md)** —
twenty questions a construction has to answer before it can call itself quantum, put to one
deterministic clockwork with its recipe frozen.

**18 passed. 1 failed. 1 unfinished.** The scorecard is in [`scorecard.md`](scorecard.md);
one deep-dive file per question is in [`tests/`](tests/); the laboratory's own frozen output
is in [`metrics/`](metrics/), unmodified.

## Run it

```
python verify_scorecard.py
```

No arguments, no network, no install beyond the standard library — it reads the JSON in
`metrics/` and writes nothing. It re-checks **every number this piece rests on** against the
lab's own measurements, recomputing the headline quantities from raw counts wherever raw
counts exist, and exits non-zero if a single one has drifted.

Compare against `expected_output/verify_scorecard.txt`, the captured output of a real run:

```
python verify_scorecard.py > mine.txt
diff mine.txt expected_output/verify_scorecard.txt
```

Verified working on the author's machine (Windows 11, CPython 3.12.11). The verifier needs no
third-party packages; `requirements.txt` exists only for regenerating the article's figures.

## Scope — read this before you read anything else

**This pack certifies the SCORECARD against frozen evidence. It does not re-run the
experiments.** The twenty rows come from about two dozen laboratory runs spanning Labs 100 to
158; several take many minutes each and pull in the full research tree. What ships here is what
those labs *wrote*: their metrics files, byte for byte, plus a checker that holds every
reported number to them.

If you want a machine you can rebuild from scratch in two seconds and watch produce its own
numbers, that is the previous episode's pack:
**[quest-for-entropy-the-machine](https://github.com/masteris777/quest-for-entropy-the-machine)**
(`python run_all.py`). This pack is the exam; that one is the machine.

The metrics files are shipped **exactly as the labs wrote them**, including their references to
internal working documents (`lab-goal.md`, `feedback-2.md`, adjudication notes) that are not
part of this repository. Editing evidence to tidy up its footnotes is not something this project
does, so those references stay in.

## What is in here

```
verify_scorecard.py       the checker - the whole point
scorecard.md              the twenty rows, with links into tests/
tests/test01..test20.md   one deep dive per question: what was asked, the frozen pass bar,
                          the protocol, the controls, the measured numbers, and the caveats
metrics/                  the laboratory's frozen output, 27 files, unmodified
ledger.md                 the five times the referee caught US while running this exam
expected_output/          the captured output of a real successful run
article.md, assets/       the article as published, and its figures
MANIFEST.sha256           checksums of everything above
.gitattributes            disables EOL conversion, so those checksums verify everywhere
```

Every number in `tests/*.md` is **read out of `metrics/` at build time**, not typed by hand —
the deep dives are rendered by `extract_the-quantum-exam.py` in the research repository. If a
metrics file changed, the deep dives would change with it and `verify_scorecard.py` would start
failing. That is the intended failure mode.

## The rules the exam ran under

1. **The suite was frozen first**, as a versioned file with a changelog, before the machine was
   pointed at it.
2. **A bar could be made harder, never softer.** One bar changed mid-campaign (CH-17); it was
   split in two and tightened, and the change is dated *before* that lab's first counting run.
3. **The recipe was frozen too.** It was tuned once, against CH-01 only, and then locked for
   every other row. No re-tuning between questions.
4. **Every probability is counted from events**, never computed from a quantum formula. The
   formula appears only afterwards, as a reference curve.
5. **Every question shipped with a control that had to fail.** Several did fire — see the
   `iso_control`, `severed`, `generic` and `v1_control` entries throughout `metrics/`.
6. **Nine rows were re-run** on fresh frames, fresh seeds and a second substrate world, with the
   bars copied over verbatim.

## The two rows that are not passes

**CH-06 — the confessed failure.** Interference contrast floors at about 1.2e-2 instead of
falling without limit. Three escape routes were tested and closed: reservoir, gauge (a
24-element Clifford twirl leaves the residual at 0.92 of baseline), and architecture — where a
certified hierarchical fold fails from the *opposite* side, producing 0 dark events in 500,000
where Born predicts about 50. The named conjecture (**cliff-or-floor**) is measured on both
sides and **proved on neither**. See [`tests/test06.md`](tests/test06.md).

**CH-16 — unfinished, not lost.** Under the guardrails imposed by adversarial review, the
certified pair is Bell-factorized, and for factorized models S ≤ 2 is a theorem. The run
measured S = 2.0005 ± 0.0077 — the classical ceiling, saturated exactly, with the severed
control at 0.002. The completion path is designed but **not built**, and may not work. See
[`tests/test17.md`](tests/test17.md).

## What this does NOT claim

> This is a **demonstration of a mechanism, not a claim about nature.** The scorecard says one
> family of machines, at one frozen setting, reproduced twenty specific behaviours at its own
> precision of about one percent. It does not say our universe is a clockwork, does not
> reinterpret quantum mechanics, and does not dodge Bell's theorem — the hidden machinery is
> *global*, not local, exactly because Bell rules out the local kind. The exam is our own, and
> the questions in it are not independent of each other. Twenty behaviours is not quantum
> mechanics: there is no spin here, no identical particles, no field theory. Where the machine
> falls short, the shortfall is measured and published rather than hidden.

Specifically **not** claimed by anything in this repository: that the cliff-or-floor dichotomy
is proved; that CH-16 was won; that the fold is unique; that any of this beats quantum
mechanics anywhere. It does not.

## How this was made

The author is a software architect, not a physicist. The direction, the questions and the calls
are his; the heavy lifting — the math, the physics checks, the code, the sums — is AI. To keep
that honest, the work runs through a harness: **every experiment declares its pass marks before
it runs**, a mark may be made harder afterwards but never softer, results are challenged by
independent adversarial AI review, and every mistake caught goes into a **public honesty
ledger** rather than quietly out of the record. The five from this exam are in
[`ledger.md`](ledger.md), with numbers. Nothing here comes from a model's
memory: every number is printed by code you can run against evidence files you can hash.

## License

Code: MIT. Article text and figures: CC BY 4.0. See `LICENSE`.
