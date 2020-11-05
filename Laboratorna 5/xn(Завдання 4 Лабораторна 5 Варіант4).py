n= int(input('Введіть значення n= '))
k=[0,9]

if n>=2:
    for i in range(2, n+1):
        x=2*k[i-1]+3*k[i-2]
        k.append(x)
    print(k.pop(-1))
