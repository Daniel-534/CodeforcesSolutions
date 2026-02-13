#include <stdio.h>
#include <stdlib.h>

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        long long c = llabs(a - b);
        long long ans = c / 5 + (c % 5 + 1) / 2;
        printf("%lld\n", ans);
    }
    return 0;
}
