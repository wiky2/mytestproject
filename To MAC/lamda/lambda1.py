# lambda.py   
#-*- coding:gb2312 -*
def fun1(n):   
    return lambda m:m**n   
   
def fun2(m, n):   
    return m+n   
   
# 演示通常的lambda用法   
f1 = lambda x,y,z: x*2+y+z   
print f1(3,2,1)   
# 动态生成一个函数   
f2 = fun1(2)   
print f2(4)   
   
# lambda用作函数参数的写法   
print fun2(3, (lambda x:x+1)(2))  