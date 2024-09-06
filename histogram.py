import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

src1 = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('data2/Hawkes_norm.jpg', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    sys.exit('이미지 로드 실패')
    
# 히스토그램 만들기 # def calcHist(images, channels, mask, histSize, ranges)
hist1 = cv2.calcHist([src1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([src2], [0], None, [256], [0, 256])


cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
# matplotlib 띄우기
plt.plot(hist1)
plt.plot(hist2)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
