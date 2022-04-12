import cv2, numpy as np

image = cv2.imread('images/color.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
center = (190, 170)

dst = cv2.circle(mask, center, 50, color=(255,255,255),  thickness=cv2.FILLED)
dst = cv2.bitwise_and(mask, image)

cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)
