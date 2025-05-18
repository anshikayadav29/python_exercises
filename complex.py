
import cmath
num = 1+2j
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# Python Program to find the area of triangle

a = 5
b = 6
c = 7

s = (a + b + c) / 2


area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)



# import complex math module
import cmath

a = 1
b = 5
c = 6


d = (b**2) - (4*a*c)


sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
