/* ========================================
   JUEGO DE DADOS CONTRA LA MAQUINA
   Proyecto Fundamentos de Programacion
   ======================================== */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* ========== FUNCIONES ========== */

/**
 * Funcion: limpiar_buffer
 * Limpia el buffer de entrada evitando errores por caracteres residuales
 */
void limpiar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

/**
 * Funcion: tirada_especial
 * Realiza la tirada especial cuando sale un 6
 * El usuario participa presionando ENTER para revelar multiplicador/divisor y el valor (2 o 3)
 * Parametros: puntos_acumulados - puntos que lleva el jugador
 * Retorna: los puntos modificados tras aplicar multiplicador/divisor
 */
int tirada_especial(int puntos_acumulados, int es_jugador) {
    // Tirar dado multiplicador/divisor: 0=divisor, 1=multiplicador
    int operacion = rand() % 2;
    // Tirar moneda: 2 o 3
    int valor = (rand() % 2) + 2;
    
    if (es_jugador) {
        printf("   --> Presiona ENTER para revelar si es MULTIPLICADOR o DIVISOR...");
        limpiar_buffer();
    }
    
    printf("   --> Tirada especial: ");
    
    if (operacion == 1) {
        printf("MULTIPLICADOR\n");
        if (es_jugador) {
            printf("   --> Presiona ENTER para revelar el valor (2 o 3)...");
            limpiar_buffer();
        }
        printf("   --> El multiplicador es: x%d\n", valor);
        puntos_acumulados *= valor;
    } else {
        printf("DIVISOR\n");
        if (es_jugador) {
            printf("   --> Presiona ENTER para revelar el valor (2 o 3)...");
            limpiar_buffer();
        }
        printf("   --> El divisor es: /%d\n", valor);
        puntos_acumulados /= valor; // Division entera (redondeo automatico)
    }
    
    return puntos_acumulados;
}

/**
 * Funcion: turno_jugador
 * Gestiona el turno completo del jugador humano
 * Parametros: puntos_maquina - puntos actuales de la maquina (por referencia)
 * Retorna: puntos que se restan a la maquina en este turno
 */
