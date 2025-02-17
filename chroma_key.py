import sys
import numpy as np
import cv2

# 트랙바 콜백 함수 생성
def on_trackbar(pos):
    global hsv
    hmin = cv2.getTrackbarPos('H_min', 'frame')
    hmax = cv2.getTrackbarPos('H_max', 'frame')
    
    # inRange함수에 적용
    mask = cv2.inRange(hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.copyTo(frame2, mask, frame1)
    cv2.imshow('frame', frame1)

# 동영상 파일명
fileName1 = "data2/woman.mp4"
fileName2 = "data2/raining.mp4"

# 1번영상 불러오기
cap1 = cv2.VideoCapture(fileName1)
# 2번영상 불러오기
cap2 = cv2.VideoCapture(fileName2)

if not cap1.isOpened():
    sys.exit('video1 open failed')
    
if not cap2.isOpened():
    sys.exit('video2 open failed')
    
# 동영상의 fps 확인
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

# 동영상의 총 프레임
frameCount1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frameCount2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# 초당 몇프레임 : 1번 동영상 기준
delay = int(1000/fps1)

# 합성 여부 설정 플래그
do_composite = False

# 창을 먼저 생성, 트렉바 추가
cv2.namedWindow('frame')

# H_min : 40~60
cv2.createTrackbar('H_min', 'frame', 40, 60, on_trackbar)
cv2.createTrackbar('H_max', 'frame', 60, 80, on_trackbar)
#on_trackbar(0)

ret1, frame1 = cap1.read()
hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break

    if do_composite:    
        ret2, frame2 = cap2.read()
        if not ret2:
            break
    
        # hsv 색공간에서 영역을 검출해서 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        # h: 50~70, s:150~255, v:0~255
        mask = cv2.inRange(hsv,(50,150,0),(70,255,255))
        cv2.copyTo(frame2, mask, frame1)
    
    # 결과 확인
    cv2.imshow('frame', frame1)
    key=cv2.waitKey(delay)
    
    # 스페이스 바를 눌렀을때 do_composite를 반전
    if key==ord(' '):
        do_composite = not do_composite
    # ESC가 입력되면 종료
    elif key==27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()