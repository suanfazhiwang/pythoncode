# 常用运算符
# 1. 算数运算符   （1）标准算数运算符 除/  整除// （2）取余运算符 % （3）幂运算符 **
# 2. 赋值运算符
# 3. 比较运算符
# 4. 布尔运算符
# 5. 位运算符

# 1. 算数运算符
print(1/2)   # 除法   得0.5
print(11//2)   # 整除   得5
print(11%2)   # 取模   得1
print(2**3)   # 二的三次方


print(-9//-4)   # 得2
print(9//-4)   # -3
print(-9//4)   # -3    一正一负向下取整


print(9%-4)   # -3
print(-9%4)   # 3   公式  余数=被除数-除数*商

# 2. 赋值运算符
# 支持链式赋值   就离谱
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

# 值得注意
a=3    # 这里是int
a/=2
print(a,type(a))    # 这里就变成了float

# 解包赋值   这个太好了不需要中间变量了
a=10
b=20
print('交换之前值',a,b)
a,b=b,a
print('交换之后值',a,b)


# 3. 比较运算符
# 比较运算符得结果为bool类型   True和False
# ==   !=   比较的是值
# is   is not   比较的是id

# 我觉得这里是离谱的地方   a=10   b=10   然后他俩的id标识还一样    指向同一地址
a=10
b=10
print(a==b)
print(a is b)
# 都是对的

# 数组里不适用
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(lst1 is not lst2)


# 4. 比较运算符
# and   全对才对   有错就错
# or    有对就对   全错才错
# not   运算数为true  结果为false      运算数为false   结果为true
a,b=1,2
print(a==1 and b==2)
print(a==1 and b==3)

print(a==1 or b==3)
print(a==2 or b==3)

# not  对bool类型操作数取反
f1=True
f2=False
print(not f1)
print(not f2)


#in 和not in    在不在其中  如下
s='helloworld'
print('w' in s)
print('w' not in s)
print('a' in s)
print('a' not in s)


# 5. 位运算符    将数据转成二进制进行计算
# 位与&   对应数位都是1，结果数位才是1，否则为0
# 位或 |   对应数位都是0，结果数位才是0，否则为1
# 左移位运算符<<   高位溢出舍弃，低位补0
# 右移位运算符>>   低位溢出舍弃，高位补0
print(4&8)   # 0
print(4|8)   # 12

print(4<<1)   # 相当于乘二    8
print(8<<1)   # 16

print(4>>1)   # 相当于除2   2
print(8>>1)   # 4


# 运算符的优先级
# 1. 算术运算符   先算乘除再算加减   有幂运算先进行幂运算
# 2. 位运算      先算算数运算  再算位运算
# 3. 比较运算符   第三算
# 4. 布尔运算     比较运算完成后进行布尔运算
# 5. 赋值运算符   最后运算
























