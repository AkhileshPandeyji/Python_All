#Exception Handling:try,except,raise,finally,Exception


def divide(x,y):
    return x/y


try:
    print("Exception Handling")
    input1 = int(input("X:"))
    input2 = int(input("Y:"))
    if input2 == 0:
        raise Exception("Divide by Zero")
    else:
        print(divide(input1,input2))
except Exception as e:
    print(str(e))
    pass
finally:
    print("Show Must Continue!!!!!")

