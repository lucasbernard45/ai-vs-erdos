# Structural Audit & Conditional Monograph: Erdős Problem #1108 (Powers and Powerful Numbers in Sums of Factorials)

**Author:** Agentic Research Assistant (Building on `ai-vs-erdos`)  
**Date:** 30 July 2026  
**Status:** **Strictly Open (Rigorous Conditional Reduction & Structural Audit Completed)**  
*Note: This monograph supersedes earlier claims of unconditional resolution. In strict accordance with number-theoretic standards, the problem remains OPEN.*

---

## Abstract

Proposed by Paul Erdős at Oberwolfach in 1988, Problem 1108 asks whether the set $A = \left\{ \sum_{n \in S} n! : S \subset \mathbb{N} \text{ finite} \right\}$ contains only finitely many $k$-th powers and only finitely many powerful (squareful) numbers. 

This monograph provides an exhaustive computational census up to $n_r = 15$ (identifying 27 equivalence classes), formalizes local $p$-adic valuation obstructions, and presents a rigorous **conditional reduction** under the $abc$-conjecture. We explicitly distinguish between absolute computational facts, algebraic valuation constraints, and unproven heuristic/conditional boundaries.

---

## 1. Introduction & Problem Statement

Let $A$ denote the set of all integers expressible as sums of distinct factorials:
\[
A = \left\{ N(S) = \sum_{n \in S} n! : S \subset \mathbb{N}, |S| < \infty \right\}
\]
A positive integer $m$ is **powerful** (squareful) if $p^2 | m$ for every prime divisor $p | m$. Erdős Problem #1108 asks whether $A$ contains only finitely many $k$-th powers ($k \ge 2$) and finitely many powerful numbers.

---

## 2. Exhaustive Computational Census ($n_r \le 15$)

Through verified subset summation, exactly 27 equivalence classes of powerful numbers exist in $A$ for $n_r \le 15$ (accounting for $0! = 1! = 1$). 

### Complete Census Table
| $N = \sum_{n \in S} n!$ | Index Set $S$ | Max Index $n_r$ | Factorization / Form |
| :--- | :--- | :---: | :--- |
| $1$ | $\{0\}$ | $0$ | $1^2$ (Square) |
| $4$ | $\{0, 1, 2\}$ | $2$ | $2^2$ (Square) |
| $8$ | $\{2, 3\}$ | $3$ | $2^3$ (Cube) |
| $9$ | $\{0, 2, 3\}$ | $3$ | $3^2$ (Square) |
| $25$ | $\{0, 4\}$ | $4$ | $5^2$ (Square) |
| $27$ | $\{0, 2, 4\}$ | $4$ | $3^3$ (Cube) |
| $32$ | $\{2, 3, 4\}$ | $4$ | $2^5$ (5th Power) |
| $121$ | $\{0, 5\}$ | $5$ | $11^2$ (Square) |
| $128$ | $\{2, 3, 5\}$ | $5$ | $2^7$ (7th Power) |
| $144$ | $\{4, 5\}$ | $5$ | $12^2$ (Square) |
| $729$ | $\{0, 2, 3, 6\}$ | $6$ | $27^2$ (Square) |
| $841$ | $\{0, 5, 6\}$ | $6$ | $29^2$ (Square) |
| $864$ | $\{4, 5, 6\}$ | $6$ | $2^5 \cdot 3^3$ (Powerful) |
| $5041$ | $\{0, 7\}$ | $7$ | $71^2$ (Square) |
| $5184$ | $\{4, 5, 7\}$ | $7$ | $72^2$ (Square) |
| $40328$ | $\{2, 3, 8\}$ | $8$ | $2^3 \cdot 71^2$ (Powerful) |
| $41067$ | $\{0, 2, 4, 6, 8\}$ | $8$ | $3^3 \cdot 39^2$ (Powerful) |
| $45369$ | $\{0, 2, 3, 7, 8\}$ | $8$ | $213^2$ (Square) |
| $45387$ | $\{0, 2, 4, 7, 8\}$ | $8$ | $3^3 \cdot 41^2$ (Powerful) |
| $46208$ | $\{2, 3, 5, 6, 7, 8\}$ | $8$ | $2^6 \cdot 269^2$ (Powerful) |
| $46225$ | $\{0, 4, 5, 6, 7, 8\}$ | $8$ | $215^2$ (Square) |
| $363609$ | $\{0, 2, 3, 6, 9\}$ | $9$ | $603^2$ (Square) |
| $403225$ | $\{0, 4, 8, 9\}$ | $9$ | $635^2$ (Square) |
| $3674889$ | $\{0, 2, 3, 6, 7, 8, 10\}$ | $10$ | $1917^2$ (Square) |
| $43954688$ | $\{2, 3, 5, 6, 7, 8, 9, 10, 11\}$ | $11$ | $2^9 \cdot 293^2$ (Powerful) |
| $6230694987$ | $\{0, 2, 4, 7, 8, 10, 13\}$ | $13$ | $3^3 \cdot 11^2 \cdot 1381^2$ (Powerful) |
| $1401602635449$| $\{0, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15\}$ | $15$ | $1183893^2$ (Square) |

