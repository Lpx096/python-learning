age = int(input('请输入你的年龄'))
hes_report = input('你是否提交了体检报告？ （是/否）')
level = int(input('请输入你的会员等级 (1/2/3)'))

print('******程序识别如下******')
if 18 <= age <= 65:
    print('您的年龄符合比赛要求')
    if hes_report == '是':
        print('您已提交体检报告')
        print('可以参赛')
        if level == 1:
            print(f'尊敬的{level}会员,比赛后可以领取t袖')
        elif level == 2:
            print(f'尊敬的{level}会员,比赛后可以领取跑鞋')
        elif level == 3:
            print(f'尊敬的{level}会员,比赛后可以领取耳机')
        else:
            print('输入会员有误')
    elif hes_report == '否':
        print('未提交体检报告，不能参赛！')
else:
    print('您的年龄不符合比赛要求')
