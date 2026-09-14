media_aprovacao = 7
nome = input("Qual o seu nome? \n")
def media_final():
    print("Calculo da média")
    nota1 = int(input("Digite a nota do primeiro bimestre: "))
    nota2 = int(input("Digite a nota do segundo bimestre: "))
    nota3 = int(input("Digite a nota do terceiro bimeste: "))
    nota4 = int(input("Digite a nota do quarto bimestre: "))
    print (f"As notas desse aluno foram: {nota1, nota2, nota3, nota4}")
    return (nota1 + nota2 + nota3 + nota4)/4

resultado = media_final()

print(f"A média final do aluno {nome} foi de: ", resultado)

if resultado > media_aprovacao:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")


