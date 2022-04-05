import numpy as np, cv2
from Common.histogram import draw_histo # 함수 재사용을 위한 임포트

def search_value_idx(hist, bias = 0): # 값 있는 첫 계급 검색함수, 히스토그램의 64개의 칸이 있을 때 몇번째 인덱스에 첫 값이 들어있을까.
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i) # 검색 위치
        if hist[idx] > 0: return idx    # 위치 반환
    return -1

image = cv2.imread("images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

bsize, ranges = [64], [0, 256]    # 계급 개수 및 화소 범위
hist = cv2.calcHist([image], [0], None, bsize, ranges)

bin_width = ranges[1]/bsize[0]      # 한 계급 너비, 흠.. histogram 사이즈..?
low = search_value_idx(hist, 0) * bin_width # 최저 화소값.
high = search_value_idx(hist, bsize[0]-1) * bin_width #최고 화소값.

idx = np.arange(0, 256) # 룩업 인덱스 설정.
# print(idx)
idx = (idx-low)/(high-low) * 255 # 수식 적용하여 룩업 인덱스 설정.

print(idx)
idx[0:int(low)] = 0         # 0보다 작은 값은 0으로 만들어주는 이유는 어짜피 너네 안나올거자나..!
idx[int(high+1):] = 255     # 255보다 큰 친구들! 근데 너네 안나오지 않음? -> 나오긴 나오더라 그러면 변환 해줘야지....
                            # OpenCV는 255 넘치면 다시 0으로 넘기니까....
# print(idx)

dst = cv2.LUT(image, idx.astype('uint8'))
print(dst)
print(image)
print(idx[176])
# 룩업 테이블을 사용하지 않고 직접 구현
# dst = np.zeros(image.shape[0], dtype=image.dtype)
#
# for i in range(dst.shape[0]):
#     for j in range(dst.shape[1]):
#         dst[i, j] = idx[image[i,j]]

hist_dst = cv2.calcHist([dst], [0], None, bsize, ranges)
hist_img = draw_histo(hist, (200,300))
hist_dst_img = draw_histo(hist_dst, (200,300))

print("high value = ", high)
print("low value = ", low)
cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.imshow("dst", dst)
cv2.imshow("hist_dst_img", hist_dst_img)
cv2.waitKey(0)