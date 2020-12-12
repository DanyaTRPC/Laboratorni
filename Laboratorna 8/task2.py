x1 = float(input('Введіть значення x1= '))
y1 = float(input('Введіть значення y1= '))
x2 = float(input('Введіть значення x2= '))
y2 = float(input('Введіть значення y2= '))
x3 = float(input('Введіть значення x3= '))
y3 = float(input('Введіть значення y3= '))

def dob(v, n):
    for i in range(0, len(v)):
        v[i]*=n

    return v

def dod(m, n):
    s=[]
    for j in range(0, len(m)):
        k=m[j]+n[j]
        s.append(k)

    return s

a=[x1,y1]
b=[x2,y2]
c=[x3,y3]
print(a,b,c)
d=dod(dod(a, dob(b, -3)), dob(c, 2))
print("d =", d)