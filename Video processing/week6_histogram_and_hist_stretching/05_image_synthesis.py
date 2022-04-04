import cv2, numpy as np

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None : raise Exception("영상파일 읽기 오류")

alpha, beta = 0.6, 0.7
add_img1 = cv2.add(image1, image2)


# 이미지 곱 이후에 saturation 처리
# 곱하기는 연산이기 때문에 image1*alpha값이 255를 넘어갈 수 있다.
# 따라서 이때 써야하는 것이 np.clip과 np.addWeighted이다.
add_img2 = cv2.add(image1 * alpha, image2 * beta)
# add_img2 = add_img2.astype('uint8')
# print(add_img2)
# cv2.imshow("img2", add_img2)
add_img2 = np.clip(add_img2, 0, 255).astype('uint8')
# print(add_img2)
# cv2.imshow("img3", add_img2)
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

titles = ["image1", "image2", "add_img1", "add_img2", "add_img3"]
for t in titles:
    cv2.imshow(t, eval(t))

cv2.waitKey(0)
