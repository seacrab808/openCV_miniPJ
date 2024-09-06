import cv2
import os
import time
import datetime
import shutil

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024) # MB 단위로 변환

def delete_oldest_folder(parent_folder):
    folders = [os.path.join(parent_folder, d) for d in os.listdir(parent_folder)]
    oldest_folder = min(folders, key=os.path.getmtime)
    shutil.rmtree(oldest_folder)
    print(f"삭제된 폴더: {oldest_folder}")

def record_video(folder_name, duration=60):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("웹캠을 열 수 없습니다")
        return
    
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"{folder_name}/{now}.avi"

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(file_name, fourcc, 20.0, (640, 480))

    start_time = time.time()
    while(int(time.time() - start_time) < duration):
        retval, frame = cap.read()
        if retval:
            out.write(frame)
        else:
            break

    cap.release()
    out.release()
    print(f"생성된 파일: {file_name}")

def main():
    base_folder = "blackbox_records"
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    video_count = 0
    max_videos = 10 # 최대 10개의 동영상만 생성

    while(video_count < max_videos):
        current_time = datetime.datetime.now()
        folder_name = current_time.strftime(f"{base_folder}/%Y%m%d_%H%M")
        create_folder(folder_name)

        record_video(folder_name)

        # 폴더 크기 확인 및 삭제
        if get_folder_size(base_folder) > 500:
            delete_oldest_folder(base_folder)

        video_count += 1
        time.sleep(60) # 다음 녹화까지 60초 대기
    
    print("10개의 동영상이 모두 생성되었습니다.")


if __name__ == "__main__":
    main()