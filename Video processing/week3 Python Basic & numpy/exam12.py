import numpy as np

a = np.zeros((2,5), np.int)
b = np.ones((3,1), np.uint8)
c = np.empty((1,5), np.float)
d = np.full(5,15,np.float32)

print(type(a), type(a[0]), type(a[0][0]))
print(type(b), type(b[0]), type(b[0][0]))
print(type(c), type(c[0]), type(c[0][0]))
print(type(d), type(d[0]))

print("c 형태 :", c.shape, 'd 형태 : ', d.shape) # 객체 형태 출력
print(a), print(b) # 객체 원소 출력
print(c), print(d)
