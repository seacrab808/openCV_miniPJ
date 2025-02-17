import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit("이미지 로드 실패")
    
kernel_size = 5
kernel = (kernel_size, kernel_size)
    
# blur 처리
dst = cv2.blur(src, kernel)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()