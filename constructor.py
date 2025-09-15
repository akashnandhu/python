class maths:
    def __init__(self,number1,number2) :
        self.number1=number1
        self.number2=number2
    def __del__(self):
        print("Erase all")
    def sum(self):
        print(" sum of the numbers is :",self.number1+self.number2)
        print("*"*50)
    def sub(self):
        print(" differnce of the numbers is :",self.number1-self.number2)
        print("*"*50)
    def mul(self,number3):
        print("product of three numbers is :",self.number1*self.number2*number3)
        print("*"*50)
cal=maths(5,3)
cal.sum()
cal.mul(4)