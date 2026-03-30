usuario_cadastrado = "admin"
senha_cadastrada = "12345"

usuario_digitado = input("usuario: ")
senha_digitada = input("senha: ")
if usuario_cadastrado == usuario_digitado and senha_cadastrada == senha_digitada:
    print("seja bem vindo, agente!")
else:
    print("acesso negado")


