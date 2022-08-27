import time
import pyautogui
import cv2
import numpy as np
import random
####1lvlmobs
krets = "img/dwar/mobs/krets.png"
delikopek = "img/dwar/mobs/delikopek.png"
####2lvlmobs
yasliiskelet = "img/dwar/mobs/yasliiskelet.png"
erkekatesorumcek = "img/dwar/mobs/erkekatesorumcek.png"
zigred = "img/dwar/mobs/zigred.png"
#####3lvlmobs
azginkopek = "img/dwar/mobs/azginkopek.png"
reiskrets = "img/dwar/mobs/reiskrets.png"
disiatesorumcek = "img/dwar/mobs/disiatesorumcek.png"
savascizigred = "img/dwar/mobs/savascizigred.png"
savasciiskelet = "img/dwar/mobs/savasci.png"
erkekkulorumcegi = "img/dwar/mobs/erkekkulorumcegi.png"
fitsilya = "img/dwar/mobs/fitsilya.png"
####4lvlmobs
yaslicinkopek="img/dwar/mobs/yaslicinkopek.png"
erguvanizigred = "img/dwar/mobs/erguvanizigred.png"


gung6tr = "img/dwar/mobs/gung6.png"
gordt8 = "img/dwar/mobs/keser.png"
minator = "img/dwar/mobs/minator.png"
legion = "img/dwar/mobs/legion.png"
close = "img/dwar/buttons/close.png"
cancel = "img/dwar/buttons/cancel.png"
win = "img/dwar/fight/win.png"
bear = "img/dwar/fight/bear.png"
milk = "img/dwar/fight/milk.png"
s1 = "img/dwar/fight/11.png"
s2 = "img/dwar/fight/22.png"
minimilk = "img/dwar/fight/minimilk.png"
coke = "img/dwar/fight/coke.png"
minicoke = "img/dwar/fight/minicoke.png"
fight = "img/global/vs.png"
map = "img/global/map.png"
sword = "img/global/sword.png"
closebutton = "img/dwar/buttons/quit.png"
####
atk1 = "mid"
atk2 = "mid"
atk3 = "up"
atk4 = "down"
atk5 = "up"
atk6 = None
wincount=0


mob=yaslicinkopek

def scr(x, y, w, h):
    if x is not None:
        im1 = pyautogui.screenshot(region=(x, y, w, h))
        im1.save(r"./hpbar.png")
        print("image saved")
        return


def aquit():
    x = pyautogui.locateOnScreen(closebutton, grayscale=True, confidence=0.80)
    if x is not None:
        pyautogui.click(x)
        exit("Succes")


def randomclick(x,y):
    c = pyautogui.locateOnScreen(s1, grayscale=True, confidence=0.90)
    if c is not None:
        y+=7
        xp = random.randint(0,128)
        yp = random.randint(0,44)
        x +=xp
        y +=yp
        pyautogui.click(x,y)
        return


def findsearch():
    x = pyautogui.locateOnScreen(s1, grayscale=True, confidence=0.90)
    if x is not None:
        print(x)
        first=x
        x = pyautogui.locateOnScreen(s2, confidence=0.90)
        if x is not None:
            print("xaxaxx")
            print(x)
            third = x
            w=(third[0]-first[0])
            print("Width",w)
            h = first[1] - third[1]
            print("Height",h)
            ############################
            x=first[0]
            y=third[1]
            x += 25
            w -= 18
            h +=8
            #im1 = pyautogui.screenshot(region=(x, y, w, h))
            #im1.save(r"./imsg.png")
            return x,y,w,h


def waitforimage(img,tries):
    c=0
    while c < tries:
        x = pyautogui.locateOnScreen(img, grayscale=True, confidence=0.75)
        if x is not None:
            print("Found!!!!")
            return True
        else:
            c += 1
            time.sleep(0.2)
            print(c)
    print("waitforimage didnt found anything")
    return None


def errorcheck():
    x = pyautogui.locateOnScreen(close, grayscale=True, confidence=0.80)
    if x is not None:
        pyautogui.click(x)
        return 1
    x = pyautogui.locateOnScreen(cancel, grayscale=True, confidence=0.80)
    if x is not None:
        pyautogui.click(x)
        return 1


def castattack(caller):
    if caller=="up":
        x = pyautogui.locateOnScreen(sword, grayscale=True, confidence=0.80)
        if x is not None:
            pyautogui.click(x)
            pyautogui.press("q")
            return 1
    elif caller=="mid":
        x = pyautogui.locateOnScreen(sword, grayscale=True, confidence=0.80)
        if x is not None:
            pyautogui.click(x)
            pyautogui.press("w")
            return 1
    elif caller=="down":
        x = pyautogui.locateOnScreen(sword, grayscale=True, confidence=0.80)
        if x is not None:
            pyautogui.click(x)
            pyautogui.press("e")
            return 1
    else:
        return None


