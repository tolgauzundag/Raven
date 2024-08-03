import cv2 as cv
import numpy as np
import pyautogui


#im2 = pyautogui.screenshot('hunt.png',region=(self.x,self.y,self.w,self.h))
#img= cv2.imread("test.png")
#test = cv2.circle(img,(434,518), 10, (0,0,255), 150)
#cv2.imwrite('mask.png',test)







def mobtemplatematching():
    #im2 = pyautogui.screenshot('hunt.png',region=(self.x,self.y,self.w,self.h))
    #cv.imwrite('res.png',img_rgb)
    img_rgb = cv.imread('test.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('attacked.png', cv.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 120)
    cv.imwrite('res.png',img_rgb)
    global imgg
    imgg=img_rgb
    ######################################
    img_rgb = cv.imread('res.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread("img/dwar/mobs/2Level/yasli.png", cv.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if "max_loc" in locals():
        return max_loc
    else:
        return None
def mobtemplatematching2():
    #im2 = pyautogui.screenshot('hunt.png',region=(self.x,self.y,self.w,self.h))
    #cv.imwrite('res.png',img_rgb)
    img_rgb = cv.imread('test2.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('attacked.png', cv.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 120)
    cv.imwrite('res.png',img_rgb)
    global imgg
    imgg=img_rgb
    ######################################
    img_rgb = cv.imread('res.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread("img/dwar/mobs/2Level/yasli.png", cv.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if "max_loc" in locals():
        return max_loc
    else:
        return None

x= mobtemplatematching()
print(x)
test = cv.circle(imgg,x, 10, (0,255,0), 10)
cv.imwrite("play.png",test)
