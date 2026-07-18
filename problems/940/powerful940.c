/* powerful940.c — computations for the research note on Erdos Problem #940
 *
 *  1. Exact constants C_r = lim_{x->oo} P_r(x)/x^{1/r} via Euler products,
 *     and lambda_r = C_r^r * Gamma(1+1/r)^r  (mean # of representations).
 *  2. Enumerate 3-powerful ("cubefull") numbers <= 1e9; verify count vs C_3.
 *  3. Census: which n <= 1e9 are sums of <= 3 cubefull numbers?
 *     (exceptions per dyadic window, largest exceptions, class structure)
 *  4. Representation histogram R(n) and 3-fold additive energy at N = 3e7.
 *
 * Compile: gcc -O3 -march=native -o powerful940 powerful940.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

#define NLIM   1000000000LL          /* support census limit */
#define HLIM   30000000LL            /* R(n)-histogram limit  */

/* ---------- primes up to 3e6 (for Euler products and generation) ---------- */
static int PMAX = 3000000;
static int *primes, nprimes;
static void sieve_primes(void){
    static char *c;
    c = calloc(PMAX+1,1);
    long long i,j;
    for(i=2;i<=PMAX;i++) if(!c[i]){ for(j=i*i;j<=PMAX;j+=i) c[j]=1; }
    nprimes=0;
    for(i=2;i<=PMAX;i++) if(!c[i]) nprimes++;
    primes=malloc((nprimes+1)*sizeof(int));
    long long k=0;
    for(i=2;i<=PMAX;i++) if(!c[i]) primes[k++]=i;
    primes[k]=0;
    free(c);
}

/* ---------- C_r by Euler product: C_r = prod_p (1 + sum_{e=r+1..2r-1} p^{-e/r}) --- */
static double Cr(int r){
    double prod = 1.0;
    for(int i=0; primes[i]; i++){
        double p = primes[i];
        double s = 0.0;
        for(int e=r+1; e<=2*r-1; e++) s += pow(p, -(double)e/r);
        prod *= 1.0 + s;
    }
    return prod;
}

/* ---------- generate r-powerful numbers <= N by recursion over primes ---------- */
static long long *A; static long long nA, capA;
static void pushA(long long v){ if(nA==capA){ capA*=2; A=realloc(A,capA*sizeof(long long)); } A[nA++]=v; }
static void rec(int r, long long N, long long v, int start){
    for(int i=start; primes[i]; i++){
        long long p = primes[i];
        /* need v * p^r <= N else break */
        __int128 t = v;
        for(int e=1;e<=r;e++){ t *= p; if(t > N){ t=-1; break; } }
        if(t == -1) break;
        long long ve = v;
        for(int e=1;; e++){
            if(ve > N/p) break;
            ve *= p;
            if(e >= r){ pushA(ve); rec(r, N, ve, i+1); }
        }
    }
}
static int cmp_ll(const void *a, const void *b){ long long x=*(const long long*)a, y=*(const long long*)b; return (x>y)-(x<y); }
static long long upper_bound_ll(long long *arr, long long n, long long v){ long long lo=0, hi=n; while(lo<hi){ long long mid=(lo+hi)/2; if(arr[mid]<=v) lo=mid+1; else hi=mid; } return lo; }

