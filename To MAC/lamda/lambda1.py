# lambda.py   
#-*- coding:gb2312 -*
def fun1(n):   
    return lambda m:m**n   
   
def fun2(m, n):   
    return m+n   
   
# ��ʾͨ����lambda�÷�   
f1 = lambda x,y,z: x*2+y+z   
print f1(3,2,1)   
# ��̬����һ������   
f2 = fun1(2)   
print f2(4)   
   
# lambda��������������д��   
print fun2(3, (lambda x:x+1)(2))  