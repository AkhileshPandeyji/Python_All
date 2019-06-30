#block statements
#1.Functions
#2.Comditional
#3.Iterative


#1.Function : sum(x,y) return the sum of x and y

def sum(x,y):
    print("X:",x)
    print("Y:",y)
    return x+y

print(sum(4,5))
print(sum(4.6,7.4))
print(sum(23+78j,-15-75j))

print(sum("Hello ","World!"))


#Conditionals

def maxM(x,y):
    print("X:",x)
    print("Y:",y)
    if x>y:
        print("1")
        return x
    else:
        print("2")
        return y


print(maxM(4,5))
print(maxM(4.5,4.49))
#can't compare two complex numbers but we can compare their magnitude
#print(maxM(23+4j,34+4j)) wrong error


#iterative

list1 = [1,2,3,4,5,6,7,8,9]
dict1 = {"A":1,
         "B":2,
         "C":3,
         "D":4,
         "E":5
         }
#for
for i in list1:
    print(i)

for i in range(90,100):
    print(i)

for x in dict1:
    print(x)
    print(dict1[x])

#while
i=0
while i<10:
    print(i)
    i=i+1







