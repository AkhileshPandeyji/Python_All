
def rang(end, start=0):
    while start < end:
        yield start
        start += 1


for i in rang(start=0,end=23):
    print(i)




