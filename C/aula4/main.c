#include <stdio.h>
#include <stdlib.h>

/*
Permite que o usuario entre com numero e mostre se
o numero é negativo, neutro ou positivo
*/

int main(){

    float n1, n2, media;

    printf("Digite um valor n1: ");
    scanf("%f", &n1);

    printf("Digite o valor n2: ");
    scanf("%f", &n2);

    media = (n1 + n2)/2;
    printf("Media: %.2f", media);
    
    system("pause");
    return 0;
}
