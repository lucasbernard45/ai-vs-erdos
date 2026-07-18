# State of the art: Erdős Problem #940

**Problem page:** [Erdős Problems #940](https://www.erdosproblems.com/940)  
**Literature check completed:** 18 July 2026  
**Status:** **open** for every stated case \(r\geq 3\).

## 1. The question

Call a positive integer \(r\)-powerful (also *\(r\)-full*) when every prime occurring in its factorisation occurs to exponent at least \(r\):
\[
p\mid n\quad\Longrightarrow\quad p^r\mid n.
\]
For a fixed \(r\geq3\), let
\[
\mathcal P_r=\{n\geq1:n\text{ is }r\text{-powerful}\},\qquad
S_r=\underbrace{\mathcal P_r+\cdots+\mathcal P_r}_{\text{at most }r\text{ summands}}.
\]
(Essentially, “at most” may be handled by allowing zero, if desired.) Erdős asked:

1. Are infinitely many positive integers outside \(S_r\)?
2. More strongly, does \(S_r\) have natural density zero?
   \[
   \lim_{x\to\infty}\frac{|S_r\cap[1,x]|}{x}=0?
   \]

The second assertion would imply the first, but the first is not presently known either.

## 2. Executive summary

* No proof or disproof of either assertion is known for the problem as posed (\(r\geq3\)). The problem page remained marked **OPEN** at the time of this check and was last edited on 3 November 2025.
* The first proposed argument in the literature does **not** work: Erdős wrote that a simple counting argument showed that not all sufficiently large integers were representable, but Schinzel found an error.
* The boundary case \(r=2\) is completely different and is understood: sums of two squarefull numbers have density zero. In fact their counting function has a substantially stronger upper bound.
* Already for \(r=3\), the requested density-zero conclusion would settle a familiar hard special case: every cube is 3-powerful, so it would imply that the integers representable as a sum of at most three non-negative cubes have density zero. This is still unknown.
* No newer paper located in the searches conducted here resolves the \(r\geq3\) problem. This is a literature snapshot, not a proof of completeness; the site itself explicitly cautions that its open-status annotation may miss literature.

## 3. Why naïve counting is critical

The number of \(r\)-powerful integers up to \(x\) is sparse—of order \(x^{1/r}\) for fixed \(r\). Thus the number of **ordered** \(r\)-tuples of \(r\)-powerful summands of size at most \(x\) is only of order \(x\). This is exactly the critical exponent: it does **not** give an \(o(x)\) bound for the number of values of their sum.

Consequently, merely counting possible tuples cannot prove density zero, and it cannot exclude the possibility that all sufficiently large integers are represented. One would need to exploit collisions between representations, local restrictions, or more refined arithmetic structure. This explains both the temptation of the original “simple counting” claim and why Schinzel’s correction matters.

For \(r=3\), a particularly stark obstruction is
\[
\{a^3+b^3+c^3:a,b,c\geq0\}\subseteq S_3.
\]
Hence a density-zero theorem for \(S_3\) would automatically give density zero for sums of three cubes. The latter is an outstanding problem; it should not be confused with the *solvability for a fixed integer* of the signed sum-of-three-cubes equation.

## 4. The solved benchmark \(r=2\)

Although #940 only asks \(r\geq3\), the squarefull case is the principal benchmark.

A 2-powerful number is a squarefull number. Every squarefull number has the form
\[
a^2b^3 \quad (b\text{ squarefree}),
\]
which connects sums of squarefull numbers to binary quadratic forms after fixing the cube factors.

Let \(A(x)\) be the number of integers \(n\leq x\) representable as a sum of two squarefull numbers. Then:

* **Baker and Brüdern (1994)** first proved the density-zero result required in this analogue of #940.
* **Odoni (1981)** had already shown that the most direct Landau-type guess for the precise order of \(A(x)\) is false, including the lower bound
  \[
  A(x)\gg \exp\!\left(c\frac{\log\log\log x}{\log\log x}\right)
  \frac{x}{\sqrt{\log x}}
  \]
  for some \(c>0\).
* **Blomer and Granville (2006)** obtained the currently cited upper estimate
  \[
  A(x)=(\log\log x)^{O(1)}\frac{x}{(\log x)^{\alpha}},
  \qquad \alpha=1-2^{-1/3}\approx0.206299.
  \]
  In particular \(A(x)=o(x)\).

This result is useful orientation, but it does not generalise automatically to \(r\geq3\): the argument relies on the exceptional structure of the critical two-summand/squarefull setting and on estimates for binary quadratic forms.

### An informal route to the \(r=2\) result

A recent discussion on the problem page records Terence Tao’s suggested route. Write two squarefull summands as \(c^3a^2\) and \(d^3b^2\). After truncating the cube factors \(c,d\), whose tails can be controlled by a convergent sum, one is led for fixed \(c,d\) to represented values of a positive binary quadratic form. Landau-type density-zero results for those forms supply the conclusion. This is a helpful explanation, not a replacement for the published proofs above.

## 5. Contrast: additive bases

The nearby positive theorem should not be read as evidence for #940:

> **Heath-Brown (1988):** every sufficiently large integer is a sum of at most **three** squarefull (2-powerful) numbers.

Thus squarefull numbers are eventually an additive basis of order 3, while their two-fold sumset has density zero. #940 asks at the corresponding critical number of summands—\(r\) summands for \(r\)-powerful numbers—whether the sumset remains sparse when \(r\geq3\). For \(r=2\), the critical two-summand sumset is sparse but adding one summand gives eventual coverage.

The related Erdős Problems page [#1107](https://www.erdosproblems.com/1107) asks whether \(r+1\) \(r\)-powerful summands suffice for all large integers. It too is open in the general \(r\geq3\) setting.

## 6. Historical record and corrections

* Erdős posed the question in *Problems and results on number theoretic properties of consecutive integers and related questions* (1976, p. 33).
* The 1986 Oberwolfach problem book records it as a problem of **Erdős and Ivić**.
* Erdős stated that a “simple counting argument” proved infinitely many omissions. As recorded on #940, **Schinzel pointed out a mistake**. The corrected historical claim is only that the asserted simple argument does not establish the result.
* The #940 discussion in October 2025 clarified the \(r=2\) record: Baker–Brüdern is the first published proof cited there; the sharper later work is by Blomer and Granville.

## 7. What is and is not known

| Statement | Status |
|---|---|
| \(S_r\) has density zero for every fixed \(r\geq3\) | Open |
| Infinitely many integers are not in \(S_r\), \(r\geq3\) | Open |
| Sums of at most three cubes have density zero | Open; a consequence of the \(r=3\) density-zero assertion |
| Sums of two squarefull numbers have density zero | Proved |
| Every sufficiently large integer is a sum of at most three squarefull numbers | Proved (Heath-Brown) |

## 8. Primary and secondary references

1. P. Erdős, *Problems and results on number theoretic properties of consecutive integers and related questions*, Proceedings of the Fifth Manitoba Conference on Numerical Mathematics (1976), 25–44. [Problem page record](https://www.erdosproblems.com/latex/940).
2. R. C. Baker and J. Brüdern, [*On sums of two squarefull numbers*](https://doi.org/10.1017/S0305004100072340), *Mathematical Proceedings of the Cambridge Philosophical Society* **116** (1994), 1–5.
3. D. R. Heath-Brown, *Ternary quadratic forms and sums of three square-full numbers*, *Séminaire de Théorie des Nombres, Paris 1986–87* (1988), 137–163. Listed at [#940](https://www.erdosproblems.com/940) and [#941](https://www.erdosproblems.com/941).
4. R. W. K. Odoni, *A problem of Erdős on sums of two squarefull numbers*, *Acta Arithmetica* (1981), 145–162. Bibliographic record at [#1081](https://www.erdosproblems.com/latex/1081).
5. V. Blomer, *Binary quadratic forms with large discriminants and sums of two squareful numbers*, *Journal für die reine und angewandte Mathematik* (2004), 213–234. Bibliographic record at [#1081](https://www.erdosproblems.com/latex/1081).
6. V. Blomer and A. Granville, *Estimates for representation numbers of quadratic forms*, *Duke Mathematical Journal* (2006), 261–302. The #1081 page records the quoted bound.
7. T. F. Bloom, [Erdős Problem #940](https://www.erdosproblems.com/940), including editorial remarks, references, and the [October 2025 discussion](https://www.erdosproblems.com/forum/thread/940). Accessed 18 July 2026.

## 9. Scope note

The literature search used the current #940 and #1081 records, their bibliography and discussion, DOI/publisher records for the principal papers, and targeted searches for “\(r\)-/\(k\)-powerful (full) numbers” and additive representations. The closest recent papers found concern other questions about 3-powerful numbers (for example coprime solutions of \(x+y=z\)), not the density or omission questions of #940. No claim is made that every possible unpublished preprint or non-indexed source has been exhausted.
