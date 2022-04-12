import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("images/flor_pantar.jfif", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")
if image.ndim != 3 :raise  Exception("영상파일 차원오류")

#일단 돌면서 H,S,V 구하기
H = np.zeros((image.shape[0], image.shape[1]), np.uint8)
S = np.zeros((image.shape[0], image.shape[1]), np.uint8)
V = np.zeros((image.shape[0], image.shape[1]), np.uint8)
for width in range(image.shape[0]):
    for height in range(image.shape[1]):

        # OpenCV의 BGR채널 일단 넣어두기.
        b = image[width, height][0]
        g = image[width, height][1]
        r = image[width, height][2]


        # 채널 구하기 전 min, max 구해두기.
        v = max(image[width, height])

        # V채널.
        V[width, height] = v

        # S채널.
        min_value = min(image[width, height])
        s = int((v - min_value) / v * 255)
        if v!=0:
            S[width, height] = s
        else:
            S[width, height] = 0

        # H채널

        if s: H_tmp = ((g - b) * 60) / s
        else: H_tmp = 0

        if   (v==r):  H[width, height] = H_tmp/360 * 255
        elif (v==g):  H[width, height] = (H_tmp + 120)/360 * 255
        elif (v==b):  H[width, height] = (H_tmp + 240)/360 * 255

hsv_img = cv2.merge([H,S,V])
hs_cv2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("CV_HSV", hs_cv2)
cv2.imshow("basic", image)
cv2.imshow("HSV", hsv_img)



def draw_histo(img, shape=image.shape):
    Hue, Saturation, v = cv2.split(img)


    calc_hist = np.zeros((256,256), np.int32)

    for w in range(img.shape[0]):
        for h in range(img.shape[1]):
            calc_hist[Hue[w,h], Saturation[w,h]] += 1


    calc_hist = np.array(calc_hist, np.uint8)
    calc_hist*=10 # 이거 왜 해줘야 할까..? 심지어 해줘도 결과는 같음.
    # print(calc_hist)

    cv2.imshow("draw_points", calc_hist)
    calc_hist*=5
    draw_hist22 = np.zeros((256,256,3), np.uint8)
    for w in range(calc_hist.shape[0]):
        for h in range(calc_hist.shape[1]):
            col = calc_hist[w,h]
            if (col != 0):
                draw_hist22[w,h] = [w,h, col]

    cv2.imshow("dst", draw_hist22)

ranges = [0, 256]
histSize = [256]


draw_histo(hs_cv2)
cv2.waitKey(0)