tabela = ['_','_','_',
          '_','_','_',
          '_','_','_']

print('Olá, seja bem vindo ao jogo da velha!!\n')
print('Como jogar:\n')
print('Escolha com seu amigo qual você vai ser, sendo o jogador 1 "X" e o jogador 2 "O"')

def desenhar_tabela(vetor_da_velha):
    jogoDaVelha = ''
    for i in range(len(vetor_da_velha)):
        if(i == 2 or i == 5 or i == 8):
            jogoDaVelha += " " + vetor_da_velha[i] + " \n"
        else :
            jogoDaVelha += " " + vetor_da_velha[i] + " |"
    return jogoDaVelha

def verificar_tabela(vetor_da_velha, posicao):
    resultado = False
    if(vetor_da_velha[posicao] == '_'):
        resultado = True
    return resultado

def verificar_vitoria(vetor_da_velha,simbolo):
    resultado = False
    # Linha
    if(vetor_da_velha[0] == simbolo and vetor_da_velha[1] == simbolo and vetor_da_velha[2] == simbolo):
        resultado = True
    elif(vetor_da_velha[3] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[5] == simbolo):
        resultado = True
    elif(vetor_da_velha[6] == simbolo and vetor_da_velha[7] == simbolo and vetor_da_velha[8] == simbolo):
        resultado = True
    # Coluna
    elif(vetor_da_velha[0] == simbolo and vetor_da_velha[3] == simbolo and vetor_da_velha[6] == simbolo):
        resultado = True
    elif(vetor_da_velha[1] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[7] == simbolo):
        resultado = True
    elif(vetor_da_velha[2] == simbolo and vetor_da_velha[5] == simbolo and vetor_da_velha[8] == simbolo):
        resultado = True
    # Vertical
    elif(vetor_da_velha[0] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[8] == simbolo):
        resultado = True
    elif(vetor_da_velha[6] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[2] == simbolo):
        resultado = True
    return resultado

# verificar o empate
def verificar_empate(vetor_da_velha):
    resultado = True
    for i in vetor_da_velha:
        if(i == '_'):
            resultado = False
    return resultado

# Variaveis do jogo
jogador = 1
jogador_numero_1 = 0
jogador_numero_2 = 0

while(True):
    # verifica se é a vez do jogador 1
    if(jogador == 1):
        jogador_numero_1 = input('Jogador 1 Digite uma posição de 1 a 9 : ')
        if(verificar_tabela(tabela,int(jogador_numero_1)-1)):
            tabela[int(jogador_numero_1)-1] = 'X'
            jogador = 2
            print(desenhar_tabela(tabela))
        else :
            print(desenhar_tabela(tabela))
            print('Posicao ja ocupada')
    if(verificar_vitoria(tabela,'X')):
        print('Jogador numero 1 ganhou. Parabéns!!!')
        break
    if(verificar_empate(tabela)):
        print('Empate')
        break

    # verifica se é a vez do jogador 2
    if(jogador == 2):
        jogador_numero_2 = input('Jogador 2 Digite uma posição de 1 a 9 : ')
        if(verificar_tabela(tabela,int(jogador_numero_2)-1)):
            tabela[int(jogador_numero_2)-1] = 'O'
            jogador = 1
            print(desenhar_tabela(tabela))
        else :
            print(desenhar_tabela(tabela))
            print('Posicao ja ocupada')
    if(verificar_vitoria(tabela,'O')):
        print('Jogador numero 2 ganhou. Parabéns!!!')
        break
    if(verificar_empate(tabela)):
        print('Empate')
        break