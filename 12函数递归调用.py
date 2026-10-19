#指函数自己调用自己
def welcome(n):
    if n > 1:
        welcome(n-1)
    print(f'welcome{n}')
welcome(5)