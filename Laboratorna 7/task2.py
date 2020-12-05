from random import randint
n = int(input('Введіть кількість рядків та стовпців = '))
randomA=[[randint(-100,100) for i in range(n)]for j in range(n)]
print('randomA=',randomA)
a = int(input('Введіть рядок: '))
b = int(input('Введіть стовпець: '))
column=[]
row=[]
if 0<a<=n:
    for j in range(0,n):
        row.append(randomA[a-1][j])
    print(row)
else:
    print("Рядок під таким номером не існує")


if 0 < b <= n:
    for i in range(0, n):
        column.append(randomA[i][b-1])
    print(column)
else:
    print("Стовпець під таким номером не існує")
s = 0
for k in range(n):
    s += column[k] * row[k]


print('s =', s)
