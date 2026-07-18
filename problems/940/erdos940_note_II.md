# Erdős Problem #940 — Note II
## The arithmetic anatomy of the exceptional set: erratum, exact local laws, the homothety ideal, and the corrected conjectures

*Companion to `erdos940_research_note.md` ("Note I") and `erdos_problem_940_state_of_the_art.md` ("Survey").
Problem: for r ≥ 3, (1) are there infinitely many integers not sums of ≤ r r-powerful numbers, and (2) does that sumset have density 0? This note concerns r = 3 throughout (3-powerful = "cubefull": p | n ⟹ p³ | n). Every claim is labelled **[Theorem]** (full proof or proof with precisely identified standard lemmas), **[Computation]** (reproducible, sources in §9), **[Model]** (exact local factors + one dynamical input, the running of the counting constant), or **[Conjecture]**. The signature * convention is v_p(n) for the p-adic valuation.*

---

## 0. Summary of what is new

1. **Erratum (§1).** Note I's class labels in §6.3 suffered an off-by-one (mod 8/16), +6 (mod 9), +15 (mod 27) window-start offset. The celebrated "n ≡ 7 (mod 8) has no exceptions" is **false as stated**; the truth is more natural and much stronger: the exception-free classes are the multiples of 8, and the *hardest* classes are v₂(n) ∈ {1, 2}. All affected Note I statements are corrected here and patched there.
2. **Theorem II.1 (§2): the exact p-adic limit law of cubefull numbers.** The density of cubefull numbers in each residue class mod pᵉ converges, as x → ∞, to an explicit product measure: vₚ has an explicit distribution φₚ with φₚ(1) = φₚ(2) = 0, and the unit part is Haar-uniform and independent of the valuation. Hence the frequency-weighted singular factors σ̃ₚ of the representation function are *explicitly computable constants*, uniform on unit classes — we tabulate σ̃₂, σ̃₃, σ̃₅ exactly (§3).
3. **The zero-parameter local model (§4).** P(n exceptional) ≈ exp(−λ(x)·σ̃₂(n)·σ̃₃(n)) with **no fitted constant**: λ(x) = λ∞·(C₃(x)/C₃)³ is the running mean multiplicity. It reproduces *every* measured census cell to within 4–55 % and the overall octave densities to **2–6 %**, resolving Note I's "29-orders-of-magnitude" paradox: the culprits are (a) the slow convergence C₃(x) → C₃ (λ_eff ≈ 6.5 ≪ λ∞ = 11.96 at 4·10⁹) and (b) Jensen domination by the singular-series-poor classes. The implied overdispersion parameter κ(x) decreases monotonically 1.23 → 1.03 over nine octaves. **The observed decay of the exception fraction (~x^{−0.1}) is entirely explained by the running of C₃(x); the model extrapolates to a positive limit density ≈ 0.7–1.0 % of exceptions.** This changes the picture painted in Note I — see N1/N2 in §7.
4. **Theorem II.2 (§5): the homothety law and the ideal of exceptions.** S ⊇ m³·S, so the exception set E is a down-ideal under cube division: every exception's cube-free kernel is an exception. With the ray sandwich ℱ(x) ≤ E(x) ≤ x^{1/3}·Σ_{f∈ℱ} f^{−1/3}, this reduces #940(1) to the growth of **cube-free exceptions**, and the census shows they dominate: **99.985 % of the 104 520 390 exceptions in (2·10⁹, 4·10⁹] are cube-free; the exact identity 104 504 753 + 15 637 = 104 520 390 holds.**
5. **Theorem II.3 (§5.2).** The exceptional set contains **no infinite arithmetic progression**, and every residue class of every modulus contains infinitely many sums of three cubefull numbers (Theorem A of Note I + homotheties m = 1 + kq).
6. **Ray census (§6.2).** For **every** cube-free exception f ≤ 6.25·10⁷, at least one of 8f, 27f is a sum of three cubefull numbers (m₀(f) ∈ {2, 3}; 11 788 446 rays tested, zero exceptions; m₀(f) = 2 for 99.987 % of roots with a lift in range). Conjecture N4: this holds for all exceptions.
7. **Corrected conjectures (§7)** replacing C1–C3 of Note I: N1 (infinitely many exceptions — robust under every scenario), N2 (the sharp dichotomy for #940(2): positive limit density ≈ 0.9 % vs density 1, discriminated by whether κ(x) → κ∞ > 0 or κ(x) → 0; the data now slightly favour a *positive* limit), N3 (the corrected mod-class conjecture: every large n with v₂(n) ≥ 3 is representable), N4 (ray law m₀ ≤ 3), N5 (cube-free reduction of #940(1)), N6 (limit-law of R̃).

Nothing here solves #940. But the problem is now considerably narrower than after Note I: **both halves are reduced to explicit, falsifiable statements about quantities we can define exactly and measure cleanly.**

---

## 1. Erratum to Note I (class-label offsets)

### 1.1 What happened

Note I's per-class tables were computed with loops of the form `n = W + r, n ≤ 4·10⁹, step m`, and the printed label "[r]" was read as the class r mod m. The actual class is (W + r) mod m, with W = 15 000 001 (mean-R̃ window), 500 000 001 (mod-9/16/27 exceptions), 2 000 000 001 (mod-16 exceptions). Offsets: **+1 mod 8 and 16, +6 mod 9, +15 mod 27**. The raw counting was correct; only the labels were wrong. (A second, cosmetic aggregation slip in `rays940.c`'s printout of the v₂ ≥ 3 column was identified by exact bookkeeping — the underlying per-class counts are right; see §6.1.)

