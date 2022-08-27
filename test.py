import cv2
import pytesseract

img="hpbar.png"
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

image = cv2.imread(img,0)

thresh = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
data = pytesseract.image_to_string(thresh,config= '--psm 7 digits')
print(data)

cv2.imshow("yarak",image)
cv2.waitKey()