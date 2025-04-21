'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
'''

temperatura = float(input("Digite a temperatura da sala: "))

if temperatura > 25:
    print("Alerta! Temperatura acima do esperado")
else:
    print("Temperatura normal")