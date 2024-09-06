# 첫 번째 사진
# 배경 노이즈 fastMeanDenoising으로 제거, 밝기 어둡게, 채도 살짝 낮추기

import cv2, sys
import numpy as np

src = cv2.imread('misson/01.png', cv2.COLOR_BGR2GRAY)

if src is None:
    sys.exit('이미지 로드 실패')
    
# 이미지 밝기 조절
dark = cv2.add(src, -20)  # BGR 채널마다 -20을 적용

# fastNlMeansDenoising Filter 적용
dst = cv2.fastNlMeansDenoising(dark, None, h=5, templateWindowSize=7, searchWindowSize=21)

# HSV 색상 공간으로 변환
hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
# 채도 채널 가져오기
saturation = hsv[:, :, 1]
# 채도 감소 비율 설정 (예: 0.5배로 줄이기)
saturation = saturation * 0.9
# 채도 값을 0-255 범위로 클램핑
saturation = np.clip(saturation, 0, 255).astype(np.uint8)
# 채도 값을 HSV 이미지에 다시 설정
hsv[:, :, 1] = saturation
# HSV를 BGR로 다시 변환
result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


cv2.imshow('basic', src)
cv2.imshow('edit', result)
cv2.waitKey()
cv2.destoryAllWindows()