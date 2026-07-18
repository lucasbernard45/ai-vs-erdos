# Erdős Problem #524 — State of the Art

**Prepared:** 18 July 2026  
**Status:** A very recent arXiv preprint gives a sharp lower-envelope theorem and, in the natural lower-envelope interpretation, resolves the problem. The result has not yet been peer reviewed or published in a journal. The Erdős Problems website still labels the entry “open,” but its discussion thread now links to this preprint; that label therefore appears not yet to reflect the April 2026 development.

---

## 1. Problem and probabilistic formulation

For almost every \(t\in(0,1)\), write the binary expansion
\[
t=\sum_{k\geq 1}\epsilon_k(t)2^{-k},\qquad \epsilon_k(t)\in\{0,1\},
\]
and set
\[
a_k(t)=(-1)^{\epsilon_k(t)}\in\{-1,1\}.
\]
With respect to Lebesgue measure in \(t\), the \(a_k(t)\) are i.i.d. Rademacher signs. Thus the question is equivalently about
\[
f_n(x)=\sum_{k=1}^{n} a_kx^k,\qquad
M_n=\max_{x\in[-1,1]}|f_n(x)|.
\]

The original request is to determine the “correct order of magnitude” of \(M_n\) almost surely. There are two distinct pathwise quantities:

1. **Upper envelope:** exceptionally large values as \(n\to\infty\), measured by a limsup.
2. **Lower envelope:** exceptionally small values along subsequences, measured by a liminf.

The lower envelope is the substantive content of the Salem–Zygmund/Erdős question. For a *fixed* \(n\), \(M_n\) is naturally of order \(\sqrt n\), while its almost-sure upper and lower subsequential behavior contains nontrivial iterated-logarithmic corrections.

> **Important formulation note.** The current statement on ErdősProblems.com is the corrected one: signs \((-1)^{\epsilon_k(t)}\), absolute values, and \(x\in[-1,1]\). A former formulation with \(0/1\) coefficients on \([0,1]\) is trivial because the polynomial is nonnegative and increasing there. The correction is documented in the site’s discussion thread.

---

## 2. Main result (2026)

Let
\[
F(\delta)=\mathbb P\left(\sup_{u\ge0}\left|\int_0^1e^{-us}\,dB_s\right|\le \delta\right),
\]
where \(B\) is standard Brownian motion.

### Exact lower-envelope formulation

Letwin and Sawhney prove that, almost surely,
\[
\boxed{\quad
\liminf_{n\to\infty}
\frac{M_n}{\sqrt n\,F^{-1}((\log n)^{-1/2})}=1.
\quad}
\]

They also obtain the sharp small-ball asymptotic
\[
\log F(\delta)
=-\frac{2}{3\pi^2}\log^3(1/\delta)+o\!\left(\log^3(1/\delta)\right)
\qquad(\delta\downarrow0).
\]
Combining the two yields
\[
\boxed{\quad
\liminf_{n\to\infty}
\frac{\log(M_n/\sqrt n)}{(\log\log n)^{1/3}}
=-\left(\frac{3\pi^2}{4}\right)^{1/3}.
\quad}
\]
Equivalently, along the lower envelope,
\[
M_n=
\sqrt n\,
\exp\!\left[-\left(\frac{3\pi^2}{4}\right)^{1/3}
(\log\log n)^{1/3}+o\!\left((\log\log n)^{1/3}\right)\right].
\]

The constant is approximately \(1.949\). This is substantially sharper than merely identifying the scale \(\sqrt n\exp(-\Theta((\log\log n)^{1/3}))\).

### Upper envelope

The classical result, already in Salem–Zygmund, is
\[
\boxed{\quad
\limsup_{n\to\infty}\frac{M_n}{\sqrt{2n\log\log n}}=1
\quad\text{a.s.}\quad}
\]
Thus the full known almost-sure envelope picture is
\[
\sqrt n\,e^{-C(\log\log n)^{1/3}}
\quad\text{on the lower envelope,}\qquad
\sqrt{2n\log\log n}
\quad\text{on the upper envelope},
\]
with the sharp lower-envelope constant \(C=(3\pi^2/4)^{1/3}\).

---

## 3. Chronology

