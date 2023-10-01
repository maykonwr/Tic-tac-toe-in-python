table = ['_','_','_',
          '_','_','_',
          '_','_','_']

print('Olá, seja bem vindo ao jogo da velha!!\n')
print('Como jogar:\n')
print('Escolha com seu amigo qual você vai ser, sendo o jogador 1 "X" e o jogador 2 "O"')

def draw_table(old_vector):
    ticTacToe = ''
    for i in range(len(old_vector)):
        if(i == 2 or i == 5 or i == 8):
            ticTacToe += " " + old_vector[i] + " \n"
        else :
            ticTacToe += " " + old_vector[i] + " |"
    return ticTacToe

def check_table(old_vector, position):
    result = False
    if(old_vector[position] == '_'):
        result = True
    return result

def check_victory(old_vector,symbol):
    result = False
    # Linhas
    if(old_vector[0] == symbol and old_vector[1] == symbol and old_vector[2] == symbol):
        result = True
    elif(old_vector[3] == symbol and old_vector[4] == symbol and old_vector[5] == symbol):
        result = True
    elif(old_vector[6] == symbol and old_vector[7] == symbol and old_vector[8] == symbol):
        result = True
    # Colunas
    elif(old_vector[0] == symbol and old_vector[3] == symbol and old_vector[6] == symbol):
        result = True
    elif(old_vector[1] == symbol and old_vector[4] == symbol and old_vector[7] == symbol):
        result = True
    elif(old_vector[2] == symbol and old_vector[5] == symbol and old_vector[8] == symbol):
        result = True
    # Vertical
    elif(old_vector[0] == symbol and old_vector[4] == symbol and old_vector[8] == symbol):
        result = True
    elif(old_vector[6] == symbol and old_vector[4] == symbol and old_vector[2] == symbol):
        result = True
    return result

# verificar o empate
def check_draw(old_vector):
    result = True
    for i in old_vector:
        if(i == '_'):
            result = False
    return result

# Variaveis do jogo
player = 1
player_number_1 = 0
player_number_2 = 0

while(True):
    # verifica se é a vez do jogador 1
    if(player == 1):
        player_number_1 = input('Jogador 1 Digite uma posição de 1 a 9 : ')
        if(check_table(table,int(player_number_1)-1)):
            table[int(player_number_1)-1] = 'X'
            player = 2
            print(draw_table(table))
        else :
            print(draw_table(table))
            print('Posicao ja ocupada')
    if(check_victory(table,'X')):
        print('Jogador numero 1 ganhou. Parabéns!!!')
        break
    if(check_draw(table)):
        print('Empate')
        break

    # verifica se é a vez do jogador 2
    if(player == 2):
        player_number_2 = input('Jogador 2 Digite uma posição de 1 a 9 : ')
        if(check_table(table,int(player_number_2)-1)):
            table[int(player_number_2)-1] = 'O'
            player = 1
            print(draw_table(table))
        else :
            print(draw_table(table))
            print('Posicao ja ocupada')
    if(check_victory(table,'O')):
        print('Jogador numero 2 ganhou. Parabéns!!!')
        break
    if(check_draw(table)):
        print('Empate')
        break