'''
Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. 
O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" 
a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
'''

quantidade = 5

while quantidade > 0:
    print(f"Estoque restante: {quantidade}")
    
    quantidade -= 1
    if quantidade == 0:
        print("Estoque vazio! ")