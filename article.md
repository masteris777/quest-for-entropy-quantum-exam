# The Machine Takes a Quantum Exam

*Quest for Entropy #3: twenty questions, one deterministic clockwork, and the two answers it could not give.*

![the scorecard](assets/scorecard.png)
<!-- The frozen conformance scorecard, suite v1.14. Eighteen passed, one failed, one unfinished. -->


Last time we took the machine apart. A pool of ninety-six rotors turning at speeds that never line up. A state of three numbers. And one move — **the fold** — where the observer compares three lengths, writes down which one won, and rewrites the state from six fresh rotor readings.

No dice. No collapse rule. No quantum formula anywhere inside it.

We said it comes out looking quantum. That is a big claim, and a claim like that is worth nothing until someone writes down what would prove it wrong. So we did. We wrote a twenty-question exam, fixed every pass mark before the machine ran, and made it sit the paper.

Here is the whole result, question by question. Including the one it failed.

## The question

What would it even mean for a machine to "be quantum"?

Not that it uses the quantum formula — this one never does. Not that it feels mysterious. The only test that means anything is behavioural: **put it through the things quantum systems do, and see if it does them too.**

So the question became a list. Twenty items. Not a vague feeling about weirdness, but twenty specific, countable behaviours with a number attached to each: Born statistics, interference with the right shape, the decoherence law, repeatability, delayed choice, the quantum eraser, no-signalling, the trade-off between knowing the path and seeing the stripes.

That list is the exam. It is the thing that can fail.

## The rules

An exam you write for your own machine is worth nothing unless the rules are strict. Ours:

**1. The exam was frozen first.** Every question and every pass mark was written down and version-stamped before the machine was pointed at it. The file has a changelog. You can read it.

**2. A mark may get harder, never softer.** If we found a bar too easy, we could tighten it. We could never loosen one because the machine missed it. One bar did change mid-exam — question 17 — and it changed *before* that test's first counting run, and it got harder. It is dated and on the record.

**3. The recipe was frozen too.** The machine has one setting — the lean, the two-and-a-half-to-one from last episode. It was tuned once, against question 1 only. Then it was locked. Nothing was re-tuned between questions. A machine that gets re-adjusted for each question is not passing an exam, it is being coached.

**4. Every probability is counted, never computed.** The machine counts events. The quantum formula appears only afterwards, as a line on the chart to compare against. If the formula were inside the machine, the whole exercise would be a circle.

**5. Every question needs a control that fails.** A test that everything passes is not a test. So each question came with a deliberately broken version — a scrambled frame, a severed link, a fold switched off — and the broken version had to fail. If the control passed too, the question was measuring nothing and we threw it out.

**6. Then we did it all again on a different machine.** Nine of the questions were re-run on fresh frames, fresh seeds and a second substrate world, with the bars copied over word for word. That is the part we trust most.

## The run

**Eighteen passed. One failed. One we could not finish.**

**A. Static statistics** — 4 questions, all passed.
**B. Interference** — 4 questions, 3 passed, **1 failed**.
**C. Measurement dynamics** — 7 questions, all passed.
**D. Two systems at once** — 3 questions, 2 passed, **1 unfinished**.
**E. Structural theorems** — 2 questions, both machine-checked arguments rather than experiments.

The failure is question 6, and it is the most valuable line in the table. The unfinished one is question 16, and it is unfinished for a reason worth understanding. Both get their own section below.

Now the paper itself. **Every question links to its own file in the companion repository** — the exact setup, the pass mark as it was frozen, the protocol, the controls, the measured numbers, and the caveats. The numbers are all there. They are deliberately not here, because a wall of digits you cannot check is not evidence, it is decoration.

## Part A — Does it get the numbers right?

**[CH-01](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test01.md) · Born statistics.** The foundation. Quantum mechanics says the chance of an outcome is the squared length of its arrow. The machine never squares anything — it compares three lengths and keeps the winner. So: count tens of thousands of events and see where the frequencies land. They land on the quantum values, at the machine's own precision of roughly one percent. Hold on to that one percent; the whole rest of this piece lives at that scale. **PASS.**

**[CH-02](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test02.md) · Any frame.** A worry you should have: maybe we found one lucky set of questions for the observer to ask. So we turned the frame. Fresh directions, and then a fresh substrate world underneath. Same result. Not one lucky frame — the behaviour, not the setup. **PASS.**

