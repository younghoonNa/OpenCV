import cv2, numpy as np

BGR_img = cv2.imread("images/color_model.jpg", cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception("영상파일 읽기 오류")
if BGR_img.ndim != 3 : raise Exception("영상 파일 차원 오류")

white = np.array([255,255,255], np.uint8) # 브로드 캐스팅 적용 됨.
CMY_img = white - BGR_img
CMY = cv2.split(CMY_img)

black = cv2.min(CMY[0], cv2.min(CMY[1], CMY[2]))
yellow , magenta, cyan = CMY - black

titles = ['black', 'yellow', 'magenta', 'cyan']
[cv2.imshow(t, eval(t)) for t in titles]

cv2.waitKey(0)