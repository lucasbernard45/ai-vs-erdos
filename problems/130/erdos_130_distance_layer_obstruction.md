# Distance-layer obstructions for Erdős Problem 130

**Date:** 18 July 2026  
**Status:** rigorous new deduction; novelty checked against the directly relevant literature, but—as always—historical priority requires expert verification

## 1. Result obtained

Let \(A\subset\mathbb R^2\) contain no four concyclic points, and let \(G(A)\) join pairs at positive integer distance. For each positive integer \(r\), write

\[
G_r(A):=(A,\{xy:\|x-y\|=r\}).
\]

The key observation is that the strong general-position hypothesis turns every individual distance layer into an extremely simple graph.

### Distance-layer theorem

For every \(r>0\),

\[
\boxed{\Delta(G_r(A))\le 2.}
\]

Consequently every connected component of \(G_r(A)\) is a finite path, a ray, a double ray, or a cycle. In particular,

\[
\chi(G_r(A))\le 3.
\]

More substantially, if only \(q\) different positive integer lengths occur as edges of \(G(A)\), then

\[
\boxed{\chi(G(A))\le 2q+1.}
\]

If \(G(A)\) is finite and connected, then Brooks’ theorem sharpens this to

\[
\boxed{\chi(G(A))\le 2q}
\]

unless \(G(A)\) is a complete graph or an odd cycle.

This gives a quantitative obstruction to every proposed positive solution of Problem 130:

> A countably infinite chromatic example must use infinitely many distinct integer edge lengths. More precisely, finite subgraphs of chromatic number \(k\) must use at least \((k-1)/2\) distinct integer lengths; apart from the complete-graph and odd-cycle exceptions, they must use at least \(k/2\).

The conclusion is stronger than merely saying that the configuration must have unbounded diameter: it forces **arithmetically many occupied integer distance layers** inside every high-chromatic witness.

---

## 2. Proof of the distance-layer theorem

Fix \(v\in A\) and a positive integer \(r\). Every neighbour of \(v\) in \(G_r(A)\) lies on the circle

\[
C(v,r)=\{x\in\mathbb R^2:\|x-v\|=r\}.
\]

If \(v\) had three distinct \(r\)-neighbours \(x,y,z\), then \(x,y,z\), together with \(v\), would be four points on the same circle \(C(v,r)\). This is forbidden. Hence

\[
\deg_{G_r(A)}(v)\le2.
\]

Since \(v\) was arbitrary, \(\Delta(G_r(A))\le2\). The component classification and 3-colourability are the standard classification of graphs of maximum degree at most two. ∎

---

## 3. Combining the layers

Suppose the integer edge lengths occurring in \(G(A)\) form a finite set

\[
R=\{r_1,\ldots,r_q\}.
\]

Since each vertex has degree at most two in each layer,

\[
\deg_{G(A)}(v)
 =\sum_{i=1}^q\deg_{G_{r_i}(A)}(v)
 \le 2q.
\]

Thus \(\Delta(G(A))\le2q\).

For a finite graph, greedy colouring gives \(\chi(G(A))\le2q+1\). For an infinite graph the same conclusion follows either by applying the de Bruijn–Erdős compactness theorem to all finite subgraphs or by orienting each path/cycle layer with outdegree at most one and applying the standard finite-outdegree colouring argument.

If a finite connected component is neither a complete graph nor an odd cycle, Brooks’ theorem gives

\[
\chi(G(A))\le\Delta(G(A))\le2q.
\]

For a disconnected graph, apply this componentwise. ∎

---

## 4. Quantitative corollaries

### Corollary 4.1 — length complexity of a chromatic witness

Let \(S\) be a finite strongly-general configuration and let

\[
q(S)=\big|\{\|x-y\|\in\mathbb Z_{>0}:x,y\in S\}\big|.
\]

Then

\[
q(S)\ge \frac{\chi(G(S))-1}{2}.
\]

If a \(k\)-critical component of \(G(S)\) is neither \(K_k\) nor an odd cycle, then

\[
q(S)\ge \left\lceil\frac{k}{2}\right\rceil.
\]

### Corollary 4.2 — diameter obstruction

All occupied integer lengths are distinct positive integers not exceeding \(\operatorname{diam}(S)\), so

\[
q(S)\le\lfloor\operatorname{diam}(S)\rfloor.
\]

Therefore

\[
\chi(G(S))\le2\lfloor\operatorname{diam}(S)\rfloor+1,
\]

and any \(k\)-chromatic witness has

\[
\operatorname{diam}(S)\ge\frac{k-1}{2}.
\]

The importance is not the linear constant by itself, but the mechanism: every new pair of possible colours requires another occupied arithmetic distance layer.

### Corollary 4.3 — bounded sets are finitely colourable

If an infinite admissible set \(A\) has finite diameter \(D\), then only the integer lengths

\[
1,2,\ldots,\lfloor D\rfloor
\]

can occur, and hence

\[
\chi(G(A))\le2\lfloor D\rfloor+1.
\]

Thus every positive solution of Problem 130 must be unbounded.

### Corollary 4.4 — no finite distance alphabet can solve #130

More generally, if the set of integer distances actually realised by \(A\) is finite—even when \(A\) itself is unbounded—then \(G(A)\) has finite chromatic number.

This rules out constructions built by repeating a fixed finite collection of integer-distance motifs at arbitrarily remote locations.

---

## 5. Interaction with the finite–infinite reduction

