# desafio :
# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por exrtenso, de zero ate vinte
# o programa devera ler o numero pelo teclado(entre 0 e 20)
# e mostra-lo por extenso

numeros = "zero", "um", "dois", "tres",
"quatro", "cinco", "seis", "sete", "oito", "nove",
"dez", "onze", "doze", "treze", "quatorze", "quinze",
"dezesseis", "dezessete", "dezoito", "dezenove", "vinte"


while True:
    digite_num = int(input("Digite um numero de 0 e 20: "))
    if 0 <= digite_num <= 20:
        break
    print("tente novamente. ", end="")
print(f"voce digitou o numero {numeros[digite_num]}")
    