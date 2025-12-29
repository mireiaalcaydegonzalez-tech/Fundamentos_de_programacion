// Incluimos la biblioteca estándar de entrada y salida
#include <stdio.h>
// Funcion principal
int main(void) {
    // Definición de variables de diferentes tipos
    int entero = 10;            // Variable entera  
    float flotante = 5.5f;      // Variable de punto flotante
    double doble = 9.99;        // Variable de doble precisión
    char caracter = 'A';        // Variable de carácter

    // Definir edad sin inicializar
    int edad;
    edad = 25; // Asignar valor a la variable edad

    // Imprimir los valores de las variables
    printf("Entero: %d\n", entero);
    printf("Flotante: %.2f\n", flotante);
    printf("Doble: %.2lf\n", doble);
    printf("Caracter: %c\n", caracter);

    printf("Edad: %d\n", edad);

    // Retornar 0 para indicar que el programa terminó correctamente
    return 0;
} 