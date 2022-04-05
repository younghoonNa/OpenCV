import cv2, numpy as np
from Common.histogram import draw_histo

image = cv2.imread("images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기오류")

# 128크기로 만들어보자, 범위는 0부터 256까지
histSize = 128; ranges = [0, 256]
non_img = np.full((histSize, 1), 0).astype(np.float32) #astype 안붙이면 ERROR 형변환 해줘야햄.
# print(non_img)

# cv2.calcHist() 였나.. 이친구 만들기.
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        non_img[image[i,j]//int(ranges[1]/histSize)] += 1.0

# hist1 = cv2.calcHist([image], [0], None, [histSize], [0, 256])
# hist2 = draw_histo(hist1)

hist = draw_histo(non_img)
# print(hist)
cv2.imshow("histogram", hist)
cv2.waitKey(0)
