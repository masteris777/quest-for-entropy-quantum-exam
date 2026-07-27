# Scorecard — rotor family, recipe frozen (suite v1.14)

Twenty questions. **18 passed, 1 failed, 1 unfinished.** Every pass bar was written and
version-stamped before the machine was pointed at it; a bar could be made harder afterwards
and never softer.

| ID | question | result | deep dive |
|---|---|---|---|
| [CH-01](tests/test01.md) | Born statistics | PASS | [test01.md](tests/test01.md) |
| [CH-02](tests/test02.md) | Frame robustness | PASS | [test02.md](tests/test02.md) |
| [CH-03](tests/test03.md) | Non-contextuality at the Gleason hinge | PASS | [test03.md](tests/test03.md) |
| [CH-04](tests/test04.md) | Mixture affinity and the superposition gap | PASS | [test04.md](tests/test04.md) |
| [CH-05](tests/test05.md) | Cosine fringes with first-harmonic purity | PASS | [test05.md](tests/test05.md) |
| [CH-06](tests/test06.md) | Arbitrarily deep interference nulls | FAIL — the confessed discriminator | [test06.md](tests/test06.md) |
| [CH-07](tests/test07.md) | The decoherence law | PASS | [test07.md](tests/test07.md) |
| [CH-08](tests/test08.md) | The which-path sum rule | PASS | [test08.md](tests/test08.md) |
| [CH-09](tests/test09.md) | Repeatability | PASS | [test09.md](tests/test09.md) |
| [CH-09b](tests/test10.md) | The one-step collapse chain | PASS | [test10.md](tests/test10.md) |
| [CH-10](tests/test11.md) | Post-measurement blurring | PASS | [test11.md](tests/test11.md) |
| [CH-11](tests/test12.md) | Delayed choice | PASS | [test12.md](tests/test12.md) |
| [CH-12](tests/test13.md) | Interaction-free (null-result) collapse | PASS | [test13.md](tests/test13.md) |
| [CH-13](tests/test14.md) | The quantum eraser | PASS | [test14.md](tests/test14.md) |
| [CH-14](tests/test15.md) | The visibility-distinguishability trade-off | PASS | [test15.md](tests/test15.md) |
| [CH-15](tests/test16.md) | No signalling | PASS | [test16.md](tests/test16.md) |
| [CH-16](tests/test17.md) | CHSH from an embedded pair | PARTIAL — unfinished, obstruction measured | [test17.md](tests/test17.md) |
| [CH-17](tests/test18.md) | Apparatus recoil (the two-dial complementarity) | PASS (with a named anomaly) | [test18.md](tests/test18.md) |
| [CH-18](tests/test19.md) | The observer's view is forced to be complex-unitary | PASS (theorem, machine-checked) | [test19.md](tests/test19.md) |
| [CH-19](tests/test20.md) | Passive observation cannot fake collapse | PASS (theorem, machine-checked) | [test20.md](tests/test20.md) |

**CH-06 is the confessed failure** — the interference-contrast floor, and the one place this
family makes a prediction that experiment can kill. **CH-16 is unfinished, not lost** — under
the guardrails imposed, S <= 2 is a theorem, so the run measured a ceiling that had already
been derived.

The suite itself (the frozen contract, with its full changelog) lives in the research
repository as `quantum-conformance-suite.md`. This pack carries the evidence for the rows.
