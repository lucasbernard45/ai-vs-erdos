# Erdős #524: A Universality Extension Beyond Rademacher Coefficients

**Research note — 18 July 2026**  
**Status:** rigorous proof adaptation proposed; **novelty not independently certified**.  

## Claim of this note

The April 2026 Letwin–Sawhney preprint treats i.i.d. Rademacher coefficients. Its proof appears to extend, with only explicit routine replacements, to every centered i.i.d. coefficient law having nonzero finite variance and a finite exponential moment in a neighborhood of zero.

I did not find this extension stated in the preprint or in the targeted literature search. That makes it a plausible **new extension**, but not a certified novel result: an author or specialist may know it as an immediate corollary. The purpose of this note is to make the extension precise and give an audit trail for every place where the Rademacher law enters.

---

## 1. The proposed universality theorem

Let \((\xi_k)_{k\ge0}\) be i.i.d. real random variables satisfying
\[
\mathbb E\xi_0=0,\qquad \mathbb E\xi_0^2=\sigma^2\in(0,\infty),
\qquad \mathbb E e^{\lambda|\xi_0|}<\infty
\quad\text{for some }\lambda>0. \tag{H}
\]
Set
\[
P_n(x)=\sum_{k=0}^n\xi_kx^k,
\qquad \mathcal M_n=\sup_{x\in[-1,1]}|P_n(x)|.
\]
Let
\[
Y(t)=\int_0^1e^{-ts}\,dB_s,
\qquad
F(u)=\mathbb P\left(\sup_{t\ge0}|Y(t)|\le u\right),
\]
and define \(b_n=F^{-1}((\log n)^{-1/2})\).

> ### Theorem U (universality of the sharp lower envelope)
> Under (H), almost surely,
> \[
> \boxed{
> \liminf_{n\to\infty}\frac{\mathcal M_n}{\sigma\sqrt n\,b_n}=1.
> } \tag{U1}
> \]
> Consequently,
> \[
> \boxed{
> \liminf_{n\to\infty}
> \frac{\log(\mathcal M_n/(\sigma\sqrt n))}{(\log\log n)^{1/3}}
> =-\left(\frac{3\pi^2}{4}\right)^{1/3}.
> } \tag{U2}
> \]

The statement includes non-symmetric, continuous, lattice, and bounded centered laws. It does **not** include non-centered laws: a nonzero mean produces a deterministic order-\(n\) contribution near \(x=1\), so a different problem results.

---

## 2. Why the result is a meaningful extension

The initial Erdős problem has signs as coefficients, and the 2026 preprint is explicitly a theorem for random Littlewood polynomials. The proposed theorem says that the sharp lower-envelope constant is determined solely by the variance-normalized Brownian limit, not by the coefficient distribution, under an exponential-moment assumption.

This is stronger than a finite-dimensional CLT assertion. The event
\[
\{\mathcal M_n\le \sigma\sqrt n\, b_n\}
\]
has probability on the order of \(1/\log n\) at the relevant scale, and the proof must preserve this rare-event scale over sparse subsequences. Ordinary weak convergence is inadequate; a strong approximation with a uniform error much smaller than \(b_n\) is needed.

---

## 3. Main transfer lemma

The only probabilistic input specific to the coefficient law is KMT coupling.

### Lemma U.1 (uniform two-endpoint Gaussian coupling)
Under (H), there is a coupling of \((\xi_k)_{0\le k\le n}\) with two independent copies \(Y_+,Y_-\) of \(Y\) such that, for every fixed \(A>0\),
\[
\mathbb P\!\left(
\sup_{t\ge0}\left|
\frac{P_n(e^{-t/n})}{\sigma\sqrt n}-Y_+(t)
\right|
+
\sup_{t\ge0}\left|
\frac{P_n(-e^{-t/n})}{\sigma\sqrt n}-Y_-(t)
>C_A\frac{\log n}{\sqrt n}
\right)\le C_A n^{-A}. \tag{3.1}
\]

