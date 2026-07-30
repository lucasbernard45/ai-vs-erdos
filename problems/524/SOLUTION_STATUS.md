# Erdős Problem #524 — solution-status record

**Repository status:** solved externally by a public preprint; this repository does **not** claim authorship of the solution.

**Problem:** for i.i.d. Rademacher signs \(\varepsilon_k\), determine the almost-sure order of
\[
M_n=\max_{x\in[-1,1]}\left|\sum_{k=0}^n\varepsilon_kx^k\right|.
\]
Equivalently, under Lebesgue measure on \(t\in(0,1)\), take \(\varepsilon_k=(-1)^{\epsilon_k(t)}\) from the binary digits of \(t\).

## Resolution

Letwin and Sawhney, *On the maxima of Littlewood polynomials on* \([-1,1]\), arXiv:2604.19294v1 (21 April 2026), prove:

\[
\liminf_{n\to\infty}\frac{M_n}
{\sqrt n\,F^{-1}((\log n)^{-1/2})}=1
\quad\text{almost surely},
\]
where
\[
F(\delta)=\mathbb P\left(\sup_{u\geq0}
\left|\int_0^1e^{-us}\,dB_s\right|\leq\delta\right).
\]
They also prove
\[
\log F(\delta)=-\frac{2}{3\pi^2}\log^3(1/\delta)
+o\!\left(\log^3(1/\delta)\right),
\]
which yields
\[
\liminf_{n\to\infty}
\frac{\log(M_n/\sqrt n)}{(\log\log n)^{1/3}}
=-\left(\frac{3\pi^2}{4}\right)^{1/3}
\quad\text{almost surely}.
\]

These are Theorems 1.1 and 1.2 of the preprint. They give the sharp lower envelope requested in the Salem--Zygmund/Erdős formulation. Thus, subject to the usual independent checking of a new preprint, #524 should be recorded as **solved**.

## Scope and attribution

- This status follows the external paper, not any theorem first proved in this repository.
- `erdos_problem_524_universality_extension_attempt.md` concerns a separate proposed extension to more general coefficient laws. It must remain labelled **unverified** until checked independently.
- The Erdős Problems website may lag the preprint and should not be edited to “proved” without the site maintainer’s normal verification process.

## Sources

1. B. Letwin and M. Sawhney, [arXiv:2604.19294](https://arxiv.org/abs/2604.19294), v1, 21 April 2026. See Theorems 1.1 and 1.2.
2. [Erdős Problem #524](https://www.erdosproblems.com/524), original formulation and historical context.
3. `stateoftheart.md` in this directory, for a fuller proof map and chronology.
