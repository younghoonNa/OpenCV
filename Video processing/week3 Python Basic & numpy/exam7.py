kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum1, sum2, sum3, sum4 = 0,0,0,0

for i in range(0,5):
    sum1 += kor[i] + eng[i]

for k in kor:
    sum2 = sum2 + k

for e in eng:
    sum2 = sum2 + e

for i, k in enumerate(kor):
    sum3 = sum3 + k + eng[i]
    # print(i , " ", k)
    # i에는 인덱스가 k에는 kor[i] 값이 들어옴.


for k, e, in zip(kor, eng):
    sum4 = sum4 + k + e

print("sum1 = ", sum1), print("sum2 = ", sum2)
print("sum3 = ", sum3), print("sum4 = ", sum4)