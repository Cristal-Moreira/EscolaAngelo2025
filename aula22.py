# EXERCÍCIOS WHILE

#  1. Adivinhação de números:
#  • Criem uma lista com 10 números.
#  • Peçam ao usuário para adivinhar um número da lista.
#  • Usem um loop while para continuar pedindo adivinhações até que o usuário acerte.

import random

numeros = random.sample(range(1, 101), 10)  # Lista com 10 números aleatórios
print("Tente adivinhar um número da lista!")

while True:
  tentativa = int(input("Digite um número: "))
  if tentativa in numeros:
    print("Parabéns! Você acertou.")
    break
  else:
    print("Tente novamente!")
 
#  2. Contagem regressiva:
#  • Criem uma lista de contagem regressiva de 10 a 1.
#  • Usem um loop while para imprimir cada número da lista

contagem = list(range(10, 0, -1))  # Lista de 10 a 1
i = 0

while i < len(contagem):
  print(contagem[i])
  i += 1

# 3. Adição de números:
#  • Criem uma lista vazia para armazenar números.
#  • Peçam ao usuário para fornecer números e os adicionem à lista.
#  • Continuem pedindo números até que o usuário decida parar.

numeros = []

while True:
    num = input("Digite um número (ou 'sair' para parar): ")
    if num.lower() == "sair":
        break
    numeros.append(int(num))

print("Lista final:", numeros)

#  4.Média de notas:
#  • Criem uma lista vazia para armazenar notas.
#  • Peçam ao usuário para fornecer notas e as adicionem à lista.
#  • Calculem e imprimam a média das notas quando o usuário decidir parar
  
notas = []

while True:
    nota = input("Digite uma nota (ou 'sair' para calcular a média): ")
    if nota.lower() == "sair":
        break
    notas.append(float(nota))

if notas:
    media = sum(notas) / len(notas)
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")

# 5.Busca em lista:
#  • Criem uma lista de cinco nomes.
#  • Peçam ao usuário para digitar um nome.
#  • Usem um loop while para verificar se o nome está na 
# lista e informar o resultado.

nomes = ["Ana", "Carlos", "Beatriz", "Daniel", "Fernanda"]

while True:
    nome = input("Digite um nome para buscar (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    if nome in nomes:
        print(f"{nome} está na lista!")
    else:
        print(f"{nome} não foi encontrado.")

#  6. Contador de números:
#  • Solicitem ao usuário um número inicial.
#  • Usem um loop while para imprimir os números de 1 até o 
# número fornecido pelo usuário.
#  • Exibam uma mensagem indicando que o loop terminou

num = int(input("Digite um número inicial: "))
contador = 1

while contador <= num:
    print(contador)
    contador += 1

print("O loop terminou.")