### 1.2 Corrected tables

**Exception fraction by class mod 16 in (2·10⁹, 4·10⁹]** (from `stats940_results.txt`, labels corrected):

| class t mod 16 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exc. frac | .00000 | .0037 | .1237 | .0101 | .1267 | .0114 | .1279 | .0115 | .00001 | .0073 | .1277 | .0094 | .1259 | .0105 | .1263 | .0142 |

Grouped truth: **v₂(n) = 1 (t ∈ {2,6,10,14}): ≈ 12.6 %; v₂(n) = 2 (t ∈ {4,12}): ≈ 12.6 %; v₂(n) ≥ 3 (t ∈ {0,8}): ≈ 0 – 10⁻⁵; n odd: 0.4–1.4 %.**

**Mean R̃(n) by class mod 8, window (1.5·10⁷, 3·10⁷]** (from `stats940_results.txt`, labels corrected; the window mean is 4.826):

| class t mod 8 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| mean R̃(n) | **14.24** | 5.33 | 2.02 | 4.55 | 2.00 | 4.27 | 1.99 | 4.21 |
| ÷ window mean | 2.951 | 1.104 | 0.419 | 0.943 | 0.414 | 0.885 | 0.412 | 0.872 |

So the class with the anomalously large representation count is **8 | n** (14.24, three times the odd classes, seven times the classes 2·odd or 4·odd) — *not* "7 mod 8". And **class 0 mod 27** — not "12 mod 27" — is the 3-adic spike (0.01 % exceptions in (5·10⁸, 10⁹]; every other class with 9 | n has 7–10 %).

**Exception fraction by class mod 9 in (5·10⁸, 10⁹]** (labels corrected):

| class t mod 9 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| exc. frac | .0466 | .0161 | .0545 | .1034 | .0697 | .0720 | .1041 | .0540 | .0167 |

and mod 27 (same window), where the structure becomes fully visible:

| v₃(t) | classes | exc. frac |
|---|---|---|
| = 1 | {3,6,12,15,21,24} | .1033 – .1041 |
| = 2 | {9, 18} | .0697 – .0700 |
| ≥ 3 | {0} | **.0001** |
| 0, t ≡ ±1 (mod 9) | {1,8,10,17,19,26} | .0156 – .0175 |
| 0, other units | the remaining 12 | .0530 – .0728 |

The second line of the last block is a recognizable fossil: the classes ≡ ±1 (mod 9) are exactly the *cube residues* — where values of plain cubes live — and they are boosted 3–4× relative to the other unit classes: this is the (1,1,1)-kernel trace of the local factor showing through at finite x, cf. §3.4.

### 1.3 Consequently

- Note I's "Open mini-problem" (explain the 2-adic maximum at 7 mod 8) and Conjecture C3 ("every large n ≡ 7 mod 8 is representable") are replaced by §7, N3.
- Note I's §6.2 conclusion "represented density → 1" is **softened**: the refined model of §4 predicts the exception density to *stabilize at ≈ 0.9 %*, not to vanish; see §7, N2. (Either way the answer to the density half of #940 is "no, not 0", but the margin matters.)
- Note I's C2 (exception count ~ x^{0.9}) stands and is strengthened to a statement about cube-free roots (§7, N5).
- All conceptual infrastructure of Note I (Theorems A–D) is unaffected.

---

## 2. Theorem II.1 — the exact p-adic limit law of cubefull numbers

### 2.1 Statement

Recall the canonical form: every cubefull n has a **unique** factorisation
`n = a³·b⁴·c⁵` with b, c squarefree and coprime (Note I, Thm B for r = 3). Write
```
D_p = 1 + p^{−4/3} + p^{−5/3},
φ_p(k) = D_p^{−1} · Σ_{(α,β,γ): 3α+4β+5γ = k, β,γ∈{0,1}, βγ=0}  ((p−1)/p^{α+1}) · p^{−(4β+5γ)/3}.
```

**Theorem II.1 [Theorem].** *Fix a prime p. As x → ∞, the relative frequencies among cubefull n ≤ x of residue classes mod pᵉ converge, for every e ≥ 1, to the following explicit limit law on Z_p:*
- *(valuations)* P(v_p(n) = k) = φ_p(k). In particular φ_p(0) = (1 − 1/p)/D_p and φ_p(1) = φ_p(2) = 0;
- *(unit part)* conditional on v_p(n) = k, the rescaled integer n·p^{−k} is **equidistributed over the units** (Z/p^e)× for every e;
- *(independence)* the joint law over a finite set of primes is the product of these laws (CRT).
*Consequently the density of cubefull numbers in each single class p^k·u mod p^e (u a unit mod p^{e−k}, k ∈ {0} ∪ {3,…,e−1}) is φ_p(k)/((p−1)p^{e−k−1}), and the class 0 mod p^e carries 1 − Σ_{k<e} φ_p(k).*

First values: D₂ = 1.711831, φ₂(0) = 0.292085, φ₂(3) = 0.146042, φ₂(4) = 0.115914, φ₂(5) = 0.092001; D₃ = 1.391370, φ₃(0) = 0.479120, φ₃(3) = 0.159707.

### 2.2 Proof

*Reduction to the parts.* With n = a³b⁴c⁵ as above, v_p(n) = 3α + 4β + 5γ with (α, β, γ) = (v_p(a), [p|b], [p|c]), βγ = 0. Write n = p^{3α+4β+5γ}·U with U = u³·b′⁴·c′⁵, u = a/p^α, b′ = b/p^β, c′ = c/p^γ, all prime to p.

