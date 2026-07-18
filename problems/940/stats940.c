/* stats940.c — second-stage computations
 *  (a) multiset R~(n) histogram to 3e7 with dyadic-window energy E/|w|, support, mean R~;
 *      per-class (mod 8, mod 9) mean R~ in the top window.
 *  (b) support census to 4e9 with dyadic exception fractions.
 * Compile: gcc -O3 -march=native -o stats940 stats940.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

#define NLIM 4000000000LL
#define HLIM 30000000LL
#define PMAX 3000000

static int *primes, nprimes;
static void sieve_primes(void){
    char *c = calloc(PMAX+1,1);
    for(long long i=2;i<=PMAX;i++) if(!c[i]) for(long long j=i*i;j<=PMAX;j+=i) c[j]=1;
    nprimes=0; for(long long i=2;i<=PMAX;i++) if(!c[i]) nprimes++;
    primes=malloc((nprimes+1)*sizeof(int));
    long long k=0; for(long long i=2;i<=PMAX;i++) if(!c[i]) primes[k++]=i; primes[k]=0;
    free(c);
}
static long long *A; static long long nA, capA;
static void pushA(long long v){ if(nA==capA){ capA*=2; A=realloc(A,capA*sizeof(long long)); } A[nA++]=v; }
static void rec(int r, long long N, long long v, int start){
    for(int i=start; primes[i]; i++){
        long long p = primes[i];
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

int main(void){
    sieve_primes();
    capA = 1<<20; A = malloc(capA*sizeof(long long)); nA = 0; pushA(1);
    rec(3, NLIM, 1, 0);
    qsort(A, nA, sizeof(long long), cmp_ll);
    long long m = 0;
    for(long long i=0;i<nA;i++) if(i==0 || A[i]!=A[i-1]) A[m++]=A[i];
    nA = m;
    printf("cubefull <= 4e9 : %lld   ( /4e9^(1/3) = %.4f )\n\n", nA, nA/pow(4e9,1.0/3.0));

    /* ---------- (a) multiset histogram to HLIM ---------- */
    long long na = 0; while(na < nA && A[na] <= HLIM) na++;
    uint32_t *T = calloc(3*HLIM+3, 4);
    if(!T){ fprintf(stderr,"mem T\n"); return 1; }
    for(long long i=0;i<na;i++)
        for(long long j=i;j<na && A[i]+A[j]<=HLIM;j++){
            long long s2 = A[i]+A[j];
            for(long long k=j;k<na;k++){
                long long s = s2 + A[k];
                if(s > HLIM) break;
                if(s >= 1) T[s]++;
            }
        }
    printf("=== (a) multiset counting, windows to %lld ===\n", HLIM);
    printf("%12s %12s %10s %8s %10s %10s\n","w_lo","w_hi","meanR","P(R=0)","E/|w|","supp%");
    long long edges[] = {0, 100000, 1000000, 3000000, 10000000, HLIM, 0};
    for(int t=0;edges[t+1];t++){
        long long a = edges[t]+1, b = edges[t+1];
        double sr=0, sr2=0; long long nz=0, n0=0;
        for(long long n=a;n<=b;n++){ double v=T[n]; sr+=v; sr2+=v*v; if(v>0){nz++;} else n0++; }
        double len = b-a+1;
        printf("%12lld %12lld %10.4f %10.6f %10.2f %10.6f\n",
               a-1, b, sr/len, n0/len, sr2/len, nz/len);
    }
    /* per-class mean R in top window [HLIM/2, HLIM] : mod 8 and mod 9 */
    for(int mm=8; mm<=9; mm++){
        printf("modulo %d: mean R~(n) per class in (%lld, %lld]:\n  ", mm, HLIM/2, HLIM);
        for(int r=0;r<mm;r++){
            double s=0; long long t=0;
            for(long long n=HLIM/2+1+r;n<=HLIM;n+=mm){ s+=T[n]; t++; }
            printf("[%d]:%.2f ", r, s/t);
        }
        printf("\n");
    }
    /* P(R~=0 | odd classes) sanity */
    free(T);

    /* ---------- (b) census to NLIM=4e9 ---------- */
    uint64_t words = (uint64_t)(NLIM/64 + 2);
    uint64_t *bits = calloc(words, 8);
    if(!bits){ fprintf(stderr,"mem bits\n"); return 1; }
    for(long long i=0;i<nA && A[i]<=NLIM;i++){
        bits[(uint64_t)A[i]>>6] |= 1ULL << (A[i]&63);
        for(long long j=i;j<nA;j++){
            long long s = A[i]+A[j];
            if(s>NLIM) break;
            bits[(uint64_t)s>>6] |= 1ULL << (s&63);
        }
    }
    double t0 = 0;
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
    (void)t0;
    printf("\n=== (b) census to 4e9 ===\n");
    long long w = NLIM;
    while(w >= 500000000){
        long long a = w/2 + 1, b = w;
        long long exc = 0;
        for(long long n=a;n<=b;n++) if(!(bits[(uint64_t)n>>6]>>(n&63)&1ULL)) exc++;
        printf("  (%lld, %lld] : exc %lld  (%.6f)\n", a-1, b, exc, (double)exc/(b-a+1));
        w /= 2;
    }
    /* top-window class stats mod 16 (to check the mod-8 class 7 phenomenon at 2e9..4e9) */
    printf("modulo 16, exceptions fraction in (2e9, 4e9]:\n  ");
    for(int r=0;r<16;r++){
        long long exc=0, tot=0;
        for(long long n=2000000001LL + r; n<=NLIM; n+=16){
            tot++;
            if(!(bits[(uint64_t)n>>6]>>(n&63)&1ULL)) exc++;
        }
        printf("[%d]:%.5f ", r, (double)exc/tot);
    }
    printf("\n");
    free(bits);
    return 0;
}
