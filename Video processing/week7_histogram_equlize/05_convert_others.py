import cv2

bgr_img = cv2.imread("images/color_space.jpg", cv2.IMREAD_COLOR)
if bgr_img is None : raise Exception("영상파일 읽기 오류")
if bgr_img.ndim != 3 : raise Exception("영상파일 차원 오류")

gray_img = cv2.cvtColor(bgr_img , cv2.COLOR_BGR2GRAY)
ycc_img = cv2.cvtColor(bgr_img , cv2.COLOR_BGR2YCrCb)
yuv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2YUV)
lab_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2LAB)

ycc_ch = cv2.split(ycc_img)
yuv_ch = cv2.split(yuv_img)
lab_ch = cv2.split(lab_img)

cv2.imshow("BGR_img", bgr_img)
cv2.imshow("Gray_img", gray_img)

sp1, sp2, sp3 = ["Y", "Cr", "Cb"], ["Y", "U", "V"], ["L", "A", "B"]
for i in range(len(sp1)):
    cv2.imshow("YCC_img[%d]-%s" % (i, sp1[i]), ycc_ch[i])
    cv2.imshow("YUV_img[%d]-%s" % (i, sp2[i]), yuv_ch[i])
    cv2.imshow("LAB_img[%d]-%s" % (i, sp3[i]), lab_ch[i])
cv2.waitKey(0)