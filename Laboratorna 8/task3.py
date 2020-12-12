n = int(input('Введіть значення n = '))
k=[1, 1]

def eq(n):
    if n>=2:
        for i in range(2, n+1):
            x=k[i-1]+2*k[i-2]
            k.append(x)

        return k.pop(-1)

print(eq(n))
