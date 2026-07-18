#!/usr/bin/env python3
# sigma940.py — exact p-adic singular densities sigma_p(t) for sums of three
# 3-powerful ("cubefull") numbers, via the stabilized residue structure.
#
# Cubefull residues mod p^e (Lemma 2.1 of the research note, p odd or p=2, e>=r=3):
#   R(p^e) = {units mod p^e} ∪ {p^3 * w mod p^e}
# Reduction mod p^e -> p^{e-1} has uniform fibers of size p for e >= 4, so the
# normalized density  sigma_p(t) = lim_e p^{2e} N_e(t) / |R(p^e)|^3
# stabilizes EXACTLY at e = 3 (proved in the note). So finite computation is exact.
import numpy as np

def residues(p, e):
    R = set()
    pe = p ** e
    for u in range(1, pe):
        if u % p != 0:
            R.add(u)
    if e >= 3:
        for w in range(pe // (p ** 3) + 1):
            R.add((p ** 3 * w) % pe)
    return np.array(sorted(R), dtype=np.int64), pe

def sigma_table(p, e=3):
    R, pe = residues(p, e)
    a = np.zeros(pe, dtype=np.int64)
    a[R] = 1
    # circular convolution a * a * a  (counts ordered triples summing to t mod pe)
    n = pe
    A = np.fft.rfft(np.concatenate([a, np.zeros(n, dtype=np.int64)]))  # size 2n: linear conv ok
    c = np.fft.irfft(A * A * A, 2 * n)
    c = np.rint(c).astype(np.int64)
    conv = np.zeros(n, dtype=np.int64)
    for i in range(len(c)):
        conv[i % n] += c[i]
    assert conv.sum() == len(R) ** 3, f"sanity: {conv.sum()} != {len(R)**3}"
    M = len(R)
    # sigma(t) = N(t) * pe / M^3   (mean over t equals 1)
    return conv, M, pe

def report(p, e, show_mod):
    conv, M, pe = sigma_table(p, e)
    print(f"\n=== sigma_{p}(t),  base modulus {pe} (stabilized), |R| = {M} ===")
    m = show_mod
    print(f"per class t mod {m}:  sigma value (exact, as fraction N*pe/M^3)")
    vals = {}
    for t in range(m):
        total = sum(conv[t::m])
        cnt = len(conv[t::m])
        # sigma for the class: N-class normalized: mean sigma over residues in class
        sig = total * pe / (M ** 3) / cnt
        vals[t] = (total, cnt, sig)
    for t in range(m):
        total, cnt, sig = vals[t]
        from fractions import Fraction
        fr = Fraction(total * pe, cnt * M ** 3).limit_denominator(10 ** 6)
        print(f"  t ≡ {t:3d} (mod {m}):  sigma = {sig:.6f}   ≈ {fr}")
    mx = max(vals[t][2] for t in vals)
    mn = min(vals[t][2] for t in vals)
    print(f"  max sigma = {mx:.6f}, min sigma = {mn:.6f}, max|sigma-1| = {mx-1:.6f}/{1-mn:.6f}")
    return vals

# --- p = 2, modulus 16 and 8 ---
v16 = report(2, 5, 16)   # e=5 (mod 32), grouped mod 16; mod-8 classes are stabilized
report(2, 5, 8)

# --- p = 3, modulus 27 ---
report(3, 3, 27)

# --- p = 5, 7, 11, 13: deviation from 1 ---
for p in [5, 7, 11, 13, 17]:
    conv, M, pe = sigma_table(p, 3)
    sig = conv * pe / (M ** 3)
    print(f"p={p:2d}: max sigma = {sig.max():.6f}, min sigma = {sig.min():.6f}, "
          f"max|sigma-1| = {max(sig.max()-1, 1-sig.min()):.6f}")
