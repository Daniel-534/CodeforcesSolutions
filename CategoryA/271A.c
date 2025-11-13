#include <stdio.h>

int numeros_diferentes(int year) {
    int digito; // Almacena cada digito del anho
    int usados = 0; // Registro de digitos

    while (year > 0) {
        digito = year % 10; // Ultimo digito del anho

        // Verificamos si ese dígito ya fue visto
        if (usados & (1 << digito)) {
            // Si ya estaba, retornamos 0 (no todos los dígitos son distintos)
            return 0;
        }

        usados |= (1 << digito); // Marcamos el dígito como visto

        year /= 10; // Eliminamos el ultimo dígito y seguimos con el siguiente

    }

    // Si llegamos aquí, todos los dígitos son distintos
    return 1;
}

int main() {
    int y; // Variable de anho
    scanf("%d", &y); // \ingreso de anho

    int contador = y + 1; // Variable para buscar el proximo anho con digitos distintos

    // Repetimos hasta encontrar un año válido
    while (!numeros_diferentes(contador)) { // Si el anho no es valido, incrementamos en 1

        contador++;
    }

    // Imprimimos el anho que cumple la condicion
    printf("%d\n", contador);

    return 0;
}

