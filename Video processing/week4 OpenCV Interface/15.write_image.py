import cv2

image = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10) # 0 ~ 100 높을수록 화질 굿.
params_png = (cv2.IMWRITE_PNG_COMPRESSION, 9) # 0~9 높을수록 용량 작아짐, 압축시간 증가.

cv2.imwrite("images/write_test1.jpg", image)
cv2.imwrite("images/write_test2.jpg", image, params_jpg)
cv2.imwrite("images/write_test3.png", image, params_png)
cv2.imwrite("images/write_test4.png", image)
print("저장 완료")