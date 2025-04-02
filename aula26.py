#  Você está construindo um sistema de gerenciamento de contatos. Crie um programa que realize as seguintes tarefas:

#  a) Peça ao usuário para digitar seu nome completo.

nome_completo = input("Cristal Liberdade da Silva Moreira:")

#  b) Concatene “Olá,” com o nome fornecido e exiba o resultado.

print("olá,"",nome_completo")

#  c) Conte quantos caracteres existem no nome completo digitado e exiba o resultado.

print("O nome completo possui",len(nome_completo),("caracteres"))

#  d) Peça ao usuário para digitar um sobrenome para procurar na string do nome completo.

sobrenome = input("Digite um sobrenome para procurar o nome completo:")

#  e) Verifique se o sobrenome fornecido está presente no nome completo e exiba uma mensagem apropriada.

if sobrenome in nome_completo:
  print(f'O sobrenome {sobrenome} está presente no nome completo')
else:
  print(f"O sobrenome {sobrenome} NÃO está presente no nome completo.")

#  f) Exiba o nome completo em letras maiúsculas.

print("Nome completo em letras maiusculas:", nome_completo.upper())

#  g) Substitua todas as ocorrências da vogal “a” na string do nome completo pelo carac
print("Nome com'a' substituido por '4':", nome_completo.replace('a','4'.replace('a','4')))
