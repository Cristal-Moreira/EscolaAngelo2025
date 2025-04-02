# EXERCICIOS

# 1. Na lista pares = [0, 2, 4, 8]:
# a) Acrecente o valor 10 ao final da lista.
# b) Acrecente o valor 6 na posição 3.
pares = [0, 2, 4, 8]
pares.append(10)
pares.insert(3, 6)
print(pares)# 2. Na lista impares = [1, 3, 3, 5, 7, 9]:


# a) Remova o valor 3.
# b) Remova o valor da posição (indice) 4.
# c) Mostre o valor que sera removido da posição (indice)
impares = [1, 3, 3, 5, 7, 9]
impares.remove(3)
valor_removido = impares.pop(4)
print(valor_removido)
print(impares)


# 3. Na lista fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]:
# a) Ordene a lista.
# b) Coloque em valor reverso a lista fibonacci.
fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
fibonacci.sort()
print(fibonacci)


# 4. Na lista pi = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# a) Busque o elemento que esta no indice 5 da lista.
# b) Imprima o tamanho da lista.
# c) Imprima o tamanho maximo da lista.
# d) Imprima o valor minimo da lista.
# e) Imprima apenas o resultado [4, 5]
pi = [3, 1, 4, 1, 5, 9, 2, 6, 5,]
print(pi[5])
print(len(pi))
print(max(pi))
print(min(pi))
nova_lista = [4, 5]
print(nova_lista)
