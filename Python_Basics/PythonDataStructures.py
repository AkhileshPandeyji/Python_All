#List = Arrays
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2.3,4.0,6.7,8.9,9.0]
list3 = [2+4j,5+6j,9+23j,24+90j,12+89j]
list4 = ['a','b','c','d','e']
list5 = ["Apples","Bananas","Pineapples","Oranges","Guavas"]
list6 = list([1,2,3,4,5,6,7,8,9])

print(list1,list2,list3,list4,list5,list6)

#tuples = sets
tuple1 = (1,2,3,4,5,6,7,8,9)
tuple2 = (2.3,4.0,6.7,8.9,9.0)
tuple3 = (2+4j,5+6j,9+23j,24+90j,12+89j)
tuple4 = ('a','b','c','d','e')
tuple5 = ("Apples","Bananas","Pineapples","Oranges","Guavas")
tuple6 = tuple((1,2,3,4,5,6,7,8,9))

print(tuple1,tuple2,tuple3,tuple4,tuple5,tuple6)

#difference : lists are mutable and tuples are immutable

list1[0] = 0
# wrong error tuple[0] = 0
print(list1,tuple1)


#dictionary = map
dict1 = {"A":1,
         "B":2,
         "C":3,
         "D":4,
         "E":5
         }
print(dict1)

print(dict1["A"],dict1["E"])
dict1["A"] = 0;
print(dict1)

dict2 = dict({"A":1,"B":2,"C":3,"D":4,"E":5 })
print(dict2)

#2D-Lists
list2D_1 = [[1,2,3],
            [4,5,6],
            [6,7,8],
            [9,0,0]]

print(list2D_1[2][2])

#Manipulations on Data Structures

list1.append(8)

list1.sort()

list7 = list5.copy()
list7.sort()

list8 = list7.copy()
list8.reverse()

index = list1.index(5)

list1.insert(2,99)
print(list1)

print(list1.count(1))

list1.remove(99)
print(list1)

#deleting dictionaries

del dict2['A']
print(dict2)

del dict2
#print(dict2) //error

