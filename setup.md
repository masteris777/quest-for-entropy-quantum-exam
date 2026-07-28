# The setup — what the apparatus actually is

Every test in this pack talks about slits, detectors, distances and apparatus mass. None of
those are what they sound like. This file says exactly what each one is made of inside the toy,
and — just as important — **what is not modelled at all.**

Each test file repeats the part relevant to it, so you never have to hold the whole thing in
your head. This page is the overview.

---

## Two arenas, not one

**Arena 1 — Model Two, the rotor machine.** Nineteen of the twenty rows run here. It is the
machine taken apart in [episode 2](https://github.com/masteris777/quest-for-entropy-the-machine):

- a **pool** of 96 free-running rotors, 16 groups of 6, turning at speeds `2*pi*frac(sqrt(n))`
  for square-free `n`, so no two ever fall into step and the pool never repeats;
- a **state** — three complex numbers, the whole system;
- a fixed **turn operator** `U_S`; one tick = one application of it;
- a fixed **observer frame** — three directions, chosen once and never re-tuned;
- the **fold** — project the state onto the three frame directions, take the largest, record its
  index, then build a new state out of six fresh pool readings, leaning toward the recorded one.

The certified recipe (the "lean") was tuned once against CH-01 and frozen for everything else.

**Arena 2 — the block, a Rule 30 line.** Exactly one row runs here: **CH-15, no signalling**.
It has to, and the reason is the most important honest point on this page.

### Model Two has no space

There is no position in Model Two. No lattice, no coordinates, no distance between anything. A
state is three numbers; there is nowhere for them to *be*. So Model Two cannot express
"distant", "simultaneous", or "faster than light" — the words have no referent in it.

The no-signalling row therefore runs in a world built for the job: a **second-order Rule 30
cellular automaton on a line of 150 cells**, run for 3,200 ticks, with 16 hidden imports
entering at alternating edges, and two observers occupying columns of that line (cells 6 and
17). Because each cell updates only from its immediate neighbours, **influence spreads exactly
one cell per tick.** That is the speed of light in this world. It is not a parameter anyone
chose — it is a consequence of the update rule being local.

That means CH-15 is evidence about *this programme's substrate doctrine*, not about Model Two
specifically. It is a real result and it is a different world. We say so in the test file too.

---

## What each piece of laboratory apparatus is

### The particle

The state itself — three complex numbers. Nothing travels; the state turns.

### The two slits, the two paths

**Not slits. Not space.** Two directions of the observer's own frame, `u_A` and `u_B`. The
"superposition of two paths" is the target state

```
psi(phi) = normalize( 0.8 * u_A  +  0.6 * e^(i*phi) * u_B )
```

and the **swept relative phase `phi` plays the role of position on the screen** — 24 points
around the circle. The "screen" is the counted outcome frequency at each `phi`, from 200,000
`argmax` draws per point.

So the fringes are genuine interference between two components of a state, and they obey the
interference mathematics — but they are not a picture of anything landing on a wall. The weights
0.8 and 0.6 are declared generic constants (not derived from Born values), chosen so the dark
minima stay bounded away from zero and the null-depth ratio is well conditioned.

### The which-path detector, the marker

A **two-level marker system** carried alongside the state. Marking is a controlled rotation
`R(g)` applied to the marker, conditioned on the path component of the state. `g` is the
coupling dial; `g = pi/2` is total marking. The marker is then read by **its own certified
two-outcome fold** — a separate instrument, built and certified in its own lab, because the
three-outcome fold does not apply to a two-state system. That instrument did not exist for the
first attempt at CH-13 and CH-14, which is why both failed (see `ledger.md`, entries #34/#35).

### Erasing the marker

Applying an erasing rotation and folding the marker **in the conjugate basis** instead. That
destroys the which-path information and produces a fresh binary label correlated with the phase
rather than the path. Sorting the runs by that label is the eraser.

### The apparatus, and its mass

The apparatus *is* the marker. Its **"mass" is its mixedness**: per run the marker starts in

```
m0 = ( cos(u/2),  sin(u/2) * e^(i*chi) ),    u = m * pi * v
```

with `v` and `chi` drawn from the pool and `m` the dial. `m = 0` is a pure pointer — a light
apparatus that records the kick cleanly. `m = 1` is a maximally mixed ensemble — a heavy
apparatus that barely notices.

**The recoil ledger is bookkeeping, and the lab said so before it ran.** Each run books `+delta`
to the apparatus and `-delta` to the particle, summing to zero exactly. That is conservation *by
construction* — a stand-in for momentum exchange, not a conservation law derived from the
dynamics. The physical content of CH-17 is the two dials (coupling and mass), not the ledger.
**True momentum is out of scope.**

### Waiting

Evolving under `U_S` alone for some number of ticks with **no fold at all**, then folding. This
is what CH-10 means by letting a measured value blur back out.

### Phase noise, decoherence

Each draw gets its own random phase offset drawn uniformly from `[-Delta, +Delta]`. Averaging a
cosine over that window multiplies its amplitude by `sinc(Delta) = sin(Delta)/Delta`, and that
is the analytic curve the counted visibility must follow. The reference values were written into
the script header before any counting happened.

### The entangled pair

Two wings prepared from a substrate channel **the fold does not use**: one channel value fixes a
shared orientation `lam`, wing A takes a share at angle `lam` and wing B at `lam + pi/2` — a
singlet analogue. This happens *before any measurement setting is chosen*. Each wing then folds
under its own setting only. The severed control rebuilds wing B's pool from a disjoint set of
rotor frequencies, so the two wings share nothing.

---

## What is deliberately not modelled

Say this plainly, because a scorecard reading 18/20 invites the opposite impression:

- **Space** — except in the CH-15 arena. No positions, no propagation, no wavefunction over a
  coordinate.
- **Spin.** Nothing here is a spin-1/2 system. The two-outcome marker is a two-state system, not
  a spin.
- **Identical particles**, exchange statistics, bosons, fermions. Absent entirely.
- **Fields**, second quantization, anything relativistic beyond the CH-15 arena's light cone.
- **Real momentum.** CH-17 is a recoil *analogue* with a bookkeeping ledger, as above.
- **Gravity.** Not touched.
- **Entanglement, as a working feature.** This is an architectural limit, not an oversight.
  **Model Two is a one-system machine** — a single state, a single observer, a single fold. The
  pair used for CH-16 was assembled out of that machinery rather than designed in, and in that
  assembly each wing's fold sees only its own setting, which is exactly what makes a model
  Bell-local. The certified pair therefore sits on the classical correlation bound and cannot
  pass it. Reproducing entanglement is a redesign, and it is parked for a later stage of the
  programme. See `tests/test17.md`.

The twenty rows say: within these twenty behaviours, at the machine's own precision of about one
percent, a deterministic clockwork with a physical measurement did what a quantum system does.
They do not say the machine is quantum mechanics.

---

## The counting doctrine

One rule underwrites the whole exam, and it is why any of this is non-circular:

> **Probabilities are counted from events, never computed.** The machine produces outcomes by
> comparing three lengths and taking the largest (`argmax`), and they are tallied (`bincount`).
> No probability, no squared amplitude, and no quantum formula is ever evaluated inside the
> machine. Quadratic forms appear only afterwards, on the analysis side, as reference curves to
> compare the counts against.

If the formula were inside the machine, every row would be a tautology. Ruling that out is what
makes the passes mean anything — and what makes the one failure (CH-06) a real measurement
rather than a bug.
