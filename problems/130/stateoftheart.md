# Erdős Problem 130: state of the art

**Research cutoff:** 18 July 2026  
**Problem page:** [Erdős Problems #130](https://www.erdosproblems.com/130)

## 1. The problem

Let \(A\subset \mathbb R^2\) be infinite and in **general position** in the following strong sense:

- no three points of \(A\) are collinear;
- no four points of \(A\) are concyclic.

Define the integer-distance graph \(G(A)\) on vertex set \(A\) by

\[
xy\in E(G(A)) \quad\Longleftrightarrow\quad \|x-y\|\in\mathbb Z_{>0}.
\]

Andrásfai and Erdős asked how large \(\chi(G(A))\) and \(\omega(G(A))\) can be, and especially whether \(\chi(G(A))\) can be infinite.

The problem is still listed as **open**. The cleanest present formulation of the main chromatic question is:

> Is there such an \(A\) for which \(\chi(G(A))=\aleph_0\), or must every such graph have finite chromatic number?

Here “infinite chromatic number” can only mean countably infinite; see §2.1.

---

## 2. Immediate bounds and structural facts

### 2.1 The chromatic number is always at most countable

Partition the plane into half-open squares of side length less than \(1/\sqrt2\), and give every square its own colour. Two points in one square are at distance strictly less than 1, hence cannot be at a positive integer distance. This gives a proper colouring with countably many colours:

\[
\chi(G(A))\leq \aleph_0.
\]

Thus the unresolved dichotomy is **finite versus countably infinite**, not countable versus uncountable.

### 2.2 Every clique is finite

A clique is a set of points all of whose pairwise distances are integers—an *integer distance set*. The Anning–Erdős theorem says that every infinite integer distance set in the plane is collinear. Since \(A\) contains no three collinear points, \(G(A)\) has no infinite clique.

Consequently,

\[
\omega(G(A))<\infty
\]

for each individual admissible set \(A\). This does **not** provide a uniform numerical upper bound valid for every \(A\).

A useful stronger local obstruction, already implicit in Erdős’s hyperbola proof, is that an integral distance graph contains no \(K_{3,\aleph_0}\): three noncollinear points cannot have infinitely many common integer-distance neighbours. Solymosi’s 2024 paper develops stronger restrictions of this type; for example, the graph induced by the common neighbours of any two vertices has finite chromatic number.

---

## 3. Best known clique information

### Lower bound: \(\omega\geq 7\)

Kreisel and Kurz constructed two seven-point configurations with all pairwise distances integral, no three points collinear, and no four concyclic. Therefore an admissible infinite set can contain a \(K_7\): after taking one such configuration, one may add countably many generic points while avoiding the finitely or countably many forbidden lines, circles, and integer-distance circles created at each stage. Hence

\[
\sup_A \omega(G(A))\geq 7,
\qquad
\sup_A \chi(G(A))\geq 7.
\]

### Upper bound: unknown; even \(K_8\) is open

No eight-point configuration satisfying all the requirements is known. Solymosi explicitly records in 2024 that it remains open whether \(K_8\) has an integral-distance realization with no three collinear and no four concyclic.

Thus the present unconditional clique picture is strikingly narrow but unresolved:

\[
7\leq \sup_A\omega(G(A)),
\]

with no known finite uniform upper bound, and with the very next case \(8\) open.

This is essentially Erdős Problem #213, the finite complete-graph version of #130.

---

## 4. Best known chromatic information

The unconditional bounds currently visible from the literature are

\[
7\leq \sup_A\chi(G(A))\leq\aleph_0.
\]

The upper bound here is merely the elementary countable colouring. The central question—whether the upper endpoint can occur—remains open.

It is important not to confuse Problem #130 with less restricted integral-distance representation results. Maehara, Ota and Tokushige proved that every **finite graph** is representable as an integral distance graph in the plane when only collinear triples are forbidden. Their construction does not settle #130 because forbidding four concyclic points makes the representation problem much harder; indeed, even \(K_8\) is unknown under the extra condition.

Likewise, Solymosi constructed several infinite graphs that cannot be integral-distance graphs, including locally finite examples and examples with unbounded chromatic number. These are obstructions to representation, not constructions answering #130. His results do, however, show that integral-distance graphs satisfy considerably subtler restrictions than merely excluding \(K_{3,\aleph_0}\).

No source found in this review gives either:

1. an admissible integer-distance graph of chromatic number greater than 7; or
2. a universal finite chromatic bound for all admissible \(A\).

Accordingly, the exact best finite lower bound for the chromatic question appears still to come from the known \(K_7\).

---

## 5. Quantitative progress on complete subgraphs

Recent progress concerns finite integer distance sets inside a bounded box. Greenfeld, Iliopoulou and Peluse proved a strong structure theorem: if an integer distance set \(S\subset[-N,N]^2\), then all but \((\log N)^{O(1)}\) points lie on one line or circle. In particular, if no three points are collinear and no four are concyclic, then

\[
|S|=(\log N)^{O(1)}.
\]

This improved the previous \(O(N)\) bound. It says that a large general-position clique, if one exists, must have enormous diameter. It does **not** give an absolute bound independent of \(N\), so it does not decide whether clique sizes are uniformly bounded.

Ascher, Braune and Turchet proved, conditional on the Bombieri–Lang/Lang conjectural framework, a uniform bound for general-position rational-distance sets. Since integer distances are rational, this conditionally gives a uniform bound on clique size in Problem #130. The bound is conditional and does not determine the largest clique; in particular, it does not settle the \(K_8\) case unconditionally.

---

## 6. What is known versus what remains open

| Question | Current state |
|---|---|
| Can an admissible graph contain an infinite clique? | **No**, by Anning–Erdős. |
| Largest known clique | **7**, from Kreisel–Kurz integral heptagons. |
| Does an admissible \(K_8\) exist? | **Open**. |
| Is there an unconditional uniform finite bound on clique size? | **Open**. |
| Conditional uniform clique bound | **Yes**, assuming Bombieri–Lang/Lang-type conjectures. |
| Largest established chromatic lower bound found in this review | **At least 7**, via \(K_7\). |
| General upper bound for chromatic number | **\(\aleph_0\)**. |
| Can the chromatic number be infinite? | **Open**. |
| Must every admissible graph have finite chromatic number? | **Open**. |

---

## 7. Promising fault lines for further work

1. **The \(K_8\) bottleneck.** Even a single integral octagon in the required general position would improve both clique and chromatic lower bounds and resolve the next case of Problem #213.
2. **High chromatic number without large cliques.** The chromatic question may be more approachable through sparse finite subgraphs of high chromatic number rather than complete configurations. By the de Bruijn–Erdős compactness theorem, an infinite graph has finite chromatic number at most \(k\) exactly when all its finite subgraphs are \(k\)-colourable. Thus \(\chi(G(A))=\aleph_0\) would require finite integer-distance subgraphs of arbitrarily large chromatic number inside one admissible realization.
3. **Exploit common-neighbour restrictions.** Solymosi’s finite-colourability theorem for common-neighbour graphs is a genuine structural constraint. A route to a finite global colouring would need to amplify such local restrictions.
4. **Quantitative geometry versus colouring.** The Greenfeld–Iliopoulou–Peluse theorem controls complete subgraphs, not arbitrary high-chromatic subgraphs. Extending its line/circle concentration methods to dense or critical subgraphs could connect the strongest recent number-theoretic progress to #130’s chromatic side.
5. **Arithmetic geometry.** Conditional uniformity results suggest that rational/integer distance constraints in general position are governed by high-genus curves and uniformity conjectures. Whether those tools can say anything about noncomplete high-chromatic graphs is largely unexplored.

---

## 8. References and links

1. N. H. Anning and P. Erdős, “Integral distances,” *Bulletin of the American Mathematical Society* **51** (1945), 598–600. [AMS link](https://www.ams.org/journals/bull/1945-51-08/S0002-9904-1945-08407-9/)
2. P. Erdős, “Integral distances,” *Bulletin of the American Mathematical Society* **51** (1945), 996. (Simplified hyperbola proof.)
3. T. Kreisel and S. Kurz, “There are integral heptagons, no three points on a line, no four on a circle,” *Discrete & Computational Geometry* **39** (2008), 786–790. [DOI](https://doi.org/10.1007/s00454-007-9038-6)
4. K. Ascher, L. Braune and A. Turchet, “The Erdős–Ulam problem, Lang’s conjecture and uniformity,” *Bulletin of the London Mathematical Society* **52** (2020), 1053–1063. [DOI](https://doi.org/10.1112/blms.12393)
5. R. Greenfeld, M. Iliopoulou and S. Peluse, “On integer distance sets” (2024). [arXiv:2401.10821](https://arxiv.org/abs/2401.10821)
6. J. Solymosi, “Integral and rational graphs in the plane,” *Graphs and Combinatorics* **40** (2024), article 107. [DOI](https://doi.org/10.1007/s00373-024-02841-1), [arXiv:2402.08215](https://arxiv.org/abs/2402.08215)
7. H. Maehara, K. Ota and N. Tokushige, “Every graph is an integral distance graph in the plane,” *Journal of Combinatorial Theory, Series A* **80** (1997), 290–294.
8. T. F. Bloom, [Erdős Problem #130](https://www.erdosproblems.com/130), accessed 18 July 2026.
9. T. F. Bloom, [Erdős Problem #213](https://www.erdosproblems.com/213), accessed 18 July 2026.

---

## Bottom line

As of 18 July 2026, Problem #130 remains wide open on its chromatic side. Every admissible graph is countably colourable and has only finite cliques, but the best known clique has size 7, \(K_8\) is still unknown, and no universal finite chromatic bound is known. The strongest recent advances sharply constrain complete integer-distance configurations, while the possibility of a countably infinite chromatic number remains essentially untouched.
