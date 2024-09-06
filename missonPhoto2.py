# 두 번째 사진
# 조금 더 선명하게

import cv2, sys
import matplotlib.pyplot as plt

src = cv2.imread('misson/03.png')

if src is None:
    sys.exit('이미지 로드 실패')
    
# 블러 이미지 생성
blurred = cv2.GaussianBlur(src, (5, 5), 0)

# High Pass Filter 적용
high_pass = cv2.subtract(src, blurred)

# 원본 이미지에 High Pass Filter 추가
sharpened = cv2.add(src, high_pass)


cv2.imshow('basic', src)
cv2.imshow('edit', sharpened)
cv2.waitKey()
cv2.destoryAllWindows()