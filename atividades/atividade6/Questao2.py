senha = "123456"
senha_digitada = input("digite a sua senha:")

while senha_digitada != senha:
    print ("Senha inválida. Tente novamente")
    senha_digitada = input("digite a sua senha:")

print("Acesso liberado.")