nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
frequencia = int(input("Digite a porcentagem de presença:"))

media = (nota1 + nota2) / 2


print("Sua média foi:", media)
print(media >= 6 and frequencia >= 75)