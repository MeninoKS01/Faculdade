"""
Diferenciando qual é o maior número.
"""

primeiro_num = float(input("Digite o primeiro número: "))
segundo_num = float(input("Digite o segundo número: "))
terceiro_num = float(input("Digite o terceiro número: "))

if primeiro_num == segundo_num == terceiro_num:
    print("Os números são iguais")
else:  
    maior_numero = max(primeiro_num,segundo_num,terceiro_num)
    menor_numero = min(primeiro_num,segundo_num,terceiro_num)

    print(f"O maior número é {maior_numero}")
    print(f"O menor número é {menor_numero}")