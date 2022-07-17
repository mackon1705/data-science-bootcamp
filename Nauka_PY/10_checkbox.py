import cv2
import numpy as np

img = cv2.imread(r'assets/checkbox.png')
# cv2.imshow('img', img)

img = cv2.copyMakeBorder(
    src=img,
    top=20,
    bottom=20,
    left=20,
    right=20,
    borderType=cv2.BORDER_CONSTANT,
    value=(255, 255, 255)
)
# cv2.imshow('img_border', img)


# skala szarosc
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

# blurrowanie (rozmywanie) - przy detekcji krawedzi mozna patrzyc mniej szczegolowo - nie bedzie problem za bardzo zlozony
blurred = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)
# cv2.imshow('blurred', blurred)

# maska ze zdjecia - znikają napisy
thresh = cv2.threshold(src=blurred, thresh=75, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

# znajdowanie krawedzie
contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[info] Liczba wszystkich znalezionych konturów: {len(contours)}')

# rysowanie konturów
img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[0]], contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow('contour', img_cnt)

# wyznaczanie konturu z checkboxem

checked_idx = None
total = 0

for idx in [1, 2]:
    # generujemy maske z samymi zerami o rozmiarze zdjecia
    mask = np.zeros(shape=gray.shape, dtype='uint8')
    cv2.drawContours(mask, [contours[idx]], contourIdx=-1, color=255, thickness=-1)
    # cv2.imshow(f'mask {idx}', mask)

    mask_inv = cv2.bitwise_not(mask)
    # cv2.imshow(f'mask_inv {idx}', mask_inv)

    # wydobycie wnętrza
    answer = cv2.add(gray, mask_inv)
    cv2.imshow(f'answer: {idx}', answer)  # inwersja odpowiedzi
    answer_inv = cv2.bitwise_not(answer)
    # cv2.imshow(f'answer_inv: {idx}', answer_inv)

    cnt = cv2.countNonZero(answer)
    if cnt > total:
        checked_idx = idx
print(checked_idx)

img = cv2.drawContours(image=img, contours=[contours[checked_idx]], contourIdx=-1, color=(255, 0, 0), thickness=2)
cv2.imshow('checked contoru', img)
cv2.waitKey(5000)
