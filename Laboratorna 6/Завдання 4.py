import math
a=[0.1,1,4,3,-0.45]
n=len(a)
b=[]
z=0
for i in range(0,n):
    if math.fabs(a[i])<=1:
        z+=1
    if math.fabs(a[i])>1:
        b.append(a[i])
for j in range(z):
    b.append(0)
print('Заданий масив',a)
print('Відсортований масив',b)






