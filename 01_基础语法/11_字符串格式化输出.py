#写法一 直接用加号进行拼接，只能字符串拼接
from os import name
name = '张三'
gender = '男'
info1 = '我叫' + name
info1= '我叫' + name +',我是' + gender +'生'
print(info1)
#写法2 使用占位符,%s是万能的
info2 = '我叫%s, 我是%s生' % (name, gender)
print(info2)
#写法3 使用f-string 最简洁
info3 = f'我叫{name} , 我是{gender}生'
print(info3)