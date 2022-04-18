import numpy as np, cv2

image = cv2.imread("images/flor_pantar.jfif", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일 읽기 오류")
if image.ndim != 3 : raise Exception("영상파일 차원 오류")

#HSV 칼라 공간 변화.
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# two dim histogram 구현, uint8로 지정한 이유는 2차원 0~255 사이 값을 넣어서 출력할 것이기 때문.
two_dim_histo = np.zeros((image.shape[:2]), np.uint8)

# calcHist
for row in range(hsv_img.shape[0]):
    for col in range(hsv_img.shape[1]):
        two_dim_histo[hsv_img[row, col, 0], hsv_img[row, col, 1]] += 1

# max_val = 56, min_val은 없는 부분도 있을거니까 당연히 0 -> 히스토그램 스트레칭 진행.
# 근데 원래 max값은 23이 되어야 하는데... 화나네..;;;;; 내가 그림 잘못 잘라서 그런가봐...ㅜㅜ
max_val = 23 # np.max(two_dim_histo)
two_dim_histo = (two_dim_histo/max_val) * 255
# round 불가능 -> np.array로 재정렬.
two_dim_histo = np.array(two_dim_histo, np.uint8)

# 여기까지 했으면 80% 완료 이제 color 색 입히기
color_histo1 = np.zeros(image.shape, np.uint8)
color_histo2 = np.zeros(image.shape, np.uint8)


# 여기를 이해 못하는 사람이 많을거 같다. 나도 여기서 막혔다.
# two_dim_histo[row, col]은 빈도수가 되어야 하니까
# row, col이 왜 들어가야 하냐 위에서 row col이 Hue, Saturation에 따른 Intensity를 넣었자나
# 그러면 Hue와 Saturation의 상관관계를 보여야 하니까 row와 col이 들어가야징
for row in range(color_histo1.shape[0]):
    for col in range(color_histo1.shape[1]):

        if two_dim_histo[row, col] > 50:
            color_histo1[row, col] = [row, col, two_dim_histo[row, col]]

        color_histo2[row, col] = [row, col, two_dim_histo[row, col]]


# 근데 출력하면 이상하게 나온다...
# 마지막 intensity값이 0이 아닐때만 출력해 보아도 이상하다..
cv2.imshow("color hist1", color_histo1)
cv2.imshow("color hist2", color_histo2)

# 그렇다 이 사진은 BGR 채널이 아닌 HSV채널이다. Hue, Saturation으로 넣었으니까..
color_histo = cv2.cvtColor(color_histo1, cv2.COLOR_HSV2BGR)
cv2.imshow("color hist BGR", color_histo)


print(two_dim_histo)

cv2.imshow("hsv_plot", two_dim_histo)
cv2.imshow("hsv_img", hsv_img)
cv2.imshow("original img", image)
cv2.waitKey(0)
