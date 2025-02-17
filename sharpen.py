import cv2, sys
import numpy as np

# cartoon

src = cv2.imread('data/lena.bmp')

if src is None:
    sys.exit("이미지 로드 실패")
    
dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()