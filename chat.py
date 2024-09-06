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

# 선택된 이미지가 무엇인지 출력
print(f"Selected Image Path: {selected_img_path}")

# 선택된 이미지에 대해 색상 판별
detected_color = classify_color_hsv(hsv_image)
print(f"The selected image is classified as: {detected_color}")

# 가로 크기와 이미지 높이 설정
height, width, _ = selected_img.shape

# 이미지 아래에 검정색 공간 추가 (50 픽셀 높이)
blank_space = np.zeros((50, width, 3), dtype=np.uint8)

# 이미지 아래에 빈 공간 붙이기
extended_img = np.vstack((selected_img, blank_space))

# 이미지 아래 (추가된 공간)에 텍스트 삽입
cv2.putText(extended_img, f"^ Color: {detected_color}", (10, height + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# 이미지 창에 표시
cv2.imshow("Selected Image with Text Below", extended_img)

# 'q' 키를 누를 때까지 창을 유지
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 창 닫기
cv2.destroyAllWindows()