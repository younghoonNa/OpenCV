import numpy as np, cv2

def calc_histo(image, histSize, ranges = [0,256]): #행렬 원소의 1차원 히스토그램 게산
    hist = np.zeros((histSize, 1), np.float32)
    gap = ranges[1]/histSize

    for row in image:
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1


    return hist

image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기오류")

histSize, ranges = [32], [0,256]        # 히스토그램 간격수, 값 범위
gap = ranges[1]/histSize[0]             # 계급 간격
ranges_gap = np.arange(0, ranges[1]+1, gap)
hist1 = calc_histo(image, histSize[0], ranges)
hist2 = cv2.calcHist([image], [0], None, histSize, ranges) #OpenCV 내장함수 사용.
hist3, bins = np.histogram(image, ranges_gap)               #numpy 모듈함수

print("User 함수, \n", hist1.flatten())
print("OpenCV 함수, \n", hist2.flatten())
print("numpy 함수, \n", hist3.flatten())