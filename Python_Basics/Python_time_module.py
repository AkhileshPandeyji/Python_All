import time

# print(str(time.asctime()))

start = time.time()

y =str(time.asctime())

z = y.split()
# print(z)

# Day Month Date Time[hh:mm:ss] Year [0-4] indexes we can access
print('Day:'+z[0])
print('Date:'+z[1]+' '+z[2]+' '+z[4])
print('Month:'+z[1])
print('Time:'+z[3])

x = z[3].split(':')
# print(x)


print('Hour:'+x[0])
print('Min:'+x[1])
print('Sec:'+x[2])

for i in range(500000):
    pass


end = time.time()

# calculating time of executing script
print("Time Taken to execute this script is in(millisec):",(end-start)*1000,'ms')