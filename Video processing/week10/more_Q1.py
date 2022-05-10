import numpy as np, cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨.")

f_low = 50
f_high = 100

while True:
    ret, frame = capture.read()

    if not ret: break # 더 이상 읽을 동영상이 없는 경우
    if cv2.waitKey(30) >= 0: break

    title = "View Frame from Camera"
    cv2.imshow(title, frame)

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # gray_img = cv2.GaussianBlur(gray_img, (5,5), 0)
    canny = cv2.Canny(gray_img, f_low, f_high, 5)
    cv2.imshow("Canny ", canny)

capture.release()

