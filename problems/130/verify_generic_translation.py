#!/usr/bin/env python3
"""
Algorithmic verification of generic translation lemma for Erdos 130.

Given finite A, B, find t avoiding:
- integer cross distances
- collinear mixed triples
- concyclic mixed quadruples

Random continuous sampling succeeds with probability 1 because bad set is measure 0.
"""

import random, math
import itertools
from typing import List, Tuple

Point = Tuple[float,float]

def dist(p:Point,q:Point)->float:
    return math.hypot(p[0]-q[0], p[1]-q[1])

def det2(ax,ay,bx,by): return ax*by - ay*bx

def collinear(p,q,r,eps=1e-9)->bool:
    return abs(det2(q[0]-p[0], q[1]-p[1], r[0]-p[0], r[1]-p[1])) < eps

def concyclic(p,q,r,s,eps=1e-7)->bool:
    # det | x y x^2+y^2 1 |
    import numpy as np
    M = [
        [p[0], p[1], p[0]**2+p[1]**2, 1],
        [q[0], q[1], q[0]**2+q[1]**2, 1],
        [r[0], r[1], r[0]**2+r[1]**2, 1],
        [s[0], s[1], s[0]**2+s[1]**2, 1],
    ]
    det=0
    # compute via expansion (use numpy for simplicity if available)
    try:
        det = np.linalg.det(np.array(M))
    except:
        # manual
        # use formula - simplified fallback
        pass
    return abs(det) < eps

def is_integer_dist(d,eps=1e-7)->bool:
    if d < 0.5: return False
    rd = round(d)
    return abs(d-rd) < eps and rd>=1

def translate(B:List[Point], t:Point)->List[Point]:
    return [(b[0]+t[0], b[1]+t[1]) for b in B]

def check_valid(A,Bt,eps=1e-7)->Tuple[bool,str]:
    # cross integer distances
    for a in A:
        for b in Bt:
            d=dist(a,b)
            if is_integer_dist(d,eps):
                return False, f"integer cross dist {a} {b} d={d}"
    # collinear triples mixed
    S=A+Bt
    # check all triples that straddle
    for p,q,r in itertools.combinations(S,3):
        # if triple fully inside A or fully inside Bt, assume already ok by input assumption
        inA = sum(1 for x in (p,q,r) if x in A)
        if inA==0 or inA==3:
            # could still check but skip for generic lemma focusing on mixed
            pass
        # check mixed triples
        if inA==1 or inA==2:
            if collinear(p,q,r,eps=1e-7):
                return False, f"collinear mixed {p,q,r}"
    # concyclic quadruples mixed
    for quad in itertools.combinations(S,4):
        inA = sum(1 for x in quad if x in A)
        if inA==0 or inA==4:
            continue
        if concyclic(*quad, eps=1e-6):
            return False, f"concyclic mixed {quad}"
    return True, "ok"

def find_translation(A,B, attempts=1000, R=5000):
    for _ in range(attempts):
        t = (random.uniform(-R,R), random.uniform(-R,R))
        Bt = translate(B,t)
        ok,msg = check_valid(A,Bt)
        if ok:
            return t, Bt
    return None,None

if __name__ == "__main__":
    # Example: Use known 7-point heptagon approximated (Kreisel-Kurz example is more complex)
    # For demonstration we use random strongly general sets: perturbations of random points to avoid collinear/cocircular.
    random.seed(0)
    def random_strongly_general(n)->List[Point]:
        pts=[]
        while len(pts)<n:
            p = (random.uniform(0,10), random.uniform(0,10))
            # check against existing for collinear/cocircular (simple)
            bad=False
            for q,r in itertools.combinations(pts,2):
                if collinear(q,r,p,1e-6):
                    bad=True
                    break
            if bad: continue
            for q,r,s in itertools.combinations(pts,3):
                if concyclic(q,r,s,p,1e-6):
                    bad=True
                    break
            if not bad:
                pts.append(p)
        return pts

    A = random_strongly_general(5)
    B = random_strongly_general(7)

    print("A=",A)
    print("B=",B)

    t,Bt = find_translation(A,B, attempts=5000, R=2000)
    if t:
        print(f"Found t={t}")
        print("Bt=",Bt)
        # verify integer-distance disjointness
        # also compute chromatic lower bound: check K7? Not computed here
    else:
        print("Failed to find translation (unlikely)")

    # Test bounded-gap lemma for 1108 comparison: translation doesn't need to avoid integer distances for general position only,
    # but we also avoid integer distances exactly.
