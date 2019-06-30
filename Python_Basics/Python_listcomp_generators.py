# list comprehensions : [expression]
# Are lists that are loaded and retrieved whole once at a time and then executed.
# They contain sequential data that follows some rule.

xyz = [i for i in range(10)]
print(xyz)
print(type(xyz))

# Generators : (expression)
# types:generator variable ,generator function
# Are lists that are loaded whole somewhere and then one item is retrieved at a time in
# a stream and then loaded into the memory.
# They also contain the sequential data that follows some rule.

xyz = (i for i in range(10))
print(xyz)
print(type(xyz))

gen_list = []
for i in xyz:
    print(i)
    gen_list.append(i)

print(gen_list)

# Advance Concepts on generators and list Comprehensions
# Nested list comprehension and generators
# conversion from gen to list
# list comp and gen using expression if

# nested list comp
x = [[i for i in range(5)] for ii in range(5)]
print(x)

# x= [[i for i in range(5)]for ii in range(5)] is equivalent to
x=[]
for ii in range(5):
    x.append([])
    for i in range(5):
        x[ii].append(i)

print(x)

# nested generators

y = ((i for i in range(5))for ii in range(5))
print(y)


for i in y:
    for a in i:
        print(a)

# convert a generator to list comp
z = list(y)
print(z)

# list comp and gen with if expression
r = [5, 7, 10,15, 20, 24, 28, 30, 32, 35]


def divisible_by5(j):
    if j % 5 == 0:
        return True
    else:
        return False


xy = [i for i in r if divisible_by5(i)]
print(xy)

ty = (i for i in r if divisible_by5(i))
print(ty)

for i in ty:
    print(i)


