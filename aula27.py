# Exercícios

#  1. Crie duas variáveis do tipo string, uma contendo “Olá” e outra contendo “Mundo”. Concatene-as e imprima o resultado.

s1 = "Olá"
s2 = "Mundo"
resultado = s1 + " " + s2
print(resultado)

#  2. Dada a string “Python”, imprima o caractere que está no índice 2.

s = "Python"
print(s[2])

#  3. Crie uma string qualquer. Substitua um dos caracteres por outro e imprima a nova string resultante.

s = "Python"
s_modificada = s.replace("y", "i")  # Substitui 'y' por 'i'
print(s_modificada)

#  4. Solicite ao usuário que digite seu nome. Em seguida, imprima o comprimento do nome fornecido.

s = input("Digite uma string: ")
print(len(s))

#  5. Crie uma string que represente uma frase. Verifique se a palavra “gato” está presente na frase e imprima o resultado (verdadeiro ou falso)

frase = "Meu gato é fofo"
print("gato" in frase)

#  6. Peça ao usuário que digite uma frase. Conte o número de palavras na frase e imprima o resultado.

frase = input("Digite uma frase: ")
print(len(frase.split()))

#  7. Crie uma função que receba uma frase como parâmetro e retorne a mesma frase com as palavras invertidas. Por exemplo, “Olá Mundo” deve ser transformado em “Mundo Olá”.

def inverter_frase(frase):
    return " ".join(frase.split()[::-1])

frase = input("Digite uma frase: ")
print(inverter_frase(frase))

#  8. Solicite ao usuário que digite uma string que contenha espaços em branco no início e no final. Remova esses espaços e imprima a string resultante.

s = input("Digite uma string com espaços extras: ")
print(s.strip())

#  9. Crie uma função que receba um número inteiro e retorne uma string que o represente com separadores de milhares. Por exemplo, para o número 1234567, a função 
# deve retornar “1,234,567”.

def formatar_numero(n):
    return f"{n:,}"

numero = int(input("Digite um número: "))
print(formatar_numero(numero))

#  10. Implemente uma função que receba uma string e um número (chamado de “deslocamento”) como parâmetros e retorne a string cifrada, usando a Cifra de César. 
# Cada letra na string deve ser deslocada pelo número fornecido. Por exemplo, com um deslocamento de 3, “ABC” seria cifrado como “DEF”

def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            inicio = ord('A') if char.isupper() else ord('a')
            resultado += chr(inicio + (ord(char) - inicio + deslocamento) % 26)
        else:
            resultado += char
    return resultado

texto = input("Digite um texto: ")
deslocamento = int(input("Digite o deslocamento: "))
print(cifra_de_cesar(texto, deslocamento))

# 11. Escreva um programa que receba uma palavra ou frase do usuário e determine se ela é um palíndromo ou não. O programa deve ignorar maiúsculas e minúsculas, bem como 
# espaços em branco

def eh_palindromo(texto):
    texto_limpo = "".join(texto.lower().split())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")
print("É um palíndromo" if eh_palindromo(frase) else "Não é um palíndromo")
