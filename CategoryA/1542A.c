#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        int pares = 0, impares = 0;
        int x;

        for (int i = 0; i < 2 * n; i++) {
            scanf("%d", &x);
            if (x % 2 == 0) {pares++;
            } 
			else {impares++;
            }
        }
        if (pares == n && impares == n) {printf("Yes\n");
        } 
		else {printf("No\n");
        }
    }
    return 0;
}

