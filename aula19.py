nomes = ["Ana", "Paula", "Maria", "Sophia", "Fernanda", "sophia"]

print(f"a primeira ocorrencia de sophia e no indice: {nomes.index("Sophia")}")

print(f"Sophia aparece {nomes.count("Sophia")} vezes na lista")

nomes.sort()
print(nomes)

nomes.reverse()
print(nomes)

copiaNomes = nomes.copy()
print(f"Nomes copiados: {copiaNomes}")
