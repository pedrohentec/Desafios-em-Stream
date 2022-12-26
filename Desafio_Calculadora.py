## Calculadora
while True:
    try:
        # Faça um programa que peça ao usuário um número
        numero1_usuario = input('Digite um número: ')
        # logo em seguida o número novamente
        numero2_usuario = input('Digite outro número: ')
        numero1_usuario = numero1_usuario.replace(',', '.') 
        numero2_usuario = numero2_usuario.replace(',', '.')
        numero1_usuario_float = float(numero1_usuario)
        numero2_usuario_float = float(numero2_usuario)
        #  logo em seguida, peça a ele à operação matemática que ele deseja fazer
        print('Qual operação deseja fazer?')
        print('------------------------------------------')
        print(f'soma\nsubtração\ndivisão\nmultiplicação\n')
        print('------------------------------------------')
        operacao = input('').lower()
        # Apos ter em mãos as informações que e necessárias, faça o cálculo
        if operacao == 'soma':
            resultado = (numero1_usuario_float) + (numero2_usuario_float)
            print(str(resultado).replace('.', ','))
        elif operacao == 'substração':
            resultado = (numero1_usuario_float) - (numero2_usuario_float)
            print(str(resultado).replace('.', ','))
        elif operacao == 'divisão':
            resultado = (numero1_usuario_float) / (numero2_usuario_float)
            print(str(resultado).replace('.', ','))
        elif operacao == 'multiplicação':
            resultado = (numero1_usuario_float) * (numero2_usuario_float)
        else:
            print('Comando inválido!')
        reiniciar = input('Deseja recomençar ? [S/N]').upper()
        if reiniciar == 'S':
            True
        else:
            break
    except ValueError:
        print('Número inválido')
    except ZeroDivisionError:
        print('∞')
    except Exception as e:
        print(f'Erro {e}')

