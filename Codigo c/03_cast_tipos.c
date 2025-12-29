#include <stdio.h>

// Funcion principal
int main() {
    //Declaración de variables
    int entero = 10;
    float flotante = 5.5f;
    char caracter = 'A';

    // Conversion implicita: de int a float
    float resultado_implicito = entero + flotante;
    printf("Resultado de la conversion implicita (int a float): %f\n", resultado_implicito);

    // Conversion de int a float
    flotante = (float)entero;
    printf("Conversion de int a float: %f\n", flotante);

    // Conversion de float a int
    int resultado_entero = (int)flotante + entero;
    p rintf("Conversion de float a int: %d\n", resultado_entero);

    // Conversion de char a int
    int ascii_valor = (int)caracter;
    printf("Conversion de char a int (valor ASCII): %d\n", ascii_valor);

    return 0;
}
