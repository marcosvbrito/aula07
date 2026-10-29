print("entre com os nomes e coloque em ordem alfabetica crescente\n")
nomes = []
quantidade = int(input("quantos nomes deseja inserir? "))
for i in range(quantidade):
    nome = input(f"{i+1}º nome: ")
    nomes.append(nome)

nomes.sort()
print(f"nomes em ordem alfabetica{nomes}")
nomes.sort(reverse=True)
print(f"nomes em ordem alfabetica decrescente {nomes}")

nome_remover = input("escolha um nome para remover da lista: ")
nomes.remove(nome_remover)
print(f"nomes: {nomes}")