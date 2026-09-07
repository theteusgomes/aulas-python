"""CRIE UM ALGORITMO, QUE FACA UM FORMULARIO EM QUE O USUARIO DIGITE SEU NOME
SUA IDADE E SE ELE TEM PLANO DE SAUDE TRUE OU FALSE

O SEU SISTEMA DEVE RETORNAR EM QUE UM UNICO PRINT(), TODAS AS INFORMACOES E
SE ELE FOR MENOR DE IDADE OU IDOSO OU SE NAO TIVER PLANO DE SAUDE,
QUE ELE NAO SERA ACEITO NO NOSSO FORMULARIO.
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
plano_de_saude = input("Você possui plano de saúde?")

idade <=18 and idade > 65 and plano_de_saude == "sim"
print("Seu nome é:" , nome, ", você tem:", idade, "anos. Bem vindo! Você foi aceito em nosso formulário.")


idade >=17 and idade <=65 and plano_de_saude == "nao"
print("Seu nome é:" , nome, ", você tem:", idade, "anos. Bem vindo! Você foi recusado em nosso formulário.")



