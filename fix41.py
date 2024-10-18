import os, math

os.system('cls')
valor = int(input("Digite um número de 1 à 9: "))
if (valor == 1 or valor == 2 or valor ==3):
    valor = valor**2
    print(valor)
elif (valor == 4 or valor == 9):
    valor = math.sqrt(valor)
    print(valor)
elif (valor == 6 or valor == 7 or valor == 8):
    valor = valor / 9
    print(valor)