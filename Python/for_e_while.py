"""
Usando estrutura de repetição usando o for e range
"""

linha=0
soma=0
for ano in range(2000,2020):
    
    linha=linha+1

    if ano % 4 == 0:
        print(f"{linha}- O ano {ano} é bissexto")
    else:
        print(f"{linha}- O ano {ano} não é bissexto")

    soma=soma+1

print(f"Totais de anos {soma}")
