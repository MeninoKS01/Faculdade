"""
Fazendo aprovação de alunos com base na média.
"""

nome = input("Qual seu nome? ")
disciplina = input("Qual sua disciplina? ")
nota_ex = int(input("Digite sua nota em exercícios: "))
nota_port = int(input("Digite sua nota do portfólio: "))
nota_prova = int(input("Digite sua nota da prova: "))

media = nota_ex * 0.2 + nota_port * 0.3 + nota_prova * 0.5

print(f"O aluno {nome} na disciplina: {disciplina}, obteve a média {media}")

if media >= 6:
    print(f"O aluno {nome} está aprovado!")
else:
    print(f"O aluno {nome} está reprovado!")


