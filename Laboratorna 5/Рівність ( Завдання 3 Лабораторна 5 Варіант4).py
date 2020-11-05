import math
x= float(input('Введіть значення x= '))
a= float(input('Введіть значення a= '))
n= int(input('Введіть значення n= '))
s=1
if n>0 and a>0 :
    for i in range(1,n+1):
        k=(x* math.log1p(a-1) )**i/math.factorial(i)
        s+=k
    e=(a**x)-s
    print(e)
else:
    print('Рівність не виконується')


