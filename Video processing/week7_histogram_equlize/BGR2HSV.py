import numpy as np, cv2
import math

image = cv2.imread("images/flor_pantar.jfif", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일 읽기 오류")

# HSV로 변환
blue = np.zeros(image.shape[:2], np.uint8)
green = np.zeros(image.shape[:2], np.uint8)
red = np.zeros(image.shape[:2], np.uint8)


hsv_img = np.zeros(image.shape, np.uint8)
# blue, green, red = cv2.split(image)
for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        blue[row, col] = image[row, col, 0]
        green[row, col] = image[row, col, 1]
        red[row, col] = image[row, col, 2]

for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        b = blue[row, col]
        g = green[row, col]
        r = red[row, col]

        v = max(r, g, b)
        s = ((v-min(r,g,b)) / v) * 255

        b_  = b/255.0
        g_ = g/255.0
        r_ = r/255.0

        num = ((r_-g_) + (r_-b_)) * 0.5
        den = np.sqrt((r_-g_)**2 + (r_-b_) * (g_-b_))

        if den: theta = math.acos(num/den) * (180/np.pi)
        else: theta = 0

        if b <= g: h = theta
        else:  h = 360-theta

        hsv_img[row, col, 0] = round(h/2)
        hsv_img[row, col, 1] = int(round(s))
        hsv_img[row, col, 2] = int(v)


cv_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# hsv_img = cv2.merge([H,S,V])
# for row in range(hsv_img.shape[0]):
#     for col in range(hsv_img.shape[1]):
#         print([H[row, col], S[row, col], V[row, col]])
#         hsv_img[row, col] = [H[row, col], S[row, col], V[row, col]]

# hsv_img = np.array(hsv_img,  np.uint8)



cv2.imshow("dst", hsv_img)
cv2.imshow("cv hsv", cv_hsv)
cv2.imshow("image original", image)
cv2.waitKey(0)