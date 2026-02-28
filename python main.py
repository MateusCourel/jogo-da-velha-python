from random import randrange

#Para colorir:
from colorama import init, Fore, Style
init() 


board = [
    
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    
]

def display_board(board):
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            
            #Para colorir o game (requisito não funcional)
            value = board[row][col]

            if value == "X":
                value = Fore.RED + "X" + Style.RESET_ALL
            elif value == "O":
                value = Fore.BLUE + "O" + Style.RESET_ALL

            
            print("|   " + str(value) + "   ", end="")     #aqui o original seria: print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")


def enter_move(board):
    while True:
        try:
            num = int(input("Digite o número da posição: "))
        except ValueError:
            print("Caracter inválido, tente novamente! ")
            continue

        if num < 1 or num > 9:
            print("Erro! Insira um valor disponível!")
            continue
        
        #Para descobrir agora em que posição está na matriz:
        lin = (num - 1)//3
        col = (num - 1)% 3
        if board[lin][col] in ["X", "O"]:
            print("Erro, posição inválida!")
            continue
        else:
            board[lin][col] = "O"
        break




def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                free.append((i, j))
    return free



def victory_for(board, sign):
    for i in range(3):
        #Para encontrar sequência nas linhas:
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign: 
            return True
        
        #Para encontrar sequência nas colunas:
        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    
    #Para encontrar sequência na 1ª diagnonal:
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    
    #Para encontrar sequência na 2ª diagnonal:
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    #Caso não encontre nenhuma sequência:
    return False
        

                                                                
def draw_move(board):
    free = make_list_of_free_fields(board)

    if free:   #segurança caso não tenha posições livres ---> mesma coisa que: if free > 0:
        #Usando o randrange():
        index = randrange(len(free))
        
        #Desempacotando a tupla:
        lin, col = free[index]

        #Colocando o "X" na posição escolhida pelo random
        board[lin][col] = "X"


#CÓDIGO PRINCIPAL:
board[1][1]  = "X"
while True:
    display_board(board)
    enter_move(board)
    
    if victory_for(board, "O") == True:
        display_board(board)
        print("Jogador venceu a partida!")
        break
    
    if not make_list_of_free_fields(board):    #isso é a mesma coisa que: if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Ninguém venceu! Empate!")
        break
    
    draw_move(board)
    
    if victory_for(board, "X") == True:
        display_board(board)
        print("Computador venceu a partida!")
        break
    
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Ninguém venceu! Empate!")
        break





