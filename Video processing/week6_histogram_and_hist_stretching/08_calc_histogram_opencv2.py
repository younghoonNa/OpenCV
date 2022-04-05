import numpy as np, cv2

def calc_histo(image, histSize, ranges=[0, 256]):
    hist = np.zeros((histSize, 1), np.float32)
    gap = ranges[1] / histSize  # 256 / histSize

    for row in image:
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1

    return hist

image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")

histSize, ranges = [32], [0, 256]
gap = ranges[1] / histSize[0]
ranges_gap = np.arange(0, ranges[1] + 1, gap)
# print(ranges_gap)
hist1 = calc_histo(image, histSize[0], ranges)
hist2 = cv2.calcHist([image], [0], None, histSize, ranges)
hist3, bins = np.histogram(image, ranges_gap)

print("User 함수 : \n", hist1.flatten())
print("Opencv 함수 : \n", hist2.flatten())
print("numpy 함수 : \n", hist3.flatten())