The preceding note proved that Problem 130 has a positive answer exactly when finite strongly-general integer-distance graphs have unbounded chromatic number. Combining that result with the present theorem gives a sharper equivalence.

### Refined finite formulation

Problem 130 has a positive answer if and only if there exists a sequence of finite strongly-general configurations \(S_k\) such that

\[
\chi(G(S_k))\longrightarrow\infty.
\]

Necessarily, along every such sequence,

\[
q(S_k)\longrightarrow\infty,
\qquad
q(S_k)\ge\frac{\chi(G(S_k))-1}{2},
\]

and

\[
\operatorname{diam}(S_k)\longrightarrow\infty.
\]

Conversely, the generic-translation assembly lemma can place these witnesses in one infinite set without adding cross-block integer edges. The resulting infinite graph has chromatic number \(\aleph_0\) and uses infinitely many integer lengths.

This identifies a concrete two-parameter finite search problem:

\[
F(q):=\max\{\chi(G(S)):S\text{ finite, strongly general, }q(S)\le q\}.
\]

The theorem proves

\[
F(q)\le2q+1,
\]

or \(F(q)\le2q\) away from complete and odd-cycle components. Problem 130 asks whether \(F(q)\) is unbounded as \(q\to\infty\).

That formulation is closer to the actual obstruction than the original infinitary statement: it asks whether unions of degree-two Euclidean distance layers can realise unbounded chromatic number while satisfying all cross-layer metric compatibility constraints.

---

## 6. A structural reformulation

Every admissible integer-distance graph admits an edge partition

\[
E(G)=E_1\sqcup E_2\sqcup\cdots,
\]

indexed by positive integer lengths, in which every \((V,E_i)\) has maximum degree two.

Abstractly, a union of \(q\) maximum-degree-two graphs can have chromatic number on the order of \(q\), so this fact alone cannot settle Problem 130. What makes the geometric problem difficult is that the layers are not arbitrary: all of them must arise from one Euclidean embedding, with the additional prohibition on collinear triples and concyclic quadruples.

A route to a negative solution would therefore be a genuinely geometric improvement of

\[
\chi(G)\le2q+1
\]

that is uniform in \(q\), or an argument showing that sufficiently many layers cannot interact chromatically efficiently. A route to a positive solution must construct Euclidean-compatible degree-two layers whose union has unbounded chromatic number.

This is a substantially narrower target than “construct an infinite chromatic integer-distance graph.”

---

## 7. A further exact parameter: local length diversity

Define the local integer-length spectrum at \(v\) by

\[
R(v)=\{r\in\mathbb Z_{>0}:\exists w\in A,\ \|v-w\|=r\}.
\]

The same circle argument gives

\[
\deg(v)\le2|R(v)|.
\]

Hence every finite \(k\)-critical subgraph satisfies minimum degree at least \(k-1\), and therefore every one of its vertices obeys

\[
\boxed{|R(v)|\ge\left\lceil\frac{k-1}{2}\right\rceil.}
\]

This is stronger than the global statement \(q(S)\ge(k-1)/2\): high chromatic number cannot be generated by distributing many lengths sparsely across different portions of the configuration. **Every vertex of a critical witness must participate in linearly many distinct integer lengths.**

Combining with the finite–infinite reduction:

> A positive solution of Problem 130 forces, for every \(k\), a finite strongly-general configuration containing a \(k\)-critical integer-distance graph in which every vertex is incident with at least \(\lceil(k-1)/2\rceil\) different integer lengths.

This local arithmetic-density requirement is a useful obstruction for both constructions and computer searches.

---

## 8. Why this is closer to a solution

The earlier reduction said *what kind of finite objects suffice*. The present result says *what every such object must look like*:

1. It must use linearly many distinct integer lengths.
2. Every vertex of a critical witness must itself see linearly many distinct lengths.
3. Its diameter must grow at least linearly with chromatic number.
4. Fixed-distance and fixed-alphabet constructions are impossible.
5. The problem becomes the study of Euclidean-compatible unions of degree-two layers.

These are testable, quantitative necessary conditions. In particular, a search for an 8-chromatic witness may discard immediately any configuration in which a vertex of an 8-critical core sees fewer than four distinct integer lengths.

---

## 9. Novelty assessment

The elementary circle observation is unlikely, by itself, to be historically new. The contribution claimed here is the **assembled quantitative framework**:

- the distance-layer decomposition for this exact strong-general-position problem;
- the \(2q+1\) and Brooks-type \(2q\) chromatic bounds in terms of occupied integer lengths;
- the vertexwise length-diversity obstruction for critical witnesses;
- its combination with the finite–infinite assembly theorem to obtain an exact finite search target for Problem 130.

I searched the Erdős #130/#213 pages, Solymosi’s 2024 paper, Greenfeld–Iliopoulou–Peluse, Kreisel–Kurz, and web-indexed discussions using combinations of “integer distance graph,” “no four concyclic,” “chromatic number,” “distance layers,” and “maximum degree two.” I did not find this formulation or these quantitative consequences stated for Problem 130.

This supports genuine novelty relative to the located literature, but no document can certify absolute historical priority without specialist peer review.

---

## 10. Bottom line

The new obstruction can be summarised in one sentence:

> **Under the no-four-concyclic hypothesis, each integer distance contributes at most two edges at any vertex; therefore unbounded chromatic number requires linearly growing, vertexwise arithmetic diversity of integer distances.**

This does not solve Problem 130, but it moves beyond the finite–infinite reduction by imposing a rigid and quantitative shape on every possible positive solution.