**[CH-03](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test03.md) · No contextuality.** In quantum mechanics, the answer to a question does not depend on which other questions you ask alongside it. That sounds obvious. It is not — it is a strong constraint, and it is the hinge that forces the squared law. We asked the same question inside many different groupings and measured the drift. It stayed at the machine's one percent while the scrambled control drifted ten times worse. **PASS.**

**[CH-04](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test04.md) · Mixtures and superpositions.** Two setups. Flip a coin to pick one, and the statistics should be the plain average of the two — nothing extra. Combine them *coherently* instead, and an extra term must appear, of a size the theory pins down. The machine does both. This is the difference between "don't know which" and "both at once", and it keeps them apart. **PASS.**

## Part B — Does it interfere?

**[CH-05](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test05.md) · Fringes.** Point the machine at a two-path setup, sweep the phase, count. The counts trace a cosine — the real interference curve. And the shape is clean: no false overtones above the noise. Plenty of things can wiggle. Very few wiggle as a pure first harmonic. **PASS.**

**[CH-06](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test06.md) · Deep nulls.** *The one it failed.* Full section below.

**[CH-07](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test07.md) · Decoherence.** Add phase noise and interference should fade — not any old way, but along one specific curve. Turn the noise up and the machine's visibility follows that curve step for step. It loses coherence by the right law, not just in the right direction. **PASS.**

**[CH-08](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test08.md) · The which-path sum rule.** Mark which path was taken, and interference must die completely: the two paths just add, no cross term. Under full marking the machine's fringes collapse to the residual floor while the path information reads exactly 1 — total knowledge, no stripes. This is the one the browser demo shows live. **PASS.**

## Part C — Does measurement behave?

This is the section we care about most. Statistics can be faked by many things. *Dynamics* — what happens to a system after you look at it — is much harder to fake, and it is where our earlier attempts died.

**[CH-09](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test09.md) · Repeatability.** Measure, then measure again immediately. Quantum mechanics says: certainty, the same answer. Not "usually" — always. The machine repeated the answer every single time, in two different worlds, without a single exception. And nobody wrote a collapse rule anywhere; it falls out of the fact that the rewritten state leans toward what was just recorded. **PASS.**

**[CH-09b](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test10.md) · The collapse chain.** Harder version. Do not just re-measure — measure, let one tick pass, measure again, and check the *whole table* of transitions between the two, off-diagonal entries included. Quantum mechanics gives an exact table. The machine's counted table matches it, every entry inside the bar we had set beforehand. This is the one that convinced us. Repeatability is a single number and a lucky machine might hit it. A nine-entry table is not luck. **PASS.**

**[CH-10](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test11.md) · Blurring back out.** After a measurement the answer is sharp. Wait without measuring and it should blur again — down a specific curve, with a dip and a partial revival. The machine follows that curve, revival included. And it sits far closer to that curve than to the control that fakes it by measuring over and over, freezing the value instead of letting it move. Freezing and evolving look different, and the machine does the second one. **PASS.**

**[CH-11](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test12.md) · Delayed choice.** Decide whether to check the path *after* the particle is already on its way. Quantum mechanics says the fringes depend on **whether** you check, never on **when**. So we slid the check up and down the timeline, from before the flight begins to the last instant before it ends. The fringes died the same amount every time — flat, no dependence on timing at all. Nothing here travels backwards in time. **PASS.**

**[CH-12](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test13.md) · The detector that never fired.** The strangest one on the paper. Put a detector on one path. It does not fire — so the particle went the other way. Nothing touched it. And yet the fringes are gone, because the *possibility* of detection was enough. Learning something by not-seeing it still costs you the interference. The machine does this. **PASS.**

**[CH-13](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test14.md) · The quantum eraser.** Mark the path, so the fringes die. Then erase the marker and sort the records into two piles by what the erased marker said. Fringes come back in each pile — and the two piles are exactly out of step with each other, so pooling them cancels back to nothing.

![the eraser](assets/eraser_fringes.png)
<!-- Counted events. Two subensembles at full visibility, half a turn apart; everything together, flat. -->

The machine splits the records evenly, brings both piles back at nearly full visibility, and puts them almost exactly half a turn apart. Pooled together they flatten. Nothing was un-measured here. The information was reorganised, and that is all the eraser ever was. **PASS.**

**[CH-14](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test15.md) · The trade-off.** Path knowledge and fringe visibility cannot both be high — squared and added, they must not pass 1. The machine's counted values reach that limit and go no further, and they saturate it at full coupling, which is the interesting part: it does not sit safely below, it rides the edge exactly where quantum mechanics rides it. This row also came within one check of us publishing something false. That story is in the ledger. **PASS.**

