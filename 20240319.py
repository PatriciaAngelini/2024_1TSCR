#Condição é uma comparação que resulta em sim/nao True/False

print(1>2)
x = 9
print(x==9)
print(x+4<=18)
print('patricia' == 'Patricia')
nome = 'Ana Julia'
print(nome=='Patricia')

#constante
idade = 7
idade_direito_a_voto = 16
print(type(idade))
idade = int(input('Informe a sua idade: '))
print(type(idade))
print('a sua idade é', idade)
print(f'a sua idade é {idade} anos')
#if idade >= 16:
if idade >= idade_direito_a_voto:
  print('Você pode votar')

print('Você é um cidadão brasileiro')

#combinando condicoes
print("Operador logico or - bonzinho")
print('or - Combinando dois lados verdadeiros')
print(1 != 2 or 10 > 3)
print('or - Combinando um dos lados verdadeiro')
print(1 == 2 or 10 > 3)
print('or - Combinando os dois lados falsos')
print(1 == 2 or 10 < 3)

print("Operador logico and - malvado")
print('and - Combinando dois lados verdadeiros')
print(1 != 2 and 10 > 3)
print('and - Combinando um dos lados verdadeiro')
print(1 == 2 and 10 > 3)
print('and - Combinando os dois lados falsos')
print(1 == 2 and 10 < 3)

print("Operador logico not - do contra")
print(not(1 != 2))
print(not(1 == 2))


clima_bom = 'sim'
dinheiro = 'sim'
print("Viagem otima")
if clima_bom == 'sim' and dinheiro == 'sim':
  print("Vou viajar")

print("Viagem mais ou menos")
if clima_bom == 'sim' or dinheiro == 'sim':
  print("Vou viajar")

print("Viagem do contra")
if not(clima_bom == 'sim') and not(dinheiro == 'sim'):
  print("Vou viajar")

#Um condomínio possui 4 blocos que são abastecidos por duas caixas d’água diferentes. A caixa A abastece os blocos pares e a caixa B abastece os blocos ímpares. Escreva um algoritmo que pergunte ao usuário em qual bloco ele mora (1- 4) e escreva na tela qual a caixa que abastece seu bloco: a caixa a ou a caixa B;
bloco = int(input("Digite seu bloco [1 - 4] >> "))
if bloco % 2 == 0:
  print(f'O bloco {bloco} é abastecido pela caixa A')
else:
  print(f'O bloco {bloco} é abastecido pela caixa B')

#Kaique
bloco = int(input("Digite seu bloco [1 - 4] >> "))

if bloco > 0 and bloco < 5:
    if bloco % 2 == 0:
        print(f'O bloco {bloco} é abastecido pela caixa A')
    else:
        print(f'O bloco {bloco} é abastecido pela caixa B')
else:
    print('Digite uma opção valida!')


bloco = int(input("Digite seu bloco [1 - 4] >> "))
if bloco in (2,4):
  print(f'O bloco {bloco} é abastecido pela caixa A')
else:
  print(f'O bloco {bloco} é abastecido pela caixa B')

#Um condomínio possui 20 blocos e para uma correta administração possui dois síndicos: o sr José que administra os blocos de 1 a 10 e o sr Hamilton que administra os blocos de 11 a 20. Escreva um algoritmo que pergunte ao usuário em qual bloco ele mora e escreva na tela qual o síndico responsável;

print("Sindico")
bloco = int(input("Digite seu bloco [1 - 20] >> "))
#errado: bloco >=1 and <=10
if bloco >= 1 and bloco <=10:
  print(f'O bloco {bloco} é adm Sindico Sr José')
else:
  print(f'O bloco {bloco} é adm Sindico Sr Hamilton')

print("Sindico")
bloco = int(input("Digite seu bloco [1 - 20] >> "))
if bloco >= 1 and bloco <=10:
  print(f'O bloco {bloco} é adm Sindico Sr José')
if bloco >= 11 and bloco <=20:
    print(f'O bloco {bloco} é adm Sindico Sr Hamilton')
print("Sindico")
bloco = int(input("Digite seu bloco [1 - 20] >> "))
if bloco >= 1 and bloco <=20:
  if bloco >= 1 and bloco <=10:
    print(f'O bloco {bloco} é adm Sindico Sr José')
  else:
    print(f'O bloco {bloco} é adm Sindico Sr Hamilton')
else:
  print('Entre com um bloco valido')

# Escreva um algoritmo que pergunte o valor de uma mercadoria e qual o valor que o usuário tem em mãos e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria;


#Giovanni
mercadoria=float(input("Qual o valor da mercadoria?"))
dinheiro=float(input("Qual o valor que você tem em mãos?"))
if dinheiro >= 0 and mercadoria >= 0:
  if dinheiro>=mercadoria:
    print("Você pode adquirir a mercadoria")
  else:
    print("Quantidade insuficiente de dinheiro")
else:
  print('Entre com valores positivos')

#Kaique
mercadoria = float(input('Valor da mercadoria >> '))
usuario = float(input('Dinheiro do usuario>> '))

print(f'O produto custa R${mercadoria:.2f} e o usuario tem R${usuario:.2f} ')
if usuario >= mercadoria:
    print('O usuario tem dinheiro suficiente para comprar!')
else:
    print('O usuario não tem dinheiro suficiente para comprar!')

#Maria Julia
produto = float(input('Informe valor mercadoria:'))
money = float(input('dinheiro que vc tem:'))

if money >= produto:
     print('Pode comprar')
else:
     print('Pode comprar não')

# Um estacionamento cobra R$ 5,00 por hora porém possui um teto de cobrança máxima de R$ 35,00, independente do   número de horas. Escreva um algoritmo que pergunte ao usuário qual foi o período de permanência em horas e escreva na tela o total a pagar;

# #Kaique
#constante
hora = 5
periodo = int(input('Tempo de permanencia >> '))

if periodo > 7:
    valor = 35
    print(f'Tempo de permanencia: {periodo}:00 \nTotal a pagar: R${valor:.2f}')
else:
    print(f'Tempo de permanencia: {periodo}:00 \nTotal a pagar: R${(hora * periodo):.2f}')

# #Maria Julia
parking = int(input('Tempo de permanência: '))
total = 5*(parking)

if (total >= 35):
  print('Vc ficou {} horas e deve pagar 35'.format(parking))

else:
  print('Vc ficou {} horas e deve pagar {}'.format(parking, total))


#Ana Julia
permanencia = int(input(" Digite o período de permanência em horas? "))
if permanencia >= 7: 
  #total = 35
  print("Você ficou", permanencia, "horas, o valor a ser pago é de R$35,00")
else:
  total = permanencia * 5
  print("Você ficou", permanencia,"horas, o valor a ser pago é de R$", total)

#Escreva um programa que pergunte ao usuário qual foi a média anual de um aluno da FIAP e ao final diga se ele está aprovado, reprovado, de exame ou se a nota digitada é inválida.

print('Media')
nota = float(input('Entre com a media: '))
if nota < 0 or nota > 10:
  print('Nota invalida')
else:
  if nota >= 6:
    print('Aprovado')
  else:
    if nota >= 4:
      print('Exame')
    else:
      print('Reprovado')

#Kaique
n1 = float(input('Nota primeiro semestre >> '))
n2 = float(input('Nota segundo semestre >> '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Média: {media} REPROVADO!')
elif media < 5.9:
    print(f'Média: {media} EXAME!')
else:
    print(f'Média: {media} APROVADO!')