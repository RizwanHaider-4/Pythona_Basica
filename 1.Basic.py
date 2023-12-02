name  = str(input("Enter a name       :  "))
age   = str(input("Enter age          :  "))
roll  = int(input("Enter Roll Number  :  "))

print("Is new Student")
print("1 yes")
print("2 No")

choice = int(input())

if choice==1:
    is_new=True
else:
    is_new = False

if(is_new == True):
    print("Name of new Student is        : ", name)  #it will print the details of new student
    print("Age of new Student is         : ", age)
    print("Roll number of new Student is : ", roll)
else:
    print("Existing Student")
    print("Name of existing Student is        : ", name)  # it will print the details of existing Student
    print("Age of existing Student is         : ", age)
    print("Roll number of existing Student is : ", roll)