int main(void){
    sieve_primes();

    printf("=== 1. Constants C_r and lambda_r (Euler products, primes <= %d) ===\n", PMAX);
    for(int r=2; r<=7; r++){
        double c = Cr(r);
        double tgam_local = pow(c, r) * pow(tgamma(1.0 + 1.0/r), r);
        printf("r=%d : C_r = %.8f   lambda_r = C_r^r*Gamma(1+1/r)^r = %.4f  e^{-lambda} = %.3g\n",
               r, c, tgam_local, exp(-tgam_local));
    }

    /* ---- build cubefull numbers up to NLIM ---- */
    capA = 1<<20; A = malloc(capA*sizeof(long long)); nA = 0; pushA(1);
    rec(3, NLIM, 1, 0);
    qsort(A, nA, sizeof(long long), cmp_ll);
    /* dedup (shouldn't be needed) */
    long long m = 0;
    for(long long i=0;i<nA;i++) if(i==0 || A[i]!=A[i-1]) A[m++]=A[i];
    nA = m;
    printf("\n=== 2. Cubefull numbers <= 1e9 : %lld ; C_3*N^(1/3) predicts %.1f ===\n",
           nA, Cr(3)*pow((double)NLIM, 1.0/3.0));

    /* ---- 3. support census: sums of <= 3 cubefull numbers <= NLIM ---- */
    uint64_t words = (uint64_t)(NLIM/64 + 2);
    uint64_t *bits = calloc(words, 8);
    if(!bits){ fprintf(stderr,"no memory\n"); return 1; }
    /* 1 and 2 summands */
    for(long long i=0;i<nA && A[i]<=NLIM;i++){
        bits[(uint64_t)A[i]>>6] |= 1ULL << (A[i]&63);
        for(long long j=i;j<nA;j++){
            long long s = A[i]+A[j];
            if(s>NLIM) break;
            bits[(uint64_t)s>>6] |= 1ULL << (s&63);
        }
    }
    /* 3 summands, i<=j<=k */
    for(long long i=0;i<nA && A[i]<=NLIM/3+2;i++){
        for(long long j=i;j<nA;j++){
            long long s2 = A[i]+A[j];
            if(s2 > NLIM) break;
            for(long long k=j;k<nA;k++){
                long long s = s2 + A[k];
                if(s > NLIM) break;
                bits[(uint64_t)s>>6] |= 1ULL << (s&63);
            }
        }
    }
    printf("\n=== 3. Census: sums of <= 3 cubefull numbers <= 1e9 ===\n");
    /* exception counts in dyadic windows */
    long long lo = 1, hi = NLIM;
    long long total_rep = 0, total_exc = 0;
    /* last exceptions (top 40) */
    {
        printf("window [x/2, x] : #exceptions / window size   (fraction)\n");
        long long w = hi;
        while(w >= 1000000){
            long long a = w/2 + 1, b = w;
            long long exc = 0;
            for(long long n=a;n<=b;n++) if(!(bits[(uint64_t)n>>6]>>(n&63)&1ULL)) exc++;
            printf("  (%lld, %lld] : %lld / %lld   (%.6f)\n", a-1, b, exc, b-a+1, (double)exc/(b-a+1));
            w /= 2;
        }
    }
    for(long long n=1;n<=NLIM;n++) if(bits[(uint64_t)n>>6]>>(n&63)&1ULL) total_rep++; else total_exc++;
    printf("TOTAL in [1,1e9]: represented %lld (%.6f), exceptions %lld (%.6f)\n",
           total_rep, (double)total_rep/NLIM, total_exc, (double)total_exc/NLIM);
    /* largest exceptions */
    printf("largest exceptions below 1e9:\n");
    {
        long long found = 0;
        for(long long n=NLIM; n>0 && found<40; n--){
            if(!(bits[(uint64_t)n>>6]>>(n&63)&1ULL)){ printf("%lld\n", n); found++; }
        }
    }
    /* exception count by residue class mod m, for m in {2,3,8,9,16,27}: in top window */
    for(int mm=2; mm<=32; mm *= 2){}
    {
        int mods[6] = {2,3,8,9,16,27};
        for(int t=0;t<6;t++){
            int mm = mods[t];
            printf("modulo %d: exceptions per class in (5e8,1e9]:\n  ", mm);
            for(int r=0;r<mm;r++){
                long long exc=0, tot=0;
                for(long long n=500000001 + r; n<=NLIM; n+=mm){
                    tot++;
                    if(!(bits[(uint64_t)n>>6]>>(n&63)&1ULL)) exc++;
                }
                printf("[%d]:%.4f ", r, tot? (double)exc/tot : 0);
            }
            printf("\n");
        }
    }
    free(bits);

    /* ---- 4. R(n) histogram and additive energy, ordered triples, n <= HLIM ---- */
    {
        long long H = HLIM;
        uint32_t *T = calloc(3*H+3, 4);
        if(!T){ fprintf(stderr,"no memory for T\n"); return 1; }
        /* enumerate ALL ordered triples a,b,c cubefull with sum <= 3H (we need T(n) for n<=H;
           any summand <= H suffices) */
        long long na = 0;
        while(na < nA && A[na] <= H) na++;
        fprintf(stderr, "cubefull <= %lld: %lld\n", H, na);
        for(long long i=0;i<na;i++)
            for(long long j=0;j<na && A[i]+A[j]<=H;j++){
                long long s2 = A[i]+A[j];
                long long room = H - s2;
                /* count c <= room among first na entries (A sorted) */
                long long kmax = (long long)(upper_bound_ll(A, na, room));
                for(long long k=0;k<kmax;k++) T[s2 + A[k]]++;
            }
        /* energy and stats over n <= H (windowed) */
        double sumR=0, sumR2=0; long long nz=0;
        for(long long n=1;n<=H;n++){ double t=T[n]; sumR+=t; sumR2+=t*t; if(t>0) nz++; }
        printf("\n=== 4. n <= %lld (summands 3-powerful <= n) ===\n", H);
        printf("sum R(n) = %.0f  (E[R] = %.4f; lambda_3 predicts %.2f)\n", sumR, sumR/H,
               pow(Cr(3),3)*pow(tgamma(4.0/3.0),3));
        printf("E = sum R(n)^2 = %.0f ; E/H = %.2f ; support %% = %.6f\n", sumR2, sumR2/H, (double)nz/H);
        /* Poisson comparison: P(R=0..6) */
        for(int k=0;k<=6;k++){
            long long c=0; for(long long n=1;n<=H;n++) if(T[n]==(uint32_t)k) c++;
            double lam = sumR/H;
            printf("  P(R=%d) = %.5f  Poisson(lam): %.5f\n", k, (double)c/H, pow(lam,k)*exp(-lam)/tgamma(k+1));
        }
        /* variance / mean : equidispersion test */
        double mean = sumR/H, var = sumR2/H - mean*mean;
        printf("Var(R)/mean = %.4f  (Poisson would give 1)\n", var/mean);
        /* top window energy scaling */
        free(T);
    }
    return 0;
}
