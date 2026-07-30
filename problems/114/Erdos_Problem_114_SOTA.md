# State of the Art: Erdős Problem #114

## Problem Statement

**Erdős Problem #114** is a long-standing question in complex analysis regarding the length of polynomial lemniscates. Originally posed by Paul Erdős, Fritz Herzog, and George Piranian in 1958, it asks:

> If $p(z) \in \mathbb{C}[z]$ is a monic polynomial of degree $n$, is the length of the curve $\{z \in \mathbb{C} : |p(z)| = 1\}$ maximised when $p(z) = z^n - 1$?

The problem currently carries a **$250 prize** (as reported by Borwein in 1995) and remains one of the prominent open problems in the study of polynomials.

## Background and Evolution of Bounds

Let the maximal length of such a curve for a degree $n$ polynomial be denoted by $f(n)$. The curve defined by $\{z \in \mathbb{C} : |p(z)| = 1\}$ is often referred to as a *lemniscate*. 

For the specific polynomial $p(z) = z^n - 1$, the length of the lemniscate is known to be $2n + O(1)$. Consequently, if the conjecture is true, it implies that $f(n) = 2n + O(1)$.

Historically, the bounds on $f(n)$ have been progressively tightened over several decades:

*   **1961**: E. P. Dolzhenko proved an upper bound of $f(n) \leq 4\pi n$. However, this work was not widely known at the time.
*   **1961**: Ch. Pommerenke independently proved a quadratic bound, $f(n) \ll n^2$.
*   **1995**: P. Borwein proved a linear bound $f(n) \ll n$, unaware of Dolzhenko's earlier result. 
*   **1999**: A. Eremenko and W. Hayman fully proved the conjecture for the base case $n = 2$ (proving the extremal level set is the Bernoulli Lemniscate) and established a general bound of $f(n) \leq 9.173n$.
*   **2007**: V. Danchenko improved the linear bound to $f(n) \leq 2\pi n$.
*   **2009**: A. Fryntov and F. Nazarov made significant asymptotic progress. They proved that $z^n - 1$ is a local maximizer and solved the problem asymptotically, showing that $f(n) \leq 2n + O(n^{7/8})$.

## State of the Art (Recent Breakthroughs)

The most significant recent development occurred in **December 2025**, marking a near-complete resolution of the problem. 

Fields Medalist **Terence Tao** released a preprint titled *"The maximal length of the Erdős–Herzog–Piranian lemniscate length in high degree"* (arXiv:2512.12455). Building upon the previous analytical framework established by Fryntov and Nazarov, Tao formally established the conjecture for all sufficiently large $n$. 

Tao proved that $p(z) = z^n - 1$ is indeed the **unique maximizer** (up to rotation and translation) for the length of the lemniscate as long as the degree $n$ is sufficiently large. 

### Current Status

Because of Tao's 2025 result, the problem is now solved asymptotically for high degrees. The general conjecture technically remains **Open** overall because it has not been verified for all small, finite values of $n$ strictly between $n=2$ (solved by Eremenko and Hayman) and the lower bound of Tao's "sufficiently large $n$". However, the overarching geometric intuition of Erdős, Herzog, and Piranian has been robustly vindicated.

## Related Result

Erdős, Herzog, and Piranian [EHP58] also asked a related question: if the interior region $\{z : |p(z)| < 1\}$ is connected, is the length of the boundary at least $2\pi$? 

This secondary question was completely resolved by Pommerenke in 1959, who proved it affirmatively, with the monomial $p(z) = z^n$ serving as the sharp example.

***
*Sources: Erdős Problems Database (erdosproblems.com), T. Tao (2025) arXiv:2512.12455, and historical references therein.*