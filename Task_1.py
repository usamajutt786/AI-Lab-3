
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print("Name is ",self.name," Roll no is ",self.rollno)
    def display(self):
        print("Your name is :",self.name)
        print("Your roll no is :",self.rollno)
obj=student("Usama",12)
#obj.display()
