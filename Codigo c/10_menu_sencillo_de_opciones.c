#include <stdio.h>

int main() {
    int opcion;

    printf("Elige un color:\n");
    printf("1. Amarillo\n");
    printf("2. Naranja\n");
    printf("3. Azul\n");
    printf("Introduce el número de tu opción: ");
    scanf("%d", &opcion);

    if ( opcion < 1 || opcion > 3) {
        printf("Opción no válida\n");} 
        else {
        printf("Has elegido: ");
        switch(opcion) {
            case 1:
                printf("Amarillo\n");
                break;
            case 2:
                printf("Naranja\n");
                break;
            case 3:
                printf("Azul\n");
                break;
        }
    }

    return 0;
}