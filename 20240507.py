#########
#COLECOES
#########

#Colecoes sao variaveis que apresentam mais de um valor em sua memoria
#os elementos das colecoes podem ser do mesmo tipo ou de tipos diferentes
#TODA colecao é um elemento ITERAVEL, ou seja eu posso percorrer esse elemento

#LISTA
#a primeira que veremos
#Caracteristicas
#a mais comum
#PODEROSA e FLEXIVEL
#MUTAVEIS - permite inserir elementos, modificar, excluir
#EXPANSIVEIS - permite juntas muitas listas em uma so
#ORDENAVEIS - existem metodos para ordenacao
#PERMITEM DUPLICADOS
#PERMITEM TIPOS DE DADOS DIFERENTES
#PODEM SER ACESSADAS POR INDICE 

print('LISTAS')
minhaLista = ['cafe', 'agua', 'acucar']
print(minhaLista)
#Entendendo como acessar cada elemento
            #-5    -4        -3        -2      -1  
            #0      1        2          3      4
minhaLista= ['cafe', 'agua', 'acucar', 'cafe', 'canela']
print(minhaLista)

print('Primeiro elemento', minhaLista[0])
print('Segundo elemento', minhaLista[1])
print('Terceiro elemento', minhaLista[2])
print('Primeiro elemento (negativo)', minhaLista[-5])
print('Ultimo elemento positivo', minhaLista[4])
print('Ultimo elemento negativo', minhaLista[-1])


#Slicing ou fatiamento
#é a capacidade de pegarmos um pedaco de um elemento iteravel
print('\n\nSlicing')
              #-5    -4        -3        -2      -1  
              #0      1        2          3      4
minhaLista= ['cafe', 'agua', 'acucar', 'cafe', 'canela']
print(minhaLista)
#agua esta na posicao 1
#acucar esta na posicao 2
#slicing --> [posicao inicial:posicao final + 1:pulo/incremento ]
pequenaLista = minhaLista[1:3] 
print(pequenaLista)
pequenaLista = minhaLista[1:5:2] 
print(pequenaLista)
#agua esta na posicao -4
#acucar esta na posicao -3
pequenaLista = minhaLista[-4:-2]
print(pequenaLista)
pequenaLista = minhaLista[-2:-4]
print(pequenaLista)
pequenaLista = minhaLista[-2:-4:-1]
print(pequenaLista)
minhaListaInversa = minhaLista[-1:-6:-1]
print(minhaListaInversa)
minhaListaInversa = minhaLista[::-1]
print(minhaListaInversa)

palavra = 'JOCA'
print(f'original:{palavra} inversa:{palavra[::-1]}')

print('\n\nAcresentando Elementos')
minhaLista= ['cafe', 'agua', 'acucar', 'cafe', 'canela']
print(minhaLista)
print('Acrescenta no final com append')
minhaLista.append('pimenta')
print(minhaLista)
print('Acrescenta elemento numa posicao especifica - 3')
minhaLista.insert(3,'nibs de cacau')
print(minhaLista)

print('\n\nEliminando Elementos')
minhaLista= ['cafe', 'agua', 'acucar', 'nibs de cacau', 'cafe', 'canela', 'pimenta']
print(minhaLista)
print('Eliminando o ultimo elemento')
minhaLista.pop()
print(minhaLista)
print('Eliminando um elemento especifico - 3')
minhaLista.pop(3)
print(minhaLista)
print('Eliminando o ultimo elemento com del')
del minhaLista[-1]
print(minhaLista)
print('Eliminando um elemento pelo nome')
minhaLista.remove('acucar')
print(minhaLista)

print('Eliminando todos elementos')
minhaLista.clear()
print(minhaLista)
print('Apagando a Lista')
del minhaLista

print('\n\nConstrutores de Lista')
outraLista = []
print(outraLista)

outraLista = list(('chantilly', 'baunilha'))
print(outraLista)

print('\n\nExtender a Lista')
complementoLista = ['raspas limao', 'flor de sal']
print(complementoLista)
outraLista.extend(complementoLista)
print(outraLista)

print('\n\nCriando uma nova lista a partir de duas listas')
print(pequenaLista)
novaLista = pequenaLista + complementoLista
print(novaLista)

print('\n\nPosicao de um determinado elemento')
onde = novaLista.index('raspas limao')
print(f'Raspas de Limao esta na posicao {onde}')

if 'flor de sal' in outraLista:
  print('Flor de sal presente')

print('\n\nListas sao ordenaveis se os elementos forem do mesmo tipo')
print(novaLista)
novaLista.sort()
print(novaLista)

#Estudo de ordenacao
print('\n\n\nEstudo ordenacao')
minhaLista= ['cafe', 'agua', 'acucar', 'mexirica', 'canela', 'pimenta']
print('original')
print(minhaLista)
print('ordenada com sorted')
print(sorted(minhaLista))
print('depois de ordenada')
print(minhaLista)

print('\n\n\n')
minhaLista= ['cafe', 'agua', 'acucar', 'mexirica', 'canela', 'pimenta']
print('original')
print(minhaLista)
print('ordenada com o metodo sort')
minhaLista.sort()
print(minhaLista)
print('depois de ordenada')
print(minhaLista)
print('reversa')
minhaLista.sort(reverse=True)
print(minhaLista)

print('\n\nLista com tipos de dados diferentes')
listaTiposDadosDiferentes = ['Giovanni', 'Maria Julia', 12, 30, True, ['Puppy', 'Mel']]
print(listaTiposDadosDiferentes)

#listaTiposDadosDiferentes.sort()
#print(sorted(listaTiposDadosDiferentes))
print('Listas COM TIPOS DIFERENTES NAO SAO ORDENAVEIS')

