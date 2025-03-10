# 1. faça um programa que peça a idade do usuario e inprima se ele for maior ou 
# menor de 18 anos.
idade = int(input("digite sua idade: "))

if idade >= 18:
  print("é de maior!")
else:
  print("é d mernor!")

  # 2. faça um programa que peça um numero de mostre se ele épositivo ou negativo.

numero = int(input("digite um numero inteiro: "))

if numero >= 0:
  print("o numero é positivo")
else:
  print("o numero é negativo")

# 3. faça um programa que, dado um numero digitado, mostre se ele é par ou impa.

numero = int(input("digite um numjero inteiro: ")) 
if numero % 2 == 0:
   print("o numero é par.")
else:
   print("o numero é impar.")


# 4. faça um programa que peça dois numeros e mostre o maior deles.

n1 = int(input("digite um inteiro: "))
n2 = int(input("digite outro inteiro: "))
         
if n1 > n2:
  print(n1)
else:
  print(n2)

# 5. faça um programa que leia a validade das informaçoes:
# a. idade : entre 0 e 150;
# b. salario: maior que 0
# c. sexo: m, f ou outro;

idade = int(input("digite a idade maior que o menor 150: "))
if idade > 0 and idade < 150:
  print("idade valida")
else:
  print("idade invalida")

salario = int(input("digite o salario: r$ "))
if salario > 0:
  print(f"o salario invalido")
else: 
  print("salaria invalido")

sexo= input("digite o sexo [m , f, outro]: ")
if sexo.upper == "m":
  print("sexo masculino")
elif sexo.upper == "f":
  print("sexo feminino.")
elif sexo. lower == "outro":
  print("sexo outo")
else:
  print("sexo invalido")