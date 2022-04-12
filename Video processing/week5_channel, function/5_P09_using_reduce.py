import numpy as np, cv2

m1 = np.ones((3,6), np.float32)
m1 = np.array([[1.,10.,3.,6.,5.,6.],
      [5, 3,5,7,9,11],
      [2, 8,2,3,5,9],
      ])

# m1 = m1.reshape(3,6)
print(m1, "===")

m2 = cv2.reduce(src = m1, dim = 0, rtype=1)
print(m2)