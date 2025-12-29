// Genera una temperatura aleatoria y muestra un mensaje según el rango usando switch
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	// Semilla del generador de números aleatorios
	srand((unsigned)time(NULL));

	// Temperatura entre 0 y 45 (ambos inclusive)
	int temp = rand() % 46;

	printf("Temperatura generada: %d\n", temp);

	switch (temp) {
		case 0: case 1: case 2: case 3: case 4:
		case 5: case 6: case 7: case 8: case 9: case 10:
			printf("Hace mucho frío\n");
			break;
		case 11: case 12: case 13: case 14: case 15:
		case 16: case 17: case 18: case 19: case 20:
			printf("Hace fresquito\n");
			break;
		case 21: case 22: case 23: case 24: case 25:
		case 26: case 27: case 28: case 29: case 30:
			printf("No se está mal\n");
			break;
		case 31: case 32: case 33: case 34: case 35:
		case 36: case 37: case 38: case 39: case 40:
			printf("Comienza a hacer calor\n");
			break;
		default:
			// Incluye 41-45, y el caso teórico de valores mayores de 45
			printf("Muero achicharrado\n");
			break;
	}

	return 0;
}
