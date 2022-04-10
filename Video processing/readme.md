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

- rectangle 그리기. `cv2.rectangele(src, (우측하단 ~ 좌측상단) , fill_value, option)`

---
## 4주차 배운 내용.

##### cv2.namedWindow()
- cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)  # cv2.WINDOW_AUTOSIZE는 크기 설정 불가.
- cv2.namedWindow(title1, cv2.WINDOW_NORMAL) # cv2.WINDOW_NORMAL은 크기 변경 가능

##### cv2.resizeWindow()
- 크기 변경은 `cv2.resizeWindow(title1, 400, 300)` # 400x300 size로 resize

##### cv2.waitKeyEx()
- `cv2.waitKeyEx()`는 특정 입력에 대해서 반응. 사용법은 `cv2.waitKey()`와 같음

##### cv2.setMouseCallback(windowName, 사용자 정의 함수(onMouse), param=None(추가적인 사용자 정의 인수))
- 함수 정의 후 마우스 움직임 : `cv2.EVENT_LBUTTONDOWN` , `cv2.EVENT_RBUTTONDOWN`, `cv2.EVENT_LBUTTONUP`, `cv2.EVENT_RBUTTONUP`
- `cv2.EVENT_LBUTTONDBCLICK` 이거는 더블클릭하는 친구인데.. 말을 안듣는다..
- `cv2.setMouseCallback(windowName, onMouse) : 마우스 관련 사용자 정의 함수 `onMouse`및 작동할 windowName 적기.

##### def onMouse(event, x, y, flags, param = None):
  - 발생한 이벤트에 대한 처리와 제어를 구현하는 콜백함수. cv2.setMouseCallback() 함수의 두번째 인수 구현부, 따라서 이름이 같아야 함.
  - onMouse와 setMouseCallback의 인수와 인자는 같아야함.

##### cv2.createTrackbar(trackbarname, windowname, value, count, onChange) -> None:
- `createTrackbar("Name of Track Bar", window Name, start value, end value, 사용자 정의 함수)` # 트랙바 만들기.
- 트랙바 함수 정의 def onChange() 선언 후 `global image, title` 을 통해 전역변수로 사용함. 안그러면 지역변수로 주소 다른애 또 생겨버려.. 
- trackbarname은 imshow를 하여 그림안에 나타나는 trackbar의 name지정.
- windowName은 이 trackbar를 띄울 windowName을 지정.
- value는 이 그림이 imshow를 하여 띄워졌을 때 나타날 초기 값.
- count는 이 트랙바의 maxValue로 0부터 count까지의 값.
- onChange는 트랙바의 콜백 함수.



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

#### 배열 처리 함수 (np.array)
  - cv2.flip :        입력된 2차원 배열을 수직, 수평, 양축으로 뒤집음
    - x_flip - x축 기준 뒤집기 -> cv2.flip(image,0) 
    - y_flip - y축 기준 뒤집기 -> cv2.flip(image,1)
    - xy_flip - x,y축으로 한번씩 뒤집기. -> cv2.flip(image,-1) 
    - repeat : 복붙, transpose - 대각선 뒤집기.
  - cv2.repeat :      입력 배열의 반복된 복사본으로 출력 배열을 채움.
  - cv2.transpose() : 입력 행렬의 전치 행렬을 출력으로 반환

###  `채널 처리.`
- 이미지란 : 2차원 행렬로 표현이 되는 것이 아니라 `RGB 3가지`가 겹쳐져 있는 형태이다.
- OpenCV는 BGR의 형태로 되어있다.
- `Pixel-wise` 화소 단위로 순회 : 값을 저장할 때 BGR값을 Pixel 단위로 나옴.!
- 채널 관련 함수
  - cv2.merge() : 여러개의 단일채널 배열을 다차원 배열로 합성
    - (2,4) 형태의 3개의 BGR을 merge() 하였을 떼 (2,4,3) 형태가 됨 column vector처럼 이어 붙인달까?
  - cv2.split() : 다차원 배열을 여러개의 단일채널로 분리.
    - split() 의 형태는 merge의 BGR이 (2,4) 짜리가 3개가 생김. (2,4,3) 아님, (3,2,4)가 됨,
    - why : 2,4짜리가 3개가 있으니까 3,2,4
    - Split은 BGR을 쪼개서 출력이 가능하게 해줌. 
    - 파란색을 가지는 사진을 쪼개서 보면 파란색 부분이 좀 더 밝음, 초록색도 마찬가지.

#### 사칙 연산
- cv2.add()
- cv2.subtract()
- cv2.multiply()
- cv2.divide()
- cv2.addWeighted()
- `mask`를 통해 관심영역 지정 가능. 0, 1을 통해 영역 지정가능 2들어가도 상관없더리..!

### 지수, 로그, 제곱근 함수
- cv2.exp() : 모들 배열 원소의 지수 계산
- cv2.log() : 모든 배열 원소의 절대값에 대한 자연로그
- cv2.sqrt() : 제곱근 계산
- cv2.pow() : 제곱 승수를 계산

`2학기에 배우는 친구들`
- cv2.magnitude() : $ magnitude =  \sqrt { x^{(i)}^2 + y^{(i)}^2 }  $ 
  - 아 왜 마크다운 안되냐...  휴... 아무튼 두 점 사이의 거리를 구하는 것과 같음.!
- cv2.phase : 이거는 각도 계산.
  - angle(i) = a x tan2(y, x)·[180/\pi]

- cv2.cartToPolar() : 극좌표로 변환되서 동그마리가 됌.
- cv2.polarToCart()

#### 논리(비트) 연산 함수
- cv2.bitwise_and : 논리 곱 연산인 AND 연산 수행. 
- cv2.bitwise_or : 논리 합 연산인 OR 연산 수행.
- cv2.bitwise_xor : 배타적 논리합 XOR
- cv2.bitwise_not : not을 통해 비트반전.

#### 원소의 최솟값과 최댓값.
- cv2.min()
- cv2.max()
- cv2.minMaxLoc() : 위치 반환

#### 통계 관련 함수
- cv2.sumElecs()
- cv2.mean()
- cv2.meanStdDev()  : 배열 원소들의 평균과 표준편차를 계산한다.
- cv2.countNonZero() : 0이 아닌 배열의 원소 개수 N을 반환.
- cv2.reduce() : 행렬 축소
  - dim = 0 => 한 행으로 감축, dim =1 => 한 열로 갑축 
  - cv2.REDUCE_SUM : 행렬의 모든 행을 한방향으로 찌부 시킴 
  - cv2.REDUCE_AVG
  - cv2.REDUCE_MAX
  - cv2.REDUCE_MIN
- cv2.sort()   : 행렬 정렬

---
## 6주차 내용

#### OpenCV와 numpy의 0 미만 255 이상의 화소값 처리 방식 다름 주의
- OpenCV : 255+100 = 360 -> 255 (stauration 방식)
  - `cv2.add(iamge, 100)`, `cv2.subtract(image,100)`
- numpy  : 255+100 = 350%255 -> 104 (modulo 방식)
  - `image + 100`, `image-100`

- np.clip(image, 0, 255) -> 0부터 255까지 처리.
- `cv2.addWeighted(image1, alpha, image2, beta, c)` -> result = image1 * a + image2 * b + c

### 대비 : 같은 색도 인접한 색에 밝기에 따라서 다르게 보임
- cv2.scaledAdd(image, 0.5, 더할 이미지 *필수)  -> 일정 값을 곱하고 같은 크기의 이미지를 더함. 
- cv2.addWeighted(image, 2, 더할 이미지, 0, c) image * 2 + 더할 이미지 * 0 + c 값을 계산.
  - OpenCV 내의 scaledAdd를 사용하기 때문에 saturation 연산이 적용됨.

### 히스토그램
#### 관측값의 개수를 겹치지 않는 다양한 계급으로 표시하는 것.
- Histogram의 value / count of Histogram => P(i), 특정 Pixel이 등장할 확률을 구할 수 있음.
- cv2.calcHist(image, channels, mask, histSize, ranges)
- `cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)` ->  n = (filtered - np.min()) / (np.max() - np.min())


