selecao = input("Selecione seu produto: \n"
          "Código        Produto          Preço\n"
          "  1       Cachorro quente       R$10,00 \n "
          "  2          Hambúrger          R$15,00 \n "
          "  3         Batata frita        R$8,00 \n "
          "  4         Refrigerante        R$5,00 \n ")

match selecao:
    case '1':
        print("Cachoro quente")
    case '2':
        print("Hambúrger")
    case '3':
        print("Batata frita")
    case '4':
        print("Refrigerante")
    case _:
        print("Código invalido")