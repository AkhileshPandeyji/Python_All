from multiprocessing import Pool
import time


def squares(number):
    sum_ = 0
    for i in range(number):
        sum_ += i*i
    return sum_


def squares_mp(numbers):
    s = time.time()
    p = Pool()
    result = p.map(squares, numbers)

    p.close()
    p.join()

    print("Result:", result)
    e = time.time()
    tot = e-s
    print(f"Time of execution: {tot}")


def squares_no_mp(numbers):
    s = time.time()
    square_nums = []
    for number in numbers:
        square_nums.append(squares(number))
    print("Result:", square_nums)
    e = time.time()
    tot = e-s
    print(f"Time of Execution: {tot}")


if __name__ == '__main__':

    numbers = range(10000)
    squares_no_mp(numbers)
    squares_mp(numbers)

