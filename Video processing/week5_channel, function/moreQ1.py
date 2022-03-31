import numpy as np, cv2
logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None : raise Exception("영상 파일 오류!")
if logo.ndim != 3 : raise Exception("영상 차원 오류")

blue, green, red = cv2.split(logo)
zero = np.zeros(logo.shape[:2], np.uint8)

blue_img = cv2.merge([blue, zero, zero])
green_img = cv2.merge([zero, green, zero])
red_img = cv2.merge([zero, zero, red])

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey(0)

