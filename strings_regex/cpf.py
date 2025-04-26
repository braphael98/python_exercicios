'''
O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).

Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no formato correto. 
'''

import re

cpf = input("Informe o numero do cpf: ")

padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padrao,cpf):
    print("CPF VALIDO")
else:
    print("CPF INVALIDO")