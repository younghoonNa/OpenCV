def calc_area (type, a, b, c = None):
    if type == 1:
        result =  a * b
        msg = "사각형"
    elif type == 2:
        result = a * b / 2
        msg = "삼각형"

    elif type == 3:
        result =  (a+b)*c /2
        msg = "평행사변형"

    return result, msg

def say():
    print("넓이를 구해요.")

def write(result, msg):
    print(msg, "넓이는", result, "m2 입니다.")

say()
ret = calc_area(type=1, a=5,b=5)
area, msg = calc_area(2,5,5)
area2, _ = calc_area(3, 10, 7, 5)

print(type(ret))
print(type(area), type(msg))
write(ret[0], ret[1])
write(area, msg)
write(area2, "평행사변형")