#and判断其两侧值是否都为true
print(True and True)
print(True and False)
#and具备逻辑短路的能力
#and返回的不一定是布尔值，他返回的某个参与计算的本身
#规则；and会先看左边，左边为假就直接返回左边，否则返回右边
#备注：若参与and运算的值不是布尔值，那python会自动转化为布尔值，然后再进行逻辑操作
print(2 - 2 and True)
print('' and True)
#or判断两侧，是否至少有一个为true，输出为true
#or同样具有逻辑短路的能力
print(9>0 or 3 / 0)
#or返回也不一定是布尔值
#规则；or会先看左边，左边为假就直接返回左边，否则返回右边
#备注：若参与or运算的值不是布尔值，那python会自动转化为布尔值，然后再进行逻辑操作

#not用于取反
print(not True)
print(not False)
print(not 9 // 4)
print(not 9 % 4)
print(not 2 - 2)
