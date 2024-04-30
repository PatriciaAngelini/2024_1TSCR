#Primeiro programa em Python
print("Hello World")
print('Bem vindos')

print(1+2)
print(4**2)
print(10/3)

print(type(2))
print(type(10/3))
print(type('Bem vindos'))

print(len('Bem vindos'))

x = 10
print(x)
print(x+87)
y=x+96
print(y)
print(x)
print(type(x))
#print(len(x))
temp = str(x)
print(type(temp))
print(len(temp))

#Exercicios
#Vamos escrever um programa em Python que calcule a média de dois números;
x=5
y=47
#precedencia de operadores da matematica
#exponenciacao **
#divisao e multiplicacao / * // %
#adicao e subtracao + -
media=(x+y)/2
print(media)
print(type(media))

#Sobre outros dois operadores matematicos
x = 13 / 3
print(x)
divinteira_X = 13 // 3
print(divinteira_X)
resto=13%3
print(resto)

#Exercicios
#Calcular a media de duas notas
#Constantes
#Valores fixos de uma variavel, definidos ja na atribuição
nota1 = 7
nota2 = 8
media = (nota1 + nota2)/2
print("Media", media)

#Taximetro
#Kaique
km_custo = 2.5
km_rodado = 10
pagar = km_rodado * km_custo

print("O valor do km", km_custo, "rodamos", km_rodado, "quilometros")

print("O valor do km", km_custo)
print("rodamos", km_rodado, "quilometros")

print("O valor do km", km_custo, "\nrodamos", km_rodado, "quilometros")

print(f" Valor KM: R${km_custo} \n rodou {km_rodado}KM \n valor pagar: R${pagar}")

print(" Valor KM: R${km_custo} \n rodou {km_rodado}KM \n valor pagar: R${pagar}")

#A entrada de dados é feita pelo comando INPUT
#nome = 'Patricia'
nome = input("Qual é o seu nome? ")
print("Boa noite", nome)
#idade = input("Qual sua idade? ")
idade = int(input("Qual sua idade? "))
print("Você parece muito jovem para", idade, "anos")
print(f"Você parece muito jovem para {idade} anos")
print(type(idade))
#idade_futura = int(idade) + 8
idade_futura = idade + 8
print(idade_futura)

#Media pedindo as notas
print("Calcula Medias")
nota1 = float(input("Entre com a primeira nota "))
nota2 = float(input("Entre com a segunda nota "))
media = (nota1 + nota2)/2
print("Sua média será", media)

#Programa do Taximetro
titulo = "Taximetro"
print(titulo)
km_custo = 2.5
km_rodado = float(input("Quantos km o taxi rodou? "))
pagar = km_rodado * km_custo

print(f" Valor KM: R${km_custo} \n rodou {km_rodado}KM \n valor pagar: R${pagar}")


#Desafio
#Conversor de Celsius para Farenheit
# C/5 = (F-32)/9
# 9*C=5*(F-32)
# 9*C=5*F - (32*5)
# 9*C=5*F-160
# 5*F-160=9*C
# 5*F=9*C+160
# F=(9*C+160)/5

# #Kaique
celsius = float(input("Temperatura em graus Celsius:  "))

fahrenheit = (celsius * 1.8) + 32

print(chr(176))

print(f"{celsius} graus celsius equivale a {fahrenheit} graus  Fahrenheit")

#Giovanni
temperatura=float(input("Digite a temperatura:"))
escala=str(input("Digite a escala (C/F):"))
if escala=="C":
  resultado1=float(((temperatura*9)/5)+32)
  print(resultado1)
else: 
  resultado2=float(((temperatura-32)*5)/9)
  print(resultado2)


#Conversor de Farenheit para Celsius
# #Kaique
fahrenheit = float(input("Temperatura em graus fahrenheit:  "))

celsius = (fahrenheit - 32) / 1.8

print(f"{fahrenheit} fahrenheit graus fahrenheit equivale a {celsius} graus  celsius")

#Felipe
# Conversor de graus Celsius para Farenheit

celsius = float(input("Digite a temperatura em graus Celsius: "))
farenheit = (celsius * 9/5) + 32
print(f"A temperatura em graus Farenheit é: {farenheit:.2f} °F")

# Conversor de graus Farenheit para Celsius

farenheit = float(input("Digite a temperatura em graus Farenheit: "))
celsius = (farenheit - 32) * 5/9
print(f"A temperatura em graus Celsius é: {celsius:.2f} °C")

mensagem = 'A temperatura em graus Celsius é:' + str(celsius) + chr(176) + 'C'
print(mensagem)