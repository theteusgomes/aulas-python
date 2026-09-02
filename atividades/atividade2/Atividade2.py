nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
plano_de_saude = str(input("Você tem plano de saude: "))

aceito = idade>=18 and idade >=65


print("Seu nome é:" , nome, ", você tem:", idade, "anos" , ", Tem plano?", plano_de_saude, aceito)


"""CRIE UM ALGORITMO, QUE FACA UM FORMULARIO EM QUE O USUARIO DIGITE SEU NOME
SUA IDADE E SE ELE TEM PLANO DE SAUDE TRUE OU FALSE

O SEU SISTEMA DEVE RETORNAR EM QUE UM UNICO PRINT(), TODAS AS INFORMACOES E
SE ELE FOR MENOR DE IDADE OU IDOSO OU SE NAO TIVER PLANO DE SAUDE, 
QUE ELE NAO SERA ACEITO NO NOSSO FORMULARIO.
"""