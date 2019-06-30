######################################## ZIP ############################################
# zip returns the zip object which is a generator of tuples (x,y,z)
# x => values/items of list1
# y => values/items of list2
# z => values/items of list3 which is passed as an argument in zip(list1,list2,list3)
# exhaustion :if any list has shortest elements then zip combines till that last ellemnt of that list

list1 = [1,2,3,4,5,6,7,8,9]
list2 = ['MON', 'TUE', 'WED', 'THURS', 'FRI', 'SAT', 'SUN']
list3 = [1.0, 7.9, 0.8, 9.0, 6.7]


print(zip(list1,list2,list3))

# converting zip object into list
list4 = list(zip(list1,list2,list3))
print(list4)

# converting zip object into dictionary
# dictionary=>(key,value) =>zip(list1,list2)=> key=>list1, value=>list2
# i.e why,two arguments required in dict(zip(list1,list2))
dict1 = dict(zip(list1,list2))
print(dict1)

# converting zip object to list comp
xyz = [(x,y,z) for x,y,z in zip(list1,list2,list3)]
print(xyz)

# converting zip object to generator
xyz = ((x,y,z) for x,y,z in zip(list1,list2,list3))
for i in xyz :
    print(i)
