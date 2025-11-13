// Daniel.Soto - CosmologyAndGravitation_GravitationalWaves_LVK
// Contact: daniel.soto1@udea.edu.co

#include <stdio.h>

int main(void) {
    int t;
    scanf("%d", &t);
    
    for (int i = 0; i < t; i++) {
        int n;
        scanf("%d", &n);
        
        int h[n];
        for (int j = 0; j < n; j++) {
            scanf("%d", &h[j]);
        }
        
        int contador = 0;
        for (int j = 0; j < n; j++) {
            if (h[j] == 1) { contador++;
            }
        }
        
        printf("%d\n", n - contador / 2);
    }
    
    return 0;
}
