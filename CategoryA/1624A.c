#include <stdio.h>

int main(void) {
    int t;
    if (scanf("%d", &t) != 1) return 0;

    while (t--) {
        int n;
        scanf("%d", &n);

        int x, minimo, maximo;
        for (int i = 0; i < n; i++) {
            scanf("%d", &x);
            if (i == 0) { minimo = maximo = x; }
            else {
                if (x < minimo) minimo = x;
                if (x > maximo) maximo = x;
            }
        }
        printf("%d\n", maximo - minimo);
    }
    return 0;
}

