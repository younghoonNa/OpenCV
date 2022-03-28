# 영상처리 프로그레밍


---
## 3주차 배운 내용중 기억해야 하는 것.

##### 다차원 객체의 1차원 변환방법.
a = np.random.rand(2,3) # 2*3 크기의 (2행 3열) 넘파이 배열 랜덤 생성. <br>
b = np.random.randn(3,2) # 3*2 크기의 (3행 2열) 평균 0, 표준편차가 1인 넘파이 배열 랜덤 생성. <br>
c = np.random.randint(1,6) # 1*6 크기의 (1행 6열) 정수로 이루어진 랜덤 넘파이 배열 생성. <br>

1. a.flatten()
2. b.ravel(b)
3. np.reshape(c, (-1, ))
4. d.reshape(-1)

---
## 4주차 배운 내용.

##### cv2.namedWindow()
- cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)  # cv2.WINDOW_AUTOSIZE는 크기 설정 불가.
- cv2.namedWindow(title1, cv2.WINDOW_NORMAL) # cv2.WINDOW_NORMAL은 크기 변경 가능

##### cv2.resizeWindow()
- 크기 변경은 `cv2.resizeWindow(title1, 400, 300)` # 400x300 size로 resize

##### cv2.waitKeyEx()
- `cv2.waitKeyEx()`는 특정 입력에 대해서 반응. 사용법은 `cv2.waitKey()`와 같음

##### cv2.setMouseCallback(title, 사용자 정의 함수)
- 함수 정의 후 마우스 움직임 : `cv2.EVENT_LBUTTONDOWN` , cv2.EVENT_RBUTTONDOWN`, `cv2.EVENT_LBUTTONUP`, `cv2.EVENT_RBUTTONUP`
- `cv2.EVENT_LBUTTONDBCLICK` 이거는 더블클릭하는 친구인데.. 말을 안듣는다..
- `cv2.setMouseCallback(title1, onMouse) : 마우스 관련 사용자 정의 함수 `onMouse`및 작동할 window name 적기.

##### cv2.createTrackbar()
- `createTrackbar("Name of Track Bar", window Name, start value, end value, 사용자 정의 함수)` # 트랙바 만들기.
- 트랙바 만들 때 `global image, title` 을 통해 전역변수로 사용함. 

##### OpenCV에서 사진에 그림그리기
- <b> `OpenCV`에서 색상 배열은 `BGR` 순임. 참고로 `matplotlib은 RGB`니까 다시 변환 해야함. </b>
- cv2.line(image, startpoint, stoppoint, color,  THICKNESS, draw Line_AA or LINE_4 , 8 ..ect )
- rectangle(image, (image, first point (Left-high) , second 3point (Right-bottom) .. 위와 같음)

##### cv2.imread()
- cv2.imread()를 통해 이미지를 불러옴. 흑백으로 불러올까? -> `cv2.IMREAD_GRAYSCALE`, 컬러로 불러올까? -> `cv2.IMEAD_COLOR`

##### JPEG, PNG
- JPEG : 압축시 손실이 있지만 압축 성능이 좋음                -> (`cv2.IMWRITE_JPEG_QUALITY, 0~100)
- PNG : 무손실 압축파일. 손실이 나는걸 원하지 않는다면 PNG 사용. -> (`cv2.IMWRITE_PNG_COMPRESSION, 0~9)

##### Matplotlib
- `cv2.cvtColor(image, 여기에 들어갈 수 있는건 많은데.. 일단 배운건 말이지)` 
1. `cv2.COLOR_BGR2RGB` : OpenCV에서 제공하는 BGR형식은 matplotlib의 RGB형식과 다르기 때문에 `cv2.cvtColor`로 바꿈.
2. `cv2.COLOR_GBR2GRAY` : BGR형식을 GRAY의 회색 형식으로 바꿔줌
- `plt.axis('off')` # 축을 없앰, `plt.tight_layout()` # 여백도 없음
- `plt.suptitle("서브타이틀이 존재할 떄 슈퍼 타이틀로 제목 설정...!! ")`

---
## 5주차 내용
- 파이썬에서 배열을 처리하기 위한 자료형
  - 열겨형 객체 (sequence) - List, tuple, dictionary
 
- 명칭 및 표현
  - 1차원 데이터 : 벡터
  - 2차원 데이터 : 행렬
  - 1차원과 2차원 데이터 통칭해서 배열

- 배열 처리 함수 (np.array)
  - cv2.flip :        입력된 2차원 배열을 수직, 수평, 양축으로 뒤집음
    - x_flip - x축 기준 뒤집기 -> cv2.flip(image,0) 
    - y_flip - y축 기준 뒤집기 -> cv2.flip(image,1)
    - xy_flip - x,y축으로 한번씩 뒤집기. -> cv2.flip(image,-1) 
    - repeat : 복붙, transpose - 대각선 뒤집기.
  - cv2.repeat :      입력 배열의 반복된 복사본으로 출력 배열을 채움.
  - cv2.transpose() : 입력 행렬의 전치 행렬을 출력으로 반환

---
## 6주차 내용
