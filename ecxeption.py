try:
    x=int(input("enter a number : "))
    y=int(input("Enter a number : "))
    print("answer is :",x/y)
except ZeroDivisionError:
    print("can't divide by 0")
except SyntaxError:
    print("check your input message")
except Exception as w:
    print("an eror accured",w)
