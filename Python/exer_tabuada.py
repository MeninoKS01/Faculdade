print("----------------------------------") 

numero = int(input("Digite um número: "))

print("----------------------------------")

for i in range(10):
    i=i+1
    resultado_soma = numero + i
    resultado_sub = numero - i
    resultado_mult = numero * i
    resultado_div = numero / i

    print(
        f"{numero} + {i} = {resultado_soma}\t", 
        f"{numero} - {i} = {resultado_sub}\t", 
        f"{numero} x {i} = {resultado_mult}\t",
        f"{numero} / {i} = {resultado_div:.2f}\t"
        )
 
print("----------------------------------") 