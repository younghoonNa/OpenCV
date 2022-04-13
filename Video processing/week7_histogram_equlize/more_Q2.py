import cv2, numpy as np

# 이미지 불러오는 과정
image = cv2.imread("images/flor_pantar.jfif", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일 읽기오류")
if image.ndim != 3 : raise Exception("영상파일 차원 오류")

# draw histo 험수 수정.
def draw_histo(hue, saturation, shape = (image.shape[0],image.shape[1])):

    # 2차원 히스토그램을 만들 공간. 크기는 이미지와 동일하게.
    my_calc_hito = np.zeros((shape[0], shape[1]), np.float32)

    # calcHist를 2차원으로 구현하는 부분.
    for row in range(shape[0]):
        for col in range(shape[1]):
            """
            1차원은 해당 컬러 값에 해당하는 부분에 빈도를 게산하는 것 처럼
            2차원도 비슷한 방법으로 시도하였습니다.
            세로 부분이 Hue 이므로 hue[row, col]을  
            가로부분이 saturation이므로 saturation[row, col] 일 때 +1을 해주었습니다.
            
            참고 : image의 행렬 접근, dst = imaeg[y:y+h , x:x+w]            
            """
            my_calc_hito[hue[row, col], saturation[row, col]] += 1
    cv2.imshow("h = hue, w = sat show gray", my_calc_hito)

    # 흑백이 아닌 컬러 공간에 표시해야 하므로 3차원으로 변환.
    # 기존의 shape에 BGR을 가지는 3을 추가.
    my_HSV = np.zeros((shape[0], shape[1], 3), np.uint8)

    # cnt값은 최댓값이 255가 아니기 때문에 히스토그램 스트레칭을 하겠습니다.
    # min값은 모두 0이기 때문에 그대로 진행.

    # max_val = (np.max(my_calc_hito))
    max_cnt_calcHist = 23

    for row in range(shape[0]):
        for col in range(shape[1]):
            # v의 max값은 255가 아니므로 히스토그램 스트레칭
            v = round((my_calc_hito[row, col]/max_cnt_calcHist) * 255)

            # 2차원 칼라 히스토그램 -> 3차원에 mapping
            # 빈도 값이 밝기가 되어야 함.
            # row, col (색상, 채도) 에 따른 밝기 관계를 표현해야 하므로 [row, col, v]
            my_HSV[row, col] = [row, col, v]

    cv2.imshow("HSV__2dim_histogram", my_HSV)

    """
    HSV로 만든 2차원 히스토 그램.
    실습시간까지 그린 부분입니다.
    배경을 까맣게 만들기 위해 v값이 0인 부분은 제거하여 보여드렸습니다.
    위의 row와 col값은 항상 파란색과 초록색을 출력한다는 걸 알았습니다.
    그리고 my_HSV가 HSV 컬러공간으로 나타내어져 있다는 걸 깨달았습니다.
    따라서 HSV컬러공간을 BGR 컬러공간으로 바꾸어주었습니다.  
    """

    dst = cv2.cvtColor(my_HSV, cv2.COLOR_HSV2BGR)
    cv2.imshow("dst", dst)

# 이미지 HSV 이미지로 변환
# 직접 구현한 부분은 밑에 주석처리하여 첨부하였습니다.
HSV_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 채널 분리.
hue, saturation, value = cv2.split(HSV_img)

# 원본 이미지와 변환된 이미지 Show
cv2.imshow("HSV_img", HSV_img)
cv2.imshow("original_img", image)

draw_histo(hue, saturation, shape = image.shape)
cv2.waitKey(0)


print("직접 제작한 Custom cv2.cvtColor(cv2.COLOR_BGR2HSV================")

#일단 돌면서 H,S,V 구하기
H = np.zeros((image.shape[0], image.shape[1]), np.uint8)
S = np.zeros((image.shape[0], image.shape[1]), np.uint8)
V = np.zeros((image.shape[0], image.shape[1]), np.uint8)
for width in range(image.shape[0]):
    for height in range(image.shape[1]):

        # OpenCV의 BGR채널 일단 넣어두기.
        b = image[width, height][0]
        g = image[width, height][1]
        r = image[width, height][2]


        # 채널 구하기 전 min, max 구해두기.
        v = max(image[width, height])

        # V채널.
        V[width, height] = v

        # S채널. 수식을 (V - min(R,G,B)/V) 에서 (V-min(R,G,B)/V * 255로 수정하였습니다.
        min_value = min(image[width, height])
        s = int((v - min_value) / v * 255)
        if v!=0:
            S[width, height] = s
        else:
            S[width, height] = 0

        # H채널

        if s: H_tmp = ((g - b) * 60) / s
        else: H_tmp = 0

        if   (v==r):  H[width, height] = H_tmp/360 * 255
        elif (v==g):  H[width, height] = (H_tmp + 120)/360 * 255
        elif (v==b):  H[width, height] = (H_tmp + 240)/360 * 255

hsv_img = cv2.merge([H,S,V])
hs_cv2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("CV_HSV", hs_cv2)
cv2.imshow("basic", image)
cv2.imshow("HSV", hsv_img)