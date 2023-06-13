

def textChecker(text,min,max):
    bp=0
    selector = 0
    while bp == 0:
        selector:str = input(text+" > ")
        if selector == "999":
            developerTool()
        else:
            pass
        if selector.isdecimal():
            selector: int = int(selector)
            if min<=selector and selector<=max:
                bp = 1
                return selector
            else:  
                print("\x1B[31;1m",min,"~",max,"を入力してください\x1B[37;m")
                bp = 0
        else:
            print("\x1B[31;1m数字を入力してください\x1B[37;m")
            bp = 0

def debugTextChecker(text2,min2,max2):
    bp=0
    selector = 0
    while bp == 0:
        selector:str = input(text2+" > ")
        if selector.isdecimal():
            selector: int = int(selector)
            if min2<=selector and selector<=max2:
                bp = 1
                return selector
            else:  
                print("\x1B[31;1m",min2,"~",max2,"を入力してください\x1B[37;m")
                bp = 0
        else:
            print("\x1B[31;1m数字を入力してください\x1B[37;m")
            bp = 0
def developerTool():
    bp = 0
    selector = 0
    print("debugMode")
    while bp == 0:
        selector = debugTextChecker("debugEnd:1  break:2",1,2)
        if selector == 1:
            bp = 1
            print("back")
        elif selector == 2:
            exit(0)
        else:
            pass