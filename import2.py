from import1 import*
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
            