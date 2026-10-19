#/ 前边只能用位置参数， *后面只能用关键字参数，同时出现时/必须在*号前面
def greet(name,/,gender, *,age,weight):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{weight}')
greet('张三','男',age=18,weight=120)