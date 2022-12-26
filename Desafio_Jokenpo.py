## Jokenpo
# Tratar o error caso usuário digite alguma coisa diferente dos três itens listado acima.
import random
# Faça um programa que peça ao usuário para escolher alguma das opções abaixo.
# - Pedra
# - Papel
# - Tesoura 
print('Escolha alguma das opções abaixo') 
print('--------------------------------')
a = 'Pedra'
b = 'Papel'
c = 'Tesoura'
lista = [a, b, c]
print(f'{a} {b} {c}')
while True:
    escolha_usuario = input('')
    if escolha_usuario not in ['Pedra', 'Papel', 'Tesoura']:
        print('Digite uma opção válida!')
        print('--------------------------------')
        print(f'{a} {b} {c}')
    else:
        break
print('--------------------------------')
# Com base na escolha do usuário, você deve escolher também um item aleatoriamente para competir com usuário
escolha_maquina = random.choice(lista)
# ápos todos terem escolhido, você deve informar quem foi o ganhador daquela rodada.
if escolha_usuario == escolha_maquina:
    print('Empate')
elif escolha_usuario != escolha_maquina:
    if escolha_maquina == a and escolha_usuario == b:
        print('Você ganhou!')
    elif escolha_maquina == b and escolha_usuario == c:
        print('Você ganhou!')
    elif escolha_maquina == c and escolha_usuario == a:
        print('Você ganhou!')
    else:
        print('Você perdeu!')