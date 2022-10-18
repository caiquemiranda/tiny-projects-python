from random import randint

numero_secreto = randint(0, 10)
total_tentativas = 5

while total_tentativas > 0 :
    print('Pensei em um numero, tente adivinhar! ')
    chute = int(input(f'Vou te dar {total_tentativas} chances, digite um numero: '))
    print('Voce digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Voce acertou! ')
        break

    elif maior:
        print('Pensei em um numero menor, tente de novo')
        print(f'Voce tem mais {total_tentativas - 1} tentativas!')

    elif menor:
        print('Pensei em um numero maior, tente de novo')
        print(f'Voce tem mais {total_tentativas - 1} tentativas!')

    total_tentativas -= 1

print(f'Eu pensei no numero : {numero_secreto}')
print('Tente de novo o jogo!')