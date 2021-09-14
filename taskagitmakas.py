import random
game_list = ['Taş','Kağıt','Makas']
winner_list = ['robot','you','nobody']
robot_score = 0
your_score = 0
begin = 0
match_time = int(input('Taş,Kağıt,Makas oyununa hoşgeldiniz! Lütfen oyun sayısını seçiniz.'))
print('Kurallar:\n1)Hamlenizi sadece Taş, Kağıt ya da Makas olarak giriş yapınız.\n2)Tüm kurallar onun dışında aynıdır :)\n Bol şanslar.')

while(begin < (match_time+1)):
    your_turn = input('Taş ? Kağıt ? Makas ?')
    robot_turn = random.choice(game_list)
    begin += 1
    if(str(your_turn)=='Taş' and str(robot_turn)==game_list[1]):
        robot_score += 1
        print(f'Robot said {robot_turn} and you said {your_turn} so the winner of this turn is the {winner_list[0]}!')
        print(F'Score of the robot is {robot_score}- Your score is {your_score}')
    elif(your_turn=='Taş' and robot_turn==game_list[2]):
        your_score += 1
        print(f'Robot said {robot_turn} and you said {your_turn} so the winner of this turn is {winner_list[1]}! Congratulations!!')
        print(F'Score of the robot is {robot_score}- Your score is {your_score}')
    elif(your_turn=='Makas' and robot_turn==game_list[0]):
        robot_score += 1
        print(f'Robot said {robot_turn} and you said {your_turn} so the winner of this turn is the {winner_list[0]}!')
        print(F'Score of the robot is {robot_score}- Your score is {your_score}')
    elif(your_turn=='Makas' and robot_turn==game_list[1]):
        your_score += 1
        print(f'Robot said {robot_turn} and you said {your_turn} so the winner of this turn is {winner_list[1]}! Congratulations!!')
        print(F'Score of the robot is {robot_score}- Your score is {your_score}')
    elif(your_turn=='Kağıt' and robot_turn==game_list[2]):
        robot_score += 1
        print(f'Robot said {robot_turn} and you said {your_turn} so the winner of this turn is the {winner_list[0]}!')
        print(F'Score of the robot is {robot_score}- Your score is {your_score}')
    elif(your_turn=='Kağıt' and robot_turn==game_list[0]):
        your_score += 1
        print(f'Robot said {robot_turn} and you said {your_turn} so the winner of this turn is {winner_list[1]}! Congratulations!!')
        print(F'Score of the robot is {robot_score}- Your score is {your_score}')
    elif(your_turn==robot_turn):
        print(f'Robot said {robot_turn} and you said {your_turn} so the winner of this turn is {winner_list[2]}')
        print(F'Score of the robot is {robot_score}- Your score is {your_score}')
print(f'\nGame finished. The final result is \nRobot={robot_score} You={your_score}')
