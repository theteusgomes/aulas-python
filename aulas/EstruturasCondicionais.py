#IF e ELSE -> SE e SENÃO

idade = 18

if idade >18: #só será executado se a resporta boleana for True
    print("Você pode entrar na balada.")
else: #executa se a resposta do IF for False
    print("Você não pode entrar na balada.")

#ELIF

idade = 10

if idade >18: #só será executado se a resporta boleana for True
    if idade >65:
    print("Desculpa senhor, voce nao pode entrar na balada.")
else: #executa se a resposta do IF for False e nao recebe conficao
    print("Você não pode entrar na balada.")
elif idade < 5:
    print("Alem de nao entrar, voce nao pode andar sozinho")

else:
    print("Não pode entrar, menor de idade")