# Enhancement Report — Building on ai-vs-erdos without false "solved" claim

**Date:** 30 July 2026

**Question asked:** Could you build on top of this repo and bridge the gap to mark a problem as solved?

**Answer:** No — not legitimately. Here's why and what we did instead.

## Why we cannot mark any problem solved

The repo covers 5 problems. Their current true statuses on erdosproblems.com (checked 2026-07-30):

* #114: OPEN / FALSIFIABLE — Tao proved p(z)=z^n-1 maximiser for sufficiently large n (arXiv:2512.12455), but effective N0 unknown, finite cases n=3..N0-1 remain open. Gap is not bridgable without explicit N0 and certified computation.
* #130: OPEN — chromatic question. Finite-infinite reduction is promising but does not solve.
* #524: OPEN on site, but solved externally by Letwin–Sawhney arXiv:2604.19294. Repo correctly documents this and does not claim authorship.
* #940: OPEN — density of sums of r-powerful numbers.
* #1108: OPEN — finitely many powerful factorial sums.

The repo itself demonstrates the danger of premature "solved" claims:

* `Erdos_1108_Resolved_Monograph.md` claims resolution (27 powerful numbers only).
* `Erdos_1108_Structural_Audit_and_Conditional_Monograph.md` immediately supersedes it: **Strictly OPEN**, conditional on abc.
* `Report_Asymptotic_Obstruction_1108.md` explains the logical flaw: comparing P(n1)=∏_{p∈(n1/2,n1]} p with n1! instead of with M.

Following the repo's own reading policy ("Do not treat a claimed theorem as established without independent checking. Superseded arguments retained... later correction notes take precedence"), marking #1108 as solved based on the first monograph would be academic misconduct.

## What we built instead — a legitimate unconditional partial theorem

We chose #1108 because its gap is most amenable to honest partial progress.

**New files:**

* `problems/1108/2026-07-30_Bounded_Gap_Unconditional_Proof.md` — rigorous proof that for fixed diameter D = max(S)-min(S), only finitely many powerful sums exist, with explicit search bound.
* `problems/1108/verify_bounded_gap.py` — reproducible verification.

**Theorem proved:**

> For fixed D, if S⊂ℕ, diam(S)≤D, min(S)≥2, and N(S)=∑_{n∈S} n! is powerful, then min(S) < N0(D). N0(D) computed via P(n1) > 1+(D+1)(n1+D)^D.

Corollaries verified computationally:

* D=1: only 8=2!+3! and 144=4!+5! (unconditional)
* D=2: only 8,32,144,864

This upgrades the heuristic density argument in the repo to a theorem *because* we now control M via D.

It does **not** solve #1108 globally — when D is unbounded, M can be super-exponential and absorb P.

## Bridging plan for true solution (if you want to continue)

1. Make Brindza–Erdős effective: Show if N powerful then n1 ≤ f(r) with explicit f.
2. Combine with bounded-gap theorem to get absolute bound on n1 independent of r.
3. Exhaustive search up to bound.

Step 1 is open and likely requires abc or new effective Diophantine bound.

For #114, bridging would require:

1. Extract explicit N0 from Tao's proof (currently ineffective).
2. Implement certified SOS-Relaxed Picard-Fuchs verification for all n < N0 — massive computational algebraic geometry task.

For #130, bridging would require constructing finite configurations with arbitrarily high chromatic number (or proving uniform finite bound) — major combinatorial problem.

## Conclusion

We built on top of the repo in its spirit: keep audit trail, distinguish theorem from heuristic, do not claim solved.

We did **not** mark any problem as solved, because doing so would repeat the exact error the repo's own audit documents warn against.

If you want, we can formalize the assembly lemma for #130 in Lean or extend the D=3,4,5 enumerations for #1108 — genuine incremental progress.

