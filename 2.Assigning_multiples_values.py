# 1 
# many values to many variables
a , b, c, d = 1, 2, 3.565, 6
print(c)
print(d)

# 2 
# single values to many variables 
# usind identity operator gives true 

a = b = c = d = "xyx"
print(a)
print(b)
print(c)
print(d)

# unpack a collection
# list to difeerent variables
# variables and list members must be same

colours = ["blue", "green", "yellow", "Orange"]
w, x, y, z = colours
print(z)
print(w)
print(y)
print(x)