### Proof
Split into even and odd subsums,
\[
E_n(t)=\frac1{\sigma\sqrt n}\sum_{\substack{k\le n\\k\ \mathrm{even}}}\xi_ke^{-kt/n},
\qquad
O_n(t)=\frac1{\sigma\sqrt n}\sum_{\substack{k\le n\\k\ \mathrm{odd}}}\xi_ke^{-kt/n}.
\]
They are independent because they use disjoint coefficient sets. KMT, valid under (H), couples each reindexed partial-sum process to an independent Brownian motion with error \(O(\log n)\), except on an event of probability \(O(n^{-A})\). After scaling by \(\sigma\sqrt n\), the two errors are \(O((\log n)/\sqrt n)\).

For the even process, write its partial-sum error as \(R_e(s)\). Summation by parts/integration by parts gives
\[
\int_0^1e^{-ts}\,dR_e(s)
=e^{-t}R_e(1)+\int_0^1te^{-ts}R_e(s)\,ds.
\]
Since
\[
\sup_{t\ge0}\int_0^1te^{-ts}\,ds\le1,
\]
this contribution is bounded uniformly in \(t\) by \(2\|R_e\|_\infty\); similarly for the odd process. Brownian continuity fills the lattice interpolation gap.

The Gaussian limits of \(E_n\) and \(O_n\) are independent copies with covariance one-half that of \(Y\). Their sum and difference therefore yield independent copies
\[
Y_+=Y_e+Y_o,\qquad Y_-=Y_e-Y_o
\]
of \(Y\). Since \(P_n(e^{-t/n})/(\sigma\sqrt n)=E_n(t)+O_n(t)\) and the negative-endpoint profile is the difference, (3.1) follows. ∎

**Distributional point worth noting.** Symmetry of \(\xi_0\) is not used. The independence of the two *Gaussian limiting endpoint profiles* comes from the orthogonal sum/difference transformation of independent even and odd Brownian motions, not from symmetry of the original coefficient law.

---

## 4. Comparison with the Rademacher proof: complete dependency audit

Below, “replacement” means the cited Rademacher step can be replaced without changing the conclusion or scale.

| Component in Letwin–Sawhney | Rademacher-specific feature | Replacement under (H) |
|---|---|---|
| Endpoint profile reduction | \(|f_n(0)|=1\) | Replace by \(|\xi_0|\). Since \(|\xi_0|/(\sigma\sqrt n b_n)\to0\) a.s., this has no effect. |
| KMT coupling | signs | Standard KMT theorem under a finite exponential moment after variance normalization. |
| Even/odd decomposition | signs | Disjoint i.i.d. subsequences remain independent; no symmetry needed. |
| Uniform interpolation between nearby degrees | bounded random-walk increments | Bernstein’s maximal inequality for centered variables satisfying (H), replacing the bounded-increment Hoeffding/reflection estimate. |
| Lower-envelope mesh bound | coupling plus Gaussian small-ball estimate | Lemma U.1 has the same \(O(\log n/\sqrt n)\) normalized error, which is \(o(b_n)\). |
| Infinitely-often (“fresh block”) part | independent Rademacher blocks | Independent i.i.d. blocks; Lemma U.1 applies to each. |
| Negligibility of old block | Rademacher LIL/upper bound | Apply the i.i.d. LIL to \(\sum\xi_k\) and the independent, centered, variance-homogeneous (but if nonsymmetric not identically distributed) alternating sequence \(\sum(-1)^k\xi_k\); the standard independent-variable LIL, or a maximal Bernstein/Borel–Cantelli bound, is sufficient with the same sparse scales. |

No step uses an exact identity special to \(\xi_k\in\{-1,1\}\), apart from the harmless value at \(x=0\).

---

## 5. Details for the one non-identical estimate: modulus in the degree variable

The Rademacher proof controls, within a dyadic block \([N,2N]\),
\[
\max_{|n-m|\le\Delta N}\|P_n-P_m\|_{\infty}.
\]
For general coefficients, it is enough to establish the following analogue.

