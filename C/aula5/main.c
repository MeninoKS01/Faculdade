#include <stdio.h>
#include <stdlib.h>

main (){

    float preco = printf("Digite o preco: ");
    scanf("%f", &preco);

    int porcentagem = printf("Digite o aumento em porcentagem: ");
    scanf("%i", &porcentagem);

    float novo_preco = preco + ((preco * porcentagem) / 100); 

    printf("O preco com o aumento e: R$ %.2f", novo_preco);

}