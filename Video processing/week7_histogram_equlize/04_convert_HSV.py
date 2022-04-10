import numpy as np, cv2, math

def calc_hist(bgr):
    # print(bgr[0], bgr[1], bgr[2])
    B,G,R = float(bgr[0]), float(bgr[1]), float(bgr[2])
    bgr_sum = (R+G+B)

    tmp1 = ((R-G) + (R-B)) * 0.5
    tmp2 = math.sqrt((R-G) * (R-G) + (R-B) * (G-B))
    angle = math.acos(tmp1/tmp2) * (180/np.pi) if tmp2 else 0

    H = angle if B<= G else 360-angle
    S = 1.0 - 3*min([R,G,B]) / bgr_sum if bgr_sum else 0
    I = bgr_sum / 3
    return (H/2, S*255, I)

def bgr2hsi(image):
    hsv = [[calc_hist(pixel) for pixel in row] for row in image]
    return cv2.convertScaleAbs(np.array(hsv))


BGR_img = cv2.imread("images/color_space.jpg", cv2.IMREAD_COLOR)
if BGR_img is None : raise Exception("영상파일 읽기 오류")

HSI_img = bgr2hsi(BGR_img)
HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV)
Hue, Saturation, Intensity = cv2.split(HSI_img)
Hue2, Saturation2, Intensity2 = cv2.split(HSV_img)

titles = ["BGR_img", "Hue", "Saturation", "Intensity"]
[cv2.imshow(t, eval(t)) for t in titles]
[cv2.imshow("Opencv"+t, eval(t+'2')) for t in titles[1:]]
cv2.waitKey(0)