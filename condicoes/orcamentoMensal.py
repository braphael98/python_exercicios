'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00,para seus gastos
e precisa de um programa que ajude a controlar suas despesas. 
O programa deve receber o total de despesas realizadas
e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
'''
despesas = float(input("Digite o total de despesas do mes (R$): "))
orcamento = 3000.00
if despesas > orcamento:
    print("ATENÇÃO !!!! VOCÊ ULTRAPASSOU O LIMITE DO ORÇAMENTO !")
else:
    print(f"Você gastou R$: {despesas} de R$ {orcamento}")