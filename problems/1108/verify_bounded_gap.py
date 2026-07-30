#!/usr/bin/env python3
"""
Verification for bounded-gap unconditional finiteness on Erdos 1108.
Provides explicit thresholds where P(n1) > polynomial bound for M,
and brute-force enumeration for D=1,2.
"""
import math
from sympy import primerange

def product_interval(n1):
    P=1
    for p in primerange(n1//2+1, n1+1):
        P*=p
    return P

def max_M_bound(n1, D):
    # r <= D+1, each term <= (n1+D)^D
    return 1 + (D+1)*((n1+D)**D)

def is_powerful(n):
    if n < 2:
        return True
    temp=n
    d=2
    while d*d <= temp:
        if temp % d == 0:
            cnt=0
            while temp % d == 0:
                temp//=d
                cnt+=1
            if cnt < 2:
                return False
        d+=1 if d==2 else 2
    if temp>1:
        return False
    return True

def enumerate_powerful(D, n1_max):
    res=[]
    for n1 in range(2, n1_max+1):
        indices = list(range(n1, n1+D+1))
        k=len(indices)
        for mask in range(1, 1<<k):
            if not (mask & 1): # must include n1
                continue
            s=sum(math.factorial(indices[i]) for i in range(k) if mask>>i &1)
            if is_powerful(s):
                S = [indices[i] for i in range(k) if mask>>i &1]
                res.append((n1, s, S))
    # deduplicate by value+set
    uniq={}
    for _, s, S in res:
        uniq[(s,tuple(S))]=True
    return list(uniq.keys())

if __name__ == "__main__":
    print("=== Thresholds ===")
    for D in [1,2,3,5]:
        for n1 in range(10, 80):
            P=product_interval(n1)
            Mb=max_M_bound(n1,D)
            if P>Mb:
                print(f"D={D} threshold N0 <= {n1}: P={P} > bound {Mb}")
                break
    print("\n=== Enumeration D=1 up to 25 ===")
    for s,S in enumerate_powerful(1,25):
        print(s,S)
    print("\n=== Enumeration D=2 up to 30 ===")
    for s,S in enumerate_powerful(2,30):
        print(s,S)
