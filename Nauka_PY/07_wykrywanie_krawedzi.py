import  cv2
import imutils

#Canny Edge Detection - popularne narzedzie wykrywania krawedzi

img = cv2.imread(r'assets/guido.jpg')
img = imutils.resize(image= img, height= 500)
cv2.imshow('img', img)

canny = cv2.Canny(image=img, threshold1=250, threshold2=250)

#dzialanie detektora w zaleznosci od wartosci
# z kazdym kolejnym krokiem krawedzie sa mniej zaszumione
for threst in [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]:
    canny = cv2.Canny(image=img, threshold1=threst, threshold2= threst)
    cv2.imshow(f'canny: {threst}', canny)
    cv2.waitKey(2000)
    cv2.destroyWindow(f'canny: {threst}')

cv2.waitKey(0)
# while True:
#
#     cv2.imshow('canny', canny)
#     if cv2.waitKey(1) == 27:
#         break