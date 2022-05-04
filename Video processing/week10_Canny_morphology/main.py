import cv2, numpy as np

def put_string(frame, text, pt, value, color = (120, 900, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0,0,0), 2)
    cv2.putText(frame, text, pt   , font, 0.7, color, 2)


capture = cv2.VideoCapture(0)

if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨.")

print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))


while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, 'EXPOS : ', (10,40), exposure)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)


    gray_img = np.zeros(frame.shape[:2], np.float32)
    gray_img = (0.299 * frame[2]) + ( 0.587 * frame[1]) + (0.114 * frame[0])

    cv2.imshow("sg", gray_img)

capture.release()
