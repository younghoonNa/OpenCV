import numpy as np, cv2

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th2", "result")

    _, result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)
    cv2.imshow("result", result)

bgr_img = cv2.imread("images/color_space.jpg", cv2.IMREAD_COLOR)
if bgr_img is None: raise Exception("영상파일 읽기 오류")

hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
hue = np.copy(hsv_img[:, :, 0])

th = [50, 100]
cv2.namedWindow("result")
cv2.createTrackbar("Hue_th1", "result", th[0], 255, onThreshold)
cv2.createTrackbar("Hue_th2", "result", th[1], 255, onThreshold)
onThreshold(th[0])
cv2.imshow("BGR_Img", bgr_img)
cv2.waitKey(0)