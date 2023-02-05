from time import time

start = time()

def perebor(number):
    index = 1
    result = []
    while index <= number:
        if number % index == 0:
            result.append(index)
        index +=1
    return(result)

def factorize(*numbers):

    args = (numbers)
    res = []
    for x in args:
        res.append(perebor(x))
    res = tuple(res)
    return res


a, b, c, d  = factorize(128, 255, 99999, 10651060)

end = time() - start
print(end)
print(a)
print(b)
print(c)
print(d)