### Lemma U.2 (degree-modulus estimate at the required mesh scale)
Fix \(A>0\), put \(s_N=(\log\log N)^{1/3}\), and let
\[
\Delta_N=e^{-As_N}.
\]
There are constants \(C,c>0\), depending only on the law of \(\xi_0\) and on \(A\), such that
\[
\mathbb P\left(
\max_{\substack{m,n\in[N,2N]\\|n-m|\le\Delta_N N}}
\|P_n-P_m\|_{\infty}
>C\sqrt{\Delta_N N}\sqrt{\log(1/\Delta_N)+\log\log N}
\right)
\ll (\log N)^{-2}. \tag{5.1}
\]

### Proof
For an interval of indices \(I\) of length \(L\le2\Delta_N N+1\), Abel summation gives for \(0\le x\le1\)
\[
\left|\sum_{k\in I}\xi_kx^k\right|
\le\max_{r\le L}\left|\sum_{j=1}^r\xi_{u+j}\right|.
\]
The negative half interval is handled by replacing \(\xi_k\) with \((-1)^k\xi_k\), which preserves independence, centering, variance, and the exponential-moment bound.

The maximal Bernstein inequality for partial sums of centered variables satisfying (H) gives
\[
\mathbb P\left(\max_{r\le L}\left|\sum_{j=1}^r\xi_{u+j}\right|>v\right)
\le 2\exp\left[-c\min\left(\frac{v^2}{L},v\right)\right]. \tag{5.2}
\]
Cover all pairs \((m,n)\) with \(|n-m|\le\Delta_NN\) by \(O(\Delta_N^{-1})\) overlapping index intervals of length at most \(2\Delta_NN+1\). Put
\[
v=C\sqrt{\Delta_N N}\sqrt{\log(1/\Delta_N)+\log\log N}.
\]
Now \(\Delta_NN=N\exp(-A(\log\log N)^{1/3})\to\infty\) faster than every power of \(\log N\). Hence \(v=o(\Delta_NN)\), so the quadratic regime in (5.2) applies for all sufficiently large \(N\). A union bound gives
\[
\Delta_N^{-1}\exp\{-cC^2(\log(1/\Delta_N)+\log\log N)\}
\ll (\log N)^{-2}
\]
when \(C\) is sufficiently large. This proves (5.1). ∎

### Why the restriction is necessary
The same assertion is **false** uniformly down to \(\Delta=N^{-1}\) for unbounded coefficient laws: then a difference \(P_{n+1}-P_n=\xi_{n+1}x^{n+1}\) contains a single coefficient, and the maximum of \(N\) such coefficients need not be \(O(\sqrt{\log N})\). The Rademacher proof can cover that endpoint because individual increments are bounded. The lower-envelope proof, however, only uses the mesoscopic scale \(\Delta_N=e^{-As_N}\), where the corrected lemma is exactly sufficient.

This correction removes the only bounded-coefficient obstruction in the proof transfer.

---

## 6. Derivation of Theorem U from the transfer lemma

This section explains why the original proof can be reused once Lemmas U.1 and U.2 are available.

### 6.1 Lower bound for the liminf

Let
\[
\mathcal A_n=\{\mathcal M_n\le(1-\eta)\sigma\sqrt n b_n\}.
\]
On a geometric mesh of a dyadic block \([N,2N]\), Lemma U.2 reduces \(\bigcup_{n\in[N,2N]}\mathcal A_n\) to a union over \(O(e^{A(\log\log N)^{1/3}})\) mesh points. Lemma U.1 transfers each mesh event to the event that both independent Gaussian endpoint processes are bounded by \((1-c\eta)b_n\). Its probability is
\[
F((1-c\eta)b_n)^2.
\]
The small-ball continuity estimate used by Letwin–Sawhney gives
\[
F((1-c\eta)b_n)^2
\le F(b_n)^2\exp[-c_\eta\log^2(1/b_n)].
\]
Since \(F(b_n)^2=(\log n)^{-1}\) and \(\log(1/b_n)\asymp(\log\log n)^{1/3}\), the mesh union probabilities are summable over dyadic \(N\). Borel–Cantelli yields
\[
\liminf_n\frac{\mathcal M_n}{\sigma\sqrt n b_n}\ge1.
\]

