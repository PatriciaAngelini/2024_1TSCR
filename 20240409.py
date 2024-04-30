titulo = "Pares ate 600"
print(f"\033[31m{titulo:*^30}\033[0;0m")

#Kaique

for n in range(1, 601):
  if n % 2 == 0:
    print(f'{n:0>3d}', end=' ')

#6 é primo?
#qq numero é divisivel por 1 e por ele mesmo
#6 sabemos q é divisivel por 1 e 6
#lista de teste: 2,3,4,5
#se um numero é divisivel por qq numero da lista de teste, entao ele não é primo

#para testarmos o numero 6, tivemos a lista de 2 a 5

#para o numero 7 a nossa lista deveria ser de 2 até 6
#para o num 8 a lista deveria ser de 2 até 7
titulo = "Primos"
print(f"\033[31m{titulo:*^30}\033[0;0m")
num = int(input("Qual nro vc quer testar: "))
eh_primo = True
for i in range(2, num):
    if num % i == 0:
        eh_primo = False
        break
if eh_primo:
    print(f"O numero {num} é primo")
else:
    print(f"O numero {num} não é primo")

# #Arthur
# falta desenvolver mais, corrigindo o pensamento
# #exercicio para verificar se um numero e primo
#
# numero = int(input('insira um numero: '))
# if numero % 1 == 0 and numero % numero == 0:
#     print('o numero e primo')
# if numero % 1 != 0 and numero % numero != 0:
#     print('o numero nao e primo')

#Kaique
num = int(input('Digite um numero: '))
if num == 0:
    print('Digite um numero positivo')
elif num == 1:
    print('1 não é primo')
else:
    count = 0
    for i in range(2, num):
            if num % i == 0:
                count += 1
    if count > 0:
        print(f'{num} não é primo')
    else:
        print(f'{num} é primo')

titulo = "Soma dos Pares"
print(f"\033[33m{titulo:*^30}\033[0;0m")
#Kaique
num = int(input('Digite um numero: '))
soma = 0
if num <= 0:
    print('Digite um numero positivo')
else:
    for i in range(1, num+1):
        if i % 2 == 0:
            soma += i
            print(i, end=' ')

print(f'\nSoma dos numeros pares: \033[31m{soma}\033[0;0m')


titulo = "Soma dos Pares com o While"
print(f"\033[33m{titulo:*^30}\033[0;0m")
#
num = int(input('Digite um numero: '))
soma = 0
i = 0
if num <= 0:
    print('Digite um numero positivo')
else:
    while i <= num:
        if i % 2 == 0:
            soma += i
            print(i, end=' ')
        i += 1

print(f'\nSoma dos numeros pares: \033[31m{soma}\033[0;0m')

#Estado onde nasceu
# estados = ['SP', 'MG']
# cidades = ['paulista', 'mineiro']

print(f"\033[33m{titulo:*^30}\033[0;0m")
estado = input("Digite o estado onde você nasceu ").upper()
if estado == 'SP' or estado == 'SAO PAULO' or estado == 'SÃO PAULO':
    print('Voce é paulista')
elif estado in ('RJ', 'RIO DE JANEIRO'):
    print('Você é carioca')
elif estado in ('BA', 'BAHIA'):
    print('Você é baiano')
elif estado in ('MG', 'MINAS', 'MINAS GERAIS'):
    print('Você é mineiro')
elif estado in ('CE', 'CEARA', 'CEARÁ'):
    print('Você é cearense')

#Kaique
estados_sigla = {
    "AC": "Acreano(a)",
    "AL": "Alagoano(a)",
    "AP": "Amapaense",
    "AM": "Amazonense",
    "BA": "Baiano(a)",
    "CE": "Cearense",
    "ES": "Capixaba",
    "GO": "Goiano(a)",
    "MA": "Maranhense",
    "MT": "Mato-Grossense",
    "MS": "Sul-Mato-Grossense",
    "MG": "Mineiro(a)",
    "PA": "Paraense",
    "PB": "Paraibano(a)",
    "PR": "Paranaense",
    "PE": "Pernambucano(a)",
    "PI": "Piauiense",
    "RJ": "Carioca",
    "RN": "Potiguar",
    "RS": "Gaúcho(a)",
    "RO": "Rondoniense",
    "RR": "Roraimense",
    "SC": "Catarinense",
    "SP": "Paulista",
    "SE": "Sergipano(a)",
    "TO": "Tocantinense"
}

estado = str(input('Digite a sigla do estado: ')).upper().strip()

if estado not in estados_sigla:
    print('Digite um estado valido!')
else:
    print(f'Quem nasce em {estado} é {estados_sigla[estado]}')

#Terça parte do número: Crie um algoritmo que solicite 10 números
# e imprima a terça parte deles.
# Utilize o FOR, atenção a formatação. Repita o exercício usando WHILE


titulo="Terca Parte com FOR"
print(f"\033[33m{titulo:*^30}\033[0;0m")

for i in range(3): #o range aqui vai de 0 a 9 gerando 10 numeros
    # n = float(input('Entre com um numero: '))
    # print(n/3)

    # n = float(input('Entre com um numero: '))
    # print(round(n/3, 2))

    #print(float(input('Entre com um numero: '))/3)

    n = float(input('Entre com um numero: '))
    print(f"{n/3:.2f}" )

titulo="Terca Parte com WHILE"
print(f"\033[33m{titulo:*^30}\033[0;0m")

i = 0
while i < 3:
    n = float(input("Entre um numero: "))
    terca_parte = n / 3
    print(f"{terca_parte:.2f}")
    i += 1