for day in range(1,31):
    print(f'*****第{day}天*****')
    for group in range(1,4):
        print(f'这是第{group}组')
    print(f'{day}天完成 \n')
print(f'为期{day}天已完成')
#while
day = 1
while day <= 30:
    print(f'*****第{day}天*****')
    group = 1
    while group <= 3:
        print(f'这是第{group}组')
        group += 1
    print(f'{day}天完成 \n')
    day += 1
print(f'为期{day-1}天已完成')