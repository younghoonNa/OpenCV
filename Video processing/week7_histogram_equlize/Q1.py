import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("images/equalize.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

bin, ranges =[256], [0,256]

hist = np.zeros(bin, np.int32)
for row in image:
    for pix in row:
        hist[pix//(ranges[1]//bin[0])]+=1

# print(hist)
# print(sum(hist))
cumulativeSum = np.zeros(hist.shape[:2], np.float32)


cumulativeSum[0] = hist[0]
for i in range(1, hist.shape[0]):
    cumulativeSum[i] = cumulativeSum[i-1] + hist[i]
cumulativeSum = (cumulativeSum / sum(hist))*255
# cumulativeSum = np.array(cumulativeSum, np.uint8)

histo_equalization = np.zeros(image.shape, np.float32)
for w in range(histo_equalization.shape[0]):
    for h in range(histo_equalization.shape[1]):
        histo_equalization[w, h] = cumulativeSum[image[w,h]]

histo_equalization = np.array(histo_equalization, np.uint8)
print(histo_equalization)
dst = draw_histo(cumulativeSum)
dst2 = draw_histo(hist)
# dst3 = draw_histo(histo_equalization)
cv2.imshow("Ss", dst)
cv2.imshow("Ss2", dst2)
cv2.imshow("Ss23", histo_equalization)
cv2.waitKey(0)