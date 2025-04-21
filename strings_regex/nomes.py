'''
Ajude Victor a criar um programa que receba um nome de produto e o padronize,
 deixando todas as letras minúsculas e removendo os espaços extras.
'''
nome_produto = input("Digite o nome do produto: ")
produto_padronizado = nome_produto.strip().lower()
print(produto_padronizado)