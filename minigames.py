import random
class minigames:
    def roll(self,rolling_time):
        begin = 0
        x_win_score = 0
        y_win_score = 0
        draw_times = 0
        while(begin < rolling_time):
            x = random.randint(1,7)
            y = random.randint(1,7)
            begin += 1
            if(x>y):
                x_win_score += 1
            elif(x==y):
                draw_times += 1
            else:
                y_win_score += 1
        print(f'x won {x_win_score} times.\ny won {y_win_score} times.\nIt finished draw {draw_times} times.')
    def toss(self,tossing_time):
        begin = 0
        heads_win_score = 0
        tails_win_score = 0
        while(begin < tossing_time):
            money = random.randint(1,3)
            begin += 1
            if(money==1):
                heads_win_score += 1
            else:
                tails_win_score += 1

        print(f'Heads won {heads_win_score} times.\n Tails won {tails_win_score} times.')
    def play(self):
        list_1 = ['','','']
        list_2 = ['','','']
        list_3 = ['','','']
        winner = False
        while(winner==False):
            try:
                move = input('Choose x or o...')
                area_choice = int(input('Which area u want to put? '))

                if(area_choice==1):
                    list_1[0] = move
                elif(area_choice==2):
                    list_1[1] = move
                elif(area_choice==3):
                    list_1[2] = move
                elif(area_choice==4):
                    list_2[0] = move
                elif(area_choice==5):
                    list_2[1] = move
                elif(area_choice==6):
                    list_2[2] = move
                elif(area_choice==7):
                    list_3[0] = move
                elif(area_choice==8):
                    list_3[1] = move
                elif(area_choice==9):
                    list_3[2] = move

                else:
                    print('u can choose any number except zero')
                
                print(list_1)
                print(list_2)
                print(list_3)

                if(list_1[0]==list_1[1]==list_1[2]):
                    if(list_1 == ['','','']):
                        winner = False
                    elif(list_2 == ['','','']):
                        winner = False
                    elif(list_3 == ['','','']):
                        winner = False
                    else:
                        winner = True
                        print('You won... Congratulations')
                elif(list_2[0]==list_2[1]==list_2[2]):
                    if(list_1 == ['','','']):
                        winner = False
                    elif(list_2 == ['','','']):
                        winner = False
                    elif(list_3 == ['','','']):
                        winner = False
                    else:
                        winner = True
                        print('You won... Congratulations')
                elif(list_3[0]==list_3[1]==list_3[2]):
                    if(list_1 == ['','','']):
                        winner = False
                    elif(list_2 == ['','','']):
                        winner = False
                    elif(list_3 == ['','','']):
                        winner = False
                    else:
                        winner = True
                        print('You won... Congratulations')
                elif(list_1[0]==list_2[0]==list_3[0] != ''):
                    if(list_1[1]==list_2[1]==list_3[1] == ''):
                        winner = False
                    elif(list_1[2]==list_2[2]==list_3[2] == ''):
                        winner = False
                    else:
                        winner = True
                        print('You won... Congratulations')
                elif(list_1[1]==list_2[1]==list_3[1] != ''):
                    if(list_1[0]==list_2[0]==list_3[0] == ''):
                        winner = False
                    elif(list_1[2]==list_2[2]==list_3[2] == ''):
                        winner = False
                    else:
                        winner = True
                        print('You won... Congratulations')
                elif(list_1[2]==list_2[2]==list_3[2] != ''):
                    if(list_1[0]==list_2[0]==list_3[0] == ''):
                        winner = False
                    elif(list_1[1]==list_2[1]==list_3[1] == ''):
                        winner = False
                    else:
                        winner = True
                        print('You won... Congratulations')
                elif(list_1[0]==list_2[1]==list_3[2] == 'x'):
                    winner = True
                    print('You won... Congratulations')
                elif(list_1[2]==list_2[1]==list_3[0] == 'x'):
                    winner = True
                    print('You won... Congratulations')
                elif(list_1[0]==list_2[1]==list_3[2] == 'o'):
                    winner = True
                    print('You won... Congratulations')
                elif(list_1[2]==list_2[1]==list_3[0] == 'o'):
                    winner = True
                    print('You won... Congratulations')

                else:
                    if(list_1[0] != '' and list_1[1] != '' and list_1[2] != ''):
                        if(list_2[0] != '' and list_2[1] != '' and list_2[2] != ''):
                            if(list_3[0] != '' and list_3[1] != '' and list_3[2] != ''):
                                winner = True
                                print('Game has finished. The result is draw.')
                        else:
                            winner = False
                    else:
                        winner = False
                                
            except ValueError:
                print('Please just use numbers when u are choosing area.')
                area_choice = int(input('You can continue, say your area: '))
      

dice = minigames()
coin = minigames()
tictactoe = minigames()
print('Welcome to our terminal minigames.\n1)Dice Rolling\n2)Coin Tossing\n3) Tic-Tac-Toe')
start_choice = int(input('You can play the games with entering the right number that show in above\n'))
if(start_choice==1):
    rolling_time = int(input('how many times u want to roll a dice:\n'))
    dice.roll(rolling_time)
elif(start_choice==2):
    tossing_time = int(input('How many times u want to toss a coin'))
    coin.toss(tossing_time)
elif(start_choice==3):
    tictactoe.play()
else:
    print('you entered wrong.')
