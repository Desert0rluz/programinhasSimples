#programa que faz palpites para megasena
from random import randint

lista = list()
sorte = list()

#painel inicial e imputs
print("-" * 30)
print("     MAQUINA DE PALPITES     ")
print("-" * 30)
jogos = int(input("Quantos jogos devem ser sorteados? "))
total = 1

#randomiza palpites
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort() #ordena os numeros
    sorte.append(lista[:])#coloca palpites na lista
    lista.clear()#limpa lista
    total += 1

#resultado final
print("=-" *3, f"GERANDO {jogos} PALPITES", "-=" *3)
for i, l in enumerate(sorte):
    print(f"palpite {i+1}: {l}")
print("=-" *4, "BOA SORTE! ", "-=" *4)
