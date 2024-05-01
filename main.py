
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