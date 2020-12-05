from random import randint
n = int(input('Введіть кількість рядків і кількість стовпців = '))
randomA = [[randint(-100,100) for i in range(n)]for j in range(n)]
print(randomA)
s=1
for i in range(0,n-1):
    for j in range (i+1,n):
        if randomA[i][j]>0:
            s*=randomA[i][j]
        print(s)

