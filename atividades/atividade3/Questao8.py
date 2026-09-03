nome_produto = input("Qual o nome do seu produto?")
custo = int(input("Qual o custo do produto?"))
preco = int(input("Qual o preco oferecido em loja?"))

lucro = preco - custo

lucro_bom = lucro > 20

print("o", nome_produto, "tem te gerado o lucro de:", lucro, "um bom lucro?", lucro_bom)
