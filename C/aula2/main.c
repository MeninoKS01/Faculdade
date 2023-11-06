#include <stdio.h>
#include <stdlib.h>

main()
{
    printf("AULA2 \n");

        int valor1;
        int valor2;
        int valor3;
        int valor4;
        int valor5;

        printf("Digite um valor: ");
        scanf("%i",&valor1);

        printf("Digite um valor: ");
        scanf("%i",&valor2);

        printf("Digite um valor: ");
        scanf("%i",&valor3);

        printf("Digite um valor: ");
        scanf("%i",&valor4);

        printf("Digite um valor: ");
        scanf("%i",&valor5);

        int total;
        total = valor1 + valor2 + valor3 + valor4 + valor5;

    printf("A soma dos valores: %i \n" , total);

    system("pause");
}