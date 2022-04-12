import numpy as np, cv2

image = cv2.imread("images/flor_pantar.jfif", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")
if image.ndim != 3 :raise  Exception("영상파일 차원오류")

#일단 돌면서 H, S,V 구하기
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

hue_hist = np.zeros(256, np.uint8)
saturation_hist = np.zeros(256, np.uint8)

hist_img = np.full((256,256), 0, np.uint8)

for width in range(image.shape[0]):
    for height in range(image.shape[1]):
        hist_img[H[width, height], S[width, height]] +=1
        hue_hist[H[width, height]]+=1
        saturation_hist[S[width, height]]+=1


print(hist_img)

hue = np.zeros(image.shape[:2], np.uint8)
cv2.normalize(hue_hist, hue, 0 , image.shape[0], cv2.NORM_MINMAX) # 세로니까..!
cv2.normalize(saturation_hist, saturation_hist, 0, 256, cv2.NORM_MINMAX)

# def draw_histo(hue, saturation, shape=(194, 259,3)):
#     hist_img = np.full((256,256,3), 0, np.uint8)
#
#
#
#
#
#     # print(hue, saturation)
#
#     for h in range(0, 256):
#         for s in range(0, 256):
#             # print(h,s, hue[h], saturation[s])
#             cv2.rectangle(hist_img, (h, s), (1, 1), (int(hue[h]), int(saturation[s]), h), thickness=cv2.FILLED)
#
#
#     cv2.imshow("sssss", hist_img)
#
# draw_histo(hue_hist, saturation_hist)

#
# hs_cv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
#
# # print(image)
# # print("===========================================")
# # print(hs_cv)
# # print("===========================================")
# # print(hsv_img)
#
# cv2.imshow("hsv", hs_cv)
# cv2.imshow("aimeg", hsv_img)
# cv2.waitKey(0)