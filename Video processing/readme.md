# 영상처리 프로그레밍

- openCV의 cv2.CV_8S, cv2.CV_8U, cv2.CV_16U, cv2.CV_16S, cv2.CV_32F, cv2.CV_64F 는 모두 타입이 int형이다.. 놀랍게도..
- np.uint8, np.int32의 타입은 type이다. 

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

##### cv2.namedWindow(windowName, [flag])
- cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)  # cv2.WINDOW_AUTOSIZE는 크기 설정 불가. flag = 1
- cv2.namedWindow(title1, cv2.WINDOW_NORMAL) # cv2.WINDOW_NORMAL은 크기 변경 가능       flag = 0

#### cv2.moveWindow(windowName, x, y):
  - windowName 이름을 가진 window를 x,y만큼 이동시킨다.
  - cv2.namedWindow()가 선언되어야 사용할 수 있다.

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
- cv2.line(img, pt1, pt2, color, [thickness, lineType, shift]) -> img
  - pt1 = startpoint, pt2 = stoppoint
  - cv2.line(image, startpoint, stoppoint, color,  THICKNESS, draw Line_AA or LINE_4 , 8 ..ect )
- cv2.rectangle(img, pt1, pt2, color, [thickness, lineType, shift])
- cv2.rectangle(img rec, color, [thickness, lineType, shift])
  - rec = image, pt1 = lefttop, pt2 = bottomright 
  - rectangle(image, (image, first point (Left-high) , second 3point (Right-bottom) .. 위와 같음)
- cv2.circle(img, center, radius, color, [thickness, lineType, shift])
  - thickness = cv2.FILLED 일 경우 내부를 채움.  `-1` 도 가능.!
 

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
- `plt.suptitle("서브타이틀이 존재할 때 슈퍼 타이틀로 제목 설정...!! ")`

---
## 5주차 내용
- 파이썬에서 배열을 처리하기 위한 자료형
  - 열겨형 객체 (sequence) - List, tuple, dictionary
 
- 명칭 및 표현
  - 1차원 데이터 : 벡터
  - 2차원 데이터 : 행렬
    - 행렬에 접근시 roi_img = image[y:y+h, x:x+w] 
    - x와 y가 바뀌게 됨 -> 우리가 평소에 사용하는 numpy에 접근하는 개념은 같음.
    - x,y보단 row, col 개념으로 접근하는게 이해하기 더 편함.
    - image.shape -> (300, 240) 일 때.
      - count of row = 300
      - count of col = 240
    - image[2, 0]
      - 0th Column in Second row.
    - image[0, 2]
      - Second column in 0th row.
  - 1차원과 2차원 데이터 통칭해서 배열

#### 배열 처리 함수 (np.array)
  - cv2.flip(srt, flipCode) :    입력된 2차원 배열을 수직, 수평, 양축으로 뒤집음
    - x_flip - x축 기준 뒤집기 -> cv2.flip(image,0) 
    - y_flip - y축 기준 뒤집기 -> cv2.flip(image,1)
    - xy_flip - x,y축으로 한번씩 뒤집기. -> cv2.flip(image,-1) 
  - cv2.repeat(srt, ny, nx) :     입력 배열의 반복된 복사본으로 출력 배열을 채움.
    - ny를 통해 y축방향으로 즉 밑으로 얼마나 내릴지 결정. row증가.
    - nx를 통해 x축방향으로 즉 옆으로 몇개를 복사할지 결정. col 증가.
    - cv2.repeat(image , 1, 2) 라면 image가 1x2즉 ㅁ가 ㅁㅁ가 되어 나타남.
  - cv2.transpose() : 입력 행렬의 전치 행렬을 출력으로 반환
    - 전치 행렬이란 대각선을 기준으로 값이 바뀌는 것.
    
###  `채널 처리.`
- 이미지란 : 2차원 행렬로 표현이 되는 것이 아니라 `RGB 3가지`가 겹쳐져 있는 형태이다.
- OpenCV는 BGR의 형태로 되어있다.
- `Pixel-wise` 화소 단위로 순회 : 값을 저장할 때 BGR값을 Pixel 단위로 나옴.!
- 채널 관련 함수
  - cv2.merge(mv[,dst]) : 여러개의 단일채널 배열을 다차원 배열로 합성
    - (2,4) 형태의 3개의 BGR을 merge() 하였을 떼 (2,4,3) 형태가 됨 column vector처럼 이어 붙인달까?
    - (2,4) 형태의 4개를 merge하면 (2,4,4) 형태가 됨. |||| 이렇게 column vector처럼 이어 붙인달까..?
  - cv2.split(m[,mv]) : 다차원 배열을 여러개의 단일채널로 분리.q
    - split() 의 형태는 merge의 BGR이 (2,4) 짜리가 3개가 생김. (2,4,3) 아님, (3,2,4)가 됨,
    - why : 2,4짜리가 3개가 있으니까 3,2,4 
    - Split은 BGR을 쪼개서 출력이 가능하게 해줌. 
    - 파란색을 가지는 사진을 쪼개서 보면 파란색 부분이 좀 더 밝음, 초록색도 마찬가지.'
    - bgr을 3개로 나눌 수 있는데 반대로 생각하면 3개로 결합되어있는 상태가 되려면 3,2,4가 됨.

#### 사칙 연산
- openCV의 연산에서는 saturation 방식 사용 255+100 = 255, but numpy에서는 255+100 = 355%255
- cv2.add(src1, src2, [dst, mask, dtype]) -> dst
  - 연산 수행 방식 : `if mask(i) != 0: dst = src1(i)+src2(i)`
  - 만약 c = cv2.add(a,b,b,None) 일 때. 출력결과는 어떻게 될까? 
    -  src1 = a, src2 = b, dst = b, mask = None -> dst = c
    -  dst가 b와 c 이므로 b와 c는 같음.
  - 그렇다면 c = cv2.add(a,b,b.copy(), None) 일 때 출력 결과는? 
    - c와 b의 값은 다르다.
    - a 와 b를 더한 값을 b에 넣어주고 그 값이 c로 들어가기 때문에 1번문장에서는 같다.
    - but. 2번문장은 b.copy()를 통해 deep copy해주었기 때문에 다른 주소에 값이 저장됨. 
    - 즉 b가 수정되지않음 but a+b의 값인 b.copy()가 c에들어가므로 c와 b는 다름.
    - dst = b.copy()는 사실상 무의미함.
  - dtype은 cv2.CV_8S 와 같은 형태로 써 주어야 함. np안되더라...
    - 참고. type(cv2.CV_8S) 의 타입은 int형 이다.
    - openCV에서 dtype을 매개변수로 가지는 내장함수들은 모두 dtype에 int형이 들어가야 함. 
- cv2.subtract(srt1, srt2, [dst, mask, dtype])
- cv2.multiply(srt1, srt2, [dst, scale, dtype])
  - 여기서 scale이란 추가적으로 곱해주는 배율 입니다.
- cv2.divide(srt1, srt2, [dst, scale, dtype])
  - d = cv2.divide(a,b,c,2) 가 존재할 때 이 식의 값은? 2*a/b 이다. 또한 c == d 이다. scale은 곱해준다 무조건!
  - cv2.divide(scale, srt1, [dst, dtype]) -> scale/srt1 = dst
- cv2.addWeighted(src1, alpha, src2, beta, gamma, [dst, type])
  - saturate(src1 * alpha + src2 * beta + gamma)
- `mask`를 통해 관심영역 지정 가능. 0, 1을 통해 영역 지정가능 2들어가도 상관없더라..!
  - 0만 아니면 되더라고..! 
  - if mask !=0 .. 수식1.. 과 같은 형태이기 때문. 

### 지수, 로그, 제곱근 함수
- cv2.exp() : 모들 배열 원소의 지수 계산
- cv2.log() : 모든 배열 원소의 절대값에 대한 자연로그
- cv2.sqrt() : 제곱근 계산
- cv2.pow(src, power, [dst]) : 제곱 승수를 계산
  - 수식 -> dst(i) = src(i)^power
  - scaler  4차원으로 return
  - tuple -> tuple의 dim에 맞게 return

`2학기에 배우는 친구들`
- cv2.magnitude(x,y, [magnitude]) : $ magnitude =  \sqrt { x^{(i)}^2 + y^{(i)}^2 }  $ 
  - 아 왜 마크다운 안되냐...  휴... 아무튼 두 점 사이의 거리를 구하는 것과 같음.!
  -  수식 : dst = cv2.sqrt(cv2.pow(x,2) + cv2.pow(y,2))

- cv2.phase : 이거는 각도 계산.
  - angle(i) = a x tan2(y, x)·[180/\pi]

- cv2.cartToPolar() : 극좌표로 변환되서 동그마리가 됌.
- cv2.polarToCart()

#### 논리(비트) 연산 함수
- 얘의 연산방식. 10진수와 10진수를 비트연산할 경우. 둘 다 2진수로 바꿔서 계산하고 반환함.
- cv2.bitwise_and(src1, src2, [dst, mask]) : 논리 곱 연산인 AND 연산 수행. 
  - `if mask(i) != 0: dst(i) =  src1(i)^src2(i)`
- cv2.bitwise_or(src1, src2, [dst, mask]) : 논리 합 연산인 OR 연산 수행.
  - `if mask(i) != 0: dst(i) =  src1(i)|src2(i)`
- cv2.bitwise_xor(src1, src2, [dst, mask]) : 배타적 논리합 XOR
  - `if mask(i) != 0: dst(i) = src1(i) and src2(i)`
- cv2.bitwise_not(src, [dst, mask]) : not을 통해 비트반전.
  - dst = ~src 

#### 원소의 최솟값과 최댓값.
- cv2.min(src1, src2, [dst])
  - 수식 : `dst(i) = min(src1(i), src2(i))` 
- cv2.max()
- cv2.minMaxLoc(src, [mask] ) -> minVal, maxVal, minLoc, maxLoc 반환

#### 통계 관련 함수
- cv2.sumElems(src): 배열의 채널별로 각 원소들의 합 N을 반환함. src는 1부터 4사이의 채널을 갖는 입력배열
- cv2.mean(src, [mask] ) : 각 채널별 원소들의 평균을 계산하여 스칼라 값으로 반환. src는 위와 같음 mask부분 제외.
- cv2.meanStdDev()  : 배열 원소들의 평균과 표준편차를 계산한다.
- cv2.countNonZero() : 0이 아닌 배열의 원소 개수 N을 반환.
- cv2.reduce(src, dim, rtype, [dst, dtype]) : 행렬 축소 
  - src의 type은 float32 혹은 float64 만 가능.
  - dim = 0 => 한 행으로 감축, dim =1 => 한 열로 갑축 
  - rtype : 축소 타입 고르기 0 : 합, 1 : 평균, 3 : 최대값, 4 : 최소값
    - cv2.REDUCE_SUM : 행렬의 모든 행 또는 열을 한방향으로 찌부 시킴 그리고 행 또는 열의 합을 return 
    - cv2.REDUCE_AVG : 행렬의 행 또는 열의 평균
    - cv2.REDUCE_MAX : 행렬의 행 또는 열의 최댓값
    - cv2.REDUCE_MIN : 최솟값.
- cv2.sort(src, flags, [dst])   : 행렬 정렬
  - flags : 연산 플래그, 다음의 상수를 `+`로 조합해서 정렬 방식 구성.
    - cv2.SORT_EVERY_ROW     0  -> 각 행을 독립적으로 정렬.
    - cv2.SORT_EVERY_COLUMN  1  -> 각 열을 독립적으로 정렬
    - cv2.SORT_ASCENDING     0  -> 오름차순으로 정렬
    - cv2.SORT_DECENDING     16 ->  내림차순으로 정렬
  - 넘파이 사용시 사용 가능한 정렬.
    - numpy는 OpenCV와 다르게 1, 0 flag가 반대!
    - np.sort(src, axis = 1) -> x축 방향 정렬.
    - np.sort(src, axis = 0) -> y축 방향 정렬.
    - np.sort(src, axis = 1)[:, ::-1] -> 열 방향 내림차순 정렬.
---
## 6주차 내용

- 행렬 원소 접근 방법 : 
``` python:
[mat[row, col]*=2 for row in range(image.shape[0]) for col in range(image.shape[1])]
```
- 행렬 원소를 item과 itemset으로 접근하기. 
  - mat.itemset((i,j), mat.item(i,j)*2))
