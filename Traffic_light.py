import cv2
import numpy as np
import random

# 이미지 경로 설정
green_img_path = "data/green.jpg"
red_img_path = "data/red.jpg"
yellow_img_path = "data/yellow.jpg"

# 이미지 경로 리스트
image_paths = [green_img_path, red_img_path, yellow_img_path]

# 랜덤으로 하나의 이미지를 선택
selected_img_path = random.choice(image_paths)

# 선택된 이미지 불러오기 (BGR로 불러옴)
selected_img = cv2.imread(selected_img_path)

# BGR 이미지를 HSV로 변환
hsv_image = cv2.cvtColor(selected_img, cv2.COLOR_BGR2HSV)

# HSV 범위를 이용하여 색상을 판별하는 함수
def classify_color_hsv(hsv_image):
    # 빨강, 노랑, 초록의 HSV 범위 설정
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    lower_green = np.array([35, 70, 50])
    upper_green = np.array([85, 255, 255])

    lower_yellow = np.array([20, 70, 50])
    upper_yellow = np.array([35, 255, 255])

    # 각 색상 범위에 해당하는 픽셀들만 마스크 처리
    red_mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    # 각 마스크에서 해당 색상의 픽셀이 차지하는 비율 계산
    red_ratio = np.sum(red_mask) / (hsv_image.shape[0] * hsv_image.shape[1])
    green_ratio = np.sum(green_mask) / (hsv_image.shape[0] * hsv_image.shape[1])
    yellow_ratio = np.sum(yellow_mask) / (hsv_image.shape[0] * hsv_image.shape[1])

    # 가장 높은 비율을 가진 색상 반환
    if red_ratio > green_ratio and red_ratio > yellow_ratio:
        return "Red"
    elif green_ratio > red_ratio and green_ratio > yellow_ratio:
        return "Green"
    elif yellow_ratio > red_ratio and yellow_ratio > green_ratio:
        return "Yellow"
    else:
        return "Unknown"

# HSV 트랙바 콜백 함수
def nothing(x):
    pass

# 창 생성
cv2.namedWindow('HSV Adjustments')

# 트랙바 생성
cv2.createTrackbar('H Min', 'HSV Adjustments', 0, 179, nothing)
cv2.createTrackbar('S Min', 'HSV Adjustments', 0, 255, nothing)
cv2.createTrackbar('V Min', 'HSV Adjustments', 0, 255, nothing)
cv2.createTrackbar('H Max', 'HSV Adjustments', 179, 179, nothing)
cv2.createTrackbar('S Max', 'HSV Adjustments', 255, 255, nothing)
cv2.createTrackbar('V Max', 'HSV Adjustments', 255, 255, nothing)

while True:
    # 트랙바 값 읽기
    h_min = cv2.getTrackbarPos('H Min', 'HSV Adjustments')
    s_min = cv2.getTrackbarPos('S Min', 'HSV Adjustments')
    v_min = cv2.getTrackbarPos('V Min', 'HSV Adjustments')
    h_max = cv2.getTrackbarPos('H Max', 'HSV Adjustments')
    s_max = cv2.getTrackbarPos('S Max', 'HSV Adjustments')
    v_max = cv2.getTrackbarPos('V Max', 'HSV Adjustments')

    # HSV 범위 설정
    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])

    # 색상 범위에 맞는 마스크 생성
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    result = cv2.bitwise_and(selected_img, selected_img, mask=mask)

    # 결과 창에 표시
    cv2.imshow('Masked Image', result)

    # 'q' 키를 누를 때까지 창을 유지
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 창 닫기
cv2.destroyAllWindows()
