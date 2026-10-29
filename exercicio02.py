print("o usuario escolhe os numeros")
numeros = []
quantidade = int(input("quantos numeros voce quer digitar na lista? "))
for i in range(quantidade):
    numero = int(input(f"digite o {i+1}º numero: "))
    numeros.append(numero)
print(f"numeros digitados: {numeros}")

#mostrae somente os numeros pares
print("nuemros pares")
for i in numeros:
    if i %2 ==0:
        print(i)