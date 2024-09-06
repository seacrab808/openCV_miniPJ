import cv2, sys

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit("이미지 로드 실패")
    
# GaussianBlur 처리 세 번째 인수 sigma 값으로 블러 분포 증가 시키
dst = cv2.GaussianBlur(src, (0, 0), 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()