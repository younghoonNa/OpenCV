import numpy as np, cv2

image1 = np.zeros((50,512), np.uint8)
image2 = np.zeros((50,512), np.uint8)

rows, cols = image1.shape[:2] # 0부터 1까지 출력 50, 512
# print(rows, cols)

for i in range(rows):
    for j in range(cols):
        image1.itemset((i,j), j//2);
        image2.itemset((i,j), j//20*10) # 연산자 우선순위 : j//20 후 * 10
        print(j//2)

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)