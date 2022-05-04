import numpy as np, cv2

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.zeros((2,2))

# image = [
#     12,20,30,0,
#     8, 12,2,0,
#     34, 70, 37, 4,
#     112, 100, 25, 12
# ]

# image = np.array(image).reshape(4,4)


result = np.zeros((image.shape[0]//2, image.shape[1]//2), np.float32)


for row in range(0, image.shape[0]-1, 2):
    for col in range(0, image.shape[1]-1, 2):

        li = []

        for k_row in range(kernel.shape[0]):
            for k_col in range(kernel.shape[0]):
                li.append(image[row+k_row, col+k_col])
                nd = np.array(li)
                max_val = np.max(nd)

        result[row//2, col//2] = max_val

        print(li)

result = np.array(result, np.uint8)
print(result)
cv2.imshow("result", result)
cv2.waitKey(0)