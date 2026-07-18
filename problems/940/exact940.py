#!/usr/bin/env python3
# exact940.py — EXACT asymptotic local frequency laws for 3-powerful numbers
# and the corresponding frequency-weighted singular factors sigma_2, sigma_3.
#
# Canonical form: every 3-powerful n has a UNIQUE factorisation
#     n = a^3 b^4 c^5 ,  b,c squarefree, gcd(b,c)=1.
# Hence  v_p(n) = 3*alpha + 4*beta + 5*gamma,  alpha>=0, beta,gamma in {0,1}, beta*gamma=0.
#
# Weight (leading term of the count of n<=x) for the p-part (alpha,beta,gamma):
#     w_p(alpha,beta,gamma) = (p-1)/p^{alpha+1} * p^{-(4*beta+5*gamma)/3}
# (since #{a<=Y : v_p(a)=alpha} ~ Y*(p-1)/p^{alpha+1}).
# So  phi_p(k) = P(v_p(n)=k) = [sum_{3a+4b+5g=k} w_p(a,b,g)] / D_p,
#     D_p = 1 + p^{-4/3} + p^{-5/3}
# (the sum over alpha telescopes to 1).
#
# Conditional on v_p(n)=k < e, n mod p^e is p^k * U with U EXACTLY uniform over
# units mod p^{e-k}: the c'-part is uniform over units (c'^5 is a bijection on
# (Z/2^e)* and on (Z/3^e)* since gcd(5,2)=gcd(5,3)=1; equidistribution of the
# squarefree parts over unit classes holds by inclusion-exclusion), and unit x unit
# is uniform.  => the asymptotic class frequencies are EXPLICIT constants.
#
# We also verify against the empirical list of cubefull numbers <= 4e9 (6058).
import numpy as np

# ---------------- exact phi_p(k) ----------------
def phi_p(p, kmax):
    D = 1 + p**(-4/3) + p**(-5/3)
    num = {}
    for alpha in range(0, 30):
        for beta in (0, 1):
            for gamma in (0, 1):
                if beta and gamma: continue
                k = 3*alpha + 4*beta + 5*gamma
                w = (p-1)/p**(alpha+1) * p**(-(4*beta+5*gamma)/3)
                num[k] = num.get(k, 0.0) + w
    return {k: num.get(k, 0.0)/D for k in range(kmax+1)}, D

phi2, D2 = phi_p(2, 12)
phi3, D3 = phi_p(3, 12)
print(f"D_2 = 1+2^(-4/3)+2^(-5/3) = {D2:.6f}   D_3 = {D3:.6f}")
print("phi_2(k):", {k: round(v,6) for k,v in phi2.items()})
print("phi_3(k):", {k: round(v,6) for k,v in phi3.items()})

# ---------------- exact class-frequency vector mod p^e ----------------
def exact_weights(p, e, phi):
    """asymptotic frequency of each residue class mod p^e among cubefull numbers."""
    mod = p**e
    w = np.zeros(mod)
    # v_p(n) = k, k < e: classes p^k*u, u unit mod p^{e-k}: count phi(p-1)p^{e-k-1}
    for k in range(0, e):
        if k in (1, 2) : continue
        if k not in phi: continue
        pk = p**k
        nunits = (p-1)*p**(e-k-1)
        for u in range(1, p**(e-k)):
            if u % p != 0:
                w[pk*u] += phi[k]/nunits
    # v_p(n) >= e: class 0
    w[0] += 1.0 - sum(phi[k] for k in range(0, e) if k not in (1,2) or k < 3 and False) \
                   + (phi.get(1,0)+phi.get(2,0))  # k=1,2 impossible anyway (0 mass)
    return w

def sigma_from_weights(w):
    mod = len(w)
    A = np.fft.rfft(np.concatenate([w, np.zeros(mod)]))
    conv = np.fft.irfft(A**3, 2*mod)
    S = np.zeros(mod)
    for i in range(len(conv)):
        S[i % mod] += conv[i]
    return S*mod

# ---------------- build empirical list, compare ----------------
LIM = 4_000_000_000
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
        ve = v; e = 0
        while ve <= LIM//p:
            ve *= p; e += 1
            if e >= 3:
                if ve not in cf:
                    cf.add(ve); rec(ve, i+1)
rec(1, 0); cf = sorted(cf)
print(f"\ncubefull <= 4e9: {len(cf)}")

def empirical(mod):
    w = np.zeros(mod)
    for m in cf: w[m % mod] += 1.0
    return w/len(cf)

# convergence trend of P(v_2 = 0) among cubefull <= x
print("\nP(n odd | cubefull <= x) trend (exact asymptotic value %.6f):" % phi2[0])
for X in [10**5, 10**6, 10**7, 10**8, 10**9, 4*10**9]:
    cnt = sum(1 for m in cf if m <= X and m % 2 == 1)
    tot = sum(1 for m in cf if m <= X)
    print(f"  x={X:>11d}: {cnt}/{tot} = {cnt/tot:.6f}")

