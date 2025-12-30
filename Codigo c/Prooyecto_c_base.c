/* ========================================
   JUEGO DE DADOS CONTRA LA MAQUINA
   Proyecto Fundamentos de Programacion
   ======================================== */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* ========== FUNCIONES ========== */

/**
 * Funcion: tirada_especial
 * Realiza la tirada especial cuando sale un 6
 * Aplica multiplicador o divisor (2 o 3) a los puntos acumulados
 * Parametros: puntos_acumulados - puntos que lleva el jugador
 * Retorna: los puntos modificados tras aplicar multiplicador/divisor
 */
int tirada_especial(int puntos_acumulados) {
    // Tirar dado multiplicador/divisor: 0=divisor, 1=multiplicador
    int operacion = rand() % 2;
    // Tirar moneda: 2 o 3
    int valor = (rand() % 2) + 2;
    
    printf("   --> Tirada especial: ");
    
    if (operacion == 1) {
        printf("MULTIPLICADOR x%d\n", valor);
        puntos_acumulados *= valor;
    } else {
        printf("DIVISOR /%d\n", valor);
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
int turno_jugador(int puntos_maquina) {
    int puntos_acumulados = 0;
    int continuar = 1;
    char enter;
    
    printf("\n========== TU TURNO ==========\n");
    
    while (continuar) {
        printf("\nPuntos acumulados en este turno: %d\n", puntos_acumulados);
        printf("Presiona ENTER para tirar el dado...");
        
        // Limpiar buffer y esperar ENTER
        while (getchar() != '\n');
        
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
            
            // Preguntar si quiere continuar
            printf("\n¿Quieres seguir tirando? (1=Si, 0=Plantarse): ");
            scanf("%d", &continuar);
            
            if (continuar == 0) {
                printf("   Te plantas con %d puntos acumulados.\n", puntos_acumulados);
            }
            
        } else if (dado == 6) {
            // Tirada especial
            printf("   ¡TIRADA ESPECIAL!\n");
            puntos_acumulados = tirada_especial(puntos_acumulados);
            printf("   Puntos tras tirada especial: %d\n", puntos_acumulados);
            
            // Preguntar si quiere continuar
            printf("\n¿Quieres seguir tirando? (1=Si, 0=Plantarse): ");
            scanf("%d", &continuar);
            
            if (continuar == 0) {
                printf("   Te plantas con %d puntos acumulados.\n", puntos_acumulados);
            }
        }
    }
    
    return puntos_acumulados;
}

/**
 * Funcion: turno_maquina
 * Gestiona el turno completo de la maquina
 * Estrategia: la maquina tira hasta conseguir 15 puntos o mas
 * Parametros: ninguno
 * Retorna: puntos que se restan al jugador en este turno
 */
int turno_maquina() {
    int puntos_acumulados = 0;
    int continuar = 1;
    
    printf("\n========== TURNO DE LA MAQUINA ==========\n");
    
    // Estrategia: la maquina tira hasta conseguir al menos 15 puntos
    while (continuar && puntos_acumulados < 15) {
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
            
        } else if (dado == 6) {
            // Tirada especial
            printf("   ¡TIRADA ESPECIAL DE LA MAQUINA!\n");
            puntos_acumulados = tirada_especial(puntos_acumulados);
            printf("   Puntos de la maquina tras tirada especial: %d\n", puntos_acumulados);
        }
        
        // Decidir si continua (estrategia: plantarse con 15 o mas puntos)
        if (puntos_acumulados >= 15) {
            printf("   La maquina decide plantarse con %d puntos.\n", puntos_acumulados);
            continuar = 0;
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
    getchar();
    
    // Bucle principal del juego
    while (puntos_jugador > 0 && puntos_maquina > 0) {
        
        // Mostrar puntuacion actual
        printf("\n\n+++++++++++++++++++++++++++++++++++++++++++\n");
        printf("  JUGADOR: %d puntos | MAQUINA: %d puntos\n", puntos_jugador, puntos_maquina);
        printf("+++++++++++++++++++++++++++++++++++++++++++\n");
        
        // TURNO DEL JUGADOR
        int danio_jugador = turno_jugador(puntos_maquina);
        
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
        
        printf("\nPresiona ENTER para el turno de la maquina...");
        while (getchar() != '\n');
        
        // TURNO DE LA MAQUINA
        int danio_maquina = turno_maquina();
        
        if (danio_maquina > 0) {
            puntos_jugador -= danio_maquina;
            if (puntos_jugador < 0) puntos_jugador = 0;
            printf("\n>>> La maquina te resta %d puntos! <<<\n", danio_maquina);
            printf("    Tus puntos: %d\n", puntos_jugador);
        }
    }
    
    // MOSTRAR RESULTADO FINAL
    printf("\n\n");
    printf("=============================================\n");
    printf("            FIN DEL JUEGO                   \n");
    printf("=============================================\n");
    printf("  JUGADOR: %d puntos | MAQUINA: %d puntos\n", puntos_jugador, puntos_maquina);
    printf("---------------------------------------------\n");
    
    if (puntos_jugador > 0) {
        printf("         ¡¡¡ GANASTE !!!\n");
    } else {
        printf("         PERDISTE - Gana la maquina\n");
    }
    
    printf("=============================================\n\n");
    
    return 0;
}
