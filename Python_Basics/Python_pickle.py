import pickle

# Object serialization and Deserialization

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name:'+self.name+': Age:'+str(self.age)

    def show(self):
        print('Name:'+self.name+': Age:'+str(self.age))


student1 = Student('Prashant Varshney',90)
student2 = Student('Abhishek Kajla',80)


filename = open('Student_Record.pickle','ab')

pickle.dump(student1,filename)
pickle.dump(student2,filename)
filename.close()

filename = open('Student_Record.pickle','rb')

student3 = pickle.load(filename)
student4 = pickle.load(filename)

print(student3)
print(student4)

print('\n')

student3.show()
student4.show()




