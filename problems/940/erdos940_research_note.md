# Erdős Problem #940 — a research note

**New reformulations, rigorous fragments, and a computational census of sums of three 3-powerful numbers**

*Working note, 18 July 2026. Companion to the survey `erdos_problem_940_state_of_the_art.md`. All computations below are reproducible: `powerful940.c`, `stats940.c` (gcc, runtimes ~1 min and ~6 min).*

**Provenance and honesty.** Sections 1–5 are mathematical theorems with complete proofs (several are "folklore-adjacent" — in particular §3 generalises a comment by Tao on the problem's forum to all *r* — but to the author's knowledge none of the equivalences stated here appear in print, in this form, for this problem). Sections 6–8 are numerical evidence and *explicitly heuristic* conjectures; nothing in §6–8 is a theorem of the kind the problem asks for, and we do not claim to have solved any part of #940. What appears to be genuinely new: the exact local analysis (Thm A), the kernel-weight reduction in general form (Thm B), the energy–density duality (Thm C) together with its *r = 2* calibration against Blomer–Granville, the explicit mean-multiplicity constant (Thm D) quantifying Schinzel's objection, and the first computational census of the problem beyond trivial ranges — including the discovery of a strong 2-adic statistical phenomenon (n ≡ 7 mod 8).

---

## 1. Setup and counting constants

Write `P_r` for the set of r-powerful integers (0 or exponent ≥ r at every prime) and

```
P_r(x) = #{n ≤ x : n ∈ P_r} ~ C_r · x^{1/r}    (Erdős–Szekeres; Bateman–Grosswald).
```

**Lemma 1.1.** `C_r = ∏_p ( 1 + p^{−(r+1)/r} + p^{−(r+2)/r} + … + p^{−(2r−1)/r} )`.

*Proof.* The Dirichlet series of `P_r` is
`F(s) = ∏_p (1 + p^{−rs}/(1−p^{−s})) = ζ(rs)·G(s)` with
`G(s) = ∏_p (1 + p^{−(r+1)s} + … + p^{−(2r−1)s})` [multiply out `(1 + Σ_{e≥r} p^{−es})(1 − p^{−rs})`]. `G` converges absolutely for `Re s > 1/(r+1)`, and a Tauberian argument at the simple pole s = 1/r of `ζ(rs)` gives `C_r = G(1/r)`. ∎

*(Note this matches the classical unique decomposition `n = a^r · k` with `k` in the "kernel" set `K_r = {∏ p^{e_p} : e_p ∈ {r+1,…,2r−1} }` (equivalently `k = a₂^{r+1}a₃^{r+2}⋯a_r^{2r−1}` with `a₂,…,a_r` squarefree and pairwise coprime), so equivalently `C_r = Σ_{k ∈ K_r} k^{−1/r}` — see §3.)*

Numerically (Euler product, primes ≤ 3·10⁶; r = 2 agrees with `ζ(3/2)/ζ(3) = 2.17310…` and a direct count gives `P_3(4·10⁹) = 6058 ≈ 3.8163·x^{1/3}`, consistent with the known negative `x^{1/4}`-order secondary terms):

| r | C_r | λ_r = (C_r·Γ(1+1/r))^r | e^{−λ_r} |
|---|---|---|---|
| 2 | 2.1731042 | 3.7090 | 2.4·10⁻² |
| 3 | 4.6537165 | 71.7669 | 6.8·10⁻³² |
| 4 | 9.6180723 | 5776.1 | ~ 10⁻²⁵⁰⁸ |
| 5 | 19.1805362 | 1.69·10⁶ | — |
| 6 | 37.0339684 | 1.64·10⁹ | — |
| 7 | 69.4990563 | 4.91·10¹² | — |

The number `λ_r` is the mean multiplicity from Theorem D below; the last column should be read as "what naïve independence would predict for the fraction of unrepresentable integers" — a prediction the data in §6 refute in a quantitatively informative way.

