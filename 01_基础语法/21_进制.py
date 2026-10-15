#num = 0b 11001（二进制）；0o（转八进制） 0x（十六进制）————转十进制
num1 = 0b11001
#使用bin（）将十进制转化为二进制————转化为字符串
#使用oct（）将十进制换转化为八进制————转化为字符串
#使用hex（）将十进制转换为16进制————转化为字符串
#int 其他进制转十进制数字
value1 = int('0b11001', 2)
value2 = int('0o1034', 8)
value3 = int('0x1cf', 16)
print(value1)
print(value2)
print(value3)