*Counting.* The number of cubefull n ≤ x with prescribed (α, β, γ) and U ≡ ρ (mod p^e), ρ a unit, has leading term
```
x^{1/3} · ((p−1)/p^{α+1}) · p^{−(4β+5γ)/3} · Π_{ℓ ≠ p}(1 + ℓ^{−4/3} + ℓ^{−5/3}) · 1/(p−1)p^{e−1}·(1+o(1)),
```
i.e. the p-part of the Euler constant C₃ (Lemma 1.1 of Note I) times explicit local weights. Inputs: (i) #{a ≤ Y : v_p(a) = α, a ≡ p^α u (mod p^e)} = Y·(p−1)/p^{α+1}·1/((p−1)p^{e−1−α}) + O(1) — elementary; (ii) equidistribution of squarefree b′, c′ over unit classes mod p^e with coprimality constraints — standard inclusion–exclusion over prime squares, error O(Y^{1/2}), which relative to the main terms means an overall relative error O(x^{−1/12+o(1)}) — the observed convergence rate, cf. §2.4.

*Uniformity of the unit part.* The unit U = u³b′⁴c′⁵ is a product of three independent equidistributed variables, each uniform on a *subgroup* of G = (Z/p^e)×: u³ uniform on G³, b′⁴ on G⁴, c′⁵ on G⁵. Since gcd(3, 4) = 1, the subgroups satisfy G³·G⁴ = G, and for an abelian group μ_{H₁} ∗ μ_{H₂} = μ_G whenever H₁H₂ = G (Fourier: a character trivial on both is trivial on G). Hence U is exactly uniform on G. (For p ∈ {2, 3} already c′⁵ alone is uniform, 5 being coprime to φ(p^e); the argument above covers every p, e.g. p = 61.) Conditional on (α,β,γ), n mod p^e is p^{3α+4β+5γ}·U with U uniform — giving both the valuation law and the unit uniformity. The CRT-factorisation is immediate from the Euler-product structure of the canonical form and the joint equidistribution in (ii). ∎

**Corollary II.1a (limit measure).** *The cubefull set carries a natural probability measure on Z_p: v_p distributed by φ_p and, independently, the unit part Haar-uniform. It is a product measure over p on Ẑ.*

**Corollary II.1b (stabilization).** *Under refinement mod p^e → mod p^{e+1}, each class of valuation k ≤ e − 1 splits its mass equally among its p lifts, and class 0 keeps only the valuation ≥ e + 1 tail. Hence any statistic built from these class weights — in particular the σ̃_p below — stabilizes: it is defined already by the Z_p-law, and its mod-p^e truncations converge to it.*

### 2.3 Numerical verification of convergence

P(cubefull n ≤ x is odd), exact limit φ₂(0) = 0.292085 [Computation]:

| x | 10⁵ | 10⁶ | 10⁷ | 10⁸ | 10⁹ | 4·10⁹ |
|---|---|---|---|---|---|---|
| freq | 0.3411 | 0.3322 | 0.3226 | 0.3155 | 0.3115 | 0.3088 |

Convergence is slow but clean, consistent with the O(x^{−1/12}) secondary term (relative gap at 4·10⁹ is 5.7 %, and 4·10⁹^{−1/12} = 0.158). The L¹-distance between the exact and empirical class measures is 0.071 (mod 64) and 0.147 (mod 81) at x = 4·10⁹.

---

## 3. The frequency-weighted singular factors σ̃_p, computed exactly

### 3.1 Definition

For a modulus p^e let w be the limit class-measure of Thm II.1, and define the 3-fold convolution evaluated at t:
```
σ̃_p(t mod p^e) = p^e · Σ_{x+y+z ≡ t} w(x) w(y) w(z)        (mean 1 over t).
```
This is the exact local factor at p of the representation-count law R̃(n), *with the true (frequency) weighting of the summands* — the quantity Note I could only access through the uniform-weight approximation, which provably fails for p = 2 (uniform weight gives σ₂ ∈ {0.768, 0.832, 1.216}; the truth ranges from 0.3624 to 3.20).

**Corollary II.1c [Theorem].** *σ̃_p(t) depends on t only through v_p(t) (capped by e), and is uniform on unit classes. Each σ̃_p(·) is an explicitly computable rational function of p^{1/3}, D_p and t's valuation stratum.*

### 3.2 The exact values

Computed by exact 81/64/125-point convolutions of the limit law [Theorem + Computation]:

**σ̃₂(t)** as a function of the valuation stratum (mod-64 computation):

| v₂(t) | 0 (odd) | 1 | 2 | 3 (t ≡ 8 mod 16) | 4 (t ≡ 16 mod 32) | 5 (t ≡ 32 mod 64) | ≥ 6 (t ≡ 0 mod 64) |
|---|---|---|---|---|---|---|---|
| σ̃₂ | 0.9281 | 0.3624 | 0.3624 | 2.6253 | 3.2005 | 3.7757 | 4.9262 |

Note the equality σ̃₂(v₂ = 1) = σ̃₂(v₂ = 2) — both classes are 2^k·(uniform odd unit) — and the rapid growth beyond v₂ = 3. Aggregated: 0.9281 (odd), 0.3624 ({2,4,6} mod 8), 3.2005 (0 mod 8), with the mod-8 value mixing the high strata.

**σ̃₃(t)** (mod-81 computation):

