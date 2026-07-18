# Erdős Problem 130: deeper audit and corrected distance-layer theory

**Date:** 18 July 2026

## Important correction

A deeper audit found an error in my preceding distance-layer note. I had claimed that a vertex and three neighbours at the same distance are four concyclic points. That is false: the vertex is the **centre** of the circle containing its neighbours, and is not on that circle.

The correct conclusion is

\[
\Delta(G_r)\le 3,
\]

not \(2\). Four same-distance neighbours of a vertex would be four concyclic points. This document replaces the erroneous layer bounds in the earlier note. The finite–infinite generic-translation reduction is unaffected.

Finding and repairing this issue is essential: mathematical soundness takes precedence over preserving a claimed result.

---

## 1. Correct fixed-distance structure

Let \(A\subset\mathbb R^2\) have no three collinear points and no four concyclic points. For \(r>0\), define

\[
G_r(A)=(A,\{xy:\|x-y\|=r\}).
\]

### Theorem 1 (subcubic layers)

For every \(r>0\),

\[
\boxed{\Delta(G_r(A))\le3.}
\]

### Proof

All \(r\)-neighbours of a fixed vertex \(v\) lie on the circle with centre \(v\) and radius \(r\). Four such neighbours would be four points of \(A\) on one circle, contrary to the hypothesis. Hence \(v\) has at most three \(r\)-neighbours. ∎

The bound three cannot be reduced merely from the two general-position axioms: three points may lie on a circle centred at \(v\), with no antipodal pair and hence no collinear triple involving \(v\).

---

## 2. A stronger fact: every fixed-distance layer is 3-colourable

The maximum-degree bound alone would give four colours, but the unique Brooks obstruction at degree three cannot occur geometrically.

### Theorem 2 (three-colourability of each layer)

For every \(r>0\),

\[
\boxed{\chi(G_r(A))\le3.}
\]

### Proof

Consider a connected component \(H\) of \(G_r(A)\).

- If \(\Delta(H)\le2\), then \(H\) is a path or cycle (with the usual infinite analogues) and is 3-colourable.
- If \(\Delta(H)=3\), Brooks’ theorem says that a finite connected component is 3-colourable unless it is \(K_4\). But a Euclidean plane cannot contain four pairwise equidistant points: the largest equilateral set in \(\mathbb R^2\) has size three. Thus \(K_4\) cannot occur.

Every finite subgraph is therefore 3-colourable. The de Bruijn–Erdős compactness theorem extends the colouring to an infinite component. Applying this to all components proves the result. ∎

This recovers, under the strong-general-position condition, a sharp universal bound for every individual distance layer. An equilateral triangle shows that three colours can be necessary.

---

## 3. Correct bounds for a finite distance alphabet

Let

\[
R(A)=\{r\in\mathbb Z_{>0}: \text{some pair in }A\text{ is at distance }r\}.
\]

Suppose \(|R(A)|=q<\infty\).

### Theorem 3 (degree and chromatic bounds)

\[
\boxed{\Delta(G(A))\le3q}
\]

and

\[
\boxed{\chi(G(A))\le3q+1.}
\]

For every finite connected component that is neither a complete graph nor an odd cycle, Brooks’ theorem gives

\[
\boxed{\chi(G(A))\le3q.}
\]

For infinite graphs the \(3q+1\) bound follows from de Bruijn–Erdős compactness.

There is also a different, generally weaker but structurally useful product colouring: colour each of the \(q\) layers with three colours and assign each vertex its vector of layer colours. This gives

\[
\chi(G(A))\le3^q.
\]

The linear degree bound is better for \(q\ge2\).

---

## 4. A corrected local arithmetic obstruction

For a vertex \(v\), define its local integer-length spectrum

\[
R(v)=\{r\in\mathbb Z_{>0}:\exists w\in A,\ \|v-w\|=r\}.
\]

Since at most three neighbours of \(v\) can occur at any one length,

\[
\boxed{\deg(v)\le3|R(v)|.}
\]

If \(H\) is a finite \(k\)-critical subgraph, every vertex of \(H\) has degree at least \(k-1\). Therefore

\[
\boxed{|R_H(v)|\ge\left\lceil\frac{k-1}{3}\right\rceil
\quad\text{for every }v\in V(H).}
\]

Thus a positive solution of Problem 130 would force finite critical witnesses in which the number of distinct integer lengths incident with **every** vertex tends to infinity.

The factor is \(1/3\), not the erroneous \(1/2\) from the previous note.

---

## 5. A new equality-case analysis

The corrected degree estimate has a useful rigid equality case.

Let a finite graph use exactly \(q\) integer lengths and have chromatic number \(3q+1\). A \((3q+1)\)-critical subgraph \(H\) then has minimum degree at least \(3q\), while the layer bound gives maximum degree at most \(3q\). Hence:

### Proposition 4 (saturation forced at the linear bound)

If \(\chi(G(A))=3q+1\) and only \(q\) integer lengths occur, then a \((3q+1)\)-critical subgraph \(H\) exists with all of the following properties:

