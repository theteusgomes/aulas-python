

def media_notas(nota1, nota2, nota3):
   return (nota1 + nota2 + nota3)/3

print("Calculo da média")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = media_notas(nota1, nota2, nota3)

print(f"A média foi de: {media:.2f}")