import numpy as np, cv2

m = np.random.randint(0, 100, 15).reshape(3,5)

#행렬 원소 정렬
sort1 = cv2.sort(m, cv2.SORT_EVERY_ROW)
sort2 = cv2.sort(m, cv2.SORT_EVERY_COLUMN)
sort3 = cv2.sort(m, cv2.SORT_EVERY_ROW + cv2.SORT_DESCENDING) #행 단위 내림차순.
sort4 = np.sort(m, axis = 1) #가로방향
sort5 = np.sort(m, axis = 0) #0이 행방향
sort6 = np.sort(m, axis= 1)[:, ::-1] # 열 방향 내림차순 정렬

titles = ['m', 'sort1', 'sort2', 'sort3', 'sort4', 'sort5', 'sort6']

for title in titles:
    print("[%s] = \n%s\n" % (title, eval(title)))
