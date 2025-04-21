'''
Crie um programa que utilize um laço for para exibir as seguintes mensagens:

    Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
    Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
    Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
'''

for segundos in range(10,0,-1):    
    if segundos % 2 == 0:
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua {segundos} segundos")
print("Aproveite a promoção!")