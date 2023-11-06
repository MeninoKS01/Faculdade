#include <stdio.h>
#include <stdlib.h>

int main(){
    
	int diaSemana ;
	printf("Digite o dia da semana: ") ;
	scanf("%d" , &diaSemana ) ;
	
	switch( diaSemana ) {
		case 2 :
		printf("Segunda-feira") ;
		break ;
		case 3 :
		printf("Terca-feira") ;
		break ;
        case 4 :
		printf("Quarta-feira") ;
		break ;
		case 5 :
		printf("Quinta-feira") ;
		break ;
		case 6 :
		printf("Sexta-feira") ;
		break ;
        case 7 :
		printf("Sabado") ;
		break ;		
		case 1 :
		printf("Domingo") ;
		break ;	
		default : 
		printf("Dia incorreto") ;
	}

}
