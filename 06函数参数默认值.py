#定义函数（设置参数默认值）
def greet(name,gender,age,height,msg='你好'):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{height}')
    print(msg)
greet('张三','男',age=18,height=120)