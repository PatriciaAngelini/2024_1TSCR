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

