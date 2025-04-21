while True:
    usuario = input("Digite seu nome: ")
    senha = (input("Digite a senha: "))
    if len(usuario) < 5:
        print("O nome de usuario deve ter no minimo 5")
        continue
    if len(senha) < 8:
        print("A senha deve ter no minimo 8 caracteres")
        continue
    print("Cadastro realizado com sucesso")
    break