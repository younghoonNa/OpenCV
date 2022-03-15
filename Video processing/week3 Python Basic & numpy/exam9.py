import exam9_header as mod
from exam9_header import write # exam9_header 의 write 만 import


mod.say()
ret = mod.calc_area(type=1, a=5,b=5)
area, msg = mod.calc_area(2,5,5)
area2, _ = mod.calc_area(3, 10, 7, 5)

print(type(ret))
print(type(area), type(msg))
write(ret[0], ret[1])
write(area, msg)
write(area2, "평행사변형")