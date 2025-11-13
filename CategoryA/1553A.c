#include <stdio.h>

// como n va hasta 1e9, entonces utilizo long long
int main(void) {
    int t;
    if (scanf("%d", &t) != 1) return 0;

    while (t--) {
        long long n;
        scanf("%lld", &n);
        long long ans = (n + 1) / 10;
        printf("%lld\n", ans);
    }
    return 0;
}

