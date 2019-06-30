#################### EVAL #####################
#Data Structure String

list_str = '[1,2,3,4,5,6,7]'

print(list_str)
print(type(list_str))

list1 = eval(list_str)
print(list1)
print(type(list1))

#expression evaluation
value = eval('3>2')

print(value)

#Function call
def show(text):
    print(text)


call_str = 'show("Hello There!!!")'

eval(call_str)


#################### EXEC #####################

compile_str = '''
x = input('Number1:')
y = input('Number2:')
if x > y :
    print(x)
else :
    print(y) '''

exec(compile_str)