### 6.2 Upper bound for the liminf

Choose sparse block endpoints \(N_j\) as in the Rademacher proof and write
\[
P_{N_{j+1}}(x)=P_{N_j}(x)+x^{N_j+1}G_j(x),
\]
where \(G_j\) uses the fresh coefficient block \((N_j,N_{j+1}]\). The events
\[
\left\{\|G_j\|_\infty\le(1+\eta)\sigma\sqrt{M_j}b_{M_j}\right\}
\]
are independent. Lemma U.1 and the Gaussian event with two endpoint copies give their probabilities at least
\[
F(b_{M_j})^2-o(1/\log M_j)
\asymp\frac1{\log M_j}.
\]
Their sum diverges, so second Borel–Cantelli gives infinitely many favorable fresh blocks.

The old part is negligible because Abel summation bounds \(\|P_{N_j}\|_\infty\) by the maxima of the ordinary and alternating partial sums. The i.i.d. LIL controls the ordinary sum; the standard LIL for independent centered variables with common variance and a uniform exponential moment controls the alternating sum (which need not be identically distributed when the law is nonsymmetric). Hence
\[
\|P_{N_j}\|_\infty=O\!\left(\sigma\sqrt{N_j\log\log N_j}\right)
\quad\text{a.s.},
\]
and the chosen sparseness makes this \(o(\sigma\sqrt{N_{j+1}}b_{N_{j+1}})\). Thus
\[
\liminf_n\frac{\mathcal M_n}{\sigma\sqrt n b_n}\le1.
\]
Together with §6.1, this proves (U1). Equation (U2) follows from the same Gaussian small-ball asymptotic used in the Rademacher theorem.

---

## 7. Limits of the claim

### What has been established in this note

- A precise extension is formulated.
- The Rademacher-only points in the published-preprint proof are identified.
- The two required replacements (KMT and maximal Bernstein) are standard and are given explicitly.
- The rest of the proof is structurally unchanged, including the constants.

### What has *not* been established

- I have not checked whether this universality extension appears in a paper, a revised arXiv version, or unpublished notes after 18 July 2026.
- This note is not peer reviewed.
- “Genuinely novel” should therefore be interpreted as **a credible new theorem candidate not found in the source paper or targeted searches**, not a priority claim.

A publication-quality version should: cite a precise KMT formulation for (H); spell out the general-coefficient version of every lemma in Sections 3 and 5 of Letwin–Sawhney; and obtain author/literature feedback on priority.

---

## 8. Why this is a better novelty candidate than a new proof of #524

The original problem’s Rademacher case now has a sharp lower-envelope theorem. The extension above:

1. changes the mathematical class of random polynomials;
2. retains the same explicit constant;
3. requires an actual rare-event strong-approximation argument, not merely a central-limit heuristic; and
4. appears not to be stated by the paper that solved the Rademacher case.

If confirmed absent from the literature, Theorem U is a genuine generalization rather than a restatement.

---

## References

1. B. Letwin and M. Sawhney, *On the maxima of Littlewood polynomials on \([-1,1]\)*, arXiv:2604.19294 (2026). [HTML](https://arxiv.org/html/2604.19294).
2. J. Komlós, P. Major, and G. Tusnády, strong approximation theorems for sums of independent random variables (1975–1976). The finite-exponential-moment version is the standard KMT input.
3. F. Gao, W. V. Li, and J. A. Wellner, *How many Laplace transforms of probability measures are there?*, Proc. Amer. Math. Soc. 138 (2010), 4331–4344. [arXiv:1001.0200](https://arxiv.org/abs/1001.0200).
