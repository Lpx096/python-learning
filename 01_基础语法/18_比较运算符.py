#==相等 ！=不等 >判断左侧是否大于右侧 ;<  ;>= ;<= ;以上运算符同样适用于字符串
#字符串比较时，是依次比较字符的unicode编码，使用ord（）查看字符unicode码，使用chr（）将unicode码转换为字符
print(ord('a'))
print(ord('我'))
print(chr(97))