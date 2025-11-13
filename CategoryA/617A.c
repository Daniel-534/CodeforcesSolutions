#include <stdio.h>

int main() {
    int n, respuesta;
    scanf("%d", &n);

    if (n % 5 == 0) {
        respuesta = n / 5;
    } 
	else {
        respuesta = n / 5 + 1;
    }
    
	printf("%d\n", respuesta);
    return 0;
}

