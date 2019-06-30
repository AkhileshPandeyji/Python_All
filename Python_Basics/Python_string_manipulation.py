import os

list1 =['Radha','Krishna','Ganga','Preeti']

for item in list1:
    print('Hello my friend '+item+' !')

str1 = 'I love my parents,subjects,teachers,friends'

list2 = str1.split()

print(' | '.join(list2).replace(',',':'))

filepath = 'C:\\Users\\Akhilesh Kr. Pandey\\PycharmProjects\\Python_Basics'
filename = 'great.py'
print(os.path.join(filepath,filename))

str2 = '{0} loves to eat {1}'
names = ['A','B','C','D']
fruits = ['mangoes','apples','oranges','bananas']

for x,y in zip(names,fruits):
    print(str2.format(x,y))

