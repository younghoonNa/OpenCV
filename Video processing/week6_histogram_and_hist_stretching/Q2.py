import cv2, numpy as np
from Common.histogram import draw_histo

image = cv2.imread("images/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")

hist_size = 32 #histogram은 몇 개로 이루어져 있을까.
ranges = [0, 256]
hist_bin = ranges[1]//hist_size # histogram의 한 칸의 크기.
show_hist = np.full((hist_size,1), 0).astype(np.float32)

def my_histo(image, show_hist):
    for width in range(image.shape[0]):
        for height in range(image.shape[1]):
            show_hist[image[width, height]//hist_bin, 0] += 1

    return show_hist

show_hist = my_histo(image, show_hist)

# print(np.min(image)//hist_bin)
# print(np.max(image)//hist_bin)

b = False
for idx in range(show_hist.shape[0]):
    if not b and show_hist[idx, 0] != 0: Min_idx = idx; b = True
    if b and show_hist[idx, 0] == 0 : Max_idx = idx; break

# 사상시킬 좌표 설정.
a = 150; b = 250
print("({0}, {1}) 을 ({2}, {3})으로 이동 시킵니다.".format(np.min(image), np.max(image), a, b))
Max_idx *= hist_bin; Min_idx *= hist_bin

# Look up table 만들기.
idx = np.arange(0, 256)
idx = (idx - Min_idx) * ((b-a) / (Max_idx - Min_idx)) + a
idx[0:int(Min_idx)] = 0
idx[int(Max_idx):] = 255


dst = np.full(image.shape, 0, dtype = image.dtype)

for width in range(dst.shape[0]):
    for height in range(dst.shape[1]):
        dst[width, height] = idx[image[width, height]]

print(dst)


show_hist2 = np.full((hist_size,1), 0).astype(np.float32)
hist_dst = my_histo(dst, show_hist2)
hist_img = draw_histo(hist_dst, (200,500))
cv2.imshow("hist_s", hist_img)
cv2.imshow("hist_img", dst)
cv2.imshow("hist1s", image)



# show_hist = my_histo(image, show_hist)
hist = draw_histo(show_hist, (200,500))
cv2.imshow("hist", hist)
cv2.waitKey(0)
print(show_hist)


