def test1():
    print(' in test1')
    test2()
    print(' exit test1')
def test2():
    print(' in test2')
    test3()
    print(' exit test2')
def test3():
    print(' in test3')
    print('***test3ing****')
    print(' exit test3')
test1()