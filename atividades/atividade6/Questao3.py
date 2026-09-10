soma = 0

while True:
    numero = int(input("digite um numero: "))
    if numero != 0:
        soma += numero

    elif numero == 0:
        break

print("A soma dos números digitados é: ", soma)