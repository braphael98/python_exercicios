'''
crie um programa que receba um texto com uma descrição e exiba uma mensagem com o número encontrado.
'''
import re

descricao = input("Digite a descrição da receita: ")
numero = re.findall(r'\d+',descricao)[0]
print(f"o numero da receita é : {numero}")


