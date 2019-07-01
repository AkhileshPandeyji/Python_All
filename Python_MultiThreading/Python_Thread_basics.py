from threading import *
import time

# Without extending thread class


def sayHello(n=5):
    for i in range(n):
        print("Hello:"+str(i+1), "Control:"+current_thread().getName())
        time.sleep(1)


s = time.time()
print("Control at Start:", current_thread().getName())
t1 = Thread(target=sayHello, args=(10,))
t1.start()
t1.join()
t2 = Thread(target=sayHello, args=(10,))
t2.start()
t2.join()
print("Control at End:", current_thread().getName())
e = time.time()
print("Time of Execution:"+str(e-s))

# With Extending Thread Class


class MyThread(Thread):
    def __init__(self, n=10):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            time.sleep(1)
            print("Hello:"+str(i+1), "Control:"+current_thread().getName())


s = time.time()
print("Control at Start:", current_thread().getName())
t3 = MyThread(20)
t3.start()
t3.join()
print("Control at End:", current_thread().getName())
e = time.time()
print("Time of Execution:"+str(e-s))


# With Class but without extending Thread Class

class Target:
    def __init__(self, n):
        self.n = n

    def say_hello(self):
        for i in range(self.n):
            time.sleep(1)
            print("Hello:"+str(i+1), "Control:"+current_thread().getName())


s = time.time()
print("Control at Start:", current_thread().getName())
target1 = Target(20)
t1 = Thread(target=target1.say_hello)
t1.start()
t1.join()
e = time.time()
print("Time of Execution:"+str(e-s))
