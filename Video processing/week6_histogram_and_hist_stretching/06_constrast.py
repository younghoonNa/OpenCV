import numpy as np, cv2

image = cv2.imread('images/contrast.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

noimage = np.zeros(image.shape[:2], image.dtype)
avg = cv2.mean(image)[0]/2.0 # 영상 평균화소의 절반

# 곱셈을 통한 영상 대비 변경
dst1 = cv2.scaleAdd(image, 0.5, noimage)             # 명암 대비 감소
dst2 = cv2.scaleAdd(image, 2.0, noimage)             # 명암 대비 증가

# 영상 평균값을 통한 대비 변경
dst3 = cv2.addWeighted(image, 0.5, noimage, 0, avg)  #명암 대비 감소
dst4 = cv2.addWeighted(image, 2.0, noimage, 0, -avg) #명암 대비 증가
# 이미지의 값에 2배를 해준 다음, 0을 더해줌 -> 변화 없고, 그 다음 영상 평균 밝기를 빼주면
# 원래 밝기의 차이에 2배의 차이가 남. 대비 증가가
cv2.imshow("image", image)
cv2.imshow("dst1 - decrease contrast", dst1)
cv2.imshow("dst2 - decrease contrast", dst2)
cv2.imshow("dst3 - decrease contrast using average", dst3)
cv2.imshow("dst4 - decrease contrast using average", dst4)
cv2.waitKey(0)