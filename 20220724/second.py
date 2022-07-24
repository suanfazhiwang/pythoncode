# 将我能够认识的符号和数字对应好，然后做成一张表叫ASCII表，告诉计算机某种符号你应该使用哪个整数表示,
# ’A’使用了8个位（置）才能装得下我，在计算机中他们叫一个字节
print(chr(0b100111001011000))   # 输出的是乘
print(ord('乘'))   # 输出十进制的100111001011000

# 变量、函数、类、模块和其它对象的起的名字就叫标识符
# 规则：
# 字母、数字、下划线_
# 不能以数字开头
# 不能是我的保留字
# 我是严格区分大小写的

name = '玛丽亚'
print(name)

# 变量由三部分组成
# 标识：表示对象所存储的内存地址，使用内置函数id(obj)来获取
# 类型 :表示的是对象的数据类型，使用内置函数type(obj)来获取
# 值:表示对象所存储的具体数据，使用print(obj)可以将值进行打印输出
print('标识', id(name))
print('类型', type(name))
print('值', name)

# 当多次赋值之后，变量名会指向新的空间

name = '大笨蛋'
print('标识', id(name))      # 这里会发生变化
print('类型', type(name))
print('值', name)

# 常用的数据类型
# 整数类型   int   98
# 浮点数类型float 3.14159
# 布尔类型  bool True ,False  只能是真或者假
# 字符串类型str  ’人生苦短，我用Python’

# 整数类型
# 英文为integer，简写为int，可以表示正数、负数和零
# 整数的不同进制表示方式
# 十进制默认的进制
# 二进制以0b开头
# 八进制以0o开头
# 十六进制0x开头
n1 = 90
n2 = -76
n3 = 0
print('类型', type(n1))
print('类型', type(n2))
print('类型', type(n3))

# 浮点类型
# 浮点数整数部分和小数部分组成
# 浮点数存储不精确性
# 使用浮点数进行计算时，可能会出现小数位数不确定的情况
print(1.1+2.2)   # 3.3000000000000003
print(1.1+2.1)   # 3.2

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))   # 3.3

# 布尔类型
# 用来表示真或假的值
# True表示真，False表示假
# 布尔值可以转化为整数
# True1
# False0
f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))

print(True+1)    # 2
print(False+1)   # 1
print(f1+1)    # 2
print(f2+1)   # 1

# 字符串类型
# 字符串又被称为不可变的字符序列
# 可以使用单引号’’ 双引号”” 三引号’’’  ’’’ 或””” ”””来定义
# 单引号和双引号定义的字符串必须在一行
# 三引号定义的字符串可以分布在连续的多行
str1 = '人生苦短，何妨一试'
str2 = "人生苦短，何妨一试"
str3 = """人生苦短，
何妨一试"""
str4 = '''人生苦短，
何妨一试'''

print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))

# 为什么需要数据类型转换？
# 将不同数据类型的数据拼接在一起
name = '张三'
age = 20
print(type(name), type(age))
# print('我叫'+name+'今年，'+age+'岁')    # +连接符，将str类型与int类型链接的时候报错，解决方案：类型转换
print('我叫'+name+'今年，'+str(age)+'岁')   # 这样就可以了   就像c中的强制类型转换

print('----------str()将其他类型转为str类型----------')
a = 10
b = 198.2
c = False
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))

# int()将其他类型转为int类型
# 但是文字类和小数类的字符串无法转为int   只能转数字串整数！！！
# 同时浮点数转为int   抹零取整

# float()将其他数据了类型转成浮点数
# 1. 文字类无法转为浮点类型
# 2. 整数转为浮点数末尾.0






































