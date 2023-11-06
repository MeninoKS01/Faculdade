#include <stdio.h>
#include <stdlib.h>

int main(){

    float preco;
    int comida_kg;

    //Painel de opções
    printf("Animais do Zoo \n");
    printf("1- Coala \n");
    printf("2- Macaco Prego\n");
    printf("3- Cobra \n");
    printf("4- Flamingo \n");
    printf("5- Girafa \n");
    
    //Escolha do animal
    int opcao = printf("Escolha uma opcao(1-5): ");
    scanf("%i",&opcao);

    //Escolha quantidade de animais da especie
    int qtd_animais_especie = printf("Digite a Quantidade de Animais da Especie: ");
    scanf("%i", &qtd_animais_especie);

    if(opcao == 1){
        //Armazenar preço e quilo do Coala
        comida_kg = 2;
        preco = 122.31;
    } else if (opcao == 2){
        //Armazenar preço e quilo do Macado Prego
        comida_kg = 2;
        preco = 176.48;
    } else if (opcao == 3){
        //Armazenar preço e quilo da Cobra
        comida_kg = 1;
        preco = 80.7;
    } else if (opcao == 4){
        //Armazenar preço e quilo do Flamingo
        comida_kg = 3;
        preco = 204.86;
    } else if (opcao == 5){
        //Armazenar preço e quilo da Girafa
        comida_kg = 3;
        preco = 236.90;
    }

    //Cálculo de preço e quilo
    int qtd_comida_dia = comida_kg * qtd_animais_especie;
    int qtd_comida_mes = qtd_comida_dia * 30;
    float preco_mes = qtd_comida_mes * preco;

    //Todos os resultado
    printf("\n Resultado: ");
    printf("\n Qtde Comida ao dia: %i", qtd_comida_dia);
    printf("\n Qtde Comida ao mes: %i", qtd_comida_mes);
    printf("\n Custo Mensal: %.2f", preco_mes);
    

}