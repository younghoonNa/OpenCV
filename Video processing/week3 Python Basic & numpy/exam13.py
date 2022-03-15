import numpy as np

np.random.seed(10)

a = np.random.rand(2,3)
b = np.random.rand(3,2)
c = np.random.randn(6)
d = np.random.randint(1,100, 6)
e = np.reshape(c, (2,3))
f = d.reshape(2, -1)

print("a 형태 : ", a.shape, '\n', a)
print("b 형태 : ", b.shape, '\n', b)
print("c 형태 : ", c.shape, '\n', c)
print("d 형태 : ", d.shape, '\n', d)
print("e 형태 : ", e.shape, '\n', e)
print("f 형태 : ", f.shape, '\n', f)

print("다차원 객체 1차원 변환 방법.")
print("a = ", a.flatten())
print("b = ", np.ravel(b))
print("c = ", np.reshape(c, (-1, )))
print("d = ", d.reshape(-1,))