- 행렬을 통한 slice 방법 사용시 y,x가 바뀌는 것에 주의, 
  - 근데 생각해보면 image[100:200, 0:300] 일 때 100,300 크기의 창을 띄운다고 생각하면 이해가 되기도 함.
  - drawing `100th row to 200th row` and `0th col to 300th col`

#### OpenCV와 numpy의 0 미만 255 이상의 화소값 처리 방식 다름 주의
- OpenCV : 255+100 = 360 -> 255 (stauration 방식)
  - numpy에서 사용하려면 np.clip(image, minValue, maxValue)
  - `cv2.add(iamge, 100)`, `cv2.subtract(image,100)`
- numpy  : 255+100 = 350%255 -> 104 (modulo 방식)
  - `image + 100`, `image-100`

- np.clip(image, 0, 255) -> 0부터 255까지 처리.
- `cv2.addWeighted(image1, alpha, image2, beta, c)` -> result = image1 * a + image2 * b + c
  -  cv2.add(image1*alpha, image2*beta) 와 같음.

### 대비 : 같은 색도 인접한 색에 밝기에 따라서 다르게 보임 add, scaledAdd addWeighted
- cv2.add(src1, src2, dst, mask, dtype)
  - cv2.add의 경우 src에 sclar를 곱하고 싶을 때 src1 = src*scalr 형태가 됨.
  - 따라서 add가 적용되기 전 numpy.ndarray와 곱하기 때문에 255를 넘을 수 있음.
  - `cv2.clip(src1, min_value, max_value).astype('uint8')` 을 통해 잘라주어야 함.
  -  이를 보완하기 위해 scaledAdd가 등장.!
