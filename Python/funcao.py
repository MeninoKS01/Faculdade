"""
Função: estruturação do programa
"""

#Criar função

def calcula_media():

    continua=True
    while(continua):
        import os
        os.system('cls')

        nome=input('Digite o nome do aluno: ')
        disciplina=input('Digite a disciplina: ')

        ex=float(input('Digite a nota do exercício entre 0 e 10: '))
        while(ex < 0 or ex > 10):
            ex=float(input('\n nota inválida !! \n digite a nota entre 0 e 10: '))
        pt=float(input('Digite a nota do portfólio(entre 0 e 10: '))
        while(pt < 0 or pt > 10):
            pt=float(input('\n nota inválida !! \n digite a nota entre 0 e 10: '))
        pr=float(input('Digite a nota da prova entre 0 e 10: '))
        while(pr < 0 or pr > 10):
            pr=float(input('\n nota inválida !! \n digite a nota entre 0 e 10: '))

        mf=(ex*20 + pt*30 + pr*50)/100

        print(f'\nO aluno {nome} na disciplina {disciplina} obteve a média {mf} \n')
        if mf>=6:
            print(' O aluno está aprovado\n\n')
        else:
            print(' o aluno está reprovado\n\n')

        opcao=input('Deseja continuar (S ou N): ')
        while(opcao.upper()!= 'S' and opcao.upper()!= 'N'):
            opcao=input('\nOpção inválida !! \n\n Digite (S ou N)')
        if opcao.upper()== 'S':
            continua=True
        else:
            continua=False
    print('\n\n\nFim do Programa !!')
    os.system('cls')

calcula_media()