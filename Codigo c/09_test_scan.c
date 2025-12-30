/*EJEMPLO DE SCANF*/
#include <stdio.h>

/*Programa que lee varios tipos de datos usando scanf*/
int main(void) {
    int entero;
    float flotante;
    char caracter;
    char cadena[50];
    // Solicitar y leer un numero entero
    printf("Introduce un numero entero: ");
    scanf("%d", &entero);

    // Solicitar y leer un numero flotante
    printf("Introduce un numero flotante: ");
    scanf("%f", &flotante);

    // Solicitar y leer un caracter 
    printf("Introduce un caracter: ");
    scanf(" %c", &caracter); // Espacio antes de %c para consumir cualquier espacio en blanco previo

    // Solicitar y leer una cadena de texto
    printf("Introduce una cadena de texto: ");
    scanf("%s", cadena); // Limitar la entrada a 49 caracteres para evitar

    // Mostrar los datos leidos
     printf("--------------------\n");
    printf("\nDatos introducidos:\n");  
    printf("Numero entero: %d\n", entero);
    printf("Numero flotante: %.2f\n", flotante);
    printf("Caracter: %c\n", caracter);
    printf("Cadena de texto: %s\n", cadena);

    return 0;
}