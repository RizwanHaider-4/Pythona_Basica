# Conditional Statements works on conditional operators
# 4 types
# 1. if statement
# 2. if, else
# 3. if, elif, else:
# 4. Nested If Statement
# if 
#     if
#          if
#          else
#     else
# else


# 2
gen = str(input("Enter Your Gender      :   "))
if ((gen=="Male") or (gen=="male")):
    print("You are",gen)
else:
    print("You are",gen)

handsome = input("Are you Handsome           :  ")
salary   = input("Are you have good salary   :  ")

print("He is Handsome",handsome)
print("He has Good salary",salary)

print("type of handsome data types  :",type(handsome))
print("Type of Salary data types    :",type(salary))

if handsome=='True' and salary=='True':
    print("you can able to marry blue eyes beautiful girl")
elif handsome=='False' and salary=='True':
    print("You can marry Beautiful girl")
elif handsome=='True' and salary=='False':
    print("You can marry")
else:
    print("LoL Have a patience, You can't marry")