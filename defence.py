ball = 0
strike = 0
out = 0
strike = 0
place= [0,0,0,0]
ballType = 0
Score = 0
select = 0
hit = 0
swing = 0
inOut = 0
bp = 0

import baseball
import data
import random

def defence():

    while out <= 2:
        print("バッターが構えている")
        select = data.textChecker()

            ballType = random.randint(1,3)
            if select == ballType :
                strike = 0
                ball = 0
                hit = random.randint(1,10)
                print(hit)
                if hit <= 5:
                    print("\x1B[31;1mシングルヒット\x1B[37;m")
                    for j in range(3):
                        if place[2-j] == 1:
                            place[3-j] = 1
                            place[2-j] = 0                   
                        else:
                            pass
                    if place[3] == 1:
                        Score=Score+1
                        place[3] = 0
                    else:
                        pass
                    place[0] = 1
                elif hit <= 8:
                    print("\x1B[31;1mツーベースヒット!\x1B[37;m")
                    for i in range(2):
                        if place[2-i] == 1:
                            Score = Score +1
                            place[2-i] = 0
                        else:
                            pass
                    if place[0] == 1:
                        place[2] = 1
                        place[0] = 0
                    else:
                        pass
                    place[1]=1
                elif hit <= 9:
                    print("\x1B[31;1mスリーベースヒット!\x1B[37;m")               
                    for i in range(3):
                        if place[2-i] == 1:
                            Score = Score +1
                            place[2-i] = 0
                        else:
                            pass
                    place[2]=1
                else:
                    print("\x1B[31;1mホームラン!!!\x1B[37;m")
                    for i in range(3):
                        if place[2-i] == 1:
                            Score = Score +1
                            place[2-i] = 0
                        else:
                            pass
                    Score = Score+1
            else:
                ts = random.randint(1,3)
                if ts <= 2:
                    print("\x1B[31;1mファール!\x1B[37;m")
                    if strike < 2:
                        strike = strike+1
                    else:
                        pass
                else:
                    print("\x1B[31;1mストライク!\x1B[37;m")
                    strike = strike+1
        else:
            inOut = random.randint(1,2)
            if inOut == 1:
                strike = strike+1
                print("\x1B[31;1mストライク!\x1B[37;m")
            else :
                ball = ball+1
                print("\x1B[31;1mボール!\x1B[37;m")

        if strike == 3:
            out = out+1
            ball=0
            strike=0
            print("\x1B[31;1mバッター三振アウト\x1B[37;m")
    
        if ball == 4:
            ball = 0
            strike = 0
            print("\x1B[31;1mフォアボール!\x1B[37;m")
            if place[0]== 1:
                if place[1] ==1:
                    if place[2]==1:
                        place[3] = 1
                    else:
                        place[2] = 1
                else:
                    place[1] = 1
            else:
                place[0] = 1

            if place[3] == 1:
                Score=Score+1
                place[3] = 0
            else:
                pass
            place[0] = 1

        CountSet()
        print("----------------")