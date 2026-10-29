print("exercico\n")
numeros = []
quantidade = int(input("escolha a quantidade de numeros para a lista: "))

for i in range(quantidade):
    numero =int(input(f"digite o {i+1} numero: "))
    numeros.append(numero)
print(f"numeros digitados: {numeros}\n ")
print("nuemros impares")
for i in numeros:
    if i %2 == 1:
        print(i)

print("ordem crescente:\n")
numeros.sort()
print(f"numeros {numeros}")
print("ordem decrescente:\n")
numeros.sort(reverse=True)
print(f"numero {numeros}")
numero_r = int(input("escolha um numero para remover: "))
numeros.remove(numero_r)
numeros.sort(reverse=True)
print(f"numero atualizados: {numeros}")

