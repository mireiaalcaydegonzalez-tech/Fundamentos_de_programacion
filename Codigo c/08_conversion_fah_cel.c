/*
*    CONVERSION FAH CEL
*/
#include <stdio.h>
#include <stdlib.h>

int main(){
    //Variables
    float celsius,fahr;
    int min,max,paso;


    //Inicializacion
    //Rango de temperaturas en grados Fahrenheit
    //min 0 max 300 paso 20
    min=0;
    max=300;
    paso=20;

    //Inicializacion variables
    fahr=min;
    celsius=min;

    //Bucle de conversion
    while(fahr<=max){
        celsius=5*(fahr-32)/9;
        printf("Conversion temp ºF:%.2f ºC:%.2f\n",fahr,celsius);
        fahr=fahr+paso;
    }


}