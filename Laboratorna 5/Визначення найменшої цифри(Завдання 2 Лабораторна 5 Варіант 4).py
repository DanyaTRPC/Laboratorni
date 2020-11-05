n= int(input('Введіть значення n= '))
k=[]
if n>0:
    n=str(n)
    a=len(n)
    for i in range(0, a):
        k.append(int(n[i]))
    print(min(k))

else:
    print('Порожня множина')