- cv2.scaledAdd(src1, scaler, src2) -> dst
  - 일정 값을 곱하고 같은 크기의 이미지를 더함.
  - dst = src1*scaler + src2 
- cv2.scaledAdd(scalr를 곱할 이미지, sclar, 더할 이미지) -> dst
  - cv2.add(src1, src2, dst, mask, dtype)인데
  - cv2.scaledAdd(src1, scalr, src2)는 다름.

- cv2.addWeighted(src1, scalr1, src2, sclar2, avg) 
  - src1 * sclar + src * sclar2 + avg
  - OpenCV 내의 scaledAdd를 사용하기 때문에 saturation 연산이 적용됨.
  - 위와 같이 sclar을 곱해주면 전체적인 밝기가 증가/감소하기 때문에 avg를 통해 밝기 조절을 해줌.
  - `cv2.addWeighted(img1, 0.6, img2, 0.4, 0)`
    - img1에 0.6을 곱한 값과, img2에 0.4를 곱한값을 더해줌.
    - 자동 saturation 연산 적용.
      - img의 타입은 numpy.ndarray, 
      - 직접적으로 img1 * 2 를 할 경우 255 넘을 수 있음 -> modulo 연산 적용.
      - but addWeighted는 직접적으로 곱하고 더해주지 않음.

