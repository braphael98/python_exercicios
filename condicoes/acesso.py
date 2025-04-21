'''
Mariana é responsável por liberar o acesso ao escritório
e precisa de um programa que verifique se os funcionários podem entrar.
Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. 
Crie um programa que receba a hora atual como entrada (em formato de 24 horas)
e exiba uma mensagem informando se o acesso é permitido ou negado.
'''
entrada = float(input("Digite a hora atual (Formato 24 horas): "))

if 8 <= entrada < 18:
    print("Acesso negado")
else:
    print("Acesso permitido")