#include <stdio.h>
#include <stdlib.h>

int main(){

    float novo_preco, porcentagem;
    

    float preco = printf("Digite o preco: ");
    scanf("%f", &preco);

    if(preco <= 1000){
        porcentagem = 2.5;
        novo_preco = preco + ((preco * porcentagem) / 100);
    }else if(preco > 1000 && preco < 3500){
        porcentagem = 5;
        novo_preco = preco + ((preco * porcentagem) / 100);
    }else{  
        porcentagem = 5;
        novo_preco = preco + ((preco * porcentagem) / 100);
    }

    printf("O produto custara %.2f ja com o aumento de %.2f", novo_preco, porcentagem);
}