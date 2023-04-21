import win32api, pyautogui as g
from time import sleep

count = 0
savedpos = win32api.GetCursorPos()


def actions():
    print(g.size()) 
    while True:
        g.press('home')
        g.moveTo(541, 142, 0)
        sleep(0.5)
        g.moveTo(541, 172, 0)
        sleep(5)
        cond()

def cond():
    count = 0
    while True:
        savedpos = win32api.GetCursorPos()
        sleep(.5)
        cursorpos = win32api.GetCursorPos()
        if savedpos == cursorpos:
            savedpos = cursorpos
            print("AFK Elapsed Time: ", (count+1)/2, " seconds.")
            count += 1
            if count >= 4: # number / 2 = time til script starts (seconds)
                print("User away for more than 4 minutes, taking control of the system.")
                actions()
            else:
                pass
        else:
            print("User Online")
            sleep(5)
            count = 0

cond()