### 히스토그램
#### 관측값의 개수를 겹치지 않는 다양한 계급으로 표시하는 것.
- Histogram의 value / count of Histogram => P(i), 특정 Pixel이 등장할 확률을 구할 수 있음.
- cv2.calcHist(image, channels, mask, histSize, ranges)
  - image    : input Image
  - channels : 히스토그램 계산에 사용되는 차원 목록. 
    - 2차원 히스토그램을 그리고 싶다면 이친구 이용. 
  - mask     : 특정 영역만 계산하기 위한 마스크 영역.
  - histSize : 각 차원의 히스토그램 배열 크기. 단일 채널 8bit 행렬이라 할 때. ranges[1] = 256, ranges/bin_width(bin의 폭)
    - 반대로  bin, gap, bin width = ranges[1]/histSize 
  - ranges   : 각 차원의 히스토그램의 범위.
  - [accumulate] : 각 차원의 히스토 그램의 범위, channel과 같이 쓰이지 않을까 싶다.
- cv2.calcHist(images, [0], None, [histSize], ranges)
  - histSize는 벡터 형태, scalr 안됨. ranges = [0,256]
``` python:
def calcHist_custom(images, histSize, ranges = [0, 256]):
  hist = np.zeros((histSize,1), np.float32)
  gap = ranges[1]/histSize
  
  for row in images:
    for pix in row:
      hist[pix//gap] +=1
```

#### 히스토그램 그리기
``` python:
def draw_histo(hist, shape = (200,256)):
  hist_img = np.full(shape, 255, np.uint8)
  cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) # 이미지의 row 수가 max값이 되게 정규화 진행.
  gap = hist_img.shape[1]/hist.shape[0] # 이미지의 col수/히스토그램의 size = (width/histSize) -> gap
  
  for i, h in enumerate(hist):
    x = int(round(i*gap))
    w = int(round(gap))
    cv2.rectangle(hist_img, (x,0, w, int(h)) , 0, cv2.FILLED)
    # x,0에 w길이 만큼 width, h길이만큼 height 그리기. 색상은 0, thickness는 굵기! -> cv2.FILLED 쓰면 안에 꽉참
    
  return cv.flip(hist_img, 0) # x축으로 회전.
```

- `cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)` ->  n = (filtered - np.min()) / (np.max() - np.min())


