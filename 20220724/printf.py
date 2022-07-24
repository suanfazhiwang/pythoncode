# 1. 向计算机发出指令打印520
# 2. 把代码编译成计算机能听懂的计算机语言
# 3. 做出相应的执行 在控制台上输出结果
# print函数可以输出数字  字符串  含有运算符的表达式
# print函数可以将内容输出到显示器或者文件中
# 还有换行和不换行的输出形式
print(520)

print('hello world')
print("hello world")

print(3+1)# 输出为4

# 将数据输出到文件中
# 注意点：1. 所指定的盘符存在   2. 使用file = fp
fp = open('C:/pythoncode/pythoncode/20220724/text.txt', 'a+')  # a+的意思是如果文件不存在就创建，存在就在文件内容的后面继续追加
print('hello world', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行当中）
print('hello world', 'python')

# 转义字符
# 换行：\n   回车\r   水平制表位\t   退格\b
print('hello\rworld')# 只会输出world  world将hello进行了覆盖
print('hello\bworld')# hellworld   将o退没了
# 当字符串中包含反斜杠、单引号和双引号等有特殊用途的字符时，必须使用反斜杠对这些字符进行转义（转换一个含义）
#         反斜杠 :\\
#         单引号:\'
#         双引号: \“