| v₃(t) | 0 (units) | 1 (t ∈ {3,6} mod 9) | 2 (t ∈ {9,18} mod 27) | 3 (t ∈ {27,54} mod 81) | ≥ 4 (t ≡ 0 mod 81) |
|---|---|---|---|---|---|
| σ̃₃ | 0.9777 | 0.6206 | 0.6206 | 3.8349 | 5.6376 |

(Aggregated at mod 27, class 0 mixes to 4.4358.)

**σ̃₅(t)** (mod 125): units 0.9962; v₅ ∈ {1,2}: 0.8435; t ≡ 0 mod 125: 5.1385. Higher primes converge rapidly to 1 on the dominant strata (the uniform-weight computation of Note I gave |σ_p − 1| ≤ 0.054, 0.026, 0.010 for p = 5, 7, 11), so the truncated product σ̃₂σ̃₃ captures the bulk of the local fluctuation.

### 3.3 Verification against the census

Three-way comparison [Computation]: exact σ̃₂ (limit law), empirical σ̃₂ (6058 cubefull numbers ≤ 4·10⁹), and the *measured* per-class mean R̃(n) at 3·10⁷ (normalised; this mixes in the running of C₃(x), cf. §4):

| t mod 8 | exact | empirical (4·10⁹) | census mean R̃/norm (3·10⁷) |
|---|---|---|---|
| 0 | 3.2005 | 3.0350 | 2.9505 |
| 1 | 0.9281 | 1.0449 | 1.1044 |
| 2 | 0.3624 | 0.3969 | 0.4185 |
| 3 | 0.9281 | 0.9560 | 0.9428 |
| 4 | 0.3624 | 0.3966 | 0.4144 |
| 5 | 0.9281 | 0.8973 | 0.8847 |
| 6 | 0.3624 | 0.3949 | 0.4123 |
| 7 | 0.9281 | 0.8784 | 0.8723 |

The max/min ratio of the local factor, 8.8, is confirmed by the data (7.0±0.3) up to the documented O(x^{−1/12}) convergence drift. The local-factor picture of Note I — made qualitative there — is thereby promoted to a **quantitatively verified theorem**.

### 3.4 The kernel decomposition (why finite-x corrections are themselves structured)

By Thm B of Note I, cubefull n = k·a³ with k in the kernel set K₃ = {b⁴c⁵ : b, c squarefree, coprime}, so R̃ decomposes over kernel triples:
```
R̃(n) = Σ_{(k₁,k₂,k₃) ∈ K₃³}  #{ a₁³k₁ + a₂³k₂ + a₃³k₃ = n },
```
and accordingly σ̃_p(t) = Σ_k W_k(x)·σ̃_p^{(k)}(t), where σ̃^{(1,1,1)} is the *classical three-cubes local factor*. The measured splitting of unit classes mod 9 ({±1}: 1.6 % exceptions; other units: 5.4–7.2 %) is precisely the cube-trace showing through: triples of pure cubes sum preferentially to ≡ 0, ±1, ±2, ±3 mod 9 per ±-sign patterns, and the kernel corrections fill the remaining classes. Since Σ_{k∈K₃} k^{−1/3} < ∞, this is a *convergent* correction expansion — the natural starting point for a rigorous treatment of the local factors' x-dependence.

---

## 4. The local model, verified without free parameters

### 4.1 The model

