import cv2

#progowanie obrazu

img = cv2.imread(r'assets/grey.png',0)
print(img)
cv2.imshow('img', img)

#Thresh Binary
#wszystkie piksele ponizej 150 przyjma kolor czarny, powyzej kolor bialy (255)
thresh_binary = cv2.threshold(src=img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]
cv2.imshow('thresh_binary', thresh_binary)

#petla pokazujaca dzialanie threshold
#threst_binary - tylko czarny i bialy,
#threst_binary_inverse - przeciwne dzialanie
for threst in [0, 50, 100, 150, 200]:
    thresh_binary = cv2.threshold(src=img, thresh=threst, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.imshow(f'thresh_binary: {threst}', thresh_binary)
    cv2.waitKey(1000)
    cv2.destroyWindow(f'thresh_binary: {threst}')

cv2.waitKey(0)