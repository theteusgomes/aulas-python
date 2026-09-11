soma = 0
while True:
    num_digitado = int(input("digite um número:"))
    if num_digitado != 0:
        soma = int(input("digite um outro número:"))
        soma += num_digitado

    else _:
        print(soma)
        break