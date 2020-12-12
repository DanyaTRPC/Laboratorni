import math

def sin(x):
  s1=0
  for i in range(1, 6):
    s1+=math.sin(x**i)

  return s1

def cos(y):
  s2=0
  for j in range(1, 6):
    s2+=((-1)**j)*((math.cos(y))**j)

  return s2

def f(t):
  if t>3 :
    sin(t)
    return sin(t)

  else:
    cos(t)
    return cos(t)

a = float(input("Enter a: "))
b = float(input("Enter b: "))
print(f(a), f(b))

u = min(f(a), f(b))
print("min {f(a), f(b)} =", u)