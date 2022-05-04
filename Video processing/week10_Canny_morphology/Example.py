import cv2, numpy as np

image = cv2.imread("images/edge.jpg", cv2.IMREAD_COLOR)


# gray_img = np.zeros(image.shape, np.float32)
gray_img = (0.299 * image[:,:,2]) + ( 0.587 * image[:,:,1]) + (0.114 * image[:,:,0])
gray_img = np.array(gray_img, np.uint8)

cv2.imshow("gr", gray_img)
cv2.waitKey(0)