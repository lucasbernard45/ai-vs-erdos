# A finite–infinite reduction for Erdős Problem 130

**Date:** 18 July 2026  
**Status:** proved below; apparent novelty only (not a certified priority claim)

## Executive summary

I found a clean reduction that appears not to be stated on the Erdős Problems page or in the directly relevant papers located in the literature search:

> **The infinite-chromatic part of Erdős Problem 130 is equivalent to a purely finite unboundedness problem.**
>
> There is an infinite strongly-general-position set whose integer-distance graph has chromatic number \(\aleph_0\) **if and only if** finite strongly-general-position integer-distance graphs have unbounded chromatic number.

The nontrivial direction is not merely abstract compactness: finite configurations with larger and larger chromatic number can be translated and assembled into one infinite set while preserving strong general position and creating **no integer-distance edges between different blocks**.

Consequently, if

\[
M:=\sup\{\chi(G(S)):S\subset\mathbb R^2\text{ finite, no 3 collinear, no 4 concyclic}\},
\]

then the supremum over infinite admissible sets is exactly the same \(M\), interpreted as \(\aleph_0\) when the finite values are unbounded.

This makes Problem 130 a finite representation problem: either prove one uniform finite colouring bound for all finite configurations, or construct finite admissible configurations of arbitrarily high chromatic number.

---

## 1. Definitions

Call a set \(S\subset\mathbb R^2\) **strongly general** if

1. no three points of \(S\) are collinear; and
2. no four points of \(S\) are concyclic.

Its integer-distance graph \(G(S)\) has vertex set \(S\), with

\[
xy\in E(G(S))\iff \|x-y\|\in\mathbb Z_{>0}.
\]

Let

\[
\mathcal X_{\mathrm{fin}}
 =\{G(S):S\subset\mathbb R^2\text{ finite and strongly general}\}.
\]

Notice that this definition imposes no requirement that all distances be integers: edges are exactly the pairs at positive integer distance.

---

## 2. The assembly lemma

### Lemma (generic translation with edge isolation)

Let \(B\subset\mathbb R^2\) be a finite strongly-general set, and let \(A\subset\mathbb R^2\) be a finite or countable strongly-general set. Then there is a translation vector \(t\in\mathbb R^2\) such that

1. \(A\cup(B+t)\) is strongly general; and
2. no point of \(A\) is at an integer distance from a point of \(B+t\).

In particular, the integer-distance graph induced by the union is the disjoint union

\[
G(A\cup(B+t))=G(A)\sqcup G(B).
\]

### Proof

We exclude the bad translation vectors.

#### Cross-block integer distances

For fixed \(a\in A\), \(b\in B\), and \(m\in\mathbb Z_{>0}\), the condition

\[
\|a-(b+t)\|=m
\]

says that \(t\) lies on a circle in the translation plane. There are only countably many triples \((a,b,m)\), so all unwanted cross-block integer distances are excluded by a countable union of circles. Each circle is closed and nowhere dense.

#### Collinear triples

Triples wholly inside \(A\) or wholly inside \(B+t\) are already noncollinear.

For every mixed triple, collinearity is a nonzero polynomial condition on \(t\):

- for two old points and one translated point, the forbidden translations form a line;
- for one old point and two translated points, the forbidden translations also form a line (the translate of the line through the two points of \(B\)).

Thus mixed collinearity excludes a countable union of closed nowhere-dense lines.

#### Concyclic quadruples

Quadruples wholly inside either block are already nonconcyclic. For a mixed quadruple, concyclicity is the vanishing of the usual determinant

\[
\det
\begin{pmatrix}
 x_1&y_1&x_1^2+y_1^2&1\\
 x_2&y_2&x_2^2+y_2^2&1\\
 x_3&y_3&x_3^2+y_3^2&1\\
 x_4&y_4&x_4^2+y_4^2&1
\end{pmatrix}.
\]

