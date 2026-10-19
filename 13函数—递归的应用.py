#使用递归求阶乘
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
reslute = fact(5)
print(reslute)