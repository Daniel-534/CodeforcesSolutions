#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n, k, x;
        scanf("%d %d %d", &n, &k, &x);

        if (x != 1) {
            printf("YES\n");
            printf("%d\n", n);
            for (int i = 0; i < n; i++) {
                printf("1");
                if (i < n - 1) printf(" ");
            }
            printf("\n");
        } else {
            if (k == 1) {
                printf("NO\n");
            } else if (k == 2) {
                if (n % 2 == 0) {
                    printf("YES\n");
                    printf("%d\n", n / 2);
                    for (int i = 0; i < n / 2; i++) {
                        printf("2");
                        if (i < n / 2 - 1) printf(" ");
                    }
                    printf("\n");
                } else {
                    printf("NO\n");
                }
            } else { // k >= 3
                if (n % 2 == 0) {
                    printf("YES\n");
                    printf("%d\n", n / 2);
                    for (int i = 0; i < n / 2; i++) {
                        printf("2");
                        if (i < n / 2 - 1) printf(" ");
                    }
                    printf("\n");
                } else {
                    printf("YES\n");
                    printf("%d\n", n / 2);
                    printf("3");
                    if ((n - 3) / 2 > 0) printf(" ");
                    for (int i = 0; i < (n - 3) / 2; i++) {
                        printf("2");
                        if (i < (n - 3) / 2 - 1) printf(" ");
                    }
                    printf("\n");
                }
            }
        }
    }

    return 0;
}

