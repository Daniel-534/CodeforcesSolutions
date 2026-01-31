#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main() {
    long long n, k;
    scanf("%lld %lld", &n, &k);

    long long S = 0;
    for (long long i = 1; i <= n; i++) {
        S += gcd(i, k);
    }

    printf("%lld\n", S);
    return 0;
}
