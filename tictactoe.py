
print('')
print('''LET'S PLAY TIC TAC TOE
INSTRUCTIONS: 
1) YOU HAVE TO CHOOSE A NUMBER BETWEEN 1 TO 9 WHERE 1 | 2 | 3 
                                                    4 | 5 | 6
                                                    7 | 8 | 9''')

def main():
    board = ['_','_','_','_','_','_','_','_','_']
    run = True
    play1 = 'X'
    play2 = 'O'

    def draw_board():  
        b = 1
        for i in board:
            if b % 3 != 0:
                print(i ,end=' | ')
            elif b % 3 == 0:
                print(i, end=' ')
                print('')
            b+=1

    def condition(value):
        global run
        if board[0] == board[3] and board[0] == board[6]and board[0]and board[3] and board[6]!='_':
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[1] == board[4] and board[1] == board[7]and board[1]and board[4]and board[7]!="_":
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[2] == board[5] and board[2] == board[8]and board[2]and board[5]and board[2]!='_':
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[0] == board[1] and board[0] == board[2]and board[1]and board[2]and board[0]!="_":
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[3] == board[4] and board[3] == board[5]and board[3]and board[4]and board[5]!="_":
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[6] == board[7] and board[6] == board[8]and board[6]and board[8]and board[7]!="_":
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[0] == board[4] and board[0] == board[8]and board[0]and board[4]and board[8]!="_":
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[2] == board[4] and board[2] == board[6]and board[6]and board[4]and board[2]!="_":
            print(f'{value} WINS!')
            print('')
            draw_board()
            run = False
        elif board[0]!="_"and board[1]!="_"and board[2]!="_"and board[3]!="_"and board[4]!="_"and board[5]!="_"and board[6]!="_"and board[7]!="_"and board[8]!="_":
            print("DRAW MATCH!")
            print('')
            draw_board()
            run = False

    def play(value):
        def player_value():
            if value == play1:
                play(play1)
            if value == play2:
                play(play2)
        print(f'ITS {value} TURN')
        print('')
        draw_board()
        print('')
        inp = input('PLEASE CHOOSE A NUMBER FROM 1 TO 9 (press y to quit): ')  
        print('') 
        if inp == 'y':
            quit()
 
        elif 1<=int(inp)<=9: 
            if board[int(inp)-1] == play1 or board[int(inp) -1] == play2:
                print('THIS PLACE IS ALREADY TAKEN!')
                print('')
                player_value()
            else:    
                board[int(inp)-1] = value

        else:
            print('INVALID INPUT!')
            print('')
            player_value()     
          
    def gameplay():
        global run
        run = True
        while run == True:
            play(play1)
            condition(play1)
            if run == False:
                break
            play(play2)
            condition(play2)
            if run == False:
                break
            
    def start():
        global run
        if run == False:
            print('')
            again = input('DO YOU WANT TO PLAY AGAIN(y/n): ')
            print('')
            if again == 'y':
                run = True
                main()
            else:
                quit()
    
    gameplay()
    while True:
        start()
        
main()

