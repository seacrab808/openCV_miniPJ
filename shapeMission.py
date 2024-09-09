import cv2
import numpy as np

# 그릴 캔버스 설정
canvas_size = 512
img = np.ones((canvas_size, canvas_size, 3), dtype=np.uint8) * 255

# 마우스 이벤트 콜백 함수
def draw_shape(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_RBUTTONDOWN:  # 마우스 오른쪽 버튼 클릭 시 원 그리기
        radius = 50
        color = (0, 255, 0)  # 녹색
        thickness = 2
        cv2.circle(img, (x, y), radius, color, thickness)

    elif event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 클릭 시 다각형 그리기
        if flags & cv2.EVENT_FLAG_CTRLKEY:  # Ctrl + 왼쪽 클릭: 사각형
            pts = np.array([[x - 50, y - 50], [x + 50, y - 50], [x + 50, y + 50], [x - 50, y + 50]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 0), thickness=2)  # 파란색
        else:  # 그냥 왼쪽 클릭: 삼각형
            pts = np.array([[x, y - 50], [x - 50, y + 50], [x + 50, y + 50]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], isClosed=True, color=(0, 0, 255), thickness=2)  # 빨간색

# 창과 마우스 이벤트 연결
cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw_shape)

while True:
    cv2.imshow('Canvas', img)
    
    # 's' 키를 누르면 이미지 저장
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('output_image.jpg', img)
        print("이미지를 저장했습니다.")
        
        # 저장된 이미지 불러오기
        saved_img = cv2.imread('output_image.jpg')

        # 리사이징할 크기 설정
        new_size = (256, 256)

        # cv2.INTER_AREA 보간법을 사용한 리사이징
        resized_area = cv2.resize(saved_img, new_size, interpolation=cv2.INTER_AREA)

        # cv2.INTER_LINEAR 보간법을 사용한 리사이징
        resized_linear = cv2.resize(saved_img, new_size, interpolation=cv2.INTER_LINEAR)

        # cv2.INTER_CUBIC 보간법을 사용한 리사이징
        resized_cubic = cv2.resize(saved_img, new_size, interpolation=cv2.INTER_CUBIC)

        # 원본 이미지와 리사이징된 이미지들 비교를 위해 창에 출력
        cv2.imshow('original', saved_img)
        cv2.imshow('INTER_AREA', resized_area)
        cv2.imshow('INTER_LINEAR', resized_linear)
        cv2.imshow('INTER_CUBIC', resized_cubic)
        
    elif key == 27:  # ESC 키를 누르면 종료
        break

cv2.destroyAllWindows()