1. \(H\) is \(3q\)-regular;
2. every vertex has exactly three neighbours at each of the \(q\) integer lengths;
3. every distance layer induced on \(H\) is 3-regular;
4. by Brooks’ theorem, \(H\cong K_{3q+1}\).

### Proof

Criticality gives \(\deg_H(v)\ge3q\). There are only \(q\) lengths, each contributing at most three neighbours, so \(\deg_H(v)\le3q\). Equality holds throughout at every vertex, proving (1)–(3). A connected \((3q+1)\)-critical graph of maximum degree \(3q\) must be the Brooks complete-graph exception, proving (4). ∎

Consequently,

\[
\boxed{\chi(G(A))=3q+1\ \Longrightarrow\
A\text{ contains a }(3q+1)\text{-point }q\text{-distance set}.}
\]

Here “\(q\)-distance set” means that all pairwise distances among those \(3q+1\) points belong to the same set of \(q\) positive integers.

This converts equality in the chromatic estimate into a highly constrained finite-distance-set problem.

---

## 6. Parity improves half of the cases

Every distance layer in the equality case would be a 3-regular graph on \(3q+1\) vertices. A 3-regular finite graph has an even number of vertices, by the handshake lemma. Therefore \(3q+1\) must be even, which occurs only when \(q\) is odd.

### Corollary 5 (even-alphabet improvement)

If \(q\) is even, then

\[
\boxed{\chi(G(A))\le3q.}
\]

### Proof

The general bound is \(3q+1\). If equality held, Proposition 4 would make every one of the \(q\) layers 3-regular on \(3q+1\) vertices. For even \(q\), \(3q+1\) is odd, impossible for a 3-regular graph. ∎

This is a genuine sharpening of the naive maximum-degree bound for every even number of occupied integer lengths.

For odd \(q\), equality would still require an exceptionally rigid \((3q+1)\)-point, \(q\)-distance configuration in strong general position.

---

## 7. The one-distance case is exact

When \(q=1\), Theorem 2 gives

\[
\chi(G(A))\le3,
\]

and an equilateral triangle with integral side length attains three. Thus

\[
\boxed{F(1)=3,}
\]

where

\[
F(q)=\sup\{\chi(G(S)):S\text{ finite strongly general and using at most }q
\text{ integer edge lengths}\}.
\]

The general results now read

\[
F(q)\le
\begin{cases}
3q,&q\text{ even},\\
3q+1,&q\text{ odd},
\end{cases}
\qquad F(1)=3.
\]

The unresolved equality case for odd \(q\ge3\) is reduced to the existence of a strongly-general \((3q+1)\)-point \(q\)-distance set whose \(q\) distance graphs are all cubic.

---

## 8. Consequences for Problem 130

Combining the corrected theory with the finite–infinite assembly theorem gives:

### Necessary conditions for a positive solution

If Problem 130 has a positive answer, then for every \(k\) there is a finite strongly-general \(k\)-critical integer-distance graph \(H_k\) such that

1. every vertex is incident with at least \(\lceil(k-1)/3\rceil\) distinct integer lengths;
2. globally, at least \(\lceil(k-1)/3\rceil\) integer lengths occur;
3. the diameter is at least \(\lceil(k-1)/3\rceil\);
4. no construction using a fixed finite distance alphabet can work;
5. if a witness comes close to the extremal ratio \(\chi\approx3q\), almost every vertex–length incidence must be saturated.

The fifth point is the most useful new direction. High chromatic efficiency forces the geometry toward many triples of points on circles centred at other points. Those triples are individually allowed, but any fourth point on one of those circles is forbidden. A possible negative approach is to prove that simultaneous near-saturation across many integer radii is geometrically impossible.

---

## 9. A concrete next target

The refined problem is no longer merely “find high chromatic examples.” It is:

> How large can the chromatic number of a strongly-general integer-distance graph be relative to the number \(q\) of occupied integer lengths?

The corrected universal slope is at most three. To move materially closer to a negative solution of #130, one should seek a **sublinear-in-\(q\)** or uniform bound using compatibility between the cubic layers. To move toward a positive solution, one should try to build configurations whose chromatic number grows with \(q\).

A particularly concrete first case is \(q=2\). Corollary 5 gives

\[
\chi(G(A))\le6.
\]

Determining whether 5 or 6 is attainable under the full general-position constraints is a finite, sharply posed problem. Resolving it would test whether different integer-distance layers can interact anywhere near the maximum-degree limit.

---

## 10. Novelty and reliability statement

The subcubic observation itself is elementary. The following package was not found in the directly relevant sources searched:

- three-colourability of each fixed-distance layer under the no-four-concyclic condition;
- the \(3q+1\) finite-alphabet bound;
- the vertexwise critical-spectrum bound;
- the complete saturation description at equality;
- the parity improvement \(\chi\le3q\) for even \(q\);
- integration of these statements with the finite–infinite assembly reduction for Problem 130.

These deductions are mathematically proved above. “Novel” here means not located in the searched literature and apparently new in this formulation; absolute priority still requires specialist review.

Most importantly, this audit openly corrects the prior false \(\Delta\le2\) claim. Any future work should cite this corrected document, not the earlier distance-layer note.
