import numpy as np, cv2

def Convolution(img, mask):
    newImg = np.zeros(img.shape, np.float32)
    for r in range(1, len(img)-1):
        for c in range(1, len(img[0])-1):
            temp_area = img[r-1:r+2, c-1:c+2]
            # print('temp_area', temp_area)
            result = 0.0
            for fil_r in range(len(mask)):
                for fil_c in range(len(mask[0])):
                    result += temp_area[fil_r][fil_c] * mask[fil_r][fil_c]


            newImg[r, c] = result
    return newImg

image = cv2.imread("../images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

sobel_x = [
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
]

sobel_y = [
    [1, 2, 1],
    [0, 0 ,0],
    [-1, -2, -1]
]
sobel_x_img = Convolution(image, sobel_x)
sobel_y_img = Convolution(image, sobel_y)

sobel_img = np.sqrt(np.power(sobel_x_img, 2) + np.power(sobel_y_img, 2))
print(np.max(sobel_img))


# sobel_x_img = cv2.convertScaleAbs(sobel_x_img).astype('uint8')
# print(image)
# print(sobel_x_img)

# sobel_img = cv2.convertScaleAbs(sobel_img).astype('uint8')
sobel_img = np.clip(sobel_img, 0, 255).astype('uint8')

sobel_y_img = np.clip(sobel_y_img, 0, 255)


# print(sobel_img)
cv2.imshow('origin', image)
cv2.imshow('edge2', sobel_img)
cv2.imshow('edge', sobel_x_img)
cv2.waitKey(0)