After replacing the coordinates of the points from \(B\) by \((x+t_1,y+t_2)\), this is a polynomial in \((t_1,t_2)\). It is not the zero polynomial:

- with three points in one block and one in the other, the moving point can plainly be translated off the unique circle through the fixed noncollinear triple;
- with two points in each block, take a translation far in a direction not parallel to either of the two determined lines. The circle through one pair and one translated point does not identically contain the second translated point; equivalently, direct expansion leaves a nonzero polynomial unless one of the within-block pairs collapses, which it does not.

Hence each mixed quadruple excludes a proper real algebraic set, which is closed and nowhere dense. There are countably many mixed quadruples.

The complete bad set is therefore a countable union of closed nowhere-dense subsets of \(\mathbb R^2\). By the Baire category theorem it cannot cover \(\mathbb R^2\). Any translation outside it has the two required properties. ∎

### Strengthened form

The same proof permits simultaneously avoiding any prescribed countable set \(D\subset(0,\infty)\) of cross-block distances, not just \(D=\mathbb Z_{>0}\). One can also require \(t\) to lie outside any prescribed countable family of proper algebraic curves, or inside any chosen nonempty open region after checking that the bad sets remain nowhere dense there.

---

## 3. Countable disjoint-union closure

### Corollary

For every sequence \((S_n)_{n\ge1}\) of finite strongly-general point sets, there are translations \(t_n\) such that

\[
A=\bigcup_{n\ge1}(S_n+t_n)
\]

is strongly general and

\[
G(A)\cong\bigsqcup_{n\ge1}G(S_n).
\]

### Proof

Place the blocks inductively. At stage \(n\), the previously placed union is finite, so apply the lemma. (The lemma’s countable version also shows directly that later constraints pose no conceptual problem.) Each forbidden triple, quadruple, or cross-block integer-distance pair appears at a finite stage and is avoided then. ∎

An optional refinement is to place the \(n\)-th block in a ball centred beyond radius \(n\), making the union discrete and unbounded, while retaining all conclusions.

---

## 4. Main finite–infinite equivalence

### Theorem

The following are equivalent:

1. There exists an infinite strongly-general \(A\subset\mathbb R^2\) such that \(\chi(G(A))=\aleph_0\).
2. For every \(k\in\mathbb N\), there exists a finite strongly-general \(S_k\subset\mathbb R^2\) such that \(\chi(G(S_k))\ge k\).

Moreover, if the finite chromatic numbers are bounded, then their maximum equals the largest chromatic number possible for an infinite admissible set.

### Proof

#### \((1)\Rightarrow(2)\)

If every finite subgraph of \(G(A)\) were \((k-1)\)-colourable, the de Bruijn–Erdős compactness theorem would make all of \(G(A)\) \((k-1)\)-colourable. Since \(G(A)\) has infinite chromatic number, for every \(k\) it contains a finite subgraph of chromatic number at least \(k\). Its vertex set is a finite subset \(S_k\subset A\), and therefore is strongly general.

#### \((2)\Rightarrow(1)\)

Choose one such \(S_k\) for every \(k\). By countable disjoint-union closure, translated copies can be assembled into a strongly-general countable set \(A\) with

\[
G(A)\cong\bigsqcup_{k\ge1}G(S_k).
\]

Therefore

\[
\chi(G(A))=\sup_k\chi(G(S_k))=\aleph_0.
\]

The final assertion follows similarly. If every finite admissible graph is \(M\)-colourable, then every finite subgraph of every infinite admissible graph is \(M\)-colourable, so de Bruijn–Erdős gives a global \(M\)-colouring. Conversely, a finite configuration attaining \(M\) can be included as one block of an infinite strongly-general set, so the bound is attained in the infinite class as well. ∎

---

## 5. Exact equality of the finite and infinite extremal parameters

Define

\[
\chi_{\mathrm{fin}}^*:=\sup\{\chi(G(S)):S\text{ finite and strongly general}\}
\]

