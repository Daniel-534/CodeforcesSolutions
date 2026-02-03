#include <stdio.h>
#include <math.h>

int main() {
    int x;
    scanf("%d", &x);
    for (int i=2; i <= (int)sqrt(x); i++) {
        if (x %i == 0) {
            printf("%d\n", i);
            return 0;
        }
    }
    return 0;
}