int turno_jugador(int *puntos_jugador, int *puntos_maquina) {
    int puntos_acumulados = 0;
    int continuar = 1;
    int entrada_valida;
    int opcion;
    
    printf("\n========== TU TURNO ==========\n");
    
    while (continuar) {
        printf("\nPuntos acumulados en este turno: %d\n", puntos_acumulados);
        printf("Presiona ENTER para tirar el dado...");
        
        // Limpiar buffer y esperar ENTER
        limpiar_buffer();
        
        // Tirar dado de 6 caras
        int dado = (rand() % 6) + 1;
        printf("   [DADO] Has sacado un: %d\n", dado);
        
        if (dado == 1) {
            // Pierde turno y puntos acumulados
            printf("   ¡OH NO! Has sacado 1. Pierdes el turno y los %d puntos acumulados.\n", puntos_acumulados);
            puntos_acumulados = 0;
            continuar = 0;
            
        } else if (dado >= 2 && dado <= 5) {
            // Acumular puntos
            puntos_acumulados += dado;
            printf("   Sumas %d puntos. Total acumulado: %d\n", dado, puntos_acumulados);
            
            // Preguntar si quiere continuar con validacion de entrada
            entrada_valida = 0;
            while (!entrada_valida) {
                printf("\n¿Quieres seguir tirando?\n");
                printf("   1 = Si, continuar tirando\n");
                printf("   0 = Plantarse y terminar turno\n");
                printf("   2 = Salir del juego\n");
                printf("Elige una opcion: ");
                if (scanf("%d", &opcion) == 1) {
                    if (opcion == 0 || opcion == 1 || opcion == 2) {
                        entrada_valida = 1;
                    } else {
                        printf("   ERROR: Ingresa solo 0, 1 o 2\n");
                        limpiar_buffer();
                    }
                } else {
                    printf("   ERROR: Debes ingresar un numero\n");
                    limpiar_buffer();
                }
            }
            
            if (opcion == 0) {
                printf("   Te plantas con %d puntos acumulados.\n", puntos_acumulados);
                continuar = 0;
            } else if (opcion == 2) {
                printf("   ¡Has decidido salir del juego!\n");
                // Restar los puntos acumulados antes de salir
                *puntos_maquina -= puntos_acumulados;
                if (*puntos_maquina < 0) *puntos_maquina = 0;
                *puntos_jugador = -1; // Marca para salida sin perder
                continuar = 0;
            }
            // Si opcion == 1, continua el bucle
            
        } else if (dado == 6) {
            // Tirada especial
            printf("   ¡TIRADA ESPECIAL!\n");
            puntos_acumulados = tirada_especial(puntos_acumulados, 1); // 1 = es jugador
            printf("   Puntos tras tirada especial: %d\n", puntos_acumulados);
            
            // Preguntar si quiere continuar con validacion de entrada
            entrada_valida = 0;
            while (!entrada_valida) {
                printf("\n¿Quieres seguir tirando?\n");
                printf("   1 = Si, continuar tirando\n");
                printf("   0 = Plantarse y terminar turno\n");
                printf("   2 = Salir del juego\n");
                printf("Elige una opcion: ");
                if (scanf("%d", &opcion) == 1) {
                    if (opcion == 0 || opcion == 1 || opcion == 2) {
                        entrada_valida = 1;
                    } else {
                        printf("   ERROR: Ingresa solo 0, 1 o 2\n");
                        limpiar_buffer();
                    }
                } else {
                    printf("   ERROR: Debes ingresar un numero\n");
                    limpiar_buffer();
                }
            }
            
            if (opcion == 0) {
                printf("   Te plantas con %d puntos acumulados.\n", puntos_acumulados);
                continuar = 0;
            } else if (opcion == 2) {
                printf("   ¡Has decidido salir del juego!\n");
                // Restar los puntos acumulados antes de salir
                *puntos_maquina -= puntos_acumulados;
                if (*puntos_maquina < 0) *puntos_maquina = 0;
                *puntos_jugador = -1; // Marca para salida sin perder
                continuar = 0;
            }
            // Si opcion == 1, continua el bucle
        }
    }
    
    return puntos_acumulados;
}

/**
 * Funcion: turno_maquina
 * Gestiona el turno completo de la maquina
 * Estrategia: la maquina decide aleatoriamente si continuar o plantarse
 * Parametros: ninguno
 * Retorna: puntos que se restan al jugador en este turno
 */
int turno_maquina() {
    int puntos_acumulados = 0;
    int continuar = 1;
    int decision; // 0 = plantarse, 1 = continuar
    
    printf("\n========== TURNO DE LA MAQUINA ==========\n");
    
    while (continuar) {
        printf("\nLa maquina tira el dado...\n");
        
        // Tirar dado de 6 caras
        int dado = (rand() % 6) + 1;
        printf("   [DADO] La maquina saca un: %d\n", dado);
        
        if (dado == 1) {
            // Pierde turno y puntos acumulados
            printf("   ¡La maquina saca 1! Pierde el turno y los %d puntos acumulados.\n", puntos_acumulados);
            puntos_acumulados = 0;
            continuar = 0;
            
        } else if (dado >= 2 && dado <= 5) {
            // Acumular puntos
            puntos_acumulados += dado;
            printf("   La maquina suma %d puntos. Total acumulado: %d\n", dado, puntos_acumulados);
            
            // La maquina decide aleatoriamente si continua o se planta
            decision = rand() % 2; // 0 o 1
            if (decision == 0) {
                printf("   La maquina decide plantarse con %d puntos acumulados.\n", puntos_acumulados);
                continuar = 0;
            } else {
                printf("   La maquina decide continuar tirando.\n");
            }
            
        } else if (dado == 6) {
            // Tirada especial
            printf("   ¡TIRADA ESPECIAL DE LA MAQUINA!\n");
            puntos_acumulados = tirada_especial(puntos_acumulados, 0); // 0 = es maquina
            printf("   Puntos de la maquina tras tirada especial: %d\n", puntos_acumulados);
            
            // La maquina decide aleatoriamente si continua o se planta
            decision = rand() % 2; // 0 o 1
            if (decision == 0) {
                printf("   La maquina decide plantarse con %d puntos acumulados.\n", puntos_acumulados);
                continuar = 0;
            } else {
                printf("   La maquina decide continuar tirando.\n");
            }
        }
    }
    
    return puntos_acumulados;
}


