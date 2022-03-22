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
