print("----------------------------------------------------------------------------")
print("|                           MÉDIA PONDERADA                                |")
print("----------------------------------------------------------------------------")

nome_aluno = input("Qual o seu nome? ")
disciplina = input("Qual a sua disciplina? ")
nota_exercicio = float(input("Sua nota em exercícios: "))
nota_portifolio = float(input("Sua nota no Portifólio: "))
nota_prova = float(input("Sua nota na prova: "))

media = nota_exercicio * 0.2 + nota_portifolio * 0.3 + nota_prova * 0.5

print(f"O aluno {nome_aluno} obteve a média {media} na disciplina: {disciplina}")






