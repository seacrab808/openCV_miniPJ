import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit("이미지 로드 실패")
    
# equalize 전 히스토그램
hist1 = cv2.calcHist([src], [0], None, [256], [0, 256])

# equalize 실행
dst = cv2.equalizeHist(src)
dst2 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

# equalize 후 히스토그램
hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])

cv2.imshow('normal', src)
cv2.imshow('equalize', dst)
cv2.imshow('normalize', dst2)
plt.plot(hist1)
plt.plot(hist2)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()