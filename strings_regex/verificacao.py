'''
 programa que peça ao usuário uma URL e informe se ela é válida ou inválida?
'''
url = input('Digite a url: ')

if url.startswith("https//") and url.endswith(".com"):
    print("URL VALIDA")
else:
    print("URL INVALIDADA")

