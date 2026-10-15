for n in range(10):
    print(f'{n}helllo')
print(f'我在for外，n是 {n}')

for m in 'abcdef':
    print(m)
#只要不在for循环内部修改可迭代对象，一般不会死循环