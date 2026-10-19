#定义函数 （使用*args去接受：可变位置参数）
def test1(*args):
    #此处args的值，是一种新的数据类型，叫元组
    print(args)
test1('张三','男',18,172)

 #定义函数（使用**kwargs去接受：可变关键字参数）
def test2(**kwargs):
    print(kwargs)
test2(nanme='张三')
#定义函数（同时使用：可变位置参数，可变关键字参数）