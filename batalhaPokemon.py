treinador1 = input("Escreva o nome do primeiro treinador Pokémon: ")
bonus1 = int(input("Informe o valor do bônus: "))
ataque1 = int(input("Informe o valor do ataque: "))
defesa1 = int(input("Informe o valor da defesa: "))

treinador2 = input("Escreva o nome do segundo treinador Pokémon: ")
bonus2 = int(input("Informe o valor do bônus: "))
ataque2 = int(input("Informe o valor do ataque: "))
defesa2 = int(input("Informe o valor da defesa: "))

'''def vencedorBatalha(ataque, defesa, bonus):
    if 0 > bonus > 100 or 1 > ataque > 100 or 1 > defesa > 100:
        print("O valor informado é inválido. É necessário que o bônus seja um número de 0 a 100 e ataque e defesa números de 1 a 100")
    else:
        valorGolpe = ((ataque + defesa)/2) + bonus

valorTreinador1 = vencedorBatalha(ataque1, defesa1, bonus1)
valorTreinador2 = vencedorBatalha(ataque2, defesa2, bonus2)'''

valorGolpeTreinador1 = ((ataque1 + defesa1)/2) + bonus1
valorGolpeTreinador2 = ((ataque2 + defesa2)/2) + bonus2

if valorGolpeTreinador1 > valorGolpeTreinador2:
    print("O vencedor dessa batalha foi: ", treinador1)
elif valorGolpeTreinador1 == valorGolpeTreinador2:
    print("Empate entre os treinadores.")
else:
    print("O vencedor dessa batalha foi: ", treinador2)