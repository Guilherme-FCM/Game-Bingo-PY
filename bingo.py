#gerar a cartela
import random, time

def printao(v, espacos = 0):
    print('~'*(len(v) + 4))
    print(f'  {v}')
    print('~'*(len(v) + 4))

def gerar_numero(lista):
    x = random.choice(lista)
    lista.remove(x)
    return(x)

def gerar_cartela(numeros):
    copia = numeros[:]
    cartela = [[],[],[],[],[]]
    lista = []
    z = len(copia) / 5
    cont = 0
    for x in copia:
        lista.append(x)
        cont += 1
        if cont == z:
            for y in cartela:
                y.append(gerar_numero(lista)) 
            z += len(copia) / 5
            lista = []
    cartela[2][2] = '><'
    return(cartela)

def print_cartela(cartela, jogador):
    string = 'Cartela Do(a) ' + str(jogador)
    espacos = 27 - len(string)
    if espacos <= 0:
        espacos = 0
    else:
        if espacos % 2 == 0:
            espacos = espacos / 2
        else: espacos = (espacos - 1) / 2
        espacos = int(espacos)
    espacos = ' ' * espacos
    print('\n'+espacos + string+'\n')
    letras = ['B','I','N','G','O']
    c = 1
    for x in letras:
        print(f'    {x}', end='')
    print(' ')
    for x in cartela:
        print(f'{c}  ',end='')
        c += 1
        for y in x:
            print(f'[{y}]', end=' ') 
        print(' ')
    
def processar_maquina(aleatorio, cartela):
    for x in cartela:
        for y in x:
            if y == aleatorio:
                x[x.index(y)] = '><'

def analisar_posicao(posicao):
    colunas = {
        'B':0,
        'I':1,
        'N':2,
        'G':3,
        'O':4,
    }
    posicao = posicao.split(',')
    if posicao[0].upper() in 'BINGO':
        for k,i in colunas.items():
            if k == posicao[0].upper():
                posicao[0] = i
                break
        if posicao[1] in '12345' or posicao[1] == '':
            posicao[1] = (int(posicao[1]) - 1)
        else: return(False)
    else: return(False)
    return(posicao)

def vitoria(cartela):
    for x in cartela:
        for y in x:
            if y != '><':
                return(False)
    return(True)            
    

#Código Principal    
numeros = []
for x in range(1,51):
    if x < 10:
        x=str(x)
        x = '0'+ x
    numeros.append(x)
jogador = input('Nome do Jogador: ')
cartela_jogador = gerar_cartela(numeros)
cartela_maquina = gerar_cartela(numeros)

#executar game / print('[><]')
bingo = False
while bingo == False:
    print_cartela(cartela_maquina, 'Máquina')
    print_cartela(cartela_jogador, jogador)
    bingo = vitoria(cartela_jogador)
    if bingo:
        printao('BINGO! VOCÊ VENCEU!')
        break
    bingo = vitoria(cartela_maquina)
    if bingo:
        printao('GAME OVER')
        break
    aleatorio = gerar_numero(numeros)
    processar_maquina(aleatorio, cartela_maquina)
    print('\nSorteando um número...')
    time.sleep(2)
    print(f'\nNÚMERO SORTEADO: {aleatorio}\n')
    
    while True:
        resp = input('\nAchou o número na tabela? (S / N) ')
        if resp.lower() == 's':
            print('Escreva o primeiro valor para coluna e o segundo para linha')
            print('EX: G,4 ou I,2')
            resp_posicao = input('\nPosição: ')
            posicao = analisar_posicao(resp_posicao)
            if posicao != False:
                cartela_jogador[posicao[1]][posicao[0]] = '><'
                bingo = vitoria(cartela_jogador)
                if bingo:
                    printao('BINGO! VOCÊ VENCEU!')
                    break
                bingo = vitoria(cartela_maquina)
                if bingo:
                    printao('GAME OVER')
                    break
            else:
                print('Posição inválida! Tente novamente')
                continue
            break
        elif resp.lower() == 'n':
            print('\nTente na próxima rodada...')
            break
        else: 
            print('Valor invalido! Tente novamente.')