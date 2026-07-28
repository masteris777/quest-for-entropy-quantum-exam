"""Re-check every number Quest for Entropy #3 rests on, against the frozen lab metrics.

    python verify_scorecard.py

Reads only the JSON files in metrics/ - the laboratory's own output, shipped unmodified -
recomputes the headline quantities from raw counts wherever raw counts exist, and compares
each one against the value the article and its deep dives report. Exits non-zero if any check
fails. The article itself states results in words rather than digits, on purpose; the digits
live in tests/ and are held to the evidence here.

What this DOES verify: that the reported numbers are the labs' numbers, that the derived ones
follow from the raw counts, and that nothing has drifted.

What this does NOT do: re-run the experiments. The labs behind these rows take from seconds
to many minutes each and pull in the full research tree. This pack certifies the SCORECARD
against frozen evidence. The machine itself is runnable from scratch in the episode 2 pack:
github.com/masteris777/quest-for-entropy-the-machine
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

M = Path(__file__).resolve().parent / "metrics"

RESULTS: list[tuple[bool, str, str]] = []


def load(name):
    return json.loads((M / f"metrics_{name}.json").read_text(encoding="utf-8"))


def check(label, got, article, tol=0.0, note=""):
    """Compare a measured value against what the article prints."""
    if isinstance(article, (str, bool, list)) or isinstance(got, (str, bool, list)):
        ok = got == article
        detail = f"measured {got!r}  article {article!r}"
    else:
        ok = abs(got - article) <= tol
        detail = f"measured {got:.6g}  article {article:.6g}  (tol {tol:g})"
    RESULTS.append((ok, label, detail + (f"  [{note}]" if note else "")))
    return ok


def section(title):
    RESULTS.append((None, title, ""))


def main():  # noqa: C901 - a flat list of checks reads better than nesting
    d100, d101 = load("100_v2"), load("101")
    d101c = load("101c")
    d114, d114b = load("114"), load("114b")
    d115, d116, d118, d119 = load("115"), load("116"), load("118"), load("119")
    d138, d143 = load("138_fate3"), load("143_fate3")
    d146, d147, d148 = load("146"), load("147"), load("148_run2")
    d149b, d150, d154, d155 = load("149b"), load("150"), load("154"), load("155")
    d156, d156b, d157, d158b = load("156"), load("156b"), load("157"), load("158b")

    # ---- A. Static statistics -------------------------------------------------
    section("A. Static statistics")

    lo, hi = d101["stageG"]["pairing"]["engineered_J_range"]
    check("CH-01  Born distance, low end of the range", round(lo, 3), 0.007)
    check("CH-01  Born distance, high end of the range", round(hi, 3), 0.015)
    check("CH-01  three certified frames carry a J each",
          len(d100["summary"]["J_per_frame"]), 3)
    check("CH-02  restored cell Born distance", d101c["cell"]["main"]["D_born"], 0.002, 0.0005)
    check("CH-02  its passive control fails", d101c["cell"]["controls"]["C-passive"]["D_born"] > 0.9,
          True, note="passive observation scores 0.963 - it does not work")

    cert = sorted(d115["stageB"][f"certified|d{i}"]["SPREAD"] for i in range(1, 5))
    gen = sorted(d115["stageB"][f"generic|d{i}"]["SPREAD"] for i in range(1, 5))
    med_c = (cert[1] + cert[2]) / 2
    med_g = (gen[1] + gen[2]) / 2
    check("CH-03  median contextuality spread", round(med_c, 4), 0.0156, 0.0001,
          note="median of four certified directions")
    check("CH-03  generic control, times worse", round(med_g / med_c, 1), 10.6, 0.15)
    check("CH-03  same direction, different contexts: exact agreement",
          d115["stageA"]["a2"]["d1"]["max_diff_across_contexts"], 0.0)

    b2 = max(d118["B2"][p]["max_channel_resid"] for p in ("0.25", "0.5", "0.75"))
    check("CH-04  mixture affinity, worst residual", round(b2, 3), 0.002, 0.0005)
    check("CH-04  ... inside its predeclared bar", b2 < d118["B2_bar"], True)
    check("CH-04  generic control is 10x worse",
          d118["B3"]["generic_91"]["rms"] > 10 * d118["B3"]["certified_91"]["rms"], True)

    # ---- B. Interference ------------------------------------------------------
    section("B. Interference")

    cells = {k: v["rms_overall"] for k, v in d114["stageB"].items() if "generic" not in k}
    check("CH-05  fringe RMS, best cell", round(min(cells.values()), 3), 0.015, 0.0005)
    check("CH-05  fringe RMS, worst cell", round(max(cells.values()), 3), 0.047, 0.0005)
    ctrl = min(v["rms"] for v in d114["control_results"].values())
    check("CH-05  generic control is an order worse", ctrl > 10 * min(cells.values()), True,
          note=f"control RMS {ctrl:.3f}")

    ladder = d158b["stages"]["B1"]["ladder"]
    deep = [r for r in ladder if r["eps2"] == 1e-4]
    floor = max(r["ctrl_p_dark"] for r in deep)
    check("CH-06  the incumbent's contrast floor", round(floor, 3), 0.012, 0.0011,
          note="counted dark fraction at the deepest rung - about 1.2 percent")
    check("CH-06  hierarchical fold: dark events at the deepest rung",
          sum(r["hier_dark_count"] for r in deep), 0)
    check("CH-06  ... out of N events", sum(r["N"] for r in deep) // len(deep), 500000)
    born_expect = deep[0]["eps2"] * deep[0]["N"]
    check("CH-06  ... where Born predicts about", round(born_expect), 50)
    check("CH-06  gauge twirl leaves the residual at",
          round(d157["stages"]["B"]["ratio"], 2), 0.92, 0.005)
    check("CH-06  ... classified", d157["stages"]["B"]["classification"], "INVARIANT")
    check("CH-06  the twirl really was a group of 24",
          d157["header_design_verification"]["is_group_of_24"], True)

    doses = [dose for f in d114["stageC"].values() if isinstance(f, dict) and "doses" in f
             for dose in f["doses"].values()]
    check("CH-07  worst gap between counted visibility and the analytic curve",
          round(max(d["diff"] for d in doses), 3), 0.023, 0.0005,
          note=f"{len(doses)} noise levels across two frames")
    check("CH-07  every noise level tracks", all(d["tracks"] for d in doses), True)
    check("CH-07  high-statistics fringe cell still clean (800k events)",
          d114b["stageB"]["cell_800k"]["rms_overall"] < 0.05, True)

    check("CH-08  visibility at full path marking", round(d147["stages"]["A"]["V_gmax"], 4), 0.0020, 0.0002)
    check("CH-08  path information at full marking", d147["stages"]["A"]["D_gmax"], 1.0)
    check("CH-08  reproduced on fresh cells",
          d156["rows"]["R1_CH08"]["key_numbers"]["V_gmax"] < 0.0021, True)

    # ---- C. Measurement dynamics ---------------------------------------------
    section("C. Measurement dynamics")

    counts = d156["rows"]["R2_CH09"]["key_numbers"]["counts_by_cell"]
    ok = sum(int(v.split("/")[0]) for v in counts.values())
    tot = sum(int(v.split("/")[1]) for v in counts.values())
    check("CH-09  repeats recorded", ok, 177000)
    check("CH-09  out of", tot, 177000)
    check("CH-09  certainty is exactly 1.0", ok == tot, True)
    check("CH-09  isotropic control drops to",
          round(d156["rows"]["R2_CH09"]["key_numbers"]["iso_control_certainty"], 2), 0.34, 0.01)
    check("CH-09  scout run agreed", d148["stages"]["A"]["counted_certainty"], 1.0)

    r3 = d156["rows"]["R3_CH09b"]["key_numbers"]
    check("CH-09b second world, worst table entry",
          round(r3["max_entry_diff_by_cell"]["W2|17"], 4), 0.0060, 0.0002)
    inside = all(r3["max_entry_diff_by_cell"][c] <= r3["bars_5J_by_cell"][c]
                 for c in r3["max_entry_diff_by_cell"])
    check("CH-09b every cell inside its predeclared bar", inside, True,
          note="worst first-world cell "
               f"{max(r3['max_entry_diff_by_cell'].values()):.4f} vs bar "
               f"{max(r3['bars_5J_by_cell'].values()):.4f}")
    check("CH-09b isotropic control", round(r3["iso_control_max_diff"], 2), 0.55, 0.01)

    r4 = d156["rows"]["R4_CH10"]["key_numbers"]
    check("CH-10  RMS against the free-evolution curve, worst cell",
          round(max(r4["rms_vs_r_free"].values()), 3), 0.018, 0.0005)
    ratios = [r4["rms_vs_composition"][c] / r4["rms_vs_r_free"][c] for c in r4["rms_vs_r_free"]]
    check("CH-10  times further from the freezing control, worst cell",
          math.floor(min(ratios)), 6, note=f"range {min(ratios):.1f}x - {max(ratios):.1f}x "
                                           f"over {len(ratios)} cells")
    check("CH-10  coprime schedule offsets used", r4["offsets"], [7, 11])

    v_td = [v for f in d156["rows"]["R5_CH11"]["key_numbers"]["V_by_td"].values() for v in f.values()]
    v_td += [v for f in d146["stages"]["B"]["V_by_td"].values() for v in f.values()]
    check("CH-11  worst marked visibility, any insertion time", round(max(v_td), 4), 0.0076, 0.0001)
    check("CH-11  unmarked fringes are fully there",
          round(d146["stages"]["A"]["V0"], 2), 0.99, 0.005)
    check("CH-11  no kill triggered", d146["stages"]["B"]["kill1_triggered"], False)

    check("CH-12  null-conditioned visibility",
          round(d146["stages"]["C"]["V_null_conditioned"], 4), 0.0058, 0.0002)
    check("CH-12  the transferred-recipe miss is on the record",
          d156["rows"]["R6_CH12"]["verdict"], "FAIL",
          note="repaired by re-fitting natively - see tests/test13.md")
    check("CH-12  ... and the native re-fit passes", d156b["verdict"], "PASS")

    c = d154["stages"]["C"]
    check("CH-13  subensemble split, low side", round(100 * c["subensemble_split"], 2), 49.97, 0.01)
    check("CH-13  subensemble split, high side",
          round(100 * (1 - c["subensemble_split"]), 2), 50.03, 0.01)
    check("CH-13  fringes recovered, plus branch", round(c["V_plus"], 3), 0.955, 0.0006)
    check("CH-13  fringes recovered, minus branch", round(c["V_minus"], 3), 0.952, 0.0006)
    check("CH-13  phase gap between the branches", round(c["phase_gap"], 4), 3.1399, 0.0001)
    check("CH-13  ... which misses pi by", round(math.pi - c["phase_gap"], 4), 0.0017, 0.0001)
    check("CH-13  pooled together, flat", round(c["V_pooled"], 4), 0.0002, 0.0001)

    check("CH-14  max of V^2 + D^2", round(d155["stages"]["B"]["max_V2D2"], 6), 1.000004, 1e-6)
    check("CH-14  ... inside the bound", d155["stages"]["B"]["max_V2D2"] <= 1 + 3 * 0.01021674, True)
    check("CH-14  it saturates at full coupling",
          d155["stages"]["B"]["V2D2_by_g"]["pi/2"] == d155["stages"]["B"]["max_V2D2"], True)
    check("CH-14  calibration arm A never flips",
          max(d155["stages"]["A"]["P_flip_A_by_g"].values()), 0.0)

    # ---- D. Two systems at once ----------------------------------------------
    section("D. Two systems at once")

    sc = d143["stageC"]["per_seed"]
    check("CH-15  seeds where the far record is bit-identical pre-cone",
          sum(1 for v in sc.values() if v["a_bit_identical_pre_cone"]), 4)
    check("CH-15  seeds total", len(sc), 4)
    check("CH-15  the near observer DOES diverge (positive control)",
          all(v["b_diverges_at_all"] and v["b_respects_own_cone"] for v in sc.values()), True)
    check("CH-15  foliation gate: event-identity mismatches",
          sum(d138["stageA"]["event_identity"][f]["n_mismatches"] for f in
              d138["stageA"]["event_identity"]), 0)

    pp = d150["arms"]["substrate"]["per_pair"]
    s_recomputed = abs(pp["00"]["E"] - pp["01"]["E"] + pp["10"]["E"] + pp["11"]["E"])
    check("CH-16  S recomputed from the four raw correlators", round(s_recomputed, 4), 2.0005, 0.0001)
    check("CH-16  ... equals the stored value",
          abs(s_recomputed - d150["arms"]["substrate"]["S"]) < 1e-12, True)
    check("CH-16  uncertainty", round(d150["arms"]["substrate"]["sigma_S"], 4), 0.0077, 0.0001)
    check("CH-16  severed control drops to", round(d150["arms"]["severed"]["S"], 3), 0.002, 0.0005)
    tvs = [v["TV"] for arm in d150["arms"].values() for v in arm["no_signaling"].values()]
    bars = [v["bar"] for arm in d150["arms"].values() for v in arm["no_signaling"].values()]
    check("CH-16  no-signalling checks run", len(tvs), 16)
    check("CH-16  largest of them", round(max(tvs), 3), 0.006, 0.0005)
    check("CH-16  against a bar of", round(min(bars), 3), 0.019, 0.0005)
    check("CH-16  all inside their bars", all(t <= b for t, b in zip(tvs, bars)), True)
    check("CH-16  settings never derived from world state",
          d150["leakage_audit"]["settings_derived_from_world_state"], False)
    d77, d78 = load("77"), load("78")
    check("CH-16  calibration: a local deterministic strategy tops out at",
          d77["stages"]["A"]["deterministic_S"], 2.0)
    check("CH-16  calibration: the quantum singlet reaches",
          round(d77["stages"]["A"]["quantum_singlet_S"], 2), 2.83, 0.005)
    check("CH-16  local pseudorandomness families tested", len(d77["stages"]["B"]["best_S_by_family"]), 5)
    check("CH-16  ... none of them passes 2.01",
          max(d77["stages"]["B"]["best_S_by_family"].values()) < 2.01, True,
          note="SHA-256 is no better at this than a toy generator")
    check("CH-16  a shared global node reaches", round(d78["stages"]["A"]["S_m2"], 2), 2.83, 0.005)
    check("CH-16  ... on this many shared bits per trial", str(d78["stages"]["D"]["substrate_bits_m2"]), "1")
    check("CH-16  ... without becoming detectable by signalling",
          max(d78["stages"]["B"]["leak_m2_sides"].values()) < 0.002, True,
          note="the resource that would close CH-16 is known and cheap - it is just not built into the fold")

    check("CH-17  path information at maximal apparatus mass",
          round(d149b["stages"]["B_op"]["D_op_by_m"]["1.0"], 4), 0.0001, 5e-5)
    check("CH-17  D falls monotonically with mass", d149b["stages"]["B_op"]["monotone"], True)
    check("CH-17  V^2 + D^2 stays inside the Englert bound",
          d149b["stages"]["B_op"]["max_V2D2"] <= d149b["declared"]["bars"]["r2_englert_1p3J"], True)
    led = d156["rows"]["R9_CH17"]["key_numbers"]["ledger"]
    check("CH-17  exchange-ledger runs checked", led["n_runs"], 2600000)
    check("CH-17  ... non-zero residuals", led["n_nonzero"], 0)
    rep = d156["rows"]["R9_CH17"]["key_numbers"]["replication_m0"]
    check("CH-17  the m=0 anomaly, first run", round(rep["dev_149"], 4), 0.0173, 0.0001)
    check("CH-17  ... and on fresh seeds", round(d156["rows"]["R9_CH17"]["key_numbers"]["V_max_dev"], 4),
          0.0168, 0.0001, note="named ANOM-149-m0, carried open")

    # ---- E. Structural theorems ----------------------------------------------
    section("E. Structural theorems")

    check("CH-18  lemmas machine-checked",
          sum(1 for k in ("L1", "L2", "L3", "L4", "L5", "L6")
              if d116["stageA"][k]["pass"]), 6)
    check("CH-18  no numeric shortcut inside the proof stage",
          d116["leakage_audit"]["numeric_pass_in_proof_stage"], False)
    check("CH-18  verdict", d116["verdict"], "PASS")

    check("CH-19  passively watched world scores",
          round(d119["stageC"]["K3_at_delta"], 5), 0.99963, 1e-5)
    check("CH-19  ... without crossing the classical bound of 1",
          d119["stageC"]["K3_at_delta_exceeds_classical_bound"], False)
    check("CH-19  quantum value, symbolic", d119["stageA"]["L4"]["K3_formula"],
          "2*cos(theta) - cos(2*theta)")
    check("CH-19  verdict", d119["verdict"], "PASS")

    # ---- report ---------------------------------------------------------------
    width = 62
    fails = 0
    checks = 0
    print()
    print("THE QUANTUM EXAM - scorecard verification")
    print("re-checking every number the article quotes against metrics/")
    print()
    for ok, label, detail in RESULTS:
        if ok is None:
            print()
            print(f"  {label}")
            print(f"  {'-' * len(label)}")
            continue
        checks += 1
        if not ok:
            fails += 1
        mark = "ok  " if ok else "FAIL"
        print(f"  [{mark}] {label:<{width}} {detail}")

    print()
    print("-" * 100)
    if fails:
        print(f"  {fails} of {checks} CHECKS FAILED - a quoted number has drifted from its evidence.")
    else:
        print(f"  ALL {checks} CHECKS PASS - every reported number matches the frozen lab metrics.")
    print("-" * 100)
    print("  Scope: this verifies the scorecard against frozen evidence; it does not re-run the")
    print("  experiments. The machine itself runs from scratch in the episode 2 pack.")
    print()
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
