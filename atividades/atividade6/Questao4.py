
opcao = 0
while True:
    opcao = int(input("Digite a sua opção: \n"
                      "1 - Mostrar saudação \n"
                      "2 - Sair do prgrama \n"
                      ))
    match opcao:
        case 1:
            print("Olá, seja muito bem vindo(a)!")
        case 2:
            print("Programa encerrado!")
            break
        case _:
            print("Opção inválida!")
            break