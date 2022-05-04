import cv2

def put_string(frame, text, pt, value, color = (120, 900, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0,0,0), 2)
    cv2.putText(frame, text, pt   , font, 0.7, color, 2)

def onTrackbar(th):

    rep_edge = cv2.GaussianBlur(image_gray, (5,5), 0) # 에지 검출 위해 영상에서 부드러운 부분 제거.
    rep_edge = cv2.Canny(rep_edge, th, th*2, 5) # 에지 검출
    h,w = frame.shape[:2]
    cv2.rectangle(frame, (0,0,w,h), 255, -1)
    color_edge = cv2.bitwise_and(image_gray, image_gray, mask = rep_edge)
    cv2.imshow("color edge", color_edge)

capture = cv2.VideoCapture(0)

if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨.")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    t_low = 30
    t_high = 70

    put_string(frame, 'THRESHOLD : ', (10,40), (t_low, t_high))
    title = "View Frame from Camera"

    image_bgr = cv2.repeat(frame, 1,2)
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    rep_edge = cv2.GaussianBlur(image_gray, (5,5), 0) # 에지 검출 위해 영상에서 부드러운 부분 제거.
    rep_edge = cv2.Canny(rep_edge, t_low, t_high, 5) # 에지 검출
    h,w = frame.shape[:2]
    cv2.rectangle(rep_edge, (0,0,w,h), 255, -1) # -> 왼쪽은 흰색으로 채움.
    color_edge = cv2.bitwise_and(image_gray, image_gray, mask = rep_edge)
    cv2.imshow("color edge", color_edge)

capture.release()