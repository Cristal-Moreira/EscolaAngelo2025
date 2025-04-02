

# EXERCICIOS DE FIXAÇÃO

# 1. Adicione o numero 50 ao final da lista.
lista_numero = [10, 20, 30, 40]

lista_numero.append(50)
print(lista_numero)

# 2. Adicione "laranja" ao indice 1 da lista.
lista_frutas = ["maça", "banana", "uva"]

lista_frutas.insert(1, "laranja")
print(lista_frutas)

# 3. Remova "cachorro" da lista.
lista_animais = ["cachorro", "gato", "passaro", "cachorro"]

while "cachorro" in lista_animais:
   lista_animais.remove("cachorro")
print(lista_animais)

# 4. remova o elemento de indece 2 da lista e mostre o elemento removido.
lista_nomes = ["alice", "bob", "charlie", "david"]

lista_nomes = ["alice", "bob", "charlie", "david"]
print(lista_nomes.pop(2))

# 5. encontre o indice da primeira ocorrencia "azul" na lista.
lista_cores = ["vermelho", "azul", "verde", "amarelo", "azul"]

lista_cores = ["vermelho", "azul", "verde" "amarelo", "azul"]
print(lista_cores.index("azul"))

# 6. conte quantas vezes o numero 2 aparece na lista.
lista_numeros_repitidos = [1, 2, 3, 2, 4, 2, 5, 2]

lista_numeros_repitidos = [1, 2, 3, 2, 4, 2, 5, 2]
print(lista_numeros_repitidos.count(2))

# 7. ordene a linta em ordem crecente.
lista_desordenada = [50, 20, 80, 10, 40]

lista_desordenada = [50, 20, 80, 10, 40]
lista_desordenada.sort()
print(lista_desordenada)

# 8. inverta a ordem dos elementos da lista.
lista_invertida = ["maça", "banana", "laranja", "uva"]
lista_invertida.reverse()
print(lista_invertida)
