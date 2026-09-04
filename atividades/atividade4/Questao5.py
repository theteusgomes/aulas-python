idade = int(input("Digite sua idade: "))
vip = int(input("Você possui vip? Digite 1 para SIM e 0 para NÃO "))
organizador = int(input("Você faz parte da organização? Digite 1 para SIM e 0 para NÃO "))

if idade >= 18 and vip == 1 or organizador == 1:
    print("Você está autorizado")
else:
    print("Você não está autorizado")
