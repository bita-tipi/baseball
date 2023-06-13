from baseball import attack
import data
import text
selector = 0

        
print(text.binder)
selector = data.textChecker("ゲーム開始:1  設定:2  終了:3",1,3)

if selector ==  1:
    selector = input(text.modeText,1,2)
    if selector == 1:
        attack()
    else:
         pass
elif selector == 2:
    pass
else:
    exit(0)

