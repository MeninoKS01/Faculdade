"""
Atividade

Realizar uma adição, subtração, multiplicação ou divisão.

"""
resultado = 0
primeiro_num = float(input("Digite o primeiro número: "))
segundo_num = float(input("Digite o segundo número: "))
print("Escolha um operador pelo número: \n1 - Adição \n2- Subtração\n3 - Multiplição\n4 - Divisão")
operador = int(input("Operador de escolha: "))


if operador < 1 or operador > 4:
    print("Operador Inválido")

if operador == 1:
    resultado = primeiro_num + segundo_num
    print(f"Sua conta deu {resultado}")

if operador == 2:
    resultado = primeiro_num - segundo_num
    print(f"Sua conta deu {resultado}")

if operador == 3:
    resultado = primeiro_num * segundo_num
    print(f"Sua conta deu {resultado}")

if operador == 4:
    resultado = primeiro_num / segundo_num
    print(f"Sua conta deu {resultado}")

