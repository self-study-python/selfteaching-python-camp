# 加法
def add(x, y):
    return x+y


# 减法
def subtraction(x, y):
    return x - y


# 乘法
def chengfa(x, y):
    return x * y


# 除法
def chufa(x, y):
    return x / y


print('输入1：加法；2：减法；3：乘法；4；除法')

input_math = int(input('请输入1/2/3/4其中的一个数字：'))

first = int(input('第一个数字'))
second = int(input('第二个数字'))

if input_math == 1:
    print(add(first, second))

elif input_math ==2:
    print(subtraction(first, second))

elif input_math ==3:
    print(chengfa(first, second))

elif input_math ==4:
    print(chufa(first, second))

else:
    print('您的输入有误')

# 出现的问题：input_math无论输入什么值，最后输出都是您的输入有误，一开始觉得是不是
            # 要给判断语句加break，当然这是不存在的，循环语句才需要
# 原因：最后发现问题出在input，input传入的值是字符串，需要转化成int类型才能进行判断

