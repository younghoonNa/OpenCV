import numpy as np, cv2

data = [ 10, 200, 5, 7, 9,
         15, 35, 60, 80, 170,
         100, 2, 55, 37, 70]

m1 = np.reshape(data, (3,5))
m2 = np.full((3,5), 50)

m_min = cv2.min(m1, 30)
m_max = cv2.max(m1,m2)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(m1)

print("[m1] = \n%s\n" % m1)
print("[m_min] = \n%s\n" % m_min)
print("[m_max] = \n%s\n" % m_max)

print("m1 행렬 최솟값 좌표 %s, 최솟값 : %d" %(min_loc, min_val))
print("m1 행렬 최댓값 좌표 %s, 최댓값 : %d" %(max_loc, max_val))

