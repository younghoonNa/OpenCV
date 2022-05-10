import cv2
import numpy as np

# ksize = (17, 5)
#
# print(np.array(ksize))
#
# print(np.array(ksize) - 1.0)
#
# print((np.array(ksize) - 1.0) * 0.5)
#
# print((np.array(ksize) - 1.0) * 0.5 - 0.1)
#
# print(0.3 * ((np.array(ksize) - 1.0) * 0.5 - 0.1))

image = [
    12, 20, 30, 0,
    8 , 12, 2 , 0,
    34, 70, 37, 4,
    112, 100, 25, 12
]

image = np.array(image, np.uint8).reshape(4,4)

kernel = np.zeros((2,2))

def maxpooling(image):
    result = np.zeros((image.shape[0] // 2, image.shape[1] // 2))

    for row in range(0, image.shape[0], 2):
        for col in range(0, image.shape[1], 2):



            li = []

            for k_row in range(kernel.shape[0]):
                for k_col in range(kernel.shape[1]):
                    li.append(image[row + k_row, col+k_col])

            li = np.array(li, np.uint8)
            result[row//2, col//2] = np.max(li)

    return result
    # print(result)

s = maxpooling(image)
print(s)

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

result = maxpooling(image)
result = np.array(result, np.uint8)
cv2.imshow("result", result)
cv2.imshow("Original Image", image)
cv2.waitKey(0)