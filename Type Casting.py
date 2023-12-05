# implicit type casting -> Automatically by Python Int...
a = 12
b = 12.89
print(type(a))
print(type(b))
c = a+b
print(c)
print(type(c))


# implicit type conversion
b = 9.8
a = 8
c = b+a
print(c)
print(type(a))
print(type(b))
print(type(c))

# Explicit -> Manually by Programmer
# int(), float(), str(), ord(), hex(), oct(),
# tuple(), set(), list(), dict()

a = "1111"
b = "1111"

c = int(a)+int(b)
print(c)