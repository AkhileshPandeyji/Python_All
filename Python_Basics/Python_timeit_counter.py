# timeit module helps us to create a
# counter to execute a task for any number of times.


import timeit
import time

start = time.time()

timeit.timeit('3+4',number=500000)

timeit.timeit('''list_num = [5, 7, 10, 15, 16, 17, 25, 45, 56]
def divby5(num):
    if num % 5 == 0:
        return True
    else:
        return False


list2 = list((i for i in list_num if divby5(i)))
''',number=500000)


print("Time Taken For Execution:",(time.time()-start),'s')