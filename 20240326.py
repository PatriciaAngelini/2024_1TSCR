print('Triangulo')
titulo = 'Triangulo'
print(f'{titulo:^30}')
nome = input('Entre com o seu nome').strip().lower() #strip tira os espacos, lower deixa tudo em minusculo, UPPER deixa tudo em MAIUSCULO
print(nome)
a = float(input(f'{nome}, entre com o primeiro lado do triangulo: '))
b = float(input('Entre com o segundo lado do triangulo: '))
c = float(input('Entre com o terceiro lado do triangulo: '))

if (a == b == c == 0) or (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
else:
    if (a==b==c): #a==b and b==c
        print("Equilatero")
    else:
        if (a == b) or (a == c) or (b ==c) :
            print("Isosceles")
        else:
            print("Escaleno")

#Ana Julia
lado_a = float(input("Digite a medida do lado A do triângulo: "))
lado_b = float(input("Digite a medida do lado B do triângulo: "))
lado_c = float(input("Digite a medida do lado C do triângulo: "))

if lado_a == lado_b == lado_c:
  print("O triângulo é equilátero!")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
  print("O triângulo é isósceles!")
else:
   print("O triângulo é escaleno!")

#Kaique
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    tipo = "equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "isósceles"
else:
    tipo = "escaleno"

print(f"O triângulo com lados de comprimento {lado1}, {lado2} e {lado3} é um triângulo {tipo}.")

#Ana Julia

X = int(input("Digite o número do mês em que estamos(1-12): "))
if X == 1:
    print("Mês:", "Janeiro")
elif X == 2:
    print("Mês:", "Fevereiro")
elif X == 3:
    print("Mês:", "Março")
elif X == 4:
    print("Mês:", "Abril")
elif X == 5:
    print("Mês:", "Maio")
elif X == 6:
    print("Mês:", "Junho")
elif X == 7:
    print("Mês:", "Julho")
elif X == 8:
    print("Mês:", "Agosto")
elif X == 9:
    print("Mês:", "Setembro")
elif X == 10:
    print("Mês:", "Outubro")
elif X == 11:
    print("Mês:", "Novembro")
elif X == 12:
    print("Mês:", "Dezembro")
else:
    print("Mes Invalido")

# #Kaique
mes = int(input("Digite o mês [1 - 12] >>  "))
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

if mes > 0 and mes < 13:
    print(f"{meses[mes - 1]}")
else:
    print("Digite um valor valido [1 - 12]")

#Arthur
#exercicio sobre programa que diz qual mes estamos

# janeiro = 1
# fevereiro = 2
# março = 3
# abril = 4
# maio = 5
# junho = 6
# julho = 7
# agosto = 8
# setembro = 9
# outubro = 10
# novembro = 11
# dezembro = 12

print('qual mes estamos?')
mes = int(input('digite o numero do mes: '))

if mes == 1: print('janeiro')
elif mes == 2: print('fevereiro')
elif mes == 3: print('março')
elif mes == 4: print('abril')
elif mes == 5: print('maio')
elif mes == 6: print('junho')
elif mes == 7: print('julho')
elif mes == 8: print('agosto')
elif mes == 9: print('setembro')
elif mes == 10: print('outubro')
elif mes == 11: print('novembro')
elif mes == 12: print('dezembro')
elif mes > 12: print('isso nao e um mes')