| Date | Result | Significance |
|---|---|---|
| 1954 | Salem–Zygmund study random-sign series and random polynomials. | Establishes the classical framework; their LIL-based argument gives the sharp limsup law above. |
| 1961 | Erdős reiterates the question in *Some unsolved problems*. | Source cited for Erdős Problem #524. |
| Classical / reported on the problem page | Chung: for a.e. \(t\), infinitely many \(n\) satisfy \(M_n\ll\sqrt{n/\log\log n}\). | An early upper bound for the lower envelope; it shows much smaller values than \(\sqrt n\) recur. |
| Unpublished Erdős result (reported by the problem page) | For every \(\varepsilon>0\), \(M_n/n^{1/2-\varepsilon}\to\infty\) a.s. | Excludes polynomially smaller lower envelopes, but leaves a broad subpolynomial range. |
| 2010 | Gao–Li–Wellner prove \(\log F(\delta)\asymp-\log^3(1/\delta)\). | Identifies the Gaussian small-deviation exponent underlying the problem, but not its leading constant. |
| Jan. 2026 | Discussion of the endpoint/Gaussian-process reduction on the ErdősProblems forum. | Predicts the scale \(\sqrt n\exp[-\Theta((\log\log n)^{1/3})]\). |
| 21 Apr. 2026 | Letwin–Sawhney preprint posted. | Gives the inverse-small-ball lower-envelope law and the sharp constant. |

---

## 4. Why the Gaussian process appears

The maximum is controlled near the two endpoints \(x=1\) and \(x=-1\). Write
\[
x=\pm e^{-u/n},\qquad u\ge0.
\]
Then the normalized endpoint profiles are
\[
n^{-1/2}f_n(e^{-u/n}),\qquad n^{-1/2}f_n(-e^{-u/n}).
\]
A strong invariance principle (KMT coupling), applied after separating even and odd coefficients, approximates these profiles by two independent copies of
\[
Y(u)=\int_0^1e^{-us}\,dB_s.
\]

Consequently, a small value of \(M_n/\sqrt n\) is governed by the small-ball event
\[
\sup_{u\ge0}|Y(u)|\le\delta.
\]
The threshold for infinitely many such rare events over a suitable sparse sequence of scales is determined by \(F(\delta)\) at approximately probability \((\log n)^{-1/2}\). This explains the inverse \(F^{-1}((\log n)^{-1/2})\) in the sharp theorem.

### Deriving the constant

If
\[
F(\delta)\approx\exp\left[-\frac{2}{3\pi^2}\log^3(1/\delta)\right],
\]
then solving \(F(\delta)\approx(\log n)^{-1/2}\) gives
\[
\frac{2}{3\pi^2}\log^3(1/\delta)\sim\frac12\log\log n,
\]
hence
\[
\log(1/\delta)\sim\left(\frac{3\pi^2}{4}\log\log n\right)^{1/3}.
\]
This is exactly the lower-envelope exponent above.

---

## 5. Main ingredients of the 2026 proof

The Letwin–Sawhney preprint has two major components.

### A. Transfer from random signs to Brownian motion

- Reparameterize close to \(\pm1\) by \(x=\pm e^{-u/n}\).
- Use KMT strong approximation to couple partial sums of Rademacher variables to Brownian motion with sufficiently small uniform error.
- Use a sparse-scale/Borel–Cantelli argument. The lower-bound direction requires isolating a fresh independent coefficient block; the upper-bound direction follows from suitable rare-event estimates.
- Use a Gaussian \(B\)-inequality to control the continuity of the inverse small-ball function, avoiding the need for a much sharper error term than is available directly.

### B. Sharp small deviations for the Laplace-transform process

- Transform the process to a stationary Gaussian process with covariance
  \[
  \mathbb E[X_sX_t]=\tfrac12\operatorname{sech}\!\big((s-t)/2\big).
  \]
- Compare the weighted \(L^\infty\) small-ball event to an \(L^2\) small-ball event.
- Analyze the relevant covariance operator spectrally; its eigenvalue-counting asymptotics yield the cubic logarithmic rate.
- Obtain
  \[
  \log F(\delta)=-\frac{2}{3\pi^2}\log^3(1/\delta)+o(\log^3(1/\delta)).
  \]

This division is conceptually useful: the random-polynomial problem is reduced to a Gaussian small-deviation problem, and the leading constant is obtained from spectral analysis rather than from a direct combinatorial estimate on signs.

---

## 6. Relation to elementary random-walk bounds

