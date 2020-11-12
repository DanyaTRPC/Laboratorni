n= int(input('Введіть значення n='))
k=[]
while n>0:
    x= float(input('Введіть значення x= '))
    k.append(x)
    n-=1
print(min(k))

