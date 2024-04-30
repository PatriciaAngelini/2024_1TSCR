titulo = "Tabuada com o For"
print(f'{titulo:^30}')

numero = int(input("Entre com o numero da tabuada:"))

for i in range(1,11):
  tabuada = numero * i
  print(f'{numero} X {i} = {tabuada}')
  #print(numero, "X", i, "=", tabuada)

# #Equivalente
# tabuada = 1 * numero
# print(numero, "X", "1", "=", tabuada)
# tabuada = 2 * numero
# print(numero, "X", "2", "=", tabuada)
# tabuada = 3 * numero
# print(numero, "X", "3", "=", tabuada)

# for i in range(1,10+1):
#   tabuada = numero * i
#   print(numero, "X", i, "=", tabuada)



# for i in range(10):
#   tabuada = numero * i
#   print(numero, "X", i, "=", tabuada)

# for i in range(1,11,2):
#   tabuada = numero * i
#   print(numero, "X", i, "=", tabuada)

titulo = "PIM"
print(f'{titulo:^30}')

for i in range(1,31):
  if i%4==0:
    print("PIM")
  else:
    print(i)


#Ana Julia
for i in range(1, 31):
  if i % 4 == 0:
    print("pim")
  else:
    print(i)


titulo = "Divisiveis por 5"
print(f'{titulo:>30}')

x = int(input("Entre com o primeiro numero:"))

y = int(input("Entre com o segundo numero:"))

if x>y:
  # temp = x
  # x = y
  # y = temp
  x, y = y, x

for i in range(x,y+1):
  if i % 5 == 0:
    print(i)

#Kaique
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
cont = 0
divisiveis = ""
for i in range(n1, n2 + 1):
    print(i, end=' ')
    if i % 5 == 0:
        divisiveis = divisiveis + " " + str(i) 
        cont += 1


print(f"\n\nEntre {n1} e {n2} existem {cont} divisiveis por 5: {divisiveis}")

#Giovanni
#Ana Julia
numero_1 = int(input("Escreva o primeiro número:"))
numero_2 = int(input("Escreva o segundo número:"))

for i in range(numero_1, numero_2+1):
  if i % 5 == 0: 
    print(i)

titulo = "Contagem Regressiva"
print(f'{titulo:40}')

import time

for i in range(60,-1,-1):
  time.sleep(1)
  print(i)


titulo = "Tabuada com o While"
print(f'{titulo:^30}')

numero = int(input("Entre com o numero da tabuada:"))
i = 1
while i <= 10:
  #tabuada = numero * i
  #print(f'{numero} X {i} = {tabuada}')
  #i = i + 1
  print(f'{numero} X {i} = {numero * i}')
  i += 1


print("Imprimindo um nome 10 x")
nome = "Jabuticaba"

print("Imprimindo com o FOR")
for i in range (10):
  print(i, nome)

print("Imprimindo com o WHILE")
i = 0
while (i < 10):
  print(i, nome)
  i += 1

# #problema do Fibonacci
# 1o termo/numero (a):0
# 2o termo/numero (b):1
# 3o termo (c) - calculo - 1o termo + 2o termo = 1

# 1o termo/numero (a):1
# 2o termo/numero (b):1
# 3o termo(c) - calculo - 1o termo + 2o termo = 2

# 1o termo/numero:1
# 2o termo/numero:2
# 3o termo - calculo - 1o termo + 2o termo = 3

# 1o termo/numero:2
# 2o termo/numero:3
# 3o termo - calculo - 1o termo + 2o termo = 5

# 1o termo/numero:3
# 2o termo/numero:5
# 3o termo - calculo - 1o termo + 2o termo = 8
# Sequencia de Fibonacci
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34