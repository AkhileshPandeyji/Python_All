#Declaring and Defining a class.
#self = this pointer
#__init__ = constructor

class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def show(self):
        print("Name:"+self.name,"Rollno:",self.rollno)


#Creating an object
student1 = student("Prashant Varshney","03620802717")
student2 = student("Abhishek Kajla","00420802717")
student3 = student("Nikhil Lohia","03520802717")
student4 = student("Akhilesh Kumar Pandey","00620802717")

student1.show()
student2.show()
student3.show()
student4.show()

print(student1.rollno)

#inheritance

class enginner(student):
    def showMe(self):
        print("Enginner")


class doctor(student):
    def showMe(self):
        print("Doctor")


Engineer1 = enginner("Anant Rungta","00820802717")
Doctor1 = doctor("Ankesh Krishnan Prasad","01020802717")

Engineer1.show()
Engineer1.showMe()

Doctor1.show()
Doctor1.showMe()
