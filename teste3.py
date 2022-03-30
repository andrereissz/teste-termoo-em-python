import os
import colorama
from colorama import Fore, Back


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


reset = Fore.RESET+Back.RESET
senha = ['t','o','r','a','s']
junta = ''.join(senha)
while True:
    clearConsole()
    senha = list(junta)
    erro = 0
    palavra = str(input('Digite a palavra de 5 letras: ')).lower().strip()
    tentativa = list(palavra)
    for n in (tentativa):
        if n.isdigit() == True:
            input('Numero digitado tente novamente\nAperte enter para retornar...')
            erro = 1
            break
    if erro == 1:
        continue
    if len(palavra) != 5:
        input('Palavra invalida tente novamente\nAperte enter para retornar...')
        continue
    else:
        for n in range(0,5):
            if tentativa[n] == senha[n]:
                print(f'{Fore.WHITE+Back.GREEN} {tentativa[n]} {reset}', end = ' ')
                senha[n] = '9'
            elif tentativa[n] in senha:
                print(f'{Fore.WHITE+Back.BLUE} {tentativa[n]} {reset}', end = ' ')
            else:
                print(f'{Fore.BLACK+Back.WHITE} {tentativa[n]} {reset}', end = ' ')
    if palavra == junta:
        print(f'\nVOCE ACERTOU A PALAVRA ERA: {junta}!')
        input('Aperte enter para finalizar...')
        break
    input('\nTente novamente...')
clearConsole()
