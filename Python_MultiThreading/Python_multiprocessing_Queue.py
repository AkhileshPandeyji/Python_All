from multiprocessing import Queue, Process


def squares(numbers, queue):
    for number in numbers:
        queue.put(number**2)


def cubes(numbers, queue):
    for number in numbers:
        queue.put(number**3)


if __name__ == '__main__':
    numbers_list = range(10)
    q = Queue()

    square_process = Process(target=squares, args=(numbers_list, q))
    cube_process = Process(target=cubes, args=(numbers_list, q))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not q.empty():
        print(q.get())



