from multiprocessing import Process
from multiprocessing import Lock, Value
import time


def add_500_no_mp(total):
    for i in range(100):
        total += 5
    return total


def add_500_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total.value += 5


def add_500_mp_lock(total,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()


def sub_500_no_mp(total):
    for i in range(100):
        total -= 5
    return total


def sub_500_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total.value -= 5


def sub_500_mp_lock(total,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()


if __name__ == '__main__':
    # print("# No MultiProcessing")
    # total = 500
    # total = add_500_no_mp(total)
    # print(total)
    # total = sub_500_no_mp(total)
    # print(total)

    # print("# With MultiProcessing and Shared Variable")
    # total = Value('i', 500)
    # add_process = Process(target=add_500_mp, args=(total,))
    # sub_process = Process(target=sub_500_mp, args=(total,))
    # add_process.start()
    # sub_process.start()
    # print(total.value)
    total = Value('i', 500)
    try:
        print("# With MultiProcessing and Shared Variable and Locks")
        lock = Lock()
        add_process = Process(target=add_500_mp_lock, args=(total, lock,))
        sub_process = Process(target=sub_500_mp_lock, args=(total, lock))
        add_process.start()
        sub_process.start()
        add_process.join()
        sub_process.join()
        print(total.value)
    except WindowsError as e:
        print(total.value)
        pass