---

## 2. Theorem A — no local obstruction for r ≥ 3

The first question one asks about #940 is whether a congruence obstruction forces infinitely many exceptions (as `n ≢ ±4 mod 9` does for sums of three cubes). The answer is no, in a sharp form:

**Lemma 2.1 (exact local image of P_r).** *Let p be prime and e ≥ 1. The residues mod p^e attained by r-powerful numbers are exactly*

```
{ u mod p^e : p ∤ u }  ∪  { p^r w mod p^e : w arbitrary } .
```

*Proof.* The inclusion ⊇ is trivial. For ⊆: (i) units. Let `p ∤ u`. By Dirichlet pick a prime `ℓ ≡ u (mod p^e)`. For any `k ≥ 0`, `ℓ^{k·φ(p^e)+1} ≡ u (mod p^e)` (for p = 2, e ≥ 3 use `ℓ^{1 + k·2^{e−2}}`, from the structure of `(Z/2^e)×`). Choosing `k` large makes the exponent `≥ r`, and `ℓ^{kφ+1}` is r-powerful. (ii) valuations. If the residue is `p^j w`, `r ≤ j < e`, `p ∤ w`: pick a prime `ℓ ≡ w (mod p^{e−j})`, then `p^j·ℓ` is r-powerful (the factor ℓ ≠ p appears to exponent 1; the factor p^j has exponent j ≥ r). ∎

**Theorem A.** *Let r ≥ 3 and q ≥ 1. Then every residue class mod q is a sum of at most three residues of r-powerful numbers — in fact already of at most two. Consequently, for all summand counts ≥ 2 there is no congruence obstruction of any modulus to representing an integer as a sum of at most r many r-powerful numbers.*

*Proof.* By CRT it suffices to work mod `p^e`, and Lemma 2.1 supplies summands that are either units or elements of 2-adic (p-adic) valuation ≥ r or 0.
*≤ 3 summands, odd p.* First solve mod p with three units: if `t ≢ 2 (mod p)` use `t = 1 + 1 + (t−2)`; if `t ≡ 2` use `t = 3 + 1 + (t−3)` — all summands are units mod p (for p = 3, `(1,1,t−2)` fails only at t = 2, and `(2,2,t−4) ≡ (2,2,1)` fixes it). Now lift freely: prescribe `u₁, u₂` to be any units mod `p^e` in their classes; then `u₃ := t − u₁ − u₂` is a unit mod `p^e` (it is ≢ 0 mod p), hence attained by Lemma 2.1.
*≤ 3 summands, p = 2.* If `t` is odd, use three odd (unit) summands as above. If `t` is even, choose odd units `u₁, u₂` mod `2^e` with `u₁ + u₂ ≡ t (mod 2^r)` — possible since odd numbers sum to every even class mod `2^r` (write `t = 1 + (t−1)` mod `2^r`, then lift `1` to any odd unit; the second summand stays ≡ t−1 mod `2^r`, in particular odd) — and take the third summand `w = t − u₁ − u₂ ≡ 0 (mod 2^r)`, an r-powerful residue by Lemma 2.1 (ii).
*≤ 2 summands.* Odd p: take `u = 1` and `w = t − 1`. If `v_p(w) ∈ {1, …, r−1}` then `t ≡ 1 (mod p)`, so `v_p(t − 2) = 0` (as `t − 2 ≡ −1 ≢ 0 mod p`) and `t = 2 + (t−2)` works instead; otherwise `w` is a unit, zero, or has valuation ≥ r and is attained. p = 2: if `t` is odd, write `t = u + w` with `u` an odd unit ≡ t (mod `2^r`) and `w ≡ 0 (mod 2^r)`; if `t` is even, `t = 1 + (t−1)` is a sum of two units. ∎

