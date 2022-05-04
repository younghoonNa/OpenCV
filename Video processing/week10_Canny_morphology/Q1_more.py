import cv2
import numpy as np

capture = cv2.VideoCapture(0)

if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨.")

filter_gaussian = [
    1/9, 1/9, 1/9,
    1/9, 1/9, 1/9,
    1/9, 1/9, 1/9
]

sobel_vertical = [
    -1, 0, 1,
    -2, 0, 2,
    -1, 0, 1
]

sobel_horizontal = [
    -1, -2, -1,
    0, 0, 0,
    1, 2, 1
]



def mask(image, kernel):
    kernel = np.array(kernel, np.float32).reshape(3,3)

    result = np.zeros(image.shape[:2], np.float32)

    len_row = image.shape[0]
    len_col = image.shape[1]

    k_len_row = kernel.shape[0]
    k_len_col = kernel.shape[1]
    k_cen = k_len_col//2

    for row in range(len_row):
        for col in range(len_col):

            acc = 0.0

            if (row < k_cen or row > len_row-k_cen): continue
            if (col < k_cen or col > len_col-k_cen): continue

            for k_row in range(k_len_row):
                for k_col in range(k_len_col):
                    tmp = image[row- k_row , col - k_col] * kernel[k_row, k_col]
                    acc += tmp

            print(acc)
            result[row, col] = acc


    return result

def non_maximum_suppression(magnitude, phase):

    result = np.zeros(magnitude.shape[:2], np.float32)

    len_row = magnitude.shape[0]
    len_col = magnitude.shape[1]

    kernel = np.zeros((3,3), np.float32)
    k_len_row = kernel.shape[0]
    k_len_col = kernel.shape[1]
    k_cen = k_len_col//2

    for row in range(len_row):
        for col in range(len_col):

            if (row <= k_cen or row >= len_row-k_cen): continue
            if (col <= k_cen or col >= len_col-k_cen): continue

            p = phase[row, col]
            if p == 0:
                idx1 = [0,-1]; idx2 = [0,1]
            elif p == 45:
                idx1 = [-1,-1]; idx2 = [1,1]
            elif p == 90:
                idx1 = [-1,0]; idx2 = [1,0]
            else:
                idx1 = [-1,1]; idx2 = [1,-1]

            left = magnitude[row + idx1[0], col + idx1[1]]
            right = magnitude[row + idx2[0], col + idx2[1]]
            mid = magnitude[row , col]


            if mid >= left and mid >= right:
                result[row, col] = mid
                print(left, right, mid)
        else:
                result[row, col] = 0

    return result



image = cv2.imread("images/canny.jpg", cv2.IMREAD_GRAYSCALE)

r = mask(image, filter_gaussian)

r = np.abs(r)
r = np.clip(r, 0, 255).astype('uint8')

rv = mask(r, sobel_vertical)
rh = mask(r, sobel_horizontal)

rs = np.power(rv, 2) + np.power(rh, 2)
rc = np.sqrt(rs)
rc = np.clip(rc, 0, 255).astype('uint8')

ran = cv2.phase(rv, rh)
ran = ran/np.max(ran) * 180
print(ran)
print(np.max(ran), np.min(ran))


rss = non_maximum_suppression(rc, ran)
rss = np.array(rss, np.uint8)

cv2.imshow("rms", image)
cv2.imshow("r", r)
cv2.imshow("r3", rc)

cv2.imshow("rss", rss)

th = 50

def threshold(image, th):
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):

            if image[row , col] < th:
                image[row, col] = 0

    return image

rs2 = threshold(rss, th)
cv2.imshow("rs2", rs2)

cv2.waitKey(0)


def angle45(image):

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            angle = image[row, col]

            if angle >= 0 and angle < 22.5:
                 image[row, col] = 0
            elif angle >= 22.5 and angle < 45 + 22.5:
                image[row, col] = 45
            elif angle >= 45 + 22.5 and angle < 90 + 22.5:
                image[row, col] = 90
            elif angle >= 90 + 22.5 and angle < 135 + 22.5:
                image[row, col] = 135
            else:
                image[row, col] = 0

    return image




while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    t_low = 30; t_high = 70

    blur_frame = mask(frame, filter_gaussian)

    # cv2.convertScaleAbs() 구현
    blur_frame = np.abs(r)
    blur_frame = np.clip(blur_frame, 0, 255).astype('uint8')


    sobel_v = mask(frame, sobel_vertical)
    sobel_h = mask(frame, sobel_horizontal)

    # cv2.magnitude 계산
    sobel_sqrt = np.power(sobel_v, 2) + np.power(sobel_h, 2)
    sobel_conv = np.sqrt(sobel_sqrt)
    sobel_conv = np.clip(sobel_conv, 0, 255).astype('uint8')

    # 각도 계산 -> 삼각함수를 직접 구현하는 것이 아직은 어려워 cv2.phase 사용하였습니다.
    angle = cv2.phase(sobel_v, sobel_h)
    angle = angle/np.max(angle) * 180 # 0 ~ 5 사이의 값을 0부터 180까지로 변환.

    angle = angle45(angle) # 0, 45, 90, 135로 변환하는 함수

    result = non_maximum_suppression(sobel_conv, angle)
    result = np.array(result, np.uint8)


print(ran)
print(np.max(ran), np.min(ran))



