#!/usr/bin/env python3
# verif940.py — zero-free-parameter test of the local model:
#   P(n exceptional) ~ exp(-lambda(x) * s2(n mod 64) * s3(n mod 81))
# with EXACT asymptotic s2, s3 and lambda(x) = 11.961*(C3(x)/C3)^3  (kappa = 1 !).
# Compared against the measured census cells at (2e9, 4e9] and (5e8, 1e9].
import numpy as np

# ---- exact phi_p and class weights (as in exact940.py) ----
def phi_p(p):
    D = 1 + p**(-4/3) + p**(-5/3)
    num = {}
    for alpha in range(0, 30):
        for beta in (0, 1):
            for gamma in (0, 1):
                if beta and gamma: continue
                k = 3*alpha + 4*beta + 5*gamma
                num[k] = num.get(k, 0.0) + (p-1)/p**(alpha+1) * p**(-(4*beta+5*gamma)/3)
    return {k: num.get(k, 0.0)/D for k in range(0, 13)}, D

def exact_weights(p, e, phi):
    mod = p**e
    w = np.zeros(mod)
    for k in range(0, e):
        if k in (1, 2): continue
        pk = p**k
        nunits = (p-1)*p**(e-k-1)
        for u in range(1, p**(e-k)):
            if u % p != 0:
                w[pk*u] += phi[k]/nunits
    w[0] += 1.0 - sum(phi[k] for k in range(0, e) if k not in (1, 2))
    return w

def sigma_from_weights(w):
    mod = len(w)
    A = np.fft.rfft(np.concatenate([w, np.zeros(mod)]))
    conv = np.fft.irfft(A**3, 2*mod)
    S = np.zeros(mod)
    for i in range(len(conv)):
        S[i % mod] += conv[i]
    return S*mod

phi2, _ = phi_p(2); phi3, _ = phi_p(3)
sig2 = sigma_from_weights(exact_weights(2, 6, phi2))   # mod 64
sig3 = sigma_from_weights(exact_weights(3, 4, phi3))   # mod 81

C3 = 4.6537165
def lam_multiset(x, c3x):     # multiset mean at scale x
    return 11.9611 * (c3x/C3)**3

# empirical C3(x): cubefull counts (from the 4e9 list)
cub = {}
for X, c in [(125e6, 1781), (250e6, 2276), (5e8, 2908), (1e9, 3721), (2e9, 4752), (4e9, 6058)]:
    cub[X] = c

def P_exc(n, lam):
    return np.exp(-lam * sig2[n % 64] * sig3[n % 81])

def cell_means(lam):
    """average P_exc over groups of classes, uniform over residues."""
    groups = {}
    cnt = {}
    for a in range(16):       # mod 16 captures v2
        for b in range(81):   # mod 81 captures all v3 detail
            # resolve combined residue exists by CRT (16,81 coprime)
            v2 = 0 if a % 2 == 1 else (1 if a % 4 == 2 else (2 if a % 8 == 4 else 3))
            if b % 9 == 0 and b != 0 and b % 27 != 0 and False: pass
            if b == 0: v3 = 4
            elif b % 27 == 0 and b % 81 != 0: v3 = 3
            elif b % 27 == 0 and b == 0: v3 = 4
            elif b % 9 == 0: v3 = 2
            elif b % 3 == 0: v3 = 1
            else: v3 = 0
            # find n with n%64 == a (mod 64) and n%81 == b: use a directly (16 | 64)
            p = np.exp(-lam * sig2[a] * sig3[b])
            g = (min(v2,3), v3)
            groups[g] = groups.get(g, 0.0) + p
            cnt[g] = cnt.get(g, 0) + 1
    return {g: groups[g]/cnt[g] for g in groups}

