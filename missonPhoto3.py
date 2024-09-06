# 세 번째 사진
# 밝기 낮추기, 선명도 올리기

import cv2, sys


src = cv2.imread('misson/05.png', cv2.COLOR_BGR2GRAY)

if src is None:
    sys.exit('이미지 로드 실패')
    

# 블러 이미지 생성
blurred = cv2.GaussianBlur(src, (5, 5), 0)

# Unsharp Masking 적용
sharpened = cv2.addWeighted(src, 1.5, blurred, -0.5, 0)
    
# 이미지 밝기 조절
dark = cv2.add(sharpened, -20)

cv2.imshow('basic', src)
cv2.imshow('edit', dark)
cv2.waitKey()
cv2.destoryAllWindows()