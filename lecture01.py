a=float(input('введите а= '))
b=float(input('введите b= '))
x=float(input('введите угол х='))
from math import sqrt, cos
c=sqrt(a*a+b*b-2*a*b*cos(x))
print('сторона c равна ',c)