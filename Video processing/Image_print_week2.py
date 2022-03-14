import cv2                              # opencv를 불러옵니다.
import numpy as np                      # numpy를 불러와 np라는 이름으로 사용합니다.

image = np.zeros((100,200), np.uint8)   # 300*400 크기의 numpy 배열을 0으로 채움.
image.fill(-978220009)                  # 300*400 크기로 선언된 이미지(넘파이 배열)을 200으로 채움.
# print(image)

cv2.imshow("My OPENCV2", image)       # 윈도우의 제목.
cv2.waitKey(0)                          # 조교님께 여쭤본 결과 :  키보드 입력을 받는 함수.
cv2.destroyAllWindows()                 # 종료? 윈도우 닫기.
print(-978220009%256) #23


#  fill(x) 에서 x값이 0부터 255 사이의 수가 아니더라도 출력을 잘 하며 x가 0보다 작거나 255보다 큰 수일 지라도 x %= 256으로 변환되어 출력하는 것을 확인하였습니다.
