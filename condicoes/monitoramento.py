'''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
Ele registrou a quantidade vendida de dois produtos: 
maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
Crie um programa que receba o número de vendas dos dois produtos 
e exiba uma mensagem indicando qual deles vendeu mais. 
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
'''


maças = int(input("Digite o numero de maças vendidas: "))
bananas = int(input("Digite o numero de bananas vendidas: "))
if maças > bananas:
    print("As maças tiveram mais vendas")
elif bananas > maças:
    print("As bananas tiveram mais vendas")
else:
    print("Ambas tiveram o mesmo numero de vendas")