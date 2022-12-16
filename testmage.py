import pyautogui
import time
sword = "img/global/sword.png"
minimana = "img/dwar/fight/minimana.png"
def waitforimage(img, tries, conf):
    c = 0
    while c < tries:
        x = pyautogui.locateOnScreen(img, grayscale=True, confidence=conf)
        if x is not None:
            print(x)
            exit()
        else:
            c += 1
            time.sleep(0.2)

    return None


#x = waitforimage(sword, 10, 0.75)
while True :
    x = pyautogui.locateOnScreen(minimana, grayscale=True, confidence=0.80,
                                 region=(261, 228, 209, 49))
    if x is None:
        print(x)
