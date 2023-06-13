import random
def main():
    print("\x1B[31;1mデジタル野球盤\x1B[37;m")
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

    def CountSet(): 
        batterScore = fr'''
            b {'●'*ball}{"o"*(3-ball)}
            s {"●"*strike}{"o"*(2-strike)}
            o {"●"*out}{"o"*(2-out)}

            走者:{"一塁"*place[0]},{"二塁"*place[1]},{"三塁"*place[2]}

            得点:{Score}点
            '''
        print(batterScore)

    print("あなたは先攻です")
    CountSet()
    while out <= 2:
        print("ピッチャーが構えている")
        while bp == 0:
            swing: str = input("バットを振りますか?(振る:1,振らない:2)")
            if swing.isdecimal():
                swing: int = int(swing)
                if swing < 3 and swing > 0:
                    bp = 1
                else:
                    print("\x1B[31;1m1~2を入力してください\x1B[37;m")
            else: 
                print("\x1B[31;1m数字を入力してください\x1B[37;m")
        bp = 0
        print("----------------")
        if swing == 1:
            while bp == 0:
                select:str = input("何で待つ?(ストレート:1,スライダー:2,フォーク:3)")
                if select.isdecimal():
                    select: int = int(select)
                    if select < 5 and select > 0:
                        bp = 1

                    else:
                        print("\x1B[31;1m1~4を入力してください\x1B[37;m")
                else:
                    print("\x1B[31;1m数字を入力してください\x1B[37;m")
            bp = 0
            print("----------------")
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

    print("あなたのスコアは",Score,"点です")