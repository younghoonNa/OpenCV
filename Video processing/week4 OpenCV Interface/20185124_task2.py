import numpy as np
import cv2

def onMouse(event, x, y, flags, params):
    global title, THICKNESS, RADIUS #전역변수로 선언

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), 20, (255,255,255), THICKNESS, cv2.LINE_AA) #LINE_AA가 가장 부드럽게 나옴.
        #cv2.circle(image, 원의 중심, Radius, color, thickness, line type?  선의 부드러운 정도)

        # cv2.circle(image, (x,y), 20, (255,255,255), 2, cv2.LINE_8) #LINE_4보단 부드러움.
        # cv2.circle(image, (x,y), 20, (255,255,255), 2, cv2.LINE_4)
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x,y), (x+RADIUS, y+RADIUS), (0,255,255), THICKNESS, cv2.LINE_AA) #BGR 순서이니까 R+G = Y 노란색으로 출력,
        #cv2.rectangle(image, starting point, stop point, color, thickness, line type)
        cv2.imshow(title, image)

def onChange_THICKNESS(value):
    global image, title, THICKNESS #전역변수로 선언
    THICKNESS = value
    cv2.imshow(title, image)

def onChange_RADIUS(value):
    global image, title, RADIUS
    RADIUS = value
    cv2.imshow(title, image)


image = np.zeros((300, 300, 3), np.uint8) #검은 배경에 그려보기.
title = "Task2"
THICKNESS = 1 #굵기설정
RADIUS = 1 #반지름 설정.

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse) # 마우스 이벤트 함수.
cv2.createTrackbar("THICKNESS", title, 1, 10, onChange_THICKNESS) # 트랙바 만드는 - 굵기부분
cv2.createTrackbar("RADIUS", title, 1, 50, onChange_RADIUS) #트랙바 만들기 - 반지름 부분
cv2.waitKey(0)
cv2.destroyAllWindows()