# Cifra de César 
import time

print('    CODIFICAÇÃO   CIFRA   DE   CÉSAR    ')
print('-=' * 20)
frase = input('Digite uma frase e escolha a ação\n')
print('-=' * 20)
acao = input('[ 1 ] CRIPTOGRAFAR\n[ 2 ] DESCRIPTOGRAFAR\n')
print('-=' * 20)

if acao == '1' or acao == '2':
    salto = int(input('Qual a chave de codificação? '))
    print('-=' * 20)
    print('Processando.', end='\r')
    time.sleep(1)
    print('Processando..', end='\r')
    time.sleep(1)
    print('Processando...', end='\r')
    time.sleep(1)
    print('Processando....')

if acao == '1':
    for letra in frase:
        if letra.isalpha():
            letra_num = ord('a') + (ord(letra.lower()) - ord('a') + salto) % 26
            letra = chr(letra_num)
        elif letra.isnumeric():
            letra_num = ord('0') + (ord(letra.lower()) - ord('0') + salto) % 10
            letra = chr(letra_num)
        print(letra, end='')
elif acao == '2':
    for letra in frase:
        if letra.isalpha():
            letra_num = ord('a') + (ord(letra.lower()) - ord('a') - salto) % 26
            letra = chr(letra_num)
        elif letra.isnumeric():
            letra_num = ord('0') + (ord(letra.lower()) - ord('0') - salto) % 10
            letra = chr(letra_num)
        print(letra,end='')
else:
    print('Digite uma opção válida!', end='') 
print('\n', '-=' * 20, sep='')