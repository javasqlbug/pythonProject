import cv2
import time
# 打开视频捕获设备
video_capture = cv2.VideoCapture(0)
#face_cascade = cv2.CascadeClassifier('D:\pythonProject\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(r'D:\pythonProject\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        time.sleep(5)
        pass
    else:
        print('able to load camera.')
        video_capture.set(cv2.CAP_PROP_FPS,30)
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH,352)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,288)
        # 读视频帧
        ret, frame = video_capture.read()
        if ret == True:
            cv2.imshow("v1",frame)
            # 转为灰度图像
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 调用分类器进行检测
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),)
            # 画矩形框
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # 显示视频
            cv2.imshow('Video', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# 关闭摄像头设备
video_capture.release()

# 关闭所有窗口
cv2.destroyAllWindows()
