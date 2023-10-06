"""
Diferenciando qual é o maior número.
"""
primeiro_num = int(input("Digite o primeiro número: "))
segundo_num = int(input("Digite o segundo número: "))

if primeiro_num == segundo_num:
    print("Os números são iguais")
else:
    if primeiro_num > segundo_num:
        print(f"O maior número é {primeiro_num}")
    else:
        print(f"O maior número é {segundo_num}")