## Part D — Does it work with two systems?

**[CH-15](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test16.md) · No signalling.** Two distant observers. Measuring one must not change what the other one sees — not "on average", not "approximately". This is the row where the toy needs an actual notion of *distance* and *light speed*, and it has one: the test runs in a second, simpler world built as a line of cells where each cell only ever talks to its neighbours. That makes the speed limit exactly one cell per tick, by construction. We poked the world next to one observer and compared the far observer's record bit by bit. It stayed identical until the exact tick a signal could have arrived — while the near observer, inside the cone, noticed immediately. That second half matters: it proves the poke was real. **PASS.**

**[CH-16](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test17.md) · CHSH.** *The one we could not finish.* Full section below.

**[CH-17](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test18.md) · Recoil.** A neat way to see the double slit: the wall the slits are cut in gets a kick when a particle goes past, and that kick carries which-slit information. A light wall records the kick and the fringes die. A heavy wall barely moves, learns nothing, and the fringes survive. The machine reproduces both dials — the kick is booked exactly every run, and as the apparatus gets heavier the recoverable path information falls away to nothing while the visibility holds. **PASS**, with one anomaly we will not paper over: at the extreme light-apparatus end the visibility runs slightly above the reference curve, inside the bar but consistently, and it replicated on fresh seeds. We named it and carried it forward rather than rounding it away.

## Part E — Two things that are argued, not measured

Two rows are not experiments. They are proofs, checked step by step by machine.

**[CH-18](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test19.md) · The observer's view is forced to be complex.** Physics students always ask why quantum mechanics needs imaginary numbers. This is a partial answer, and only for this kind of observer: given a real, information-preserving view of a steadily turning world with nothing standing still, the structure of that view forces a complex-unitary description. Not chosen for convenience — forced by the geometry.

We should be careful about how much weight this carries. Every step is machine-checked, and there is a scope note on the record: when two rotation rates coincide the uniqueness breaks, and we have an explicit counterexample. More importantly, **the theorem is about a different object than the machine's own three-number state**, which is written complex by hand in the source. We do not lean on it, and this article does not use it to claim the machine invented complex numbers. It did not. **PASS.**

**[CH-19](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test20.md) · Watching is not enough.** This one is the wall that killed many of our earlier ideas, and it is worth more than any pass on the list.

Take a deterministic world. Watch it passively, through a fixed set of questions, changing nothing. Then the outcomes you record can always be arranged into one consistent joint story — and something that admits a consistent joint story can never break the classical bounds that quantum mechanics breaks.

**So passive observation of a deterministic world cannot fake collapse.** The argument is machine-checked and we are convinced by it. Its scope is exactly as stated, and no wider: passive observation, through a *fixed* partition. It says nothing about what an active, state-rewriting observer can do — which is precisely the gap the fold walks through, deliberately.

We met this as a measurement before we had the argument: a passively watched world came out riding the classical limit and never crossing it. **PASS.**

That is why the fold exists. Not because it was elegant — because everything gentler was ruled out.

## The one it failed

**CH-06. Can the dark stripes go arbitrarily dark?**

In an interference pattern the dark bands come from two contributions cancelling. Quantum mechanics allows perfect cancellation: line it up exactly and the darkness is *total*. Zero. And you can approach that zero as closely as you want.

Our machine cannot. Push toward a perfect null and the contrast stops falling. It flattens out at a bit above one percent and stays there. There is always a little light left in the dark.

**Where does that floor come from?** From the same place everything else comes from: the fold rewrites the state from rotor readings, and those readings carry a small, structured leftover. That leftover is about the same size as the one percent we met back in question 1. The floor is not a bug we could patch. It is the price of the mechanism.

So we spent time trying to get under it. Three routes:

**Change the reservoir.** Different pool, different statistics. The floor stayed.

**Change the coordinates.** If the leftover were an artifact of how we set things up, a symmetry transformation should smear it away. We averaged the whole system over a group of twenty-four symmetries. The leftover came back essentially untouched. It is not a bookkeeping artifact.

**Change the architecture.** The last idea: fold in stages instead of all at once. We built it, certified it, and ran the same ladder — and it failed from **the opposite side.** Below a certain depth the staged machine does not floor out. It snaps to exactly zero: not one single event in half a million, where quantum mechanics predicts a small but definite handful. Not too much light in the dark. *No* light at all, where there should be a little.

