year=int(input("Enter your birth year :"))
age = 2025-year
print("-"*50)
if age == 18 :
    print("you are still in teenage,but you can vote")
    print("-"*50)
elif age >= 19 :
     print("you can vote")
     print("-"*50)
elif age < 18 :
      print("you are in teenage,you cannot vote")
      print("-"*50)