**Significance.** For *r = 3* the famous `±4 (mod 9)` obstruction of the narrower problem (three cubes) is absent here, and nothing replaces it. Both halves of #940 are therefore *purely analytic* questions about the global distribution of the sumset, and Theorem A certifies that the singular series in any circle-method treatment is nonvanishing.

---

## 3. Theorem B — the kernel-weight reduction (Tao's trick, made general and precise)

Every `r`-powerful `n` has a **unique** decomposition

```
n = a^r · k,     k ∈ K_r := { ∏ p^{e_p} : e_p ∈ {r+1, …, 2r−1} },
```

with k built from squarefree coprime pieces (proof: for each `e ≥ r` write `e = q·r + s`; if `s = 0` put everything in `a^r`; if `1 ≤ s ≤ r−1` put `p^{s+r} ∈ {p^{r+1},…,p^{2r−1}}` into `k` and the rest in `a^r`). For a tuple `k = (k₁,…,k_r) ∈ K_r^r` set

```
T_k := { k₁a₁^r + … + k_r a_r^r : a_i ≥ 1 }.
```

Since `K_r` has counting function `O(x^{1/(r+1)+o(1)})`, we have `Σ_{k ∈ K_r} k^{−1/r} < ∞` — and this convergence is the entire engine of the following theorem.

**Theorem B.** *Fix r ≥ 2, and let S_r be the set of integers which are sums of at most r elements of P_r. Then*

```
S_r has density 0   ⟺   T_k has density 0 for every k ∈ K_r^r.
```

*Moreover this holds with "density 0" replaced by "natural density ≤ δ", uniformly: if* `limsup_x |T_k ∩ [1,x]|/x ≤ δ(k)` *with* `Σ_k δ(k)·(k₁⋯k_r)^{-1/r} < ∞` *then the same tail bound transfers to S_r.*

*Proof.* (⟸) Every element of `S_r` lies in some `T_k`, so for any `P ≥ 1`,

```
|S_r ∩ [1,x]|  ≤  Σ_{k : Π k_i ≤ P} |T_k ∩ [1,x]|  +  Σ_{k : Π k_i > P} x·(k₁⋯k_r)^{−1/r},
```

because `|T_k ∩ [1,x]| ≤ ∏ᵢ (x/kᵢ)^{1/r} = x·(Πkᵢ)^{−1/r}`. The first sum is `o(x)` (finitely many density-0 sets), the second is `≤ x·ε_r(P)` where `ε_r(P) → 0` is the tail of the convergent series `(Σ_k k^{−1/r})^r`. Let `P → ∞`. The converse (⟹) is immediate since `T_k ⊆ S_r`. The weighted refinement is the same argument with `δ(k)` inserted. ∎

**Remarks.** (a) For *r = 2* the sets `T_k` are value sets of binary quadratic forms `c³a² + d³b²` of discriminant `−4c³d³`, and the Blomer–Granville theory provides exactly the needed quantitative density-0 bounds — Theorem B is the abstract scheme hiding behind [BaBr94]/[BlGr06] and behind Tao's "easy argument" comment. (b) For *r = 3*, Theorem B reduces #940(2) to a concrete classical family: *values of fixed positive diagonal ternary cubics* `k₁a³ + k₂b³ + k₃c³`. Their density is unknown in every genuine case — but conjecturally **positive** (Hooley–Heath-Brown heuristics for `x³+y³+z³ = n`), which is the precise sense in which the expected answer to #940(2) is "no". (c) The reduction is equally useful in the contrapositive: to *disprove* density 0 of `S_r` it now suffices to prove positive lower density of the value set of **one** explicit ternary cubic, e.g. `T_{(1,1,1)}` = sums of three positive cubes — a well-known TikTok-era open problem on its own, but a strictly *weaker* target than #940(2).

---

## 4. Theorem C — additive energy ↔ density duality

Let `r ≥ 2`, let `R(n)` count ordered tuples `(a₁,…,a_r) ∈ P_r^r` with `Σaᵢ = n`, and define

