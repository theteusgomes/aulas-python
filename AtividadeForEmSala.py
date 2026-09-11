lista_funcionario = []
while True:
    funcionario = input("Digite o nome do funcionário: ")
    lista_funcionario.append(funcionario)

    sair = input("Fim da lista? [S/N]")
    if sair == "S" or "s":
        break

    for funcionario in lista_funcionario[1]:
        print(f"O {funcionario} receberá aumento no próximo mês.")

