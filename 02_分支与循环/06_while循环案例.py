print('你在密室，回答正确可以逃脱')
riddle = '你是什么人'
answer = '你的心上人'
guess = ''

while guess != answer:
    print(f'问题: {riddle}')
    guess = input('请输入')
    if guess == answer:
        print('回答正确，成功')
    else:
        print('回答错误')