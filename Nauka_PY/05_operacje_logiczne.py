"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import cv2
import imutils

img = cv2.imread(r'assets/view.jpg')
logo = cv2.imread(r'assets/python.png')
logo = imutils.resize(logo, height=150)

# cv2.imshow('img', img)
# cv2.imshow('logo', logo)
# cv2.waitKey(0)

# wycięcie obszaru roi - region of interest
rows, cols, channels = logo.shape
roi = img[:rows, :cols]
# cv2.imshow('roi', roi)
# cv2.waitKey(0)

gray = cv2.cvtColor(src=logo, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
# cv2.waitKey(0)

# budowanie maski

mask = cv2.threshold(src=gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('mask', mask)
# cv2.waitKey(0)

#nowa maska - odwrotna - czarne pozostale rzeczy - umozliwia laczenie obrazow
mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv', mask_inv)
# cv2.waitKey(0)

#operacja laczenia
#wyciecie tła
img_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)
#otrzymanie loga
logo_fg = cv2.bitwise_and(src1=logo, src2=logo, mask=mask_inv)
# cv2.imshow('img_bg', img_bg)
# cv2.imshow('logo_fg', logo_fg)
# cv2.waitKey(0)

#nałożenie jednego obrazu na drugi (operacja add)
dst = cv2.add(src1=img_bg, src2=logo_fg)
cv2.imshow('out1', dst)
#przypisanie do wejsciowego obrazu
img[:rows, :cols] = dst
cv2.imshow('out', img)
cv2.waitKey(0)

#maskowanie, zdjecie w skali szarosci ->threshold (bierzemy pierwszy element
#odwrocenie maski - bit_wise_not