print("=== predicted vs measured exception fractions (kappa=1, lambda from C3(x) running) ===")
for (lo, hi) in [(2e9, 4e9), (5e8, 1e9)]:
    xm = (lo*hi)**0.5
    c3x = cub[hi] / hi**(1/3) * xm**(1/3)   # interpolate C3 at geometric mid
    c3x = cub[hi] / hi**(1/3)
    lam = lam_multiset(xm, c3x)
    cm = cell_means(lam)
    print(f"\noctave ({lo:.1e},{hi:.1e}]:  C3(x_mid)={c3x:.4f}  lambda_multiset={lam:.3f}")
    meas_hi = {(0,0):0.00975,(1,0):0.12640,(2,0):0.12629,(3,0):0.000005,
               ('u',0):0.04047,('u',1):0.09301,('u',2):0.04151}  # 'u' = mixed over v2
    # aggregate to v2 rows (v3 mixed) and v3 rows (v2 mixed), like the census printout
    for v2 in [0,1,2,3]:
        num = sum(cm[(v2,v3)]*cnt2 for (g,v3),cnt2 in [((v2,x),1) for x in []]) # placeholder
    # print full grid
    print("        v3=0(units)  v3=1    v3=2   v3>=3(0mod27&81... showing groups)")
    for v2 in [0,1,2,3]:
        row = f"  v2={v2}: "
        for v3 in [0,1,2,3,4]:
            if (v2,v3) in cm: row += f" {cm[(v2,v3)]:.5f} "
            else: row += "   -    "
        print(row)

# measured grids at (2e9,4e9]: known cells
print("\n=== aggregate cells for direct comparison ===")
for label, hi, lo, meas in [
    ("top octave (2e9,4e9]", 4e9, 2e9,
     {"v2=0 (odd)":0.00975, "v2=1":0.12640, "v2=2":0.12629, "v2>=3":0.000005,
      "v3=0 (units mod 9)":0.04047, "v3=1":0.09301, "v3=0mod9 (mixed v3>=2)":0.04151}),
    ("octave (5e8,1e9]", 1e9, 5e8,
     {"v2=0 (odd)":0.01308, "v2=1":0.14166, "v2=2":0.14187, "v2>=3":0.0,
      "v3=0 (units mod 9)":0.04719, "v3=1":0.10373, "v3=0mod9 (mixed v3>=2)":0.04660}),
]:
    xm = (lo*hi)**0.5
    c3x = cub[hi] / hi**(1/3)
    lam = lam_multiset(xm, c3x)
    print(f"\n{label}: lambda={lam:.3f}")
    # v2 rows: average over all 81 mod-81 classes
    for v2, key in [(0,"v2=0 (odd)"), (1,"v2=1"), (2,"v2=2"), (3,"v2>=3")]:
        acc = 0.0
        for a in range(16):
            v = 0 if a%2==1 else (1 if a%4==2 else (2 if a%8==4 else 3))
            if v != v2: continue
            for b in range(81):
                acc += np.exp(-lam*sig2[a]*sig3[b])
        pred = acc/( len([a for a in range(16) if (0 if a%2==1 else (1 if a%4==2 else (2 if a%8==4 else 3)))==v2]) *81)
        print(f"  {key:22s}: pred {pred:.5f}   meas {meas[key]:.5f}")
    # v3 rows: average over 16 classes
    for v3sel, key in [("units","v3=0 (units mod 9)"), ("one","v3=1"), ("9","v3=0mod9 (mixed v3>=2)")]:
        acc = 0.0; nb = 0
        for b in range(81):
            if v3sel=="units" and b%3!=0: ok=True
            elif v3sel=="one" and (b%3==0 and b%9!=0): ok=True
            elif v3sel=="9" and b%9==0: ok=True
            else: ok=False
            if not ok: continue
            nb += 1
            for a in range(16):
                acc += np.exp(-lam*sig2[a]*sig3[b])
        pred = acc/(nb*16)
        print(f"  {key:22s}: pred {pred:.5f}   meas {meas[key]:.5f}")

# overall predicted exception density per octave
print("\n=== overall octave density ===")
for lo, hi, m in [(1e9,2e9,0.05610),(5e8,1e9,0.05969),(2.5e8,5e8,0.06424),(2e9,4e9,0.05226)]:
    xm = (lo*hi)**0.5
    c3x = cub[hi] / hi**(1/3)
    lam = lam_multiset(xm, c3x)
    acc = 0.0
    for a in range(64):
        for b in range(81):
            acc += np.exp(-lam*sig2[a]*sig3[b])
    print(f"  ({lo:.1e},{hi:.1e}]: pred {acc/(64*81):.5f}   meas {m:.5f}")