# ---------------- sigma_2 exact mod 64, grouped ----------------
w64e = exact_weights(2, 6, phi2)
w64i = empirical(64)
print(f"\ncheck sums: exact={w64e.sum():.9f} empirical={w64i.sum():.9f}")
print(f"L1 distance exact vs empirical mod 64: {np.abs(w64e-w64i).sum():.5f}")
sig2e = sigma_from_weights(w64e)
sig2i = sigma_from_weights(w64i)

def grp(sig, mod, base):
    out = {}
    for t in range(base):
        out[t] = float(np.mean([sig[t], *[sig[t+k*base] for k in range(1, mod//base)]]))
    return out

meas8 = {0:2.9505, 1:1.1044, 2:0.4185, 3:0.9428, 4:0.4144, 5:0.8847, 6:0.4123, 7:0.8723}
print("\n  t mod 8 :   sigma_2 EXACT   sigma_2 empirical4e9   census mean-R/norm")
g2e, g2i = grp(sig2e, 64, 8), grp(sig2i, 64, 8)
for t in range(8):
    print(f"  t=={t}   :   {g2e[t]:8.4f}        {g2i[t]:8.4f}           {meas8[t]:8.4f}")
print("\n  mod 16 detail (exact vs empirical):")
for t in range(16):
    se = float(np.mean([sig2e[t], sig2e[t+16], sig2e[t+32], sig2e[t+48]]))
    si = float(np.mean([sig2i[t], sig2i[t+16], sig2i[t+32], sig2i[t+48]]))
    print(f"  t=={t:2d} :  {se:8.4f}   {si:8.4f}")

# ---------------- sigma_3 exact mod 81, grouped ----------------
w81e = exact_weights(3, 4, phi3)
w81i = empirical(81)
print(f"\ncheck sums: exact={w81e.sum():.9f} empirical={w81i.sum():.9f}")
print(f"L1 distance exact vs empirical mod 81: {np.abs(w81e-w81i).sum():.5f}")
sig3e = sigma_from_weights(w81e)
sig3i = sigma_from_weights(w81i)
exc9 = {0:0.0466, 1:0.0161, 2:0.0545, 3:0.1034, 4:0.0697, 5:0.0720, 6:0.1041, 7:0.0540, 8:0.0167}
print("\n  t mod 9 :  sigma_3 EXACT   empirical   census exc.frac")
for t in range(9):
    se = float(np.mean([sig3e[t+k*9] for k in range(9)]))
    si = float(np.mean([sig3i[t+k*9] for k in range(9)]))
    print(f"  t=={t}   :   {se:8.4f}     {si:8.4f}     {exc9[t]:.4f}")
print("\n  mod 27 detail (exact vs empirical):")
for t in range(27):
    se = float(np.mean([sig3e[t], sig3e[t+27], sig3e[t+54]]))
    si = float(np.mean([sig3i[t], sig3i[t+27], sig3i[t+54]]))
    print(f"  t=={t:2d}(mod27): {se:8.4f}  {si:8.4f}")

# ---------------- joint model ----------------
print("\n=== joint model: exception prob ~ exp(-kappa*lam*sig2*sig3), lam=11.96 multiset ===")
def joint(sig2, sig3, kappa, lam):
    tot = 0.0; per = {}
    for t2 in range(8):
        s2 = float(np.mean([sig2[t2+k*8] for k in range(8)]))
        for t3 in range(9):
            s3 = float(np.mean([sig3[t3+k*9] for k in range(9)]))
            p = np.exp(-kappa*lam*s2*s3)
            tot += p/72.0
            per[(t2,t3)] = p
    return tot, per
for kappa in [0.5, 0.51, 1.0]:
    tot, _ = joint(sig2e, sig3e, kappa, 11.96)
    toti, _ = joint(sig2i, sig3i, kappa, 11.96)
    print(f"  kappa={kappa}: exact-sigmas -> {tot:.5f}   empirical-sigmas -> {toti:.5f}   (census .0523-.0597)")

# per-class exact predictions at kappa=0.51 (fit value from lam_eff=6.1/11.96)
tot, per = joint(sig2e, sig3e, 0.51, 11.96)
print("\npredicted exception fraction by (t mod 8, t mod 9), exact sigma, kappa=0.51:")
hdr = "        " + "".join(f" m9={t:2d} " for t in range(9))
print(hdr)
for t2 in range(8):
    row = f"  m8={t2}  " + "".join(f"{per[(t2,t3)]:6.3f} " for t3 in range(9))
    print(row)
