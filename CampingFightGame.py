import random
class CampingFightGame:
    def CampingFightGame(self):
        while(True):
            animal = random.randint(1,4)
            if(animal==1):
                a = 'lion'
                lion_health = 140
                your_health = 100
            elif(animal==2):
                a = 'crocodile'
                crocodile_health = 125
                your_health = 100
            else:
                a = 'bear'
                bear_health = 160
                your_health = 100
            print('\n\n\n\n\n\n\nYou went to forest for camping. but there were some animals waiting for you.\nYou need to fight with them or you will die...')
            print('There is a', a, 'in front of you...')
            while(True):
                choice = int(input('What will you do now?\n1)attack 2)heal '))
                if(choice==1):
                    if(animal==1):
                        enemy_attack = random.randint(15,40)
                        your_attack = random.randint(1,50)
                        your_health -= enemy_attack
                        lion_health -= your_attack
                        print('You attacked to your enemy with', your_attack,'damage. Enemys health is now', lion_health, '.')
                        print('Lion attacked you with',enemy_attack ,'damage. your health is now', your_health, '.')
                        if(your_health<=0):
                            print('You lost brother...Game over')
                            break
                        elif(lion_health<=0):
                            print('Well done brother. This is your victory.')
                            break
                    elif(animal==2):
                        enemy_attack = random.randint(15,30)
                        your_attack = random.randint(1,50)
                        your_health -= enemy_attack
                        crocodile_health -= your_attack
                        print('You attacked to your enemy with', your_attack,'damage. Enemys health is now', crocodile_health, '.')
                        print('Crocodile attacked you with',enemy_attack ,'damage. your health is now', your_health, '.')
                        if(your_health<=0):
                            print('You lost brother...Game over')
                            break
                        elif(crocodile_health<=0):
                            print('Well done brother. This is your victory.')
                            break
                    else:
                        enemy_attack = random.randint(15,35)
                        your_attack = random.randint(1,50)
                        your_health -= enemy_attack
                        bear_health -= your_attack
                        print('You attacked to your enemy with', your_attack,'damage. Enemys health is now', bear_health, '.')
                        print('Bear attacked you with',enemy_attack ,'damage. your health is now', your_health, '.')
                        if(your_health<=0):
                            print('You lost brother...Game over')
                            break
                        elif(bear_health<=0):
                            print('Well done brother. This is your victory.')
                            break
                else:
                    if(animal==1):
                        enemy_attack = random.randint(15,40)
                        your_heal = random.randint(1,50)
                        your_health += your_heal
                        your_health -=  enemy_attack
                        print('You healed yourself with', your_heal)
                        print('Lion attacked you with',enemy_attack ,'damage. your health is now', your_health, '.')
                        if(your_health<=0):
                            print('You lost brother...Game over')
                            break
                        elif(lion_health<=0):
                            print('Well done brother. This is your victory.')
                            break
                    elif(animal==2):
                        enemy_attack = random.randint(15,30)
                        your_heal = random.randint(1,50)
                        your_health += your_heal
                        your_health -=  enemy_attack
                        print('You healed yourself with', your_heal)
                        print('Crocodile attacked you with',enemy_attack ,'damage. your health is now', your_health, '.')
                        if(your_health<=0):
                            print('You lost brother...Game over')
                            break
                        elif(crocodile_health<=0):
                            print('Well done brother. This is your victory.')
                            break
                    else:
                        enemy_attack = random.randint(15,35)
                        your_heal = random.randint(1,50)
                        your_health += your_heal
                        your_health -=  enemy_attack
                        print('You healed yourself with', your_heal)
                        print('Bear attacked you with',enemy_attack ,'damage. your health is now', your_health, '.')
                        if(your_health<=0):
                            print('You lost brother...Game over')
                            break
                        elif(bear_health<=0):
                            print('Well done brother. This is your victory.')
                            break
start = CampingFightGame()
y = input('Welcome to Camping fight game...\n If you want to start just say yes:\n')  
if(y=='yes'):
    start.CampingFightGame()
else:
    print('Get the fuck out of the here...')
