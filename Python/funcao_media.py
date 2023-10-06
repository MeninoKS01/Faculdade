"""
Calcular a média ponderada do Centro Universário Eniac

Declarar funções trabalhar com funções trazendo retorno de valores
Estruturar o programa
"""

#Função de calcular a média

def calcular_media(exer, port, prov):
    media= exer*0.20 + port*0.30 + prov*0.50
    return media

# Função de Mensagens: Aprovado ou Reprovado

def mensagem_aprovado(nota_media, aluno):
    print(f"{aluno} está aprovado!!")

def mensagem_reprovado(nota_media, aluno):
    print(f"{aluno} está reprovado!!")

# Programa principal

continua=True
while (continua):

    # Entrada de dados

    aluno=input("Digite seu nome: ")
    exer=float(input("Digite a nota do exercício: "))
    port=float(input("Digite a nota do portifólio: "))
    prov=float(input("Digite a nota da prova: "))

    # Chamar a função de cálculo da média

    nota_media = calcular_media(exer, port, prov)

    #Resultado
    
    if nota_media >= 6:
        mensagem_aprovado(nota_media, aluno)
    else:
        mensagem_reprovado(nota_media, aluno)






