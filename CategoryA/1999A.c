// Daniel.Soto - CosmologyAndGravitation_GravitationalWaves_LVK
// Contact: daniel.soto1@udea.edu.co

#include <stdio.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);
    
    for (int i = 0; i < t; i++) {
        char n[101];
        scanf("%s", n);
        
        int suma = 0;
        for (int j = 0; n[j] != '\0'; j++) { 
											  
            suma += n[j] - '0';	
        }
        printf("%d\n", suma);
    }
    
    return 0;
}
