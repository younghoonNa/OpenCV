import cv2, numpy as np
from Common.histogram import draw_histo

image = cv2.imread("images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기오류")

# 128크기로 만들어보자, 범위는 0부터 256까지
histSize = 128; ranges = [0, 256]
bin_width = ranges[1]//histSize # 이거는 histogram의 gap이랄까? 너비?
print(bin_width)
non_img = np.full((histSize, 1), 0).astype(np.float32) #astype 안붙이면 ERROR 형변환 해줘야햄.

# cv2.calcHist() 였나.. 이친구 만들기.
def my_hist(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            non_img[image[i,j]//bin_width] += 1.0

    return non_img

hist = draw_histo(my_hist(image))
cv2.imshow("custom histogram", hist)

histogram = cv2.calcHist([image], [0], None, [histSize], [0, 256])
cv_histo = draw_histo(histogram)

cv2.imshow("opencv histogram", cv_histo)


print("=================================== Q1 =========================================")

b = False #b를 넣어서 Min_index, Max_index 완성.

for index in range(non_img.shape[0]):

    if not b and non_img[index,0] != 0:
        Min_index = index
        b = True

    if b and non_img[index, 0] == 0:
        Max_index = index
        break

print(Min_index, Max_index)
look_up_table = np.arange(0,256)
Min_index *= bin_width
Max_index *= bin_width
look_up_table = (look_up_table-Min_index)/(Max_index-Min_index) * 255

look_up_table[:Min_index] = 0
look_up_table[Max_index:] = 255 #내꺼는 Max_index의 value가 0이기 때문 +1 안해줌.

base_img = np.zeros(image.shape, dtype=image.dtype)

for width in range(base_img.shape[0]):
    for height in range(base_img.shape[1]):
        base_img[width, height] = round(look_up_table[image[width, height]])


print(base_img)

cv2.imshow("image", image)
cv2.imshow("stretching hist", base_img)
cv2.imshow("stretching hist histogram", draw_histo(my_hist(base_img)))

cv2.waitKey(0)
