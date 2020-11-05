x= float(input('Введіть значення x= '))
a= float(input('Введіть значення a= '))
n= int(input('Введіть значення n= '))
s=0

if n>0 :
    k=(x+a)**2
    n=n-1
    while n > 0:
        k=(k+a)**2
        n=n-1
    k=k+a
    print(k)


else:
    print('Рівняння не виконується')
