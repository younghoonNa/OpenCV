import numpy as np
import cv2

def onMouse(event, x, y, flags, params):
    global title  #전역변수 선언

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), 20, (255,255,255), 2, cv2.LINE_AA) #LINE_AA가 가장 부드럽게 나옴
        #cv2.circle(image, 원의 중심, Radius, color, thickness, line type?  선의 부드러운 정도)

        # cv2.circle(image, (x,y), 20, (255,255,255), 2, cv2.LINE_8) #LINE_4보단 부드러움.
        # cv2.circle(image, (x,y), 20, (255,255,255), 2, cv2.LINE_4)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x-15,y-15), (x+15, y+15), (0,255,255), 4, cv2.LINE_AA) #BGR 순서이니까 R+G = Y 노란색으로 출력,
        #cv2.rectangle(image, starting point, stop point, color, thickness, line type)
        cv2.imshow(title, image)


image = np.zeros((300, 300, 3), np.uint8) # 300x 300 크기, 배경은 검은색.
title = "Task1"

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse) # 마우스 이벤트 함수.
cv2.waitKey(0)
cv2.destroyAllWindows()