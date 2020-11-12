import math
n=int(input('Введіть значення n= '))
A=[]
B=[]
s1=0
s2=0
for i in range(1,n+1):
    a=((2*i-1)*math.cos(i))/(i**2)
    if a>0:
        A.append(a)
    else:
        B.append(a)
for j in A:
    s1+=j**2
for t in B:
    s2+=t**2
if s2<s1:
    z=-1
else:
    z=1
print('z=',z)



