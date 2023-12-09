# Variable in Python
# In python Variable is consider as tag that is pointing to some value.
# in pyhton values are consider as Object.

# if values are same and data types are same then, seprate memory allocation does not requires.
# both the variable tag to same memory location 
# memory location contain values.

# variable name is tag to memory location.
# memory location contains value, which is opposite to C or java etc.

a = 12
b = 12
y = a
print(y)

print(id(y))
print(id(a))
print(id(b))

c = id(a)
d = id(b)
e = id(y)

if c==d==e:
    print("a, b and y is Stored at same memory location  : ",id(a))
    print("values--->objects are same")
    print("Data types are same")
else:
    print("Different values at different memory location")
