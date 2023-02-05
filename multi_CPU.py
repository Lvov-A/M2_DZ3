from time import time
from multiprocessing import Pool
import os

def perebor(number):
    index = 1
    result = []
    while index <= number:
        if number % index == 0:
            result.append(index)
        index +=1
    return(result)

if __name__ == '__main__':
    start = time()
    A = (128, 255, 99999, 10651060)
    res = []
    with Pool(os.cpu_count()) as pool:
        res = pool.map(perebor, A)
    end = time() - start
    print(end)
    for i in res:
        print(i)

