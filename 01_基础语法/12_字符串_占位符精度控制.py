#%m.ns
#m 字符串的最小宽度，位数不够自动用空格补全 正数右对齐·负数左对齐
#n 精度控制 最多输出n个字符
#%m,nf n精度控制 四舍五入 m 整体宽度
name = '张三'
weight = 64.56
info = '我叫%-6.3s，体重是%-4.6f' %(name, weight)
print(info)