#aula de TUPLAS

#variaveis compostas tem 3 possibilidades 1.( TUPLAS ) / 2.[ listas ] / 3.{ dicionarios }
#TUPLA é uma variavel que guardam mais de um valor IMUTAVEIS
# as variaves sao compostas de de elementos diferentes(valores), que sao atribuidos automaticamente a indices(numeros)

lanche = ("hamburger", "suco","pizza", "pudim")
#range()
for cont in range(len(lanche)):
    print(f"eu vou comer {lanche[cont]}")

#direto na variavel composta
# for comida in lanche:
#     print(f"eu vou comer {comida}")
print("comi pra caramba")
