import cv2
import numpy as np

isColor = True

if not isColor:
    # grayscale
    src = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)
    print(src.shape)

    # 밝기 변화
    dst1 = cv2.add(src, 100)
    # dst1 = src + 100
    # 범위를 0~255로 지정하고 덧셈연산을 수행
    # dst1 = np.clip(src+100, 0, 255).astype(np.uint8)
    
if isColor:
    src = cv2.imread('data/cat.jpg')
    # 채널별로 100씩 더한다. 채널의 순서는 BGR
    # 더하는 값은 튜플로 입력
    dst1 = cv2.add(src, (100, 100, 100))
    

cv2.imshow('img', src)
cv2.imshow('dst1', dst1)
cv2.waitKey()
cv2.destroyAllWindows()