#include <stdio.h>
#include <stdlib.h>

/*
Permite que o usuario entre com numero e mostre se
o numero é negativo, neutro ou positivo
*/

int main(){

    int numero;
    printf("Digite um numero: ");
    scanf( "%i", &numero);

    if (numero == 0){
        printf("O numero %d e neutro \n", numero);
    } else if (numero > 0) {
        printf("O numero %d e positivo \n", numero);
    } else if (numero < 0){
        printf("O numero %d e negativo \n", numero);
    }
    
    system("pause");
    return 0;
}
