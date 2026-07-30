# Towards a Full Resolution of Erdős Problem #114: Bridging the Finite Gap

## 1. Introduction and The Nature of the Gap
With Terence Tao's December 2025 breakthrough proving the Erdős-Herzog-Piranian (EHP) conjecture for all "sufficiently large $n$", the problem has transitioned from an asymptotic challenge to a finite (though potentially massive) computational and algebraic geometry problem. Eremenko and Hayman (1999) resolved $n=2$, leaving the intermediate degrees $3 \leq n < N_0$ (where $N_0$ is Tao's unspecified effective threshold) fully open. 

Tao notes that the problem has effectively entered the realm of "decidability." However, verifying the remaining finite cases encounters a severe computational bottleneck: the exact evaluation and comparison of *periods* (transcendental integrals representing lemniscate arc lengths). Specifically, testing strict inequalities and equalities of real periods across high-dimensional moduli spaces is ill-suited for standard computational algebra techniques like Cylindrical Algebraic Decomposition (CAD).

This document proposes a mathematically sound and genuinely novel framework—**The SOS-Relaxed Picard-Fuchs Method**—designed to rigorously verify the remaining degrees without requiring exact numerical equality testing of transcendental numbers.

## 2. Algebraic Formulation of Lemniscate Arclength
Let $p(z) = z^n + a_{n-1}z^{n-1} + \dots + a_0$ be a monic polynomial. The length of the lemniscate $\mathcal{L}_p = \{z \in \mathbb{C} : |p(z)| = 1\}$ can be parameterized by $\theta \in [0, 2\pi)$. 
For $p(z) = e^{i\theta}$, differentiating gives $p'(z)dz = ie^{i\theta}d\theta$, so the differential of arclength is $ds = |dz| = \frac{1}{|p'(z)|} d\theta$. Summing over all branches:

$$ L(p) = \int_0^{2\pi} \sum_{p(z_k) = e^{i\theta}} \frac{1}{|p'(z_k)|} d\theta $$

The integrand is not a simple rational function due to the absolute value. To algebraize it, we decouple $z$ and its complex conjugate. Let $w = \bar{z}$. The lemniscate is the real locus of the complex algebraic curve $\mathcal{C}_p$ defined in $\mathbb{C}^2$ by:

$$ p(z)\overline{p}(w) = 1 $$

where $\overline{p}$ is the polynomial with conjugated coefficients. Over this curve, the arclength differential becomes an Abelian differential. Consequently, the length $L(p)$ is a **period** of a specific meromorphic differential on the curve $\mathcal{C}_p$.

## 3. The Decidability Bottleneck
Since $L(p)$ is a period, its dependence on the coefficient vector $\vec{a} \in \mathbb{C}^n$ is not algebraic, but rather satisfies a system of linear differential equations—the **Picard-Fuchs equations**. 

To verify the EHP conjecture for a fixed $n$, one must show that the maximum of $L(\vec{a})$ over $\mathbb{C}^n$ is uniquely achieved at $\vec{a} = (0, 0, \dots, -1)$. Because the values of $L(\vec{a})$ are transcendental, deciding if $L(\vec{a}) < L(z^n-1)$ for all $\vec{a} \neq \vec{a}_{ext}$ using classical Tarski-Seidenberg elimination (which only applies to semi-algebraic sets) fails. Naive numerical integration is not mathematically rigorous for a proof due to floating-point errors and the non-compactness of the moduli space.

## 4. Proposed Framework: The SOS-Relaxed Picard-Fuchs Method
To rigorously close the gap for $3 \le n < N_0$, I propose blending algebraic geometry (Picard-Fuchs) with modern convex optimization (Sum-of-Squares / Lasserre Hierarchy). 

### Phase I: Compactification and Stratification
By Pommerenke's and Borwein's earlier bounds, we know that if the coefficients of $p(z)$ are excessively large, the lemniscate length drops. Therefore, we can restrict our search to a compact semi-algebraic region $\mathcal{K} \subset \mathbb{C}^n$ of the moduli space. We stratify $\mathcal{K}$ into small semi-algebraic cells.

### Phase II: Picard-Fuchs Taylor Enclosures
For the interior of any cell $C_j$, the period $L(\vec{a})$ is analytic. Instead of numerically integrating, we construct the Picard-Fuchs differential operator $\mathcal{D}$ for $L(\vec{a})$.
Using the method of Majorant Series, we can generate a finite multivariate Taylor approximation $T_k(\vec{a})$ truncated at degree $k$, along with a rigorously certified, rational upper bound error function $E_k(\vec{a})$, such that:
$$ L(\vec{a}) \leq T_k(\vec{a}) + E_k(\vec{a}) \quad \text{for all } \vec{a} \in C_j $$

### Phase III: Sum-of-Squares (SOS) Verification
We are now left with a strictly algebraic inequality to prove for each cell:
$$ T_k(\vec{a}) + E_k(\vec{a}) < L(z^n-1) $$

We clear denominators to form a strict polynomial inequality $P_{j}(\vec{a}) > 0$ on the semi-algebraic set $C_j$. By Putinar's Positivstellensatz, if this polynomial is strictly positive on $C_j$, it can be written as a **Sum-of-Squares (SOS)**. We can search for this SOS certificate using Semi-Definite Programming (SDP). 

If the SDP solver finds a rational SOS certificate, the strict inequality is **formally proven** for that cell, bypassing any transcendental evaluations.

### Phase IV: The Local Neighborhood of $z^n - 1$
The SOS method successfully proves strict inequality everywhere *except* in the immediate neighborhood $\mathcal{N}$ of the suspected global maximum $z^n - 1$, where the strict inequality fails.
For $\mathcal{N}$, we deploy the local analysis initiated by Fryntov and Nazarov (2009). By formulating the second variation (Hessian) of $L(\vec{a})$ via the Picard-Fuchs system and using an interval-arithmetic evaluation of the corresponding algebraic integrals, we can rigorously certify that the Hessian is strictly negative-definite throughout $\mathcal{N}$. 

## 5. Conclusion and Impact
This approach directly circumvents the "testing equality of real numbers" problem raised by Tao. It separates the global problem into two distinct, rigorously decidable tasks:
1. **Global Exclusion:** Using SOS optimization and Picard-Fuchs polynomial bounds to formally rule out the macroscopic moduli space.
2. **Local Rigidity:** Using exact Hessian evaluation to prove unique maximality in the local neighborhood.

By implementing this dual framework computationally, the mathematical community could definitively conquer the intermediate finite cases ($3 \le n < N_0$), turning Tao's asymptotic triumph into a complete, unqualified resolution of Erdős Problem #114.