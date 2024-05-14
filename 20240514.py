#Tuplas
#Colecao imutavel, ou seja, uma vez criada não se pode alterar a tupla, nem acrescentar elementos, nem retirar, nem mudar

#Caracteristicas
#Imutaveis
#Indexadas - cada elemento tem uma posicao
#Permitem duplicados
#Permitem elemento de tipos de dados diferentes

print('Tuplas')
minhaTupla = ('sono', 'comida', 'sol', 'sono')
print(minhaTupla)
print(type(minhaTupla))
print(len(minhaTupla))

# --> direcao da esquerda para direita SOMAR 1
# <-- direcao da direita para esquerda RETIRAR 1
#    0       1        2      3
#   -4      -3       -2      -1
#('sono', 'comida', 'sol', 'sono')
print('Primeiro elemento positivo', minhaTupla[0])
print('Primeiro elemento negativo', minhaTupla[-4])

print('\n\nSlicing ou Fatiamento')
#comida, sol --> 1 e 2
minhaTuplinha = minhaTupla[1:2+1]
print(minhaTuplinha)
#comida, sol --> -3 e -2
minhaTuplinha = minhaTupla[-3:-2+1]
print(minhaTuplinha)
#se quiser invertido
minhaTuplinha = minhaTupla[-2:-3-1:-1]
print(minhaTuplinha)

#Tupla tem uma representacao diferente quando ela tem um elemento so
#Normalmente esperariamos assim
#minhaTuplaUmElemento = ('um elemento')
#mas nao acontece desse jeito
#o que acontece aqui é que temos uma string apenas
print('\n\nTupla de um elemento')
print('Falsa')
minhaTuplaUmElementoFalsiane = ('um elemento')
print(minhaTuplaUmElementoFalsiane)
print(type(minhaTuplaUmElementoFalsiane))

#na Tupla de um elemento verdadeira, precisamos colocar uma virgula depois do elemento
print('Verdadeira')
minhaTuplaUmElemento = ('um elemento',)
print(minhaTuplaUmElemento)
print(type(minhaTuplaUmElemento))

print('\n\nOrdenacao')
#sera que eu consigo ordenar uma tupla?
#minhaTupla.sort()
#nao consigo fazer o sort, mas porque
#porque a tupla é IMUTAVEL, ou seja, se eu tentar alterar a ordem dos elementos, estou querendo alterar a tupla, e ela nao permite
print('Gambiarra da Ordenacao')
minhaColecao = sorted(minhaTupla)
print(minhaColecao)
print(type(minhaColecao))
print('Transformo em lista com o sorted e converto para tupla com o tuple')
minhaTuplaOrdenada = tuple(sorted(minhaTupla))
print(minhaTuplaOrdenada)
print(type(minhaTuplaOrdenada))

print('\n\nTupla Vazia')
#sera que podemos criar uma tupla vazia?
tuplaVazia = ()
print(tuplaVazia)

tuplaVazia = tuple()
print(tuplaVazia)

#tem alguma vantagem? NAO! pq eu nao posso acrescentar nenhum elemento

#E como acrescentamos elementos?
print('\n\nAcrescentando elementos numa tupla - Gambiarra')

tuplaInicial = ()
print(tuplaInicial)
listaInicial = list(tuplaInicial)
listaInicial.append('Acrescentar um elemento')
print(listaInicial)
#sobrescrevendo a tupla inicial
tuplaInicial = tuple(listaInicial)
print(tuplaInicial)

print('Em menos passos')
tuplaInicial = ()
tuplaInicial = list(tuplaInicial)
tuplaInicial.append('elemento')
tuplaInicial = tuple(tuplaInicial)
print(tuplaInicial)

print('\n\n Indexacao em Tupla')
minhaTupla = ('sono', 'comida', 'sol', 'sono')
print(minhaTupla)
if 'sol' in minhaTupla:
  print(f'O sol está na posicao {minhaTupla.index("sol")}')

print('\n\nRemovendo Elementos da Tupla - Gambiarra')
minhaLista = list(minhaTupla)
print(minhaLista)
minhaLista.remove('comida')
print(minhaLista)
minhaTupla = tuple(minhaLista)
print(minhaTupla)

print('\n\nApagando a Tupla')
del minhaTupla


# Com esse grande evento você está planejando agora o cardápio. Você deve inicialmente
# montar uma lista de entradas para que sua irmã possa te ajudar. Monte uma lista com
# usando o WHILE com todas as delicias gourmets. Não se esqueça de colocar o queijo
# Roquefort.

listaDelicias = []
resp = 's'
#resp = True
while resp in ('s', 'sim', 'y'):
  comida = input('Entre com a entrada a ser servida na reunião: ')
  listaDelicias.append(comida)
  resp = input('Quer cadastrar mais uma entrada? ').lower()

if 'queijo roquefort' in listaDelicias:
  print('O queijo roquefort esta na lista')
else:
  listaDelicias.append('queijo roquefort')
print(listaDelicias)

# ▪ Sua irmã não quer providenciar mais nada e para não chateá-la você transformou essa lista
# em uma coleção imutável. Apresente a coleção

tuplaDelicias = tuple(listaDelicias)
del listaDelicias
print(tuplaDelicias)