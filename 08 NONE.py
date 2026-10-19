#none是一个特殊的字面量，他表示空值/无值/无意义
msg = None
#none的类型是nonetype
print(type(msg))
#none转化为布尔值是False
print(bool(msg))
if msg:
    print('你好')

#不能参与数字运算也不能与字符串拼接