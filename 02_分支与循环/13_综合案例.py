print('欢迎来到：答题挑战赛（输入q直接退出）\n')

#题目与答案
ques1, ans1 = 'python中用于输出的函数是', 'print'
ques2, ans2 = 'python中用于表示逻辑“并且”的关键字是', 'and'
ques3, ans3 = 'python是解释型还输编译型', '解释型'

#最多可尝试次数
max_tries = 3
#总关卡数
total_levels = 3
#是否处于可游戏状态
is_playing = True

#根据题目数量循环
for level in range(1, total_levels + 1):
    print(f'****第{level}关****')
    #取出当前关卡对应题目和答案
    if level == 1:
       question, answer = ques1, ans1
    elif level == 2:
        question, answer = ques2, ans2
    else:
        question, answer = ques3, ans3
    tries = 1
    # 根据用户输入决定做什么
    while tries <= max_tries:
        user_input = input('' + question)
        if user_input == answer:
            print('回答正确 \n')
            break
        elif user_input == ' ':
            print('输入为空，重新做答')
            continue
        elif user_input == 'q':
            print('你已退出\n')
            is_playing = False
            break
        else:
            leave = max_tries - tries
            if leave > 0:
                print(f'错误还有{leave}次机会 \n')
                tries += 1
                continue
            else:
                print(f'失败，答案为{answer}')
                is_playing = False
                break
    if not is_playing:
                break
if is_playing:
    print('通关')

