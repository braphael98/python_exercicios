'''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, 
ficaram de recuperação ou reprovados. As regras são:
    Média >= 7: Aprovado
    5 <= Média < 7: Recuperação
    Média < 5: Reprovado
'''
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")
