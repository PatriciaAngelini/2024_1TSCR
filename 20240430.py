#Contagem de Vogais e Consoantes: Receba uma frase do usuário e conte o número de vogais e consoantes nela.
print("Contador de vogais e consoantes")
frase = input("digite uma frase: ")
vogais, consoantes, espacos = 0, 0, 0
for letra in frase:
  if letra in 'aeiouAEIOU':
    vogais +=1
  elif letra == ' ':
    espacos +=1
  else:
    consoantes += 1
  print(letra)
print(f'Na frase:{frase} temos {vogais} vogais e {consoantes} consoantes')

#Ana Julia 
# def contar_vogais_consoantes(frase):

#   vogais = sum(1 for letra in frase if letra in 'aeiouAEIOU')

#   consoantes = sum(1 for letra in frase if letra not in 'aeiouAEIOU')

#   return vogais, consoantes

# frase = input("digite uma frase: ")
# num_vogais, num_consoantes = contar_vogais_consoantes(frase)
# print("essa frase tem", num_vogais, "números de vogais, e", num_consoantes, "números de consoantes.")


#X elevado a Y: Crie um algoritmo que calcule o valor de x elevado a y, onde x é maior que 1 e y é inteiro maior igual a 2. Simule a operação de exponenciação utilizando o comando FOR. Exemplo: 3 elevado a 4 = 81. Repita o exerício usando o WHILE
#Arthur
# X > 1
# Y >= 2

print('insira os valores de X e Y')
x = float(input('x:'))
y = int(input('y:'))
total = 1
#3 elevado a 4 = 81 
#total = 3**4 -> 3*3*3*3
if x > 1 and y >= 2:
  for i in range(4):
    total = total * x
  print(f'{x} elevado {y} = {total}')
else:
  print('nao é possivel simular a exponenciacao')

#Menor, intermediario, maior:. Entre com 3 números em 3 variáveis diferentes ordene imprimindo também a classificação: menor, intermediário, maior
num1 = float(input("Digite o primeiro número: ")) 
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
#8, 7, 6
# 8 > 7
if num1 > num2:
  temp = num1 #8
  num1 = num2 #7
  num2 = temp # 8
#7, 8, 6  
if num1 > num3:
  temp = num1 #7
  num1 = num3 # 6
  num3 = temp # 7
#6, 8, 7
if num2 > num3:
  temp = num2 #8
  num2 = num3 #7
  num3 = temp #8
#6, 7, 8

print(f'menor:{num1}, intermediario{num2}, maior:{num3}')


#um outro jeito de fazer 
num1 = float(input("Digite o primeiro número: ")) 
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
#8, 7, 6
# 8 > 7
if num1 > num2:
  num1, num2 = num2, num1
#7, 8, 6  
if num1 > num3:
  num1, num3 = num3, num1
#6, 8, 7
if num2 > num3:
  num2, num3 = num3, num2
print(f'menor:{num1}, intermediario:{num2}, maior:{num3}')

#Felipe Nakamura
# Função para ordenar e imprimir os números
# def ordenar_numeros(a, b, c):
#     # Coloca os números em uma lista
#     numeros = [a, b, c]

#     # Ordena os números
#     numeros.sort()

#     # Imprime os números ordenados
#     print("Menor:", numeros[0])
#     print("Intermediário:", numeros[1])
#     print("Maior:", numeros[2])

# # Solicita ao usuário que entre com os números
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))

# # Chama a função para ordenar e imprimir os números
# ordenar_numeros(num1, num2, num3)


#Verificação de Palíndromo: Receba uma palavra do usuário e verifique se ela é um palíndromo (igual quando lida de trás para frente).
#ana
#abba
#Giovanni 
palavra=str(input("Digite uma palavra: ")).lower()
print(palavra)
palindromo=palavra[::-1]
if palavra==palindromo:
  print("Essa palavra é um palindromo")
else:
  print("Essa palavra nao é um palindromo")


palavra = 'ana'
invertida = ''
# range(0, 4) -> 0, 1, 2, 3
# range(4, 0, -1) -> 4, 3, 2, 1
for i in range(len(palavra), 0, -1): 
  print(i, palavra[i-1])
  invertida = f'{invertida}{palavra[i-1]}' 
print(invertida)  
if palavra == invertida:
  print(f"A palavra {palavra} é palindromo")

# Temporizador: Crie um algoritmo que simule um temporizador. Peça os minutos e imprima um relógio de minutos e segundos. Utilize o FOR – um for dentro do outro. Repita o exerício usando o WHILE

#Kaique
from time import sleep

minutos = int(input("Digite a quantidade de minutos: "))
total_segundos = minutos * 60

for s in range(total_segundos + 1):
    minutos = s // 60
    segundos = s % 60
    print(f"  {minutos:02d}:{segundos:02d}", end="\r")
    sleep(1)

print("Tempo completado!")


#while
from time import sleep

minutos = int(input("Digite a quantidade de minutos: "))
total_segundos = minutos * 60
segundos_passados = 0

while segundos_passados <= total_segundos:
    minutos = segundos_passados // 60
    segundos = segundos_passados % 60
    print(f"  {minutos:02d}:{segundos:02d}") #, end="\r")
    segundos_passados += 1
    #sleep(1)

print("Tempo completado!")


minutos = int(input("Digite a quantidade de minutos: "))
#total_segundos = minutos * 60
for m in range(minutos):
  for s in range(60):
    print(f'{m:02d}:{s:02d}')
print(f'{minutos:02d}:{00:02d}')

#Soma de Dígitos: Peça ao usuário um número inteiro e calcule a soma dos seus dígitos.
numero = input("Digite um número inteiro: ")
print(type(numero))
soma = 0
for digito in numero:
    print(digito)
    soma += int(digito)
print(soma)


numero = int(input("Digite um número inteiro: "))
soma_digitos = 0
while numero > 0:
    ultimo_digito = numero % 10
    soma_digitos += ultimo_digito
    numero //= 10
print("A soma dos dígitos é:", soma_digitos)

# Temporizador decrescente: Crie um algoritmo que simule um temporizador decrescente. Peça os minutos e imprima um relógio de minutos e segundos. Utilize o FOR. Repita o exerício usando o WHILE

minutos = int(input("quantidade de minutos para o temporizador "))
horario = minutos * 60
for i in range(horario, -1, -1):
    min = i // 60  
    seg = i % 60  
    print(f"{min:02d}:{seg:02d}")