/* ========== PROGRAMA PRINCIPAL ========== */

int main(void) {
    // Inicializar generador de numeros aleatorios
    srand((unsigned)time(NULL));
    
    // Puntuacion inicial de ambos jugadores
    int puntos_jugador = 100;
    int puntos_maquina = 100;
    
    // Presentacion del juego
    printf("\n");
    printf("=============================================\n");
    printf("     JUEGO DE DADOS CONTRA LA MAQUINA      \n");
    printf("=============================================\n");
    printf("\nREGLAS:\n");
    printf("- Cada jugador comienza con 100 puntos\n");
    printf("- En cada tirada se lanza un dado de 6 caras:\n");
    printf("  * 2-5: Acumulas esos puntos\n");
    printf("  * 1: Pierdes turno y puntos acumulados\n");
    printf("  * 6: Tirada especial (multiplicador o divisor)\n");
    printf("- Los puntos acumulados se restan al oponente\n");
    printf("- Gana quien hace llegar a 0 al contrario\n");
    printf("=============================================\n");
    
    printf("\nPresiona ENTER para comenzar...");
    limpiar_buffer();
    
    // Bucle principal del juego
    while (puntos_jugador > 0 && puntos_maquina > 0) {
        
        // Mostrar puntuacion actual
        printf("\n\n+++++++++++++++++++++++++++++++++++++++++++\n");
        printf("  JUGADOR: %d puntos | MAQUINA: %d puntos\n", puntos_jugador, puntos_maquina);
        printf("+++++++++++++++++++++++++++++++++++++++++++\n");
        
        // TURNO DEL JUGADOR
        int danio_jugador = turno_jugador(&puntos_jugador, &puntos_maquina);
        
        if (danio_jugador > 0) {
            puntos_maquina -= danio_jugador;
            if (puntos_maquina < 0) puntos_maquina = 0;
            printf("\n>>> Le restas %d puntos a la maquina! <<<\n", danio_jugador);
            printf("    Puntos de la maquina: %d\n", puntos_maquina);
        }
        
        // Verificar si el jugador ha ganado
        if (puntos_maquina <= 0) {
            break;
        }
        
        // Verificar si el jugador decidio salir
        if (puntos_jugador <= 0) {
            break;
        }
        
        // TURNO DE LA MAQUINA
        int danio_maquina = turno_maquina();
        
        if (danio_maquina > 0) {
            puntos_jugador -= danio_maquina;
            if (puntos_jugador < 0) puntos_jugador = 0;
            printf("\n>>> La maquina te resta %d puntos! <<<\n", danio_maquina);
            printf("    Tus puntos: %d\n", puntos_jugador);
        }
        
        // Verificar si la maquina ha ganado
        if (puntos_jugador <= 0) {
            break;
        }
        
        // Esperar ENTER antes del siguiente turno del jugador
        printf("\nPresiona ENTER para tu siguiente turno...");
        limpiar_buffer();
    }
    
    // MOSTRAR RESULTADO FINAL
    printf("\n\n");
    printf("=============================================\n");
    printf("            FIN DEL JUEGO                   \n");
    printf("=============================================\n");
    printf("  JUGADOR: %d puntos | MAQUINA: %d puntos\n", puntos_jugador, puntos_maquina);
    printf("---------------------------------------------\n");
    
    if (puntos_jugador > 0 && puntos_maquina > 0) {
        printf("         ¡¡¡ SALISTE DEL JUEGO !!!\n");
    } else if (puntos_jugador > 0) {
        printf("         ¡¡¡ GANASTE !!!\n");
    } else {
        printf("         PERDISTE - Gana la maquina\n");
    }
    
    printf("=============================================\n\n");
    
    return 0;
}
