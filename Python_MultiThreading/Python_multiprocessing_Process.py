from multiprocessing import Process, current_process
import os
import time


def square(number):
    squared = number*number
    pid = os.getpid()
    time.sleep(3)
    print(f"Process id:{pid}")
    print(f"The Number {number} is squared to {squared} by:",current_process().name)


def sequential(numbers):
    s = time.time()
    print("Sequential:")
    for number in numbers:
        squared = number * number
        pid = os.getpid()
        time.sleep(3)
        print(f"Process id:{pid}")
        print(f"The Number {number} is squared to {squared} by:", current_process().name)
    e = time.time()
    print("Time of Execution:", str(e-s))


if __name__ == '__main__':
    s = time.time()
    processes = []
    numbers = range(10)
    print("MultiProcessing Started", current_process().name)
    for i in range(len(numbers)):
        process = Process(target=square, args=(numbers[i],))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print("MultiProcessing Complete", current_process().name)
    e = time.time()
    print("Time of Execution:", str(e - s))
    sequential(numbers)