print('\n\nVarrendo elemento a elemento da lista')
for elemento in minhaLista:
  print(elemento)
print('\n')
for item in listaTiposDadosDiferentes:
  print(item)

print('\n\nTipo e tamanho da lista')
print(type(listaTiposDadosDiferentes))
print(len(listaTiposDadosDiferentes))

#Exercicios
# Acabou a pandemia, chegou o dia e você está ajudando a montar a lista de uma pequena reunião no seu apartamento. Conversando com o seu síndico ele proibiu que houvesse mais de 15 pessoas no seu apartamento. Faça um algorimo que peça a quantidade de pessoas da sua reunião. E utilizando a função FOR peça o nome dos convidados um a um. Certifique-se que seu melhor amigo João está na sua lista

# Você vai precisar dos nomes em ordem alfabética para poder enviar a portaria. Altere se algoritmo e ordene a sua lista. Depois apresente o resultado

titulo = 'Reuniao pos pandemia'
print(f'{titulo:^30}')
qtde_max_pessoas = 15
qtde_anfitrioes = 3 #eu, marido, filha
qtde_convidados = int(input('Entre com a qtde de convidados: '))

listaConvidados = []
if qtde_convidados > qtde_max_pessoas - qtde_anfitrioes:
  print('O sindico proibiu mais de 15 pessoas na reuniao')
else:
  for i in range(qtde_convidados):
    nome = input(f'Entre com o nome do {i+1}o convidado: ')
    listaConvidados.append(nome)

  if 'João' in listaConvidados:
    print('o João já está na lista de convidados')
  else:
    if qtde_convidados + 1 <= qtde_max_pessoas - qtde_anfitrioes:
      resp = input('Você quer acrescentar o João?').lower()
      if resp in ('s', 'sim', 'y', 'yes'):
        listaConvidados.append('João')
        print('o João foi acrescentado na lista de convidados')
  print(listaConvidados)
  # print(1, listaConvidados)
  # print(2, sorted(listaConvidados))
  # listaConvidadosOrdem = sorted(listaConvidados)
  # print(3, listaConvidados)
  # print(4, listaConvidadosOrdem)

  listaConvidados.sort()
  print(listaConvidados)

# # #Ana Julia
# # print(lista_convidados)

# # lista_convidados_organizada = sorted(lista_convidados)

#Falando com a portaria, foi pedido que adicionasse o número do RG em frente cada um dos nomes dos convidados. Altere seu algoritmo para colocar esses documentos na ordem solicitada. Exemplo ['Pat', 345453, 'Hamilton', 924504]

listaConvidadosRG = []
for nome in listaConvidados:
  rg = int(input(f'Entre com o RG do {nome}:'))
  listaConvidadosRG.append(nome)
  listaConvidadosRG.append(rg)

# listaConvidados = listaConvidadosRG
# del listaConvidadosRG
print(listaConvidadosRG)

#Ana Julia
# lista_convidados = []
# qtde_convidados = 2
# for i in range(qtde_convidados):
#     nome = input(f'Entre com o nome do {i+1}o convidado: ')
#     rg = input(f'Entre com o RG do {nome}: ')
#     lista_convidados.append((nome, rg))
# print(lista_convidados)

# titulo = 'Reunião pós pandemia'
# print(f'{titulo:^30}')
# qtde_max_pessoas = 15
# qtde_anfitrioes = 3 
# lista_convidados = []
# qtde_convidados = int(input('Entre com a quantidade de convidados: '))
# if qtde_convidados  > qtde_max_pessoas - qtde_anfitrioes:
#  print ('O síndico proibiu mais de 15 pessoas na reunião.')
# else:
#  for i in range(qtde_convidados):
#     nome = input(f'Entre com o nome do {i+1}o convidado: ')
#     rg = input(f'Entre com o RG do {nome}: ')
#     lista_convidados.append([nome, rg])
# print(lista_convidados)

#lista []
#tupla ()
#dicionario {}

#Você percebeu que esse primeira reunião vai passar de 20 pessoas e você alugou o salão de festas do seu condomíno. Sendo assim você vai precisar alterar seu algoritmo e agora não vai mais utilizar o comando FOR, vai utilizar o comando WHILE e enquanto a resposta da pergunta “Tem mais convidados” for igual a SIM você cadastrará um novo amigo na sua lista.

titulo = 'Reuniao pos pandemia WHILE'
print(f'{titulo:^30}')

listaConvidados = []
resp = 's'
i = 1
while resp in ('s', 'sim'):
    nome = input(f'Entre com o nome do {i}o convidado: ')
    listaConvidados.append(nome)
    rg = int(input(f'Entre com o rg do {nome}: '))
    listaConvidados.append(rg)
    i += 1
    resp = input('Quer cadastrar um novo convidado? ').lower()

if 'João' in listaConvidados:
  print('o João já está na lista de convidados')
else:
  resp = input('Você quer acrescentar o João? ').lower()
  if resp in ('s', 'sim', 'y', 'yes'):
    listaConvidados.append('João')
    listaConvidados.append(int(input(f'Entre com o rg do João:')))
    print('o João foi acrescentado na lista de convidados')
print(listaConvidados)
  # listaConvidados.sort()
  # print(listaConvidados)

# A cada dia mais perto da sua festa, alguns amigos ainda estão meio noiados com a transmissão do virus (e não é para menos com tantas variantes de depois de tantos mortos).
# Seu amigo João é um deles. Infelizmente ele pediu para ser retirado da lista. Remova o João a Lista

if 'João' in listaConvidados:
  ondeJoao = listaConvidados.index('João')
  print(ondeJoao)
  #eliminando o rg do João
  listaConvidados.pop(ondeJoao + 1)
  listaConvidados.remove('João')
  print(listaConvidados)

