import time
def countdown(t):
    while(True):
        while(t>0):
            print(t,'minutes')
            t -= 1
            time.sleep(0.15)     
            if(t==4):
                x = int(input('>: '))
                if(x==4815162342):
                    for i in range(108):
                        print(i)
                        countdown(108)
            elif(t==0):
                a=0  
                while(10>a):
                    print("SYSTEM FAILURE")
                    a += 1
                y = input('Desmond is turning the key...\n I love you penny...')
                print(y)

print('DHARMA Initiative - Swan Station')
countdown(108)