'''
Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.
O padrão esperado é 
que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais).
'''
import re

nome = input("Digite seu nome: ")
if re.fullmatch(r'[A-Z][a-z]*',nome):
    print(f"Nome valido {nome}")
else:
    print("Nome invalido")