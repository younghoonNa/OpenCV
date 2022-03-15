list1 = [1,2,3,4]
list2 = [1, 1.5, 'a', 'a', '문자열']
tuple1 = (1,2)
tuple2 = (1,1.5, 'b', 'b', '문자열')
dict1 = {'name' : '배종욱', 'email':'daum.net'}
set1, set2 = set(list2), set(tuple2) #set은 중복 처리를 허용하지 않아!!!!!!


list1[0] = 5
list2.insert(3,'b')
#tuple[0] = 5
dict1['email'] = 'naver.com'

print('list1', list1, type(list1))
print('list2', list2, type(list2))
print('tuple1', tuple2, type(tuple1))
print('tuple2', tuple2, type(tuple2))
print('set1', set2, type(set1))
print('set2', set2, type(set2))
print('dict1', dict1, type(dict1))