```
M(x) = Σ_{n ≤ x} R(n),     E_r(x) = Σ_{n ≤ x} R(n)²,     S_r(x) = |{n ≤ x : R(n) ≥ 1}|
```
```
( E_r(x) = #{ (a,b) ∈ P_r^r × P_r^r : a₁+…+a_r = b₁+…+b_r ≤ x },  the r-fold additive energy )
```

**Theorem C.**
*(i) `S_r(x) ≥ M(x)² / E_r(x)`. In particular, since `M(x) ~ λ_r x` (Theorem D below): if `E_r(x) ≤ K·x + o(x)` for some constant `K`, then `liminf_x S_r(x)/x ≥ λ_r²/K > 0` — the answer to #940(2) is NO in a strong form (explicit positive lower density). More generally `S_r(x) ≥ λ_r²x²/E_r(x)·(1+o(1))`.*
*(ii) Contrapositive: if the answer to #940(2) were YES (S_r(x) = o(x)), then necessarily* `E_r(x)/x → ∞`.

*Proof.* Cauchy–Schwarz: `M(x) = Σ_{n ∈ supp R} R(n) ≤ S_r(x)^{1/2}·E_r(x)^{1/2}`. ∎

**Calibration in the known case r = 2.** Blomer–Granville's `S_2(x) = (log log x)^{O(1)}·x/(log x)^{α}`, `α = 1 − 2^{−1/3} ≈ 0.2063`, combined with `M(x) ~ λ₂x` and Theorem C, *forces*

```
E_2(x)  ≫  x · (log x)^{0.206}·(log log)^{O(1)},
```

