quantidade_dia = int(input("quantas macas foram colhidas hoje?"))

caixa_maca = 12

producao_caixa =  quantidade_dia / caixa_maca

resto = quantidade_dia % caixa_maca

print(producao_caixa)
print(resto)
