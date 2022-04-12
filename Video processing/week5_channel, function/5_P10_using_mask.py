import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_GRAYSCALE)
image_col = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
mask[0:200, 0:100] = 1

n = 0
cnt = 0
for w in range(image.shape[0]):
    for h in range(image.shape[1]):
        if mask[w,h] == 1:
            n += image[w,h]
            cnt +=1

print(n, cnt, n/cnt)

print("grayscale  = " , cv2.mean(image, mask = mask))
print("color = " , cv2.mean(image_col, mask = mask))
cv2.imshow("mask", mask)
cv2.waitKey(0)