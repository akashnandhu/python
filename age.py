age=int(input("Enter the age : "))
print("-"*50)
if age >=1 and age <= 12 :
    print("you are child")
    print("-"*50)
elif age >=13 and age <= 19 :
    print("you are in teenage")
    print("-"*50)
elif age >=20 and age <= 40 :
    print("you are adult ")
    print("-"*50)
elif age >=40 and age <= 60 :
    print("you are elder ")
    print("-"*50)
else :
    print("you are senior ")
    print("-"*50)