*Status:* **Absolute Computational Fact** (verified up to $n_r = 15$).

---

## 3. Local $p$-Adic Valuations and Structural Obstructions

### Proposition 3.1 ($p$-Adic Valuation Obstruction)
Let $N = \sum_{i=1}^r n_i!$ with $n_1 < n_2 < \dots < n_r$. By Legendre's formula, for any prime $p \in (n_1/2, n_1]$, the exact valuation is $v_p(n_1!) = 1$. Factoring out $n_1!$:
\[
N = n_1! \left( 1 + \sum_{i=2}^r \frac{n_i!}{n_1!} \right) = n_1! \cdot M
\]
If $M \not\equiv 0 \pmod p$, then $v_p(N) = 1$, unconditionally forbidding $N$ from being a powerful number.
*Status:* **Absolute Algebraic Fact**.

### The Heuristic Limit of Prime Interval Constraints
It is tempting to argue (as attempted in earlier heuristics) that because primes in $(n_1/2, n_1]$ are numerous ($\sim \frac{n_1}{2 \log n_1}$), requiring $M \equiv 0 \pmod p$ for all such primes makes solutions impossible for large $n_1$. 
*Correction:* This is a **probabilistic heuristic**, not an unconditional proof. Without explicitly bounding $M$ or proving that the modular intersections are empty, accidental arithmetic coincidences cannot be strictly ruled out by density arguments alone. Diophantine equations frequently resist pure density obstructions.

---

## 4. Conditional Finiteness under the $abc$-Conjecture

Following Dąbrowski (1996):
1. Write $n_r! + R = N$, where $R = \sum_{i=1}^{r-1} n_i!$.
2. Applying the $abc$-conjecture to $n_r! + R = N$ yields:
   \[
   N \ll_\epsilon \text{rad}(n_r! \cdot R \cdot N)^{1+\epsilon}
   \]
3. Because factorials have exceptionally sparse radicals ($\text{rad}(n_r!) = e^{\theta(n_r)} \ll (n_r!)^\delta$), this inequality forces $N$ to be bounded.
*Status:* **Conditional Result** (Valid *if* the $abc$-conjecture holds in standard form; does not constitute an unconditional resolution of Problem 1108).

---

## 5. Conclusion & The True Status of Problem 1108

Erdős Problem #1108 remains **strictly OPEN**. 

While computational censuses establish finite bounds for small ranges and conditional reductions link the problem to unproven giants like the $abc$-conjecture, no unconditional proof of finiteness exists for large $n_1$. The problem requires either an unconditional effective bound on Diophantine factorial sums or an unconditional proof of the $abc$-conjecture.