and

\[
\chi_{\mathrm{inf}}^*:=\sup\{\chi(G(A)):A\text{ infinite and strongly general}\}.
\]

Since all relevant graphs are countably colourable, use the ordered set
\(\mathbb N\cup\{\aleph_0\}\). The theorem gives the exact identity

\[
\boxed{\chi_{\mathrm{fin}}^*=\chi_{\mathrm{inf}}^*.}
\]

There is an analogous clique identity:

\[
\boxed{\omega_{\mathrm{fin}}^*=\omega_{\mathrm{inf}}^*,}
\]

again allowing the value \(\aleph_0\) to mean “finite clique sizes are unbounded.” The assembly lemma proves the nontrivial direction. Note carefully that if the clique supremum is \(\aleph_0\), the assembled graph has cliques of every finite size but no infinite clique, consistently with Anning–Erdős.

---

## 6. Why this advances the problem

The original formulation looks intrinsically infinitary. The theorem removes that aspect completely:

- A **positive** answer needs only a sequence of finite configurations with unbounded chromatic number. They need not be mutually compatible; generic translations make them compatible automatically.
- A **negative** answer is equivalent to a uniform finite chromatic bound over all finite strongly-general configurations.
- Computer-assisted searches are therefore logically relevant to the infinite question, not merely to finite variants.
- Cross-block arithmetic interference is not an obstacle: it can be eliminated exactly, rather than tolerated.

It also separates the clique and chromatic routes. Unbounded clique size would immediately solve the chromatic problem positively, but one can instead search for high-chromatic graphs with small cliques. Since even \(K_8\) is unknown, the second route may be more realistic.

---

## 7. Novelty assessment

I searched specifically for:

- reductions of Erdős Problem 130 to finite high-chromatic configurations;
- closure under generic translated disjoint unions;
- strong-general-position integer-distance graphs with no cross-block integer distances;
- discussions around the 2024 papers of Solymosi and of Greenfeld–Iliopoulou–Peluse.

I found the standard de Bruijn–Erdős compactness implication and the known integral-distance representation literature, but not this two-way geometric assembly statement. The directly relevant sources continue to formulate Problem 130 for an infinite set and do not state the exact equality of finite and infinite extremal chromatic parameters.

That is evidence of novelty, not proof of priority. A claim of publishable novelty would require expert review and a broader bibliographic search (including non-digitised literature). The mathematics of the reduction itself is independent of that priority question.

---

## 8. References consulted

1. T. F. Bloom, [Erdős Problem #130](https://www.erdosproblems.com/130), accessed 18 July 2026.
2. N. G. de Bruijn and P. Erdős, “A colour problem for infinite graphs and a problem in the theory of relations,” *Indagationes Mathematicae* **54** (1951), 371–373.
3. J. Solymosi, “Integral and rational graphs in the plane,” *Graphs and Combinatorics* **40** (2024), article 107. [arXiv:2402.08215](https://arxiv.org/abs/2402.08215)
4. R. Greenfeld, M. Iliopoulou and S. Peluse, “On integer distance sets” (2024). [arXiv:2401.10821](https://arxiv.org/abs/2401.10821)
5. T. Kreisel and S. Kurz, “There are integral heptagons, no three points on a line, no four on a circle,” *Discrete & Computational Geometry* **39** (2008), 786–790. [arXiv:0804.1303](https://arxiv.org/abs/0804.1303)

---

## 9. Suggested next theorem to pursue

The reduction identifies the precise next target:

> Construct, for each \(k\), one finite strongly-general point set whose integer-distance graph is \(k\)-chromatic.

One need not preserve nonedges under assembly, coordinate different values of \(k\), or solve any infinite placement problem. Even producing a single example with chromatic number \(8\) and clique number at most \(7\) would improve the currently documented chromatic lower bound without resolving the integral \(K_8\) problem.
