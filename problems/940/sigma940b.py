#!/usr/bin/env python3
# sigma940b.py — FREQUENCY-WEIGHTED p-adic singular factors for sums of three
# 3-powerful numbers, and validation against the measured census class-means.
#
# mu_p(c) = relative frequency of the class c mod p^e among cubefull numbers
#           (empirical = true p-adic measure, computed from the list up to 4e9)
# S(t)    = sum_{x+y+z = t} mu(x) mu(y) mu(z)   ->  sigma(t) = S(t)/mean(S)
#
import numpy as np

# ---------- build cubefull numbers <= 4e9 (recursive products) ----------
LIM = 4_000_000_000
primes = []
siv = bytearray(LIM ** (1/3) .__int__() + 2)
ub = int(round(LIM ** (1/3))) + 2
siv = bytearray(ub)
for i in range(2, ub):
    if not siv[i]:
        for j in range(i*i, ub, i):
            siv[j] = 1
primes = [i for i in range(2, ub) if not siv[i]]

cf = set([1])
def rec(v, start):
    for i in range(start, len(primes)):
        p = primes[i]
        t = v
        for _ in range(3):
            t *= p
            if t > LIM: return
        ve = v
        e = 0
        while ve <= LIM // p:
            ve *= p
            e += 1
            if e >= 3:
                if ve not in cf:
                    cf.add(ve)
                    rec(ve, i+1)
rec(1, 0)
cf = sorted(cf)
print(f"cubefull <= {LIM}: {len(cf)}")

# ---------- frequency measure mu mod 64 and mod 81 ----------
def measure(mod, plist):
    w = {}
    for m in plist:
        c = m % mod
        w[c] = w.get(c, 0) + 1.0
    tot = sum(w.values())
    return {c: v/tot for c, v in w.items()}

w64 = measure(64, cf)
w81 = measure(81, cf)

def weighted_sigma(mod, w):
    """sigma(t) = sum_{x+y+z=t} w(x)w(y)w(z), normalized to mean 1 over the modulus."""
    a = np.zeros(mod)
    for c, v in w.items():
        a[c] = v
    A = np.fft.rfft(np.concatenate([a, np.zeros(mod)]))
    conv = np.fft.irfft(A**3, 2*mod)
    S = np.zeros(mod)
    for i in range(len(conv)):
        S[i % mod] += conv[i]
    # mean of S over t equals 1/mod * sum_t S(t) = 1/mod (since weights sum to 1)
    sigma = S * mod  # mean 1
    return sigma

sig64 = weighted_sigma(64, w64)
sig81 = weighted_sigma(81, w81)

print("\n=== sigma_2(t) frequency-weighted, exact (mod 64), grouped mod 8 and mod 16 ===")
print("class:  sigma    | measured census mean-R / overall mean  (offset CORRECTED)")
meas8 = {0: 14.24, 1: 5.33, 2: 2.02, 3: 4.55, 4: 2.00, 5: 4.27, 6: 1.99, 7: 4.21}
# NOTE on the correction: in stats940.c the class label was off by +1 mod 8, and
# mod-9 classes were off by +6, mod-27 by +15 (window start offsets).
mmean = sum(meas8.values())/8
for t in range(8):
    s = np.mean([sig64[t], sig64[t+8], sig64[t+16], sig64[t+24], sig64[t+32], sig64[t+40], sig64[t+48], sig64[t+56]])
    print(f"  t≡{t} (mod 8):  {s:8.4f}   | {meas8[t]/mmean:8.4f}")
print("mod 16 detail:")
for t in range(16):
    s = np.mean([sig64[t], sig64[t+16], sig64[t+32], sig64[t+48]])
    print(f"  t≡{t:2d} (mod 16):  {s:8.4f}")

print("\n=== sigma_3(t) frequency-weighted, grouped mod 9 (offset-corrected census below) ===")
# true class exceptions fractions from run1 mod9 with +6 offset:
# true classes: fraction of exceptions in (5e8, 1e9]
exc9 = {0: 0.0466, 1: 0.0161, 2: 0.0545, 3: 0.1034, 4: 0.0697, 5: 0.0720, 6: 0.1041, 7: 0.0540, 8: 0.0167}
for t in range(9):
    s = np.mean([sig81[t], sig81[t+9], sig81[t+18], sig81[t+27], sig81[t+36], sig81[t+45], sig81[t+54], sig81[t+63], sig81[t+72]])
    print(f"  t≡{t} (mod 9):  sigma={s:8.4f}   exc.frac={exc9[t]:.4f}   e^{{-6.1*sigma}}={np.exp(-6.1*s):.4f}")

print("\n=== sigma_3(t) mod 27 detail ===")
for t in range(27):
    s = np.mean([sig81[t], sig81[t+27], sig81[t+54]])
    print(f"  t≡{t:2d}(mod 27): {s:8.4f}", end="  ")
    if t % 9 == 8: print()

print("\n=== joint 2x3 model: exception fraction ~ exp(-lam_eff * sig2*sig3), lam_eff=6.1 ===")
lam = 6.1
tot = 0.0
for t2 in range(8):
    s2 = np.mean([sig64[t2+k*8] for k in range(8)])
    for t3 in range(9):
        s3 = np.mean([sig81[t3+k*9] for k in range(9)])
        p = np.exp(-lam*s2*s3)
        tot += p/72
print(f"predicted exception fraction at lam_eff={lam}: {tot:.4f}   (census ~0.052-0.060)")

print("\n=== asymptotic prediction, lam -> 11.96 (full-strength multiset mean) ===")
for lam in [8.0, 11.96]:
    tot = 0.0
    contrib = {}
    for t2 in range(8):
        s2 = np.mean([sig64[t2+k*8] for k in range(8)])
        for t3 in range(9):
            s3 = np.mean([sig81[t3+k*9] for k in range(9)])
            p = np.exp(-lam*s2*s3)
            tot += p/72
            contrib[(t2%4, t3)] = p
    print(f"lam={lam}: predicted overall exception density ~ {tot:.5f}")
