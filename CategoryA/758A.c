// Daniel.Soto - CosmologyAndGravitation_GravitationalWaves_LVK
// Contact: daniel.soto1@udea.edu.co

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    
    int maximo = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > maximo) {
            maximo = a[i];
        }
    }
    
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += maximo - a[i];
    }
    
    printf("%d\n", total);
    
    return 0;
}
