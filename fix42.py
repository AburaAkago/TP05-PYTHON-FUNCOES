import os, statistics

os.system("cls")

nome_aluno = str(input("Digite seu nome: "))
ra_aluno = str(input("Digite seu RA: "))
np = [float(input("Digite a nota da 1ª prova: ")), float(input("Digite a nota da 2ª prova: "))]

media = statistics.mean(np)

if (media >= 7 or media <= 10):
    print(f"Parabéns {nome_aluno}, você foi aprovado!")
elif (media <= 6 or media >= 1):
    print(f"Você ainda tem chance {nome_aluno}! Estude mais para o exame.")
else:
    print("Valor invalido")