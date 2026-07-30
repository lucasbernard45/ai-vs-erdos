## Report on the Asymptotic Obstruction Analysis for Erdős Problem #1108

---

### Executive Summary

The technical note investigates whether local $p$-adic valuation gaps can be used to construct an unconditional proof of finiteness for Erdős Problem 1108. While the note ultimately reaches a flawed conclusion due to an algebraic non sequitur, its foundational setup inadvertently provides the exact mathematical framework needed to unconditionally rule out infinite solutions for tightly clustered index gaps.

---

### 1. What the Note Proposed

The document attempted to map the boundaries of local modular constraints to see if they could rule out large powerful factorial sums without relying on unproven conjectures like $abc$. Its core arguments and proposals are as follows:

* **Algebraic Factorization:** It proposed factoring the factorial sum $N$ into the form $N = n_1! \cdot M$, isolating a cofactor $M = 1 + \sum_{i=2}^r \frac{n_i!}{n_1!}$.


* **The Prime Product Constraint:** It established a strict necessary condition: for $N$ to be powerful, $M$ must be a multiple of $P$, where $P$ is the product of all primes in the interval $(n_1/2, n_1]$. This mathematically demands that $M \ge P$.


* **The Asymptotic Growth Comparison:** The note calculated that $P$ grows exponentially, behaving asymptotically as $P \sim e^{n_1/2}$. It then compared this to the super-exponential growth of the factorial base $n_1!$.


* **The "Wall" Conclusion:** The note argued that because $P \ll n_1!$, the cofactor $M$ retains vast combinatorial freedom and can easily be a multiple of $P$ without violating size constraints. Therefore, it concluded that local modular methods fail and an unconditional proof is impossible through this avenue.



---

### 2. The Core Logical Flaw

The note's conclusion fails due to a critical misstep in comparing variables. It justifies the combinatorial freedom of the cofactor $M$ by pointing to the massive size of the factorial base $n_1!$. However, the magnitude of $n_1!$ has absolutely no mathematical bearing on the size or divisibility of $M$. The value of $M$ is dictated exclusively by the spacing of the subsequent indices ($n_2, n_3, \dots, n_r$). By incorrectly tethering the size of $M$ to $n_1!$, the author dismisses the very constraint that solves a major piece of the puzzle.

---

### 3. How This Setup Actually Helps the Proof

Despite the erroneous conclusion, the note’s mathematical setup—specifically the strict requirement that $M \ge P$—is highly valuable. Instead of proving that local methods are useless, this exact framework provides a **partial unconditional proof** when applied correctly.

By binding the size of $M$ to the index gaps rather than $n_1!$, we can use the note's framework to unconditionally rule out specific families of factorial sums:

* **Bounding the Cofactor:** Consider a factorial sum with tightly clustered indices, which empirical data suggests is the most likely form for powerful numbers. If we take the tightest possible gap where $n_r = n_1 + 1$, the cofactor reduces strictly to $M = n_1 + 2$.
* **Applying the Prime Product Growth:** The note correctly proves that $P$ grows exponentially as $P \sim e^{n_1/2}$.


* **The Unconditional Barrier:** For any sufficiently large $n_1$, the exponential value $e^{n_1/2}$ will strictly exceed the linear value $n_1 + 2$. Therefore, $P > M$.
* **The Result:** Because $M$ must be a multiple of $P$ for the sum to be powerful, and a positive integer cannot be a multiple of a number larger than itself, this proves with absolute certainty that **no powerful factorial sums can exist for tightly clustered indices at large values of $n_1$.**



In short, the note accidentally provided the blueprint for an unconditional proof of non-existence for bounded index gaps. To push the proof further, researchers would simply need to apply wider bounds to $M$ and compare them against the exponential growth of $P$.