def checkwin():
    global wincount
    x = pyautogui.locateOnScreen(win, grayscale=True, confidence=0.80)
    if x is not None:
        print("Won!!!")
        x = 1
        if x is not None:
            pyautogui.click(937,108)
            wincount+=1
            if wincount == 100:
                aquit()
                exit("400 limit")
            return 1


def gamebugfix():
    x = pyautogui.locateOnScreen(bear, grayscale=True, confidence=0.80)
    if x is not None:
        pyautogui.click(x)
        time.sleep(10)
        x = waitforimage(fight, 20)
        if x is not None:
            fightmodule()
        else:
            print("succes")
            return 1


def huntmob():
    checkwin()
    x = pyautogui.locateOnScreen(mob,grayscale=True, confidence=0.85,region=(204,274,1500,494))
    if x is not None:
        print("Mob Found!")
        pyautogui.moveTo(x)
        pyautogui.move(0,-30)
        pyautogui.click()
        pyautogui.click()
        x = errorcheck()
        if x is not None:
            return None
        else:
            x = waitforimage(fight, 10)
            if x is not None:
                print("Succesfuly Clicked!")
                x = fightmodule()
                if x is not None:
                    return 1
                else:
                    x = gamebugfix()
                    if x == 1:
                        return
                    else:
                        pass
                        #exit("UNKNOWN ERROR")



    else:
        print("None Found")
        return None


def cokeuse():
    x = pyautogui.locateOnScreen(coke, grayscale=True, confidence=0.80)
    if x is not None:
        x = pyautogui.locateOnScreen(minicoke, grayscale=True, confidence=0.80,region=(278,229,163,43))
        if x is None:
            pyautogui.press("1")
            pyautogui.press("2")
            print("Used Coke!!!")
            return 1
    else:
        return 0


def milkuse():
    x = pyautogui.locateOnScreen(milk, grayscale=True, confidence=0.80)
    if x is not None:
        x = pyautogui.locateOnScreen(minimilk, grayscale=True, confidence=0.80,region=(278,229,163,43))
        if x is None:
            pyautogui.press("3")
            pyautogui.press("4")
            pyautogui.press("5")
            pyautogui.press("6")
            pyautogui.press("7")
            print("Used Milk!!!")
            time.sleep(3)
            return 1
    else:
        return 0


def hpcheck():
    scr(375,201,7,11)
    frame = cv2.imread("hpbar.png")
    print("cv2")
    if True:
        key = "purple"
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        kernel = np.ones((2, 2), np.uint8)

        low = 0, 251, 53
        up = 0, 255, 88


        mask = cv2.inRange(hsv, low, up)
        mask = cv2.erode(mask, kernel, iterations=0)
        mask = cv2.dilate(mask, kernel, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        ###################################
        print("Checking Hp Bar!")
        if len(cnts) > 0:
            print("Potion Use")
            x = milkuse()
        else:
            print("Fuark")


def fightmodule():
    counter = 1
    errorcount = 0
    while errorcount < 20:
        errorcheck()
        c = checkwin()
        if c is not None:
            return 1
        x = waitforimage(sword,3)
        if x is not None:
            errorcount=0
            hpcheck()
            if counter == 1:
                if atk1 is not None:
                    cokeuse()
                    x = castattack(atk1)
                    print("cast 1")
                    if x is not None:
                        counter +=1
                else:
                    counter = 1
            elif counter == 2:
                if atk2 is not None:
                    cokeuse()
                    x = castattack(atk2)
                    print("cast2")
                    if x is not None:
                        counter += 1
                else:
                    counter = 1
            elif counter == 3:
                if atk3 is not None:
                    cokeuse()
                    x = castattack(atk3)
                    print("cast3")
                    if x is not None:
                        counter += 1
                else:
                    counter = 1
            elif counter == 4:
                if atk4 is not None:
                    cokeuse()
                    x = castattack(atk4)
                    print("cast4")
                    if x is not None:
                        counter +=1
                else:
                    counter = 1
            elif counter == 5:
                if atk5 is not None:
                    cokeuse()
                    x = castattack(atk5)
                    print("cast5")
                    if x is not None:
                        counter +=1
                else:
                    counter = 1
            elif counter == 6:
                if atk6 is not None:
                    cokeuse()
                    x = castattack(atk6)
                    print("cast6")
                    if x is not None:
                        counter +=1
                else:
                    counter = 1
        else:
            errorcount += 1
    return None


errorcounter = 0


time.sleep(1)
x,y,w,h = findsearch()
while True:
    hunt = huntmob()
    if hunt is None:
        errorcounter += 1
        randomclick(x,y)
        if errorcounter > 20:
            pyautogui.click(937,108)
            errorcounter=0
            time.sleep(5)

    else:
        time.sleep(1)



























