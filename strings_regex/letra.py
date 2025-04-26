import re

titulo = input("Digite o nome do livro: ")
letra = input("Digite a letra inicial para pesquisa: ")

palavras = re.findall(rf'\b{letra}[a-zá-ÿ]*',titulo,re.IGNORECASE)
print(palavras)


