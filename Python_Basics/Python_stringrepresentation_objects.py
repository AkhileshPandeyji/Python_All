# Data hiding in python is done to make
# functions as well as instance variables as private:
# we place __(2x) in front of the variable and function(explicit):
# __name = '' and def __show(self,name):

class Student:
    __name = None
    __age = None

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def __age_classifier(self):
        if self.__age > 18:
            return True
        else:
            return False

    def __str__(self):
        return 'Name:{0} Age:{1}'.format(self.__name,self.__age)

    def __repr__(self):
        return '{}:{}'.format(self.__name,self.__age)

    def ispermitted(self):
        return self.__age_classifier()


student1 = Student('Prashant Varshney',23)
student2 = Student('Abhishek Kajla',24)


print(student1)
print(student2)


def printer(student):
    if student.ispermitted():
        print(student,'is allowed to go to Goa Trip')
    else:
        print(student, 'is not allowed to go to Goa Trip')


printer(student1)
printer(student2)


