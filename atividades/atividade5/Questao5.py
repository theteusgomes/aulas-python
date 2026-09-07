numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite o segundo numero inteiro: "))

operacao = input("Selecione o operador que deseja utilizar: (+ - / *) ")

match operacao:
    case "+":
        print("A soma dos seus números é: ", numero1 + numero1)
    case "-":
        print("A subtração dos seus números é: ", numero1 - numero1)
    case "/":
        print("A divisão dos seus números é: ", numero1 / numero1)
    case "*":
        print("A multiplicação dos seus números é: ", numero1 * numero1)
    case _:
        print("Operação inválida")
