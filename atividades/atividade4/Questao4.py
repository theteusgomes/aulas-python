saldo_atual = 500
saque = int(input("Quanto deseja sacar?"))

if saque <= saldo_atual:
    saldo_final = saque - saldo_atual
    print("Saque realizado com sucesso! Seu saldo agora é de:", saldo_final )
else:
    print("Saldo insuficiente para essa operação")


