# Temporizador decrescente: Crie um algoritmo que simule um temporizador decrescente. Peça os minutos e imprima um relógio de minutos e segundos. Utilize o FOR. Repita o exerício usando o WHILE

minutos = int(input("quantidade de minutos para o temporizador "))
horario = minutos * 60
for i in range(horario, -1, -1):
    min = i // 60  
    seg = i % 60  
    print(f"{min:02d}:{seg:02d}")
