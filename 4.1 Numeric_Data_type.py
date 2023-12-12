# Following are Numeric Data types
 
# 1. integer ---> number without decimals or fractions part 
#                 no size limit for int data type

# 2. float   ---> number with decimals or fraction
#                 represents floating point number

# 3. complex number
# By taking square of any number then it is neither positive number 
# and nor a '0' then such number called as imaginary number or complex.
# Representation      a+bj
# a = real part of the number
# b = imaginary part of the number
# j = Square root value of -1.
# Where a and b may contain integer or floating point numbers.

# Complex number 

# Operation allowed
# add, sub, mul, div
# absolute values abs(z), imag(), real(), z.conjugate()
# power z**n   where n is integer.
# Phase(angle in radians)

# cannot perform
# modu = a % b
# flr = a//b

a = 6+8j
b = 8+9j

ad = a+b
sub = a-b
div = a/b
mul = a*b

exp = a**b

ex2 = (6+8j)*(6+8j)

print("Complex number a is               :   ",a)
print("Complex number b is               :   ",b)
print("Data type of a and b is           :   ",type(b))

print("1. Addition of a and b is         :   ",ad)
print("2. Subtraction of a and b is      :   ",sub)
print("3. Multiplication of a and b is   :   ",mul)
print("4. Division of a and b is         :   ",div)
print("5. Real part of a is              :   ", a.real)
print("6. Imaginary part of a is         :   ", a.imag)
print("7. Absolute value of a is         :   ", abs(a))
print("8. Conjugate of a is              :   ",a.conjugate())
print("9. Power of a is                  :   ",a**4)
print("10. b Power of a is               :   ",a**b)
