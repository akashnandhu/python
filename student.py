class student:
    def __init__(self):
        self.name=input("Enter a name : ")
        self.english=int(input("Enter a mark of english : "))
        self.maths=int(input("Enter a mark of maths : "))
        self.computer=int(input("Enter a mark of computer : "))
        self.physics=int(input("Enter a mark of physics : "))
        self.malayalam=int(input("Enter a mark of malayalam : "))
    def sum(self):
        total=self.english + self.computer +self.malayalam + self.maths + self.physics
        print("Total mark :",total)
    def avg(self):
        avgg=self.english + self.computer +self.malayalam + self.maths + self.physics
        avgg=avgg/5        
        return avgg
    def display(self):
        print("student name is :",self.name)
        print("mark of english is :",self.english)
        print("mark of maths is :",self.maths)
        print("mark of malayalam is :",self.malayalam)
        print("mark of physics is :",self.physics)
        print("mark of computer is :",self.computer)     
class child(student):
    def grade(self):
        avgg = self.avg()
     
    
        if avgg >90:
            print("your grade is A+")
        elif avgg >80:
            print("your grade is A")
        elif avgg >70:
            print("your grade is B+")
        elif avgg >60:
            print("your grade is B")
        elif avgg >50:
            print("your grade is C+")
        elif avgg >40:
            print("your grade is C")
        elif avgg >30:
            print("your grade is D+")
        
        
x=child()
x.display()
x.avg()
x.grade()
            







