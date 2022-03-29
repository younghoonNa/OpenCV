import numpy as np, cv2

matplot = cv2.imread("images/matplot.jpg")
matplot_copy = matplot.copy()
if matplot is None :raise Exception("영상 파일 읽기 오류")
if matplot.ndim != 3: raise Exception("영상 파일 차원 오류")

blue, green, red = cv2.split(matplot)
zero = np.zeros(matplot.shape[:2], np.uint8)
zero2 = np.zeros(matplot.shape, np.uint8)

# shape 확인.
print(matplot.shape)

# 얼굴의 밝기 증가 -> 얼굴을 더 젊어 보이게.
mask1 = np.zeros(matplot.shape, np.uint8)
mask1[60:108, 97:136] = 50
# 밝기 증가 하려면 BGR 모두 50 증가해야 하지않나..? 그러면 그냥 or
brightness_add = cv2.bitwise_or(matplot, mask1)


# 몸체는 대비 증가. 근데 대비가 이거 맞아..?
mask2 = np.zeros(matplot.shape, np.uint8)
mask2[113:234, 50:188] = 255

# 내가 원하는 영역 지정.
for width in range(113, 234+1):
    for height in range(50, 188+1):
        for bgr in range(0, 2+1):
            matplot_copy[width, height, bgr] = 255- matplot[width, height, bgr]


# 출력 양식에 쓸 mask
mask_add = cv2.bitwise_or(mask1, mask2)

# 밝기 증가 및 대비.
result = cv2.bitwise_or(matplot_copy, mask1)

cv2.imshow("matplot", matplot)
cv2.imshow("mask1 + mask2", mask_add)
# cv2.imshow("mask1", mask1)
# cv2.imshow("mask2", mask2)
cv2.imshow("brightness_add", brightness_add)
cv2.imshow("matplot_copy", matplot_copy)
cv2.imshow("result", result)


cv2.waitKey(0)