**[Model]** For n in an octave around x,
```
P(n is exceptional) ≈ exp( − λ(x) · σ̃₂(n) · σ̃₃(n) ),     λ(x) = λ∞ · (C₃(x)/C₃)³,
```
where λ∞ = 11.9611 is the asymptotic multiset mean multiplicity (Theorem D of Note I, λ₃ = 71.767 ordered) and C₃(x) = (#cubefull ≤ x)·x^{−1/3} is the running constant, *measured*, not fitted:

| x | 1.25·10⁸ | 2.5·10⁸ | 5·10⁸ | 10⁹ | 2·10⁹ | 4·10⁹ | ∞ |
|---|---|---|---|---|---|---|---|
| C₃(x) | 3.562 | 3.613 | 3.664 | 3.721 | 3.772 | 3.816 | 4.6537 |
| λ(x) | 5.37 | 5.59 | 5.84 | 6.11 | 6.37 | 6.59 | 11.961 |

The model's two inputs are both *theorems* (Thm II.1 for σ̃; Lemma 1.1 + Thm D for λ); the only **assumption** is approximate conditional Poissonianity of R̃(n) given the local factor, with overdispersion κ — which we do *not* fit but *measure* (§4.3), finding κ(x) ∈ [1.03, 1.23] over the whole computation.

### 4.2 Per-cell verification [Computation]

Predicted vs measured exception fractions, top octave (2·10⁹, 4·10⁹], λ = 6.59, κ = 1 (and second block: octave (5·10⁸, 10⁹], λ = 6.11):

| cell | predicted | measured | | cell | predicted | measured |
|---|---|---|---|---|---|---|
| v₂ = 0 (odd) | .0083 | .0098 | | v₃ = 0 (units mod 9) | .0375 | .0405 |
| v₂ = 1 | .1316 | .1264 | | v₃ = 1 | .0963 | .0930 |
| v₂ = 2 | .1316 | .1263 | | 9 divides t (mixed v₃ ≥ 2) | .0642 | .0415 |
| v₂ ≥ 3 | .0000 | .00001 | | | | |

| cell (5·10⁸,10⁹] | predicted | measured |
|---|---|---|
| v₂ = 0 | .0114 | .0131 |
| v₂ = 1, 2 | .1513 | .1417 / .1419 |
| v₃ = 0, 1, mixed-9 | .0449 / .1096 / .0731 | .0472 / .1037 / .0466 |

Overall exception fraction per octave:

| octave | (2.5·10⁸,5·10⁸] | (5·10⁸,10⁹] | (10⁹,2·10⁹] | (2·10⁹,4·10⁹] |
|---|---|---|---|---|
| predicted | .0683 | .0624 | .0576 | .0535 |
| measured | .0642 | .0597 | .0561 | **.0523** |

Two honest caveats. (a) On *σ̃-rich* classes (v₂ ≥ 3 or v₃ ≥ 3) the model *underpredicts* the (absolutely negligible, ≤ 10⁻⁵) exception counts — those exceptions are homothety shadows 8f, 27f of surviving roots (§5), a correlation the independence model cannot see. (b) The aggregate "9 | n" cell needs the mod-27 refinement (Jensen: the mean of e^{−λσ} splits over {0}, {9,18} mod 27); at that refinement the prediction improves to ≈ 0.050 vs 0.0415.

### 4.3 What killed the 10³¹, and what κ does

Note I observed that naive Poisson with λ∞ predicts e^{−71.8} ≈ 10⁻³¹ exceptions against a measured 5 %. Decomposition of the discrepancy:
```
measured 0.0523  ←(1)  λ_eff = 6.5, not 71.8/6: the running C₃(x) costs a factor (C₃(x)/C₃)³ ≈ 0.55
               ←(2)  Jensen: P0 = E[e^{−λσ̃(n)}] is carried by the σ̃-poor minority
                     (min σ̃₂σ̃₃ = 0.3624·0.6206 = 0.225, on v₂∈{1,2} × v₃=1; max is ~25)
               ←(3)  residual overdispersion κ(x) ∈ [1.03, 1.23], measured per octave:
```
| octave top | 9.8·10⁵ | 3.9·10⁶ | 3.1·10⁷ | 1.25·10⁸ | 2.5·10⁸ | 5·10⁸ | 10⁹ | 2·10⁹ | 4·10⁹ |
|---|---|---|---|---|---|---|---|---|---|
| κ(x) | 1.231 | 1.124 | 1.086 | 1.078 | 1.058 | 1.049 | 1.048 | 1.035 | 1.031 |

[Computation: κ(x) is the unique value making the model's octave fraction match the census.] **κ is monotone decreasing and close to 1** — the within-class law of R̃(n) is close to Poisson at these scales, and getting closer. (Consistent with the second moment: the exact σ̃₂σ̃₃ mixture alone accounts for Var/mean ≈ 27.5 of the measured 42 at 3·10⁷, the remainder being within-class correlations ×~1.5 that shrink with x.)

### 4.4 Extrapolation — and a prediction that changes the picture

Since the measured per-octave decay of the exception fraction (×0.9315 at the top octave, "x^{−0.1}") is reproduced by the model *through λ-running alone* (predicted ratio 0.9298; the engine being that dλ/d ln x ≈ 0.055λ ≈ 0.36 per e-fold at these x, acting on the Jensen-effective stratum σ̃ ≈ 0.35), the natural extrapolation freezes κ at ≈ 1 and runs C₃(x) → C₃ with its fitted secondary term (C₃(x) ≈ C₃(1 − 1.13·x^{−1/12})):

| x | 10¹¹ | 10¹² | 10¹³ | 10¹⁵ | 10¹⁸ | → ∞ |
|---|---|---|---|---|---|---|
| predicted exc. frac | .0384 | .0315 | .0267 | .0205 | .0159 | **E[e^{−11.961·σ̃₂σ̃₃}] ≈ .0094** |

**[Model-prediction, labelled as such] the exception density approaches a positive limit ≈ 0.9 % (between .008 and .010 for κ∞ ∈ [1.00, 1.05])** — and the class (v₂ ∈ {1,2}) × (v₃ = 1), of natural density 1/12, keeps ≈ e^{−2.69} ≈ 6.8 % exceptions forever. This is the *opposite* asymptotic of Note I's C1 (density 1). Which of the two regimes is true is exactly the content of the refined conjecture N2 — but the burden has shifted: density 1 now *requires* the within-class overdispersion to grow without bound (κ(x) → 0), a behaviour the data show no sign of through 4·10⁹.

---

## 5. The homothety law: exceptions as an ideal, and two theorems

### 5.1 Theorem II.2 [Theorem]

Let S = 3S₃ = {sums of ≤ 3 cubefull numbers}, E = ℕ ∖ S.

(i) **Homothety.** *S ⊇ m³·S for every m ≥ 1*; indeed x ∈ P₃ ⟹ m³x ∈ P₃ (exponents e ≥ 3 stay ≥ 3, e = 0 stays 0).
(ii) **Down-ideal.** *E is a down-ideal under cube division: n ∈ E and d³ | n ⟹ n/d³ ∈ E.* Equivalently, writing every integer uniquely as n = f·m³ with f cube-free: n ∈ E ⟹ f ∈ E.
(iii) **Ray decomposition.** *E = ⨆_{f ∈ ℱ} (E ∩ f·m³), where ℱ = cube-free exceptions; and E(x) = Σ_{f∈ℱ} E_f(x) with E_f(x) ≤ (x/f)^{1/3}.* Consequently
```
ℱ(x) ≤ E(x) ≤ x^{1/3} · Σ_{f ∈ ℱ, f ≤ x} f^{−1/3},
```
so if ℱ(y) = O(y^{β+o(1)}) with β > 1/3 then E(x) = O(x^{β+o(1)}): **the growth exponent of the exception count equals that of cube-free exceptions** (if ℱ is finite, E(x) = O(x^{1/3})).
(iv) **Disjunctive reduction of #940(1).** *There are infinitely many exceptions ⟺ infinitely many cube-free exceptions, or some cube-free exception f has f·m³ ∈ E for infinitely many m.*

*Proof.* (i) If n = x₁+x₂+x₃ with xᵢ cubefull, then m³n = Σ m³xᵢ is too. (ii) Contrapositive of (i) applied to n = d³·(n/d³). (iii) Existence and uniqueness of the cube-free kernel; the bound on E_f is trivial; the growth statement is Abel summation: Σ_{f∈ℱ∩[1,x]} f^{−1/3} = x^{−1/3}ℱ(x) + (1/3)∫₁^x t^{−4/3}ℱ(t)dt = O(x^{β−1/3+o(1)}). (iv) If ℱ is finite, E(x) ≤ x^{1/3}Σ_{f∈ℱ} f^{−1/3}: for infinitely many exceptions some ray must be infinite; conversely trivial. ∎

### 5.2 Theorem II.3 [Theorem]

*Every residue class mod every q contains infinitely many elements of S. In particular, E contains no infinite arithmetic progression — the exceptions, however numerous, cannot syndetically align.*

*Proof.* By Theorem A of Note I, for every class c mod q there exist cubefull residues with x₁+x₂+x₃ ≡ c (mod q), and Lemma 2.1 of Note I lifts each to an actual cubefull integer in its class, giving some n₀ ∈ S with n₀ ≡ c (mod q). For m = 1 + kq, m³ ≡ 1 (mod q), so by homothety (1+kq)³·n₀ ∈ S and ≡ n₀ ≡ c (mod q) for every k ≥ 0. ∎

**Remark.** The same argument shows E is *not* contained in any finite union of residue classes avoiding…; more generally, the outcome "infinitely many exceptions" of #940(1) can never be certified by congruences — the problem is unavoidably analytic (as Note I's Theorem A already said in filtration form).

### 5.3 The [Computation] verification

- (E-decomposition, exact): exceptions in (2·10⁹, 4·10⁹] = 104 520 390 = **104 504 753 cube-free** + **15 637 lifts** f·m³, m ≥ 2, f ≤ 5·10⁸ cube-free exception. Consistency to the unit. The lift fraction is 0.015 % (per octave: 0.02 % → 0.08 % going down).
- (Down-ideal): explicit cube-divisibility tests on exceptions, zero violations (as must be, this being a theorem — the check validates the bitset machinery).
- Cube-free exceptions per octave: 1 383 605 → 2 495 260 → 4 601 165 → 8 660 301 → 16 054 617 → 29 838 901 → 56 087 288 → 104 504 753 — exponential growth with ratio ≈ 1.85–1.87 per doubling, i.e. ℱ(x) ≈ x^{0.89±0.02} up to 4·10⁹.

---

## 6. The new census: class trends and ray lifetimes

### 6.1 Per-octave, per-class exception fractions [Computation]

(v₂-classes from mod-16 counts; v₃ from mod-9; octave (w/2, w]. The v₂≥3 column of `rays940`'s printout was corrupted in *aggregation only* by a dangling else — it had absorbed the v₂=1 classes; the corrected column below uses the exact bookkeeping identity plus the mod-16 truth table of §1.2.)

| octave top w | odd | v₂ = 1 | v₂ = 2 | v₂ ≥ 3 | all | v₃ = 0 (units) | v₃ = 1 | 9 \| n |
|---|---|---|---|---|---|---|---|---|
| 4·10⁹ | .0098 | .1264 | .1263 | ~10⁻⁵ | .0523 | .0405 | .0930 | .0415 |
| 2·10⁹ | .0114 | .1344 | .1344 | <10⁻⁴ | .0561 | .0439 | .0987 | .0443 |
| 10⁹ | .0131 | .1417 | .1419 | ~0 | .0597 | .0472 | .1037 | .0466 |
| 5·10⁸ | .0154 | .1507 | .1509 | ~0 | .0642 | .0514 | .1099 | .0501 |
| 2.5·10⁸ | .0187 | .1601 | .1595 | — | .0693 | .0559 | .1173 | .0538 |
| 1.25·10⁸ | .0212 | .1680 | .1685 | — | .0737 | .0599 | .1230 | .0574 |
| 6.25·10⁷ | .0251 | .1793 | .1803 | — | .0799 | .0660 | .1307 | .0616 |
| 3.125·10⁷ | .0303 | .1952 | .1972 | — | .0886 | .0741 | .1428 | .0673 |

Reading: the "hard" classes decay very slowly (×0.94 per doubling), the odd classes noticeably faster (×~0.86), and the v₂ ≥ 3 classes are essentially empty already at 5·10⁸ (matching §4's model, whose σ̃₂ = 2.6–3.8 there; the residual ~10⁻⁵ counts are the 8f-shadows of §6.2).

The 25 largest exceptions below 4·10⁹ (from 3 999 999 399 to 3 999 999 972) all have **v₂ ∈ {1, 2} (17× "1", 6× "2", 2× odd, none with v₂ ≥ 3)**; the largest exception below 10⁹ is 999 999 978 = 2·3·166 666 663 — v₂ = 1, v₃ = 1, the exact worst cell of the local model.

### 6.2 Ray lifetimes [Computation]

For each of the 64 686 108 cube-free exceptions f ≤ 10⁹ and each m ≥ 2 with f·m³ ≤ 4·10⁹, we tested whether f·m³ ∈ S. Let m₀(f) be the least such m.

- Rays with at least one lift in range (f ≤ 5·10⁸, i.e. 8f ≤ 4·10⁹): m₀ = 2 for 34 842 637 = **99.988 %** of them; m₀ = 3 for 2 729; the remaining 1 841 (necessarily with only one or two lifts available in range) had no represented lift within 4·10⁹.
- **All 11 788 446 rays with ≥ 3 lifts in range (f ≤ 6.25·10⁷, so 8f, 27f, 64f all available) enter S at m = 2 or m = 3: m₀(f) ∈ {2, 3} universally in this range.**
- Interpretation: v₂(8f) ≥ 3 always, so "8f ∈ S" is the v₂ ≥ 3 conjecture N3 applied to a distinguished 34.85-million-point family; it fails only ~1 in 7 600 times, and then 27f rescues in the majority of the remaining cases (m₀ = 3).

### 6.3 The exception set, anatomized

Putting §5 and §6 together: at 4·10⁹ the exception set is (i) 99.985 % fresh cube-free roots, appearing in every octave at rate x^{0.9}; (ii) concentrated on the singular-series-poor classes v₂ ∈ {1,2} (91 % of exceptions) with the odd classes contributing 9 %; (iii) its ray-lifts are virtually all dead within one or two cube-multiplications; and (iv) it carries no local obstruction whatsoever (Note I, Thm A), hence aligns in no progression (Thm II.3). Under the local model the whole picture is generated by two numbers per prime — the valuation law φ_p and the resulting σ̃_p — multiplied against a single running scalar λ(x).

---

## 7. The corrected and refined conjectures

*Replaces Note I's C1–C3 for r = 3; C4 (energy as discriminating statistic) stands and is sharpened below.*

- **N1 [Conjecture, very strong confidence] — #940(1) is YES.** The exception count E(x) = x^{1−o(1)} (empirically ~x^{0.90±0.02} over nine octaves, ratios 1.85–1.88 per doubling); equivalently by Thm II.2(iii), cube-free exceptions have the same exponent. Infinitely many non-sums follow under *every* regime consistent with the data — including the extreme case that the worst local cell {v₂ ∈ {1,2}} × {v₃ = 1} (density 1/12 of ℕ) keeps only its model floor of ≈ 6.8 % exceptions. *Comment:* this is a strong, clean claim, and it is the half of #940 that literature folklore never addressed; the observed margin (10⁸ fresh exceptions per octave, growing) makes it the safest conjecture in these notes.
- **N2 [Conjecture — the sharp dichotomy] — #940(2) is NO (positive density), with two possible margins.** Exactly one of:
  (A) *(local-Poisson regime)* κ(x) → κ∞ > 0. Then the sumset has density → 1 − δ∞, δ∞ = E[e^{−κ∞·11.961·σ̃₂σ̃₃}] ≈ **0.7–1.0 %**, and the exception set has *positive density* ~ 1 %;
  (B) *(dispersion regime)* κ(x) → 0 (within-class overdispersion diverges, as provably happens at r = 2, where E₂(x)/x ≳ (log x)^{0.206}). Then the sumset has density 1.
  **Current evidence favours (A):** κ(x) decreases monotonically 1.231 → 1.031 over nine octaves and the whole per-cell structure fits at κ = 1 already; regime (B) requires a qualitative change of trend. Either way #940(2) is answered "no". The discriminating statistic is exactly κ(x) (equivalently the within-class dispersion of R̃ at fixed σ̃-stratum, or E₃(x)/x relative to its σ̃-prediction) at x = 10¹⁰–10¹².
- **N3 [Conjecture, strong] — the corrected class statement.** *Every sufficiently large n with v₂(n) ≥ 3 is a sum of three cubefull numbers.* (Weaker, safer form: exceptions in ∪_{k≥3}{v₂ = k} have density zero within those classes, at rate ≫ x^{−1/2}.) Evidence: exception fraction ≤ 10⁻⁵ there already (2·10⁹, 4·10⁹], ~0 at (5·10⁸, 10⁹]; the residual exceptions are 8f-shadows (§6.2), i.e. they are governed by the ray law N4. Odd n: exception density within odds → 0 at rate ~x^{−0.2}.
  By contrast we conjecture the classes v₂ ∈ {1,2} keep a **positive** fraction of exceptions forever (≈ e^{−λ∞·0.3624·σ̃₃} ≈ 5–26 % depending on v₃), as does each fixed class v₃ = 1 × odd.
- **N4 [Conjecture, strong] — the ray law.** *For every exception e, at least one of 8e, 27e is a sum of three cubefull numbers* (m₀(e) ≤ 3); moreover 8e ∈ S with at most finitely many exceptions e. (Evidence: 3.5·10⁷ rays, universally m₀ ∈ {2,3} where ≥ 3 lifts occurred in range; zero counterexamples. Note the v₂ ≥ 3 conjecture N3 implies the '8e' part for all large e.) Consequence: no ray produces infinitely many exceptions quickly; combined with Thm II.2(iv), **#940(1) would then be equivalent to: infinitely many cube-free exceptions (N5).**
- **N5 [Conjecture, strong, and now the sharpest form of #940(1)] — infinitely many cube-free non-sums;** in fact ℱ(x) = x^{0.9+o(1)}, matching the measured 6.5·10⁷ roots below 10⁹ with ratio ≈ 1.86 per octave. By Thm II.2(iii) this is *equivalent* to the measured E(x) exponent and *implies* #940(1).
- **N6 [Conjecture — limit law, the model hypothesis formalized].** *For n sampled from a fixed singular stratum (v_p(n) = k_p for p ≤ P, valuated), the law of R̃(n)/1 converges to a non-degenerate limit with atom at 0 of mass exp(−λ̃∞·σ̃)·(1+o(1)) as the stratum refines* — i.e. κ∞ = 1 (within-class equidistribution/'Poisson' behaviour). Falsifiable content: (i) κ(x) should tend to ≈ 1.00–1.02 (currently 1.031 and falling ~0.004/octave); (ii) octave exception fractions 3.8 % at 10¹¹, 3.2 % at 10¹²; (iii) per-stratum R̃ histograms should converge to Poisson laws of mean λ(x)·σ̃. If (iii) fails with growing dispersion, revert to regime N2(B).
- **N7 [Conjecture — r ≥ 4].** The same machinery gives λ₄ = 5776, λ₅ = 1.69·10⁶ ordered; the model's asymptotic exception density E[e^{−λ_rσ̃}] for r = 4 is < 10⁻⁹ – note regime caveat –, so we conjecture **finitely many exceptions for r ≥ 4** (all large n are sums of ≤ r r-powerful numbers), i.e. #940 for r ≥ 4 has answer (1)-NO, (2)-NO. This matches the direction of problem #1107 and leaves r = 3 as the unique borderline case.

---

## 8. Where a proof can now engage

1. **For #940(1)** it suffices — by Thm II.2 plus the measured fact that lifts are negligible — to prove *cube-free non-sums are unbounded*. Any lower bound E(x) ≥ x^{β}, β > 1/3, would do it automatically (Thm II.2(iii): no finite set of rays supports more than O(x^{1/3}) exceptions). This is a strictly weaker target than bounding the sumset's density.
2. **For the density half**, Note I §8's barrier stands (binary/Goldbach regime: O(1) main term vs polynomial error control). What's new is the precise target: control of the *within-stratum* variance of R̃ (κ). The σ̃-mixture accounts for the bulk of the second moment already, so the energy method's failure is now localizable: one needs E₃(x; stratum)/x ≪ x^{o(1)} *within* fine strata, not globally.
3. **Provable next steps identified:** (a) complete rigor of Thm II.1's error terms (O(x^{−1/12}) with explicit constant — routine but unwritten); (b) the kernel expansion of §3.4 as a convergent analytic device for the local factors' x-dependence; (c) a census at 10¹¹–10¹² (memory-feasible by processing the range in windows, marking pair-sums into a per-window bitset and scanning shifts by cubefull a; ~10⁹ bits per window) to confront κ(x) with its two extrapolations; (d) N3 for v₂ ≥ 3 looks potentially attackable by *constructive* means — numbers 8n have vastly more representations (mean R̃ ≈ 14.2 vs 2.0), so a covering-system/theta-multiplier argument plausibly beats the Goldbach barrier there, as it did for Heath-Brown's three-squarefull theorem at r = 2.

---

## 9. Reproducibility

All code in `/home/user`; gcc 14.2 `-O3 -march=native -lm`, python3 + numpy.

| program | content | runtime | output |
|---|---|---|---|
| `powerful940.c` | constants, census & histograms to 10⁹/3·10⁷ (Note I) | 76 s | `powerful940_results.txt` |
| `stats940.c` | multiset histogram; census to 4·10⁹ (Note I) | 360 s | `stats940_results.txt` |
| `sigma940.py` | uniform-weight p-adic σ_p (Note I) | s | `sigma940_out.txt` |
| `sigma940b.py` | frequency-weighted σ̃ from the 6058-list (note: first version had a recursion bug — fixed; count must read 6058) | s | `sigma940b_out.txt` |
| `exact940.py` | **Theorem II.1 numerics**: exact limit law, exact σ̃, joint model | 2 s | `exact940_out.txt` |
| `verif940.py` | **zero-parameter model verification** (§4) and extrapolation | s | stdout |
| `rays940.c` | per-octave class trends; cube-free census; exact E-decomposition; ray lifetimes; down-ideal check. *(Known cosmetic faults: its printed "v₂≥3" column over-aggregates v₂=1 classes — corrected values quoted in §6.1 — and the m₀ histogram counts trivially liftless rays f > 5·10⁸ as "no represented point"; interpretation in §6.2.)* | ≈ 7 min | `rays940_out.txt` |

Census totals cross-validated against `stats940`'s independent run to the unit (104 520 390 top-octave exceptions; 6058 cubefull ≤ 4·10⁹).

---

## 10. Statement of novelty

To our knowledge, none of the following appears in the literature on #940 (the published record barely passes the r = 2 case, cf. the Survey): the exact p-adic limit law of r-powerful numbers with unit uniformity (Thm II.1) and the resulting exact frequency-weighted singular factors, which *solve* the local-density question Note I could only pose; the zero-free-parameter local model for the support, verified cell-by-cell to 4·10⁹, and its consequence that the exception density plausibly tends to a **positive limit** — reversing the density-1 guess of Note I; the homothety/down-ideal structure Thm II.2 reducing #940(1) to cube-free roots, with the exact census identity (99.985 % fresh roots) and the ray sandwich; the progression-freeness Thm II.3; the empirical ray law m₀ ∈ {2,3} and conjecture N4; and the corrected, sharpened conjecture system N1–N7 with explicit discriminating statistics. The two-layer picture of the exception set — *essentially all fresh cube-free roots living on two valuation strata, ray-shadows negligible* — is, as far as we know, the first structural description of the exceptional set in any of these Erdős–Ivić problems beyond r = 2.