![cliff or floor](assets/cliff_or_floor.png)
<!-- Counted events. The dashed line is what quantum mechanics does. Neither machine can follow it. -->

So the family has two shapes, and neither one is quantum:

> **Rich folds floor. Sharp folds cut off. Quantum mechanics does neither.**

We call it the **cliff-or-floor dichotomy**, and we want to be careful about its status: it is measured on both sides and named as a conjecture. It is not proved over every possible deterministic measurement machine. Proving it — or finding the machine that escapes it — is the open problem this whole programme now points at.

Here is why we are glad this row says FAIL.

A model that matches everything tells you nothing. This one makes a **prediction that could kill it**: if the world were a machine of this family, interference could not be made arbitrarily dark. It would bottom out around a percent, or drop off a cliff to nothing. Real quantum mechanics does neither, and experiments can look. The failure is the only place in twenty questions where this thing is properly falsifiable, and that makes it the best row on the paper.

## The one we could not finish

**CH-16. Can a pair of observers inside the machine break the classical correlation bound?**

Short answer: not with this machine, and we know why.

**The machine is built around one system.** One state of three numbers, one observer, one fold. Entanglement needs two. We bolted a pair onto the existing machinery and ran the test properly — but in that arrangement each side's measurement only ever sees its own setting, and an arrangement like that is provably local. For a local arrangement the correlation number cannot pass the classical bound. Which is exactly where it landed, with every control behaving: cut the link between the pair and the correlation vanishes, and nothing measured on one side leaks to the other.

So the run did not fail. It confirmed a ceiling we had already proved.

One thing has to be said here, because it is the first objection anyone raises. This is **not** Bell's theorem shutting the door on us. Bell ruled out hidden machinery that is *local* — each particle carrying its own private instructions. The machinery here is global: one shared pool, read by everyone. Bell explicitly leaves that case open, and Bohm's theory has lived in the gap since 1952. Getting past the bound needs the substrate itself to respond to both settings at once — a different machine, not a different test.

So, plainly: **entanglement is the one big quantum behaviour this machine has not reproduced.** It needs a redesign, we have not built it, and it may not work. We have parked it for later in the quest — it is too interesting to fake and too big to bolt on properly.

That is why the row says unfinished rather than failed. The full story, with the numbers and the two supporting experiments, is in [its file](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/tests/test17.md).

## The Confession

Every episode gets one. This one is short.

**We wrote the exam.** Twenty questions we chose, with pass marks we set. Nobody handed us this paper. The rules above are real and you can check them — the file has a changelog, and no bar ever moved the convenient way — but it is still our exam, and you should weigh it as such.

**The questions are not independent.** Several lean on the same single move. So "eighteen out of twenty" is not eighteen separate pieces of evidence. It is closer to a handful of mechanisms, each seen from several angles.

**Twenty questions is not quantum mechanics.** There is no spin here, no identical particles, no fields, no gravity. And there is no *space* either: the interference in these tests happens between two components of a three-number state, with a swept phase standing in for position on the screen. The one row that does need real distance runs in a separate, simpler world built for it. The setup notes in the repository say all of this plainly, test by test, because it is the kind of thing that is easy to gloss over and shouldn't be.

**And every pass is a pass at about one percent** — the machine's own precision. Question 6 is where that one percent stops being a tolerance and becomes a wall.

What we will stand behind is narrow, and we think still worth something: **a fully deterministic machine, with a physical measurement and no quantum formula inside it, reproduced eighteen quantum behaviours at one percent — and where it broke, it broke in a way you can go and measure.**

## What this does NOT claim

> This is a **demonstration**, not a discovery about nature. The scorecard says one family of machines, at one frozen setting, reproduced twenty specific behaviours — it does not say our universe is a clockwork, does not reinterpret quantum mechanics, and does not dodge Bell's theorem, since the hidden machinery here is *global*, not local. Question 16 is unfinished, not won: the certified pair sits exactly on the classical bound, and entanglement remains unreproduced. Question 6 is a confessed failure, and the cliff-or-floor dichotomy is a named conjecture, measured on both sides and proved on neither. Every number behind this piece is at the machine's own precision, about one percent, and every pass means "within that".

## The neighbors and the credits

Test-driven design for physics models is not something we invented — it is software practice pointed at a different target. And the exam itself belongs to the people who thought of the questions. The honest note from episode one still holds: the reading and cross-checking was done mostly by AI, with a human steering.

