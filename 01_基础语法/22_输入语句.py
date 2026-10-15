#使用input（）获取用户的输入
name = input('请输入你的姓名')
age = input('请输入你的年龄')
print(f'{name}, 你今年的年龄是{age}')
#将age换为整型
age = int(age)
print(f'{name}, 你明年的年龄是{age + 1}')