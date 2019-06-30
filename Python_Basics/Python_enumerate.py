######################################## ENUMERATE ############################################
# enumerate returns the enumerate object which is a generator of tuples (x,y)
# x => index
# y => item(list) / values(list) which is passed as an argument in enumerate(list)

list_str = ['MON', 'TUE', 'WED', 'THURS', 'FRI', 'SAT', 'SUN']
list_float = [1.0, 7.9, 0.8, 9.0, 6.7, 8.9, 10.8]

# returns enumerate object
print(enumerate(list_str))


# unpacking of enumerate
for x, y in enumerate(list_str):
    print(x, y)

# it converts the enumerate object into list
list2 = list(enumerate(list_str))
print(list2)

# it converts the enumerate object into dictionary
dict1 = dict(enumerate(list_str))
print(dict1)

# converting the enumerate object to generator and then converting it to list
list3 = list(((x,y) for x,y in enumerate(list_str)))
print(list3)

# converting the enumerate object to list comp
list4 = [(x,y) for x,y in enumerate(list_str)]
print(list4)

#