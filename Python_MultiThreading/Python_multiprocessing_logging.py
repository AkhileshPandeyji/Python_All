from multiprocessing import Process
from multiprocessing import log_to_stderr, get_logger
import logging


def squares(number):
    sum_ = 0
    for i in range(number):
        sum_ += number*number
    print(sum_)


if __name__ == '__main__':
    numbers = range(10)
    processes = []
    log_to_stderr()
    logger = get_logger()
    logger.setLevel(logging.INFO)

    for number in numbers:
        process = Process(target=squares, args=(number,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
