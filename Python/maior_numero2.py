"""
Diferenciando qual é o maior número.
"""

primeiro_num = float(input("Digite o primeiro número: "))
segundo_num = float(input("Digite o segundo número: "))
terceiro_num = float(input("Digite o terceiro número: "))

if primeiro_num == segundo_num == terceiro_num:
    print("Os números são iguais")
else:    
    if primeiro_num >= segundo_num and primeiro_num >= terceiro_num:
        maior_numero = primeiro_num
    else:
        if segundo_num >= primeiro_num and segundo_num >= terceiro_num:
            maior_numero = segundo_num
        else:
            maior_numero = terceiro_num

        print(f"O maior número é {maior_numero}")
    