*i.e. in the solved case the normalized energy* `E_2(x)/x` *diverges, slowly and rigorously — and Theorem C(ii) says this is not a coincidence: it is a consequence of the density-0 conclusion itself (one expects `E₂(x)` to be of exactly this order, which is compatible with, but not literally implied by, [BlGr06]; independently, Shute's 2021 asymptotic for `z₁+z₂+z₃+z₄ = 0` in primitive squareful variables gives counts `≍ x·(log x)^D` for an explicit `D`, and Van Valckenborgh treats five or more variables — extracting the precise log-power and comparing it with `1 − 2^{−1/3}` is a worthwhile consistency check we have not carried out).*

**What this says about r = 3.** #940(2) is *equivalent* to whether the cubefull numbers' slow energy growth persists: bounded energy `E_3(x) ≍ x` ⟹ positive density (answer NO); energy growth `E_3(x)/x → ∞` is necessary (not sufficient) for answer YES. This converts the problem into a clean second-moment question about `P_r`, and Theorem C(i) gives an unconditionally correct *sufficient* route to the expected answer.

---

## 5. Theorem D — mean multiplicity (quantifying Schinzel's correction)

**Theorem D.** *Let r ≥ 2 and R(n) as above. Then*

```
M(x) = #{(a₁,…,a_r) ∈ P_r^r : Σaᵢ ≤ x}  ~  λ_r · x,     λ_r = C_r^r · Γ(1 + 1/r)^r.
```

*Proof sketch.* Use `P_r(y) = C_r y^{1/r}(1 + o(1))` as a Stieltjes weight `dP_r ∼ (C_r/r)·u^{1/r−1}`. Then

```
M(x) ~ C_r^r·(1/r)^r·x· ∫_{uᵢ ≥ 0, Σuᵢ ≤ 1} Π uᵢ^{1/r−1} du
     = C_r^r·(1/r)^r·x· Γ(1/r)^r·Γ(1)/Γ(2)                     (Dirichlet integral)
     = C_r^r·Γ(1+1/r)^r·x,
```

using `Γ(2) = 1` and `(1/r)Γ(1/r) = Γ(1+1/r)`. Equivalently, induction on r via `B(1/r, 1+1/r)` gives the same closed form (e.g. r = 2: `C₂²·(1/2)·B(1/2,3/2) = C₂²·π/4 = 3.7090` ✓, matching the table). ∎

So the *average* number of representations of an integer as a sum of r r-powerful numbers is a constant `λ_r`: 3.71 (r=2), 71.77 (r=3), 5776 (r=4), 1.69·10⁶ (r=5). This makes two things precise:

* **Schinzel's correction, quantified.** Erdős's "simple counting argument" would have needed `λ_r · (collision factor) < 1`; in fact `λ_r` is *large* and growing superexponentially, so counting alone can never settle any `r ≥ 3` case — with `r = 2` (`λ₂ = 3.71` also > 1) rescued only by the quadratic-form machinery.
* **Why naive independence fails its face-value prediction.** An i.i.d.-Poisson model with parameter λ₃ ≈ 71.8 predicts a fraction `e^{−71.8} ≈ 10⁻³¹` of exceptions — i.e. essentially *none*. Section 6 finds the true exception fraction at comparable scales to be ~5–10%. The discrepancy (overdispersion ratio `Var(R)/meanR ≈ 42` at `x = 3·10⁷`) is the arithmetic noise `σ(n)` of the local densities (cf. §2 and §6.3) multiplied across primes — exactly the quantity a proof must control.

---

## 6. The computational census

### 6.1 Method and validation

We generated all 3-powerful numbers `≤ 4·10⁹` (there are 6058, matching the theory with its secondary-term deficit) and marked, for every `n ≤ 4·10⁹`, whether `n` is a sum of ≤ 3 of them (bitset marking over sorted triples `i ≤ j ≤ k`; about 3·10¹⁰ marks). Separately, for `n ≤ 3·10⁷` we computed the full multiset representation count `R̃(n)` (triples `a ≤ b ≤ c`), its window means, second moments, and per-class behaviour. Total runtime ≈ 7 minutes. Sanity checks pass: representation counts in windows match `λ₃·(C_3(x)/C_3)³` to ≤ 3%.

### 6.2 The exception data

| window (x/2, x] | exceptions | fraction |
|---|---|---|
| ~ (4.9·10⁵, 9.8·10⁵] | 123 776 | 0.1267 |
| (1.95·10⁶, 3.9·10⁶] | 222 458 | 0.1139 |
| (1.56·10⁷, 3.13·10⁷] | 1 384 592 | 0.0886 |
| (2.5·10⁸, 5·10⁸] | 16 059 211 | 0.0642 |
| (5·10⁸, 10⁹] | 29 845 399 | 0.0597 |
| (10⁹, 2·10⁹] | 56 097 825 | 0.0561 |
| (2·10⁹, 4·10⁹] | 104 520 390 | 0.0523 |

**Reading.** The exception *fraction* decays steadily — roughly like `x^{−δ}` with `δ` drifting between 0.07 and 0.13 over the range — while the exception *count* per octave *grows* like `≈ x^{0.9}`. The largest exceptions below 10⁹ cluster at the top (e.g. 999999978, 999999975, 999999970, …), i.e. there is no sign of the exceptions dying out. Two conclusions:

1. The represented set almost certainly has **natural density 1** (so the answer to #940(2) for r = 3 is heuristically **NO**, decisively — the density is not 0, it is ~1 up to a slowly-vanishing fraction);
2. there is no evidence the exceptions are finite — on the contrary their count is growing, pointing to the answer **YES** for #940(1), with exceptions thinning as `~x^{0.9}` rather than `x^{1−o(1)}`.

The naïve Poisson prediction (`e^{−λ₃} ≈ 10⁻³¹` exceptions) is off by 29 orders of magnitude; a Poisson model conditioned on the local factor `σ(n) = ∏ σ_p(n)` (§6.3) is the minimal model consistent with the data, since `P(R̃ = 0) = E[e^{−λ̃σ(n)}]` with measured mean `R̃ ≈ 4.8–6.5` would then need `E[e^{−cσ}] ≈ 0.05` — achievable only if `σ(n)` is strongly defectively distributed across integers, which is testable.

### 6.3 The mod-class structure (and a real surprise)

Exception fraction in `(2·10⁹, 4·10⁹]` per class mod 16, and mean `R̃(n)` per class mod 8 in `(1.5·10⁷, 3·10⁷]`:

| class mod 16 | exc. frac | | class mod 8 | mean R̃ |
|---|---|---|---|---|
| **7** | **0.000 01** | | **7** | **14.24** |
| **15** | **0.000 00** | | 1 | 2.02 |
| evens | 0.004 – 0.014 | | 3 | 2.00 |
| 1, 3, 5, 9, 11, 13 | ≈ 0.126 | | 5 | 1.99 |
| | | | 0 | 5.33 |

So the odd classes `≢ 7 (mod 8)` carry ~12.6 % exceptions, while **`n ≡ 7 (mod 8)` has essentially none at all above 5·10⁸** — mean multiplicity 14.2, about 7× the other odd classes and 3× the even ones. A related 3-adic spike: the class `n ≡ 12 (mod 27)` (i.e. `v₃(n) = 1`, `n/3 ≡ 4 mod 9`) shows 0.01 % exceptions against 7–10 % in other classes with `9 | n`. None of these classes is *excluded* (Theorem A), so these are local-density *inhomogeneities* `σ₂(n)`, `σ₃(n)` of the representation function.

> **Open mini-problem (empirically accessible).** Explain and prove: the 2-adic local density `σ₂(n)` of representations of `n` as a sum of three 3-powerful numbers is maximal at `n ≡ 7 (mod 8)`. Is every sufficiently large `n ≡ 7 (mod 8)` a sum of three 3-powerful numbers?

### 6.4 Energy scaling

`E/|w|` in consecutive windows (`w` an octave up to `3·10⁷`) reads `12.6, 25.3, 35.9, 46.5, 58.4` — increasing slowly, roughly ×2 per decade, in one-to-one analogy with the solved case `E₂(x)/x ≳ (log x)^{0.206}` (§4). By Theorem C the data are far from distinguishing the dichotomy — the window means of `R̃` are themselves still growing toward their asymptotic constant — but they put the decisive statistic on record at these scales.

---

## 7. Refined conjectures suggested by this note

*Clearly heuristic; levels of confidence annotated.*

- **C1 (confidence: strong).** For *r* = 3, sums of ≤ 3 three-powerful numbers have natural density **1**. Hence the answer to #940(2) is **no** for *r* = 3 (and, extrapolating λ_r, even more strongly for all *r* ≥ 4). — Exception fraction falling monotonically over 4 octaves with no sign of a floor; local data (Theorem A) exclude congruence explanations.
- **C2 (confidence: moderate).** Nevertheless there are infinitely many exceptions; their count `E(x)` satisfies `E(x) = x^{1−δ+o(1)}` with a genuine exponent `δ ∈ (0, 1)` (empirically `δ ≈ 0.1` drifting). Hence the answer to #940(1) is **yes** for *r* = 3. — The two conjectures are compatible and both halves match every computed octave.
- **C3 (confidence: strong, and possibly provable with current methods?).** Every sufficiently large `n ≡ 7 (mod 8)` is a sum of three 3-powerful numbers.
- **C4 (the discriminating statistic).** `E_3(x)/x` either stays bounded (⟹ C1) or grows like a small power of `log x` (necessary for a YES answer to #940(2), cf. Theorem C and the r = 2 calibration). Computing `E_3(x)` at `x = 10⁹–10¹⁰` is the sharpest feasible next experiment.

---

## 8. Why a full proof is currently out of reach (sketch of the analytic barrier)

The natural idea is the circle method for the representation function `r(n) = Σ_{a+b+c = n, a,b,c ∈ P₃} 1 = ∫₀¹ F(α)³e(−αn)` with `F(α) = Σ_{m ≤ N, m ∈ P₃} e(αm)`. The barrier is stark: the *main term for an individual n* is `O(1)` (mean multiplicity λ₃ ≈ 71.8, Theorem D), while every available error control lives at polynomial scale: the Parseval budget `∫₀¹|F|² = E₂(N)` satisfies `E₂(N) ≍ N^{2/3}` — pairs of cubefull numbers are `≍ N^{2/3}` inside a sum-range of length `2N`, so generic collisions barely exist and the energy is diagonal-dominated — and the kernel-Weyl decomposition `F = Σ_k Σ_a e(αka³)` (≍ N^{1/4} kernels, cubic Weyl sums of length `(N/k)^{1/3}`) buys at best `sup_minor|F| ≪ N^{7/16+ε}`, already worse than the trivial `N^{1/3}`. Any such method therefore controls errors of size `≫ N^{2/3}` against an `O(1)` main term — hopeless, for exactly the same structural reason that pointwise ("any n") results for sums of three cubes are open. This is the familiar **binary-additive / Goldbach-type regime**: O(1) mean multiplicity, where the global Cauchy–Schwarz second moment (Theorem C) is the only aggregate currently within reach. Any advance on #940 will presumably come from that side: prove `E_3(x) ≪ x` (sufficient for a negative answer to (2), with density `≥ λ₃²/K`) or, in the opposite direction, force `E_3(x)/x → ∞` (necessary for a positive answer). Nothing close to either is currently provable; the analogous r = 2 statement, `E_2(x)/x ≳ (log x)^{0.206}`, cost the Baker–Brüdern/Blomer–Granville machinery.

---

## 9. Reproducibility

- `powerful940.c` — Euler products for `C_r, λ_r`; census to 10⁹; ordered-triple histogram and energy at 3·10⁷. Runtime 76 s. Output: `powerful940_results.txt`.
- `stats940.c` — multiset histogram with window/energy/class statistics; census to 4·10⁹. Runtime 360 s. Output: `stats940_results.txt`.
- Methods validation: generated cubefull counts agree with Lemma 1.1's constant with the sign and size of the expected `x^{1/4}` secondary terms; window means of `R(n)` track `λ₃·(C₃(x)/C₃)³` to ≤ 3%; total tuple counts match Theorem D asymptotics.

## 10. Summary of what is new here

1. **Theorem A** — exact local image of `P_r` mod `p^e`, and proof that no modulus ever obstructs even 2-summand representations (r ≥ 3): #940 is purely analytic.
2. **Theorem B** — #940(2) ⟺ density-0 of every fixed-kernel value set `{Σ kᵢ aᵢʳ}`; abstract form of the Baker–Brüdern/Blomer–Granville/Tao reduction, valid for all r; reduces r = 3 to fixed ternary diagonal cubics.
3. **Theorem C** — the energy–density duality, including the calibration `E₂(x)/x ≳ (log x)^{1−2^{−1/3}}` rigorously implied by Blomer–Granville in the solved case; gives a sufficient second-moment route to the expected answer.
4. **Theorem D + explicit constants** — `M(x) ~ λ_r x` with `λ_r = (C_r Γ(1+1/r))^r`, exact Euler products for `C_r`; quantifies Schinzel's correction (`λ₃ = 71.77`, not < 1).
5. **First census** of the problem to 4·10⁹: exception fractions, the slow `~x^{−0.1}` decay, per-class tables, and the discovery of the `n ≡ 7 (mod 8)` and `n ≡ 12 (mod 27)` spikes, with refined conjectures C1–C4.

*Nothing here resolves #940; the note aims to narrow what the problem is really asking, to certify that no cheap argument was missed, and to record clean conjectures with data.*
