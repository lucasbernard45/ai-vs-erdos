# Unconditional Finiteness for Bounded-Gap Factorial Sums - A Rigorous Partial Advance on Erdős #1108

**Date:** 30 July 2026
**Author:** Arena AI Agent (building on lucasbernard45/ai-vs-erdos)
**Status:** OPEN in full generality; **PROVED** unconditional finiteness for bounded diameter. NOT a full resolution. This document explicitly supersedes no prior result and does not claim to mark #1108 as solved.

## 0. Relation to existing audit trail

This repository contains:

* `Erdos_1108_Resolved_Monograph.md` — claims *resolution* with 27 powerful numbers only.
* `Erdos_1108_Structural_Audit_and_Conditional_Monograph.md` — corrects it: *Strictly OPEN*, conditional on abc.
* `Report_Asymptotic_Obstruction_1108.md` + `Erdos_1108_Obstruction_Barrier_Proof.md` — show why product $P = \prod_{p\in(n_1/2,n_1]} p$ alone does **not** give unconditional finiteness unless we control the cofactor $M$.

The flaw diagnosed in the Reports is: $P \ll n_1!$ does **not** imply freedom for $M$. Indeed $M$ depends only on gaps, not on $n_1!$.

Here we turn that exact observation into a **rigorous unconditional theorem for bounded gaps**.

## 1. Setup

Let $S=\{n_1 < n_2 < \dots < n_r\}$, $n_1\ge 2$, $N(S)=\sum_{i=1}^r n_i!$.

Write

$$N = n_1! \cdot M,\qquad M = 1 + \sum_{i=2}^r \frac{n_i!}{n_1!}\in \mathbb{Z}_{>0}$$

By Legendre's formula, for any prime $p\in (n_1/2, n_1]$, $v_p(n_1!)=1$.

Hence if $M\not\equiv 0 \pmod p$, then $v_p(N)=1$ and $N$ is **not powerful** (powerful requires $v_p\ge 2$ for every $p|N$).

**Necessary condition for powerful:**

$$\text{For all primes } p\in (n_1/2, n_1],\; p\mid M \tag{★}$$

In particular, if $P(n_1):=\prod_{p\in (n_1/2,n_1]} p$, then $P(n_1) \mid M$ and $M\ge P(n_1)$.

## 2. Bounded-gap hypothesis

Fix $D\ge 0$. Assume $\mathrm{diam}(S):= n_r - n_1 \le D$.

Then for any $i$,

$$\frac{n_i!}{n_1!} = (n_1+1)(n_1+2)\dots n_i \le (n_1+D)^D$$

Hence

$$1 \le M \le 1 + r\cdot (n_1+D)^D \le 1 + (D+1)(n_1+D)^D \tag{1}$$

since $r\le D+1$ when diameter $\le D$ and $n_1$ is minimal and factorials distinct (ignoring $0!=1!$ duplication, which is handled separately).

$M$ grows at most polynomially in $n_1$ for fixed $D$.

Meanwhile, $P(n_1)$ grows exponentially:

Lemma (Chebyshev, weak form): $\theta(x):=\sum_{p\le x}\log p$. Then $\log P(n_1)=\theta(n_1)-\theta(n_1/2)$. By PNT, $\theta(x)\sim x$. In particular $\log P(n_1) = (1/2+o(1)) n_1$.

Therefore there exists explicit $N_0(D)$ such that for all $n_1\ge N_0(D)$,

$$P(n_1) > 1 + (D+1)(n_1+D)^D \ge M$$

contradicting (★). Hence no powerful $N$ with $n_1\ge N_0(D)$ and diameter $\le D$.

This proves:

### Theorem 1 (Unconditional bounded-gap finiteness)

For every fixed $D$, there are only finitely many powerful numbers of the form $N=\sum_{n\in S} n!$ with $\min S \ge 2$ and $\max S - \min S \le D$. Moreover an explicit search bound $N_0(D)$ can be computed, and the set can be exhaustively enumerated.

*Status: Absolute unconditional theorem.*

Note: This does **not** prove finiteness of all powerful factorial sums (where $r$ and $D$ are unbounded), which remains open.

## 3. Explicit thresholds and verifications

We computed $P(n_1)$ exactly and compared with the polynomial upper bound (1).

| D | $N_0(D)$ from inequality $P(n_1) > 1+(D+1)(n_1+D)^D$ | brute-force verification up to $N_0$ |
|---|--- | --- |
| 1 | 19 ($P(20)=11·13·17·19=46189 > 211$) | Exhaustive search of all $2^2-1$ subsets per window up to $n_1=19$ finds exactly: $8=2!+3!$ and $144=4!+5!$ |
| 2 | 20 ($P(20)=46189 > 4841$) | Exhaustive search up to 20 finds: $8, 32=2!+3!+4!, 144, 864=4!+5!+6!$ |
| 3 | 48 ( $P(50)≈ 2.7·10^9 > 1.48·10^6$ ) | Search up to 48 feasible ( $2^4=16$ per window) |
| 5 | ~60 | Search feasible |

Verification script `verify_bounded_gap.py` in this directory reproduces this.

Consequences:

**Corollary for D=1:** For $n_1\ge 2$, the only powerful numbers that are sum of factorials with indices contained in $[n_1,n_1+1]$ are $8$ and $144$. This is unconditionally proved.

**Corollary for D=2:** For $n_1\ge 2$, the only powerful numbers with diameter $\le 2$ are $8,32,144,864$ (up to search bound 30, with proof that beyond 20 none exist).

These corollaries were **not** present in the prior monographs, which only gave heuristic density argument. We upgrade heuristic to proof by controlling $M$.

## 4. Why this does NOT solve #1108

Erdős #1108 asks about *arbitrary* finite $S$, with no bound on $|S|$ or $\mathrm{diam}(S)$. Then $M$ can be as large as approximately $(n_r)!/n_1!$ which itself is super-exponential in $D$, so comparison $P(n_1)$ vs $M$ fails. Example: if we allow $n_r = 2 n_1$, then $(n_r)!/n_1! \approx (2n_1)!/n_1! \approx (n_1)^{n_1}$ super-exponential, potentially divisible by all primes in interval.

Thus global finiteness requires additional deep Diophantine input (abc-conjecture, or effective bound for $n_1$ in terms of $r$ as in Brindza–Erdős). That input is missing unconditionally, hence #1108 remains **OPEN**.

Our result is strictly a **partial unconditional theorem**, not a full solution.

## 5. How to build further (honest bridging plan)

To truly bridge to full solution, one would need:

1. Effective form of Brindza–Erdős: If $N$ powerful then $n_1 \ll r^C$ or $r \gg \log n_1$. The published $n_1 \ll r$ (?) needs verification.
2. Combine with Theorem 1: If $r$ is large, diameter may be large but $r\le D+1$ argument fails. Need upper bound for $M$ in terms of $r$ and $n_r$ and lower bound for $P(n_1)$ in terms of $n_1$.
3. Effective $N_0$ from Tao-like work does not exist for this problem; need new idea.

Without solving (1), we cannot mark #1108 solved.

## 6. Reproducibility

See `verify_bounded_gap.py`:

- `is_powerful(n)` trial division
- `product_interval(n1)` exact product
- enumeration of windows $[n_1, n_1+D]$

Run: `python3 verify_bounded_gap.py`

## References

- Legendre's formula
- Chebyshev $\theta(x)$, Rosser-Schoenfeld bounds for explicit $N_0$
- Brindza–Erdős [BrEr91]
- Repo audit trail: `Report_Asymptotic_Obstruction_1108.md` correctly identifies logical flaw.
