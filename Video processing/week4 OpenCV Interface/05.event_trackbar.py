import cv2
import numpy as np

def onChange(value):
    global image, title #전역변수 참조

    add_value = value - int(image[0][0])
    print("추가 화소값 : ", add_value)

    image = image + add_value
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
