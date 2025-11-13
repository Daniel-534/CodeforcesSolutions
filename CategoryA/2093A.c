#include <stdio.h>

int main() {
    int n, k;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &k);   
        if (k % 2 != 0) {
            printf("YES\n");
        } 
		else {
            printf("NO\n");
        }
    }

    return 0;
}