- **[John Bell](https://cds.cern.ch/record/111654)** (1964) — the theorem behind question 16, and the reason this project targets *global* hidden variables and says so in every episode. **[John Clauser, Michael Horne, Abner Shimony and Richard Holt](https://doi.org/10.1103/PhysRevLett.23.880)** turned it into the testable CHSH form we actually ran.
- **[John Archibald Wheeler](https://en.wikipedia.org/wiki/Wheeler%27s_delayed-choice_experiment)** — the delayed-choice experiment, question 11.
- **[Marlan Scully and Kai Drühl](https://en.wikipedia.org/wiki/Quantum_eraser_experiment)** (1982) — the quantum eraser, question 13.
- **[Berthold-Georg Englert](https://doi.org/10.1103/PhysRevLett.77.2154)** (1996) — the exact visibility-distinguishability relation, question 14.
- **[Avshalom Elitzur and Lev Vaidman](https://arxiv.org/abs/hep-th/9305002)** (1993) — interaction-free measurement, question 12.
- **Sabine Hossenfelder** — her explanation of what the slits themselves are doing is what turned question 17 into a test we could actually run - watch **[video](https://www.youtube.com/watch?v=npc6Mn2CZV8)**.
- **[Andrew Gleason](https://plato.stanford.edu/entries/qt-gleason/)** (1957) — the theorem that makes question 3 load-bearing rather than decorative.
- **[Anthony Leggett and Anupam Garg](https://doi.org/10.1103/PhysRevLett.54.857)** (1985) — the tool for asking whether a system has definite values when nobody is looking; question 19 is a wall built out of it.

And the closest neighbours in spirit, as ever: Gerard 't Hooft's [Cellular Automaton Interpretation](https://arxiv.org/abs/1405.1548), [Bohmian mechanics](https://plato.stanford.edu/entries/qm-bohm/), and Jacob Barandes' [indivisible stochastic processes](https://arxiv.org/abs/2402.16935).

## Run it yourself

Every row on the scorecard has its own file: **[github.com/masteris777/quest-for-entropy-quantum-exam](https://github.com/masteris777/quest-for-entropy-quantum-exam)** — twenty deep dives, `test01.md` through `test20.md`. Each one states **exactly how that test is set up in the toy** — what the "two slits" actually are, where the "speed of light" comes from, what the detector and the apparatus mass are made of — then the pass mark as it was frozen, the protocol, the controls that had to fail, the measured numbers, and the caveats. There is a **[setup guide](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/setup.md)** covering the apparatus in one place, and a **[ledger](https://github.com/masteris777/quest-for-entropy-quantum-exam/blob/main/ledger.md)** of the five times during this exam the machine looked wrong and *we* were wrong — including the one where we nearly published a violation of quantum mechanics that turned out to be our own broken scoring code.

The laboratories' own measurement files ship with it, unedited, and `python verify_scorecard.py` re-reads every number this article rests on and fails loudly if one has drifted. The machine itself rebuilds from scratch in two seconds in the [previous episode's repository](https://github.com/masteris777/quest-for-entropy-the-machine). And you can still poke it in the browser: **[run the machine](https://quest-for-entropy.web.app/the-machine)**, or **[watch the fold kill the stripes](https://quest-for-entropy.web.app/stripes-die)** — that one is question 8, live.

## How this was made

I'm a software architect. The physics and the deep math are what I'm curious about, not my job, and I use AI to explore them. The honest split: the heavy lifting — the math, the physics checks, the code, the sums — is AI, with me setting the direction, asking the questions, and making the calls. Main models: Anthropic Fable 5, Opus 5 and Sonnet 5, with support from DeepSeek v4 Pro. To keep us honest, the work runs through a harness I built: every experiment follows rules fixed in advance, results get challenged by independent AI review, and every mistake we catch goes into a public honesty ledger — the five from this exam are in the repository, with numbers. Every number here comes from code you can run, not from a model's memory.

## Next time

Episode four: **it started with a break shot.** Long before any of this, I was watching balls scatter on a pool table and wondering how far ahead anyone could really predict them. That question turned out to have a sharp answer, and the answer is why chaos — the obvious candidate for making a quantum-looking world — is the first machine in the graveyard.

---

*Quest for Entropy is written by Marijus Masteika. Entropy was always the dark horse for me — connected to information, and maybe hiding answers to everything. That's the quest.*
