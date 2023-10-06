"""
Diferenciando menor e maiores de idade (com sexo)
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = input("Digite f - Feminino m - Masculino ")

if (idade >= 18):
    if (sexo =="f"):
        print(f"{nome} é uma mulher maior de idade")
    elif (sexo =="m"):
        print(f"{nome} é um homem maior de idade")
    else:
        print("Sexo inválido")
else:
    if (sexo == "f"):
        print(f"{nome} é uma garota menor de idade")
    elif (sexo =="m"):
        print(f"{nome} é um garoto menor de idade")
    else:
        print("Sexo inválido")

print("Fim do Programa!")