Define
\[
S_k=\sum_{j\le k}a_j,\qquad T_k=\sum_{j\le k}(-1)^ja_j.
\]
Abel summation gives, for \(x\in[0,1]\),
\[
\sum_{k=1}^n a_kx^k
=S_nx^n+\sum_{k=1}^{n-1}S_k(x^k-x^{k+1}),
\]
where the coefficients are nonnegative and sum to \(1\). Applying the same argument to \(f_n(-x)\) yields
\[
|S_n|\vee |T_n|
\le M_n
\le \max_{k\le n}|S_k|\vee\max_{k\le n}|T_k|.
\]

This immediately supplies:

- sub-Gaussian fixed-\(n\) tails at the \(\sqrt n\) scale;
- the LIL upper-envelope law;
- useful but non-sharp information for the lower envelope.

It cannot determine the lower envelope exactly, because the upper comparison involves *maxima of all partial sums* and discards the smoothing structure of the polynomial for \(x\) slightly inside \(\pm1\). The endpoint-profile/Gaussian-process analysis preserves that structure.

---

## 7. What is resolved, and what remains open?

### Resolved, subject to verification of the 2026 preprint

Under the standard lower-envelope interpretation, the problem now has a sharp answer:

- the exact inverse-small-ball lower-envelope theorem;
- the logarithmic lower-envelope asymptotic with explicit leading constant;
- the classical exact upper-envelope limsup law.

The 2026 result also strictly strengthens the previously quoted unpublished Erdős lower bound: the factor
\[
\exp[-C(\log\log n)^{1/3}]
\]
decays more slowly than \(n^{-\varepsilon}\) for every fixed \(\varepsilon>0\).

### Caveats

1. **Preprint status.** As of 18 July 2026, the decisive result is arXiv:2604.19294v1, dated 21 April 2026. It should be cited as a preprint until independently refereed.
2. **Website metadata lag.** The ErdősProblems entry remains marked open, though the discussion thread points to the new paper. This should not be read as a current mathematical assessment after April 2026.
3. **Possible finer refinements.** The theorem fixes the leading logarithmic constant, but does not give a multiplicative \(1+o(1)\) asymptotic for \(M_n\) along its lower envelope in an elementary closed form. Its exact formulation is instead through \(F^{-1}\). Refining the small-ball asymptotics beyond the leading cubic-log term could yield lower-order corrections.

---

## 8. References and links

1. **B. Letwin and M. Sawhney**, *On the maxima of Littlewood polynomials on \([-1,1]\)*, arXiv:2604.19294 (v1, 21 April 2026).  
   - [Abstract and PDF](https://arxiv.org/abs/2604.19294)  
   - [HTML version](https://arxiv.org/html/2604.19294)

2. **R. Salem and A. Zygmund**, *Some properties of trigonometric series whose terms have random signs*, *Acta Mathematica* **91** (1954), 245–301. DOI: [10.1007/BF02393433](https://doi.org/10.1007/BF02393433).  
   - [Project Euclid record](https://projecteuclid.org/euclid.acta/1485892068)

3. **P. Erdős**, *Some unsolved problems*, *Publicationes Mathematicae Instituti Mathematici Academiae Scientiarum Hungaricae* **6** (1961), 221–254. (The source listed for #524 is p. 253.)

4. **F. Gao, W. V. Li, and J. A. Wellner**, *How many Laplace transforms of probability measures are there?*, *Proceedings of the American Mathematical Society* **138** (2010), 4331–4344; [arXiv:1001.0200](https://arxiv.org/abs/1001.0200).  
   Earlier work establishing the \(\log^3(1/\delta)\) small-deviation scale relevant to the Gaussian reduction.

5. **Erdős Problem #524**, Thomas F. Bloom (editor), [erdosproblems.com/524](https://www.erdosproblems.com/524).  
   - [Discussion thread](https://www.erdosproblems.com/forum/thread/524?order=oldest), including the corrected formulation and the link to the 2026 preprint.

---

## Bottom line

The best current answer is no longer merely
\[
M_n=\sqrt n\exp\big(-\Theta((\log\log n)^{1/3})\big)
\quad\text{infinitely often}.
\]
The April 2026 preprint identifies the sharp lower-envelope exponent:
\[
\boxed{
\liminf_{n\to\infty}
\frac{\log(M_n/\sqrt n)}{(\log\log n)^{1/3}}
=-\left(\frac{3\pi^2}{4}\right)^{1/3}
}
\]
almost surely, alongside the classical upper-envelope identity
\[
\boxed{
\limsup_{n\to\infty}\frac{M_n}{\sqrt{2n\log\log n}}=1.
}
\]
