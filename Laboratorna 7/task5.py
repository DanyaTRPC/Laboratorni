from random import randint
n = int(input('Введіть кількість рядків та стовпців = '))
randomA = [[randint(-10, 100) for i in range(n)]for j in range(n)]
print('randomA =', randomA)

s=1

for i in range(0, n):
    for j in range(0, n):
        if randomA[i][j]>=0 :
            s*=randomA[i][j]
        else:
            s="Рядок містить від'ємні елементи"
            break


    print("row{0} = {1}".format(i, s))
    s=1
