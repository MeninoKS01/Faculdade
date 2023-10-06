"""
Criar uma calculadora IMC
"""

peso = float(input("Coloque seu peso (kg): "))
altura = float(input("Coloque sua altura (m): "))

imc = peso / altura ** 2

print(f"Seu índice de massa corporal é {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Seu peso está dentro da faixa padrão")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso")
elif imc >= 30:
    print("Você está com obesidade")

