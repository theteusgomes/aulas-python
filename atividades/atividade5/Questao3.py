turno = input("Selecione seu turno com a letra inicial dele: ")

match turno:
    case "M" | "m":
        print("Bom dia!")
    case "V" | "v":
        print("Boa tarde!")
    case "N" | "n":
        print("Boa noite!")
    case _:
        print("Turno invalido!")