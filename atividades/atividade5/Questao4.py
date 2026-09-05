mes = input("Digite o número do mês do ano de 1 à 12:")

match mes:
    case "12" | "1" | "2":
        print("Verão")
    case "3" | "4" | "5":
        print("Outono")
    case "6" | "7" | "8":
        print("Inverno")
    case "9" | "10" | "11":
        print("Primavera")
    case _:
        print("Mês inválido")

        