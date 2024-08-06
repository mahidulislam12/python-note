#class&instance
"""
class Student:
    college_student="abc college"
    name="anoymous"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding the new student in database")
s1=Student('kaean',90)
print(s1.name,s1.marks)
print(s1.college_student,s1.name)
"""
#method 
"""
class Student:
    college_name="amc"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks
s1=Student('k',67)
s1.welcome()
s1.get_marks()
print(s1.college_name)
#print(s1.get_marks)
#print(s1.name,s1.marks)
"""
"""
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is",sum/3)
s1=Student("k",{12,34,34})
s1.get_avg()
print("\n")"""
#static methods
"""
class St:
    @staticmethod
    def college():
        print("abc college")

# Calling the static method on the class itself
St.college()"""
class Student:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    def debit(self,amount):
        self.balance-=amount
        print("welcome the class")
        print(f"welcome:{self.get()}")
    def creadit(self,amount):
        self.balance+=amount
        print("welcome the class")
        print(f"welcome:{self.get()}")
    def get(self):
       return self .balance
s1=Student(122228888999,345553)
s1.debit(1000000000)
s1.creadit(1000990)


