#boolean type返还bool：True False(布尔值）
from operator import truediv

a = True #自己定义的布尔值
b = False
print(type(a),a)
print(type(b),b)
#布尔类型是int类型的字类型 1表示True，0表示False
print(int(True))
#转换函数bool（）除0以外任何数转化为布尔值后都为true
print(bool(12))
#除空字符串以外任何字符串，转化为布尔值都是true
print(bool('hello'))
print(bool(''))