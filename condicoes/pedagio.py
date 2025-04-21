'''
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. 
O valor do pedágio depende da distância percorrida:
    *Até 100 km: R$ 10,00
    *Entre 100 km e 200 km: R$ 20,00
    *Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
'''
distancia = float(input("Digite a distancia percorrida (em KM): "))
if distancia <= 100:
    print("Total a pagar R$ 10,00")
    
elif 100 < distancia <=200:
    print("Total a pagar R$ 20,00")
else:
    print("Total a pagar R$ 30,00")
