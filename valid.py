fnumber=input("Enter the  first number : ")
lnumber=input("Enter the second number : ")
print("-"*50)
if fnumber.isalpha() or lnumber.isalpha():
    print("Please enter a valid integer")
    print("-" * 50)
else :
    fnumber=int(fnumber)
    lnumber=int(lnumber)
    print("The result is: " + str(fnumber + lnumber))
    print("-" * 50)

